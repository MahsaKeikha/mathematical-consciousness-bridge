"""Finite response-law tools for Proposition 32 delay-quotient compatibility.

P32 asks when several declared fine delay labels can descend to one coarse temporal
label without making the retained response law depend on which fine-time
representative is chosen. The construction is operational. It does not assert that
physical times are ontologically identical or that temporal resolution is irrelevant.
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
    intervention_count: int
    fine_delay_count: int
    coarse_delay_count: int
    quotient_ambiguity: float
    exact_descent_certified: bool


def delay_fibers(
    fine_delays: Sequence[FineDelay],
    coarse_delays: Sequence[CoarseDelay],
    quotient: Mapping[FineDelay, CoarseDelay],
) -> dict[CoarseDelay, tuple[FineDelay, ...]]:
    """Return fibers of a declared surjective delay quotient."""
    fine = tuple(fine_delays)
    coarse = tuple(coarse_delays)
    _validate_unique_nonempty(fine, "fine_delays")
    _validate_unique_nonempty(coarse, "coarse_delays")
    if set(quotient) != set(fine):
        raise ValueError("quotient must be defined on every and only fine delay")
    if any(image not in set(coarse) for image in quotient.values()):
        raise ValueError("quotient images must be coarse delays")
    if set(quotient.values()) != set(coarse):
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
    """Largest within-temporal-fiber TV discrepancy, uniformly over interventions."""
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
    tolerance: float = 1e-12,
) -> DelayQuotientCertificate:
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
        exact_descent_certified=ambiguity <= tolerance,
    )


def descended_delay_response_table(
    responses: ResponseTable[Intervention, FineDelay, Outcome],
    interventions: Sequence[Intervention],
    fine_delays: Sequence[FineDelay],
    coarse_delays: Sequence[CoarseDelay],
    quotient: Mapping[FineDelay, CoarseDelay],
    *,
    tolerance: float = 1e-12,
) -> dict[Intervention, dict[CoarseDelay, dict[Outcome, float]]]:
    """Construct the unique coarse-delay response table under exact descent."""
    intervention_tuple = tuple(interventions)
    fine = tuple(fine_delays)
    coarse = tuple(coarse_delays)
    fibers = delay_fibers(fine, coarse, quotient)
    certificate = delay_quotient_certificate(
        responses, intervention_tuple, fine, coarse, quotient, tolerance=tolerance
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


def representative_delay_response_table(
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
    result: dict[Intervention, dict[CoarseDelay, dict[Outcome, float]]] = {}
    for intervention in intervention_tuple:
        if intervention not in responses:
            raise ValueError("intervention response law is missing")
        result[intervention] = {}
        for coarse_label in coarse:
            fine_label = representatives[coarse_label]
            if fine_label not in quotient or quotient[fine_label] != coarse_label:
                raise ValueError("each representative must lie in its declared quotient fiber")
            if fine_label not in responses[intervention]:
                raise ValueError("representative delay response law is missing")
            result[intervention][coarse_label] = dict(responses[intervention][fine_label])
    return result


def representative_selection_distance(
    first: Mapping[Intervention, Mapping[CoarseDelay, Distribution[Outcome]]],
    second: Mapping[Intervention, Mapping[CoarseDelay, Distribution[Outcome]]],
) -> float:
    """Maximum TV discrepancy between two coarse-time representative tables."""
    if set(first) != set(second):
        raise ValueError("representative tables must have the same interventions")
    distance = 0.0
    for intervention in first:
        if set(first[intervention]) != set(second[intervention]):
            raise ValueError("representative tables must have the same coarse delays")
        for delay in first[intervention]:
            distance = max(
                distance,
                total_variation_discrete(
                    first[intervention][delay], second[intervention][delay]
                ),
            )
    return distance


def response_geometry_selection_bound(quotient_ambiguity: float) -> float:
    """2 eta bound for intervention-pair geometry at a coarse temporal label."""
    if quotient_ambiguity < 0.0:
        raise ValueError("quotient_ambiguity must be nonnegative")
    return 2.0 * quotient_ambiguity


def temporal_path_selection_bound(
    quotient_ambiguity: float, transition_count: int
) -> float:
    """Bound representative-induced change of a sum of TV temporal transitions.

    Each temporal edge can move by at most 2 eta because both endpoint response
    laws can change by at most eta. Summing M declared transitions gives 2 M eta.
    """
    if quotient_ambiguity < 0.0:
        raise ValueError("quotient_ambiguity must be nonnegative")
    if transition_count < 0:
        raise ValueError("transition_count must be nonnegative")
    return 2.0 * transition_count * quotient_ambiguity


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
