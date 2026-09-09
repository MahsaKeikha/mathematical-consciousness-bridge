"""Pairwise component-minimality tools for Proposition 13.

The module audits whether any two components of a labeled intervention-resolved
causal-structure fingerprint can reconstruct the three-component fingerprint on a
declared finite domain. It does not infer consciousness and does not establish
global minimality of every possible representation.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from typing import TypeVar

from consciousness_bridge.causal_structure_minimality import projection_collision

P = TypeVar("P", bound=Hashable)

ComponentFingerprint = tuple[
    tuple[float, ...],
    tuple[float, ...],
    tuple[float, ...],
]

_COMPONENT_INDEX = {
    "geometry": 0,
    "influence": 1,
    "partition": 2,
}


def component_projection(
    fingerprint: ComponentFingerprint,
    retained: Sequence[str],
) -> tuple[tuple[float, ...], ...]:
    """Project a (geometry, influence, partition) fingerprint onto components."""
    names = tuple(retained)
    if not names:
        raise ValueError("At least one component must be retained.")
    if len(set(names)) != len(names):
        raise ValueError("Retained component names must be unique.")
    unknown = [name for name in names if name not in _COMPONENT_INDEX]
    if unknown:
        raise ValueError(f"Unknown causal-structure component names: {unknown}")
    return tuple(fingerprint[_COMPONENT_INDEX[name]] for name in names)


def projected_feature_map(
    full_signatures: Mapping[P, ComponentFingerprint],
    retained: Sequence[str],
) -> dict[P, tuple[tuple[float, ...], ...]]:
    """Return a component projection for every state in a finite audit domain."""
    return {
        state: component_projection(fingerprint, retained)
        for state, fingerprint in full_signatures.items()
    }


def pairwise_component_collisions(
    full_signatures: Mapping[P, ComponentFingerprint],
) -> dict[tuple[str, str], tuple[P, P] | None]:
    """Return one collision witness for each two-component projection."""
    pairs = (
        ("geometry", "influence"),
        ("geometry", "partition"),
        ("influence", "partition"),
    )
    return {
        pair: projection_collision(
            full_signatures,
            projected_feature_map(full_signatures, pair),
        )
        for pair in pairs
    }


def every_pairwise_projection_is_incomplete(
    full_signatures: Mapping[P, ComponentFingerprint],
) -> bool:
    """Return whether all three two-component projections admit a collision."""
    return all(
        collision is not None
        for collision in pairwise_component_collisions(full_signatures).values()
    )
