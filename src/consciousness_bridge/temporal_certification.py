"""Finite-error certification for temporal causal-structure trajectories.

This module implements Proposition 15. It propagates simultaneous fingerprint
error radii through the quotient metric introduced in Proposition 14. It does
not infer the error radii from a particular causal-structure estimator and does
not attach an experiential interpretation to temporal continuity.
"""

from __future__ import annotations

from collections.abc import Sequence
from math import log, sqrt

from consciousness_bridge.temporal_causal_structure import (
    ComponentFingerprint,
    PermutationAction,
    Weights,
    quotient_distance,
)


def _validate_radius(radius: float) -> None:
    if radius < 0:
        raise ValueError("Error radii must be nonnegative.")


def _validate_radii(radii: Sequence[float], path_length: int) -> None:
    if len(radii) != path_length:
        raise ValueError("One error radius is required for every path state.")
    for radius in radii:
        _validate_radius(radius)


def distance_interval(
    estimated_left: ComponentFingerprint,
    estimated_right: ComponentFingerprint,
    left_radius: float,
    right_radius: float,
    actions: Sequence[PermutationAction],
    weights: Weights = (1.0, 1.0, 1.0),
) -> tuple[float, float]:
    """Return the Proposition 15 interval for a true quotient distance."""
    _validate_radius(left_radius)
    _validate_radius(right_radius)
    estimate = quotient_distance(estimated_left, estimated_right, actions, weights)
    error = left_radius + right_radius
    return max(0.0, estimate - error), estimate + error


def certified_nonzero_change(
    estimated_left: ComponentFingerprint,
    estimated_right: ComponentFingerprint,
    left_radius: float,
    right_radius: float,
    actions: Sequence[PermutationAction],
    weights: Weights = (1.0, 1.0, 1.0),
) -> bool:
    """Return whether finite-error bounds certify a nonzero true separation."""
    lower, _ = distance_interval(
        estimated_left,
        estimated_right,
        left_radius,
        right_radius,
        actions,
        weights,
    )
    return lower > 0.0


def variation_interval(
    estimated_path: Sequence[ComponentFingerprint],
    radii: Sequence[float],
    actions: Sequence[PermutationAction],
    weights: Weights = (1.0, 1.0, 1.0),
) -> tuple[float, float]:
    """Return lower and upper bounds for true cumulative path variation."""
    if not estimated_path:
        raise ValueError("Variation certification requires at least one path state.")
    _validate_radii(radii, len(estimated_path))
    if len(estimated_path) == 1:
        return 0.0, 0.0

    estimated_variation = sum(
        quotient_distance(estimated_path[index], estimated_path[index + 1], actions, weights)
        for index in range(len(estimated_path) - 1)
    )
    variation_error = radii[0] + radii[-1] + 2.0 * sum(radii[1:-1])
    return (
        max(0.0, estimated_variation - variation_error),
        estimated_variation + variation_error,
    )


def maximum_step_interval(
    estimated_path: Sequence[ComponentFingerprint],
    radii: Sequence[float],
    actions: Sequence[PermutationAction],
    weights: Weights = (1.0, 1.0, 1.0),
) -> tuple[float, float]:
    """Return Proposition 15 bounds for the true maximum adjacent step."""
    if not estimated_path:
        raise ValueError("Maximum-step certification requires at least one path state.")
    _validate_radii(radii, len(estimated_path))
    if len(estimated_path) == 1:
        return 0.0, 0.0

    estimated_maximum = max(
        quotient_distance(estimated_path[index], estimated_path[index + 1], actions, weights)
        for index in range(len(estimated_path) - 1)
    )
    maximum_error = max(
        radii[index] + radii[index + 1] for index in range(len(radii) - 1)
    )
    return (
        max(0.0, estimated_maximum - maximum_error),
        estimated_maximum + maximum_error,
    )


def classify_step_against_threshold(
    estimated_left: ComponentFingerprint,
    estimated_right: ComponentFingerprint,
    left_radius: float,
    right_radius: float,
    threshold: float,
    actions: Sequence[PermutationAction],
    weights: Weights = (1.0, 1.0, 1.0),
) -> str:
    """Classify a step as below, above, or unresolved relative to a threshold."""
    if threshold < 0:
        raise ValueError("The structural-change threshold must be nonnegative.")
    lower, upper = distance_interval(
        estimated_left,
        estimated_right,
        left_radius,
        right_radius,
        actions,
        weights,
    )
    if lower > threshold:
        return "above"
    if upper <= threshold:
        return "below"
    return "unresolved"


def bounded_coordinate_radius(
    sample_count: int,
    coordinate_count: int,
    time_count: int,
    alpha: float,
) -> float:
    """Return the simultaneous Hoeffding radius for bounded sample-mean coordinates."""
    if sample_count <= 0:
        raise ValueError("sample_count must be positive.")
    if coordinate_count <= 0:
        raise ValueError("coordinate_count must be positive.")
    if time_count <= 0:
        raise ValueError("time_count must be positive.")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between zero and one.")

    return sqrt(log(2.0 * coordinate_count * time_count / alpha) / (2.0 * sample_count))


def weighted_bounded_coordinate_radius(
    sample_count: int,
    coordinate_count: int,
    time_count: int,
    alpha: float,
    weights: Weights = (1.0, 1.0, 1.0),
) -> float:
    """Return the weighted max-metric radius for the bounded-coordinate corollary."""
    if any(weight <= 0 for weight in weights):
        raise ValueError("All component weights must be positive.")
    return max(weights) * bounded_coordinate_radius(
        sample_count,
        coordinate_count,
        time_count,
        alpha,
    )
