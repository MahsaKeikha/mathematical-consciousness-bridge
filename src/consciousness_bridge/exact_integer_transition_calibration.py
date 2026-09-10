"""Proposition 61: exact integer transition-calibration allocation.

P60 gives a feasible integer rounding guarantee. P61 solves the same separable
integer resource-allocation problem exactly. Starting from one calibration unit
per edge, each remaining unit is assigned to the edge with the largest current
marginal uncertainty reduction.

The proof uses discrete diminishing returns: the marginal gain sequence for each
edge is strictly decreasing. The greedy allocation therefore selects an optimal
prefix from every edge's gain sequence, which is equivalent to the global
integer optimum under a fixed total budget.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from math import isfinite, sqrt
from typing import TypeVar

from consciousness_bridge.optimal_transition_calibration import objective_value

Edge = TypeVar("Edge", bound=Hashable)


@dataclass(frozen=True)
class ExactIntegerCalibrationAllocation:
    """Exact P61 integer optimum and discrete optimality certificate."""

    allocations: dict[Hashable, int]
    total_budget: int
    total_used: int
    objective_value: float
    last_selected_gain: float | None
    largest_unselected_gain: float
    exchange_condition_holds: bool


def marginal_gain(coefficient: float, current_count: int) -> float:
    """Return the reduction from increasing one count k to k+1.

    The coefficient is the combined P59 quantity b_e = w_e a_e.
    """
    _positive_finite(coefficient, "coefficient")
    if not isinstance(current_count, int) or isinstance(current_count, bool):
        raise TypeError("current_count must be an integer")
    if current_count < 1:
        raise ValueError("current_count must be at least one")
    return coefficient * (
        1.0 / sqrt(current_count)
        - 1.0 / sqrt(current_count + 1)
    )


def marginal_gain_is_decreasing(
    coefficient: float,
    first_count: int,
    second_count: int,
) -> bool:
    """Check the P61 diminishing-return ordering for two positive counts."""
    if first_count >= second_count:
        raise ValueError("first_count must be strictly smaller than second_count")
    return marginal_gain(coefficient, first_count) > marginal_gain(
        coefficient,
        second_count,
    )


def exact_integer_calibration_allocation(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    total_budget: int,
    *,
    tolerance: float = 1e-12,
) -> ExactIntegerCalibrationAllocation:
    """Return the exact integer optimum for the P59 uncertainty surrogate.

    The optimization problem is

        min sum_e b_e / sqrt(k_e)
        subject to k_e in positive integers and sum_e k_e = total_budget,

    with ``b_e = coefficients[e] * sensitivities[e]``.

    The algorithm starts from one unit on every edge and repeatedly assigns one
    remaining unit to the largest current marginal gain. Runtime is
    ``O((B-m) log m)`` for ``m`` edges and total budget ``B``.
    """
    _validate_problem(coefficients, sensitivities, total_budget, tolerance)

    effective = {
        edge: coefficients[edge] * sensitivities[edge]
        for edge in coefficients
    }
    allocations = {edge: 1 for edge in coefficients}
    remaining = total_budget - len(coefficients)

    heap: list[tuple[float, int, Edge]] = []
    for order, edge in enumerate(coefficients):
        gain = marginal_gain(effective[edge], 1)
        heap.append((-gain, order, edge))
    heapify(heap)

    last_selected: float | None = None
    for _ in range(remaining):
        negative_gain, order, edge = heappop(heap)
        selected_gain = -negative_gain
        allocations[edge] += 1
        last_selected = selected_gain
        next_gain = marginal_gain(effective[edge], allocations[edge])
        heappush(heap, (-next_gain, order, edge))

    largest_unselected = -heap[0][0]
    exchange_holds = _exchange_condition(
        allocations,
        effective,
        largest_unselected,
        tolerance=tolerance,
    )

    allocations_as_float = {
        edge: float(count)
        for edge, count in allocations.items()
    }
    achieved = objective_value(
        allocations_as_float,
        coefficients,
        sensitivities,
    )
    return ExactIntegerCalibrationAllocation(
        allocations=dict(allocations),
        total_budget=total_budget,
        total_used=sum(allocations.values()),
        objective_value=achieved,
        last_selected_gain=last_selected,
        largest_unselected_gain=largest_unselected,
        exchange_condition_holds=exchange_holds,
    )


def allocation_exchange_condition(
    allocations: Mapping[Edge, int],
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    *,
    tolerance: float = 1e-12,
) -> bool:
    """Check the discrete first-order optimality condition.

    An integer allocation is optimal exactly when no one-unit transfer can
    improve it. Thus every removable last gain on an edge with count above one
    must be at least every addable next gain on every edge.
    """
    _validate_maps(coefficients, sensitivities)
    if set(allocations) != set(coefficients):
        raise ValueError("allocations must cover exactly the declared edge keys")
    if not isfinite(tolerance) or tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative and finite")

    effective = {
        edge: coefficients[edge] * sensitivities[edge]
        for edge in coefficients
    }
    for count in allocations.values():
        if not isinstance(count, int) or isinstance(count, bool):
            raise TypeError("allocation counts must be integers")
        if count < 1:
            raise ValueError("allocation counts must be at least one")

    largest_unselected = max(
        marginal_gain(effective[edge], allocations[edge])
        for edge in allocations
    )
    return _exchange_condition(
        allocations,
        effective,
        largest_unselected,
        tolerance=tolerance,
    )


def _exchange_condition(
    allocations: Mapping[Edge, int],
    effective: Mapping[Edge, float],
    largest_unselected: float,
    *,
    tolerance: float,
) -> bool:
    removable = [
        marginal_gain(effective[edge], count - 1)
        for edge, count in allocations.items()
        if count > 1
    ]
    if not removable:
        return True
    return min(removable) + tolerance >= largest_unselected


def _validate_problem(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    total_budget: int,
    tolerance: float,
) -> None:
    _validate_maps(coefficients, sensitivities)
    if not isinstance(total_budget, int) or isinstance(total_budget, bool):
        raise TypeError("total_budget must be an integer")
    if total_budget < len(coefficients):
        raise ValueError("total_budget must be at least the number of edges")
    if not isfinite(tolerance) or tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative and finite")


def _validate_maps(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
) -> None:
    if not coefficients:
        raise ValueError("coefficients must be nonempty")
    if set(coefficients) != set(sensitivities):
        raise ValueError("sensitivities must cover exactly the coefficient keys")
    for edge, coefficient in coefficients.items():
        _positive_finite(coefficient, "coefficient")
        _positive_finite(sensitivities[edge], "sensitivity")


def _positive_finite(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")
