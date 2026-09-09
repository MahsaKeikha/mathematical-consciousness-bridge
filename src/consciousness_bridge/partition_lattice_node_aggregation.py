"""Partition-lattice transport under node aggregation (Proposition 27).

This module formalizes when a partition of fine physical nodes has a well-defined
coarse counterpart under a surjective node-aggregation map.  It also connects
that combinatorial criterion to P11 partition irreducibility and P18
reconstruction bounds.

The result concerns declared physical node and observation structure.  It does
not model genuine physical fusion, establish physical completeness, or assign
an experiential meaning to any partition.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass

from consciousness_bridge.causal_structure_coarse_graining import (
    pushforward_distribution,
)
from consciousness_bridge.causal_structure_scale_certification import (
    reconstruction_error,
)
from consciousness_bridge.identifiability import total_variation_discrete
from consciousness_bridge.intervention_causal_structure import (
    productized_partition_distribution,
)

Node = Hashable
JointOutcome = tuple[Hashable, ...]
Distribution = Mapping[JointOutcome, float]
Partition = tuple[frozenset[Node], ...]


@dataclass(frozen=True)
class NodeAggregationPartitionCertificate:
    """P27 irreducibility certificate for one descendable fine partition."""

    fine_irreducibility: float
    coarse_irreducibility: float
    product_commutation_error: float
    response_reconstruction_error: float
    product_reconstruction_error: float
    additive_loss_bound: float
    exact_preservation_certified: bool


def canonical_partition(
    partition: Sequence[Sequence[Node] | frozenset[Node]],
    universe: Sequence[Node] | frozenset[Node],
) -> Partition:
    """Validate and canonically order a finite set partition."""
    universe_set = frozenset(universe)
    if not universe_set:
        raise ValueError("Partition universe must be nonempty.")

    blocks = tuple(frozenset(block) for block in partition)
    if not blocks:
        raise ValueError("Partition must contain at least one block.")
    if any(not block for block in blocks):
        raise ValueError("Partition blocks must be nonempty.")

    flattened: set[Node] = set()
    for block in blocks:
        if flattened.intersection(block):
            raise ValueError("Partition blocks must be pairwise disjoint.")
        flattened.update(block)
    if flattened != set(universe_set):
        raise ValueError("Partition must cover the declared universe exactly.")

    return tuple(sorted(blocks, key=lambda block: tuple(sorted(map(repr, block)))))


def aggregation_fibers(
    aggregation: Mapping[Node, Node],
) -> dict[Node, frozenset[Node]]:
    """Return the nonempty fine-node fibers of a node-aggregation map."""
    if not aggregation:
        raise ValueError("Aggregation map must be nonempty.")
    fibers: dict[Node, set[Node]] = {}
    for fine, coarse in aggregation.items():
        fibers.setdefault(coarse, set()).add(fine)
    return {coarse: frozenset(fine) for coarse, fine in fibers.items()}


def is_aggregation_saturated(
    fine_partition: Sequence[Sequence[Node] | frozenset[Node]],
    aggregation: Mapping[Node, Node],
) -> bool:
    """Return whether every aggregation fiber lies within one partition block."""
    partition = canonical_partition(fine_partition, tuple(aggregation))
    for fiber in aggregation_fibers(aggregation).values():
        if not any(fiber.issubset(block) for block in partition):
            return False
    return True


def descend_partition(
    fine_partition: Sequence[Sequence[Node] | frozenset[Node]],
    aggregation: Mapping[Node, Node],
) -> Partition:
    """Descend an aggregation-saturated fine partition to coarse nodes."""
    partition = canonical_partition(fine_partition, tuple(aggregation))
    if not is_aggregation_saturated(partition, aggregation):
        raise ValueError(
            "Fine partition is not aggregation saturated and has no coarse descent."
        )

    coarse_universe = frozenset(aggregation.values())
    images = [frozenset(aggregation[node] for node in block) for block in partition]
    return canonical_partition(images, coarse_universe)


def lift_partition(
    coarse_partition: Sequence[Sequence[Node] | frozenset[Node]],
    aggregation: Mapping[Node, Node],
) -> Partition:
    """Lift a coarse partition to the unique aggregation-saturated fine partition."""
    fibers = aggregation_fibers(aggregation)
    coarse = canonical_partition(coarse_partition, tuple(fibers))
    lifted = [
        frozenset(
            fine
            for coarse_node in block
            for fine in fibers[coarse_node]
        )
        for block in coarse
    ]
    return canonical_partition(lifted, tuple(aggregation))


def partition_refines(
    finer: Sequence[Sequence[Node] | frozenset[Node]],
    coarser: Sequence[Sequence[Node] | frozenset[Node]],
    universe: Sequence[Node] | frozenset[Node],
) -> bool:
    """Return whether every block of ``finer`` lies in a block of ``coarser``."""
    fine = canonical_partition(finer, universe)
    coarse = canonical_partition(coarser, universe)
    return all(any(block.issubset(container) for container in coarse) for block in fine)


def partition_meet(
    first: Sequence[Sequence[Node] | frozenset[Node]],
    second: Sequence[Sequence[Node] | frozenset[Node]],
    universe: Sequence[Node] | frozenset[Node],
) -> Partition:
    """Return the common-refinement meet of two partitions."""
    left = canonical_partition(first, universe)
    right = canonical_partition(second, universe)
    intersections = [
        first_block.intersection(second_block)
        for first_block in left
        for second_block in right
        if first_block.intersection(second_block)
    ]
    return canonical_partition(intersections, universe)


def partition_join(
    first: Sequence[Sequence[Node] | frozenset[Node]],
    second: Sequence[Sequence[Node] | frozenset[Node]],
    universe: Sequence[Node] | frozenset[Node],
) -> Partition:
    """Return the common-coarsening join of two partitions."""
    nodes = tuple(universe)
    left = canonical_partition(first, nodes)
    right = canonical_partition(second, nodes)

    parent = {node: node for node in nodes}

    def find(node: Node) -> Node:
        root = node
        while parent[root] != root:
            root = parent[root]
        while parent[node] != node:
            next_node = parent[node]
            parent[node] = root
            node = next_node
        return root

    def union(first_node: Node, second_node: Node) -> None:
        first_root = find(first_node)
        second_root = find(second_node)
        if first_root != second_root:
            parent[second_root] = first_root

    for partition in (left, right):
        for block in partition:
            block_nodes = tuple(block)
            anchor = block_nodes[0]
            for node in block_nodes[1:]:
                union(anchor, node)

    components: dict[Node, set[Node]] = {}
    for node in nodes:
        components.setdefault(find(node), set()).add(node)
    return canonical_partition(tuple(components.values()), nodes)


def aggregation_compatible_coarse_map(
    fine_support: Sequence[JointOutcome],
    fine_nodes: Sequence[Node],
    coarse_nodes: Sequence[Node],
    aggregation: Mapping[Node, Node],
    aggregate_maps: Mapping[Node, Mapping[tuple[Hashable, ...], Hashable]],
) -> dict[JointOutcome, JointOutcome]:
    """Build a coarse outcome map whose coordinates respect aggregation fibers."""
    fine_nodes = tuple(fine_nodes)
    coarse_nodes = tuple(coarse_nodes)
    if not fine_support:
        raise ValueError("Fine support must be nonempty.")
    if len(set(fine_nodes)) != len(fine_nodes):
        raise ValueError("Fine node labels must be unique.")
    if len(set(coarse_nodes)) != len(coarse_nodes):
        raise ValueError("Coarse node labels must be unique.")
    if set(aggregation) != set(fine_nodes):
        raise ValueError("Aggregation map must cover exactly the declared fine nodes.")
    if set(aggregation.values()) != set(coarse_nodes):
        raise ValueError("Aggregation map must be surjective onto coarse nodes.")
    if set(aggregate_maps) != set(coarse_nodes):
        raise ValueError("One aggregate state map is required per coarse node.")
    if any(len(outcome) != len(fine_nodes) for outcome in fine_support):
        raise ValueError("Fine outcomes must match the declared fine-node dimension.")

    fine_index = {node: index for index, node in enumerate(fine_nodes)}
    fibers = {
        coarse: tuple(node for node in fine_nodes if aggregation[node] == coarse)
        for coarse in coarse_nodes
    }

    result: dict[JointOutcome, JointOutcome] = {}
    for outcome in fine_support:
        coarse_outcome: list[Hashable] = []
        for coarse in coarse_nodes:
            fiber_value = tuple(outcome[fine_index[node]] for node in fibers[coarse])
            state_map = aggregate_maps[coarse]
            if fiber_value not in state_map:
                raise ValueError(
                    "Aggregate state map must cover every observed aggregation-fiber state."
                )
            coarse_outcome.append(state_map[fiber_value])
        result[outcome] = tuple(coarse_outcome)
    return result


def _partition_indices(
    partition: Partition,
    nodes: Sequence[Node],
) -> tuple[tuple[int, ...], ...]:
    index = {node: position for position, node in enumerate(nodes)}
    return tuple(tuple(sorted(index[node] for node in block)) for block in partition)


def node_aggregation_partition_certificate(
    distribution: Distribution,
    fine_nodes: Sequence[Node],
    fine_partition: Sequence[Sequence[Node] | frozenset[Node]],
    aggregation: Mapping[Node, Node],
    coarse_nodes: Sequence[Node],
    coarse_map: Mapping[JointOutcome, JointOutcome],
    decoder: Mapping[JointOutcome, Mapping[JointOutcome, float]],
) -> NodeAggregationPartitionCertificate:
    """Certify P11 partition irreducibility through a genuine node aggregation."""
    fine_nodes = tuple(fine_nodes)
    coarse_nodes = tuple(coarse_nodes)
    fine = canonical_partition(fine_partition, fine_nodes)
    coarse = descend_partition(fine, aggregation)

    fine_indices = _partition_indices(fine, fine_nodes)
    coarse_indices = _partition_indices(coarse, coarse_nodes)
    fine_product = productized_partition_distribution(distribution, fine_indices)

    coarse_response = pushforward_distribution(distribution, coarse_map)
    pushed_product = pushforward_distribution(fine_product, coarse_map)
    coarse_product = productized_partition_distribution(coarse_response, coarse_indices)

    commutation_error = total_variation_discrete(pushed_product, coarse_product)
    if commutation_error > 1e-12:
        raise ValueError(
            "Coarse state map is not compatible with the descended partition product."
        )

    fine_irreducibility = total_variation_discrete(distribution, fine_product)
    coarse_irreducibility = total_variation_discrete(coarse_response, coarse_product)
    response_error = reconstruction_error(distribution, coarse_map, decoder)
    product_error = reconstruction_error(fine_product, coarse_map, decoder)
    bound = response_error + product_error

    return NodeAggregationPartitionCertificate(
        fine_irreducibility=fine_irreducibility,
        coarse_irreducibility=coarse_irreducibility,
        product_commutation_error=commutation_error,
        response_reconstruction_error=response_error,
        product_reconstruction_error=product_error,
        additive_loss_bound=bound,
        exact_preservation_certified=bound == 0.0,
    )
