"""Proposition 68: Lagrangian lower bounds and optimality-gap certificates.

P67 gives a sufficient zero-gap certificate for unrestricted P63 global
optimality. P68 keeps the same separable integer Lagrangian but uses weak
duality quantitatively: every positive multiplier gives a rigorous lower bound
on the unrestricted P63 optimum and therefore an additive and multiplicative
quality certificate for any feasible integer candidate.

A failed P67 certificate is not evidence of suboptimality. P68 instead reports
how far the candidate can be from the unknown optimum according to a declared
dual witness. The automatic multiplier rule is only a transparent witness
selection rule; it is not claimed to maximize the Lagrangian dual.

This module concerns a declared experimental resource-allocation surrogate. It
makes no experiential or quantum-ontological claim.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from math import floor, inf, isfinite, sqrt
from typing import TypeVar

from consciousness_bridge.global_integer_optimality_certificate import (
    global_integer_optimality_certificate,
)

Edge = TypeVar("Edge", bound=Hashable)


@dataclass(frozen=True)
class EdgeLagrangianMinimum:
    """Exact integer minimum of one separable Lagrangian coordinate."""

    minimizing_counts: tuple[int, ...]
    minimum_value: float
    continuous_stationary_count: float


@dataclass(frozen=True)
class LagrangianOptimalityGapCertificate:
    """P68 lower bound and candidate-quality certificate."""

    lambda_value: float
    lambda_source: str
    candidate_objective: float
    dual_lower_bound: float
    additive_gap_upper_bound: float
    relative_factor_upper_bound: float
    budget_used: int
    total_budget: int
    edge_minimizing_counts: dict[Hashable, tuple[int, ...]]
    p67_certified_global_optimum: bool
    zero_gap_recovered_from_p67: bool


def edge_lagrangian_minimum(
    b: float,
    unit_cost: int,
    lambda_value: float,
) -> EdgeLagrangianMinimum:
    """Minimize ``b/sqrt(j) + lambda_value*unit_cost*j`` over integers j >= 1.

    The real extension is strictly convex. Its stationary point is

        x0 = (b / (2*lambda_value*unit_cost))**(2/3).

    After restricting to x >= 1, an integer minimizer must be one of the floor
    or ceiling neighbors of the real minimizer. Both are evaluated so exact
    adjacent ties at a breakpoint are retained.
    """
    _positive_finite(b, "b")
    _positive_integer(unit_cost, "unit_cost")
    _positive_finite(lambda_value, "lambda_value")

    x0 = (b / (2.0 * lambda_value * unit_cost)) ** (2.0 / 3.0)
    x_star = max(1.0, x0)
    lower = max(1, floor(x_star))
    candidates = sorted({lower, max(1, lower + 1)})
    values = {
        count: b / sqrt(count) + lambda_value * unit_cost * count
        for count in candidates
    }
    minimum = min(values.values())
    tolerance = 1e-12 * max(1.0, abs(minimum))
    minimizers = tuple(
        count for count in candidates if abs(values[count] - minimum) <= tolerance
    )
    return EdgeLagrangianMinimum(
        minimizing_counts=minimizers,
        minimum_value=minimum,
        continuous_stationary_count=x0,
    )


def lagrangian_dual_lower_bound(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, int],
    total_budget: int,
    lambda_value: float,
) -> tuple[float, dict[Edge, EdgeLagrangianMinimum]]:
    """Return the P68 weak-duality lower bound for a declared multiplier."""
    _validate_problem_inputs(coefficients, sensitivities, unit_costs, total_budget)
    _positive_finite(lambda_value, "lambda_value")

    minima: dict[Edge, EdgeLagrangianMinimum] = {}
    total = -lambda_value * total_budget
    for edge in coefficients:
        b_edge = coefficients[edge] * sensitivities[edge]
        minimum = edge_lagrangian_minimum(
            b_edge,
            unit_costs[edge],
            lambda_value,
        )
        minima[edge] = minimum
        total += minimum.minimum_value
    return total, minima


def lagrangian_optimality_gap_certificate(
    allocations: Mapping[Edge, int],
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, int],
    total_budget: int,
    lambda_value: float | None = None,
) -> LagrangianOptimalityGapCertificate:
    """Bound candidate suboptimality relative to the unrestricted P63 optimum.

    For any lambda > 0, weak duality gives

        q(lambda) <= U_int^*(B),

    where

        q(lambda) = sum_e min_{j>=1} [b_e/sqrt(j) + lambda*c_e*j]
                    - lambda*B.

    Hence every feasible candidate k satisfies

        0 <= U(k) - U_int^*(B) <= U(k) - q(lambda).

    If ``lambda_value`` is omitted, a transparent P67-derived witness is used.
    That automatic rule is not claimed to maximize q(lambda). If P67 already
    certifies the candidate, its common multiplier is used and P68 recovers a
    zero duality gap, up to floating-point tolerance.
    """
    _validate_candidate_inputs(
        allocations,
        coefficients,
        sensitivities,
        unit_costs,
        total_budget,
    )
    budget_used = sum(unit_costs[e] * allocations[e] for e in allocations)
    if budget_used > total_budget:
        raise ValueError("allocation exceeds total_budget")

    p67 = global_integer_optimality_certificate(
        allocations,
        coefficients,
        sensitivities,
        unit_costs,
        total_budget,
    )

    if lambda_value is None:
        selected_lambda, source = _automatic_lambda(p67.lambda_lower, p67.lambda_upper)
        if p67.witness_lambda is not None:
            selected_lambda = p67.witness_lambda
            source = "P67 common-multiplier witness"
    else:
        _positive_finite(lambda_value, "lambda_value")
        selected_lambda = lambda_value
        source = "user-supplied multiplier"

    dual_bound, minima = lagrangian_dual_lower_bound(
        coefficients,
        sensitivities,
        unit_costs,
        total_budget,
        selected_lambda,
    )

    candidate_objective = p67.objective_value
    numerical_scale = max(1.0, abs(candidate_objective), abs(dual_bound))
    tolerance = 1e-10 * numerical_scale
    if dual_bound > candidate_objective + tolerance:
        raise RuntimeError("numerical dual bound exceeded feasible candidate objective")
    dual_bound = min(dual_bound, candidate_objective)

    gap = max(0.0, candidate_objective - dual_bound)
    factor = inf if dual_bound <= 0.0 else candidate_objective / dual_bound
    zero_gap_from_p67 = p67.certified_global_optimum and gap <= tolerance

    return LagrangianOptimalityGapCertificate(
        lambda_value=selected_lambda,
        lambda_source=source,
        candidate_objective=candidate_objective,
        dual_lower_bound=dual_bound,
        additive_gap_upper_bound=gap,
        relative_factor_upper_bound=factor,
        budget_used=budget_used,
        total_budget=total_budget,
        edge_minimizing_counts={
            edge: minimum.minimizing_counts for edge, minimum in minima.items()
        },
        p67_certified_global_optimum=p67.certified_global_optimum,
        zero_gap_recovered_from_p67=zero_gap_from_p67,
    )


def _automatic_lambda(lambda_lower: float, lambda_upper: float) -> tuple[float, str]:
    if lambda_lower <= 0.0 or not isfinite(lambda_lower):
        raise RuntimeError("P67-derived lower multiplier endpoint must be positive")
    if isfinite(lambda_upper) and lambda_upper > 0.0:
        if lambda_lower <= lambda_upper:
            return 0.5 * (lambda_lower + lambda_upper), "P67 interval midpoint"
        return sqrt(lambda_lower * lambda_upper), "P67 endpoint geometric mean"
    return lambda_lower, "P67 lower endpoint"


def _validate_problem_inputs(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, int],
    total_budget: int,
) -> None:
    if not coefficients:
        raise ValueError("coefficients must be nonempty")
    keys = set(coefficients)
    if set(sensitivities) != keys or set(unit_costs) != keys:
        raise ValueError("coefficients, sensitivities, and unit_costs must share keys")
    _positive_integer(total_budget, "total_budget")
    for edge in coefficients:
        _positive_finite(coefficients[edge], "coefficient")
        _positive_finite(sensitivities[edge], "sensitivity")
        _positive_integer(unit_costs[edge], "unit_cost")
    if total_budget < sum(unit_costs.values()):
        raise ValueError("total_budget is below the one-observation baseline")


def _validate_candidate_inputs(
    allocations: Mapping[Edge, int],
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, int],
    total_budget: int,
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
    _validate_problem_inputs(coefficients, sensitivities, unit_costs, total_budget)
    for count in allocations.values():
        _positive_integer(count, "allocation count")


def _positive_integer(value: int, name: str) -> None:
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"{name} must be an integer")
    if value < 1:
        raise ValueError(f"{name} must be positive")


def _positive_finite(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")
