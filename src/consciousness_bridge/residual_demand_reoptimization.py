"""Proposition 53: residual-demand reoptimization after safe pruning.

P53 turns the static P52 threshold-saturation problem into a dynamic one.  At a
sequential state with active edge set E_t, edge thresholds N_e, and accumulated
preparation counts n_i, define the residual demand

    r_i(t) = max_{e in E_t, e incident to i} (N_e - n_i)_+.

Under total service capacity C, P52 applied to r(t) gives the exact optimal
remaining deterministic threshold-saturation time

    T_rem(t) = sum_i r_i(t) / C.

If later counts only increase and P47 safe pruning only removes edges, every
residual demand is nonincreasing.  The exact decrease in optimal remaining time
is the released total residual demand divided by C.

This is a deterministic scheduling theorem.  It is not a claim about the actual
random statistical stopping time.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from math import isfinite
from typing import TypeVar

from .capacity_optimal_service_allocation import optimal_service_allocation

Vertex = TypeVar("Vertex", bound=Hashable)
Edge = tuple[Vertex, Vertex]


@dataclass(frozen=True)
class ResidualState:
    """P53 residual-demand state for one active witness graph."""

    residual_demands: dict[Vertex, float]
    total_residual_demand: float
    optimal_remaining_time: float
    optimal_service_shares: dict[Vertex, float]


@dataclass(frozen=True)
class ReoptimizationCertificate:
    """Exact monotonicity and released-time certificate between two states."""

    before: ResidualState
    after: ResidualState
    componentwise_nonincreasing: bool
    released_residual_demand: float
    released_optimal_time: float


def residual_vertex_demands(
    vertices: Sequence[Vertex],
    active_edges: Sequence[Edge],
    edge_thresholds: Mapping[Edge, float],
    local_counts: Mapping[Vertex, float],
) -> dict[Vertex, float]:
    """Return minimal remaining vertex demands for the active edge family."""
    declared_vertices = tuple(vertices)
    if not declared_vertices:
        raise ValueError("vertices must be nonempty")
    if len(set(declared_vertices)) != len(declared_vertices):
        raise ValueError("vertices must be unique")
    if set(local_counts) != set(declared_vertices):
        raise ValueError("local_counts must cover every and only declared vertex")
    for count in local_counts.values():
        _nonnegative_finite(count, "local count")

    edges = tuple(active_edges)
    _validate_edges(edges)
    if set(edge_thresholds) != set(edges):
        raise ValueError("edge_thresholds must cover every and only active edge")

    vertex_set = set(declared_vertices)
    residual = {vertex: 0.0 for vertex in declared_vertices}
    for edge in edges:
        first, second = edge
        if first not in vertex_set or second not in vertex_set:
            raise ValueError("edge endpoint is outside the declared vertex set")
        threshold = edge_thresholds[edge]
        _positive_finite(threshold, "edge threshold")
        for vertex in edge:
            need = max(0.0, threshold - local_counts[vertex])
            residual[vertex] = max(residual[vertex], need)
    return residual


def residual_state(
    vertices: Sequence[Vertex],
    active_edges: Sequence[Edge],
    edge_thresholds: Mapping[Edge, float],
    local_counts: Mapping[Vertex, float],
    *,
    capacity: float = 1.0,
) -> ResidualState:
    """Return the exact P52 reoptimization of the current residual problem."""
    _positive_finite(capacity, "capacity")
    residual = residual_vertex_demands(
        vertices,
        active_edges,
        edge_thresholds,
        local_counts,
    )
    allocation = optimal_service_allocation(residual, capacity=capacity)
    return ResidualState(
        residual_demands=residual,
        total_residual_demand=allocation.total_demand,
        optimal_remaining_time=allocation.completion_time,
        optimal_service_shares=allocation.shares,
    )


def reoptimization_certificate(
    vertices: Sequence[Vertex],
    before_edges: Sequence[Edge],
    after_edges: Sequence[Edge],
    edge_thresholds: Mapping[Edge, float],
    before_counts: Mapping[Vertex, float],
    after_counts: Mapping[Vertex, float],
    *,
    capacity: float = 1.0,
) -> ReoptimizationCertificate:
    """Certify monotone residual improvement after sampling and safe pruning.

    ``after_edges`` must be a subset of ``before_edges`` and every local count
    must be nondecreasing.  Thresholds are supplied for the original before-edge
    family and are restricted automatically for the after state.
    """
    before_tuple = tuple(before_edges)
    after_tuple = tuple(after_edges)
    _validate_edges(before_tuple)
    _validate_edges(after_tuple)
    if not set(after_tuple).issubset(set(before_tuple)):
        raise ValueError("after_edges must be a subset of before_edges")
    if set(edge_thresholds) != set(before_tuple):
        raise ValueError("edge_thresholds must cover every and only before edge")

    declared_vertices = tuple(vertices)
    if set(before_counts) != set(declared_vertices):
        raise ValueError("before_counts must cover every and only declared vertex")
    if set(after_counts) != set(declared_vertices):
        raise ValueError("after_counts must cover every and only declared vertex")
    for vertex in declared_vertices:
        _nonnegative_finite(before_counts[vertex], "before count")
        _nonnegative_finite(after_counts[vertex], "after count")
        if after_counts[vertex] < before_counts[vertex]:
            raise ValueError("local counts must be nondecreasing")

    before = residual_state(
        declared_vertices,
        before_tuple,
        edge_thresholds,
        before_counts,
        capacity=capacity,
    )
    after_thresholds = {edge: edge_thresholds[edge] for edge in after_tuple}
    after = residual_state(
        declared_vertices,
        after_tuple,
        after_thresholds,
        after_counts,
        capacity=capacity,
    )

    monotone = all(
        after.residual_demands[vertex] <= before.residual_demands[vertex]
        for vertex in declared_vertices
    )
    released = before.total_residual_demand - after.total_residual_demand
    released_time = before.optimal_remaining_time - after.optimal_remaining_time
    return ReoptimizationCertificate(
        before=before,
        after=after,
        componentwise_nonincreasing=monotone,
        released_residual_demand=released,
        released_optimal_time=released_time,
    )


def pruning_release_by_vertex(
    vertices: Sequence[Vertex],
    before_edges: Sequence[Edge],
    after_edges: Sequence[Edge],
    edge_thresholds: Mapping[Edge, float],
    local_counts: Mapping[Vertex, float],
) -> dict[Vertex, float]:
    """Return the exact residual demand released by pruning alone."""
    before = residual_vertex_demands(
        vertices,
        before_edges,
        edge_thresholds,
        local_counts,
    )
    after_tuple = tuple(after_edges)
    if not set(after_tuple).issubset(set(before_edges)):
        raise ValueError("after_edges must be a subset of before_edges")
    after_thresholds = {edge: edge_thresholds[edge] for edge in after_tuple}
    after = residual_vertex_demands(
        vertices,
        after_tuple,
        after_thresholds,
        local_counts,
    )
    return {vertex: before[vertex] - after[vertex] for vertex in before}


def sample_release_by_vertex(
    vertices: Sequence[Vertex],
    active_edges: Sequence[Edge],
    edge_thresholds: Mapping[Edge, float],
    before_counts: Mapping[Vertex, float],
    after_counts: Mapping[Vertex, float],
) -> dict[Vertex, float]:
    """Return the exact residual demand released by additional samples alone."""
    declared = tuple(vertices)
    if set(before_counts) != set(declared) or set(after_counts) != set(declared):
        raise ValueError("count mappings must cover every declared vertex")
    for vertex in declared:
        if after_counts[vertex] < before_counts[vertex]:
            raise ValueError("local counts must be nondecreasing")
    before = residual_vertex_demands(
        declared,
        active_edges,
        edge_thresholds,
        before_counts,
    )
    after = residual_vertex_demands(
        declared,
        active_edges,
        edge_thresholds,
        after_counts,
    )
    return {vertex: before[vertex] - after[vertex] for vertex in declared}


def _validate_edges(edges: tuple[Edge, ...]) -> None:
    seen: set[frozenset[Vertex]] = set()
    for edge in edges:
        if len(edge) != 2:
            raise ValueError("an edge must contain exactly two endpoints")
        if edge[0] == edge[1]:
            raise ValueError("self-edges are not allowed")
        key = frozenset(edge)
        if key in seen:
            raise ValueError("each undirected edge must be declared once")
        seen.add(key)


def _positive_finite(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")


def _nonnegative_finite(value: float, name: str) -> None:
    if not isfinite(value) or value < 0.0:
        raise ValueError(f"{name} must be nonnegative and finite")
