"""Proposition 33: joint intervention-delay operational quotient tools.

The theorem separates two many-to-one label maps: an intervention quotient b and a
delay quotient a. Exact descent through both maps implies exact descent through the
product quotient. In the approximate case, the product-fiber ambiguity is bounded
by the sum of the separately measured intervention and delay ambiguity budgets.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from itertools import combinations
from typing import TypeVar

from consciousness_bridge.delay_quotient_compatibility import delay_quotient_ambiguity
from consciousness_bridge.identifiability import total_variation_discrete
from consciousness_bridge.intervention_quotient_compatibility import (
    intervention_quotient_ambiguity,
)

FineIntervention = TypeVar("FineIntervention", bound=Hashable)
CoarseIntervention = TypeVar("CoarseIntervention", bound=Hashable)
FineDelay = TypeVar("FineDelay", bound=Hashable)
CoarseDelay = TypeVar("CoarseDelay", bound=Hashable)
Outcome = TypeVar("Outcome", bound=Hashable)

Distribution = Mapping[Outcome, float]
ResponseTable = Mapping[FineIntervention, Mapping[FineDelay, Distribution[Outcome]]]


@dataclass(frozen=True)
class JointOperationalQuotientCertificate:
    intervention_ambiguity: float
    delay_ambiguity: float
    joint_ambiguity: float
    additive_upper_bound: float
    exact_joint_descent_certified: bool


def joint_quotient_ambiguity(
    responses: ResponseTable[FineIntervention, FineDelay, Outcome],
    fine_interventions: Sequence[FineIntervention],
    intervention_quotient: Mapping[FineIntervention, CoarseIntervention],
    fine_delays: Sequence[FineDelay],
    delay_quotient: Mapping[FineDelay, CoarseDelay],
) -> float:
    """Return the diameter of product quotient fibers in total variation."""
    fine_u = tuple(fine_interventions)
    fine_t = tuple(fine_delays)
    _validate_unique_nonempty(fine_u, "fine_interventions")
    _validate_unique_nonempty(fine_t, "fine_delays")
    if set(responses) != set(fine_u):
        raise ValueError("responses must contain every and only declared fine intervention")
    for intervention in fine_u:
        if set(responses[intervention]) != set(fine_t):
            raise ValueError("each intervention must contain every and only declared fine delay")
    if set(intervention_quotient) != set(fine_u):
        raise ValueError("intervention_quotient must cover every fine intervention")
    if set(delay_quotient) != set(fine_t):
        raise ValueError("delay_quotient must cover every fine delay")

    cells: dict[tuple[CoarseIntervention, CoarseDelay], list[tuple[FineIntervention, FineDelay]]] = {}
    for intervention in fine_u:
        for delay in fine_t:
            key = (intervention_quotient[intervention], delay_quotient[delay])
            cells.setdefault(key, []).append((intervention, delay))

    ambiguity = 0.0
    for fiber in cells.values():
        for (u, tau), (v, sigma) in combinations(fiber, 2):
            ambiguity = max(
                ambiguity,
                total_variation_discrete(responses[u][tau], responses[v][sigma]),
            )
    return ambiguity


def joint_operational_quotient_certificate(
    responses: ResponseTable[FineIntervention, FineDelay, Outcome],
    fine_interventions: Sequence[FineIntervention],
    coarse_interventions: Sequence[CoarseIntervention],
    intervention_quotient: Mapping[FineIntervention, CoarseIntervention],
    fine_delays: Sequence[FineDelay],
    coarse_delays: Sequence[CoarseDelay],
    delay_quotient: Mapping[FineDelay, CoarseDelay],
    *,
    tolerance: float = 1e-12,
) -> JointOperationalQuotientCertificate:
    """Certify product-quotient descent and the additive ambiguity theorem."""
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")
    eta_b = intervention_quotient_ambiguity(
        responses,
        fine_interventions,
        coarse_interventions,
        intervention_quotient,
        fine_delays,
    )
    eta_a = delay_quotient_ambiguity(
        responses,
        fine_interventions,
        fine_delays,
        coarse_delays,
        delay_quotient,
    )
    eta_joint = joint_quotient_ambiguity(
        responses,
        fine_interventions,
        intervention_quotient,
        fine_delays,
        delay_quotient,
    )
    additive = eta_b + eta_a
    if eta_joint > additive + 1e-10:
        raise AssertionError("joint ambiguity exceeded the P33 additive theorem bound")
    return JointOperationalQuotientCertificate(
        intervention_ambiguity=eta_b,
        delay_ambiguity=eta_a,
        joint_ambiguity=eta_joint,
        additive_upper_bound=additive,
        exact_joint_descent_certified=eta_joint <= tolerance,
    )


def descended_joint_response_table(
    responses: ResponseTable[FineIntervention, FineDelay, Outcome],
    fine_interventions: Sequence[FineIntervention],
    coarse_interventions: Sequence[CoarseIntervention],
    intervention_quotient: Mapping[FineIntervention, CoarseIntervention],
    fine_delays: Sequence[FineDelay],
    coarse_delays: Sequence[CoarseDelay],
    delay_quotient: Mapping[FineDelay, CoarseDelay],
    *,
    tolerance: float = 1e-12,
) -> dict[CoarseIntervention, dict[CoarseDelay, dict[Outcome, float]]]:
    """Construct the unique product-quotient response table under exact descent."""
    certificate = joint_operational_quotient_certificate(
        responses,
        fine_interventions,
        coarse_interventions,
        intervention_quotient,
        fine_delays,
        coarse_delays,
        delay_quotient,
        tolerance=tolerance,
    )
    if not certificate.exact_joint_descent_certified:
        raise ValueError("response laws do not descend exactly through the joint quotient")

    result: dict[CoarseIntervention, dict[CoarseDelay, dict[Outcome, float]]] = {
        c: {} for c in coarse_interventions
    }
    for c in coarse_interventions:
        representative_u = next(
            u for u in fine_interventions if intervention_quotient[u] == c
        )
        for d in coarse_delays:
            representative_t = next(t for t in fine_delays if delay_quotient[t] == d)
            result[c][d] = dict(responses[representative_u][representative_t])
    return result


def joint_geometry_selection_bound(joint_ambiguity: float) -> float:
    """Worst-case pairwise response-geometry change under joint representative choice."""
    if joint_ambiguity < 0.0:
        raise ValueError("joint_ambiguity must be nonnegative")
    return 2.0 * joint_ambiguity


def additive_geometry_bound(intervention_ambiguity: float, delay_ambiguity: float) -> float:
    """Corollary bound 2(eta_b + eta_a) from separate quotient audits."""
    if intervention_ambiguity < 0.0 or delay_ambiguity < 0.0:
        raise ValueError("ambiguities must be nonnegative")
    return 2.0 * (intervention_ambiguity + delay_ambiguity)


def _validate_unique_nonempty(values: tuple[Hashable, ...], name: str) -> None:
    if not values:
        raise ValueError(f"{name} must be nonempty")
    if len(set(values)) != len(values):
        raise ValueError(f"{name} must contain unique labels")
