"""Proposition 50: bounded-starvation asynchronous sampling.

P50 converts the local-count stopping guarantees of P48 into global-round
stopping guarantees for adaptive priority-based sampling policies.

A policy is H-fair if every preparation that remains active throughout any
block of H consecutive global rounds is sampled at least once in that block.
Under P47 safe pruning, a truly positive edge cannot be eliminated on the
simultaneous good event. Therefore its endpoints remain active, and H-fairness
forces their local counts to increase at least once every H rounds.

This module implements deterministic schedule checks and global-time bounds.
It does not claim that bounded-starvation policies are optimal.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from typing import TypeVar

from .gap_stopping_complexity import EdgeStoppingComplexity

Vertex = TypeVar("Vertex", bound=Hashable)
Edge = tuple[Vertex, Vertex]


@dataclass(frozen=True)
class FairnessViolation:
    """One bounded-starvation violation in a realized schedule."""

    vertex: Vertex
    start_round: int
    end_round: int


@dataclass(frozen=True)
class AsynchronousStoppingBound:
    """P50 global-round stopping bound from local P48 thresholds."""

    status: str
    local_epoch_bound: int | None
    fairness_horizon: int
    global_round_bound: int | None
    controlling_edges: tuple[Edge, ...]


def local_sample_counts(
    selections: Sequence[Vertex],
) -> dict[Vertex, int]:
    """Count preparation selections in a finite realized global schedule."""
    counts: dict[Vertex, int] = {}
    for vertex in selections:
        counts[vertex] = counts.get(vertex, 0) + 1
    return counts


def prefix_local_sample_counts(
    selections: Sequence[Vertex],
    vertices: Sequence[Vertex],
) -> tuple[dict[Vertex, int], ...]:
    """Return cumulative local counts after each global round."""
    declared = tuple(vertices)
    if len(set(declared)) != len(declared):
        raise ValueError("vertices must be unique")
    counts = {vertex: 0 for vertex in declared}
    history: list[dict[Vertex, int]] = []
    allowed = set(declared)
    for selected in selections:
        if selected not in allowed:
            raise ValueError("selection contains a vertex outside the declared set")
        counts[selected] += 1
        history.append(dict(counts))
    return tuple(history)


def fairness_violations(
    active_vertices_by_round: Sequence[Sequence[Vertex]],
    selections: Sequence[Vertex],
    fairness_horizon: int,
) -> tuple[FairnessViolation, ...]:
    """Return all H-fairness violations in a realized finite schedule.

    A vertex violates H-fairness on a block when it is active in every round of
    that block but is never selected in that block.
    """
    _positive_horizon(fairness_horizon)
    if len(active_vertices_by_round) != len(selections):
        raise ValueError("active sets and selections must have the same length")

    rounds = len(selections)
    active_sets = [set(active) for active in active_vertices_by_round]
    for round_index, (active, selected) in enumerate(zip(active_sets, selections)):
        if selected not in active:
            raise ValueError(
                f"selected vertex is not active in round {round_index + 1}"
            )

    violations: list[FairnessViolation] = []
    for start in range(0, rounds - fairness_horizon + 1):
        end = start + fairness_horizon
        common_active = set.intersection(*active_sets[start:end])
        selected_in_block = set(selections[start:end])
        for vertex in sorted(common_active, key=repr):
            if vertex not in selected_in_block:
                violations.append(
                    FairnessViolation(
                        vertex=vertex,
                        start_round=start + 1,
                        end_round=end,
                    )
                )
    return tuple(violations)


def is_h_fair_schedule(
    active_vertices_by_round: Sequence[Sequence[Vertex]],
    selections: Sequence[Vertex],
    fairness_horizon: int,
) -> bool:
    """Return whether a realized finite schedule satisfies H-fairness."""
    return not fairness_violations(
        active_vertices_by_round,
        selections,
        fairness_horizon,
    )


def minimum_samples_under_fairness(
    rounds: int,
    fairness_horizon: int,
) -> int:
    """Lower-bound local samples for a vertex active throughout ``rounds``.

    H-fairness guarantees at least floor(rounds / H) selections by partitioning
    the first H * floor(rounds/H) rounds into disjoint H-round blocks.
    """
    if rounds < 0:
        raise ValueError("rounds must be nonnegative")
    _positive_horizon(fairness_horizon)
    return rounds // fairness_horizon


def rounds_for_local_samples(
    local_samples: int,
    fairness_horizon: int,
) -> int:
    """Sufficient global rounds for an always-active vertex to get local samples."""
    if local_samples < 1:
        raise ValueError("local_samples must be a positive integer")
    _positive_horizon(fairness_horizon)
    return fairness_horizon * local_samples


def asynchronous_stopping_bound(
    bounds: Mapping[Edge, EdgeStoppingComplexity],
    fairness_horizon: int,
) -> AsynchronousStoppingBound:
    """Lift P48 local stopping thresholds to P50 global-round bounds.

    Positive case:
      ``H * min_{M_e>0} N_e``.

    All-negative case:
      ``H * max_e N_e`` when all margins are strictly negative.

    If there is no positive edge and at least one zero-margin edge, no finite
    sign-gap bound exists, exactly as in P48.
    """
    _positive_horizon(fairness_horizon)
    if not bounds:
        raise ValueError("bounds must be nonempty")
    for edge, bound in bounds.items():
        if edge != bound.edge:
            raise ValueError("bound edge must match its mapping key")

    positive = [bound for bound in bounds.values() if bound.margin > 0.0]
    if positive:
        if any(bound.local_samples is None for bound in positive):
            raise ValueError("positive-margin bounds must have finite local thresholds")
        local = min(int(bound.local_samples) for bound in positive)
        controlling = tuple(
            bound.edge
            for bound in positive
            if bound.local_samples == local
        )
        return AsynchronousStoppingBound(
            status="positive-witness",
            local_epoch_bound=local,
            fairness_horizon=fairness_horizon,
            global_round_bound=fairness_horizon * local,
            controlling_edges=controlling,
        )

    zeros = tuple(bound.edge for bound in bounds.values() if bound.margin == 0.0)
    if zeros:
        return AsynchronousStoppingBound(
            status="no-finite-sign-gap-bound",
            local_epoch_bound=None,
            fairness_horizon=fairness_horizon,
            global_round_bound=None,
            controlling_edges=zeros,
        )

    negative = list(bounds.values())
    if any(bound.local_samples is None for bound in negative):
        raise ValueError("strictly negative bounds must have finite local thresholds")
    local = max(int(bound.local_samples) for bound in negative)
    controlling = tuple(
        bound.edge
        for bound in negative
        if bound.local_samples == local
    )
    return AsynchronousStoppingBound(
        status="certified-no-positive-edge",
        local_epoch_bound=local,
        fairness_horizon=fairness_horizon,
        global_round_bound=fairness_horizon * local,
        controlling_edges=controlling,
    )


def starvation_counterexample_length(
    desired_delay: int,
) -> tuple[str, ...]:
    """Construct a schedule fragment showing why no-fairness gives no time bound.

    The returned schedule samples only ``"other"`` for ``desired_delay`` rounds.
    A required endpoint named ``"needed"`` receives zero samples throughout.
    Since ``desired_delay`` is arbitrary, no finite global-time guarantee can be
    deduced from P48 local thresholds without a progress assumption.
    """
    if desired_delay < 0:
        raise ValueError("desired_delay must be nonnegative")
    return tuple("other" for _ in range(desired_delay))


def _positive_horizon(fairness_horizon: int) -> None:
    if fairness_horizon < 1:
        raise ValueError("fairness_horizon must be a positive integer")
