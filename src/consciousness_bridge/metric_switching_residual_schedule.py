"""Proposition 54: metric switching-cost residual scheduling.

P53 gives a residual sample-demand vector. P54 adds setup/transition cost between
preparations. Under a declared metric switching cost, there is always an optimal
schedule that visits each positive-demand preparation in one contiguous block.
The acquisition term is fixed by the residual demand; the remaining optimization
is a shortest Hamiltonian path through the required preparations from the
current setup state.

This module supplies metric validation, schedule-cost evaluation, and an exact
Held-Karp dynamic program for small instances. It is a deterministic scheduling
result, not a statement about statistical or experiential ontology.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from math import inf, isfinite
from typing import TypeVar

Vertex = TypeVar("Vertex", bound=Hashable)
Point = TypeVar("Point", bound=Hashable)


@dataclass(frozen=True)
class SwitchingSchedule:
    """Exact block schedule and deterministic cost decomposition."""

    order: tuple[Hashable, ...]
    acquisition_cost: float
    switching_cost: float
    total_cost: float


@dataclass(frozen=True)
class BatchingCertificate:
    """Cost comparison between an arbitrary schedule and its first-visit batching."""

    original_switching_cost: float
    batched_switching_cost: float
    batched_order: tuple[Hashable, ...]
    switching_nonincreasing: bool


def validate_metric_costs(
    points: Sequence[Point],
    costs: Mapping[tuple[Point, Point], float],
    *,
    tolerance: float = 1e-12,
) -> None:
    """Validate a finite symmetric metric supplied as a complete directed map."""
    declared = tuple(points)
    if not declared:
        raise ValueError("points must be nonempty")
    if len(set(declared)) != len(declared):
        raise ValueError("points must be unique")
    if tolerance < 0.0 or not isfinite(tolerance):
        raise ValueError("tolerance must be nonnegative and finite")

    expected = {(u, v) for u in declared for v in declared}
    if set(costs) != expected:
        raise ValueError("costs must contain every ordered pair of declared points")

    for u in declared:
        for v in declared:
            value = costs[(u, v)]
            if not isfinite(value) or value < 0.0:
                raise ValueError("switching costs must be nonnegative and finite")
            if u == v and abs(value) > tolerance:
                raise ValueError("metric diagonal must be zero")
            if abs(value - costs[(v, u)]) > tolerance:
                raise ValueError("metric costs must be symmetric")

    for u in declared:
        for v in declared:
            for w in declared:
                if costs[(u, w)] > costs[(u, v)] + costs[(v, w)] + tolerance:
                    raise ValueError("switching costs violate triangle inequality")


def switching_path_cost(
    order: Sequence[Point],
    costs: Mapping[tuple[Point, Point], float],
    *,
    start: Point | None = None,
) -> float:
    """Return transition cost of one block order from an optional current setup."""
    route = tuple(order)
    if not route:
        return 0.0
    total = 0.0
    if start is not None:
        total += costs[(start, route[0])]
    for first, second in zip(route, route[1:]):
        total += costs[(first, second)]
    return total


def expanded_schedule_cost(
    schedule: Sequence[Point],
    costs: Mapping[tuple[Point, Point], float],
    *,
    start: Point | None = None,
) -> float:
    """Return switching cost for an arbitrary possibly revisiting schedule."""
    sequence = tuple(schedule)
    if not sequence:
        return 0.0
    total = 0.0
    if start is not None:
        total += costs[(start, sequence[0])]
    for first, second in zip(sequence, sequence[1:]):
        total += costs[(first, second)]
    return total


def first_visit_order(schedule: Sequence[Point]) -> tuple[Point, ...]:
    """Return each preparation once, in order of first appearance."""
    seen: set[Point] = set()
    order: list[Point] = []
    for vertex in schedule:
        if vertex not in seen:
            seen.add(vertex)
            order.append(vertex)
    return tuple(order)


def batching_certificate(
    schedule: Sequence[Point],
    costs: Mapping[tuple[Point, Point], float],
    *,
    start: Point | None = None,
    tolerance: float = 1e-12,
) -> BatchingCertificate:
    """Compare a revisiting route with the metric first-visit block route.

    For a metric cost, deleting repeated visits from a route cannot increase its
    path length: each shortcut is bounded by the skipped segment through repeated
    triangle inequalities. Thus the first-visit block order costs no more.
    """
    order = first_visit_order(schedule)
    original = expanded_schedule_cost(schedule, costs, start=start)
    batched = switching_path_cost(order, costs, start=start)
    return BatchingCertificate(
        original_switching_cost=original,
        batched_switching_cost=batched,
        batched_order=tuple(order),
        switching_nonincreasing=batched <= original + tolerance,
    )


def shortest_block_schedule(
    residual_demands: Mapping[Vertex, int],
    costs: Mapping[tuple[Hashable, Hashable], float],
    *,
    start: Hashable | None = None,
    sample_cost: float = 1.0,
) -> SwitchingSchedule:
    """Solve the exact P54 block-order problem with Held-Karp dynamic programming.

    Positive-demand preparations are visited exactly once as blocks. The dynamic
    program finds the minimum switching path beginning at ``start`` when supplied,
    with no return-to-start requirement.
    """
    if not residual_demands:
        raise ValueError("residual_demands must be nonempty")
    if not isfinite(sample_cost) or sample_cost <= 0.0:
        raise ValueError("sample_cost must be positive and finite")

    required: list[Vertex] = []
    acquisition_units = 0
    for vertex, demand in residual_demands.items():
        if not isinstance(demand, int) or isinstance(demand, bool) or demand < 0:
            raise ValueError("residual demands must be nonnegative integers")
        if demand > 0:
            required.append(vertex)
            acquisition_units += demand

    acquisition = sample_cost * acquisition_units
    if not required:
        return SwitchingSchedule((), 0.0, 0.0, 0.0)

    points: list[Hashable] = list(required)
    if start is not None and start not in points:
        points.append(start)
    validate_metric_costs(points, costs)

    m = len(required)
    if m == 1:
        switch = 0.0 if start is None else costs[(start, required[0])]
        return SwitchingSchedule(
            order=(required[0],),
            acquisition_cost=acquisition,
            switching_cost=switch,
            total_cost=acquisition + switch,
        )

    # dp[(mask, j)] = (best switching cost, predecessor index)
    dp: dict[tuple[int, int], tuple[float, int | None]] = {}
    for j, vertex in enumerate(required):
        initial = 0.0 if start is None else costs[(start, vertex)]
        dp[(1 << j, j)] = (initial, None)

    full_mask = (1 << m) - 1
    for mask in range(1, full_mask + 1):
        for j in range(m):
            if not (mask & (1 << j)) or (mask, j) not in dp:
                continue
            current_cost, _ = dp[(mask, j)]
            for k in range(m):
                if mask & (1 << k):
                    continue
                new_mask = mask | (1 << k)
                candidate = current_cost + costs[(required[j], required[k])]
                key = (new_mask, k)
                if candidate < dp.get(key, (inf, None))[0]:
                    dp[key] = (candidate, j)

    end = min(range(m), key=lambda j: dp[(full_mask, j)][0])
    best_switch = dp[(full_mask, end)][0]

    order_indices: list[int] = []
    mask = full_mask
    current: int | None = end
    while current is not None:
        order_indices.append(current)
        _, predecessor = dp[(mask, current)]
        mask ^= 1 << current
        current = predecessor
    order_indices.reverse()
    order = tuple(required[index] for index in order_indices)

    return SwitchingSchedule(
        order=order,
        acquisition_cost=acquisition,
        switching_cost=best_switch,
        total_cost=acquisition + best_switch,
    )


def block_expanded_schedule(
    order: Sequence[Vertex],
    residual_demands: Mapping[Vertex, int],
) -> tuple[Vertex, ...]:
    """Expand a block order into individual preparation-level sample selections."""
    if set(order) != {vertex for vertex, demand in residual_demands.items() if demand > 0}:
        raise ValueError("order must contain every and only positive-demand vertex")
    if len(set(order)) != len(tuple(order)):
        raise ValueError("block order must not repeat vertices")
    result: list[Vertex] = []
    for vertex in order:
        demand = residual_demands[vertex]
        if not isinstance(demand, int) or isinstance(demand, bool) or demand <= 0:
            raise ValueError("ordered vertices must have positive integer demand")
        result.extend([vertex] * demand)
    return tuple(result)
