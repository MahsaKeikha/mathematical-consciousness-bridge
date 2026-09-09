"""Pairwise component-minimality tools for Proposition 13.

The module audits whether any two components of a labeled intervention-resolved
causal-structure fingerprint can reconstruct the three-component fingerprint on a
declared finite domain. It does not infer consciousness and does not establish
global minimality of every possible representation.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from math import isclose
from typing import TypeVar

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


def _component_tuple_close(
    left: tuple[float, ...],
    right: tuple[float, ...],
    *,
    atol: float = 1e-12,
    rtol: float = 1e-12,
) -> bool:
    """Compare one floating-point fingerprint component at audit precision."""
    return len(left) == len(right) and all(
        isclose(a, b, abs_tol=atol, rel_tol=rtol) for a, b in zip(left, right)
    )


def _fingerprint_close(
    left: tuple[tuple[float, ...], ...],
    right: tuple[tuple[float, ...], ...],
    *,
    atol: float = 1e-12,
    rtol: float = 1e-12,
) -> bool:
    """Compare nested floating-point fingerprints at declared audit precision."""
    return len(left) == len(right) and all(
        _component_tuple_close(a, b, atol=atol, rtol=rtol)
        for a, b in zip(left, right)
    )


def _projection_collision_numeric(
    full_signatures: Mapping[P, ComponentFingerprint],
    projected_features: Mapping[P, tuple[tuple[float, ...], ...]],
) -> tuple[P, P] | None:
    """Return a collision using tolerance only for floating-point audit equality.

    The proposition is exact at the mathematical level. The implementation uses
    floating-point probabilities, so equality of theoretically identical
    fingerprints is evaluated at a fixed numerical tolerance. A collision still
    requires the complete three-component fingerprints to differ beyond the same
    tolerance.
    """
    if set(full_signatures) != set(projected_features):
        raise ValueError("Full and projected features must use the same domain.")

    states = list(full_signatures)
    for left_index, left in enumerate(states):
        for right in states[left_index + 1 :]:
            if _fingerprint_close(
                projected_features[left], projected_features[right]
            ) and not _fingerprint_close(
                full_signatures[left], full_signatures[right]
            ):
                return left, right
    return None


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
        pair: _projection_collision_numeric(
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
