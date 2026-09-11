"""P74 finite-sample certification for the P73 three-view recovery.

The module propagates one simultaneous finite-sample event for the observed
three-view joint law into conservative confidence bounds for the label-invariant
P73 latent imbalance and P72 target-channel stability coefficients.

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


@dataclass(frozen=True)
class FiniteSampleTargetChannelCertificate:
    """Conservative simultaneous P74 certificate from one 2x2x2 count table."""

    confidence: float
    sample_size: int
    cell_linf_radius: float
    joint_l1_radius: float
    covariance_radius: float
    third_moment_radius: float
    empirical_moments: ThreeViewMoments
    covariance_abs_bounds: tuple[Interval, Interval, Interval]
    third_abs_bounds: Interval
    certified_nondegenerate: bool
    reason: str | None
    q_bounds: Interval | None
    latent_abs_mean_bounds: Interval | None
    latent_variance_bounds: Interval | None
    prevalence_orbit_intervals: tuple[Interval, Interval] | None
    stability_bounds: tuple[Interval, Interval, Interval] | None
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


def _absolute_interval(estimate: float, radius: float, cap: float | None) -> Interval:
    lower = max(abs(float(estimate)) - radius, 0.0)
    upper = abs(float(estimate)) + radius
    if cap is not None:
        upper = min(upper, cap)
    return float(lower), float(upper)


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

    covariance_bounds = tuple(
        _absolute_interval(value, covariance_radius, 1.0)
        for value in moments.covariances
    )
    third_bounds = _absolute_interval(
        moments.third_central_moment,
        third_radius,
        None,
    )

    if any(lower <= 0.0 for lower, _ in covariance_bounds):
        return FiniteSampleTargetChannelCertificate(
            confidence=1.0 - alpha,
            sample_size=sample_size,
            cell_linf_radius=cell_radius,
            joint_l1_radius=l1_radius,
            covariance_radius=covariance_radius,
            third_moment_radius=third_radius,
            empirical_moments=moments,
            covariance_abs_bounds=covariance_bounds,
            third_abs_bounds=third_bounds,
            certified_nondegenerate=False,
            reason=(
                "pair-covariance confidence interval reaches zero; "
                "P73 nondegeneracy is not certified"
            ),
            q_bounds=None,
            latent_abs_mean_bounds=None,
            latent_variance_bounds=None,
            prevalence_orbit_intervals=None,
            stability_bounds=None,
            joint_stability_lower_bound=None,
        )

    c12, c13, c23 = moments.covariances
    if c12 * c13 * c23 <= 0.0:
        return FiniteSampleTargetChannelCertificate(
            confidence=1.0 - alpha,
            sample_size=sample_size,
            cell_linf_radius=cell_radius,
            joint_l1_radius=l1_radius,
            covariance_radius=covariance_radius,
            third_moment_radius=third_radius,
            empirical_moments=moments,
            covariance_abs_bounds=covariance_bounds,
            third_abs_bounds=third_bounds,
            certified_nondegenerate=False,
            reason=(
                "pair-covariance sign pattern is incompatible with the "
                "nondegenerate P73 model on the simultaneous confidence event"
            ),
            q_bounds=None,
            latent_abs_mean_bounds=None,
            latent_variance_bounds=None,
            prevalence_orbit_intervals=None,
            stability_bounds=None,
            joint_stability_lower_bound=None,
        )

    (l12, u12), (l13, u13), (l23, u23) = covariance_bounds
    lm, um = third_bounds

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
        covariance_bounds[0],
        covariance_bounds[1],
        covariance_bounds[2],
        latent_variance_bounds,
    )
    gamma_2 = _stability_interval(
        covariance_bounds[0],
        covariance_bounds[2],
        covariance_bounds[1],
        latent_variance_bounds,
    )
    gamma_3 = _stability_interval(
        covariance_bounds[1],
        covariance_bounds[2],
        covariance_bounds[0],
        latent_variance_bounds,
    )
    stability_bounds = gamma_1, gamma_2, gamma_3

    return FiniteSampleTargetChannelCertificate(
        confidence=1.0 - alpha,
        sample_size=sample_size,
        cell_linf_radius=cell_radius,
        joint_l1_radius=l1_radius,
        covariance_radius=covariance_radius,
        third_moment_radius=third_radius,
        empirical_moments=moments,
        covariance_abs_bounds=covariance_bounds,
        third_abs_bounds=third_bounds,
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
        stability_bounds=stability_bounds,
        joint_stability_lower_bound=float(max(interval[0] for interval in stability_bounds)),
    )
