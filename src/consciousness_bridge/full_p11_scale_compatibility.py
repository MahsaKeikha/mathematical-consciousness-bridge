"""Assembly certificate for Proposition 30 full P11 scale compatibility.

The certificate combines already-established scale-transport results for response
geometry, directed influence, and partition irreducibility. It is a physical
structure certificate only. It does not assign consciousness, establish physical
completeness, or identify an ontological fusion of fine nodes.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Mapping, Sequence


Node = Hashable


@dataclass(frozen=True)
class P11ScaleCompatibilityCertificate:
    """Simultaneous scale-transport audit for the declared P11 signature."""

    fine_nodes: tuple[Node, ...]
    coarse_nodes: tuple[Node, ...]
    aggregation: tuple[tuple[Node, Node], ...]
    intervention_labels: tuple[Hashable, ...]
    delay_labels: tuple[Hashable, ...]
    partition_semantics_compatible: bool
    source_pair_semantics_compatible: bool
    response_grid_compatible: bool
    common_state_map_declared: bool
    common_reconstruction_family_declared: bool
    geometry_distortion: float
    geometry_bound: float
    influence_distortion: float
    influence_bound: float
    partition_distortion: float
    partition_bound: float

    @property
    def semantic_compatibility_certified(self) -> bool:
        """Return whether all non-numerical scale semantics are aligned."""
        return all(
            (
                self.partition_semantics_compatible,
                self.source_pair_semantics_compatible,
                self.response_grid_compatible,
                self.common_state_map_declared,
                self.common_reconstruction_family_declared,
            )
        )

    @property
    def p11_distortion(self) -> float:
        """Return the largest observed component distortion."""
        return max(
            self.geometry_distortion,
            self.influence_distortion,
            self.partition_distortion,
        )

    @property
    def p11_reconstruction_bound(self) -> float:
        """Return the largest declared component-wise reconstruction bound."""
        return max(self.geometry_bound, self.influence_bound, self.partition_bound)

    @property
    def quantitative_bounds_certified(self) -> bool:
        """Return whether every component distortion lies within its bound."""
        return (
            self.geometry_distortion <= self.geometry_bound
            and self.influence_distortion <= self.influence_bound
            and self.partition_distortion <= self.partition_bound
        )

    @property
    def full_declared_p11_transport_certified(self) -> bool:
        """Return whether semantic and quantitative P11 transport both hold."""
        return self.semantic_compatibility_certified and self.quantitative_bounds_certified

    @property
    def exact_declared_p11_preservation_certified(self) -> bool:
        """Return whether all three declared P11 components are preserved exactly."""
        tolerance = 1e-12
        return self.full_declared_p11_transport_certified and all(
            value <= tolerance
            for value in (
                self.geometry_distortion,
                self.influence_distortion,
                self.partition_distortion,
            )
        )


def p11_scale_compatibility_certificate(
    *,
    fine_nodes: Sequence[Node],
    coarse_nodes: Sequence[Node],
    aggregation: Mapping[Node, Node],
    intervention_labels: Sequence[Hashable],
    delay_labels: Sequence[Hashable],
    partition_semantics_compatible: bool,
    source_pair_semantics_compatible: bool,
    response_grid_compatible: bool,
    common_state_map_declared: bool,
    common_reconstruction_family_declared: bool,
    geometry_distortion: float,
    geometry_bound: float,
    influence_distortion: float,
    influence_bound: float,
    partition_distortion: float,
    partition_bound: float,
) -> P11ScaleCompatibilityCertificate:
    """Build a P30 certificate after checking one shared scale declaration.

    The inputs ``geometry_distortion``, ``influence_distortion``, and
    ``partition_distortion`` are outputs of the P29, P28/P25, and P27/P26
    branches respectively. P30 does not replace those proofs. It certifies that
    they can be assembled only when they refer to one common node quotient,
    experiment grid, state map, and reconstruction declaration.
    """
    fine = tuple(fine_nodes)
    coarse = tuple(coarse_nodes)
    interventions = tuple(intervention_labels)
    delays = tuple(delay_labels)

    _validate_unique_nonempty(fine, "fine_nodes")
    _validate_unique_nonempty(coarse, "coarse_nodes")
    _validate_unique_nonempty(interventions, "intervention_labels")
    _validate_unique_nonempty(delays, "delay_labels")

    if set(aggregation) != set(fine):
        raise ValueError("aggregation must be defined on every and only fine node")
    if any(image not in set(coarse) for image in aggregation.values()):
        raise ValueError("aggregation images must be coarse nodes")
    if set(aggregation.values()) != set(coarse):
        raise ValueError("aggregation must be surjective onto coarse_nodes")

    numeric = {
        "geometry_distortion": geometry_distortion,
        "geometry_bound": geometry_bound,
        "influence_distortion": influence_distortion,
        "influence_bound": influence_bound,
        "partition_distortion": partition_distortion,
        "partition_bound": partition_bound,
    }
    for name, value in numeric.items():
        if value < 0.0:
            raise ValueError(f"{name} must be nonnegative")

    return P11ScaleCompatibilityCertificate(
        fine_nodes=fine,
        coarse_nodes=coarse,
        aggregation=tuple((node, aggregation[node]) for node in fine),
        intervention_labels=interventions,
        delay_labels=delays,
        partition_semantics_compatible=partition_semantics_compatible,
        source_pair_semantics_compatible=source_pair_semantics_compatible,
        response_grid_compatible=response_grid_compatible,
        common_state_map_declared=common_state_map_declared,
        common_reconstruction_family_declared=common_reconstruction_family_declared,
        geometry_distortion=geometry_distortion,
        geometry_bound=geometry_bound,
        influence_distortion=influence_distortion,
        influence_bound=influence_bound,
        partition_distortion=partition_distortion,
        partition_bound=partition_bound,
    )


def uniform_p11_bound(
    *,
    geometry_reconstruction_defect: float,
    influence_reconstruction_defect: float,
    response_reconstruction_defect: float,
    product_reconstruction_defect: float,
) -> float:
    """Return the uniform P30 bound implied by P29, P28/P25, and P27/P26.

    The component bounds are

    ``2 rho_G``, ``2 rho_A``, and ``rho_P + rho_product``.
    """
    defects = (
        geometry_reconstruction_defect,
        influence_reconstruction_defect,
        response_reconstruction_defect,
        product_reconstruction_defect,
    )
    if any(value < 0.0 for value in defects):
        raise ValueError("reconstruction defects must be nonnegative")
    return max(
        2.0 * geometry_reconstruction_defect,
        2.0 * influence_reconstruction_defect,
        response_reconstruction_defect + product_reconstruction_defect,
    )


def _validate_unique_nonempty(values: tuple[Hashable, ...], name: str) -> None:
    if not values:
        raise ValueError(f"{name} must be nonempty")
    if len(set(values)) != len(values):
        raise ValueError(f"{name} must contain unique labels")
