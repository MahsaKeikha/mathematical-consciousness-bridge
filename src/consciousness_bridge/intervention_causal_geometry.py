"""Finite discrete tools for Proposition 11 intervention-resolved causal structure.

The module constructs physical perturbation-response quantities. It does not assign
consciousness and does not treat any one diagnostic as a consciousness criterion.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from itertools import combinations, product
from typing import TypeVar

from consciousness_bridge.identifiability import total_variation_discrete

Intervention = TypeVar("Intervention", bound=Hashable)
Delay = TypeVar("Delay", bound=Hashable)
OutcomeValue = TypeVar("OutcomeValue", bound=Hashable)

JointOutcome = tuple[Hashable, ...]
JointDistribution = Mapping[JointOutcome, float]
ResponseTable = Mapping[Intervention, Mapping[Delay, JointDistribution]]
InterventionPairs = Mapping[int, Sequence[tuple[Intervention, Intervention]]]


def response_distance(
    responses: ResponseTable[Intervention, Delay],
    first: Intervention,
    second: Intervention,
    delay: Delay,
) -> float:
    """Return TV distance between two intervention-conditioned joint responses."""
    _validate_response_table(responses)
    return total_variation_discrete(
        responses[first][delay],
        responses[second][delay],
    )


def response_geometry(
    responses: ResponseTable[Intervention, Delay],
    delay: Delay,
) -> dict[tuple[Intervention, Intervention], float]:
    """Return all unordered intervention-pair distances at one delay."""
    _validate_response_table(responses)
    interventions = list(responses)
    return {
        (left, right): response_distance(responses, left, right, delay)
        for left, right in combinations(interventions, 2)
    }


def response_diameter(
    responses: ResponseTable[Intervention, Delay],
    delay: Delay,
) -> float:
    """Return the diameter of the intervention-response pseudometric."""
    geometry = response_geometry(responses, delay)
    return max(geometry.values(), default=0.0)


def marginal_distribution(
    distribution: JointDistribution,
    block_indices: Sequence[int],
) -> dict[tuple[Hashable, ...], float]:
    """Marginalize a finite joint distribution onto selected block indices."""
    block_tuple = tuple(block_indices)
    if not block_tuple:
        raise ValueError("At least one block index is required.")

    dimension = _joint_dimension(distribution)
    if len(set(block_tuple)) != len(block_tuple):
        raise ValueError("Block indices must be unique.")
    if any(index < 0 or index >= dimension for index in block_tuple):
        raise ValueError("Block index is outside the joint outcome dimension.")

    marginal: dict[tuple[Hashable, ...], float] = {}
    for outcome, probability in distribution.items():
        key = tuple(outcome[index] for index in block_tuple)
        marginal[key] = marginal.get(key, 0.0) + probability
    return marginal


def productized_partition_distribution(
    distribution: JointDistribution,
    partition: Sequence[Sequence[int]],
) -> dict[JointOutcome, float]:
    """Return the product of block marginals induced by a declared partition."""
    dimension = _joint_dimension(distribution)
    blocks = _validate_partition(partition, dimension)
    marginals = [marginal_distribution(distribution, block) for block in blocks]

    product_distribution: dict[JointOutcome, float] = {}
    marginal_items = [list(marginal.items()) for marginal in marginals]

    for block_choices in product(*marginal_items):
        outcome: list[Hashable | None] = [None] * dimension
        probability = 1.0
        for block, (block_outcome, block_probability) in zip(
            blocks,
            block_choices,
            strict=True,
        ):
            probability *= block_probability
            for index, value in zip(block, block_outcome, strict=True):
                outcome[index] = value

        if any(value is None for value in outcome):
            raise RuntimeError("Partition did not reconstruct the full outcome.")
        joint_outcome = tuple(outcome)  # type: ignore[arg-type]
        product_distribution[joint_outcome] = (
            product_distribution.get(joint_outcome, 0.0) + probability
        )

    return product_distribution


def partition_response_irreducibility(
    responses: ResponseTable[Intervention, Delay],
    partition: Sequence[Sequence[int]],
    delay: Delay,
) -> float:
    """Return max intervention-wise TV distance from the partition product model."""
    _validate_response_table(responses)
    return max(
        total_variation_discrete(
            delay_table[delay],
            productized_partition_distribution(delay_table[delay], partition),
        )
        for delay_table in responses.values()
    )


def directed_influence_matrix(
    responses: ResponseTable[Intervention, Delay],
    source_pairs: InterventionPairs[Intervention],
    delay: Delay,
    block_count: int,
) -> tuple[tuple[float, ...], ...]:
    """Return source-to-target TV influence under matched intervention pairs."""
    _validate_response_table(responses)
    if block_count < 1:
        raise ValueError("block_count must be positive.")

    dimension = _response_dimension(responses)
    if dimension != block_count:
        raise ValueError("block_count must match the joint response dimension.")
    if any(source < 0 or source >= block_count for source in source_pairs):
        raise ValueError("Source block index is outside the response dimension.")

    matrix: list[list[float]] = [
        [0.0 for _ in range(block_count)] for _ in range(block_count)
    ]

    for source in range(block_count):
        pairs = source_pairs.get(source, ())
        for target in range(block_count):
            influence = 0.0
            for first, second in pairs:
                first_marginal = marginal_distribution(
                    responses[first][delay],
                    (target,),
                )
                second_marginal = marginal_distribution(
                    responses[second][delay],
                    (target,),
                )
                influence = max(
                    influence,
                    total_variation_discrete(first_marginal, second_marginal),
                )
            matrix[source][target] = influence

    return tuple(tuple(row) for row in matrix)


def aggregate_directed_influence_matrix(
    responses: ResponseTable[Intervention, Delay],
    source_pairs: InterventionPairs[Intervention],
    delays: Sequence[Delay],
    block_count: int,
) -> tuple[tuple[float, ...], ...]:
    """Return elementwise maximum influence across a nonempty delay family."""
    if not delays:
        raise ValueError("At least one delay is required.")

    matrices = [
        directed_influence_matrix(responses, source_pairs, delay, block_count)
        for delay in delays
    ]
    return tuple(
        tuple(max(matrix[source][target] for matrix in matrices) for target in range(block_count))
        for source in range(block_count)
    )


def has_directed_cycle(
    influence_matrix: Sequence[Sequence[float]],
    tolerance: float = 0.0,
) -> bool:
    """Return whether positive off-diagonal influence contains a directed cycle."""
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative.")

    size = len(influence_matrix)
    if any(len(row) != size for row in influence_matrix):
        raise ValueError("Influence matrix must be square.")

    adjacency = [
        [
            target
            for target, value in enumerate(row)
            if target != source and value > tolerance
        ]
        for source, row in enumerate(influence_matrix)
    ]

    state = [0] * size

    def visit(node: int) -> bool:
        state[node] = 1
        for neighbor in adjacency[node]:
            if state[neighbor] == 1:
                return True
            if state[neighbor] == 0 and visit(neighbor):
                return True
        state[node] = 2
        return False

    return any(state[node] == 0 and visit(node) for node in range(size))


def relabel_joint_responses(
    responses: ResponseTable[Intervention, Delay],
    relabeling: Mapping[JointOutcome, JointOutcome],
) -> dict[Intervention, dict[Delay, dict[JointOutcome, float]]]:
    """Push forward every response law through a finite outcome bijection."""
    _validate_response_table(responses)
    observed_outcomes = {
        outcome
        for delay_table in responses.values()
        for distribution in delay_table.values()
        for outcome in distribution
    }
    if not observed_outcomes.issubset(relabeling):
        raise ValueError("Relabeling must cover every observed joint outcome.")
    images = [relabeling[outcome] for outcome in observed_outcomes]
    if len(set(images)) != len(images):
        raise ValueError("Relabeling must be injective on observed outcomes.")

    transformed: dict[Intervention, dict[Delay, dict[JointOutcome, float]]] = {}
    for intervention, delay_table in responses.items():
        transformed[intervention] = {}
        for delay, distribution in delay_table.items():
            pushed: dict[JointOutcome, float] = {}
            for outcome, probability in distribution.items():
                new_outcome = relabeling[outcome]
                pushed[new_outcome] = pushed.get(new_outcome, 0.0) + probability
            transformed[intervention][delay] = pushed
    return transformed


def _response_dimension(responses: ResponseTable[Intervention, Delay]) -> int:
    first_delay_table = next(iter(responses.values()))
    first_distribution = next(iter(first_delay_table.values()))
    return _joint_dimension(first_distribution)


def _joint_dimension(distribution: JointDistribution) -> int:
    if not distribution:
        raise ValueError("Joint distribution must be nonempty.")
    first_outcome = next(iter(distribution))
    dimension = len(first_outcome)
    if dimension < 1:
        raise ValueError("Joint outcomes must contain at least one block.")
    if any(len(outcome) != dimension for outcome in distribution):
        raise ValueError("All joint outcomes must have the same dimension.")
    total_variation_discrete(distribution, distribution)
    return dimension


def _validate_partition(
    partition: Sequence[Sequence[int]],
    dimension: int,
) -> tuple[tuple[int, ...], ...]:
    blocks = tuple(tuple(block) for block in partition)
    if len(blocks) < 2:
        raise ValueError("Partition must contain at least two nonempty blocks.")
    if any(not block for block in blocks):
        raise ValueError("Partition blocks must be nonempty.")

    flattened = [index for block in blocks for index in block]
    if len(flattened) != len(set(flattened)):
        raise ValueError("Partition blocks must be disjoint.")
    if set(flattened) != set(range(dimension)):
        raise ValueError("Partition must cover every response dimension exactly once.")
    return blocks


def _validate_response_table(
    responses: ResponseTable[Intervention, Delay],
) -> None:
    if not responses:
        raise ValueError("At least one intervention is required.")

    expected_delays: set[Delay] | None = None
    expected_dimension: int | None = None
    for delay_table in responses.values():
        if not delay_table:
            raise ValueError("Every intervention must contain at least one delay.")
        delays = set(delay_table)
        if expected_delays is None:
            expected_delays = delays
        elif delays != expected_delays:
            raise ValueError("Every intervention must use the same delay family.")

        for distribution in delay_table.values():
            dimension = _joint_dimension(distribution)
            if expected_dimension is None:
                expected_dimension = dimension
            elif dimension != expected_dimension:
                raise ValueError("All response laws must use the same joint dimension.")
