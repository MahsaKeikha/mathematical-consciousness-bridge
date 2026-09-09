"""Finite projection-collision tools for the causal-structure candidate.

These utilities test whether a compressed physical feature can reconstruct a richer
three-component causal-structure fingerprint on a declared finite benchmark. They
do not infer consciousness.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from itertools import combinations
from typing import TypeVar

from consciousness_bridge.intervention_causal_geometry import (
    aggregate_directed_influence_matrix,
    partition_response_irreducibility,
    response_distance,
)

P = TypeVar("P", bound=Hashable)
Intervention = TypeVar("Intervention", bound=Hashable)
Delay = TypeVar("Delay", bound=Hashable)


def geometry_fingerprint(
    responses: Mapping[
        Intervention,
        Mapping[Delay, Mapping[tuple[Hashable, ...], float]],
    ],
    interventions: Sequence[Intervention],
    delays: Sequence[Delay],
) -> tuple[float, ...]:
    """Return ordered pairwise response distances over declared delays."""
    if not interventions:
        raise ValueError("At least one intervention is required.")
    if not delays:
        raise ValueError("At least one delay is required.")

    values: list[float] = []
    for delay in delays:
        for left, right in combinations(interventions, 2):
            values.append(response_distance(responses, left, right, delay))
    return tuple(values)


def partition_fingerprint(
    responses: Mapping[
        Intervention,
        Mapping[Delay, Mapping[tuple[Hashable, ...], float]],
    ],
    partitions: Sequence[Sequence[Sequence[int]]],
    delays: Sequence[Delay],
) -> tuple[float, ...]:
    """Return ordered partition-irredundancy values over partitions and delays."""
    if not partitions:
        raise ValueError("At least one partition is required.")
    if not delays:
        raise ValueError("At least one delay is required.")

    return tuple(
        partition_response_irreducibility(responses, partition, delay)
        for partition in partitions
        for delay in delays
    )


def influence_fingerprint(
    responses: Mapping[
        Intervention,
        Mapping[Delay, Mapping[tuple[Hashable, ...], float]],
    ],
    source_pairs: Mapping[int, Sequence[tuple[Intervention, Intervention]]],
    delays: Sequence[Delay],
    block_count: int,
) -> tuple[float, ...]:
    """Return flattened max-over-delay directed influence matrix."""
    matrix = aggregate_directed_influence_matrix(
        responses,
        source_pairs,
        delays,
        block_count,
    )
    return tuple(value for row in matrix for value in row)


def labeled_causal_structure_fingerprint(
    responses: Mapping[
        Intervention,
        Mapping[Delay, Mapping[tuple[Hashable, ...], float]],
    ],
    interventions: Sequence[Intervention],
    delays: Sequence[Delay],
    source_pairs: Mapping[int, Sequence[tuple[Intervention, Intervention]]],
    partitions: Sequence[Sequence[Sequence[int]]],
    block_count: int,
) -> tuple[tuple[float, ...], tuple[float, ...], tuple[float, ...]]:
    """Return (geometry, influence, partition) for a fixed-label finite audit."""
    return (
        geometry_fingerprint(responses, interventions, delays),
        influence_fingerprint(responses, source_pairs, delays, block_count),
        partition_fingerprint(responses, partitions, delays),
    )


def projection_collision(
    full_signatures: Mapping[P, Hashable],
    projected_features: Mapping[P, Hashable],
) -> tuple[P, P] | None:
    """Return one pair with equal projection but different full signature."""
    if set(full_signatures) != set(projected_features):
        raise ValueError("Full and projected features must use the same domain.")

    states = list(full_signatures)
    for left_index, left in enumerate(states):
        for right in states[left_index + 1 :]:
            if (
                projected_features[left] == projected_features[right]
                and full_signatures[left] != full_signatures[right]
            ):
                return left, right
    return None


def projection_is_complete(
    full_signatures: Mapping[P, Hashable],
    projected_features: Mapping[P, Hashable],
) -> bool:
    """Return whether a projection reconstructs the full signature on the domain."""
    return projection_collision(full_signatures, projected_features) is None
