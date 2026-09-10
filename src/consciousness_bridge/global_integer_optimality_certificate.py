"""Proposition 67: Lagrangian certificate for global integer optimality.

P66 is exact inside the integer class that componentwise dominates the P65
floor. P67 gives a sufficient certificate for when a feasible integer
allocation, including a P66 allocation, is also globally optimal for the
unrestricted P63 problem.

The certificate is based on a common nonnegative Lagrange multiplier for the
single budget constraint and exact one-coordinate minimization of the separable
integer Lagrangian. Failure of the certificate is inconclusive: it does not
prove that the candidate is suboptimal.

This module concerns experimental resource allocation for a declared separable
calibration surrogate. It makes no experiential or quantum-ontological claim.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from math import inf, isfinite, sqrt
from typing import TypeVar

Edge = TypeVar("Edge", bound=Hashable)


@dataclass(frozen=True)
class GlobalIntegerOptimalityCertificate:
    """P67 sufficient certificate for unrestricted P63 global optimality."""

    certified_global_optimum: bool
    budget_used: int
    total_budget: int
    budget_tight: bool
    lambda_lower: float
    lambda_upper: float
    witness_lambda: float | None
    edge_intervals: dict[Hashable, tuple[float, float]]
    objective_value: float
    reason: str


def marginal_reduction(b: float, count: int) -> float:
    """Return the objective reduction from increasing ``count`` to ``count+1``."""
    _positive_finite(b, "b")
    if not isinstance(count, int) or isinstance(count, bool):
        raise TypeError("count must be an integer")
    if count < 1:
        raise ValueError("count must be at least one")
    return b * (1.0 / sqrt(count) - 1.0 / sqrt(count + 1))


def global_integer_optimality_certificate(
    allocations: Mapping[Edge, int],
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, int],
    total_budget: int,
) -> GlobalIntegerOptimalityCertificate:
    """Certify global optimality for the unrestricted P63 integer problem.

    For ``b_e = coefficient_e * sensitivity_e`` define

        Delta_e(j) = b_e * (1/sqrt(j) - 1/sqrt(j+1)).

    A count ``k_e > 1`` minimizes the one-edge Lagrangian term

        b_e/sqrt(k) + lambda*c_e*k

    over positive integers exactly when

        Delta_e(k_e)/c_e <= lambda <= Delta_e(k_e-1)/c_e.

    For ``k_e = 1`` the upper endpoint is infinite, so the condition is

        lambda >= Delta_e(1)/c_e.

    If the candidate is feasible, spends the full budget, and all edge
    intervals have a common positive multiplier, weak duality plus exact
    coordinate minimization proves that the candidate is a global optimum of
    the unrestricted P63 problem.

    This condition is sufficient. A false result means only that this
    particular certificate did not prove global optimality.
    """
    _validate_inputs(
        allocations,
        coefficients,
        sensitivities,
        unit_costs,
        total_budget,
    )
    edges = tuple(allocations)
    effective = {
        edge: coefficients[edge] * sensitivities[edge] for edge in edges
    }
    budget_used = sum(unit_costs[edge] * allocations[edge] for edge in edges)
    if budget_used > total_budget:
        raise ValueError("allocation exceeds total_budget")

    intervals: dict[Edge, tuple[float, float]] = {}
    for edge in edges:
        count = allocations[edge]
        cost = unit_costs[edge]
        lower = marginal_reduction(effective[edge], count) / cost
        upper = (
            inf
            if count == 1
            else marginal_reduction(effective[edge], count - 1) / cost
        )
        intervals[edge] = (lower, upper)

    lambda_lower = max(lower for lower, _ in intervals.values())
    lambda_upper = min(upper for _, upper in intervals.values())
    budget_tight = budget_used == total_budget
    common_multiplier = lambda_lower <= lambda_upper and lambda_upper > 0.0
    certified = budget_tight and common_multiplier

    witness_lambda: float | None = None
    if certified:
        if isfinite(lambda_upper):
            witness_lambda = 0.5 * (lambda_lower + lambda_upper)
        else:
            witness_lambda = lambda_lower

    objective = sum(
        effective[edge] / sqrt(allocations[edge]) for edge in edges
    )

    if not budget_tight:
        reason = (
            "not certified: this P67 certificate requires a tight budget; "
            "failure is inconclusive"
        )
    elif not common_multiplier:
        reason = (
            "not certified: edgewise Lagrangian multiplier intervals do not "
            "share a common positive value; failure is inconclusive"
        )
    else:
        reason = (
            "certified: a common positive multiplier and tight budget prove "
            "global optimality for the unrestricted P63 integer problem"
        )

    return GlobalIntegerOptimalityCertificate(
        certified_global_optimum=certified,
        budget_used=budget_used,
        total_budget=total_budget,
        budget_tight=budget_tight,
        lambda_lower=lambda_lower,
        lambda_upper=lambda_upper,
        witness_lambda=witness_lambda,
        edge_intervals=dict(intervals),
        objective_value=objective,
        reason=reason,
    )


def _validate_inputs(
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
    if not isinstance(total_budget, int) or isinstance(total_budget, bool):
        raise TypeError("total_budget must be an integer")
    if total_budget < 1:
        raise ValueError("total_budget must be positive")

    for edge in allocations:
        count = allocations[edge]
        if not isinstance(count, int) or isinstance(count, bool):
            raise TypeError("allocation counts must be integers")
        if count < 1:
            raise ValueError("allocation counts must be positive")
        cost = unit_costs[edge]
        if not isinstance(cost, int) or isinstance(cost, bool):
            raise TypeError("unit costs must be integers")
        if cost < 1:
            raise ValueError("unit costs must be positive")
        _positive_finite(coefficients[edge], "coefficient")
        _positive_finite(sensitivities[edge], "sensitivity")


def _positive_finite(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")
