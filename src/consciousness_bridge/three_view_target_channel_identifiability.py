"""Proposition 73: three-view target-channel identifiability.

P72 quantifies how a declared target-measurement channel attenuates a bridge
witness. P73 asks when the channel stability can itself be identified without
observing the latent binary target directly.

Let Z in {-1,+1} be a latent target and let three observed target views satisfy

    Y_i = Z N_i,

where the binary noises N_i are mutually independent and independent of Z.
Write

    r_i = E[N_i],
    gamma_i = |r_i|,
    m_ij = E[Y_i Y_j].

Then m_ij = r_i r_j. For three nondegenerate views this identifies the
stability magnitudes gamma_i from pairwise moments, while the vector of signed
reliabilities is identified only up to one global sign. Two heterogeneous
views are insufficient because one product m_12 does not identify two factors.

The module also gives simultaneous finite-sample intervals for gamma_i using
Hoeffding bounds on the three empirical pairwise moments.

This is a target-measurement identifiability result under a declared latent
measurement model. It does not establish that the latent target is
consciousness or that the conditional-independence assumptions hold in data.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from math import isfinite, log, sqrt


@dataclass(frozen=True)
class ThreeViewStabilityIdentification:
    """Exact stability magnitudes identified from three pairwise moments."""

    moment_12: float
    moment_13: float
    moment_23: float
    stability_1: float
    stability_2: float
    stability_3: float
    global_sign_ambiguity: bool = True


@dataclass(frozen=True)
class StabilityInterval:
    """Closed confidence interval for one channel stability magnitude."""

    lower: float
    upper: float


@dataclass(frozen=True)
class ThreeViewStabilityCertificate:
    """Simultaneous finite-sample P73 stability certificate."""

    confidence_level: float
    sample_size: int
    moment_radius: float
    empirical_moment_12: float
    empirical_moment_13: float
    empirical_moment_23: float
    stability_1: StabilityInterval
    stability_2: StabilityInterval
    stability_3: StabilityInterval


def identify_three_view_stabilities(
    moment_12: float,
    moment_13: float,
    moment_23: float,
) -> ThreeViewStabilityIdentification:
    """Identify three binary symmetric-channel stability magnitudes.

    Under the P73 model,

        m_12 = r_1 r_2,
        m_13 = r_1 r_3,
        m_23 = r_2 r_3,

    with nonzero ``r_i``. Hence

        |r_1| = sqrt(m_12 m_13 / m_23),

    and cyclic permutations identify the remaining stability magnitudes.

    The moments must be compatible with nonzero binary reliabilities. The
    signed vector ``(r_1, r_2, r_3)`` remains ambiguous under one simultaneous
    global sign flip, but ``(|r_1|, |r_2|, |r_3|)`` is unique.
    """
    moments = (
        _moment(moment_12, "moment_12"),
        _moment(moment_13, "moment_13"),
        _moment(moment_23, "moment_23"),
    )
    if any(value == 0.0 for value in moments):
        raise ValueError("P73 exact identification requires nonzero pairwise moments")
    if moment_12 * moment_13 * moment_23 <= 0.0:
        raise ValueError("pairwise moments are incompatible with the P73 three-view model")

    squared = (
        moment_12 * moment_13 / moment_23,
        moment_12 * moment_23 / moment_13,
        moment_13 * moment_23 / moment_12,
    )
    tolerance = 1e-12
    if any(value <= 0.0 or value > 1.0 + tolerance for value in squared):
        raise ValueError("pairwise moments imply invalid binary channel stability")

    stability = tuple(min(1.0, sqrt(value)) for value in squared)
    return ThreeViewStabilityIdentification(
        moment_12=moment_12,
        moment_13=moment_13,
        moment_23=moment_23,
        stability_1=stability[0],
        stability_2=stability[1],
        stability_3=stability[2],
    )


def better_than_chance_error_rates(
    moment_12: float,
    moment_13: float,
    moment_23: float,
) -> tuple[float, float, float]:
    """Return oriented binary error rates after declaring ``r_i > 0``.

    Without an orientation condition, the three-view model identifies channel
    stability magnitudes but not whether all observers are aligned with or
    globally inverted relative to the latent labels. Declaring every view
    better than chance selects ``r_i = gamma_i > 0`` and therefore

        eta_i = (1 - gamma_i) / 2.
    """
    identified = identify_three_view_stabilities(moment_12, moment_13, moment_23)
    return tuple(
        (1.0 - gamma) / 2.0
        for gamma in (
            identified.stability_1,
            identified.stability_2,
            identified.stability_3,
        )
    )


def two_view_compatible_stabilities(
    moment_12: float,
    stability_1: float,
) -> tuple[float, float]:
    """Construct one member of the two-view non-identifiability family.

    With only two heterogeneous views, the observable constraint is

        |m_12| = gamma_1 gamma_2.

    Any admissible ``gamma_1`` produces a compatible
    ``gamma_2 = |m_12| / gamma_1``. A continuum of choices exists whenever
    ``0 < |m_12| < 1``.
    """
    moment = abs(_moment(moment_12, "moment_12"))
    if moment <= 0.0:
        raise ValueError("moment_12 must be nonzero for this construction")
    gamma_1 = _unit_interval(stability_1, "stability_1", positive=True)
    gamma_2 = moment / gamma_1
    if gamma_2 > 1.0 + 1e-12:
        raise ValueError("chosen stability_1 is incompatible with moment_12")
    return gamma_1, min(1.0, gamma_2)


def empirical_pairwise_moments(
    observations: Sequence[tuple[int, int, int]],
) -> tuple[float, float, float]:
    """Compute empirical pairwise sign moments from three repeated views."""
    if not observations:
        raise ValueError("observations must be nonempty")
    sum_12 = 0
    sum_13 = 0
    sum_23 = 0
    for row in observations:
        if len(row) != 3:
            raise ValueError("each observation must contain exactly three views")
        y_1, y_2, y_3 = row
        for value in row:
            if value not in (-1, 1):
                raise ValueError("P73 binary observations must be encoded as -1 or +1")
        sum_12 += y_1 * y_2
        sum_13 += y_1 * y_3
        sum_23 += y_2 * y_3
    n = len(observations)
    return sum_12 / n, sum_13 / n, sum_23 / n


def finite_three_view_stability_certificate(
    observations: Sequence[tuple[int, int, int]],
    alpha: float,
) -> ThreeViewStabilityCertificate:
    """Return simultaneous finite-sample intervals for the three stabilities.

    For each pair ``ij``, ``Y_i Y_j`` lies in ``[-1,1]``. Hoeffding's
    inequality plus a union bound across the three pair moments gives

        |m_hat_ij - m_ij| <= eps

    simultaneously with probability at least ``1-alpha``, where

        eps = sqrt(2 log(6/alpha) / n).

    Since ``||m_hat|-|m|| <= |m_hat-m|``, the same event bounds each absolute
    moment ``a_ij = |m_ij|``. Under the P73 model,

        gamma_1^2 = a_12 a_13 / a_23,

    and cyclic permutations yield conservative interval propagation. If a
    denominator cannot be separated from zero, the corresponding upper bound
    is left at the trivial value one.
    """
    _open_probability(alpha, "alpha")
    empirical = empirical_pairwise_moments(observations)
    n = len(observations)
    radius = sqrt(2.0 * log(6.0 / alpha) / n)

    absolute_intervals = tuple(
        (
            max(0.0, abs(moment) - radius),
            min(1.0, abs(moment) + radius),
        )
        for moment in empirical
    )
    interval_12, interval_13, interval_23 = absolute_intervals

    stability_1 = _ratio_sqrt_interval(interval_12, interval_13, interval_23)
    stability_2 = _ratio_sqrt_interval(interval_12, interval_23, interval_13)
    stability_3 = _ratio_sqrt_interval(interval_13, interval_23, interval_12)

    return ThreeViewStabilityCertificate(
        confidence_level=1.0 - alpha,
        sample_size=n,
        moment_radius=radius,
        empirical_moment_12=empirical[0],
        empirical_moment_13=empirical[1],
        empirical_moment_23=empirical[2],
        stability_1=stability_1,
        stability_2=stability_2,
        stability_3=stability_3,
    )


def _ratio_sqrt_interval(
    numerator_a: tuple[float, float],
    numerator_b: tuple[float, float],
    denominator: tuple[float, float],
) -> StabilityInterval:
    low_a, high_a = numerator_a
    low_b, high_b = numerator_b
    low_d, high_d = denominator

    if high_d <= 0.0:
        lower = 0.0
    else:
        lower = sqrt(max(0.0, low_a * low_b / high_d))

    if low_d <= 0.0:
        upper = 1.0
    else:
        upper = min(1.0, sqrt(max(0.0, high_a * high_b / low_d)))

    return StabilityInterval(lower=min(1.0, lower), upper=max(lower, upper))


def _moment(value: float, name: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f"{name} must be numeric")
    value = float(value)
    if not isfinite(value):
        raise ValueError(f"{name} must be finite")
    if value < -1.0 or value > 1.0:
        raise ValueError(f"{name} must lie in [-1, 1]")
    return value


def _unit_interval(value: float, name: str, *, positive: bool = False) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f"{name} must be numeric")
    value = float(value)
    if not isfinite(value):
        raise ValueError(f"{name} must be finite")
    lower_ok = value > 0.0 if positive else value >= 0.0
    if not lower_ok or value > 1.0:
        bound = "(0, 1]" if positive else "[0, 1]"
        raise ValueError(f"{name} must lie in {bound}")
    return value


def _open_probability(value: float, name: str) -> float:
    value = _unit_interval(value, name)
    if value <= 0.0 or value >= 1.0:
        raise ValueError(f"{name} must lie strictly between zero and one")
    return value
