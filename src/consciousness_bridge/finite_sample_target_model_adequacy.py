"""P76 finite-sample rejection certificate for P75 target-model adequacy.

P75 gives population restrictions for a binary latent target observed through
four conditionally independent binary views. P76 propagates one shared sixteen-cell Hoeffding event through those polynomial restrictions. This is not an acceptance test.

The resulting procedure is deliberately one-sided: if a confidence interval
for a necessary P75 constraint excludes zero, the declared model is rejected at
the stated confidence level. Failure to reject is not acceptance of the model,
and this module does not identify any latent state with consciousness.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from math import log, sqrt

import numpy as np

from consciousness_bridge.target_model_adequacy import (
    PAIR_ORDER,
    TRIPLE_ORDER,
    FourViewMoments,
    four_view_moments,
)

Interval = tuple[float, float]
MomentKey = tuple[int, ...]


@dataclass(frozen=True)
class FourViewMomentIntervals:
    """Simultaneous conservative intervals for P75 centered moments."""

    means: tuple[Interval, Interval, Interval, Interval]
    covariances: tuple[Interval, Interval, Interval, Interval, Interval, Interval]
    third_central_moments: tuple[Interval, Interval, Interval, Interval]
    fourth_central_moment: Interval


@dataclass(frozen=True)
class FiniteSampleTargetModelAdequacyCertificate:
    """Finite-sample P76 rejection certificate for the declared P75 model."""

    confidence: float
    sample_size: int
    cell_linf_radius: float
    joint_l1_radius: float
    empirical_moments: FourViewMoments
    moment_intervals: FourViewMomentIntervals
    tetrad_residual_intervals: tuple[Interval, Interval]
    cross_triple_polynomial_intervals: tuple[Interval, Interval, Interval]
    fourth_polynomial_intervals: tuple[Interval, Interval, Interval]
    certified_incompatible: bool
    rejection_witnesses: tuple[str, ...]
    conclusion: str


def categorical_16_cell_linf_radius(sample_size: int, alpha: float) -> float:
    """Return the simultaneous sixteen-cell Hoeffding radius.

    For each cell, the empirical frequency is the mean of IID Bernoulli
    indicators. Hoeffding plus a union bound over sixteen cells gives

        P(max_x |P_hat(x)-P(x)| > eps) <= 32 exp(-2 n eps^2).
    """

    if isinstance(sample_size, bool) or int(sample_size) != sample_size:
        raise ValueError("sample_size must be a positive integer")
    sample_size = int(sample_size)
    if sample_size <= 0:
        raise ValueError("sample_size must be positive")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between zero and one")
    return sqrt(log(32.0 / alpha) / (2.0 * sample_size))


def categorical_16_cell_l1_radius(sample_size: int, alpha: float) -> float:
    """Return the induced conservative L1 radius for the sixteen-cell law."""

    eps = categorical_16_cell_linf_radius(sample_size, alpha)
    return min(2.0, 16.0 * eps)


def sufficient_tetrad_rejection_sample_size(
    minimum_abs_tetrad_residual: float,
    alpha: float,
) -> int:
    """Return a conservative sample size sufficient for tetrad rejection.

    On the P76 event, every pair covariance differs from its empirical value by
    at most ``3 delta_n``. Therefore each empirical tetrad residual differs from
    its population value by at most ``12 delta_n``. A population tetrad margin
    ``tau`` is guaranteed to yield ``|D_hat| > 12 delta_n`` whenever
    ``24 delta_n < tau``.

    With ``delta_n = 16 sqrt(log(32/alpha)/(2n))`` this is ensured by

        n > 73728 log(32/alpha) / tau^2.

    The bound is sufficient and intentionally conservative.
    """

    if not 0.0 < minimum_abs_tetrad_residual <= 2.0:
        raise ValueError("minimum_abs_tetrad_residual must lie in (0, 2]")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between zero and one")
    threshold = (
        73728.0
        * log(32.0 / alpha)
        / minimum_abs_tetrad_residual**2
    )
    return int(np.floor(threshold)) + 1


def _validate_counts(counts: np.ndarray) -> tuple[np.ndarray, int]:
    array = np.asarray(counts, dtype=float)
    if array.shape != (2, 2, 2, 2):
        raise ValueError("counts must have shape (2, 2, 2, 2)")
    if not np.all(np.isfinite(array)):
        raise ValueError("counts must be finite")
    if np.any(array < 0.0):
        raise ValueError("counts must be nonnegative")
    if not np.allclose(array, np.round(array), atol=0.0, rtol=0.0):
        raise ValueError("counts must contain whole observations")
    sample_size = int(array.sum())
    if sample_size <= 0:
        raise ValueError("counts must contain at least one observation")
    return array, sample_size


def _add(first: Interval, second: Interval) -> Interval:
    return first[0] + second[0], first[1] + second[1]


def _negate(interval: Interval) -> Interval:
    return -interval[1], -interval[0]


def _subtract(first: Interval, second: Interval) -> Interval:
    return _add(first, _negate(second))


def _multiply(first: Interval, second: Interval) -> Interval:
    candidates = (
        first[0] * second[0],
        first[0] * second[1],
        first[1] * second[0],
        first[1] * second[1],
    )
    return float(min(candidates)), float(max(candidates))


def _scale(interval: Interval, scalar: float) -> Interval:
    values = scalar * interval[0], scalar * interval[1]
    return float(min(values)), float(max(values))


def _square(interval: Interval) -> Interval:
    lower, upper = interval
    if lower <= 0.0 <= upper:
        return 0.0, float(max(lower * lower, upper * upper))
    values = lower * lower, upper * upper
    return float(min(values)), float(max(values))


def _product(intervals: tuple[Interval, ...]) -> Interval:
    result: Interval = (1.0, 1.0)
    for interval in intervals:
        result = _multiply(result, interval)
    return result


def _raw_moment(probabilities: np.ndarray, axes: MomentKey) -> float:
    values = (-1.0, 1.0)
    total = 0.0
    for indices in product((0, 1), repeat=4):
        monomial = 1.0
        for axis in axes:
            monomial *= values[indices[axis]]
        total += float(probabilities[indices]) * monomial
    return float(total)


def _raw_moment_intervals(
    probabilities: np.ndarray,
    radius: float,
) -> dict[MomentKey, Interval]:
    intervals: dict[MomentKey, Interval] = {}
    for order in range(1, 5):
        for axes in combinations(range(4), order):
            estimate = _raw_moment(probabilities, axes)
            intervals[axes] = (
                float(max(-1.0, estimate - radius)),
                float(min(1.0, estimate + radius)),
            )
    return intervals


def _centered_moment_intervals(
    raw: dict[MomentKey, Interval],
) -> FourViewMomentIntervals:
    means = tuple(raw[(axis,)] for axis in range(4))

    covariance: dict[tuple[int, int], Interval] = {}
    for first, second in PAIR_ORDER:
        covariance[(first, second)] = _subtract(
            raw[(first, second)],
            _multiply(means[first], means[second]),
        )

    thirds: dict[tuple[int, int, int], Interval] = {}
    for triple in TRIPLE_ORDER:
        first, second, third = triple
        interval = raw[triple]
        interval = _subtract(
            interval,
            _multiply(means[first], raw[tuple(sorted((second, third)))]),
        )
        interval = _subtract(
            interval,
            _multiply(means[second], raw[tuple(sorted((first, third)))]),
        )
        interval = _subtract(
            interval,
            _multiply(means[third], raw[tuple(sorted((first, second)))]),
        )
        mean_product = _product(
            (means[first], means[second], means[third])
        )
        thirds[triple] = _add(interval, _scale(mean_product, 2.0))

    fourth = raw[(0, 1, 2, 3)]
    for axis in range(4):
        complement = tuple(index for index in range(4) if index != axis)
        fourth = _subtract(fourth, _multiply(means[axis], raw[complement]))

    for first, second in combinations(range(4), 2):
        complement = tuple(
            index for index in range(4) if index not in (first, second)
        )
        term = _product((means[first], means[second], raw[complement]))
        fourth = _add(fourth, term)

    all_means = _product(tuple(means))
    fourth = _subtract(fourth, _scale(all_means, 3.0))

    return FourViewMomentIntervals(
        means=(means[0], means[1], means[2], means[3]),
        covariances=tuple(covariance[pair] for pair in PAIR_ORDER),
        third_central_moments=tuple(thirds[triple] for triple in TRIPLE_ORDER),
        fourth_central_moment=fourth,
    )


def _covariance_lookup(
    intervals: FourViewMomentIntervals,
) -> dict[tuple[int, int], Interval]:
    return dict(zip(PAIR_ORDER, intervals.covariances, strict=True))


def _third_lookup(
    intervals: FourViewMomentIntervals,
) -> dict[tuple[int, int, int], Interval]:
    return dict(zip(TRIPLE_ORDER, intervals.third_central_moments, strict=True))


def _tetrad_residual_intervals(
    empirical: FourViewMoments,
    joint_l1_radius: float,
) -> tuple[Interval, Interval]:
    covariance = dict(zip(PAIR_ORDER, empirical.covariances, strict=True))
    products = (
        covariance[(0, 1)] * covariance[(2, 3)],
        covariance[(0, 2)] * covariance[(1, 3)],
        covariance[(0, 3)] * covariance[(1, 2)],
    )
    residuals = products[0] - products[1], products[0] - products[2]
    radius = 12.0 * joint_l1_radius
    return tuple(
        (float(residual - radius), float(residual + radius))
        for residual in residuals
    )


def _cross_triple_polynomial_intervals(
    intervals: FourViewMomentIntervals,
) -> tuple[Interval, Interval, Interval]:
    covariance = _covariance_lookup(intervals)
    third = _third_lookup(intervals)
    anchor_square = _square(third[(0, 1, 2)])

    first = _subtract(
        _product((anchor_square, covariance[(0, 3)], covariance[(1, 3)])),
        _product(
            (
                _square(third[(0, 1, 3)]),
                covariance[(0, 2)],
                covariance[(1, 2)],
            )
        ),
    )
    second = _subtract(
        _product((anchor_square, covariance[(0, 3)], covariance[(2, 3)])),
        _product(
            (
                _square(third[(0, 2, 3)]),
                covariance[(0, 1)],
                covariance[(1, 2)],
            )
        ),
    )
    third_residual = _subtract(
        _product((anchor_square, covariance[(1, 3)], covariance[(2, 3)])),
        _product(
            (
                _square(third[(1, 2, 3)]),
                covariance[(0, 1)],
                covariance[(0, 2)],
            )
        ),
    )
    return first, second, third_residual


def _fourth_polynomial_intervals(
    intervals: FourViewMomentIntervals,
) -> tuple[Interval, Interval, Interval]:
    covariance = _covariance_lookup(intervals)
    third = _third_lookup(intervals)

    pairing_products = (
        _multiply(covariance[(0, 1)], covariance[(2, 3)]),
        _multiply(covariance[(0, 2)], covariance[(1, 3)]),
        _multiply(covariance[(0, 3)], covariance[(1, 2)]),
    )
    triples = ((0, 1, 2), (0, 1, 3), (0, 2, 3))

    residuals = []
    for triple, pairing in zip(triples, pairing_products, strict=True):
        first, second, third_axis = triple
        denominator = _product(
            (
                covariance[tuple(sorted((first, second)))],
                covariance[tuple(sorted((first, third_axis)))],
                covariance[tuple(sorted((second, third_axis)))],
            )
        )
        residual = _subtract(
            _multiply(intervals.fourth_central_moment, denominator),
            _multiply(pairing, denominator),
        )
        residual = _subtract(
            residual,
            _multiply(_square(third[triple]), pairing),
        )
        residuals.append(residual)
    return residuals[0], residuals[1], residuals[2]


def _excludes_zero(interval: Interval) -> bool:
    return interval[1] < 0.0 or interval[0] > 0.0


def finite_sample_four_view_adequacy_certificate(
    counts: np.ndarray,
    *,
    alpha: float = 0.05,
) -> FiniteSampleTargetModelAdequacyCertificate:
    """Return a simultaneous finite-sample rejection certificate for P75.

    Every reported interval is derived from one shared sixteen-cell Hoeffding
    event. If any necessary P75 polynomial constraint excludes zero, the
    declared four-view binary latent conditional-independence model is rejected
    with confidence at least ``1-alpha``.

    If no interval excludes zero, the result is inconclusive. It is not an
    acceptance test and does not establish that the latent model is true.
    """

    array, sample_size = _validate_counts(counts)
    cell_radius = categorical_16_cell_linf_radius(sample_size, alpha)
    l1_radius = categorical_16_cell_l1_radius(sample_size, alpha)
    probabilities = array / float(sample_size)

    empirical_moments = four_view_moments(probabilities)
    raw_intervals = _raw_moment_intervals(probabilities, l1_radius)
    moment_intervals = _centered_moment_intervals(raw_intervals)

    tetrads = _tetrad_residual_intervals(empirical_moments, l1_radius)
    cross_triples = _cross_triple_polynomial_intervals(moment_intervals)
    fourth_polynomials = _fourth_polynomial_intervals(moment_intervals)

    witnesses = []
    for index, interval in enumerate(tetrads, start=1):
        if _excludes_zero(interval):
            witnesses.append(f"tetrad_{index}")
    for index, interval in enumerate(cross_triples, start=1):
        if _excludes_zero(interval):
            witnesses.append(f"cross_triple_{index}")
    for index, interval in enumerate(fourth_polynomials, start=1):
        if _excludes_zero(interval):
            witnesses.append(f"fourth_moment_{index}")

    certified_incompatible = bool(witnesses)
    if certified_incompatible:
        conclusion = (
            "declared four-view target-measurement model is rejected by at "
            "least one simultaneous P75 necessary-constraint interval"
        )
    else:
        conclusion = (
            "not rejected by the current finite-sample necessary-constraint "
            "certificate; this is not model acceptance"
        )

    return FiniteSampleTargetModelAdequacyCertificate(
        confidence=1.0 - alpha,
        sample_size=sample_size,
        cell_linf_radius=cell_radius,
        joint_l1_radius=l1_radius,
        empirical_moments=empirical_moments,
        moment_intervals=moment_intervals,
        tetrad_residual_intervals=tetrads,
        cross_triple_polynomial_intervals=cross_triples,
        fourth_polynomial_intervals=fourth_polynomials,
        certified_incompatible=certified_incompatible,
        rejection_witnesses=tuple(witnesses),
        conclusion=conclusion,
    )
