"""Directed-influence scale certification for Proposition 25.

P25 extends the P18 reconstruction argument to the P11 directed-influence
component.  For one declared source, target, and delay, the fine influence is
the supremum of total-variation distances between matched intervention-
conditioned target marginals.  A deterministic coarse observation of that
target contracts every pairwise distance.  If a fiber-consistent stochastic
decoder reconstructs all target response laws with uniform TV defect rho, then

    0 <= A_fine - A_coarse <= 2 rho.

The result concerns a declared physical intervention family and target response
variable.  It does not by itself certify the full P11 causal structure, physical
completeness, or any experiential interpretation.
"""

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
    InterventionPairs,
    ResponseTable,
    marginal_distribution,
)

Intervention = TypeVar("Intervention", bound=Hashable)
Delay = TypeVar("Delay", bound=Hashable)
FineOutcome = TypeVar("FineOutcome", bound=Hashable)
CoarseOutcome = TypeVar("CoarseOutcome", bound=Hashable)


@dataclass(frozen=True)
class DirectedInfluenceScaleCertificate:
    """P25 certificate for one source-target-delay directed-influence entry."""

    source: int
    target: int
    delay: Hashable
    fine_influence: float
    coarse_influence: float
    reconstruction_defect: float
    distortion_bound: float
    guaranteed_coarse_influence: float
    threshold: float
    coarse_edge_present: bool
    fine_edge_present: bool
    edge_preservation_certified: bool
    no_false_positive_certified: bool


def _validate_threshold(threshold: float) -> None:
    if threshold < 0.0 or threshold > 1.0:
        raise ValueError("threshold must lie between 0 and 1")


def _target_response_family(
    responses: ResponseTable[Intervention, Delay],
    pairs: Sequence[tuple[Intervention, Intervention]],
    delay: Delay,
    target: int,
) -> dict[Intervention, dict[tuple[Hashable, ...], float]]:
    if target < 0:
        raise ValueError("target must be nonnegative")
    if not pairs:
        raise ValueError("At least one matched intervention pair is required")

    interventions = {item for pair in pairs for item in pair}
    missing = interventions.difference(responses)
    if missing:
        raise ValueError("Every intervention pair must reference a declared response")

    family: dict[Intervention, dict[tuple[Hashable, ...], float]] = {}
    for intervention in interventions:
        delay_table = responses[intervention]
        if delay not in delay_table:
            raise ValueError("delay must be available for every referenced intervention")
        family[intervention] = marginal_distribution(
            delay_table[delay],
            (target,),
        )
    return family


def directed_influence_scale_certificate(
    responses: ResponseTable[Intervention, Delay],
    source_pairs: InterventionPairs[Intervention],
    *,
    source: int,
    target: int,
    delay: Delay,
    coarse_map: Mapping[tuple[Hashable, ...], CoarseOutcome],
    decoder: Mapping[CoarseOutcome, Mapping[tuple[Hashable, ...], float]],
    threshold: float = 0.0,
) -> DirectedInfluenceScaleCertificate:
    """Certify one P11 directed-influence entry under coarse observation.

    ``coarse_map`` acts on the one-target marginal outcomes returned by P11's
    ``marginal_distribution``.  ``decoder`` must satisfy the P18 fiber-support
    condition.  The same matched intervention-pair family is used at both
    scales; changing the intervention semantics is outside this theorem.
    """
    if source < 0:
        raise ValueError("source must be nonnegative")
    _validate_threshold(threshold)

    pairs = tuple(source_pairs.get(source, ()))
    family = _target_response_family(responses, pairs, delay, target)

    missing_outcomes = {
        outcome for distribution in family.values() for outcome in distribution
    }.difference(coarse_map)
    if missing_outcomes:
        raise ValueError("coarse_map must cover every observed target outcome")

    fine_distances = []
    coarse_distances = []
    for first, second in pairs:
        first_fine = family[first]
        second_fine = family[second]
        fine_distances.append(total_variation_discrete(first_fine, second_fine))

        first_coarse = pushforward_distribution(first_fine, coarse_map)
        second_coarse = pushforward_distribution(second_fine, coarse_map)
        coarse_distances.append(
            total_variation_discrete(first_coarse, second_coarse)
        )

    fine_influence = max(fine_distances)
    coarse_influence = max(coarse_distances)
    reconstruction_defect = max(
        reconstruction_error(distribution, coarse_map, decoder)
        for distribution in family.values()
    )
    distortion_bound = min(1.0, 2.0 * reconstruction_defect)
    guaranteed_coarse = max(0.0, fine_influence - distortion_bound)

    tolerance = 1e-12
    if coarse_influence > fine_influence + tolerance:
        raise RuntimeError("TV contraction was violated by the supplied scale map")
    if fine_influence > coarse_influence + distortion_bound + tolerance:
        raise RuntimeError("P18 reconstruction distortion bound was violated")

    fine_edge = fine_influence > threshold
    coarse_edge = coarse_influence > threshold
    preservation_certified = fine_influence > threshold + distortion_bound

    return DirectedInfluenceScaleCertificate(
        source=source,
        target=target,
        delay=delay,
        fine_influence=fine_influence,
        coarse_influence=coarse_influence,
        reconstruction_defect=reconstruction_defect,
        distortion_bound=distortion_bound,
        guaranteed_coarse_influence=guaranteed_coarse,
        threshold=threshold,
        coarse_edge_present=coarse_edge,
        fine_edge_present=fine_edge,
        edge_preservation_certified=preservation_certified,
        no_false_positive_certified=coarse_influence <= fine_influence + tolerance,
    )
