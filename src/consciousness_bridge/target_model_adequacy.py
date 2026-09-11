"""P75 adequacy diagnostics for binary multi-view latent target models.

P73 identifies a nondegenerate binary latent target from three conditionally
independent binary views. P75 separates that population identifiability result
from model adequacy. Three binary views are generically just-identified, while
a fourth view creates observable overidentifying restrictions.

The module does not identify a latent state with consciousness and does not
validate conditional independence from three-view fit alone.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product

import numpy as np

from consciousness_bridge.target_channel_identifiability import (
    recover_three_view_binary_model,
)

PAIR_ORDER = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
TRIPLE_ORDER = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))


@dataclass(frozen=True)
class FourViewMoments:
    """Observable centered moments for four binary views encoded as {-1,+1}."""

    means: tuple[float, float, float, float]
    covariances: tuple[float, float, float, float, float, float]
    third_central_moments: tuple[float, float, float, float]
    fourth_central_moment: float


@dataclass(frozen=True)
class FourViewAdequacyDiagnostics:
    """Population P75 diagnostics for the four-view latent target model."""

    observed_dimension: int
    model_parameter_dimension: int
    generic_overidentifying_dimension: int
    moments: FourViewMoments
    tetrad_products: tuple[float, float, float]
    tetrad_residuals: tuple[float, float]
    triple_q_values: tuple[float, float, float, float] | None
    triple_q_spread: float | None
    fourth_consistency_residuals: tuple[float, float, float] | None
    reconstruction_error: float | None
    compatible_with_declared_model: bool
    reason: str | None


def binary_observed_simplex_dimension(number_of_views: int) -> int:
    """Return the dimension of a full binary observed joint distribution."""

    if isinstance(number_of_views, bool) or int(number_of_views) != number_of_views:
        raise ValueError("number_of_views must be a positive integer")
    number_of_views = int(number_of_views)
    if number_of_views <= 0:
        raise ValueError("number_of_views must be positive")
    return 2**number_of_views - 1


def binary_latent_independent_model_parameter_dimension(number_of_views: int) -> int:
    """Return 1+2k for one binary latent state and k binary view channels."""

    if isinstance(number_of_views, bool) or int(number_of_views) != number_of_views:
        raise ValueError("number_of_views must be a positive integer")
    number_of_views = int(number_of_views)
    if number_of_views <= 0:
        raise ValueError("number_of_views must be positive")
    return 1 + 2 * number_of_views


def generic_overidentifying_dimension(number_of_views: int) -> int:
    """Return observed dimension minus model parameter dimension, floored at zero."""

    return max(
        0,
        binary_observed_simplex_dimension(number_of_views)
        - binary_latent_independent_model_parameter_dimension(number_of_views),
    )


def _validate_joint(joint: np.ndarray, number_of_views: int) -> np.ndarray:
    expected_shape = (2,) * number_of_views
    probs = np.asarray(joint, dtype=float)
    if probs.shape != expected_shape:
        raise ValueError(f"expected probability array with shape {expected_shape}")
    if not np.all(np.isfinite(probs)):
        raise ValueError("probabilities must be finite")
    if np.any(probs < 0.0):
        raise ValueError("probabilities must be nonnegative")
    total = float(probs.sum())
    if total <= 0.0:
        raise ValueError("probabilities must have positive total mass")
    return probs / total


def four_view_joint_distribution_from_model(
    prevalence_plus: float,
    conditional_plus: tuple[tuple[float, float], ...],
) -> np.ndarray:
    """Construct a four-view law under binary latent conditional independence."""

    if not 0.0 <= prevalence_plus <= 1.0:
        raise ValueError("prevalence_plus must lie in [0, 1]")
    if len(conditional_plus) != 4:
        raise ValueError("exactly four view channels are required")
    for channel in conditional_plus:
        if len(channel) != 2 or any(prob < 0.0 or prob > 1.0 for prob in channel):
            raise ValueError("each channel must contain two probabilities in [0, 1]")

    joint = np.zeros((2, 2, 2, 2), dtype=float)
    for latent_index, latent_mass in enumerate(
        (1.0 - prevalence_plus, prevalence_plus)
    ):
        for indices in product((0, 1), repeat=4):
            mass = latent_mass
            for view, observed_index in enumerate(indices):
                p_plus = conditional_plus[view][latent_index]
                mass *= p_plus if observed_index == 1 else 1.0 - p_plus
            joint[indices] += mass
    return joint


def four_view_moments(joint: np.ndarray) -> FourViewMoments:
    """Return first through fourth distinct-view centered moments."""

    probs = _validate_joint(joint, 4)
    values = (-1.0, 1.0)

    means = []
    for axis in range(4):
        other_axes = tuple(index for index in range(4) if index != axis)
        marginal = probs.sum(axis=other_axes)
        means.append(float(marginal[1] - marginal[0]))

    covariance = {pair: 0.0 for pair in PAIR_ORDER}
    third = {triple: 0.0 for triple in TRIPLE_ORDER}
    fourth = 0.0

    for indices in product((0, 1), repeat=4):
        xs = [values[index] for index in indices]
        centered = [xs[index] - means[index] for index in range(4)]
        mass = float(probs[indices])

        for pair in PAIR_ORDER:
            covariance[pair] += mass * centered[pair[0]] * centered[pair[1]]
        for triple in TRIPLE_ORDER:
            third[triple] += (
                mass
                * centered[triple[0]]
                * centered[triple[1]]
                * centered[triple[2]]
            )
        fourth += mass * float(np.prod(centered))

    return FourViewMoments(
        means=tuple(float(value) for value in means),
        covariances=tuple(float(covariance[pair]) for pair in PAIR_ORDER),
        third_central_moments=tuple(float(third[triple]) for triple in TRIPLE_ORDER),
        fourth_central_moment=float(fourth),
    )


def _covariance_lookup(moments: FourViewMoments) -> dict[tuple[int, int], float]:
    return dict(zip(PAIR_ORDER, moments.covariances, strict=True))


def _triple_q_values(
    moments: FourViewMoments,
    tolerance: float,
) -> tuple[float, float, float, float] | None:
    covariance = _covariance_lookup(moments)
    q_values = []
    for triple, third in zip(
        TRIPLE_ORDER,
        moments.third_central_moments,
        strict=True,
    ):
        i, j, k = triple
        denominator = (
            covariance[tuple(sorted((i, j)))]
            * covariance[tuple(sorted((i, k)))]
            * covariance[tuple(sorted((j, k)))]
        )
        if denominator <= tolerance:
            return None
        q_values.append(float(third * third / denominator))
    return tuple(q_values)


def four_view_overidentification_diagnostics(
    joint: np.ndarray,
    *,
    tolerance: float = 1e-10,
) -> FourViewAdequacyDiagnostics:
    """Evaluate exact P75 population restrictions and full-law reconstruction.

    The explicit residuals are necessary consequences of the declared four-view
    model. ``compatible_with_declared_model`` is stricter: it additionally uses
    the first three views for P73 recovery, infers the fourth channel, and checks
    reconstruction of the complete 2x2x2x2 law.
    """

    if tolerance <= 0.0:
        raise ValueError("tolerance must be positive")

    probs = _validate_joint(joint, 4)
    moments = four_view_moments(probs)
    covariance = _covariance_lookup(moments)

    products = (
        covariance[(0, 1)] * covariance[(2, 3)],
        covariance[(0, 2)] * covariance[(1, 3)],
        covariance[(0, 3)] * covariance[(1, 2)],
    )
    tetrad_residuals = (
        float(products[0] - products[1]),
        float(products[0] - products[2]),
    )

    q_values = _triple_q_values(moments, tolerance)
    if q_values is None:
        q_spread = None
        fourth_residuals = None
    else:
        q_spread = float(max(q_values) - min(q_values))
        pairing_products = products
        fourth_residuals = tuple(
            float(
                moments.fourth_central_moment
                - (1.0 + q_value) * pairing_product
            )
            for q_value, pairing_product in zip(
                q_values[:3],
                pairing_products,
                strict=True,
            )
        )

    first_three = probs.sum(axis=3)
    try:
        recovery = recover_three_view_binary_model(
            first_three,
            anchor_view=0,
            tolerance=tolerance,
        )
    except ValueError as exc:
        return FourViewAdequacyDiagnostics(
            observed_dimension=15,
            model_parameter_dimension=9,
            generic_overidentifying_dimension=6,
            moments=moments,
            tetrad_products=tuple(float(value) for value in products),
            tetrad_residuals=tetrad_residuals,
            triple_q_values=q_values,
            triple_q_spread=q_spread,
            fourth_consistency_residuals=fourth_residuals,
            reconstruction_error=None,
            compatible_with_declared_model=False,
            reason=f"first three views fail P73 recovery: {exc}",
        )

    latent_mean = recovery.latent_mean
    latent_variance = 1.0 - latent_mean**2
    first_loading = (
        recovery.conditional_plus[0][1] - recovery.conditional_plus[0][0]
    )
    if abs(first_loading * latent_variance) <= tolerance:
        return FourViewAdequacyDiagnostics(
            observed_dimension=15,
            model_parameter_dimension=9,
            generic_overidentifying_dimension=6,
            moments=moments,
            tetrad_products=tuple(float(value) for value in products),
            tetrad_residuals=tetrad_residuals,
            triple_q_values=q_values,
            triple_q_spread=q_spread,
            fourth_consistency_residuals=fourth_residuals,
            reconstruction_error=None,
            compatible_with_declared_model=False,
            reason="fourth-view loading is unresolved from the P73 anchor",
        )

    fourth_loading = covariance[(0, 3)] / (first_loading * latent_variance)
    fourth_intercept = moments.means[3] - fourth_loading * latent_mean
    fourth_channel = (
        0.5 * (1.0 + fourth_intercept - fourth_loading),
        0.5 * (1.0 + fourth_intercept + fourth_loading),
    )
    if any(value < -100.0 * tolerance or value > 1.0 + 100.0 * tolerance for value in fourth_channel):
        return FourViewAdequacyDiagnostics(
            observed_dimension=15,
            model_parameter_dimension=9,
            generic_overidentifying_dimension=6,
            moments=moments,
            tetrad_products=tuple(float(value) for value in products),
            tetrad_residuals=tetrad_residuals,
            triple_q_values=q_values,
            triple_q_spread=q_spread,
            fourth_consistency_residuals=fourth_residuals,
            reconstruction_error=None,
            compatible_with_declared_model=False,
            reason="observable moments imply an invalid fourth binary channel",
        )

    clipped_fourth_channel = (
        float(np.clip(fourth_channel[0], 0.0, 1.0)),
        float(np.clip(fourth_channel[1], 0.0, 1.0)),
    )
    channels = recovery.conditional_plus + (clipped_fourth_channel,)
    reconstructed = four_view_joint_distribution_from_model(
        recovery.prevalence_plus,
        channels,
    )
    reconstruction_error = float(np.max(np.abs(reconstructed - probs)))
    compatible = reconstruction_error <= 1000.0 * tolerance

    return FourViewAdequacyDiagnostics(
        observed_dimension=15,
        model_parameter_dimension=9,
        generic_overidentifying_dimension=6,
        moments=moments,
        tetrad_products=tuple(float(value) for value in products),
        tetrad_residuals=tetrad_residuals,
        triple_q_values=q_values,
        triple_q_spread=q_spread,
        fourth_consistency_residuals=fourth_residuals,
        reconstruction_error=reconstruction_error,
        compatible_with_declared_model=compatible,
        reason=None if compatible else "four-view law fails full model reconstruction",
    )
