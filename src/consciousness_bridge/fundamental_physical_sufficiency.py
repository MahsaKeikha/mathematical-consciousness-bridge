"""Exact factorization and residual tests for a declared physical descriptor.

This module contains mathematical utilities for Proposition 19.  It does not
encode an experiential ontology.  The caller supplies finite labels for a
fundamental-state sample, its declared physical descriptor, and an independently
defined target label.
"""

from collections import defaultdict
from collections.abc import Hashable, Iterable, Mapping, Sequence
from math import log


def factorization_collisions(
    physical_labels: Sequence[Hashable], target_labels: Sequence[Hashable]
) -> list[tuple[int, int]]:
    """Return index pairs with equal physical labels but unequal target labels."""
    if len(physical_labels) != len(target_labels):
        raise ValueError("physical_labels and target_labels must have equal length")

    collisions: list[tuple[int, int]] = []
    first_seen: dict[Hashable, tuple[int, Hashable]] = {}
    for index, (physical, target) in enumerate(zip(physical_labels, target_labels)):
        previous = first_seen.get(physical)
        if previous is None:
            first_seen[physical] = (index, target)
            continue
        previous_index, previous_target = previous
        if target != previous_target:
            collisions.append((previous_index, index))
    return collisions


def factors_through_physical_descriptor(
    physical_labels: Sequence[Hashable], target_labels: Sequence[Hashable]
) -> bool:
    """Whether the target is constant on every observed physical fiber."""
    return not factorization_collisions(physical_labels, target_labels)


def induced_bridge_map(
    physical_labels: Sequence[Hashable], target_labels: Sequence[Hashable]
) -> dict[Hashable, Hashable]:
    """Construct the unique bridge map on the observed image when it exists."""
    collisions = factorization_collisions(physical_labels, target_labels)
    if collisions:
        raise ValueError("target does not factor through the physical descriptor")
    return dict(zip(physical_labels, target_labels))


def _normalized_joint(
    weights: Mapping[tuple[Hashable, Hashable, Hashable], float],
) -> dict[tuple[Hashable, Hashable, Hashable], float]:
    if not weights:
        raise ValueError("weights must be non-empty")
    if any(value < 0 for value in weights.values()):
        raise ValueError("weights must be non-negative")
    total = sum(weights.values())
    if total <= 0:
        raise ValueError("weights must have positive total mass")
    return {key: value / total for key, value in weights.items() if value > 0}


def conditional_mutual_information(
    weights: Mapping[tuple[Hashable, Hashable, Hashable], float],
) -> float:
    """Compute I(E;Omega|T) in nats for a finite joint law.

    Keys are ``(omega, physical, target)``.  Zero-mass entries may be omitted.
    """
    joint = _normalized_joint(weights)
    p_t: dict[Hashable, float] = defaultdict(float)
    p_ot: dict[tuple[Hashable, Hashable], float] = defaultdict(float)
    p_et: dict[tuple[Hashable, Hashable], float] = defaultdict(float)

    for (omega, physical, target), probability in joint.items():
        p_t[physical] += probability
        p_ot[(omega, physical)] += probability
        p_et[(target, physical)] += probability

    result = 0.0
    for (omega, physical, target), probability in joint.items():
        numerator = probability * p_t[physical]
        denominator = p_ot[(omega, physical)] * p_et[(target, physical)]
        result += probability * log(numerator / denominator)
    return result


def empirical_joint_from_records(
    records: Iterable[tuple[Hashable, Hashable, Hashable]],
) -> dict[tuple[Hashable, Hashable, Hashable], float]:
    """Convert finite ``(omega, physical, target)`` records to count weights."""
    counts: dict[tuple[Hashable, Hashable, Hashable], float] = defaultdict(float)
    count = 0
    for record in records:
        if len(record) != 3:
            raise ValueError("each record must contain omega, physical, target")
        counts[record] += 1.0
        count += 1
    if count == 0:
        raise ValueError("records must be non-empty")
    return dict(counts)
