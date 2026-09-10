"""Proposition 47: anytime-valid sequential witness-graph refinement.

P47 separates statistical validity from the adaptive experimental policy.  The
policy may decide which preparation to sample next, which induced graph to keep,
which candidate edge to inspect, and when to stop.  Validity is inherited from
simultaneous preparation-level confidence sequences that cover every local
sample size before the adaptive policy is evaluated.

This module implements deterministic pieces of that theorem: Basel alpha
spending, finite-family error allocation, edgewise regularity-margin envelopes,
post-selection by simultaneous lower bounds, and safe vertex pruning from
simultaneous upper bounds.

It does not establish quantum incompleteness, physical completeness, or
consciousness.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from math import isfinite, pi
from typing import TypeVar

Vertex = TypeVar("Vertex", bound=Hashable)
Edge = tuple[Vertex, Vertex]


@dataclass(frozen=True)
class EdgeMarginInterval:
    """Simultaneous interval for one population regularity margin."""

    lower: float
    upper: float


@dataclass(frozen=True)
class SequentialWitnessDecision:
    """Current sequential decision from simultaneous edge intervals."""

    status: str
    selected_edge: Edge | None
    selected_interval: EdgeMarginInterval | None


def basel_alpha_spend(local_sample_size: int, stream_alpha: float) -> float:
    """Return the P24 Basel alpha spend for one local sample size.

    Summing this quantity over all positive local sample sizes gives exactly
    ``stream_alpha``.  In P47 the schedule is applied separately to each
    preparation-level stream, after a finite-family allocation across streams.
    """
    if local_sample_size < 1:
        raise ValueError("local_sample_size must be a positive integer")
    _probability_level(stream_alpha, "stream_alpha")
    return 6.0 * stream_alpha / (pi**2 * local_sample_size**2)


def allocate_error_budget(
    keys: Sequence[Vertex],
    total_alpha: float,
    *,
    weights: Mapping[Vertex, float] | None = None,
) -> dict[Vertex, float]:
    """Allocate a finite total failure budget across declared streams.

    Equal allocation is used when ``weights`` is omitted.  Positive predeclared
    weights recover the weighted Bonferroni construction used throughout the
    finite-family branch of the repository.
    """
    declared = tuple(keys)
    if not declared:
        raise ValueError("keys must be nonempty")
    if len(set(declared)) != len(declared):
        raise ValueError("keys must be unique")
    _probability_level(total_alpha, "total_alpha")

    if weights is None:
        share = total_alpha / len(declared)
        return {key: share for key in declared}

    if set(weights) != set(declared):
        raise ValueError("weights must cover every and only declared key")
    total_weight = 0.0
    for weight in weights.values():
        _positive_finite(weight, "weight")
        total_weight += weight
    return {
        key: total_alpha * weights[key] / total_weight
        for key in declared
    }


def edge_margin_interval(
    empirical_target_distance: float,
    empirical_quantum_distance: float,
    target_radius_first: float,
    target_radius_second: float,
    quantum_radius_first: float,
    quantum_radius_second: float,
    lipschitz_constant: float,
) -> EdgeMarginInterval:
    """Return a valid envelope for ``M = d_Y - L d_Q``.

    The assumptions are the preparation-level simultaneous bounds

    ``TV(P_i, P_hat_i) <= epsilon_i`` and
    ``D(rho_i, rho_hat_i) <= r_i``.

    Triangle inequalities imply pairwise distance intervals.  Combining the
    smallest admissible target distance with the largest admissible quantum
    distance gives the lower regularity-margin bound; the reverse choices give
    the upper bound.
    """
    _unit_interval(empirical_target_distance, "empirical_target_distance")
    _unit_interval(empirical_quantum_distance, "empirical_quantum_distance")
    _nonnegative_finite(target_radius_first, "target_radius_first")
    _nonnegative_finite(target_radius_second, "target_radius_second")
    _nonnegative_finite(quantum_radius_first, "quantum_radius_first")
    _nonnegative_finite(quantum_radius_second, "quantum_radius_second")
    _nonnegative_finite(lipschitz_constant, "lipschitz_constant")

    target_error = target_radius_first + target_radius_second
    quantum_error = quantum_radius_first + quantum_radius_second

    target_lower = max(0.0, empirical_target_distance - target_error)
    target_upper = min(1.0, empirical_target_distance + target_error)
    quantum_lower = max(0.0, empirical_quantum_distance - quantum_error)
    quantum_upper = min(1.0, empirical_quantum_distance + quantum_error)

    lower = target_lower - lipschitz_constant * quantum_upper
    upper = target_upper - lipschitz_constant * quantum_lower
    return EdgeMarginInterval(lower=lower, upper=upper)


def simultaneous_edge_intervals(
    edges: Sequence[Edge],
    empirical_target_distances: Mapping[Edge, float],
    empirical_quantum_distances: Mapping[Edge, float],
    target_radii: Mapping[Vertex, float],
    quantum_radii: Mapping[Vertex, float],
    lipschitz_constants: Mapping[Edge, float],
) -> dict[Edge, EdgeMarginInterval]:
    """Build P47 intervals for a finite predeclared witness family."""
    declared_edges = tuple(edges)
    _validate_edges(declared_edges)
    edge_set = set(declared_edges)
    _exact_keys(empirical_target_distances, edge_set, "empirical_target_distances")
    _exact_keys(empirical_quantum_distances, edge_set, "empirical_quantum_distances")
    _exact_keys(lipschitz_constants, edge_set, "lipschitz_constants")

    vertices = {vertex for edge in declared_edges for vertex in edge}
    if set(target_radii) != vertices:
        raise ValueError("target_radii must cover every and only incident vertex")
    if set(quantum_radii) != vertices:
        raise ValueError("quantum_radii must cover every and only incident vertex")

    result: dict[Edge, EdgeMarginInterval] = {}
    for edge in declared_edges:
        first, second = edge
        result[edge] = edge_margin_interval(
            empirical_target_distances[edge],
            empirical_quantum_distances[edge],
            target_radii[first],
            target_radii[second],
            quantum_radii[first],
            quantum_radii[second],
            lipschitz_constants[edge],
        )
    return result


def select_largest_lower_bound(
    intervals: Mapping[Edge, EdgeMarginInterval],
) -> Edge | None:
    """Select the candidate with the largest simultaneous lower bound."""
    if not intervals:
        return None
    for edge, interval in intervals.items():
        _validate_edge(edge)
        _validate_interval(interval)
    return max(intervals, key=lambda edge: intervals[edge].lower)


def prunable_vertices(
    vertices: Sequence[Vertex],
    edges: Sequence[Edge],
    intervals: Mapping[Edge, EdgeMarginInterval],
    *,
    tolerance: float = 0.0,
) -> tuple[Vertex, ...]:
    """Return vertices whose every incident edge is certified negative.

    On the simultaneous P47 event, pruning such a vertex cannot remove a
    positive-margin witness from the declared edge family.  Isolated vertices
    are not marked as prunable because no statistical conclusion concerns them.
    """
    declared_vertices = tuple(vertices)
    if len(set(declared_vertices)) != len(declared_vertices):
        raise ValueError("vertices must be unique")
    _nonnegative_finite(tolerance, "tolerance")
    declared_edges = tuple(edges)
    _validate_edges(declared_edges)
    edge_set = set(declared_edges)
    if set(intervals) != edge_set:
        raise ValueError("intervals must cover every and only declared edge")

    vertex_set = set(declared_vertices)
    incident: dict[Vertex, list[EdgeMarginInterval]] = {
        vertex: [] for vertex in declared_vertices
    }
    for edge in declared_edges:
        first, second = edge
        if first not in vertex_set or second not in vertex_set:
            raise ValueError("edge endpoint is outside the declared vertex set")
        interval = intervals[edge]
        _validate_interval(interval)
        incident[first].append(interval)
        incident[second].append(interval)

    return tuple(
        vertex
        for vertex in declared_vertices
        if incident[vertex]
        and all(interval.upper < -tolerance for interval in incident[vertex])
    )


def sequential_witness_decision(
    intervals: Mapping[Edge, EdgeMarginInterval],
    *,
    tolerance: float = 0.0,
) -> SequentialWitnessDecision:
    """Return the current P47 stop/continue decision.

    ``certified-positive`` means the selected edge has a strictly positive
    simultaneous lower bound.  ``certified-no-positive-edge`` means every
    declared edge has a strictly negative simultaneous upper bound.  All other
    cases remain unresolved and should not be interpreted as evidence for
    either conclusion.
    """
    _nonnegative_finite(tolerance, "tolerance")
    if not intervals:
        return SequentialWitnessDecision(
            status="unresolved",
            selected_edge=None,
            selected_interval=None,
        )

    selected = select_largest_lower_bound(intervals)
    assert selected is not None
    selected_interval = intervals[selected]

    if selected_interval.lower > tolerance:
        return SequentialWitnessDecision(
            status="certified-positive",
            selected_edge=selected,
            selected_interval=selected_interval,
        )

    if all(interval.upper < -tolerance for interval in intervals.values()):
        return SequentialWitnessDecision(
            status="certified-no-positive-edge",
            selected_edge=selected,
            selected_interval=selected_interval,
        )

    return SequentialWitnessDecision(
        status="unresolved",
        selected_edge=selected,
        selected_interval=selected_interval,
    )


def _validate_edges(edges: tuple[Edge, ...]) -> None:
    seen: set[frozenset[Vertex]] = set()
    for edge in edges:
        _validate_edge(edge)
        key = frozenset(edge)
        if key in seen:
            raise ValueError("each undirected edge must be declared once")
        seen.add(key)


def _validate_edge(edge: Edge) -> None:
    if len(edge) != 2:
        raise ValueError("an edge must contain exactly two endpoints")
    if edge[0] == edge[1]:
        raise ValueError("self-edges are not allowed")


def _validate_interval(interval: EdgeMarginInterval) -> None:
    if not isfinite(interval.lower) or not isfinite(interval.upper):
        raise ValueError("interval endpoints must be finite")
    if interval.lower > interval.upper:
        raise ValueError("interval lower endpoint cannot exceed upper endpoint")


def _exact_keys(
    mapping: Mapping[Edge, float],
    expected: set[Edge],
    name: str,
) -> None:
    if set(mapping) != expected:
        raise ValueError(f"{name} must cover every and only declared edge")


def _probability_level(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0 or value >= 1.0:
        raise ValueError(f"{name} must lie strictly between zero and one")


def _unit_interval(value: float, name: str) -> None:
    if not isfinite(value) or value < 0.0 or value > 1.0:
        raise ValueError(f"{name} must lie in [0, 1]")


def _positive_finite(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")


def _nonnegative_finite(value: float, name: str) -> None:
    if not isfinite(value) or value < 0.0:
        raise ValueError(f"{name} must be nonnegative and finite")
