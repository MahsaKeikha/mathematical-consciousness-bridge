"""Proposition 44: finite-family post-selection and confidence spending.

The module provides the statistical assembly layer needed to select a candidate
preparation pair after observing simultaneously valid lower confidence margins.
It intentionally does not infer physical completeness or identify any target
with consciousness.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from typing import TypeVar

Candidate = TypeVar("Candidate", bound=Hashable)


@dataclass(frozen=True)
class PairAdaptiveCertificate:
    """Result of selecting a candidate from simultaneous lower margins."""

    selected_candidate: Candidate
    selected_lower_margin: float
    family_failure_budget: float
    confidence_lower_bound: float
    certified: bool


def weighted_alpha_spending(
    weights: Mapping[Candidate, float],
    total_alpha: float,
) -> dict[Candidate, float]:
    """Allocate a total failure budget in proportion to positive weights."""
    _alpha(total_alpha, "total_alpha", allow_zero=True)
    if not weights:
        raise ValueError("weights must contain at least one candidate")
    total_weight = 0.0
    for weight in weights.values():
        if weight <= 0.0:
            raise ValueError("all weights must be positive")
        total_weight += weight
    return {
        candidate: total_alpha * weight / total_weight
        for candidate, weight in weights.items()
    }


def family_confidence_lower_bound(
    alpha_quantum: Mapping[Candidate, float],
    alpha_target: Mapping[Candidate, float],
) -> float:
    """Return the union-bound simultaneous confidence lower bound."""
    _same_candidates(alpha_quantum, alpha_target)
    failure = 0.0
    for name, table in (
        ("alpha_quantum", alpha_quantum),
        ("alpha_target", alpha_target),
    ):
        for value in table.values():
            _alpha(value, name, allow_zero=True)
            failure += value
    return max(0.0, 1.0 - failure)


def select_maximum_lower_margin(
    lower_margins: Mapping[Candidate, float],
    alpha_quantum: Mapping[Candidate, float],
    alpha_target: Mapping[Candidate, float],
    *,
    tolerance: float = 1e-12,
) -> PairAdaptiveCertificate:
    """Select the largest simultaneous lower margin and retain family coverage.

    The caller supplies candidate-wise lower confidence margins whose individual
    failure probabilities are bounded by the corresponding quantum and target
    alpha allocations. The union bound makes the complete family simultaneous,
    so choosing the largest observed lower margin does not require independence.
    """
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")
    if not lower_margins:
        raise ValueError("lower_margins must contain at least one candidate")
    _same_candidates(lower_margins, alpha_quantum)
    _same_candidates(lower_margins, alpha_target)

    confidence = family_confidence_lower_bound(alpha_quantum, alpha_target)
    selected, margin = max(lower_margins.items(), key=lambda item: item[1])
    failure = sum(alpha_quantum.values()) + sum(alpha_target.values())
    return PairAdaptiveCertificate(
        selected_candidate=selected,
        selected_lower_margin=margin,
        family_failure_budget=failure,
        confidence_lower_bound=confidence,
        certified=margin > tolerance,
    )


def bonferroni_spending(
    candidates: tuple[Candidate, ...],
    total_alpha: float,
) -> dict[Candidate, float]:
    """Return equal finite-family alpha spending."""
    if not candidates:
        raise ValueError("candidates must contain at least one candidate")
    if len(set(candidates)) != len(candidates):
        raise ValueError("candidates must be unique")
    _alpha(total_alpha, "total_alpha", allow_zero=True)
    share = total_alpha / len(candidates)
    return {candidate: share for candidate in candidates}


def _same_candidates(
    first: Mapping[Candidate, object],
    second: Mapping[Candidate, object],
) -> None:
    if set(first) != set(second):
        raise ValueError("candidate sets must match exactly")


def _alpha(value: float, name: str, *, allow_zero: bool) -> None:
    lower_ok = value >= 0.0 if allow_zero else value > 0.0
    if not lower_ok or value >= 1.0:
        interval = "[0, 1)" if allow_zero else "(0, 1)"
        raise ValueError(f"{name} must lie in {interval}")
