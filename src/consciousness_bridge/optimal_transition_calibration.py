"""Proposition 59: optimal transition-calibration allocation.

P58 converts noisy pairwise transition measurements into route-confidence
intervals. P59 solves a declared continuous design problem for how to allocate a
fixed transition-calibration budget across pairwise measurements when the
certified uncertainty surrogate has inverse-square-root form.

The theorem does not claim to solve the full combinatorial robust-routing design
problem. It solves the strictly convex surrogate exactly.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, isfinite, log, sqrt
from typing import Hashable, Mapping, TypeVar

Edge = TypeVar("Edge", bound=Hashable)


@dataclass(frozen=True)
class CalibrationAllocation:
    """Closed-form optimum for the P59 continuous allocation problem."""

    allocations: dict[Hashable, float]
    objective_value: float
    total_budget: float
    normalization: float


def hoeffding_coefficient(
    range_width: float,
    alpha: float,
) -> float:
    """Return the inverse-square-root coefficient in a Hoeffding radius."""
    _positive_finite(range_width, "range_width")
    if not isfinite(alpha) or alpha <= 0.0 or alpha >= 1.0:
        raise ValueError("alpha must lie strictly between zero and one")
    return range_width * sqrt(log(2.0 / alpha) / 2.0)


def optimal_continuous_calibration_allocation(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    total_budget: float,
) -> CalibrationAllocation:
    """Minimize sum_e sensitivity_e * coefficient_e / sqrt(n_e).

    The optimization is over strictly positive real allocations ``n_e`` with
    sum ``n_e = total_budget``. For positive coefficients and sensitivities the
    objective is strictly convex and has the unique optimum

        n_e = N b_e^(2/3) / sum_j b_j^(2/3),

    where ``b_e = sensitivity_e * coefficient_e``.
    """
    _positive_finite(total_budget, "total_budget")
    if not coefficients:
        raise ValueError("coefficients must be nonempty")
    if set(coefficients) != set(sensitivities):
        raise ValueError("sensitivities must cover exactly the coefficient keys")

    powered: dict[Edge, float] = {}
    for edge, coefficient in coefficients.items():
        _positive_finite(coefficient, "coefficient")
        sensitivity = sensitivities[edge]
        _positive_finite(sensitivity, "sensitivity")
        powered[edge] = (coefficient * sensitivity) ** (2.0 / 3.0)

    normalization = sum(powered.values())
    allocations = {
        edge: total_budget * value / normalization
        for edge, value in powered.items()
    }
    objective = normalization ** 1.5 / sqrt(total_budget)
    return CalibrationAllocation(
        allocations=dict(allocations),
        objective_value=objective,
        total_budget=total_budget,
        normalization=normalization,
    )


def sufficient_budget_for_target(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    target_uncertainty: float,
) -> int:
    """Return a sufficient integer budget for the optimal surrogate to meet target."""
    _positive_finite(target_uncertainty, "target_uncertainty")
    if not coefficients:
        raise ValueError("coefficients must be nonempty")
    if set(coefficients) != set(sensitivities):
        raise ValueError("sensitivities must cover exactly the coefficient keys")

    normalization = 0.0
    for edge, coefficient in coefficients.items():
        _positive_finite(coefficient, "coefficient")
        sensitivity = sensitivities[edge]
        _positive_finite(sensitivity, "sensitivity")
        normalization += (coefficient * sensitivity) ** (2.0 / 3.0)

    required = normalization**3 / target_uncertainty**2
    return ceil(required)


def objective_value(
    allocations: Mapping[Edge, float],
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
) -> float:
    """Evaluate the P59 uncertainty surrogate for a declared allocation."""
    if set(allocations) != set(coefficients) or set(coefficients) != set(sensitivities):
        raise ValueError("all mappings must have exactly the same keys")
    total = 0.0
    for edge, allocation in allocations.items():
        _positive_finite(allocation, "allocation")
        coefficient = coefficients[edge]
        sensitivity = sensitivities[edge]
        _positive_finite(coefficient, "coefficient")
        _positive_finite(sensitivity, "sensitivity")
        total += sensitivity * coefficient / sqrt(allocation)
    return total


def _positive_finite(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")
