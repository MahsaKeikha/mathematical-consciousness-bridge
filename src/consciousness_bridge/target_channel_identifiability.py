"""P73 three-view target-channel identifiability utilities.

The module treats a binary latent target as a declared statistical object. It does
not interpret the latent state as consciousness or experiential ground truth.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import sqrt

import numpy as np


@dataclass(frozen=True)
class ThreeViewMoments:
    """Observable moments for three binary views encoded as {-1, +1}."""

    means: tuple[float, float, float]
    covariances: tuple[float, float, float]
    third_central_moment: float


@dataclass(frozen=True)
class ThreeViewRecovery:
    """Recovered binary latent-class parameters under the P73 assumptions.

    ``conditional_plus[j]`` stores
    ``(P(X_j=+1 | S=-1), P(X_j=+1 | S=+1))`` in the orientation selected by
    ``anchor_view``. Reversing the latent labels swaps the two entries for every
    view and replaces ``prevalence_plus`` by ``1-prevalence_plus`` without
    changing the observable distribution or any stability coefficient.
    """

    prevalence_plus: float
    latent_mean: float
    conditional_plus: tuple[tuple[float, float], ...]
    single_view_stability: tuple[float, float, float]
    joint_stability: float
    moments: ThreeViewMoments


def _validate_probability_array(array: np.ndarray, shape: tuple[int, ...]) -> np.ndarray:
    probs = np.asarray(array, dtype=float)
    if probs.shape != shape:
        raise ValueError(f"expected probability array with shape {shape}")
    if not np.all(np.isfinite(probs)):
        raise ValueError("probabilities must be finite")
    if np.any(probs < 0.0):
        raise ValueError("probabilities must be nonnegative")
    total = float(probs.sum())
    if total <= 0.0:
        raise ValueError("probabilities must have positive total mass")
    return probs / total


def three_view_moments(joint: np.ndarray) -> ThreeViewMoments:
    """Return means, pair covariances, and the third central moment.

    Axis value 0 is interpreted as -1 and axis value 1 as +1.
    """

    probs = _validate_probability_array(joint, (2, 2, 2))
    values = (-1.0, 1.0)

    means = []
    for axis in range(3):
        other_axes = tuple(index for index in range(3) if index != axis)
        marginal = probs.sum(axis=other_axes)
        means.append(float(marginal[1] - marginal[0]))

    cov = np.zeros((3, 3), dtype=float)
    third = 0.0
    for indices in product((0, 1), repeat=3):
        xs = [values[index] for index in indices]
        mass = float(probs[indices])
        centered = [xs[index] - means[index] for index in range(3)]
        cov[0, 1] += mass * centered[0] * centered[1]
        cov[0, 2] += mass * centered[0] * centered[2]
        cov[1, 2] += mass * centered[1] * centered[2]
        third += mass * centered[0] * centered[1] * centered[2]

    return ThreeViewMoments(
        means=(float(means[0]), float(means[1]), float(means[2])),
        covariances=(float(cov[0, 1]), float(cov[0, 2]), float(cov[1, 2])),
        third_central_moment=float(third),
    )


def joint_distribution_from_model(
    prevalence_plus: float,
    conditional_plus: tuple[tuple[float, float], ...],
) -> np.ndarray:
    """Construct the three-view observable law under conditional independence."""

    if not 0.0 <= prevalence_plus <= 1.0:
        raise ValueError("prevalence_plus must lie in [0, 1]")
    if len(conditional_plus) != 3:
        raise ValueError("exactly three view channels are required")
    for channel in conditional_plus:
        if len(channel) != 2 or any(prob < 0.0 or prob > 1.0 for prob in channel):
            raise ValueError("each channel must contain two probabilities in [0, 1]")

    joint = np.zeros((2, 2, 2), dtype=float)
    for latent_index, latent_mass in enumerate(
        (1.0 - prevalence_plus, prevalence_plus)
    ):
        for indices in product((0, 1), repeat=3):
            mass = latent_mass
            for view, observed_index in enumerate(indices):
                p_plus = conditional_plus[view][latent_index]
                mass *= p_plus if observed_index == 1 else 1.0 - p_plus
            joint[indices] += mass
    return joint


def binary_channel_stability(channel: tuple[float, float]) -> float:
    """Return the P72 TV stability coefficient of a binary target channel."""

    p_plus_minus, p_plus_plus = channel
    if not 0.0 <= p_plus_minus <= 1.0 or not 0.0 <= p_plus_plus <= 1.0:
        raise ValueError("channel probabilities must lie in [0, 1]")
    return abs(float(p_plus_plus - p_plus_minus))


def joint_channel_stability(
    conditional_plus: tuple[tuple[float, float], ...],
) -> float:
    """Return TV separation between the two latent columns of the joint channel."""

    if len(conditional_plus) != 3:
        raise ValueError("exactly three view channels are required")
    columns = []
    for latent_index in (0, 1):
        column = []
        for indices in product((0, 1), repeat=3):
            mass = 1.0
            for view, observed_index in enumerate(indices):
                p_plus = conditional_plus[view][latent_index]
                mass *= p_plus if observed_index == 1 else 1.0 - p_plus
            column.append(mass)
        columns.append(np.asarray(column, dtype=float))
    return 0.5 * float(np.abs(columns[1] - columns[0]).sum())


def recover_three_view_binary_model(
    joint: np.ndarray,
    *,
    anchor_view: int = 0,
    tolerance: float = 1e-10,
) -> ThreeViewRecovery:
    """Recover the nondegenerate three-view binary latent model.

    Assumptions are exactly those used by P73: one binary latent state, three
    binary views that are conditionally independent given that state, interior
    latent prevalence, and nonzero loading for every view. The result is unique
    up to the global latent-label swap. ``anchor_view`` chooses one algebraic
    orientation by requiring that view's loading to be positive.

    The function also reconstructs the full observable law and rejects inputs
    that do not satisfy the declared model within ``tolerance``.
    """

    if anchor_view not in (0, 1, 2):
        raise ValueError("anchor_view must be 0, 1, or 2")
    if tolerance <= 0.0:
        raise ValueError("tolerance must be positive")

    probs = _validate_probability_array(joint, (2, 2, 2))
    moments = three_view_moments(probs)
    c12, c13, c23 = moments.covariances
    covariance_lookup = {
        (0, 1): c12,
        (0, 2): c13,
        (1, 2): c23,
    }

    def covariance(i: int, j: int) -> float:
        return covariance_lookup[tuple(sorted((i, j)))]

    product_cov = c12 * c13 * c23
    if product_cov <= tolerance:
        raise ValueError(
            "P73 recovery requires three nonzero pair covariances with positive product"
        )

    third = moments.third_central_moment
    q = third * third / product_cov
    latent_variance = 4.0 / (q + 4.0)
    if latent_variance <= tolerance:
        raise ValueError("latent prevalence is too close to a degenerate endpoint")

    others = [index for index in range(3) if index != anchor_view]
    ratio = (
        covariance(anchor_view, others[0])
        * covariance(anchor_view, others[1])
        / (covariance(others[0], others[1]) * latent_variance)
    )
    if ratio <= tolerance:
        raise ValueError("anchor loading is not identifiable in the declared orientation")

    loadings = np.zeros(3, dtype=float)
    loadings[anchor_view] = sqrt(ratio)
    for other in others:
        loadings[other] = covariance(anchor_view, other) / (
            loadings[anchor_view] * latent_variance
        )

    loading_product = float(np.prod(loadings))
    if abs(loading_product) <= tolerance:
        raise ValueError("all three view loadings must be nonzero")

    latent_mean = -third / (2.0 * latent_variance * loading_product)
    if abs(latent_mean) > 1.0 + 100.0 * tolerance:
        raise ValueError("recovered latent mean lies outside the binary-state range")
    latent_mean = float(np.clip(latent_mean, -1.0, 1.0))
    prevalence_plus = 0.5 * (1.0 + latent_mean)
    if prevalence_plus <= tolerance or prevalence_plus >= 1.0 - tolerance:
        raise ValueError("P73 requires interior latent prevalence")

    means = np.asarray(moments.means, dtype=float)
    intercepts = means - loadings * latent_mean

    channels = []
    for intercept, loading in zip(intercepts, loadings, strict=True):
        mean_minus = intercept - loading
        mean_plus = intercept + loading
        p_plus_minus = 0.5 * (1.0 + mean_minus)
        p_plus_plus = 0.5 * (1.0 + mean_plus)
        if (
            p_plus_minus < -100.0 * tolerance
            or p_plus_minus > 1.0 + 100.0 * tolerance
            or p_plus_plus < -100.0 * tolerance
            or p_plus_plus > 1.0 + 100.0 * tolerance
        ):
            raise ValueError("observable moments imply an invalid binary channel")
        channels.append(
            (
                float(np.clip(p_plus_minus, 0.0, 1.0)),
                float(np.clip(p_plus_plus, 0.0, 1.0)),
            )
        )

    conditional_plus = tuple(channels)
    reconstructed = joint_distribution_from_model(prevalence_plus, conditional_plus)
    if float(np.max(np.abs(reconstructed - probs))) > 1000.0 * tolerance:
        raise ValueError("joint law is not compatible with the declared three-view model")

    stability = tuple(binary_channel_stability(channel) for channel in conditional_plus)
    joint_stability = joint_channel_stability(conditional_plus)

    return ThreeViewRecovery(
        prevalence_plus=float(prevalence_plus),
        latent_mean=float(latent_mean),
        conditional_plus=conditional_plus,
        single_view_stability=(
            float(stability[0]),
            float(stability[1]),
            float(stability[2]),
        ),
        joint_stability=float(joint_stability),
        moments=moments,
    )


def symmetric_two_view_joint(loading_1: float, loading_2: float) -> np.ndarray:
    """Return a two-view law exposing the P73 two-view non-identifiability.

    The latent state has prevalence 1/2 and each conditionally independent view
    has zero intercept. The observable law depends only on the product of the two
    loadings, so distinct loading pairs with the same product are observationally
    identical.
    """

    if abs(loading_1) > 1.0 or abs(loading_2) > 1.0:
        raise ValueError("symmetric binary loadings must lie in [-1, 1]")
    correlation = loading_1 * loading_2
    joint = np.empty((2, 2), dtype=float)
    for i, x_1 in enumerate((-1.0, 1.0)):
        for j, x_2 in enumerate((-1.0, 1.0)):
            joint[i, j] = 0.25 * (1.0 + correlation * x_1 * x_2)
    return joint
