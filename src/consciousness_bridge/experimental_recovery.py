"""Finite recoverability checks for Proposition 7.

An experimental fingerprint may contain more information than the target feature. The
criterion here asks only whether equal fingerprints force equal target-feature values.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from typing import TypeVar

P = TypeVar("P", bound=Hashable)
O = TypeVar("O", bound=Hashable)
Z = TypeVar("Z", bound=Hashable)
E = TypeVar("E", bound=Hashable)


def feature_is_recoverable_from_fingerprint(
    fingerprint: Mapping[P, O],
    feature: Mapping[P, Z],
) -> bool:
    """Return whether a finite observable fingerprint determines the feature."""
    _validate_common_domain(fingerprint, feature)
    seen: dict[O, Z] = {}
    for physical_state, observable_value in fingerprint.items():
        feature_value = feature[physical_state]
        if observable_value in seen and seen[observable_value] != feature_value:
            return False
        seen[observable_value] = feature_value
    return True


def feature_decoder_from_fingerprint(
    fingerprint: Mapping[P, O],
    feature: Mapping[P, Z],
) -> dict[O, Z]:
    """Construct the unique finite decoder when Proposition 7 holds."""
    if not feature_is_recoverable_from_fingerprint(fingerprint, feature):
        raise ValueError("Observable fingerprint does not determine the feature.")

    decoder: dict[O, Z] = {}
    for physical_state, observable_value in fingerprint.items():
        decoder[observable_value] = feature[physical_state]
    return decoder


def unresolved_feature_pairs(
    fingerprint: Mapping[P, O],
    feature: Mapping[P, Z],
) -> tuple[tuple[P, P], ...]:
    """Return pairs with equal fingerprints but different target features."""
    _validate_common_domain(fingerprint, feature)
    states = list(fingerprint)
    unresolved: list[tuple[P, P]] = []
    for left_index, left in enumerate(states):
        for right in states[left_index + 1 :]:
            if (
                fingerprint[left] == fingerprint[right]
                and feature[left] != feature[right]
            ):
                unresolved.append((left, right))
    return tuple(unresolved)


def bridge_decoder_from_recoverable_feature(
    fingerprint: Mapping[P, O],
    feature: Mapping[P, Z],
    bridge: Mapping[P, E],
) -> dict[O, E]:
    """Decode bridge values when fingerprint -> feature -> bridge both factor."""
    _validate_common_domain(fingerprint, feature)
    _validate_common_domain(fingerprint, bridge)

    feature_decoder = feature_decoder_from_fingerprint(fingerprint, feature)

    feature_to_bridge: dict[Z, E] = {}
    for physical_state, feature_value in feature.items():
        bridge_value = bridge[physical_state]
        if feature_value in feature_to_bridge and feature_to_bridge[feature_value] != bridge_value:
            raise ValueError("Feature is not bridge-sufficient.")
        feature_to_bridge[feature_value] = bridge_value

    return {
        observable_value: feature_to_bridge[feature_value]
        for observable_value, feature_value in feature_decoder.items()
    }


def _validate_common_domain(
    left: Mapping[P, object],
    right: Mapping[P, object],
) -> None:
    if not left:
        raise ValueError("Physical domain must be nonempty.")
    if set(left) != set(right):
        raise ValueError("Maps must have the same physical domain.")
