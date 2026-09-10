"""Proposition 65: lower-bounded heterogeneous calibration.

P65 solves the heterogeneous-cost continuous calibration surrogate with the
executable baseline constraint of at least one observation per edge. The exact
continuous solution has a thresholded water-filling form. Flooring that
baseline-safe solution yields a feasible integer allocation with a computable
instance-specific approximation factor and a universal square-root-of-two
factor relative to the exact P63 integer optimum.

This module concerns experimental resource allocation for a declared separable
uncertainty surrogate. It makes no experiential or quantum-ontological claim.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from math import floor, isfinite, sqrt
from typing import TypeVar

Edge = TypeVar("Edge", bound=Hashable)


@dataclass(frozen=True)
class LowerBoundedCalibrationAllocation:
    """Exact continuous P65 allocation with one-sample lower bounds."""

    allocations: dict[Hashable, float]
    budget_shares: dict[Hashable, float]
    objective_value: float
    total_budget: float
    baseline_budget: float
    water_level: float
    pinned_edges: tuple[Hashable, ...]
    free_edges: tuple[Hashable, ...]


@dataclass(frozen=True)
class BaselineSafeIntegerApproximation:
    """P65 floor approximation derived from the lower-bounded optimum."""

    allocations: dict[Hashable, int]
    objective_value: float
    budget_used: float
    continuous_objective: float
    instance_factor: float
    universal_factor: float


def optimal_lower_bounded_heterogeneous_allocation(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, float],
    total_budget: float,
) -> LowerBoundedCalibrationAllocation:
    """Solve the P65 continuous problem with ``n_e >= 1`` exactly.

    The objective is

        sum_e b_e / sqrt(n_e),  b_e = coefficient_e * sensitivity_e,

    subject to

        sum_e c_e n_e <= B,  n_e >= 1.

    For ``B`` above the mandatory baseline ``sum_e c_e``, the unique optimum is

        n_e* = max(1, tau * (b_e / c_e)^(2/3)),

    where the unique positive water level ``tau`` makes the budget constraint
    tight. The active set is found exactly from sorted breakpoints
    ``(c_e / b_e)^(2/3)`` up to ordinary floating-point arithmetic.
    """
    _validate_inputs(coefficients, sensitivities, unit_costs)
    _positive_finite(total_budget, "total_budget")

    baseline_budget = sum(unit_costs.values())
    if total_budget < baseline_budget:
        raise ValueError(
            "total_budget must cover one mandatory observation per edge"
        )

    effective = {
        edge: coefficients[edge] * sensitivities[edge] for edge in coefficients
    }
    scale = {
        edge: (effective[edge] / unit_costs[edge]) ** (2.0 / 3.0)
        for edge in coefficients
    }
    threshold = {edge: 1.0 / scale[edge] for edge in coefficients}

    if total_budget == baseline_budget:
        allocations = {edge: 1.0 for edge in coefficients}
        budget_shares = {edge: unit_costs[edge] for edge in coefficients}
        objective = sum(effective.values())
        return LowerBoundedCalibrationAllocation(
            allocations=allocations,
            budget_shares=budget_shares,
            objective_value=objective,
            total_budget=total_budget,
            baseline_budget=baseline_budget,
            water_level=0.0,
            pinned_edges=tuple(coefficients),
            free_edges=(),
        )

    ordered = sorted(coefficients, key=lambda edge: threshold[edge])
    free: list[Edge] = []
    free_cost = 0.0
    free_denominator = 0.0
    water_level = 0.0

    for index, edge in enumerate(ordered):
        free.append(edge)
        free_cost += unit_costs[edge]
        free_denominator += unit_costs[edge] * scale[edge]
        pinned_cost = baseline_budget - free_cost
        water_level = (total_budget - pinned_cost) / free_denominator

        if index == len(ordered) - 1:
            break
        next_edge = ordered[index + 1]
        if water_level <= threshold[next_edge]:
            break

    free_set = set(free)
    allocations = {
        edge: water_level * scale[edge] if edge in free_set else 1.0
        for edge in coefficients
    }
    budget_shares = {
        edge: unit_costs[edge] * allocations[edge] for edge in coefficients
    }
    objective = sum(
        effective[edge] / sqrt(allocations[edge]) for edge in coefficients
    )

    return LowerBoundedCalibrationAllocation(
        allocations=dict(allocations),
        budget_shares=dict(budget_shares),
        objective_value=objective,
        total_budget=total_budget,
        baseline_budget=baseline_budget,
        water_level=water_level,
        pinned_edges=tuple(edge for edge in coefficients if edge not in free_set),
        free_edges=tuple(edge for edge in coefficients if edge in free_set),
    )


def baseline_safe_floor_approximation(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, float],
    total_budget: float,
) -> BaselineSafeIntegerApproximation:
    """Floor the exact P65 continuous optimum and certify its objective quality.

    Since every P65 continuous allocation is at least one, flooring preserves
    the mandatory integer baseline and cannot exceed the budget. Let

        r_min = min_e floor(n_e*) / n_e*.

    Then the integer objective is at most ``1 / sqrt(r_min)`` times the P65
    continuous optimum, hence at most that factor times the exact P63 integer
    optimum. Also ``floor(x) >= x / 2`` for every ``x >= 1``, so the factor is
    universally at most ``sqrt(2)``.
    """
    continuous = optimal_lower_bounded_heterogeneous_allocation(
        coefficients,
        sensitivities,
        unit_costs,
        total_budget,
    )
    integer_allocations = {
        edge: floor(allocation)
        for edge, allocation in continuous.allocations.items()
    }
    ratios = [
        integer_allocations[edge] / continuous.allocations[edge]
        for edge in coefficients
    ]
    r_min = min(ratios)
    instance_factor = 1.0 / sqrt(r_min)
    universal_factor = sqrt(2.0)
    effective = {
        edge: coefficients[edge] * sensitivities[edge] for edge in coefficients
    }
    objective = sum(
        effective[edge] / sqrt(integer_allocations[edge]) for edge in coefficients
    )
    spent = sum(
        unit_costs[edge] * integer_allocations[edge] for edge in coefficients
    )

    return BaselineSafeIntegerApproximation(
        allocations=dict(integer_allocations),
        objective_value=objective,
        budget_used=spent,
        continuous_objective=continuous.objective_value,
        instance_factor=instance_factor,
        universal_factor=universal_factor,
    )


def _validate_inputs(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, float],
) -> None:
    if not coefficients:
        raise ValueError("coefficients must be nonempty")
    keys = set(coefficients)
    if set(sensitivities) != keys or set(unit_costs) != keys:
        raise ValueError("coefficients, sensitivities, and unit_costs must share keys")
    for edge in coefficients:
        _positive_finite(coefficients[edge], "coefficient")
        _positive_finite(sensitivities[edge], "sensitivity")
        _positive_finite(unit_costs[edge], "unit_cost")


def _positive_finite(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")
