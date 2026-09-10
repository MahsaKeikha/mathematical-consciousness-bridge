"""Proposition 66: residual-exact augmentation of the P65 floor design.

P65 floors the exact lower-bounded continuous heterogeneous calibration optimum.
That floor is always feasible, but it can leave unused budget. P66 proves that
this residual budget is strictly smaller than the mandatory one-sample baseline
cost and solves the best floor-dominating integer augmentation exactly by a
dynamic program whose budget axis depends on the residual rather than the full
experimental budget.

The P66 solution is exact only within the class of integer allocations that
componentwise dominate the P65 floor. P63 remains the globally exact unequal-
cost integer solver. This module makes no experiential or quantum-ontological
claim.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from math import floor, gcd, inf, isfinite, sqrt
from typing import TypeVar

from consciousness_bridge.lower_bounded_heterogeneous_calibration import (
    optimal_lower_bounded_heterogeneous_allocation,
)

Edge = TypeVar("Edge", bound=Hashable)


@dataclass(frozen=True)
class ResidualExactAugmentation:
    """Exact P66 augmentation above the P65 integer floor."""

    floor_allocations: dict[Hashable, int]
    allocations: dict[Hashable, int]
    residual_budget: int
    residual_spend: int
    total_spend: int
    unspent_budget: int
    floor_objective: float
    objective_value: float
    objective_improvement: float
    continuous_lower_bound: float
    floor_instance_factor: float
    augmented_instance_factor: float
    universal_factor: float
    cost_gcd: int
    scaled_residual_budget: int
    states_evaluated: int


def residual_exact_augmentation(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, int],
    total_budget: int,
) -> ResidualExactAugmentation:
    """Solve the best integer augmentation above the P65 floor exactly.

    Let ``n*`` be the exact lower-bounded P65 continuous optimum and

        f_e = floor(n_e*).

    The residual budget is

        R = B - sum_e c_e f_e.

    Because P65 spends the continuous budget tightly,

        R = sum_e c_e frac(n_e*) < sum_e c_e.

    P66 minimizes the declared separable uncertainty objective over

        k_e = f_e + z_e,
        z_e in {0, 1, 2, ...},
        sum_e c_e z_e <= R.

    The dynamic program is globally exact inside this floor-dominating class.
    It is not claimed to equal the unrestricted P63 integer optimum.
    """
    _validate_inputs(coefficients, sensitivities, unit_costs, total_budget)
    edges = tuple(coefficients)

    continuous = optimal_lower_bounded_heterogeneous_allocation(
        coefficients,
        sensitivities,
        {edge: float(unit_costs[edge]) for edge in edges},
        float(total_budget),
    )
    floor_allocations = {
        edge: floor(continuous.allocations[edge]) for edge in edges
    }
    floor_spend = sum(
        unit_costs[edge] * floor_allocations[edge] for edge in edges
    )
    residual_budget = total_budget - floor_spend
    baseline_budget = sum(unit_costs.values())
    if not 0 <= residual_budget < baseline_budget:
        raise RuntimeError("P65 floor residual violated the strict baseline bound")

    effective = {
        edge: coefficients[edge] * sensitivities[edge] for edge in edges
    }
    floor_objective = sum(
        effective[edge] / sqrt(floor_allocations[edge]) for edge in edges
    )

    cost_gcd = 0
    for edge in edges:
        cost_gcd = gcd(cost_gcd, unit_costs[edge])
    scaled_costs = {edge: unit_costs[edge] // cost_gcd for edge in edges}
    scaled_residual_budget = residual_budget // cost_gcd

    previous = [inf] * (scaled_residual_budget + 1)
    previous[0] = 0.0
    predecessor_layers: list[dict[int, tuple[int, int]]] = []
    states_evaluated = 0

    for edge in edges:
        cost = scaled_costs[edge]
        base_count = floor_allocations[edge]
        b_edge = effective[edge]
        current = [inf] * (scaled_residual_budget + 1)
        parents: dict[int, tuple[int, int]] = {}

        for previous_spend, previous_value in enumerate(previous):
            if previous_value == inf:
                continue
            max_increment = (scaled_residual_budget - previous_spend) // cost
            for increment in range(max_increment + 1):
                states_evaluated += 1
                spend = previous_spend + cost * increment
                candidate = previous_value + b_edge / sqrt(base_count + increment)
                if candidate < current[spend]:
                    current[spend] = candidate
                    parents[spend] = (previous_spend, increment)

        if not parents:
            raise RuntimeError("residual dynamic program lost every feasible state")
        previous = current
        predecessor_layers.append(parents)

    best_spend = min(
        (spend for spend, value in enumerate(previous) if value < inf),
        key=lambda spend: previous[spend],
    )
    best_objective = previous[best_spend]

    increments: dict[Edge, int] = {}
    spend = best_spend
    for layer_index in range(len(edges) - 1, -1, -1):
        prior_spend, increment = predecessor_layers[layer_index][spend]
        increments[edges[layer_index]] = increment
        spend = prior_spend
    allocations = {
        edge: floor_allocations[edge] + increments[edge] for edge in edges
    }

    residual_spend = sum(unit_costs[edge] * increments[edge] for edge in edges)
    total_spend = floor_spend + residual_spend
    floor_ratio = min(
        floor_allocations[edge] / continuous.allocations[edge] for edge in edges
    )
    augmented_ratio = min(
        allocations[edge] / continuous.allocations[edge] for edge in edges
    )
    floor_factor = 1.0 / sqrt(floor_ratio)
    augmented_factor = 1.0 / sqrt(augmented_ratio)

    return ResidualExactAugmentation(
        floor_allocations=dict(floor_allocations),
        allocations=dict(allocations),
        residual_budget=residual_budget,
        residual_spend=residual_spend,
        total_spend=total_spend,
        unspent_budget=total_budget - total_spend,
        floor_objective=floor_objective,
        objective_value=best_objective,
        objective_improvement=floor_objective - best_objective,
        continuous_lower_bound=continuous.objective_value,
        floor_instance_factor=floor_factor,
        augmented_instance_factor=augmented_factor,
        universal_factor=sqrt(2.0),
        cost_gcd=cost_gcd,
        scaled_residual_budget=scaled_residual_budget,
        states_evaluated=states_evaluated,
    )


def _validate_inputs(
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
    if not isinstance(total_budget, int) or isinstance(total_budget, bool):
        raise TypeError("total_budget must be an integer")
    for edge in coefficients:
        _positive_finite(coefficients[edge], "coefficient")
        _positive_finite(sensitivities[edge], "sensitivity")
        cost = unit_costs[edge]
        if not isinstance(cost, int) or isinstance(cost, bool) or cost < 1:
            raise ValueError("unit costs must be positive integers")
    baseline = sum(unit_costs.values())
    if total_budget < baseline:
        raise ValueError(
            "total_budget is infeasible: at least one measurement per edge is required"
        )


def _positive_finite(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")
