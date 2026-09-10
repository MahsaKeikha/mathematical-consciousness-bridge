"""Proposition 58: finite-data switching-metric uncertainty.

P57 treats two switching metrics as known deterministic objects. P58 allows the
true switching metric to be unknown while pairwise transition measurements
supply simultaneous confidence intervals for its entries.

The empirical center need not itself satisfy the triangle inequality. The true
metric assumption is used by P54 to justify the one-block scheduling reduction;
a rectangular confidence envelope then bounds every candidate block route.
Exact dynamic programming over lower and upper edge envelopes produces a
finite-data interval for the unknown true optimal switching cost and a robust
route-regret certificate.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from math import inf, isfinite, log, sqrt
from typing import TypeVar

Vertex = TypeVar("Vertex", bound=Hashable)
Point = TypeVar("Point", bound=Hashable)
Edge = tuple[Point, Point]


@dataclass(frozen=True)
class RouteEnvelope:
    """Lower and upper switching cost for one candidate route."""

    lower: float
    upper: float


@dataclass(frozen=True)
class RobustSwitchingCertificate:
    """Finite-data envelope for the unknown true P54 optimum."""

    support: tuple[Hashable, ...]
    lower_order: tuple[Hashable, ...]
    robust_order: tuple[Hashable, ...]
    acquisition_cost: float
    lower_switching_cost: float
    upper_switching_cost: float
    lower_total_cost: float
    upper_total_cost: float
    robust_route_regret_upper_bound: float


@dataclass(frozen=True)
class RobustImprovementCertificate:
    """Compare two simultaneous robust total-cost intervals."""

    old_lower_total_cost: float
    new_upper_total_cost: float
    guaranteed_release: float
    strict_improvement_certified: bool


def canonical_pairs(points: Sequence[Point]) -> tuple[Edge, ...]:
    """Return each unordered off-diagonal pair once, in declared point order."""
    declared = tuple(points)
    _validate_points(declared)
    return tuple(
        (declared[first], declared[second])
        for first in range(len(declared))
        for second in range(first + 1, len(declared))
    )


def hoeffding_pair_radius(
    sample_count: int,
    range_width: float,
    alpha: float,
) -> float:
    """Return a two-sided Hoeffding radius for a bounded pairwise mean."""
    if not isinstance(sample_count, int) or isinstance(sample_count, bool):
        raise ValueError("sample_count must be a positive integer")
    if sample_count <= 0:
        raise ValueError("sample_count must be a positive integer")
    _positive_finite(range_width, "range_width")
    _probability_level(alpha, "alpha")
    return range_width * sqrt(log(2.0 / alpha) / (2.0 * sample_count))


def allocate_pair_error(
    points: Sequence[Point],
    total_alpha: float,
    *,
    weights: Mapping[Edge, float] | None = None,
) -> dict[Edge, float]:
    """Allocate a finite failure budget across unordered transition pairs."""
    pairs = canonical_pairs(points)
    _probability_level(total_alpha, "total_alpha")
    if not pairs:
        return {}

    if weights is None:
        share = total_alpha / len(pairs)
        return {pair: share for pair in pairs}

    if set(weights) != set(pairs):
        raise ValueError("weights must cover every and only canonical pair")
    total_weight = 0.0
    for value in weights.values():
        _positive_finite(value, "weight")
        total_weight += value
    return {
        pair: total_alpha * weights[pair] / total_weight
        for pair in pairs
    }


def pairwise_hoeffding_radii(
    points: Sequence[Point],
    sample_counts: Mapping[Edge, int],
    range_widths: Mapping[Edge, float],
    total_alpha: float,
    *,
    weights: Mapping[Edge, float] | None = None,
) -> dict[tuple[Point, Point], float]:
    """Return symmetric entrywise radii from bounded pairwise observations.

    Each canonical pair receives a two-sided Hoeffding interval. A union bound
    over the finite pair family gives simultaneous coverage at least
    ``1-total_alpha`` whenever the declared marginal concentration assumptions
    hold. Pairwise independence is not required for that union-bound step.
    """
    declared = tuple(points)
    pairs = canonical_pairs(declared)
    if set(sample_counts) != set(pairs):
        raise ValueError("sample_counts must cover every canonical pair")
    if set(range_widths) != set(pairs):
        raise ValueError("range_widths must cover every canonical pair")

    allocation = allocate_pair_error(
        declared,
        total_alpha,
        weights=weights,
    )
    radii: dict[tuple[Point, Point], float] = {}
    for point in declared:
        radii[(point, point)] = 0.0
    for pair in pairs:
        radius = hoeffding_pair_radius(
            sample_counts[pair],
            range_widths[pair],
            allocation[pair],
        )
        first, second = pair
        radii[(first, second)] = radius
        radii[(second, first)] = radius
    return radii


def validate_symmetric_envelope(
    points: Sequence[Point],
    estimates: Mapping[tuple[Point, Point], float],
    radii: Mapping[tuple[Point, Point], float],
    *,
    tolerance: float = 1e-12,
) -> None:
    """Validate finite symmetric estimates and nonnegative symmetric radii."""
    declared = tuple(points)
    _validate_points(declared)
    _nonnegative_finite(tolerance, "tolerance")
    expected = {(first, second) for first in declared for second in declared}
    if not expected.issubset(estimates):
        raise ValueError("estimates must contain every ordered declared pair")
    if not expected.issubset(radii):
        raise ValueError("radii must contain every ordered declared pair")

    for first in declared:
        for second in declared:
            estimate = estimates[(first, second)]
            radius = radii[(first, second)]
            if not isfinite(estimate) or estimate < 0.0:
                raise ValueError("estimates must be nonnegative and finite")
            _nonnegative_finite(radius, "radius")
            if abs(estimate - estimates[(second, first)]) > tolerance:
                raise ValueError("estimates must be symmetric")
            if abs(radius - radii[(second, first)]) > tolerance:
                raise ValueError("radii must be symmetric")
            if first == second:
                if abs(estimate) > tolerance or abs(radius) > tolerance:
                    raise ValueError("diagonal estimates and radii must be zero")


def route_envelope(
    order: Sequence[Point],
    estimates: Mapping[tuple[Point, Point], float],
    radii: Mapping[tuple[Point, Point], float],
    *,
    start: Point | None = None,
) -> RouteEnvelope:
    """Bound one route under entrywise simultaneous transition intervals."""
    route = tuple(order)
    if not route:
        return RouteEnvelope(0.0, 0.0)

    transitions: list[tuple[Point, Point]] = []
    if start is not None:
        transitions.append((start, route[0]))
    transitions.extend(zip(route[:-1], route[1:], strict=True))

    lower = 0.0
    upper = 0.0
    for first, second in transitions:
        estimate = estimates[(first, second)]
        radius = radii[(first, second)]
        lower += max(0.0, estimate - radius)
        upper += estimate + radius
    return RouteEnvelope(lower=lower, upper=upper)


def robust_optimal_switching_certificate(
    residual_demands: Mapping[Vertex, int],
    estimates: Mapping[tuple[Hashable, Hashable], float],
    radii: Mapping[tuple[Hashable, Hashable], float],
    *,
    start: Hashable | None = None,
    sample_cost: float = 1.0,
) -> RobustSwitchingCertificate:
    """Bound the unknown true P54 optimum without requiring a metric center.

    On the simultaneous event ``|c_hat-c| <= radius`` for every relevant pair,
    every route has a deterministic lower and upper cost. Minimizing the lower
    route envelope yields a lower bound on the true optimum. Minimizing the
    upper route envelope yields a feasible robust-route upper bound.
    """
    if not residual_demands:
        raise ValueError("residual_demands must be nonempty")
    _positive_finite(sample_cost, "sample_cost")

    support: list[Vertex] = []
    acquisition_units = 0
    for vertex, demand in residual_demands.items():
        if not isinstance(demand, int) or isinstance(demand, bool) or demand < 0:
            raise ValueError("residual demands must be nonnegative integers")
        if demand > 0:
            support.append(vertex)
            acquisition_units += demand

    acquisition = sample_cost * acquisition_units
    if not support:
        return RobustSwitchingCertificate(
            support=(),
            lower_order=(),
            robust_order=(),
            acquisition_cost=0.0,
            lower_switching_cost=0.0,
            upper_switching_cost=0.0,
            lower_total_cost=0.0,
            upper_total_cost=0.0,
            robust_route_regret_upper_bound=0.0,
        )

    points: list[Hashable] = list(support)
    if start is not None and start not in points:
        points.append(start)
    validate_symmetric_envelope(points, estimates, radii)

    lower_costs = _envelope_cost_table(points, estimates, radii, upper=False)
    upper_costs = _envelope_cost_table(points, estimates, radii, upper=True)
    lower_value, lower_order = _shortest_route(
        support,
        lower_costs,
        start=start,
    )
    upper_value, robust_order = _shortest_route(
        support,
        upper_costs,
        start=start,
    )
    return RobustSwitchingCertificate(
        support=tuple(support),
        lower_order=lower_order,
        robust_order=robust_order,
        acquisition_cost=acquisition,
        lower_switching_cost=lower_value,
        upper_switching_cost=upper_value,
        lower_total_cost=acquisition + lower_value,
        upper_total_cost=acquisition + upper_value,
        robust_route_regret_upper_bound=max(0.0, upper_value - lower_value),
    )


def robust_improvement_certificate(
    old: RobustSwitchingCertificate,
    new: RobustSwitchingCertificate,
    *,
    tolerance: float = 1e-12,
) -> RobustImprovementCertificate:
    """Certify strict cost improvement from simultaneous old/new envelopes."""
    _nonnegative_finite(tolerance, "tolerance")
    release = old.lower_total_cost - new.upper_total_cost
    return RobustImprovementCertificate(
        old_lower_total_cost=old.lower_total_cost,
        new_upper_total_cost=new.upper_total_cost,
        guaranteed_release=release,
        strict_improvement_certified=release > tolerance,
    )


def _envelope_cost_table(
    points: Sequence[Point],
    estimates: Mapping[tuple[Point, Point], float],
    radii: Mapping[tuple[Point, Point], float],
    *,
    upper: bool,
) -> dict[tuple[Point, Point], float]:
    result: dict[tuple[Point, Point], float] = {}
    for first in points:
        for second in points:
            if first == second:
                result[(first, second)] = 0.0
                continue
            estimate = estimates[(first, second)]
            radius = radii[(first, second)]
            result[(first, second)] = (
                estimate + radius if upper else max(0.0, estimate - radius)
            )
    return result


def _shortest_route(
    support: Sequence[Point],
    costs: Mapping[tuple[Point, Point], float],
    *,
    start: Point | None,
) -> tuple[float, tuple[Point, ...]]:
    """Solve a shortest rooted permutation route for arbitrary edge weights."""
    required = tuple(support)
    if not required:
        return 0.0, ()
    if len(required) == 1:
        value = 0.0 if start is None else costs[(start, required[0])]
        return value, required

    size = len(required)
    dp: dict[tuple[int, int], tuple[float, int | None]] = {}
    for index, vertex in enumerate(required):
        initial = 0.0 if start is None else costs[(start, vertex)]
        dp[(1 << index, index)] = (initial, None)

    full_mask = (1 << size) - 1
    for mask in range(1, full_mask + 1):
        for last in range(size):
            if (mask, last) not in dp:
                continue
            current, _ = dp[(mask, last)]
            for nxt in range(size):
                if mask & (1 << nxt):
                    continue
                new_mask = mask | (1 << nxt)
                candidate = current + costs[(required[last], required[nxt])]
                key = (new_mask, nxt)
                if candidate < dp.get(key, (inf, None))[0]:
                    dp[key] = (candidate, last)

    end = min(range(size), key=lambda index: dp[(full_mask, index)][0])
    value = dp[(full_mask, end)][0]
    indices: list[int] = []
    mask = full_mask
    current: int | None = end
    while current is not None:
        indices.append(current)
        _, predecessor = dp[(mask, current)]
        mask ^= 1 << current
        current = predecessor
    indices.reverse()
    return value, tuple(required[index] for index in indices)


def _validate_points(points: tuple[Point, ...]) -> None:
    if not points:
        raise ValueError("points must be nonempty")
    if len(set(points)) != len(points):
        raise ValueError("points must be unique")


def _probability_level(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0 or value >= 1.0:
        raise ValueError(f"{name} must lie strictly between zero and one")


def _positive_finite(value: float, name: str) -> None:
    if not isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")


def _nonnegative_finite(value: float, name: str) -> None:
    if not isfinite(value) or value < 0.0:
        raise ValueError(f"{name} must be nonnegative and finite")
