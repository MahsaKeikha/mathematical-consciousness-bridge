"""Response-geometry transport under node aggregation (Proposition 29).

P29 extends the P17/P18 scale program to the complete P11 response geometry while
holding the declared intervention labels and delay semantics fixed.  A global
aggregate-state map may reduce the node set and response alphabet, but it does
not merge interventions or resample time.

The theorem is purely physical and operational.  It does not establish physical
completeness, experiential structure, or consciousness.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from itertools import combinations
from typing import TypeVar

from consciousness_bridge.causal_structure_coarse_graining import (
    pushforward_distribution,
)
from consciousness_bridge.causal_structure_scale_certification import (
    reconstruction_error,
)
from consciousness_bridge.identifiability import total_variation_discrete
from consciousness_bridge.intervention_causal_structure import ResponseTable
from consciousness_bridge.partition_lattice_node_aggregation import (
    aggregation_compatible_coarse_map,
)

Intervention = TypeVar("Intervention", bound=Hashable)
Delay = TypeVar("Delay", bound=Hashable)
Node = Hashable
JointOutcome = tuple[Hashable, ...]
Distribution = Mapping[JointOutcome, float]
GeometryKey = tuple[Hashable, Hashable, Hashable]


@dataclass(frozen=True)
class ResponseGeometryScaleCertificate:
    """P29 certificate for one declared intervention and delay family."""

    pair_count: int
    delay_count: int
    fine_diameter: float
    coarse_diameter: float
    max_geometry_loss: float
    reconstruction_defect: float
    uniform_distortion_bound: float
    exact_geometry_preservation_certified: bool


def declared_response_family(
    responses: ResponseTable[Intervention, Delay],
    interventions: Sequence[Intervention],
    delays: Sequence[Delay],
) -> dict[tuple[Intervention, Delay], Distribution]:
    """Return the exact response family on the declared intervention-delay grid."""
    interventions = tuple(interventions)
    delays = tuple(delays)
    if not interventions:
        raise ValueError("At least one intervention is required.")
    if not delays:
        raise ValueError("At least one delay is required.")
    if len(set(interventions)) != len(interventions):
        raise ValueError("Intervention labels must be unique.")
    if len(set(delays)) != len(delays):
        raise ValueError("Delay labels must be unique.")

    family: dict[tuple[Intervention, Delay], Distribution] = {}
    for intervention in interventions:
        if intervention not in responses:
            raise ValueError("Every declared intervention must have response data.")
        for delay in delays:
            if delay not in responses[intervention]:
                raise ValueError(
                    "Every declared intervention-delay cell must have response data."
                )
            family[(intervention, delay)] = responses[intervention][delay]
    return family


def response_geometry_over_grid(
    family: Mapping[tuple[Intervention, Delay], Distribution],
    interventions: Sequence[Intervention],
    delays: Sequence[Delay],
) -> dict[GeometryKey, float]:
    """Return pairwise intervention-response TV geometry at every declared delay."""
    interventions = tuple(interventions)
    delays = tuple(delays)
    geometry: dict[GeometryKey, float] = {}
    for delay in delays:
        for first, second in combinations(interventions, 2):
            geometry[(first, second, delay)] = total_variation_discrete(
                family[(first, delay)],
                family[(second, delay)],
            )
    return geometry


def pushforward_response_family(
    family: Mapping[tuple[Intervention, Delay], Distribution],
    coarse_map: Mapping[JointOutcome, JointOutcome],
) -> dict[tuple[Intervention, Delay], dict[JointOutcome, float]]:
    """Push every response law through one declared aggregate-state map."""
    return {
        key: pushforward_distribution(distribution, coarse_map)
        for key, distribution in family.items()
    }


def response_geometry_distortion(
    fine_geometry: Mapping[GeometryKey, float],
    coarse_geometry: Mapping[GeometryKey, float],
) -> dict[GeometryKey, float]:
    """Return fine-minus-coarse TV loss for every geometry entry."""
    if set(fine_geometry) != set(coarse_geometry):
        raise ValueError("Fine and coarse geometries must use the same indexed grid.")
    distortion = {
        key: fine_geometry[key] - coarse_geometry[key]
        for key in fine_geometry
    }
    if any(value < -1e-12 for value in distortion.values()):
        raise RuntimeError("Coarse response geometry violated TV contraction.")
    return {key: max(0.0, value) for key, value in distortion.items()}


def response_geometry_node_aggregation_certificate(
    responses: ResponseTable[Intervention, Delay],
    *,
    interventions: Sequence[Intervention],
    delays: Sequence[Delay],
    fine_nodes: Sequence[Node],
    coarse_nodes: Sequence[Node],
    aggregation: Mapping[Node, Node],
    aggregate_maps: Mapping[Node, Mapping[tuple[Hashable, ...], Hashable]],
    decoder: Mapping[JointOutcome, Mapping[JointOutcome, float]],
) -> ResponseGeometryScaleCertificate:
    """Certify P11 response-geometry transport through node aggregation.

    Intervention labels and delay labels are required to be identical at the fine
    and coarse levels.  Only the physical response state is aggregated here.
    """
    family = declared_response_family(responses, interventions, delays)
    fine_support = tuple(
        {
            outcome
            for distribution in family.values()
            for outcome in distribution
        }
    )
    coarse_map = aggregation_compatible_coarse_map(
        fine_support,
        fine_nodes,
        coarse_nodes,
        aggregation,
        aggregate_maps,
    )
    coarse_family = pushforward_response_family(family, coarse_map)

    fine_geometry = response_geometry_over_grid(family, interventions, delays)
    coarse_geometry = response_geometry_over_grid(
        coarse_family,
        interventions,
        delays,
    )
    distortion = response_geometry_distortion(fine_geometry, coarse_geometry)

    reconstruction_defect = max(
        reconstruction_error(distribution, coarse_map, decoder)
        for distribution in family.values()
    )
    uniform_bound = min(1.0, 2.0 * reconstruction_defect)

    for loss in distortion.values():
        if loss > uniform_bound + 1e-12:
            raise RuntimeError("P18 uniform response-geometry bound was violated.")

    fine_diameter = max(fine_geometry.values(), default=0.0)
    coarse_diameter = max(coarse_geometry.values(), default=0.0)
    max_loss = max(distortion.values(), default=0.0)

    return ResponseGeometryScaleCertificate(
        pair_count=len(tuple(combinations(tuple(interventions), 2))),
        delay_count=len(tuple(delays)),
        fine_diameter=fine_diameter,
        coarse_diameter=coarse_diameter,
        max_geometry_loss=max_loss,
        reconstruction_defect=reconstruction_defect,
        uniform_distortion_bound=uniform_bound,
        exact_geometry_preservation_certified=reconstruction_defect == 0.0,
    )


def geometry_threshold_preserved(
    fine_distance: float,
    reconstruction_defect: float,
    threshold: float,
) -> bool:
    """Certify that one fine response-geometry separation survives aggregation."""
    for name, value in (
        ("fine_distance", fine_distance),
        ("reconstruction_defect", reconstruction_defect),
        ("threshold", threshold),
    ):
        if value < 0.0 or value > 1.0:
            raise ValueError(f"{name} must lie between 0 and 1.")
    return fine_distance > threshold + 2.0 * reconstruction_defect
