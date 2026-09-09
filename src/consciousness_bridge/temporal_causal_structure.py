"""Temporal continuation tools for intervention-resolved causal structure.

The functions in this module operate on finite component fingerprints
(geometry, directed influence, partition irreducibility). They implement the
metric, relabeling-quotient distance, and path-variation constructions used in
Proposition 14. They do not attach an experiential interpretation to temporal
continuity.
"""

from __future__ import annotations

from collections.abc import Sequence
from math import isfinite

ComponentFingerprint = tuple[
    tuple[float, ...],
    tuple[float, ...],
    tuple[float, ...],
]
Permutation = tuple[int, ...]
PermutationAction = tuple[Permutation, Permutation, Permutation]
Weights = tuple[float, float, float]


def _validate_fingerprint(fingerprint: ComponentFingerprint) -> None:
    if len(fingerprint) != 3:
        raise ValueError("A causal-structure fingerprint must contain G, A, and K.")
    for component in fingerprint:
        if any(not isfinite(value) for value in component):
            raise ValueError("Fingerprint coordinates must be finite real values.")


def _validate_weights(weights: Weights) -> None:
    if len(weights) != 3 or any(weight <= 0 or not isfinite(weight) for weight in weights):
        raise ValueError("All three component weights must be positive and finite.")


def _sup_distance(left: tuple[float, ...], right: tuple[float, ...]) -> float:
    if len(left) != len(right):
        raise ValueError("Compared fingerprint components must have equal dimensions.")
    if not left:
        return 0.0
    return max(abs(a - b) for a, b in zip(left, right))


def weighted_component_distance(
    left: ComponentFingerprint,
    right: ComponentFingerprint,
    weights: Weights = (1.0, 1.0, 1.0),
) -> float:
    """Return the weighted max metric across G, A, and K components."""
    _validate_fingerprint(left)
    _validate_fingerprint(right)
    _validate_weights(weights)

    distances = (
        _sup_distance(left[0], right[0]),
        _sup_distance(left[1], right[1]),
        _sup_distance(left[2], right[2]),
    )
    return max(weight * distance for weight, distance in zip(weights, distances))


def _validate_permutation(permutation: Permutation, dimension: int) -> None:
    if len(permutation) != dimension or set(permutation) != set(range(dimension)):
        raise ValueError("Each relabeling must be a permutation of component coordinates.")


def apply_relabeling(
    fingerprint: ComponentFingerprint,
    action: PermutationAction,
) -> ComponentFingerprint:
    """Apply a coordinate-permutation relabeling to a component fingerprint."""
    _validate_fingerprint(fingerprint)
    if len(action) != 3:
        raise ValueError("A relabeling action must specify G, A, and K permutations.")

    transformed: list[tuple[float, ...]] = []
    for component, permutation in zip(fingerprint, action):
        _validate_permutation(permutation, len(component))
        transformed.append(tuple(component[index] for index in permutation))

    return transformed[0], transformed[1], transformed[2]


def identity_action(fingerprint: ComponentFingerprint) -> PermutationAction:
    """Return the coordinate identity action for a fingerprint."""
    _validate_fingerprint(fingerprint)
    return tuple(tuple(range(len(component))) for component in fingerprint)  # type: ignore[return-value]


def quotient_distance(
    left: ComponentFingerprint,
    right: ComponentFingerprint,
    actions: Sequence[PermutationAction],
    weights: Weights = (1.0, 1.0, 1.0),
) -> float:
    """Return the minimum weighted distance over declared relabelings of right.

    Proposition 14 assumes ``actions`` forms a finite isometry group for the
    declared fingerprint representation. The implementation intentionally does
    not infer that scientific choice from the data.
    """
    if not actions:
        raise ValueError("At least one admissible relabeling action is required.")

    return min(
        weighted_component_distance(
            left,
            apply_relabeling(right, action),
            weights,
        )
        for action in actions
    )


def path_variation(
    path: Sequence[ComponentFingerprint],
    actions: Sequence[PermutationAction],
    weights: Weights = (1.0, 1.0, 1.0),
) -> float:
    """Return cumulative adjacent quotient distance along a temporal path."""
    if len(path) < 2:
        return 0.0
    return sum(
        quotient_distance(left, right, actions, weights)
        for left, right in zip(path, path[1:])
    )


def maximum_step_distance(
    path: Sequence[ComponentFingerprint],
    actions: Sequence[PermutationAction],
    weights: Weights = (1.0, 1.0, 1.0),
) -> float:
    """Return the largest adjacent quotient distance along a temporal path."""
    if len(path) < 2:
        return 0.0
    return max(
        quotient_distance(left, right, actions, weights)
        for left, right in zip(path, path[1:])
    )


def endpoint_distance(
    path: Sequence[ComponentFingerprint],
    actions: Sequence[PermutationAction],
    weights: Weights = (1.0, 1.0, 1.0),
) -> float:
    """Return quotient distance between the first and final path states."""
    if not path:
        raise ValueError("Endpoint distance requires at least one path state.")
    if len(path) == 1:
        return 0.0
    return quotient_distance(path[0], path[-1], actions, weights)
