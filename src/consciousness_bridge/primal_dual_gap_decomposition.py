"""Proposition 70: exact primal-dual gap decomposition and diagnostics.

P68 turns any positive multiplier into a valid lower bound on the unrestricted
P63 integer optimum. P69 can optimize that dual family to a certified value
tolerance. P70 decomposes the resulting candidate-to-dual gap exactly into two
nonnegative parts:

1. edgewise Lagrangian regret, measuring whether each declared candidate count
   minimizes its one-edge Lagrangian term at the common multiplier; and
2. a budget-slack penalty, measuring unused budget at that multiplier.

The decomposition is a certificate diagnostic. An edgewise regret is not, by
itself, the amount by which the coupled primal objective would improve after
changing that edge, because all counts share one budget constraint.

This module concerns a declared experimental resource-allocation surrogate. It
makes no experiential or quantum-ontological claim.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from math import isfinite, sqrt
from typing import TypeVar

from consciousness_bridge.dual_optimal_multiplier import (
    DualOptimalMultiplierCertificate,
    certified_dual_optimal_multiplier,
)
from consciousness_bridge.global_integer_optimality_certificate import (
    global_integer_optimality_certificate,
)
from consciousness_bridge.lagrangian_optimality_gap import (
    lagrangian_dual_lower_bound,
)

Edge = TypeVar("Edge", bound=Hashable)


@dataclass(frozen=True)
class EdgeLagrangianRegret:
    """One edge's contribution to the P70 certificate decomposition."""

    count: int
    minimizing_counts: tuple[int, ...]
    candidate_lagrangian_value: float
    minimum_lagrangian_value: float
    regret: float


@dataclass(frozen=True)
class PrimalDualGapDecomposition:
    """Exact decomposition of a feasible candidate's gap to q(lambda)."""

    lambda_value: float
    candidate_objective: float
    dual_lower_bound: float
    certificate_gap: float
    edge_regrets: dict[Hashable, EdgeLagrangianRegret]
    edge_regret_sum: float
    budget_used: int
    total_budget: int
    budget_slack: int
    slack_penalty: float
    reconstructed_gap: float
    zero_decomposition: bool
    p67_certified_global_optimum: bool


@dataclass(frozen=True)
class StrongestDualGapDiagnostic:
    """P70 decomposition evaluated at a P69-certified dual witness."""

    decomposition: PrimalDualGapDecomposition
    dual_search: DualOptimalMultiplierCertificate
    strongest_dual_gap_lower_bound: float
    strongest_dual_gap_upper_bound: float


def primal_dual_gap_decomposition(
    allocations: Mapping[Edge, int],
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, int],
    total_budget: int,
    lambda_value: float,
) -> PrimalDualGapDecomposition:
    """Decompose ``U(k) - q(lambda)`` into exact nonnegative components.

    For ``b_e = coefficient_e * sensitivity_e`` define

        r_e(k_e; lambda)
          = b_e/sqrt(k_e) + lambda*c_e*k_e
            - min_j [b_e/sqrt(j) + lambda*c_e*j].

    Then every feasible candidate satisfies the identity

        U(k) - q(lambda)
          = sum_e r_e(k_e; lambda)
            + lambda * (B - sum_e c_e*k_e).

    Both terms are nonnegative. The decomposition is zero exactly when the
    budget is tight and every candidate count is an edgewise Lagrangian
    minimizer at the same positive multiplier. In that case the P67 certificate
    succeeds and the candidate is globally optimal for the unrestricted P63
    problem.
    """
    _positive_finite(lambda_value, "lambda_value")
    _validate_candidate_keys(
        allocations,
        coefficients,
        sensitivities,
        unit_costs,
    )

    dual_bound, minima = lagrangian_dual_lower_bound(
        coefficients,
        sensitivities,
        unit_costs,
        total_budget,
        lambda_value,
    )
    budget_used = 0
    candidate_objective = 0.0
    regrets: dict[Edge, EdgeLagrangianRegret] = {}

    for edge, count in allocations.items():
        _positive_integer(count, "allocation count")
        b_edge = coefficients[edge] * sensitivities[edge]
        cost = unit_costs[edge]
        budget_used += cost * count
        objective_term = b_edge / sqrt(count)
        candidate_objective += objective_term
        candidate_lagrangian = objective_term + lambda_value * cost * count
        minimum = minima[edge]
        regret = candidate_lagrangian - minimum.minimum_value
        numerical_scale = max(
            1.0,
            abs(candidate_lagrangian),
            abs(minimum.minimum_value),
        )
        tolerance = 1e-12 * numerical_scale
        if regret < -tolerance:
            raise RuntimeError("numerical edge regret became negative")
        regret = max(0.0, regret)
        regrets[edge] = EdgeLagrangianRegret(
            count=count,
            minimizing_counts=minimum.minimizing_counts,
            candidate_lagrangian_value=candidate_lagrangian,
            minimum_lagrangian_value=minimum.minimum_value,
            regret=regret,
        )

    if budget_used > total_budget:
        raise ValueError("allocation exceeds total_budget")

    budget_slack = total_budget - budget_used
    slack_penalty = lambda_value * budget_slack
    edge_regret_sum = sum(item.regret for item in regrets.values())
    reconstructed = edge_regret_sum + slack_penalty
    certificate_gap = candidate_objective - dual_bound
    scale = max(1.0, abs(candidate_objective), abs(dual_bound), abs(reconstructed))
    tolerance = 1e-10 * scale
    if abs(certificate_gap - reconstructed) > tolerance:
        raise RuntimeError("P70 decomposition identity failed numerically")
    certificate_gap = max(0.0, certificate_gap)
    reconstructed = max(0.0, reconstructed)

    zero_decomposition = reconstructed <= tolerance
    p67 = global_integer_optimality_certificate(
        allocations,
        coefficients,
        sensitivities,
        unit_costs,
        total_budget,
    )
    if zero_decomposition and not p67.certified_global_optimum:
        raise RuntimeError("zero P70 decomposition did not satisfy P67 certificate")

    return PrimalDualGapDecomposition(
        lambda_value=lambda_value,
        candidate_objective=candidate_objective,
        dual_lower_bound=dual_bound,
        certificate_gap=certificate_gap,
        edge_regrets=dict(regrets),
        edge_regret_sum=edge_regret_sum,
        budget_used=budget_used,
        total_budget=total_budget,
        budget_slack=budget_slack,
        slack_penalty=slack_penalty,
        reconstructed_gap=reconstructed,
        zero_decomposition=zero_decomposition,
        p67_certified_global_optimum=p67.certified_global_optimum,
    )


def strongest_dual_gap_diagnostic(
    allocations: Mapping[Edge, int],
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, int],
    total_budget: int,
    *,
    dual_tolerance: float = 1e-10,
    max_iterations: int = 200,
) -> StrongestDualGapDiagnostic:
    """Evaluate P70 at a P69-certified near-optimal dual multiplier.

    P69 returns ``Q_low <= q* <= Q_up``. For a fixed feasible candidate U(k),

        U(k) - Q_up <= U(k) - q* <= U(k) - Q_low.

    The P70 decomposition at P69's returned multiplier equals
    ``U(k) - Q_low``. The interval above therefore certifies how close this
    diagnostic gap is to the smallest candidate-to-dual gap achievable within
    the P68 multiplier family.

    This remains a dual-certificate statement. It does not assert that q* equals
    the P63 primal optimum.
    """
    dual_search = certified_dual_optimal_multiplier(
        coefficients,
        sensitivities,
        unit_costs,
        total_budget,
        dual_tolerance=dual_tolerance,
        max_iterations=max_iterations,
    )
    decomposition = primal_dual_gap_decomposition(
        allocations,
        coefficients,
        sensitivities,
        unit_costs,
        total_budget,
        dual_search.lambda_value,
    )
    lower = max(0.0, decomposition.candidate_objective - dual_search.dual_optimum_upper_bound)
    upper = max(0.0, decomposition.candidate_objective - dual_search.dual_lower_bound)
    if upper + 1e-10 < lower:
        raise RuntimeError("invalid strongest-dual diagnostic interval")
    return StrongestDualGapDiagnostic(
        decomposition=decomposition,
        dual_search=dual_search,
        strongest_dual_gap_lower_bound=lower,
        strongest_dual_gap_upper_bound=upper,
    )


def ranked_edge_regrets(
    decomposition: PrimalDualGapDecomposition,
) -> tuple[tuple[Hashable, EdgeLagrangianRegret], ...]:
    """Rank certificate-diagnostic edge regrets from largest to smallest.

    The ranking identifies which coordinates most violate edgewise Lagrangian
    optimality at the declared common multiplier. It is not a ranking of exact
    primal objective improvements under the coupled budget constraint.
    """
    return tuple(
        sorted(
            decomposition.edge_regrets.items(),
            key=lambda item: (-item[1].regret, repr(item[0])),
        )
    )


def _validate_candidate_keys(
    allocations: Mapping[Edge, int],
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, int],
) -> None:
    if not allocations:
        raise ValueError("allocations must be nonempty")
    keys = set(allocations)
    if (
        set(coefficients) != keys
        or set(sensitivities) != keys
        or set(unit_costs) != keys
    ):
        raise ValueError("all mappings must share keys")


def _positive_integer(value: int, name: str) -> None:
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"{name} must be an integer")
    if value < 1:
        raise ValueError(f"{name} must be positive")


def _positive_finite(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")
