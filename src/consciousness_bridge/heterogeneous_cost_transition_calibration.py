"""Proposition 62: heterogeneous-cost continuous transition calibration.

P59 solves the continuous inverse-square-root calibration problem when one unit
of calibration effort costs the same on every transition. P62 allows the cost
per calibration observation to differ by edge and solves the resulting strictly
convex budget problem exactly.

The theorem concerns a declared separable uncertainty surrogate. It does not
solve the heterogeneous-cost integer problem or the full robust-routing design
problem.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from math import ceil, isfinite, sqrt
from typing import TypeVar

Edge = TypeVar("Edge", bound=Hashable)


@dataclass(frozen=True)
class HeterogeneousCostCalibrationAllocation:
    """Exact continuous P62 allocation under edge-specific unit costs."""

    allocations: dict[Hashable, float]
    budget_shares: dict[Hashable, float]
    objective_value: float
    total_budget: float
    normalization: float


def optimal_heterogeneous_cost_allocation(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, float],
    total_budget: float,
) -> HeterogeneousCostCalibrationAllocation:
    """Minimize sum_e w_e a_e / sqrt(n_e) subject to sum_e c_e n_e = B.

    Writing ``b_e = w_e a_e`` and

        T = sum_e b_e^(2/3) c_e^(1/3),

    the unique continuous optimum is

        n_e* = (B / T) b_e^(2/3) c_e^(-2/3).

    The minimum surrogate uncertainty is ``T^(3/2) / sqrt(B)``.
    """
    _validate_inputs(coefficients, sensitivities, unit_costs)
    _positive_finite(total_budget, "total_budget")

    weighted_terms: dict[Edge, float] = {}
    effective: dict[Edge, float] = {}
    for edge, coefficient in coefficients.items():
        sensitivity = sensitivities[edge]
        unit_cost = unit_costs[edge]
        b_edge = coefficient * sensitivity
        effective[edge] = b_edge
        weighted_terms[edge] = b_edge ** (2.0 / 3.0) * unit_cost ** (1.0 / 3.0)

    normalization = sum(weighted_terms.values())
    allocations = {
        edge: (
            total_budget
            / normalization
            * effective[edge] ** (2.0 / 3.0)
            * unit_costs[edge] ** (-2.0 / 3.0)
        )
        for edge in coefficients
    }
    budget_shares = {
        edge: unit_costs[edge] * allocations[edge] for edge in coefficients
    }
    objective = normalization ** 1.5 / sqrt(total_budget)

    return HeterogeneousCostCalibrationAllocation(
        allocations=dict(allocations),
        budget_shares=dict(budget_shares),
        objective_value=objective,
        total_budget=total_budget,
        normalization=normalization,
    )


def objective_value(
    allocations: Mapping[Edge, float],
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
) -> float:
    """Evaluate the P62 separable uncertainty surrogate."""
    if set(allocations) != set(coefficients) or set(coefficients) != set(sensitivities):
        raise ValueError("allocations, coefficients, and sensitivities must share keys")
    total = 0.0
    for edge, allocation in allocations.items():
        _positive_finite(allocation, "allocation")
        coefficient = coefficients[edge]
        sensitivity = sensitivities[edge]
        _positive_finite(coefficient, "coefficient")
        _positive_finite(sensitivity, "sensitivity")
        total += sensitivity * coefficient / sqrt(allocation)
    return total


def budget_used(
    allocations: Mapping[Edge, float],
    unit_costs: Mapping[Edge, float],
) -> float:
    """Return the total heterogeneous calibration cost of an allocation."""
    if set(allocations) != set(unit_costs):
        raise ValueError("allocations and unit_costs must share exactly the same keys")
    total = 0.0
    for edge, allocation in allocations.items():
        _positive_finite(allocation, "allocation")
        unit_cost = unit_costs[edge]
        _positive_finite(unit_cost, "unit_cost")
        total += unit_cost * allocation
    return total


def sufficient_budget_for_target(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, float],
    target_uncertainty: float,
) -> int:
    """Return a sufficient integer-valued cost budget for a target surrogate level."""
    _validate_inputs(coefficients, sensitivities, unit_costs)
    _positive_finite(target_uncertainty, "target_uncertainty")
    normalization = sum(
        (coefficients[edge] * sensitivities[edge]) ** (2.0 / 3.0)
        * unit_costs[edge] ** (1.0 / 3.0)
        for edge in coefficients
    )
    return ceil(normalization**3 / target_uncertainty**2)


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
