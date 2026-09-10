"""Proposition 48: gap-dependent stopping complexity for P47 witness graphs.

P48 converts the qualitative eventual-detection statement in P47 into an
explicit sufficient epoch bound under a declared envelope of the form

    radius(n) <= A * sqrt(log(B * n**2) / n).

The result is deliberately a sufficient high-probability stopping bound, not a
minimax lower bound and not a claim of optimal adaptive sampling.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from math import ceil, isfinite, log, sqrt
from typing import TypeVar

Vertex = TypeVar("Vertex", bound=Hashable)
Edge = tuple[Vertex, Vertex]


@dataclass(frozen=True)
class EdgeStoppingComplexity:
    """Sufficient local-count bound for one nonzero population margin."""

    edge: Edge
    margin: float
    gap: float
    amplitude: float
    log_factor: float
    local_samples: int | None


@dataclass(frozen=True)
class SequentialStoppingBound:
    """Finite-family P48 stopping conclusion."""

    status: str
    epochs: int | None
    controlling_edges: tuple[Edge, ...]


def uncertainty_envelope(
    local_samples: int,
    amplitude: float,
    log_factor: float,
) -> float:
    """Return ``A sqrt(log(B n^2) / n)`` for a declared P48 envelope."""
    if local_samples < 1:
        raise ValueError("local_samples must be a positive integer")
    _nonnegative_finite(amplitude, "amplitude")
    _log_factor(log_factor)
    if amplitude == 0.0:
        return 0.0
    return amplitude * sqrt(
        log(log_factor * local_samples**2) / local_samples
    )


def required_local_samples(
    gap: float,
    amplitude: float,
    log_factor: float,
) -> int:
    """Return an explicit sufficient local count for sign certification.

    If the P47 endpoint uncertainty proxy obeys

    ``U_e(n) <= A_e sqrt(log(B_e n^2) / n)``,

    this function returns a positive integer ``N_e`` for which

    ``U_e(n) < gap / 2`` for every ``n >= N_e``.

    The bound is elementary and intentionally conservative:

    ``q = (2 A_e / gap)^2``
    ``Q = max(q, 1)``
    ``N_e = ceil(4 Q log(4 Q sqrt(B_e)))``.
    """
    _positive_finite(gap, "gap")
    _nonnegative_finite(amplitude, "amplitude")
    _log_factor(log_factor)
    if amplitude == 0.0:
        return 1

    q = (2.0 * amplitude / gap) ** 2
    inflated_q = max(q, 1.0)
    logarithm = log(4.0 * inflated_q * sqrt(log_factor))
    return max(1, ceil(4.0 * inflated_q * logarithm))


def edge_uncertainty_parameters(
    edge: Edge,
    target_amplitudes: Mapping[Vertex, float],
    quantum_amplitudes: Mapping[Vertex, float],
    target_log_factors: Mapping[Vertex, float],
    quantum_log_factors: Mapping[Vertex, float],
    lipschitz_constant: float,
) -> tuple[float, float]:
    """Collapse four preparation-level envelopes into one edge envelope.

    When both endpoint target radii and both endpoint quantum radii have the
    P48 form, a common upper envelope is obtained with

    ``A_e = A_Y,i + A_Y,j + L_e (A_Q,i + A_Q,j)``

    and ``B_e`` equal to the largest endpoint log factor.
    """
    _validate_edge(edge)
    _nonnegative_finite(lipschitz_constant, "lipschitz_constant")
    first, second = edge
    for mapping, name in (
        (target_amplitudes, "target_amplitudes"),
        (quantum_amplitudes, "quantum_amplitudes"),
        (target_log_factors, "target_log_factors"),
        (quantum_log_factors, "quantum_log_factors"),
    ):
        if first not in mapping or second not in mapping:
            raise ValueError(f"{name} must cover both edge endpoints")

    for value in (
        target_amplitudes[first],
        target_amplitudes[second],
        quantum_amplitudes[first],
        quantum_amplitudes[second],
    ):
        _nonnegative_finite(value, "amplitude")
    for value in (
        target_log_factors[first],
        target_log_factors[second],
        quantum_log_factors[first],
        quantum_log_factors[second],
    ):
        _log_factor(value)

    amplitude = (
        target_amplitudes[first]
        + target_amplitudes[second]
        + lipschitz_constant
        * (quantum_amplitudes[first] + quantum_amplitudes[second])
    )
    log_factor = max(
        target_log_factors[first],
        target_log_factors[second],
        quantum_log_factors[first],
        quantum_log_factors[second],
    )
    return amplitude, log_factor


def edge_complexity_bounds(
    edges: Sequence[Edge],
    margins: Mapping[Edge, float],
    target_amplitudes: Mapping[Vertex, float],
    quantum_amplitudes: Mapping[Vertex, float],
    target_log_factors: Mapping[Vertex, float],
    quantum_log_factors: Mapping[Vertex, float],
    lipschitz_constants: Mapping[Edge, float],
) -> dict[Edge, EdgeStoppingComplexity]:
    """Build P48 gap-dependent sufficient bounds for a finite edge family."""
    declared_edges = tuple(edges)
    _validate_edges(declared_edges)
    edge_set = set(declared_edges)
    _exact_edge_keys(margins, edge_set, "margins")
    _exact_edge_keys(lipschitz_constants, edge_set, "lipschitz_constants")

    result: dict[Edge, EdgeStoppingComplexity] = {}
    for edge in declared_edges:
        margin = margins[edge]
        if not isfinite(margin):
            raise ValueError("margins must be finite")
        amplitude, log_factor = edge_uncertainty_parameters(
            edge,
            target_amplitudes,
            quantum_amplitudes,
            target_log_factors,
            quantum_log_factors,
            lipschitz_constants[edge],
        )
        gap = abs(margin)
        local_samples = None
        if gap > 0.0:
            local_samples = required_local_samples(
                gap,
                amplitude,
                log_factor,
            )
        result[edge] = EdgeStoppingComplexity(
            edge=edge,
            margin=margin,
            gap=gap,
            amplitude=amplitude,
            log_factor=log_factor,
            local_samples=local_samples,
        )
    return result


def sequential_stopping_epoch_bound(
    bounds: Mapping[Edge, EdgeStoppingComplexity],
) -> SequentialStoppingBound:
    """Return the P48 round-robin epoch bound for the declared family.

    If at least one population margin is positive, the procedure may stop at
    the first certified positive edge, so the sufficient epoch bound is the
    smallest ``N_e`` among positive edges.

    If every margin is strictly negative, certifying that no positive edge
    remains requires all edges to be eliminated, so the sufficient bound is
    the largest ``N_e``.

    If there is no positive margin and at least one margin is exactly zero,
    P48 gives no finite sign-separation bound.
    """
    if not bounds:
        raise ValueError("bounds must be nonempty")
    for edge, bound in bounds.items():
        _validate_edge(edge)
        if edge != bound.edge:
            raise ValueError("bound edge must match its mapping key")

    positive = [bound for bound in bounds.values() if bound.margin > 0.0]
    if positive:
        epochs = min(_finite_samples(bound) for bound in positive)
        controlling = tuple(
            bound.edge
            for bound in positive
            if _finite_samples(bound) == epochs
        )
        return SequentialStoppingBound(
            status="positive-witness",
            epochs=epochs,
            controlling_edges=controlling,
        )

    if any(bound.margin == 0.0 for bound in bounds.values()):
        zeros = tuple(
            bound.edge for bound in bounds.values() if bound.margin == 0.0
        )
        return SequentialStoppingBound(
            status="no-finite-sign-gap-bound",
            epochs=None,
            controlling_edges=zeros,
        )

    epochs = max(_finite_samples(bound) for bound in bounds.values())
    controlling = tuple(
        bound.edge
        for bound in bounds.values()
        if _finite_samples(bound) == epochs
    )
    return SequentialStoppingBound(
        status="certified-no-positive-edge",
        epochs=epochs,
        controlling_edges=controlling,
    )


def full_family_cost_upper_bound(
    vertices: Sequence[Vertex],
    epochs: int,
    *,
    vertex_epoch_costs: Mapping[Vertex, float] | None = None,
) -> float:
    """Return the full-family round-robin cost upper bound through ``epochs``.

    The default cost is two measurement draws per active preparation per epoch:
    one target draw and one quantum/tomography draw.  A user can instead supply
    arbitrary positive preparation-level epoch costs.
    """
    if epochs < 0:
        raise ValueError("epochs must be nonnegative")
    declared = tuple(vertices)
    if not declared:
        raise ValueError("vertices must be nonempty")
    if len(set(declared)) != len(declared):
        raise ValueError("vertices must be unique")

    if vertex_epoch_costs is None:
        one_epoch = 2.0 * len(declared)
    else:
        if set(vertex_epoch_costs) != set(declared):
            raise ValueError(
                "vertex_epoch_costs must cover every and only declared vertex"
            )
        one_epoch = 0.0
        for cost in vertex_epoch_costs.values():
            _positive_finite(cost, "vertex epoch cost")
            one_epoch += cost
    return epochs * one_epoch


def adaptive_active_cost(
    active_vertices_by_epoch: Sequence[Sequence[Vertex]],
    *,
    vertex_epoch_costs: Mapping[Vertex, float] | None = None,
) -> float:
    """Compute realized cost after P47 safe pruning.

    With no explicit costs, every active preparation contributes two draws per
    epoch.  This function is bookkeeping only; P48's theorem gives the upper
    bound by comparing this realized cost with full-family round robin.
    """
    if vertex_epoch_costs is not None:
        for cost in vertex_epoch_costs.values():
            _positive_finite(cost, "vertex epoch cost")

    total = 0.0
    for active in active_vertices_by_epoch:
        epoch_vertices = tuple(active)
        if len(set(epoch_vertices)) != len(epoch_vertices):
            raise ValueError("active vertices must be unique within each epoch")
        if vertex_epoch_costs is None:
            total += 2.0 * len(epoch_vertices)
        else:
            for vertex in epoch_vertices:
                if vertex not in vertex_epoch_costs:
                    raise ValueError("missing vertex epoch cost")
                total += vertex_epoch_costs[vertex]
    return total


def _finite_samples(bound: EdgeStoppingComplexity) -> int:
    if bound.local_samples is None:
        raise ValueError("zero-gap edge has no finite local-sample bound")
    return bound.local_samples


def _validate_edges(edges: tuple[Edge, ...]) -> None:
    seen: set[frozenset[Vertex]] = set()
    if not edges:
        raise ValueError("edges must be nonempty")
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


def _exact_edge_keys(
    mapping: Mapping[Edge, object],
    expected: set[Edge],
    name: str,
) -> None:
    if set(mapping) != expected:
        raise ValueError(f"{name} must cover every and only declared edge")


def _positive_finite(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")


def _nonnegative_finite(value: float, name: str) -> None:
    if not isfinite(value) or value < 0.0:
        raise ValueError(f"{name} must be nonnegative and finite")


def _log_factor(value: float) -> None:
    if not isfinite(value) or value < 1.0:
        raise ValueError("log_factor must be finite and at least one")
