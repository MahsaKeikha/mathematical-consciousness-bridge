"""Finite response-law tools for Proposition 32 delay quotient compatibility.

P32 asks when several declared fine delay labels can descend to one coarse temporal
label without hiding time-resolved response differences. Delay quotienting is an
operational construction on a declared experiment grid; it is not evidence that
distinct physical times or dynamical states are identical.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from itertools import combinations
from typing import TypeVar

from consciousness_bridge.identifiability import total_variation_discrete

Intervention = TypeVar("Intervention", bound=Hashable)
FineDelay = TypeVar("FineDelay", bound=Hashable)
CoarseDelay = TypeVar("CoarseDelay", bound=Hashable)
Outcome = TypeVar("Outcome", bound=Hashable)

Distribution = Mapping[Outcome, float]
ResponseTable = Mapping[Intervention, Mapping[FineDelay, Distribution[Outcome]]]


@dataclass(frozen=True)
class DelayQuotientCertificate:
    """Audit exact descent separately from a declared approximate tolerance."""

    intervention_count: int
    fine_delay_count: int
    coarse_delay_count: int
    quotient_ambiguity: float
    tolerance: float
    exact_descent_certified: bool
    within_tolerance_certified: bool


def delay_fibers(
    fine_delays: Sequence[FineDelay],
    coarse_delays: Sequence[CoarseDelay],
    quotient: Mapping[FineDelay, CoarseDelay],
) -> dict[CoarseDelay, tuple[FineDelay, ...]]:
    """Return the fibers of a declared surjective delay quotient."""
    fine = tuple(fine_delays)
    coarse = tuple(coarse_delays)
    _validate_unique_nonempty(fine, "fine_delays")
    _validate_unique_nonempty(coarse, "coarse_delays")

    if set(quotient) != set(fine):
        raise ValueError("quotient must be defined on every and only fine delay")
    coarse_set = set(coarse)
    if any(image not in coarse_set for image in quotient.values()):
        raise ValueError("quotient images must be coarse delays")
    if set(quotient.values()) != coarse_set:
        raise ValueError("quotient must be surjective onto coarse_delays")

    return {
        coarse_label: tuple(
            fine_label for fine_label in fine if quotient[fine_label] == coarse_label
        )
        for coarse_label in coarse
    }


def delay_quotient_ambiguity(
    responses: ResponseTable[Intervention, FineDelay, Outcome],
    interventions: Sequence[Intervention],
    fine_delays: Sequence[FineDelay],
    coarse_delays: Sequence[CoarseDelay],
    quotient: Mapping[FineDelay, CoarseDelay],
) -> float:
    """Return the largest within-delay-fiber TV response discrepancy.

    This is

    sup_u sup_{q(tau)=q(tau')} TV(P^{u,tau}, P^{u,tau'}).
    """
    intervention_tuple = tuple(interventions)
    fine = tuple(fine_delays)
    _validate_unique_nonempty(intervention_tuple, "interventions")
    fibers = delay_fibers(fine, coarse_delays, quotient)
    _validate_response_grid(responses, intervention_tuple, fine)

    ambiguity = 0.0
    for intervention in intervention_tuple:
        for fiber in fibers.values():
            for first, second in combinations(fiber, 2):
                ambiguity = max(
                    ambiguity,
                    total_variation_discrete(
                        responses[intervention][first], responses[intervention][second]
                    ),
                )
    return ambiguity


def delay_quotient_certificate(
    responses: ResponseTable[Intervention, FineDelay, Outcome],
    interventions: Sequence[Intervention],
    fine_delays: Sequence[FineDelay],
    coarse_delays: Sequence[CoarseDelay],
    quotient: Mapping[FineDelay, CoarseDelay],
    *,
    tolerance: float = 0.0,
) -> DelayQuotientCertificate:
    """Report exact descent and tolerance-relative approximation separately."""
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")
    intervention_tuple = tuple(interventions)
    fine = tuple(fine_delays)
    coarse = tuple(coarse_delays)
    ambiguity = delay_quotient_ambiguity(
        responses, intervention_tuple, fine, coarse, quotient
    )
    return DelayQuotientCertificate(
        intervention_count=len(intervention_tuple),
        fine_delay_count=len(fine),
        coarse_delay_count=len(coarse),
        quotient_ambiguity=ambiguity,
        tolerance=tolerance,
        exact_descent_certified=ambiguity == 0.0,
        within_tolerance_certified=ambiguity <= tolerance,
    )


def descended_response_table(
    responses: ResponseTable[Intervention, FineDelay, Outcome],
    interventions: Sequence[Intervention],
    fine_delays: Sequence[FineDelay],
    coarse_delays: Sequence[CoarseDelay],
    quotient: Mapping[FineDelay, CoarseDelay],
) -> dict[Intervention, dict[CoarseDelay, dict[Outcome, float]]]:
    """Construct the unique coarse-delay response table only under exact descent."""
    intervention_tuple = tuple(interventions)
    fine = tuple(fine_delays)
    coarse = tuple(coarse_delays)
    fibers = delay_fibers(fine, coarse, quotient)
    certificate = delay_quotient_certificate(
        responses, intervention_tuple, fine, coarse, quotient
    )
    if not certificate.exact_descent_certified:
        raise ValueError("response laws do not descend exactly through the delay quotient")

    return {
        intervention: {
            coarse_label: dict(responses[intervention][fiber[0]])
            for coarse_label, fiber in fibers.items()
        }
        for intervention in intervention_tuple
    }


def representative_response_table(
    responses: ResponseTable[Intervention, FineDelay, Outcome],
    interventions: Sequence[Intervention],
    coarse_delays: Sequence[CoarseDelay],
    quotient: Mapping[FineDelay, CoarseDelay],
    representatives: Mapping[CoarseDelay, FineDelay],
) -> dict[Intervention, dict[CoarseDelay, dict[Outcome, float]]]:
    """Construct a representative-dependent coarse-delay response table."""
    intervention_tuple = tuple(interventions)
    coarse = tuple(coarse_delays)
    _validate_unique_nonempty(intervention_tuple, "interventions")
    _validate_unique_nonempty(coarse, "coarse_delays")
    if set(representatives) != set(coarse):
        raise ValueError("representatives must select one fine delay per coarse label")

    for coarse_label in coarse:
        fine_delay = representatives[coarse_label]
        if fine_delay not in quotient or quotient[fine_delay] != coarse_label:
            raise ValueError("each representative must lie in its declared delay fiber")

    result: dict[Intervention, dict[CoarseDelay, dict[Outcome, float]]] = {}
    for intervention in intervention_tuple:
        if intervention not in responses:
            raise ValueError("representative response law is missing an intervention")
        result[intervention] = {}
        for coarse_label in coarse:
            fine_delay = representatives[coarse_label]
            if fine_delay not in responses[intervention]:
                raise ValueError("representative response law is missing a selected delay")
            result[intervention][coarse_label] = dict(responses[intervention][fine_delay])
    return result


def representative_selection_distance(
    first: Mapping[Intervention, Mapping[CoarseDelay, Distribution[Outcome]]],
    second: Mapping[Intervention, Mapping[CoarseDelay, Distribution[Outcome]]],
) -> float:
    """Return the maximum TV discrepancy between two delay representatives."""
    if set(first) != set(second):
        raise ValueError("representative tables must have the same interventions")
    distance = 0.0
    for intervention in first:
        if set(first[intervention]) != set(second[intervention]):
            raise ValueError("representative tables must have the same coarse delays")
        for coarse_delay in first[intervention]:
            distance = max(
                distance,
                total_variation_discrete(
                    first[intervention][coarse_delay],
                    second[intervention][coarse_delay],
                ),
            )
    return distance


def quotient_geometry_selection_bound(quotient_ambiguity: float) -> float:
    """Return the 2 eta bound for representative-dependent response geometry."""
    if quotient_ambiguity < 0.0:
        raise ValueError("quotient_ambiguity must be nonnegative")
    return 2.0 * quotient_ambiguity


def _validate_response_grid(
    responses: ResponseTable[Intervention, FineDelay, Outcome],
    interventions: tuple[Intervention, ...],
    fine_delays: tuple[FineDelay, ...],
) -> None:
    if set(responses) != set(interventions):
        raise ValueError("responses must contain every and only declared intervention")
    for intervention in interventions:
        if set(responses[intervention]) != set(fine_delays):
            raise ValueError("each intervention must contain every and only declared fine delay")


def _validate_unique_nonempty(values: tuple[Hashable, ...], name: str) -> None:
    if not values:
        raise ValueError(f"{name} must be nonempty")
    if len(set(values)) != len(values):
        raise ValueError(f"{name} must contain unique labels")
