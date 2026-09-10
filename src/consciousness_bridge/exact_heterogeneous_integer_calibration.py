"""Proposition 63: exact heterogeneous-cost integer calibration.

P62 gives the unique continuous optimum when transition observations have
edge-specific costs. P63 solves the corresponding whole-measurement problem
exactly when those costs and the total budget are positive integers.

Unlike P61, unequal measurement costs invalidate the simple largest-marginal-
gain greedy proof. P63 therefore uses an exact dynamic program over budget and
reports the P62 continuous optimum as a rigorous lower bound on the integer
objective.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from math import gcd, inf, isfinite, sqrt
from typing import TypeVar

from consciousness_bridge.heterogeneous_cost_transition_calibration import (
    optimal_heterogeneous_cost_allocation,
)

Edge = TypeVar("Edge", bound=Hashable)


@dataclass(frozen=True)
class ExactHeterogeneousIntegerAllocation:
    """Exact P63 whole-measurement allocation under integer edge costs."""

    allocations: dict[Hashable, int]
    total_spend: int
    unspent_budget: int
    objective_value: float
    continuous_lower_bound: float
    additive_integrality_gap: float
    multiplicative_integrality_gap: float
    cost_gcd: int
    scaled_budget: int
    states_evaluated: int


def exact_heterogeneous_integer_allocation(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, int],
    total_budget: int,
) -> ExactHeterogeneousIntegerAllocation:
    """Solve the P63 integer allocation problem exactly by dynamic programming.

    The optimization problem is

        minimize  sum_e b_e / sqrt(k_e)
        subject to sum_e c_e k_e <= B,
                   k_e in {1, 2, ...},

    where ``b_e = coefficient_e * sensitivity_e`` and the costs ``c_e`` and
    budget ``B`` are positive integers.

    The dynamic program stores the best objective achievable at each exact
    spend after processing each edge.  Its straightforward worst-case running
    time is O(m * B'**2 / c'_min), where costs have first been divided by their
    common gcd and B' = floor(B / gcd(c_e)).  Memory for objective values is
    O(B'), plus predecessor information used to reconstruct the optimum.
    """
    _validate_inputs(coefficients, sensitivities, unit_costs, total_budget)

    edges = tuple(coefficients)
    baseline = sum(unit_costs[edge] for edge in edges)
    if total_budget < baseline:
        raise ValueError(
            "total_budget is infeasible: at least one measurement per edge is required"
        )

    cost_gcd = 0
    for edge in edges:
        cost_gcd = gcd(cost_gcd, unit_costs[edge])
    scaled_costs = {edge: unit_costs[edge] // cost_gcd for edge in edges}
    scaled_budget = total_budget // cost_gcd

    effective = {
        edge: coefficients[edge] * sensitivities[edge] for edge in edges
    }

    previous = [inf] * (scaled_budget + 1)
    previous[0] = 0.0
    predecessor_layers: list[dict[int, tuple[int, int]]] = []
    states_evaluated = 0

    for edge in edges:
        cost = scaled_costs[edge]
        b_edge = effective[edge]
        current = [inf] * (scaled_budget + 1)
        parents: dict[int, tuple[int, int]] = {}

        for previous_spend, previous_value in enumerate(previous):
            if previous_value == inf:
                continue
            max_count = (scaled_budget - previous_spend) // cost
            for count in range(1, max_count + 1):
                states_evaluated += 1
                spend = previous_spend + cost * count
                candidate = previous_value + b_edge / sqrt(count)
                if candidate < current[spend]:
                    current[spend] = candidate
                    parents[spend] = (previous_spend, count)

        if not parents:
            raise RuntimeError("dynamic program lost every feasible state")
        previous = current
        predecessor_layers.append(parents)

    best_spend = min(
        (spend for spend, value in enumerate(previous) if value < inf),
        key=lambda spend: previous[spend],
    )
    best_objective = previous[best_spend]

    allocations: dict[Edge, int] = {}
    spend = best_spend
    for layer_index in range(len(edges) - 1, -1, -1):
        prior_spend, count = predecessor_layers[layer_index][spend]
        allocations[edges[layer_index]] = count
        spend = prior_spend
    allocations = {edge: allocations[edge] for edge in edges}

    total_spend = sum(unit_costs[edge] * allocations[edge] for edge in edges)
    continuous = optimal_heterogeneous_cost_allocation(
        coefficients,
        sensitivities,
        {edge: float(unit_costs[edge]) for edge in edges},
        float(total_budget),
    ).objective_value
    additive_gap = best_objective - continuous
    multiplicative_gap = best_objective / continuous

    return ExactHeterogeneousIntegerAllocation(
        allocations=allocations,
        total_spend=total_spend,
        unspent_budget=total_budget - total_spend,
        objective_value=best_objective,
        continuous_lower_bound=continuous,
        additive_integrality_gap=additive_gap,
        multiplicative_integrality_gap=multiplicative_gap,
        cost_gcd=cost_gcd,
        scaled_budget=scaled_budget,
        states_evaluated=states_evaluated,
    )


def integer_objective_value(
    allocations: Mapping[Edge, int],
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
) -> float:
    """Evaluate the P63 objective for a declared integer allocation."""
    if set(allocations) != set(coefficients) or set(coefficients) != set(sensitivities):
        raise ValueError("allocations, coefficients, and sensitivities must share keys")
    total = 0.0
    for edge, count in allocations.items():
        if not isinstance(count, int) or isinstance(count, bool) or count < 1:
            raise ValueError("allocation counts must be positive integers")
        _positive_finite(coefficients[edge], "coefficient")
        _positive_finite(sensitivities[edge], "sensitivity")
        total += coefficients[edge] * sensitivities[edge] / sqrt(count)
    return total


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
    if not isinstance(total_budget, int) or isinstance(total_budget, bool) or total_budget < 1:
        raise ValueError("total_budget must be a positive integer")
    for edge in coefficients:
        _positive_finite(coefficients[edge], "coefficient")
        _positive_finite(sensitivities[edge], "sensitivity")
        cost = unit_costs[edge]
        if not isinstance(cost, int) or isinstance(cost, bool) or cost < 1:
            raise ValueError("unit costs must be positive integers")


def _positive_finite(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")
