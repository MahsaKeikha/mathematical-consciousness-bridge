"""Proposition 46: budget-constrained witness-graph selection.

This module treats preparations as graph vertices and candidate regularity witnesses
as weighted edges. A witness edge is available only when both endpoint
preparations are selected. The resulting budgeted induced-edge problem is a
combinatorial design layer built on top of P45.

The module provides exact enumeration for small instances and a cheap certified
upper bound based on full weighted degrees and fractional knapsack relaxation.
It does not establish quantum incompleteness, physical completeness, or
consciousness.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import isfinite
from typing import Hashable, Mapping, Sequence, TypeVar

Vertex = TypeVar("Vertex", bound=Hashable)
Edge = tuple[Vertex, Vertex]


@dataclass(frozen=True)
class BudgetedWitnessSelection:
    """Exact small-instance solution and a posteriori optimality certificate."""

    selected_vertices: tuple[Vertex, ...]
    selected_cost: float
    induced_edge_value: float
    degree_relaxation_upper_bound: float
    optimality_gap_upper_bound: float


def induced_edge_value(
    selected_vertices: Sequence[Vertex],
    edge_weights: Mapping[Edge, float],
) -> float:
    """Return total weight of edges whose two endpoints are selected."""
    selected = set(selected_vertices)
    total = 0.0
    for (first, second), weight in edge_weights.items():
        _validate_edge(first, second)
        _nonnegative_finite(weight, "edge weight")
        if first in selected and second in selected:
            total += weight
    return total


def selected_vertex_cost(
    selected_vertices: Sequence[Vertex],
    vertex_costs: Mapping[Vertex, float],
) -> float:
    """Return total declared measurement cost of selected preparations."""
    selected = tuple(selected_vertices)
    if len(set(selected)) != len(selected):
        raise ValueError("selected_vertices must be unique")
    total = 0.0
    for vertex in selected:
        if vertex not in vertex_costs:
            raise ValueError("selected vertex is missing a declared cost")
        cost = vertex_costs[vertex]
        _positive_finite(cost, "vertex cost")
        total += cost
    return total


def weighted_degrees(
    vertices: Sequence[Vertex],
    edge_weights: Mapping[Edge, float],
) -> dict[Vertex, float]:
    """Return each vertex's full-graph weighted degree."""
    declared = tuple(vertices)
    _validate_vertices(declared)
    vertex_set = set(declared)
    degree = {vertex: 0.0 for vertex in declared}
    seen: set[frozenset[Vertex]] = set()
    for (first, second), weight in edge_weights.items():
        _validate_edge(first, second)
        _nonnegative_finite(weight, "edge weight")
        if first not in vertex_set or second not in vertex_set:
            raise ValueError("edge endpoint is outside the declared vertex set")
        key = frozenset((first, second))
        if key in seen:
            raise ValueError("edge_weights must contain each undirected edge once")
        seen.add(key)
        degree[first] += weight
        degree[second] += weight
    return degree


def fractional_degree_upper_bound(
    vertices: Sequence[Vertex],
    vertex_costs: Mapping[Vertex, float],
    edge_weights: Mapping[Edge, float],
    budget: float,
) -> float:
    """Upper-bound the best induced-edge value under the vertex budget.

    For any selected set S,

        2 F(S) <= sum_{i in S} d_i,

    where d_i is the full weighted degree. Maximizing the right side under the
    same vertex budget is a 0-1 knapsack problem. Its fractional relaxation is
    solved by sorting d_i / c_i, giving a computable upper bound. The result is
    also clipped by the total edge weight.
    """
    declared = tuple(vertices)
    _validate_vertices(declared)
    _nonnegative_finite(budget, "budget")
    _validate_cost_table(declared, vertex_costs)
    degree = weighted_degrees(declared, edge_weights)

    remaining = budget
    relaxed_degree_value = 0.0
    ranked = sorted(
        declared,
        key=lambda vertex: degree[vertex] / vertex_costs[vertex],
        reverse=True,
    )
    for vertex in ranked:
        if remaining <= 0.0:
            break
        cost = vertex_costs[vertex]
        fraction = min(1.0, remaining / cost)
        relaxed_degree_value += fraction * degree[vertex]
        remaining -= fraction * cost

    total_edge_weight = sum(edge_weights.values())
    return min(total_edge_weight, 0.5 * relaxed_degree_value)


def exact_budgeted_witness_selection(
    vertices: Sequence[Vertex],
    vertex_costs: Mapping[Vertex, float],
    edge_weights: Mapping[Edge, float],
    budget: float,
    *,
    max_vertices: int = 24,
    tolerance: float = 1e-12,
) -> BudgetedWitnessSelection:
    """Solve the budgeted induced-edge problem exactly by subset enumeration.

    This routine is intentionally restricted to small graphs because P46 proves
    that the decision problem is NP-hard. Ties are broken by lower cost and then
    by fewer selected vertices.
    """
    declared = tuple(vertices)
    _validate_vertices(declared)
    _nonnegative_finite(budget, "budget")
    if max_vertices < 0:
        raise ValueError("max_vertices must be nonnegative")
    if len(declared) > max_vertices:
        raise ValueError("exact enumeration exceeds max_vertices")
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")
    _validate_cost_table(declared, vertex_costs)
    weighted_degrees(declared, edge_weights)

    best_vertices: tuple[Vertex, ...] = ()
    best_cost = 0.0
    best_value = 0.0

    for size in range(len(declared) + 1):
        for subset in combinations(declared, size):
            cost = sum(vertex_costs[vertex] for vertex in subset)
            if cost > budget + tolerance:
                continue
            value = induced_edge_value(subset, edge_weights)
            better_value = value > best_value + tolerance
            equal_value = abs(value - best_value) <= tolerance
            better_tie = equal_value and (
                cost < best_cost - tolerance
                or (abs(cost - best_cost) <= tolerance and len(subset) < len(best_vertices))
            )
            if better_value or better_tie:
                best_vertices = subset
                best_cost = cost
                best_value = value

    upper = fractional_degree_upper_bound(
        declared,
        vertex_costs,
        edge_weights,
        budget,
    )
    gap = max(0.0, upper - best_value)
    return BudgetedWitnessSelection(
        selected_vertices=best_vertices,
        selected_cost=best_cost,
        induced_edge_value=best_value,
        degree_relaxation_upper_bound=upper,
        optimality_gap_upper_bound=gap,
    )


def _validate_vertices(vertices: tuple[Vertex, ...]) -> None:
    if len(set(vertices)) != len(vertices):
        raise ValueError("vertices must be unique")


def _validate_cost_table(
    vertices: tuple[Vertex, ...],
    vertex_costs: Mapping[Vertex, float],
) -> None:
    if set(vertex_costs) != set(vertices):
        raise ValueError("vertex_costs must cover every and only declared vertex")
    for cost in vertex_costs.values():
        _positive_finite(cost, "vertex cost")


def _validate_edge(first: Vertex, second: Vertex) -> None:
    if first == second:
        raise ValueError("self-edges are not allowed")


def _positive_finite(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")


def _nonnegative_finite(value: float, name: str) -> None:
    if not isfinite(value) or value < 0.0:
        raise ValueError(f"{name} must be nonnegative and finite")
