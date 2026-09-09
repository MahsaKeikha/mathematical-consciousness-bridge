"""Scale certification for P11 partition irreducibility (Proposition 26).

The theorem concerns physical response distributions only.  It assumes a declared
fine partition, a block-compatible deterministic observation map, and a
fiber-consistent reconstruction decoder.  It does not identify partition
irreducibility with consciousness and does not model genuine physical fusion.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from itertools import product
from typing import TypeVar

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

FineValue = TypeVar("FineValue", bound=Hashable)
CoarseValue = TypeVar("CoarseValue", bound=Hashable)
JointOutcome = tuple[Hashable, ...]
Distribution = Mapping[JointOutcome, float]


@dataclass(frozen=True)
class PartitionScaleCertificate:
    """P26 scale certificate for one response law and one declared partition."""

    fine_irreducibility: float
    coarse_irreducibility: float
    response_reconstruction_error: float
    product_reconstruction_error: float
    additive_loss_bound: float
    exact_preservation_certified: bool


def block_compatible_coarse_map(
    fine_support: Sequence[JointOutcome],
    block_maps: Sequence[Mapping[Hashable, Hashable]],
) -> dict[JointOutcome, JointOutcome]:
    """Build a coordinatewise deterministic coarse map on a declared fine support."""
    if not fine_support:
        raise ValueError("Fine support must be nonempty.")
    dimension = len(fine_support[0])
    if dimension < 1:
        raise ValueError("Joint outcomes must contain at least one coordinate.")
    if len(block_maps) != dimension:
        raise ValueError("One coordinate map is required per joint coordinate.")
    if any(len(outcome) != dimension for outcome in fine_support):
        raise ValueError("All fine outcomes must have the same dimension.")

    coarse_map: dict[JointOutcome, JointOutcome] = {}
    for outcome in fine_support:
        coarse: list[Hashable] = []
        for index, value in enumerate(outcome):
            mapping = block_maps[index]
            if value not in mapping:
                raise ValueError("Coordinate map must cover every fine support value.")
            coarse.append(mapping[value])
        coarse_map[outcome] = tuple(coarse)
    return coarse_map


def partition_product_distribution(
    distribution: Distribution,
    partition: Sequence[Sequence[int]],
) -> dict[JointOutcome, float]:
    """Return the product of block marginals for the declared partition."""
    return productized_partition_distribution(distribution, partition)


def coarse_partition_product_distribution(
    distribution: Distribution,
    partition: Sequence[Sequence[int]],
    coarse_map: Mapping[JointOutcome, JointOutcome],
) -> dict[JointOutcome, float]:
    """Coarse-grain the fine partition-product law."""
    product_law = partition_product_distribution(distribution, partition)
    return pushforward_distribution(product_law, coarse_map)


def partition_irreducibility(
    distribution: Distribution,
    partition: Sequence[Sequence[int]],
) -> float:
    """Return TV distance from the product of declared block marginals."""
    product_law = partition_product_distribution(distribution, partition)
    return total_variation_discrete(distribution, product_law)


def coarse_partition_irreducibility(
    distribution: Distribution,
    partition: Sequence[Sequence[int]],
    coarse_map: Mapping[JointOutcome, JointOutcome],
) -> float:
    """Return coarse-scale irreducibility for a block-compatible observation map.

    The coarse product reference is defined as the pushforward of the fine
    partition-product law. For a genuinely coordinatewise map this equals the
    product of coarse block marginals, so productization commutes with coarse
    observation.
    """
    coarse_response = pushforward_distribution(distribution, coarse_map)
    coarse_product = coarse_partition_product_distribution(
        distribution,
        partition,
        coarse_map,
    )
    return total_variation_discrete(coarse_response, coarse_product)


def partition_scale_loss(
    distribution: Distribution,
    partition: Sequence[Sequence[int]],
    coarse_map: Mapping[JointOutcome, JointOutcome],
) -> tuple[float, float, float]:
    """Return fine irreducibility, coarse irreducibility, and observed loss."""
    fine = partition_irreducibility(distribution, partition)
    coarse = coarse_partition_irreducibility(distribution, partition, coarse_map)
    return fine, coarse, fine - coarse


def partition_scale_certificate(
    distribution: Distribution,
    partition: Sequence[Sequence[int]],
    coarse_map: Mapping[JointOutcome, JointOutcome],
    decoder: Mapping[JointOutcome, Mapping[JointOutcome, float]],
) -> PartitionScaleCertificate:
    """Build the P26 contraction and reconstruction-controlled loss certificate."""
    product_law = partition_product_distribution(distribution, partition)
    fine = total_variation_discrete(distribution, product_law)
    coarse_response = pushforward_distribution(distribution, coarse_map)
    coarse_product = pushforward_distribution(product_law, coarse_map)
    coarse = total_variation_discrete(coarse_response, coarse_product)

    response_error = reconstruction_error(distribution, coarse_map, decoder)
    product_error = reconstruction_error(product_law, coarse_map, decoder)
    bound = response_error + product_error

    return PartitionScaleCertificate(
        fine_irreducibility=fine,
        coarse_irreducibility=coarse,
        response_reconstruction_error=response_error,
        product_reconstruction_error=product_error,
        additive_loss_bound=bound,
        exact_preservation_certified=bound == 0.0,
    )


def threshold_irreducibility_preserved(
    certificate: PartitionScaleCertificate,
    threshold: float,
) -> bool:
    """Certify that a fine irreducibility margin survives coarse observation."""
    if threshold < 0.0:
        raise ValueError("threshold must be nonnegative.")
    return (
        certificate.fine_irreducibility
        > threshold + certificate.additive_loss_bound
    )


def product_decoder_from_coordinate_decoders(
    coarse_outcomes: Sequence[JointOutcome],
    coordinate_decoders: Sequence[
        Mapping[Hashable, Mapping[Hashable, float]]
    ],
) -> dict[JointOutcome, dict[JointOutcome, float]]:
    """Construct a factorized decoder for a coordinatewise coarse state.

    This helper is optional but makes the block-compatibility assumption explicit:
    each coarse coordinate is decoded independently inside its own fine fiber.
    """
    if not coarse_outcomes:
        raise ValueError("Coarse outcomes must be nonempty.")
    dimension = len(coarse_outcomes[0])
    if len(coordinate_decoders) != dimension:
        raise ValueError("One coordinate decoder is required per coarse coordinate.")
    if any(len(outcome) != dimension for outcome in coarse_outcomes):
        raise ValueError("All coarse outcomes must have the same dimension.")

    decoder: dict[JointOutcome, dict[JointOutcome, float]] = {}
    for coarse_outcome in coarse_outcomes:
        choices: list[list[tuple[Hashable, float]]] = []
        for index, coarse_value in enumerate(coarse_outcome):
            coordinate = coordinate_decoders[index]
            if coarse_value not in coordinate:
                raise ValueError("Coordinate decoder must cover every coarse value.")
            conditional = coordinate[coarse_value]
            if not conditional:
                raise ValueError("Coordinate decoder conditionals must be nonempty.")
            choices.append(list(conditional.items()))

        joint: dict[JointOutcome, float] = {}
        for selected in product(*choices):
            fine_outcome = tuple(value for value, _ in selected)
            probability = 1.0
            for _, factor in selected:
                probability *= factor
            joint[fine_outcome] = joint.get(fine_outcome, 0.0) + probability
        decoder[coarse_outcome] = joint
    return decoder
