"""Intervention compatibility under physical node aggregation (Proposition 28).

P28 extends P25 and P27 to the source side of the intervention-resolved physical
candidate.  It formalizes when fine matched intervention-pair families descend
through a surjective node map, then certifies directed influence between coarse
source and target nodes.

The theorem preserves only explicitly declared intervention semantics.  Pooling
fine interventions into one aggregate source does not imply a new simultaneous
or physically fused intervention mechanism.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from typing import TypeVar

from consciousness_bridge.causal_structure_coarse_graining import (
    pushforward_distribution,
)
from consciousness_bridge.causal_structure_scale_certification import (
    reconstruction_error,
)
from consciousness_bridge.identifiability import total_variation_discrete
from consciousness_bridge.intervention_causal_structure import (
    ResponseTable,
    marginal_distribution,
)

Intervention = TypeVar("Intervention", bound=Hashable)
Delay = TypeVar("Delay", bound=Hashable)
Node = Hashable
Pair = tuple[Hashable, Hashable]


@dataclass(frozen=True)
class AggregatedInfluenceCertificate:
    """P28 certificate for one aggregate source-target-delay entry."""

    source: Node
    target: Node
    delay: Hashable
    pair_count: int
    fine_block_influence: float
    coarse_influence: float
    reconstruction_defect: float
    distortion_bound: float
    guaranteed_coarse_influence: float
    threshold: float
    fine_edge_present: bool
    coarse_edge_present: bool
    edge_preservation_certified: bool
    no_false_positive_certified: bool


def aggregation_fibers(
    fine_nodes: Sequence[Node],
    coarse_nodes: Sequence[Node],
    aggregation: Mapping[Node, Node],
) -> dict[Node, tuple[Node, ...]]:
    """Validate a surjective node map and return ordered fine-node fibers."""
    fine_nodes = tuple(fine_nodes)
    coarse_nodes = tuple(coarse_nodes)
    if not fine_nodes or not coarse_nodes:
        raise ValueError("Fine and coarse node sets must be nonempty.")
    if len(set(fine_nodes)) != len(fine_nodes):
        raise ValueError("Fine node labels must be unique.")
    if len(set(coarse_nodes)) != len(coarse_nodes):
        raise ValueError("Coarse node labels must be unique.")
    if set(aggregation) != set(fine_nodes):
        raise ValueError("Aggregation map must cover exactly the declared fine nodes.")
    if set(aggregation.values()) != set(coarse_nodes):
        raise ValueError("Aggregation map must be surjective onto coarse nodes.")
    return {
        coarse: tuple(node for node in fine_nodes if aggregation[node] == coarse)
        for coarse in coarse_nodes
    }


def pair_source_images(
    source_pairs: Mapping[Node, Sequence[tuple[Intervention, Intervention]]],
    aggregation: Mapping[Node, Node],
) -> dict[tuple[Intervention, Intervention], frozenset[Node]]:
    """Return the aggregate-source labels attached to every matched pair."""
    missing_sources = set(source_pairs).difference(aggregation)
    if missing_sources:
        raise ValueError("Every fine source with intervention pairs must be aggregated.")

    images: dict[tuple[Intervention, Intervention], set[Node]] = {}
    for source, pairs in source_pairs.items():
        for pair in pairs:
            if len(pair) != 2:
                raise ValueError("Every matched intervention entry must be a pair.")
            images.setdefault(tuple(pair), set()).add(aggregation[source])
    return {pair: frozenset(labels) for pair, labels in images.items()}


def source_pair_families_are_aggregation_compatible(
    source_pairs: Mapping[Node, Sequence[tuple[Intervention, Intervention]]],
    aggregation: Mapping[Node, Node],
) -> bool:
    """Return whether each intervention pair has at most one coarse source label."""
    return all(
        len(images) <= 1
        for images in pair_source_images(source_pairs, aggregation).values()
    )


def descend_source_pairs(
    fine_nodes: Sequence[Node],
    coarse_nodes: Sequence[Node],
    aggregation: Mapping[Node, Node],
    source_pairs: Mapping[Node, Sequence[tuple[Intervention, Intervention]]],
) -> dict[Node, tuple[tuple[Intervention, Intervention], ...]]:
    """Pool fine matched-pair families into compatible aggregate-source families."""
    fibers = aggregation_fibers(fine_nodes, coarse_nodes, aggregation)
    if not source_pair_families_are_aggregation_compatible(source_pairs, aggregation):
        raise ValueError(
            "A matched intervention pair is assigned to fine sources in different "
            "aggregate-source fibers."
        )

    descended: dict[Node, tuple[tuple[Intervention, Intervention], ...]] = {}
    for coarse, fiber in fibers.items():
        seen: set[tuple[Intervention, Intervention]] = set()
        pairs: list[tuple[Intervention, Intervention]] = []
        for source in fiber:
            for pair in source_pairs.get(source, ()):
                normalized = tuple(pair)
                if normalized not in seen:
                    seen.add(normalized)
                    pairs.append(normalized)
        descended[coarse] = tuple(pairs)
    return descended


def _target_fiber_indices(
    fine_nodes: Sequence[Node],
    target_fiber: Sequence[Node],
) -> tuple[int, ...]:
    index = {node: position for position, node in enumerate(fine_nodes)}
    return tuple(index[node] for node in target_fiber)


def _block_response_family(
    responses: ResponseTable[Intervention, Delay],
    pairs: Sequence[tuple[Intervention, Intervention]],
    delay: Delay,
    block_indices: Sequence[int],
) -> dict[Intervention, dict[tuple[Hashable, ...], float]]:
    if not pairs:
        raise ValueError("At least one descended matched intervention pair is required.")

    interventions = {item for pair in pairs for item in pair}
    missing = interventions.difference(responses)
    if missing:
        raise ValueError("Every intervention pair must reference a declared response.")

    family: dict[Intervention, dict[tuple[Hashable, ...], float]] = {}
    for intervention in interventions:
        if delay not in responses[intervention]:
            raise ValueError("Delay must exist for every referenced intervention.")
        family[intervention] = marginal_distribution(
            responses[intervention][delay],
            block_indices,
        )
    return family


def aggregated_directed_influence_certificate(
    responses: ResponseTable[Intervention, Delay],
    source_pairs: Mapping[Node, Sequence[tuple[Intervention, Intervention]]],
    *,
    fine_nodes: Sequence[Node],
    coarse_nodes: Sequence[Node],
    aggregation: Mapping[Node, Node],
    coarse_source: Node,
    coarse_target: Node,
    delay: Delay,
    target_state_map: Mapping[tuple[Hashable, ...], Hashable],
    target_decoder: Mapping[Hashable, Mapping[tuple[Hashable, ...], float]],
    threshold: float = 0.0,
) -> AggregatedInfluenceCertificate:
    """Certify directed influence after source and target node aggregation.

    Fine intervention families attached to constituents of ``coarse_source`` are
    pooled only after satisfying the P28 source-label compatibility condition.
    The fine target response is the joint marginal on the entire aggregation
    fiber of ``coarse_target``. ``target_state_map`` then performs the declared
    within-fiber state aggregation.  No new simultaneous intervention semantics
    are inferred by this construction.
    """
    if threshold < 0.0 or threshold > 1.0:
        raise ValueError("threshold must lie between 0 and 1.")

    fibers = aggregation_fibers(fine_nodes, coarse_nodes, aggregation)
    if coarse_source not in fibers or coarse_target not in fibers:
        raise ValueError("Source and target must be declared coarse nodes.")

    coarse_pairs = descend_source_pairs(
        fine_nodes,
        coarse_nodes,
        aggregation,
        source_pairs,
    )
    pairs = coarse_pairs[coarse_source]
    target_indices = _target_fiber_indices(fine_nodes, fibers[coarse_target])
    family = _block_response_family(responses, pairs, delay, target_indices)

    missing_outcomes = {
        outcome
        for distribution in family.values()
        for outcome in distribution
    }.difference(target_state_map)
    if missing_outcomes:
        raise ValueError("target_state_map must cover every observed target-fiber state.")

    fine_distances: list[float] = []
    coarse_distances: list[float] = []
    for first, second in pairs:
        first_fine = family[first]
        second_fine = family[second]
        fine_distances.append(total_variation_discrete(first_fine, second_fine))

        first_coarse = pushforward_distribution(first_fine, target_state_map)
        second_coarse = pushforward_distribution(second_fine, target_state_map)
        coarse_distances.append(
            total_variation_discrete(first_coarse, second_coarse)
        )

    fine_influence = max(fine_distances)
    coarse_influence = max(coarse_distances)
    reconstruction_defect = max(
        reconstruction_error(distribution, target_state_map, target_decoder)
        for distribution in family.values()
    )
    distortion_bound = min(1.0, 2.0 * reconstruction_defect)
    guaranteed_coarse = max(0.0, fine_influence - distortion_bound)

    tolerance = 1e-12
    if coarse_influence > fine_influence + tolerance:
        raise RuntimeError("TV contraction was violated by the target aggregation map.")
    if fine_influence > coarse_influence + distortion_bound + tolerance:
        raise RuntimeError("P18 reconstruction distortion bound was violated.")

    return AggregatedInfluenceCertificate(
        source=coarse_source,
        target=coarse_target,
        delay=delay,
        pair_count=len(pairs),
        fine_block_influence=fine_influence,
        coarse_influence=coarse_influence,
        reconstruction_defect=reconstruction_defect,
        distortion_bound=distortion_bound,
        guaranteed_coarse_influence=guaranteed_coarse,
        threshold=threshold,
        fine_edge_present=fine_influence > threshold,
        coarse_edge_present=coarse_influence > threshold,
        edge_preservation_certified=fine_influence > threshold + distortion_bound,
        no_false_positive_certified=coarse_influence <= fine_influence + tolerance,
    )
