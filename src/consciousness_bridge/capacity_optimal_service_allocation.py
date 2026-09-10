"""Proposition 52: capacity-optimal service allocation for witness graphs.

P52 solves the deterministic scheduling problem obtained after P48 has supplied
local sample thresholds for every declared witness edge.

For complete-family threshold saturation, preparation i needs

    d_i = max{N_e : e is incident to i}.

Under a unit global sampling capacity, a continuous service allocation pi_i
with sum pi_i <= 1 has completion time

    T(pi) = max_i d_i / pi_i.

P52 proves the unique minimax allocation

    pi_i* = d_i / sum_j d_j,

with optimum T* = sum_i d_i.

For integer demands, an exact discrete quota schedule of length sum_i d_i is
also optimal for threshold saturation because every global round can contribute
at most one preparation-level sample.

This is a threshold-scheduling theorem, not a claim that the resulting policy
minimizes the actual random statistical stopping time.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from math import isfinite
from typing import TypeVar

from .gap_stopping_complexity import EdgeStoppingComplexity

Vertex = TypeVar("Vertex", bound=Hashable)
Edge = tuple[Vertex, Vertex]


@dataclass(frozen=True)
class ServiceAllocation:
    """Exact P52 minimax service allocation for positive vertex demands."""

    shares: dict[Vertex, float]
    total_demand: float
    completion_time: float


@dataclass(frozen=True)
class QuotaScheduleCertificate:
    """Deterministic certificate for an exact integer quota schedule."""

    schedule: tuple[Vertex, ...]
    demands: dict[Vertex, int]
    length: int
    optimal_length: int
    is_optimal: bool


def vertex_threshold_demands(
    vertices: Sequence[Vertex],
    edges: Sequence[Edge],
    edge_thresholds: Mapping[Edge, int],
) -> dict[Vertex, int]:
    """Return the minimal per-vertex demands sufficient for all edge thresholds.

    Edge e={i,j} with threshold N_e requires both endpoints to accumulate at
    least N_e local samples.  Therefore vertex i must reach the largest N_e among
    its incident edges.  Isolated vertices receive demand zero.
    """
    declared_vertices = tuple(vertices)
    if not declared_vertices:
        raise ValueError("vertices must be nonempty")
    if len(set(declared_vertices)) != len(declared_vertices):
        raise ValueError("vertices must be unique")

    declared_edges = tuple(edges)
    _validate_edges(declared_edges)
    if set(edge_thresholds) != set(declared_edges):
        raise ValueError("edge_thresholds must cover every and only declared edge")

    vertex_set = set(declared_vertices)
    demands = {vertex: 0 for vertex in declared_vertices}
    for edge in declared_edges:
        first, second = edge
        if first not in vertex_set or second not in vertex_set:
            raise ValueError("edge endpoint is outside the declared vertex set")
        threshold = edge_thresholds[edge]
        if threshold < 1:
            raise ValueError("edge thresholds must be positive integers")
        demands[first] = max(demands[first], threshold)
        demands[second] = max(demands[second], threshold)
    return demands


def vertex_threshold_demands_from_bounds(
    vertices: Sequence[Vertex],
    bounds: Mapping[Edge, EdgeStoppingComplexity],
) -> dict[Vertex, int]:
    """Build P52 vertex demands directly from finite P48 edge bounds."""
    edge_thresholds: dict[Edge, int] = {}
    for edge, bound in bounds.items():
        if edge != bound.edge:
            raise ValueError("bound edge must match its mapping key")
        if bound.local_samples is None:
            raise ValueError("every edge must have a finite local-sample threshold")
        edge_thresholds[edge] = bound.local_samples
    return vertex_threshold_demands(vertices, tuple(bounds), edge_thresholds)


def optimal_service_allocation(
    demands: Mapping[Vertex, float],
    *,
    capacity: float = 1.0,
) -> ServiceAllocation:
    """Return the unique minimax continuous service allocation.

    For positive demands d_i and service shares pi_i >= 0 satisfying
    sum_i pi_i <= capacity, minimize max_i d_i/pi_i.  Zero-demand vertices are
    assigned zero service.  The unique optimum on the positive-demand support is

        pi_i = capacity * d_i / sum_j d_j,

    with completion time sum_j d_j / capacity.
    """
    _positive_finite(capacity, "capacity")
    if not demands:
        raise ValueError("demands must be nonempty")

    positive: dict[Vertex, float] = {}
    for vertex, demand in demands.items():
        _nonnegative_finite(demand, "demand")
        if demand > 0.0:
            positive[vertex] = float(demand)

    shares = {vertex: 0.0 for vertex in demands}
    if not positive:
        return ServiceAllocation(
            shares=shares,
            total_demand=0.0,
            completion_time=0.0,
        )

    total = sum(positive.values())
    for vertex, demand in positive.items():
        shares[vertex] = capacity * demand / total

    return ServiceAllocation(
        shares=shares,
        total_demand=total,
        completion_time=total / capacity,
    )


def completion_time(
    demands: Mapping[Vertex, float],
    shares: Mapping[Vertex, float],
) -> float:
    """Return max_i d_i/pi_i, treating unserved positive demand as infinity."""
    if set(demands) != set(shares):
        raise ValueError("demands and shares must have identical keys")
    if not demands:
        raise ValueError("demands must be nonempty")

    worst = 0.0
    for vertex, demand in demands.items():
        _nonnegative_finite(demand, "demand")
        share = shares[vertex]
        _nonnegative_finite(share, "share")
        if demand == 0.0:
            continue
        if share == 0.0:
            return float("inf")
        worst = max(worst, demand / share)
    return worst


def capacity_feasible(
    shares: Mapping[Vertex, float],
    *,
    capacity: float = 1.0,
    tolerance: float = 1e-12,
) -> bool:
    """Return whether nonnegative service shares respect total capacity."""
    _positive_finite(capacity, "capacity")
    _nonnegative_finite(tolerance, "tolerance")
    total = 0.0
    for share in shares.values():
        if not isfinite(share) or share < 0.0:
            return False
        total += share
    return total <= capacity + tolerance


def threshold_saturation_lower_bound(
    demands: Mapping[Vertex, float],
    *,
    capacity: float = 1.0,
) -> float:
    """Return the universal lower bound sum_i d_i / capacity.

    For any feasible service allocation with completion time T,

        d_i <= T pi_i

    for every positive-demand vertex.  Summing gives

        sum_i d_i <= T sum_i pi_i <= T * capacity.
    """
    _positive_finite(capacity, "capacity")
    if not demands:
        raise ValueError("demands must be nonempty")
    total = 0.0
    for demand in demands.values():
        _nonnegative_finite(demand, "demand")
        total += demand
    return total / capacity


def exact_quota_schedule(
    demands: Mapping[Vertex, int],
    *,
    order: Sequence[Vertex] | None = None,
) -> QuotaScheduleCertificate:
    """Construct an exact unit-capacity schedule for integer vertex demands.

    The schedule contains each vertex exactly d_i times.  Its length is
    sum_i d_i, which is also a lower bound under unit capacity, so it is optimal
    for deterministic threshold saturation.
    """
    if not demands:
        raise ValueError("demands must be nonempty")

    normalized: dict[Vertex, int] = {}
    for vertex, demand in demands.items():
        if not isinstance(demand, int) or isinstance(demand, bool) or demand < 0:
            raise ValueError("integer demands must be nonnegative integers")
        normalized[vertex] = demand

    if order is None:
        declared_order = tuple(demands)
    else:
        declared_order = tuple(order)
        if len(set(declared_order)) != len(declared_order):
            raise ValueError("order must contain unique vertices")
        if set(declared_order) != set(demands):
            raise ValueError("order must contain every and only demand vertex")

    remaining = dict(normalized)
    schedule: list[Vertex] = []
    while any(value > 0 for value in remaining.values()):
        for vertex in declared_order:
            if remaining[vertex] > 0:
                schedule.append(vertex)
                remaining[vertex] -= 1

    optimum = sum(normalized.values())
    return QuotaScheduleCertificate(
        schedule=tuple(schedule),
        demands=normalized,
        length=len(schedule),
        optimal_length=optimum,
        is_optimal=len(schedule) == optimum,
    )


def schedule_counts(schedule: Sequence[Vertex]) -> dict[Vertex, int]:
    """Count selections in a realized unit-capacity schedule."""
    counts: dict[Vertex, int] = {}
    for vertex in schedule:
        counts[vertex] = counts.get(vertex, 0) + 1
    return counts


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
