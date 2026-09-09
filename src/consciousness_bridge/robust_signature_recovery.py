"""Finite deterministic robustness tools for Proposition 8."""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from typing import TypeVar

from consciousness_bridge.identifiability import total_variation_discrete

P = TypeVar("P", bound=Hashable)
Protocol = TypeVar("Protocol", bound=Hashable)
Outcome = TypeVar("Outcome", bound=Hashable)
Z = TypeVar("Z", bound=Hashable)

Distribution = Mapping[Outcome, float]
PredictionTable = Mapping[P, Mapping[Protocol, Distribution]]


def max_protocol_tv_distance(
    predictions: PredictionTable[P, Protocol, Outcome],
    left: P,
    right: P,
) -> float:
    """Return max protocol-wise total variation for a physical pair."""
    _validate_prediction_table(predictions)
    protocols = set(predictions[left])
    return max(
        total_variation_discrete(
            predictions[left][protocol],
            predictions[right][protocol],
        )
        for protocol in protocols
    )


def signature_spread_and_separation(
    predictions: PredictionTable[P, Protocol, Outcome],
    feature: Mapping[P, Z],
) -> tuple[float, float]:
    """Return (within-signature spread, between-signature separation)."""
    _validate_prediction_table(predictions)
    if set(predictions) != set(feature):
        raise ValueError("Predictions and feature must use the same physical domain.")

    states = list(predictions)
    within_distances: list[float] = []
    between_distances: list[float] = []

    for left_index, left in enumerate(states):
        for right in states[left_index + 1 :]:
            distance = max_protocol_tv_distance(predictions, left, right)
            if feature[left] == feature[right]:
                within_distances.append(distance)
            else:
                between_distances.append(distance)

    if not between_distances:
        raise ValueError("At least two signature classes are required.")

    within = max(within_distances, default=0.0)
    between = min(between_distances)
    return within, between


def robust_threshold_interval(
    within_spread: float,
    between_separation: float,
    epsilon: float,
) -> tuple[float, float]:
    """Return the open threshold interval guaranteed by Proposition 8."""
    if epsilon < 0.0:
        raise ValueError("epsilon must be nonnegative.")
    if within_spread < 0.0 or between_separation < 0.0:
        raise ValueError("Distances must be nonnegative.")

    lower = within_spread + 2.0 * epsilon
    upper = between_separation - 2.0 * epsilon
    if not lower < upper:
        raise ValueError("Signature gap is not larger than 4 * epsilon.")
    return lower, upper


def classify_same_signature(
    estimated_predictions: PredictionTable[P, Protocol, Outcome],
    left: P,
    right: P,
    threshold: float,
) -> bool:
    """Classify a pair as same-signature by the P8 distance threshold."""
    if threshold < 0.0:
        raise ValueError("threshold must be nonnegative.")
    return max_protocol_tv_distance(estimated_predictions, left, right) < threshold


def _validate_prediction_table(
    predictions: PredictionTable[P, Protocol, Outcome],
) -> None:
    if not predictions:
        raise ValueError("Physical domain must be nonempty.")

    expected_protocols: set[Protocol] | None = None
    for protocol_table in predictions.values():
        protocols = set(protocol_table)
        if not protocols:
            raise ValueError("Protocol family must be nonempty.")
        if expected_protocols is None:
            expected_protocols = protocols
        elif protocols != expected_protocols:
            raise ValueError("Every physical state must use the same protocol family.")

        for distribution in protocol_table.values():
            total_variation_discrete(distribution, distribution)
