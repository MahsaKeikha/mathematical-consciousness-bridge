"""P74 finite-sample certification for the P73 three-view recovery.

The module propagates one simultaneous finite-sample event for the observed
three-view joint law into conservative confidence bounds for the label-invariant
P73 latent quantities, P72 target-channel stability coefficients, and the full
binary view channels up to the unavoidable common latent-label swap.

This is a statistical uncertainty certificate under the declared P73 model. It
does not validate conditional independence, assign experiential meaning to the
latent state, or identify the latent state with consciousness.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log, sqrt

import numpy as np

from consciousness_bridge.target_channel_identifiability import (
    ThreeViewMoments,
    three_view_moments,
)

Interval = tuple[float, float]
ChannelProbabilityOrbit = tuple[Interval, Interval]


@dataclass(frozen=True)
class FiniteSampleTargetChannelCertificate:
    """Conservative simultaneous P74 certificate from one 2x2x2 count table.

    ``channel_probability_orbit_bounds[j]`` contains confidence intervals for
    the smaller and larger values in the unordered pair

        {P(X_j=+1 | S=-1), P(X_j=+1 | S=+1)}.

    This representation is invariant under the global latent-label swap that is
    observationally unavoidable in P73.
    """

    confidence: float
    sample_size: int
    cell_linf_radius: float
    joint_l1_radius: float
    covariance_radius: float
    third_moment_radius: float
    empirical_moments: ThreeViewMoments
    mean_bounds: tuple[Interval, Interval, Interval]
    covariance_bounds: tuple[Interval, Interval, Interval]
    covariance_abs_bounds: tuple[Interval, Interval, Interval]
    third_moment_bounds: Interval
    third_abs_bounds: Interval
    certified_nondegenerate: bool
    reason: str | None
    q_bounds: Interval | None
    latent_abs_mean_bounds: Interval | None
    latent_variance_bounds: Interval | None
    prevalence_orbit_intervals: tuple[Interval, Interval] | None
    loading_times_latent_mean_bounds: tuple[Interval, Interval, Interval] | None
    channel_offset_bounds: tuple[Interval, Interval, Interval] | None
    stability_bounds: tuple[Interval, Interval, Interval] | None
    channel_probability_orbit_bounds: (
        tuple[ChannelProbabilityOrbit, ChannelProbabilityOrbit, ChannelProbabilityOrbit]
        | None
    )
    joint_stability_lower_bound: float | None


def categorical_cell_linf_radius(sample_size: int, alpha: float) -> float:
    """Return the simultaneous eight-cell Hoeffding radius.

    A union bound over the eight binary three-view cells gives

        P(max_x |P_hat(x)-P(x)| > eps) <= 16 exp(-2 n eps^2).

    The returned radius chooses the right-hand side equal to ``alpha``.
    """

    if isinstance(sample_size, bool) or int(sample_size) != sample_size:
        raise ValueError("sample_size must be a positive integer")
    sample_size = int(sample_size)
    if sample_size <= 0:
        raise ValueError("sample_size must be positive")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between zero and one")
    return sqrt(log(16.0 / alpha) / (2.0 * sample_size))


def categorical_joint_l1_radius(sample_size: int, alpha: float) -> float:
    """Return the induced conservative L1 radius for the eight-cell law."""

    eps = categorical_cell_linf_radius(sample_size, alpha)
    return min(2.0, 8.0 * eps)


def sufficient_nondegeneracy_sample_size(
    minimum_abs_covariance: float,
    alpha: float,
) -> int:
    """Return a conservative sufficient sample size for a positive covariance gate.

    If the true minimum absolute pair covariance is ``c_min`` and
    ``6 delta_n < c_min``, then every empirical absolute covariance exceeds the
    P74 covariance radius ``3 delta_n``. With the uncapped
    ``delta_n = 8 sqrt(log(16/alpha)/(2n))``, this is guaranteed whenever

        n > 1152 log(16/alpha) / c_min^2.

    This is a sufficient design bound, not an optimal sample-complexity claim.
    """

    if not 0.0 < minimum_abs_covariance <= 1.0:
        raise ValueError("minimum_abs_covariance must lie in (0, 1]")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between zero and one")
    threshold = 1152.0 * log(16.0 / alpha) / minimum_abs_covariance**2
    return int(np.floor(threshold)) + 1


def _validate_counts(counts: np.ndarray) -> tuple[np.ndarray, int]:
    array = np.asarray(counts, dtype=float)
    if array.shape != (2, 2, 2):
        raise ValueError("counts must have shape (2, 2, 2)")
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


def _signed_interval(
    estimate: float,
    radius: float,
    lower_cap: float | None = None,
    upper_cap: float | None = None,
) -> Interval:
    lower = float(estimate) - radius
    upper = float(estimate) + radius
    if lower_cap is not None:
        lower = max(lower, lower_cap)
    if upper_cap is not None:
        upper = min(upper, upper_cap)
    return float(lower), float(upper)


def _absolute_interval(estimate: float, radius: float, cap: float | None) -> Interval:
    lower = max(abs(float(estimate)) - radius, 0.0)
    upper = abs(float(estimate)) + radius
    if cap is not None:
        upper = min(upper, cap)
    return float(lower), float(upper)


def _ratio_interval(numerator: Interval, denominator: Interval) -> Interval:
    """Return the exact interval hull of x/y for endpoint intervals away from zero."""

    n_low, n_high = numerator
    d_low, d_high = denominator
    if d_low <= 0.0 <= d_high:
        raise ValueError("denominator interval must exclude zero")
    candidates = (
        n_low / d_low,
        n_low / d_high,
        n_high / d_low,
        n_high / d_high,
    )
    return float(min(candidates)), float(max(candidates))


def _scale_interval(interval: Interval, scalar: float) -> Interval:
    values = scalar * interval[0], scalar * interval[1]
    return float(min(values)), float(max(values))


def _sum_intervals(first: Interval, second: Interval) -> Interval:
    return float(first[0] + second[0]), float(first[1] + second[1])


def _clip_interval(interval: Interval, lower: float, upper: float) -> Interval:
    return float(max(interval[0], lower)), float(min(interval[1], upper))


def _stability_interval(
    numerator_a: Interval,
    numerator_b: Interval,
    denominator_covariance: Interval,
    latent_variance: Interval,
) -> Interval:
    a_low, a_high = numerator_a
    b_low, b_high = numerator_b
    d_low, d_high = denominator_covariance
    v_low, v_high = latent_variance

    lower = sqrt(max(a_low * b_low / (v_high * d_high), 0.0))
    upper = sqrt(max(a_high * b_high / (v_low * d_low), 0.0))
    return float(min(max(lower, 0.0), 1.0)), float(min(max(upper, 0.0), 1.0))


def _channel_probability_orbit(
    offset: Interval,
    stability: Interval,
) -> ChannelProbabilityOrbit:
    """Bound the unordered latent-conditioned +1 probabilities of one view.

    For a binary view, the two latent-conditioned means are ``a-b`` and
    ``a+b``. Their unordered values are ``a-gamma`` and ``a+gamma`` with
    ``gamma=|b|``. The corresponding +1 probabilities are divided by two after
    adding one. Box propagation is conservative because offset and stability
    are generally statistically dependent.
    """

    a_low, a_high = offset
    g_low, g_high = stability
    smaller = _clip_interval(
        (0.5 * (1.0 + a_low - g_high), 0.5 * (1.0 + a_high - g_low)),
        0.0,
        1.0,
    )
    larger = _clip_interval(
        (0.5 * (1.0 + a_low + g_low), 0.5 * (1.0 + a_high + g_high)),
        0.0,
        1.0,
    )
    return smaller, larger


def _failed_certificate(
    *,
    alpha: float,
    sample_size: int,
    cell_radius: float,
    l1_radius: float,
    covariance_radius: float,
    third_radius: float,
    moments: ThreeViewMoments,
    mean_bounds: tuple[Interval, Interval, Interval],
    signed_covariance_bounds: tuple[Interval, Interval, Interval],
    covariance_abs_bounds: tuple[Interval, Interval, Interval],
    signed_third_bounds: Interval,
    third_abs_bounds: Interval,
    reason: str,
) -> FiniteSampleTargetChannelCertificate:
    return FiniteSampleTargetChannelCertificate(
        confidence=1.0 - alpha,
        sample_size=sample_size,
        cell_linf_radius=cell_radius,
        joint_l1_radius=l1_radius,
        covariance_radius=covariance_radius,
        third_moment_radius=third_radius,
        empirical_moments=moments,
        mean_bounds=mean_bounds,
        covariance_bounds=signed_covariance_bounds,
        covariance_abs_bounds=covariance_abs_bounds,
        third_moment_bounds=signed_third_bounds,
        third_abs_bounds=third_abs_bounds,
        certified_nondegenerate=False,
        reason=reason,
        q_bounds=None,
        latent_abs_mean_bounds=None,
        latent_variance_bounds=None,
        prevalence_orbit_intervals=None,
        loading_times_latent_mean_bounds=None,
        channel_offset_bounds=None,
        stability_bounds=None,
        channel_probability_orbit_bounds=None,
        joint_stability_lower_bound=None,
    )


def finite_sample_three_view_certificate(
    counts: np.ndarray,
    *,
    alpha: float = 0.05,
) -> FiniteSampleTargetChannelCertificate:
    """Propagate multinomial sampling uncertainty through the P73 inversion.

    The guarantee is simultaneous on the eight-cell Hoeffding event and is
    conditional on the P73 three-view binary latent model. A failed
    nondegeneracy gate means that finite data do not certify safe inversion. It
    does not prove that the population model is degenerate.
    """

    array, sample_size = _validate_counts(counts)
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between zero and one")

    empirical_joint = array / sample_size
    moments = three_view_moments(empirical_joint)

    cell_radius = categorical_cell_linf_radius(sample_size, alpha)
    l1_radius = categorical_joint_l1_radius(sample_size, alpha)
    covariance_radius = 3.0 * l1_radius
    third_radius = 13.0 * l1_radius

    mean_bounds = tuple(
        _signed_interval(value, l1_radius, -1.0, 1.0) for value in moments.means
    )
    signed_covariance_bounds = tuple(
        _signed_interval(value, covariance_radius, -1.0, 1.0)
        for value in moments.covariances
    )
    covariance_abs_bounds = tuple(
        _absolute_interval(value, covariance_radius, 1.0)
        for value in moments.covariances
    )
    signed_third_bounds = _signed_interval(
        moments.third_central_moment,
        third_radius,
    )
    third_abs_bounds = _absolute_interval(
        moments.third_central_moment,
        third_radius,
        None,
    )

    if any(lower <= 0.0 for lower, _ in covariance_abs_bounds):
        return _failed_certificate(
            alpha=alpha,
            sample_size=sample_size,
            cell_radius=cell_radius,
            l1_radius=l1_radius,
            covariance_radius=covariance_radius,
            third_radius=third_radius,
            moments=moments,
            mean_bounds=mean_bounds,
            signed_covariance_bounds=signed_covariance_bounds,
            covariance_abs_bounds=covariance_abs_bounds,
            signed_third_bounds=signed_third_bounds,
            third_abs_bounds=third_abs_bounds,
            reason=(
                "pair-covariance confidence interval reaches zero; "
                "P73 nondegeneracy is not certified"
            ),
        )

    c12, c13, c23 = moments.covariances
    if c12 * c13 * c23 <= 0.0:
        return _failed_certificate(
            alpha=alpha,
            sample_size=sample_size,
            cell_radius=cell_radius,
            l1_radius=l1_radius,
            covariance_radius=covariance_radius,
            third_radius=third_radius,
            moments=moments,
            mean_bounds=mean_bounds,
            signed_covariance_bounds=signed_covariance_bounds,
            covariance_abs_bounds=covariance_abs_bounds,
            signed_third_bounds=signed_third_bounds,
            third_abs_bounds=third_abs_bounds,
            reason=(
                "pair-covariance sign pattern is incompatible with the "
                "nondegenerate P73 model on the simultaneous confidence event"
            ),
        )

    (l12, u12), (l13, u13), (l23, u23) = covariance_abs_bounds
    lm, um = third_abs_bounds

    q_low = lm**2 / (u12 * u13 * u23)
    q_high = um**2 / (l12 * l13 * l23)
    q_bounds = float(q_low), float(q_high)

    abs_m_low = sqrt(q_low / (q_low + 4.0))
    abs_m_high = sqrt(q_high / (q_high + 4.0))
    latent_abs_mean_bounds = float(abs_m_low), float(abs_m_high)

    variance_low = 4.0 / (q_high + 4.0)
    variance_high = 4.0 / (q_low + 4.0)
    latent_variance_bounds = float(variance_low), float(variance_high)

    prevalence_low_orientation = (
        0.5 * (1.0 - abs_m_high),
        0.5 * (1.0 - abs_m_low),
    )
    prevalence_high_orientation = (
        0.5 * (1.0 + abs_m_low),
        0.5 * (1.0 + abs_m_high),
    )

    gamma_1 = _stability_interval(
        covariance_abs_bounds[0],
        covariance_abs_bounds[1],
        covariance_abs_bounds[2],
        latent_variance_bounds,
    )
    gamma_2 = _stability_interval(
        covariance_abs_bounds[0],
        covariance_abs_bounds[2],
        covariance_abs_bounds[1],
        latent_variance_bounds,
    )
    gamma_3 = _stability_interval(
        covariance_abs_bounds[1],
        covariance_abs_bounds[2],
        covariance_abs_bounds[0],
        latent_variance_bounds,
    )
    stability_bounds = gamma_1, gamma_2, gamma_3

    # P73 gives M_123 / C_kl = -2 m b_j for the complementary pair (k,l).
    # Therefore b_j m = -M_123 / (2 C_kl). This product and the channel offset
    # a_j = mu_j - b_j m are invariant under the global latent-label swap.
    complement_covariance_bounds = (
        signed_covariance_bounds[2],
        signed_covariance_bounds[1],
        signed_covariance_bounds[0],
    )
    loading_times_latent_mean_bounds = tuple(
        _scale_interval(
            _ratio_interval(signed_third_bounds, complement_covariance),
            -0.5,
        )
        for complement_covariance in complement_covariance_bounds
    )
    channel_offset_bounds = tuple(
        _clip_interval(
            _sum_intervals(mean_interval, _scale_interval(product_interval, -1.0)),
            -1.0,
            1.0,
        )
        for mean_interval, product_interval in zip(
            mean_bounds,
            loading_times_latent_mean_bounds,
            strict=True,
        )
    )
    channel_probability_orbit_bounds = tuple(
        _channel_probability_orbit(offset, stability)
        for offset, stability in zip(
            channel_offset_bounds,
            stability_bounds,
            strict=True,
        )
    )

    return FiniteSampleTargetChannelCertificate(
        confidence=1.0 - alpha,
        sample_size=sample_size,
        cell_linf_radius=cell_radius,
        joint_l1_radius=l1_radius,
        covariance_radius=covariance_radius,
        third_moment_radius=third_radius,
        empirical_moments=moments,
        mean_bounds=mean_bounds,
        covariance_bounds=signed_covariance_bounds,
        covariance_abs_bounds=covariance_abs_bounds,
        third_moment_bounds=signed_third_bounds,
        third_abs_bounds=third_abs_bounds,
        certified_nondegenerate=True,
        reason=None,
        q_bounds=q_bounds,
        latent_abs_mean_bounds=latent_abs_mean_bounds,
        latent_variance_bounds=latent_variance_bounds,
        prevalence_orbit_intervals=(
            (float(prevalence_low_orientation[0]), float(prevalence_low_orientation[1])),
            (
                float(prevalence_high_orientation[0]),
                float(prevalence_high_orientation[1]),
            ),
        ),
        loading_times_latent_mean_bounds=loading_times_latent_mean_bounds,
        channel_offset_bounds=channel_offset_bounds,
        stability_bounds=stability_bounds,
        channel_probability_orbit_bounds=channel_probability_orbit_bounds,
        joint_stability_lower_bound=float(max(interval[0] for interval in stability_bounds)),
    )