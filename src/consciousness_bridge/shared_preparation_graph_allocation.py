"""Proposition 45: shared-preparation graph allocation.

P45 treats preparations as vertices and candidate regularity witnesses as edges.
A preparation-level quantum or target sample stream can therefore improve every
incident candidate edge. The module provides the exact deterministic allocation
geometry, single-edge closed form, and KKT certificate utilities used by the
proposition.

The result is conditional on valid preparation-level uncertainty radii and on a
declared Lipschitz bridge class. It does not establish quantum incompleteness,
physical completeness, or consciousness.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from math import isclose
from typing import TypeVar

Preparation = TypeVar("Preparation", bound=Hashable)


@dataclass(frozen=True)
class GraphEdge:
    """One candidate preparation-pair regularity witness."""

    first: Preparation
    second: Preparation
    population_gap: float
    lipschitz_constant: float


@dataclass(frozen=True)
class EdgeBudget:
    """Uncertainty consumption and remaining population gap for one edge."""

    uncertainty_cost: float
    slack: float
    feasible: bool


@dataclass(frozen=True)
class SingleEdgeAllocation:
    """Unique continuous minimum-cost uncertainty allocation for one edge."""

    first_target_radius: float
    second_target_radius: float
    first_quantum_radius: float
    second_quantum_radius: float
    minimum_cost: float


def edge_uncertainty_budget(
    edge: GraphEdge,
    target_radii: Mapping[Preparation, float],
    quantum_radii: Mapping[Preparation, float],
    *,
    tolerance: float = 1e-12,
) -> EdgeBudget:
    """Return the P42 nonuniform preparation-level uncertainty budget.

    P42 gives, for edge (i,j),

        M_hat >= Delta_ij
                 - 2(eps_i + eps_j)
                 - 2 L_ij (r_i + r_j).

    A strictly positive slack is therefore sufficient for the empirical
    regularity obstruction on the declared simultaneous confidence event.
    """
    _validate_edge(edge)
    _nonnegative(tolerance, "tolerance")
    eps_first = _radius(target_radii, edge.first, "target_radii")
    eps_second = _radius(target_radii, edge.second, "target_radii")
    r_first = _radius(quantum_radii, edge.first, "quantum_radii")
    r_second = _radius(quantum_radii, edge.second, "quantum_radii")

    cost = 2.0 * (eps_first + eps_second) + 2.0 * edge.lipschitz_constant * (
        r_first + r_second
    )
    slack = edge.population_gap - cost
    return EdgeBudget(
        uncertainty_cost=cost,
        slack=slack,
        feasible=slack > tolerance,
    )


def graph_feasibility(
    edges: Sequence[GraphEdge],
    target_radii: Mapping[Preparation, float],
    quantum_radii: Mapping[Preparation, float],
    *,
    tolerance: float = 1e-12,
) -> dict[tuple[Preparation, Preparation], EdgeBudget]:
    """Audit every declared graph edge under one shared vertex allocation."""
    edge_tuple = tuple(edges)
    if not edge_tuple:
        raise ValueError("at least one edge is required")
    _validate_unique_edges(edge_tuple)
    return {
        (edge.first, edge.second): edge_uncertainty_budget(
            edge,
            target_radii,
            quantum_radii,
            tolerance=tolerance,
        )
        for edge in edge_tuple
    }


def weighted_sampling_cost(
    target_radii: Mapping[Preparation, float],
    quantum_radii: Mapping[Preparation, float],
    target_weights: Mapping[Preparation, float],
    quantum_weights: Mapping[Preparation, float],
) -> float:
    """Return sum_x w_Y,x / eps_x^2 + w_Q,x / r_x^2.

    If eps_x = a_Y,x / sqrt(n_Y,x) and r_x = a_Q,x / sqrt(n_Q,x),
    then setting w_Y,x = c_Y,x a_Y,x^2 and w_Q,x = c_Q,x a_Q,x^2
    makes this objective the declared weighted sampling cost.
    """
    vertices = set(target_radii) | set(quantum_radii)
    if set(target_radii) != vertices or set(quantum_radii) != vertices:
        raise ValueError("target_radii and quantum_radii must cover the same vertices")
    if set(target_weights) != vertices or set(quantum_weights) != vertices:
        raise ValueError("all weight tables must cover exactly the declared vertices")

    total = 0.0
    for vertex in vertices:
        eps = _positive(target_radii[vertex], "target radius")
        radius = _positive(quantum_radii[vertex], "quantum radius")
        wy = _positive(target_weights[vertex], "target weight")
        wq = _positive(quantum_weights[vertex], "quantum weight")
        total += wy / (eps * eps) + wq / (radius * radius)
    return total


def single_edge_optimal_allocation(
    edge: GraphEdge,
    first_target_weight: float,
    second_target_weight: float,
    first_quantum_weight: float,
    second_quantum_weight: float,
) -> SingleEdgeAllocation:
    """Return the exact continuous P45 allocation for one edge.

    The problem is

        minimize sum_l w_l / u_l^2
        subject to sum_l a_l u_l <= Delta,

    with coefficients (2, 2, 2L, 2L). Strict convexity gives a unique optimum.
    """
    _validate_edge(edge)
    weights = (
        _positive(first_target_weight, "first_target_weight"),
        _positive(second_target_weight, "second_target_weight"),
        _positive(first_quantum_weight, "first_quantum_weight"),
        _positive(second_quantum_weight, "second_quantum_weight"),
    )
    if edge.lipschitz_constant <= 0.0:
        raise ValueError("single-edge four-stream allocation requires positive L")
    coefficients = (
        2.0,
        2.0,
        2.0 * edge.lipschitz_constant,
        2.0 * edge.lipschitz_constant,
    )
    scale_sum = sum(
        coefficient ** (2.0 / 3.0) * weight ** (1.0 / 3.0)
        for coefficient, weight in zip(coefficients, weights, strict=True)
    )
    radii = tuple(
        edge.population_gap
        * (weight / coefficient) ** (1.0 / 3.0)
        / scale_sum
        for coefficient, weight in zip(coefficients, weights, strict=True)
    )
    minimum_cost = scale_sum**3 / edge.population_gap**2
    return SingleEdgeAllocation(
        first_target_radius=radii[0],
        second_target_radius=radii[1],
        first_quantum_radius=radii[2],
        second_quantum_radius=radii[3],
        minimum_cost=minimum_cost,
    )


def kkt_stationarity_residuals(
    edges: Sequence[GraphEdge],
    target_radii: Mapping[Preparation, float],
    quantum_radii: Mapping[Preparation, float],
    target_weights: Mapping[Preparation, float],
    quantum_weights: Mapping[Preparation, float],
    edge_multipliers: Mapping[tuple[Preparation, Preparation], float],
) -> dict[Preparation, tuple[float, float]]:
    """Return target and quantum KKT stationarity residuals at each vertex.

    With edge constraints

        2(eps_i+eps_j) + 2 L_e(r_i+r_j) <= Delta_e,

    stationarity is

        w_Y,x / eps_x^3 = sum_{e incident x} lambda_e,
        w_Q,x / r_x^3 = sum_{e incident x} lambda_e L_e.

    Zero residuals, primal feasibility, nonnegative multipliers, and
    complementary slackness certify the unique optimum of the convex problem.
    """
    edge_tuple = tuple(edges)
    if not edge_tuple:
        raise ValueError("at least one edge is required")
    _validate_unique_edges(edge_tuple)
    vertices = {edge.first for edge in edge_tuple} | {edge.second for edge in edge_tuple}
    for table, name in (
        (target_radii, "target_radii"),
        (quantum_radii, "quantum_radii"),
        (target_weights, "target_weights"),
        (quantum_weights, "quantum_weights"),
    ):
        if set(table) != vertices:
            raise ValueError(f"{name} must cover exactly the graph vertices")

    multiplier_by_edge: dict[tuple[Preparation, Preparation], float] = {}
    for edge in edge_tuple:
        key = (edge.first, edge.second)
        reverse = (edge.second, edge.first)
        if key in edge_multipliers:
            value = edge_multipliers[key]
        elif reverse in edge_multipliers:
            value = edge_multipliers[reverse]
        else:
            raise ValueError("edge_multipliers must cover every graph edge")
        multiplier_by_edge[key] = _nonnegative(value, "edge multiplier")

    residuals: dict[Preparation, tuple[float, float]] = {}
    for vertex in vertices:
        eps = _positive(target_radii[vertex], "target radius")
        radius = _positive(quantum_radii[vertex], "quantum radius")
        wy = _positive(target_weights[vertex], "target weight")
        wq = _positive(quantum_weights[vertex], "quantum weight")
        target_dual = 0.0
        quantum_dual = 0.0
        for edge in edge_tuple:
            if vertex == edge.first or vertex == edge.second:
                multiplier = multiplier_by_edge[(edge.first, edge.second)]
                target_dual += multiplier
                quantum_dual += multiplier * edge.lipschitz_constant
        residuals[vertex] = (
            wy / eps**3 - target_dual,
            wq / radius**3 - quantum_dual,
        )
    return residuals


def kkt_certificate_holds(
    edges: Sequence[GraphEdge],
    target_radii: Mapping[Preparation, float],
    quantum_radii: Mapping[Preparation, float],
    target_weights: Mapping[Preparation, float],
    quantum_weights: Mapping[Preparation, float],
    edge_multipliers: Mapping[tuple[Preparation, Preparation], float],
    *,
    tolerance: float = 1e-9,
) -> bool:
    """Check primal feasibility, stationarity, dual feasibility, and slackness."""
    _nonnegative(tolerance, "tolerance")
    budgets = graph_feasibility(
        edges,
        target_radii,
        quantum_radii,
        tolerance=-0.0,
    )
    if any(budget.slack < -tolerance for budget in budgets.values()):
        return False
    residuals = kkt_stationarity_residuals(
        edges,
        target_radii,
        quantum_radii,
        target_weights,
        quantum_weights,
        edge_multipliers,
    )
    if any(
        abs(component) > tolerance
        for pair in residuals.values()
        for component in pair
    ):
        return False

    for edge in edges:
        key = (edge.first, edge.second)
        reverse = (edge.second, edge.first)
        multiplier = edge_multipliers.get(key, edge_multipliers.get(reverse))
        if multiplier is None or multiplier < -tolerance:
            return False
        slack = budgets[key].slack
        if not isclose(multiplier * slack, 0.0, abs_tol=tolerance):
            return False
    return True


def _validate_edge(edge: GraphEdge) -> None:
    if edge.first == edge.second:
        raise ValueError("edge endpoints must be distinct")
    _positive(edge.population_gap, "population_gap")
    _nonnegative(edge.lipschitz_constant, "lipschitz_constant")


def _validate_unique_edges(edges: tuple[GraphEdge, ...]) -> None:
    seen: set[frozenset[Preparation]] = set()
    for edge in edges:
        _validate_edge(edge)
        key = frozenset((edge.first, edge.second))
        if key in seen:
            raise ValueError("graph edges must be unique as unordered pairs")
        seen.add(key)


def _radius(table: Mapping[Preparation, float], key: Preparation, name: str) -> float:
    if key not in table:
        raise ValueError(f"{name} is missing a graph endpoint")
    return _nonnegative(table[key], name)


def _positive(value: float, name: str) -> float:
    if value <= 0.0:
        raise ValueError(f"{name} must be positive")
    return value


def _nonnegative(value: float, name: str) -> float:
    if value < 0.0:
        raise ValueError(f"{name} must be nonnegative")
    return value
