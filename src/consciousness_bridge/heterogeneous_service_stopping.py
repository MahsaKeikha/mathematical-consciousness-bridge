"""Proposition 51: heterogeneous finite-window service-rate stopping.

P51 sharpens the common H-fairness factor from P50. Each preparation i may
have its own finite-window service guarantee (W_i, q_i): whenever i remains
active throughout W_i consecutive global rounds, it is sampled at least q_i
times in that window.

For an always-active preparation this implies

    N_i(T) >= q_i * floor(T / W_i).

Hence N required local samples are guaranteed by

    T_i(N) = W_i * ceil(N / q_i).

An edge inherits the slower endpoint time, and the P48 positive/all-negative
stopping theorems lift to instance-dependent global-round bounds.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from math import ceil
from typing import TypeVar

from .gap_stopping_complexity import EdgeStoppingComplexity

Vertex = TypeVar("Vertex", bound=Hashable)
Edge = tuple[Vertex, Vertex]


@dataclass(frozen=True)
class ServiceGuarantee:
    """Finite-window service requirement for one preparation."""

    window: int
    quota: int

    def __post_init__(self) -> None:
        if self.window < 1:
            raise ValueError("window must be a positive integer")
        if self.quota < 1:
            raise ValueError("quota must be a positive integer")
        if self.quota > self.window:
            raise ValueError("quota cannot exceed window under one-sample-per-round scheduling")

    @property
    def service_rate(self) -> float:
        return self.quota / self.window


@dataclass(frozen=True)
class ServiceViolation:
    """One realized violation of a preparation-specific service guarantee."""

    vertex: Vertex
    start_round: int
    end_round: int
    required: int
    observed: int


@dataclass(frozen=True)
class EdgeServiceStoppingBound:
    """Global-round threshold for one edge under endpoint service guarantees."""

    edge: Edge
    local_samples: int | None
    endpoint_rounds: tuple[int | None, int | None]
    global_rounds: int | None
    bottleneck_vertices: tuple[Vertex, ...]


@dataclass(frozen=True)
class HeterogeneousStoppingBound:
    """Family-level positive or all-negative P51 stopping bound."""

    status: str
    global_round_bound: int | None
    controlling_edges: tuple[Edge, ...]


def guaranteed_samples(
    rounds: int,
    guarantee: ServiceGuarantee,
) -> int:
    """Lower-bound samples for a preparation active throughout ``rounds``."""
    if rounds < 0:
        raise ValueError("rounds must be nonnegative")
    return guarantee.quota * (rounds // guarantee.window)


def rounds_for_samples(
    local_samples: int,
    guarantee: ServiceGuarantee,
) -> int:
    """Sufficient global rounds for an always-active preparation."""
    if local_samples < 1:
        raise ValueError("local_samples must be a positive integer")
    blocks = ceil(local_samples / guarantee.quota)
    return guarantee.window * blocks


def service_violations(
    active_vertices_by_round: Sequence[Sequence[Vertex]],
    selections: Sequence[Vertex],
    guarantees: Mapping[Vertex, ServiceGuarantee],
) -> tuple[ServiceViolation, ...]:
    """Return all realized heterogeneous finite-window service violations."""
    if len(active_vertices_by_round) != len(selections):
        raise ValueError("active sets and selections must have the same length")
    if not guarantees:
        raise ValueError("guarantees must be nonempty")

    active_sets = [set(active) for active in active_vertices_by_round]
    for round_index, (active, selected) in enumerate(zip(active_sets, selections)):
        if selected not in active:
            raise ValueError(
                f"selected vertex is not active in round {round_index + 1}"
            )

    violations: list[ServiceViolation] = []
    rounds = len(selections)
    for vertex, guarantee in guarantees.items():
        window = guarantee.window
        if rounds < window:
            continue
        for start in range(rounds - window + 1):
            end = start + window
            if not all(vertex in active for active in active_sets[start:end]):
                continue
            observed = sum(selected == vertex for selected in selections[start:end])
            if observed < guarantee.quota:
                violations.append(
                    ServiceViolation(
                        vertex=vertex,
                        start_round=start + 1,
                        end_round=end,
                        required=guarantee.quota,
                        observed=observed,
                    )
                )
    return tuple(violations)


def is_service_compliant_schedule(
    active_vertices_by_round: Sequence[Sequence[Vertex]],
    selections: Sequence[Vertex],
    guarantees: Mapping[Vertex, ServiceGuarantee],
) -> bool:
    """Return whether a realized schedule obeys all declared service guarantees."""
    return not service_violations(active_vertices_by_round, selections, guarantees)


def edge_service_stopping_bound(
    bound: EdgeStoppingComplexity,
    guarantees: Mapping[Vertex, ServiceGuarantee],
) -> EdgeServiceStoppingBound:
    """Lift one P48 local threshold through endpoint-specific service guarantees."""
    i, j = bound.edge
    if i not in guarantees or j not in guarantees:
        raise ValueError("both edge endpoints require declared service guarantees")

    if bound.local_samples is None:
        return EdgeServiceStoppingBound(
            edge=bound.edge,
            local_samples=None,
            endpoint_rounds=(None, None),
            global_rounds=None,
            bottleneck_vertices=(),
        )

    threshold = int(bound.local_samples)
    if threshold < 1:
        raise ValueError("finite P48 local_samples must be positive")

    t_i = rounds_for_samples(threshold, guarantees[i])
    t_j = rounds_for_samples(threshold, guarantees[j])
    global_rounds = max(t_i, t_j)
    bottlenecks = tuple(
        vertex
        for vertex, endpoint_rounds in ((i, t_i), (j, t_j))
        if endpoint_rounds == global_rounds
    )
    return EdgeServiceStoppingBound(
        edge=bound.edge,
        local_samples=threshold,
        endpoint_rounds=(t_i, t_j),
        global_rounds=global_rounds,
        bottleneck_vertices=bottlenecks,
    )


def heterogeneous_stopping_bound(
    bounds: Mapping[Edge, EdgeStoppingComplexity],
    guarantees: Mapping[Vertex, ServiceGuarantee],
) -> HeterogeneousStoppingBound:
    """Return P51 positive-witness or all-negative global stopping bounds."""
    if not bounds:
        raise ValueError("bounds must be nonempty")
    if not guarantees:
        raise ValueError("guarantees must be nonempty")
    for edge, bound in bounds.items():
        if edge != bound.edge:
            raise ValueError("bound edge must match its mapping key")

    positive = [bound for bound in bounds.values() if bound.margin > 0.0]
    if positive:
        edge_bounds = [edge_service_stopping_bound(bound, guarantees) for bound in positive]
        if any(item.global_rounds is None for item in edge_bounds):
            raise ValueError("positive-margin edges require finite P48 thresholds")
        best = min(int(item.global_rounds) for item in edge_bounds)
        controllers = tuple(
            item.edge for item in edge_bounds if item.global_rounds == best
        )
        return HeterogeneousStoppingBound(
            status="positive-witness",
            global_round_bound=best,
            controlling_edges=controllers,
        )

    zeros = tuple(bound.edge for bound in bounds.values() if bound.margin == 0.0)
    if zeros:
        return HeterogeneousStoppingBound(
            status="no-finite-sign-gap-bound",
            global_round_bound=None,
            controlling_edges=zeros,
        )

    edge_bounds = [edge_service_stopping_bound(bound, guarantees) for bound in bounds.values()]
    if any(item.global_rounds is None for item in edge_bounds):
        raise ValueError("strictly negative edges require finite P48 thresholds")
    worst = max(int(item.global_rounds) for item in edge_bounds)
    controllers = tuple(
        item.edge for item in edge_bounds if item.global_rounds == worst
    )
    return HeterogeneousStoppingBound(
        status="certified-no-positive-edge",
        global_round_bound=worst,
        controlling_edges=controllers,
    )


def p50_special_case_bound(
    local_samples: int,
    fairness_horizon: int,
) -> int:
    """Recover the P50 H*N bound as the quota-one special case."""
    return rounds_for_samples(
        local_samples,
        ServiceGuarantee(window=fairness_horizon, quota=1),
    )
