"""Finite helpers for Proposition 5 feature sufficiency.

The functions test whether a proposed finite physical feature determines a declared
bridge assignment on the supplied domain. They do not establish that the bridge
assignment is empirically correct.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Hashable, Mapping
from typing import TypeVar

P = TypeVar("P", bound=Hashable)
Z = TypeVar("Z", bound=Hashable)
E = TypeVar("E", bound=Hashable)


def feature_is_bridge_sufficient(
    feature: Mapping[P, Z],
    bridge: Mapping[P, E],
) -> bool:
    """Return whether the bridge is constant on every finite feature fiber."""
    _validate_common_domain(feature, bridge)
    seen: dict[Z, E] = {}
    for physical_state, feature_value in feature.items():
        bridge_value = bridge[physical_state]
        if feature_value in seen and seen[feature_value] != bridge_value:
            return False
        seen[feature_value] = bridge_value
    return True


def induced_bridge_from_feature(
    feature: Mapping[P, Z],
    bridge: Mapping[P, E],
) -> dict[Z, E]:
    """Construct the unique finite factor map g when Proposition 5 holds."""
    if not feature_is_bridge_sufficient(feature, bridge):
        raise ValueError("Feature is not bridge-sufficient on the supplied domain.")

    induced: dict[Z, E] = {}
    for physical_state, feature_value in feature.items():
        induced[feature_value] = bridge[physical_state]
    return induced


def feature_counterexamples(
    feature: Mapping[P, Z],
    bridge: Mapping[P, E],
) -> tuple[tuple[P, P], ...]:
    """Return pairs sharing a feature value but receiving different bridge values."""
    _validate_common_domain(feature, bridge)
    fibers: dict[Z, list[P]] = defaultdict(list)
    for physical_state, feature_value in feature.items():
        fibers[feature_value].append(physical_state)

    counterexamples: list[tuple[P, P]] = []
    for states in fibers.values():
        for left_index, left in enumerate(states):
            for right in states[left_index + 1 :]:
                if bridge[left] != bridge[right]:
                    counterexamples.append((left, right))
    return tuple(counterexamples)


def feature_is_bridge_complete(
    feature: Mapping[P, Z],
    bridge: Mapping[P, E],
) -> bool:
    """Return whether feature equality is equivalent to bridge equality.

    This helper anticipates Proposition 6's complete-invariant condition.
    """
    _validate_common_domain(feature, bridge)
    states = list(feature)
    for left_index, left in enumerate(states):
        for right in states[left_index:]:
            same_feature = feature[left] == feature[right]
            same_bridge = bridge[left] == bridge[right]
            if same_feature != same_bridge:
                return False
    return True


def _validate_common_domain(
    feature: Mapping[P, Z],
    bridge: Mapping[P, E],
) -> None:
    if not feature:
        raise ValueError("Physical domain must be nonempty.")
    if set(feature) != set(bridge):
        raise ValueError("Feature and bridge maps must have the same physical domain.")
