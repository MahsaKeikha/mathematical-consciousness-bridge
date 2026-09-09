"""Composition tools for Proposition 16 intervention-resolved causal structure.

The module formalizes independent physical composition and coupling witnesses at the
level of intervention-conditioned response laws. It does not assign experiential
meaning to composition, coupling, or irreducibility.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from itertools import product
from typing import TypeVar

from consciousness_bridge.identifiability import total_variation_discrete
from consciousness_bridge.intervention_causal_structure import (
    JointDistribution,
    ResponseTable,
    directed_influence_matrix,
    marginal_distribution,
    partition_response_irreducibility,
)

InterventionA = TypeVar("InterventionA", bound=Hashable)
InterventionB = TypeVar("InterventionB", bound=Hashable)
Delay = TypeVar("Delay", bound=Hashable)


def tensor_product_distribution(
    left: JointDistribution,
    right: JointDistribution,
) -> dict[tuple[Hashable, ...], float]:
    """Return the product law on concatenated joint outcomes."""
    result: dict[tuple[Hashable, ...], float] = {}
    for (left_outcome, left_probability), (
        right_outcome,
        right_probability,
    ) in product(left.items(), right.items()):
        outcome = tuple(left_outcome) + tuple(right_outcome)
        result[outcome] = result.get(outcome, 0.0) + (
            left_probability * right_probability
        )
    total_variation_discrete(result, result)
    return result


def compose_independent_response_tables(
    left: ResponseTable[InterventionA, Delay],
    right: ResponseTable[InterventionB, Delay],
) -> dict[
    tuple[InterventionA, InterventionB],
    dict[Delay, dict[tuple[Hashable, ...], float]],
]:
    """Construct the exactly independent product-response composition."""
    if not left or not right:
        raise ValueError("Both response tables must be nonempty.")

    left_delays = set(next(iter(left.values())))
    right_delays = set(next(iter(right.values())))
    if left_delays != right_delays:
        raise ValueError("Response tables must use the same delay family.")
    if any(set(table) != left_delays for table in left.values()):
        raise ValueError("Left response table has inconsistent delay families.")
    if any(set(table) != right_delays for table in right.values()):
        raise ValueError("Right response table has inconsistent delay families.")

    composed = {}
    for left_intervention, right_intervention in product(left, right):
        composed[(left_intervention, right_intervention)] = {
            delay: tensor_product_distribution(
                left[left_intervention][delay],
                right[right_intervention][delay],
            )
            for delay in left_delays
        }
    return composed


def composed_response_distance_bounds(
    left_distance: float,
    right_distance: float,
) -> tuple[float, float]:
    """Return generic lower and product-coupling upper TV bounds."""
    for value in (left_distance, right_distance):
        if value < 0.0 or value > 1.0:
            raise ValueError("Total-variation distances must lie in [0, 1].")
    lower = max(left_distance, right_distance)
    upper = left_distance + right_distance - left_distance * right_distance
    return lower, upper


def common_factor_product_distance(
    first: JointDistribution,
    second: JointDistribution,
    common: JointDistribution,
) -> float:
    """Return TV after tensoring both distributions with the same factor."""
    return total_variation_discrete(
        tensor_product_distribution(first, common),
        tensor_product_distribution(second, common),
    )


def subsystem_partition(block_count_left: int, block_count_right: int):
    """Return the partition separating complete left and right subsystems."""
    if block_count_left < 1 or block_count_right < 1:
        raise ValueError("Subsystem block counts must be positive.")
    left = tuple(range(block_count_left))
    right = tuple(range(block_count_left, block_count_left + block_count_right))
    return (left, right)


def coupling_defect(
    responses: ResponseTable[Hashable, Delay],
    block_count_left: int,
    block_count_right: int,
    delay: Delay,
) -> float:
    """Return response-factorization defect across the declared subsystem split."""
    partition = subsystem_partition(block_count_left, block_count_right)
    return partition_response_irreducibility(responses, partition, delay)


def response_factorization_defect_direct(
    distribution: JointDistribution,
    block_count_left: int,
    block_count_right: int,
) -> float:
    """Return TV distance to the product of the two subsystem marginals."""
    if block_count_left < 1 or block_count_right < 1:
        raise ValueError("Subsystem block counts must be positive.")
    expected = block_count_left + block_count_right
    if any(len(outcome) != expected for outcome in distribution):
        raise ValueError("Joint outcome dimension does not match subsystem counts.")

    left_indices = tuple(range(block_count_left))
    right_indices = tuple(range(block_count_left, expected))
    left = marginal_distribution(distribution, left_indices)
    right = marginal_distribution(distribution, right_indices)
    product_distribution = tensor_product_distribution(left, right)
    return total_variation_discrete(distribution, product_distribution)


def maximum_response_factorization_defect(
    responses: ResponseTable[Hashable, Delay],
    block_count_left: int,
    block_count_right: int,
    delay: Delay,
) -> float:
    """Return the maximum direct factorization defect across interventions."""
    return max(
        response_factorization_defect_direct(
            delay_table[delay], block_count_left, block_count_right
        )
        for delay_table in responses.values()
    )


def maximum_cross_component_influence(
    responses: ResponseTable[Hashable, Delay],
    source_pairs: Mapping[int, Sequence[tuple[Hashable, Hashable]]],
    block_count_left: int,
    block_count_right: int,
    delay: Delay,
) -> float:
    """Return the strongest directed influence crossing the subsystem split."""
    total_blocks = block_count_left + block_count_right
    matrix = directed_influence_matrix(
        responses,
        source_pairs,
        delay,
        total_blocks,
    )
    left = range(block_count_left)
    right = range(block_count_left, total_blocks)
    return max(
        (
            value
            for i in left
            for j in right
            for value in (matrix[i][j], matrix[j][i])
        ),
        default=0.0,
    )


def composition_witness(
    responses: ResponseTable[Hashable, Delay],
    source_pairs: Mapping[int, Sequence[tuple[Hashable, Hashable]]],
    block_count_left: int,
    block_count_right: int,
    delay: Delay,
) -> tuple[float, float]:
    """Return factorization defect and maximum cross-component influence."""
    return (
        maximum_response_factorization_defect(
            responses,
            block_count_left,
            block_count_right,
            delay,
        ),
        maximum_cross_component_influence(
            responses,
            source_pairs,
            block_count_left,
            block_count_right,
            delay,
        ),
    )
