"""Scale-sufficiency tools for Proposition 18.

The module quantifies when a deterministic coarse response description remains
sufficient for a declared finite family of fine response laws.  A stochastic
decoder reconstructs fine laws inside each coarse fiber.  Small reconstruction
error then certifies small distortion of total-variation response geometry.

The result concerns physical response laws only.  It does not assign an
experiential meaning to a scale or imply that arbitrary coarse-graining
preserves the full intervention-resolved causal structure.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from itertools import combinations
from typing import TypeVar

from consciousness_bridge.causal_structure_coarse_graining import (
    pushforward_distribution,
)
from consciousness_bridge.identifiability import total_variation_discrete

FineOutcome = TypeVar("FineOutcome", bound=Hashable)
CoarseOutcome = TypeVar("CoarseOutcome", bound=Hashable)
LawLabel = TypeVar("LawLabel", bound=Hashable)


@dataclass(frozen=True)
class ScaleSeparationCertificate:
    """Finite-family separation certificate associated with Proposition 18."""

    fine_min_separation: float
    coarse_min_separation: float
    reconstruction_defect: float
    guaranteed_coarse_separation: float
    certified_identifiable: bool


def _validate_fiber_decoder(
    decoder: Mapping[CoarseOutcome, Mapping[FineOutcome, float]],
    coarse_map: Mapping[FineOutcome, CoarseOutcome],
) -> None:
    if not decoder:
        raise ValueError("Decoder must be nonempty.")

    for coarse_outcome, conditional in decoder.items():
        if not conditional:
            raise ValueError("Every decoder conditional must be nonempty.")
        total_variation_discrete(conditional, conditional)
        for fine_outcome, probability in conditional.items():
            if probability <= 0.0:
                continue
            if fine_outcome not in coarse_map:
                raise ValueError("Decoder output must be covered by the coarse map.")
            if coarse_map[fine_outcome] != coarse_outcome:
                raise ValueError(
                    "Decoder support must remain inside the corresponding coarse fiber."
                )


def decode_distribution(
    coarse_distribution: Mapping[CoarseOutcome, float],
    decoder: Mapping[CoarseOutcome, Mapping[FineOutcome, float]],
    coarse_map: Mapping[FineOutcome, CoarseOutcome],
) -> dict[FineOutcome, float]:
    """Decode one coarse law through a fiber-consistent stochastic decoder."""
    if not coarse_distribution:
        raise ValueError("Coarse distribution must be nonempty.")
    total_variation_discrete(coarse_distribution, coarse_distribution)
    _validate_fiber_decoder(decoder, coarse_map)
    if not set(coarse_distribution).issubset(decoder):
        raise ValueError("Decoder must cover every observed coarse outcome.")

    reconstructed: dict[FineOutcome, float] = {}
    for coarse_outcome, coarse_probability in coarse_distribution.items():
        for fine_outcome, conditional_probability in decoder[coarse_outcome].items():
            reconstructed[fine_outcome] = reconstructed.get(fine_outcome, 0.0) + (
                coarse_probability * conditional_probability
            )

    total_variation_discrete(reconstructed, reconstructed)
    return reconstructed


def reconstruct_distribution(
    fine_distribution: Mapping[FineOutcome, float],
    coarse_map: Mapping[FineOutcome, CoarseOutcome],
    decoder: Mapping[CoarseOutcome, Mapping[FineOutcome, float]],
) -> dict[FineOutcome, float]:
    """Apply coarse-graining followed by stochastic fine-scale reconstruction."""
    coarse_distribution = pushforward_distribution(fine_distribution, coarse_map)
    return decode_distribution(coarse_distribution, decoder, coarse_map)


def reconstruction_error(
    fine_distribution: Mapping[FineOutcome, float],
    coarse_map: Mapping[FineOutcome, CoarseOutcome],
    decoder: Mapping[CoarseOutcome, Mapping[FineOutcome, float]],
) -> float:
    """Return TV error between a fine law and its coarse/decode reconstruction."""
    reconstructed = reconstruct_distribution(fine_distribution, coarse_map, decoder)
    return total_variation_discrete(fine_distribution, reconstructed)


def uniform_reconstruction_defect(
    family: Mapping[LawLabel, Mapping[FineOutcome, float]],
    coarse_map: Mapping[FineOutcome, CoarseOutcome],
    decoder: Mapping[CoarseOutcome, Mapping[FineOutcome, float]],
) -> float:
    """Return the maximum reconstruction error over a declared response family."""
    if not family:
        raise ValueError("Response family must be nonempty.")
    return max(
        reconstruction_error(distribution, coarse_map, decoder)
        for distribution in family.values()
    )


def pairwise_scale_distortion(
    first: Mapping[FineOutcome, float],
    second: Mapping[FineOutcome, float],
    coarse_map: Mapping[FineOutcome, CoarseOutcome],
    decoder: Mapping[CoarseOutcome, Mapping[FineOutcome, float]],
) -> tuple[float, float, float]:
    """Return fine distance, coarse distance, and the P18 additive error bound."""
    fine_distance = total_variation_discrete(first, second)
    coarse_distance = total_variation_discrete(
        pushforward_distribution(first, coarse_map),
        pushforward_distribution(second, coarse_map),
    )
    additive_bound = reconstruction_error(first, coarse_map, decoder) + (
        reconstruction_error(second, coarse_map, decoder)
    )
    return fine_distance, coarse_distance, additive_bound


def minimum_pairwise_separation(
    family: Mapping[LawLabel, Mapping[FineOutcome, float]],
) -> float:
    """Return the minimum TV distance over distinct laws in a finite family."""
    if len(family) < 2:
        raise ValueError("At least two response laws are required.")
    return min(
        total_variation_discrete(family[first], family[second])
        for first, second in combinations(family, 2)
    )


def scale_separation_certificate(
    family: Mapping[LawLabel, Mapping[FineOutcome, float]],
    coarse_map: Mapping[FineOutcome, CoarseOutcome],
    decoder: Mapping[CoarseOutcome, Mapping[FineOutcome, float]],
) -> ScaleSeparationCertificate:
    """Build the finite-family P18 scale-identifiability certificate."""
    fine_min = minimum_pairwise_separation(family)
    coarse_family = {
        label: pushforward_distribution(distribution, coarse_map)
        for label, distribution in family.items()
    }
    coarse_min = minimum_pairwise_separation(coarse_family)
    defect = uniform_reconstruction_defect(family, coarse_map, decoder)
    guaranteed = max(0.0, fine_min - 2.0 * defect)

    return ScaleSeparationCertificate(
        fine_min_separation=fine_min,
        coarse_min_separation=coarse_min,
        reconstruction_defect=defect,
        guaranteed_coarse_separation=guaranteed,
        certified_identifiable=fine_min > 2.0 * defect,
    )
