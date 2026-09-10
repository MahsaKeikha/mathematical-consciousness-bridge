"""Finite response-law tools for Proposition 31 intervention quotient compatibility.

P31 asks when several declared fine intervention labels can descend to one coarse
intervention label without hiding physically distinguishable response laws. The
module treats intervention quotienting as a semantic/operational construction,
not as evidence that distinct actuators are physically identical or simultaneous.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from itertools import combinations
from typing import TypeVar

from consciousness_bridge.identifiability import total_variation_discrete

FineIntervention = TypeVar("FineIntervention", bound=Hashable)
CoarseIntervention = TypeVar("CoarseIntervention", bound=Hashable)
Delay = TypeVar("Delay", bound=Hashable)
Outcome = TypeVar("Outcome", bound=Hashable)

Distribution = Mapping[Outcome, float]
ResponseTable = Mapping[FineIntervention, Mapping[Delay, Distribution[Outcome]]]


@dataclass(frozen=True)
class InterventionQuotientCertificate:
    """Audit of exact or approximate response-law descent through an intervention map."""

    fine_intervention_count: int
    coarse_intervention_count: int
    delay_count: int
    quotient_ambiguity: float
    exact_descent_certified: bool


def intervention_fibers(
    fine_interventions: Sequence[FineIntervention],
    coarse_interventions: Sequence[CoarseIntervention],
    quotient: Mapping[FineIntervention, CoarseIntervention],
) -> dict[CoarseIntervention, tuple[FineIntervention, ...]]:
    """Return the fibers of a declared surjective intervention quotient."""
    fine = tuple(fine_interventions)
    coarse = tuple(coarse_interventions)
    _validate_unique_nonempty(fine, "fine_interventions")
    _validate_unique_nonempty(coarse, "coarse_interventions")

    if set(quotient) != set(fine):
        raise ValueError("quotient must be defined on every and only fine intervention")
    if any(image not in set(coarse) for image in quotient.values()):
        raise ValueError("quotient images must be coarse interventions")
    if set(quotient.values()) != set(coarse):
        raise ValueError("quotient must be surjective onto coarse_interventions")

    return {
        coarse_label: tuple(
            fine_label for fine_label in fine if quotient[fine_label] == coarse_label
        )
        for coarse_label in coarse
    }


def intervention_quotient_ambiguity(
    responses: ResponseTable[FineIntervention, Delay, Outcome],
    fine_interventions: Sequence[FineIntervention],
    coarse_interventions: Sequence[CoarseIntervention],
    quotient: Mapping[FineIntervention, CoarseIntervention],
    delays: Sequence[Delay],
) -> float:
    """Return the largest within-quotient-fiber TV response discrepancy.

    This is

    sup_{tau} sup_{b(u)=b(v)} TV(P^{u,tau}, P^{v,tau}).
    """
    delay_tuple = tuple(delays)
    _validate_unique_nonempty(delay_tuple, "delays")
    fibers = intervention_fibers(fine_interventions, coarse_interventions, quotient)
    _validate_response_grid(responses, tuple(fine_interventions), delay_tuple)

    ambiguity = 0.0
    for fiber in fibers.values():
        for first, second in combinations(fiber, 2):
            for delay in delay_tuple:
                ambiguity = max(
                    ambiguity,
                    total_variation_discrete(
                        responses[first][delay], responses[second][delay]
                    ),
                )
    return ambiguity


def intervention_quotient_certificate(
    responses: ResponseTable[FineIntervention, Delay, Outcome],
    fine_interventions: Sequence[FineIntervention],
    coarse_interventions: Sequence[CoarseIntervention],
    quotient: Mapping[FineIntervention, CoarseIntervention],
    delays: Sequence[Delay],
    *,
    tolerance: float = 1e-12,
) -> InterventionQuotientCertificate:
    """Certify exact response-law descent iff within-fiber ambiguity vanishes."""
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")
    fine = tuple(fine_interventions)
    coarse = tuple(coarse_interventions)
    delay_tuple = tuple(delays)
    ambiguity = intervention_quotient_ambiguity(
        responses, fine, coarse, quotient, delay_tuple
    )
    return InterventionQuotientCertificate(
        fine_intervention_count=len(fine),
        coarse_intervention_count=len(coarse),
        delay_count=len(delay_tuple),
        quotient_ambiguity=ambiguity,
        exact_descent_certified=ambiguity <= tolerance,
    )


def descended_response_table(
    responses: ResponseTable[FineIntervention, Delay, Outcome],
    fine_interventions: Sequence[FineIntervention],
    coarse_interventions: Sequence[CoarseIntervention],
    quotient: Mapping[FineIntervention, CoarseIntervention],
    delays: Sequence[Delay],
    *,
    tolerance: float = 1e-12,
) -> dict[CoarseIntervention, dict[Delay, dict[Outcome, float]]]:
    """Construct the unique coarse response table when exact descent is certified."""
    fine = tuple(fine_interventions)
    coarse = tuple(coarse_interventions)
    delay_tuple = tuple(delays)
    fibers = intervention_fibers(fine, coarse, quotient)
    certificate = intervention_quotient_certificate(
        responses, fine, coarse, quotient, delay_tuple, tolerance=tolerance
    )
    if not certificate.exact_descent_certified:
        raise ValueError("response laws do not descend exactly through the intervention quotient")

    descended: dict[CoarseIntervention, dict[Delay, dict[Outcome, float]]] = {}
    for coarse_label, fiber in fibers.items():
        representative = fiber[0]
        descended[coarse_label] = {
            delay: dict(responses[representative][delay]) for delay in delay_tuple
        }
    return descended


def representative_response_table(
    responses: ResponseTable[FineIntervention, Delay, Outcome],
    coarse_interventions: Sequence[CoarseIntervention],
    quotient: Mapping[FineIntervention, CoarseIntervention],
    representatives: Mapping[CoarseIntervention, FineIntervention],
    delays: Sequence[Delay],
) -> dict[CoarseIntervention, dict[Delay, dict[Outcome, float]]]:
    """Construct a representative-dependent coarse response table.

    This function is useful when exact descent fails. It does not call the result a
    unique quotient law; the representative dependence is controlled by P31's
    ambiguity bound.
    """
    coarse = tuple(coarse_interventions)
    delay_tuple = tuple(delays)
    _validate_unique_nonempty(coarse, "coarse_interventions")
    _validate_unique_nonempty(delay_tuple, "delays")
    if set(representatives) != set(coarse):
        raise ValueError("representatives must select one fine intervention per coarse label")

    result: dict[CoarseIntervention, dict[Delay, dict[Outcome, float]]] = {}
    for coarse_label in coarse:
        fine_label = representatives[coarse_label]
        if fine_label not in quotient or quotient[fine_label] != coarse_label:
            raise ValueError("each representative must lie in its declared quotient fiber")
        if fine_label not in responses:
            raise ValueError("representative response law is missing")
        missing = [delay for delay in delay_tuple if delay not in responses[fine_label]]
        if missing:
            raise ValueError("representative response law is missing a declared delay")
        result[coarse_label] = {
            delay: dict(responses[fine_label][delay]) for delay in delay_tuple
        }
    return result


def representative_selection_distance(
    first: Mapping[CoarseIntervention, Mapping[Delay, Distribution[Outcome]]],
    second: Mapping[CoarseIntervention, Mapping[Delay, Distribution[Outcome]]],
) -> float:
    """Return the maximum TV discrepancy between two quotient representatives."""
    if set(first) != set(second):
        raise ValueError("representative tables must have the same coarse labels")
    distance = 0.0
    for coarse_label in first:
        if set(first[coarse_label]) != set(second[coarse_label]):
            raise ValueError("representative tables must have the same delay labels")
        for delay in first[coarse_label]:
            distance = max(
                distance,
                total_variation_discrete(
                    first[coarse_label][delay], second[coarse_label][delay]
                ),
            )
    return distance


def quotient_geometry_selection_bound(quotient_ambiguity: float) -> float:
    """Return the 2 eta bound for representative-dependent pairwise geometry."""
    if quotient_ambiguity < 0.0:
        raise ValueError("quotient_ambiguity must be nonnegative")
    return 2.0 * quotient_ambiguity


def _validate_response_grid(
    responses: ResponseTable[FineIntervention, Delay, Outcome],
    fine: tuple[FineIntervention, ...],
    delays: tuple[Delay, ...],
) -> None:
    if set(responses) != set(fine):
        raise ValueError("responses must contain every and only declared fine intervention")
    for intervention in fine:
        if set(responses[intervention]) != set(delays):
            raise ValueError("each fine intervention must contain every and only declared delay")


def _validate_unique_nonempty(values: tuple[Hashable, ...], name: str) -> None:
    if not values:
        raise ValueError(f"{name} must be nonempty")
    if len(set(values)) != len(values):
        raise ValueError(f"{name} must contain unique labels")
