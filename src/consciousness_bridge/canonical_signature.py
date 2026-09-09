"""Finite constructions for Proposition 6 canonical bridge signatures.

The canonical signature is defined from a supplied finite bridge assignment. It is
therefore a mathematical audit object, not an empirical discovery of consciousness.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Hashable, Mapping
from typing import TypeVar

from consciousness_bridge.feature_sufficiency import feature_is_bridge_sufficient

P = TypeVar("P", bound=Hashable)
Z = TypeVar("Z", bound=Hashable)
E = TypeVar("E", bound=Hashable)


def canonical_bridge_signature(
    bridge: Mapping[P, E],
) -> dict[P, frozenset[P]]:
    """Map each physical state to its canonical bridge-equivalence class."""
    if not bridge:
        raise ValueError("Bridge domain must be nonempty.")

    fibers: dict[E, set[P]] = defaultdict(set)
    for physical_state, experiential_state in bridge.items():
        fibers[experiential_state].add(physical_state)

    frozen_fibers = {
        experiential_state: frozenset(states)
        for experiential_state, states in fibers.items()
    }
    return {
        physical_state: frozen_fibers[experiential_state]
        for physical_state, experiential_state in bridge.items()
    }


def canonical_class_to_bridge_image(
    bridge: Mapping[P, E],
) -> dict[frozenset[P], E]:
    """Return the Proposition 6 bijection from canonical classes to bridge image."""
    signature = canonical_bridge_signature(bridge)
    result: dict[frozenset[P], E] = {}
    for physical_state, bridge_value in bridge.items():
        result[signature[physical_state]] = bridge_value
    return result


def sufficient_feature_to_canonical_signature(
    feature: Mapping[P, Z],
    bridge: Mapping[P, E],
) -> dict[Z, frozenset[P]]:
    """Return the unique factor map from a sufficient feature to canonical classes."""
    if not feature_is_bridge_sufficient(feature, bridge):
        raise ValueError("Feature is not bridge-sufficient on the supplied domain.")

    signature = canonical_bridge_signature(bridge)
    result: dict[Z, frozenset[P]] = {}
    for physical_state, feature_value in feature.items():
        result[feature_value] = signature[physical_state]
    return result


def canonical_factor_is_bijective(
    feature: Mapping[P, Z],
    bridge: Mapping[P, E],
) -> bool:
    """Return whether a sufficient feature is complete via the P6 factor map."""
    if not feature_is_bridge_sufficient(feature, bridge):
        return False

    factor = sufficient_feature_to_canonical_signature(feature, bridge)
    canonical_classes = set(canonical_bridge_signature(bridge).values())
    return len(factor) == len(canonical_classes) and set(factor.values()) == canonical_classes
