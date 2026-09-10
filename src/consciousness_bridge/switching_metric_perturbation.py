"""Proposition 57: switching-metric perturbation reoptimization stability.

P56 controls changes in the current setup state while the switching metric is
fixed. P57 controls deterministic changes in the metric itself. If two finite
metrics differ uniformly by at most delta on the relevant setup/preparation
points, an optimal rooted Hamiltonian path changes by at most q * delta, where
q is the maximum number of nontrivial route edges required by the active
support and start state.

The module also composes this metric-drift term with the P55 fixed-start
residual release and the P56 moving-start term, and exposes a tighter route-reuse
certificate that evaluates an old optimal order directly under the new metric.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from math import isfinite

from consciousness_bridge.metric_switching_residual_schedule import (
    shortest_block_schedule,
    switching_path_cost,
    validate_metric_costs,
)
from consciousness_bridge.pruning_aware_switching_monotonicity import (
    componentwise_nonincreasing,
)


@dataclass(frozen=True)
class MetricPerturbationCertificate:
    """Uniform-metric perturbation certificate for one fixed residual state."""

    support: tuple[Hashable, ...]
    start: Hashable | None
    metric_sup_distance: float
    route_edge_count: int
    old_switching_cost: float
    new_switching_cost: float
    absolute_switching_change: float
    uniform_bound: float
    bound_holds: bool


@dataclass(frozen=True)
class MetricDriftReoptimizationCertificate:
    """P55-P57 release bound under residual, start, and metric changes."""

    old_total_cost: float
    new_fixed_old_geometry_cost: float
    new_total_cost: float
    fixed_geometry_release: float
    metric_sup_distance: float
    old_metric_start_distance: float
    new_metric_start_distance: float
    old_start_route_edges: int
    new_start_route_edges: int
    perturbation_penalty: float
    guaranteed_release_lower_bound: float
    actual_release: float
    lower_bound_holds: bool
    strict_decrease_certified: bool


@dataclass(frozen=True)
class RouteReuseCertificate:
    """One-sided perturbation bound obtained by reusing an old optimal order."""

    old_optimal_order: tuple[Hashable, ...]
    old_optimal_switching_cost: float
    reused_order_new_switching_cost: float
    new_optimal_switching_cost: float
    one_sided_change_upper_bound: float
    actual_change: float
    bound_holds: bool


def positive_support(residual_demands: Mapping[Hashable, int]) -> tuple[Hashable, ...]:
    """Return positive-demand preparations in declared mapping order."""
    if not residual_demands:
        raise ValueError("residual_demands must be nonempty")
    support: list[Hashable] = []
    for vertex, demand in residual_demands.items():
        if not isinstance(demand, int) or isinstance(demand, bool) or demand < 0:
            raise ValueError("residual demands must be nonnegative integers")
        if demand > 0:
            support.append(vertex)
    return tuple(support)


def rooted_route_edge_count(
    support: Sequence[Hashable],
    *,
    start: Hashable | None,
) -> int:
    """Return the sharp maximum number of nontrivial edges in an optimal route.

    With no start, a path through m active preparations has m-1 edges. With an
    external start it has m edges. If the start itself is an active preparation,
    metric shortcutting permits an optimum that begins there, again giving m-1
    nontrivial edges.
    """
    declared = tuple(support)
    if len(set(declared)) != len(declared):
        raise ValueError("support must contain unique preparations")
    m = len(declared)
    if m == 0:
        return 0
    if start is None or start in declared:
        return m - 1
    return m


def metric_sup_distance(
    points: Sequence[Hashable],
    old_costs: Mapping[tuple[Hashable, Hashable], float],
    new_costs: Mapping[tuple[Hashable, Hashable], float],
) -> float:
    """Return max |c-c'| on a finite common metric point set."""
    declared = tuple(points)
    if not declared:
        raise ValueError("points must be nonempty")
    if len(set(declared)) != len(declared):
        raise ValueError("points must be unique")
    validate_metric_costs(declared, old_costs)
    validate_metric_costs(declared, new_costs)
    return max(
        abs(old_costs[(first, second)] - new_costs[(first, second)])
        for first in declared
        for second in declared
    )


def metric_perturbation_certificate(
    residual_demands: Mapping[Hashable, int],
    old_costs: Mapping[tuple[Hashable, Hashable], float],
    new_costs: Mapping[tuple[Hashable, Hashable], float],
    *,
    start: Hashable | None = None,
    sample_cost: float = 1.0,
    tolerance: float = 1e-12,
) -> MetricPerturbationCertificate:
    """Certify |L_c^*(S;s)-L_c'^*(S;s)| <= q(S;s) ||c-c'||_inf."""
    _validate_tolerance(tolerance)
    support = positive_support(residual_demands)
    old = shortest_block_schedule(
        residual_demands,
        old_costs,
        start=start,
        sample_cost=sample_cost,
    )
    new = shortest_block_schedule(
        residual_demands,
        new_costs,
        start=start,
        sample_cost=sample_cost,
    )

    if not support:
        return MetricPerturbationCertificate(
            support=(),
            start=start,
            metric_sup_distance=0.0,
            route_edge_count=0,
            old_switching_cost=0.0,
            new_switching_cost=0.0,
            absolute_switching_change=0.0,
            uniform_bound=0.0,
            bound_holds=True,
        )

    points = list(support)
    if start is not None and start not in points:
        points.append(start)
    delta = metric_sup_distance(points, old_costs, new_costs)
    edge_count = rooted_route_edge_count(support, start=start)
    change = abs(old.switching_cost - new.switching_cost)
    bound = edge_count * delta
    return MetricPerturbationCertificate(
        support=support,
        start=start,
        metric_sup_distance=delta,
        route_edge_count=edge_count,
        old_switching_cost=old.switching_cost,
        new_switching_cost=new.switching_cost,
        absolute_switching_change=change,
        uniform_bound=bound,
        bound_holds=change <= bound + tolerance,
    )


def route_reuse_certificate(
    residual_demands: Mapping[Hashable, int],
    old_costs: Mapping[tuple[Hashable, Hashable], float],
    new_costs: Mapping[tuple[Hashable, Hashable], float],
    *,
    old_start: Hashable | None = None,
    new_start: Hashable | None = None,
    sample_cost: float = 1.0,
    tolerance: float = 1e-12,
) -> RouteReuseCertificate:
    """Bound new optimal switching cost by evaluating the old optimal order.

    If pi_c is optimal under the old geometry, then

        L_c'(S; s') <= length_c'(pi_c; s').

    Therefore the actual optimal switching-cost change is no larger than the
    directly computable reused-route change.
    """
    _validate_tolerance(tolerance)
    old = shortest_block_schedule(
        residual_demands,
        old_costs,
        start=old_start,
        sample_cost=sample_cost,
    )
    new = shortest_block_schedule(
        residual_demands,
        new_costs,
        start=new_start,
        sample_cost=sample_cost,
    )
    reused = switching_path_cost(old.order, new_costs, start=new_start)
    upper = reused - old.switching_cost
    actual = new.switching_cost - old.switching_cost
    return RouteReuseCertificate(
        old_optimal_order=old.order,
        old_optimal_switching_cost=old.switching_cost,
        reused_order_new_switching_cost=reused,
        new_optimal_switching_cost=new.switching_cost,
        one_sided_change_upper_bound=upper,
        actual_change=actual,
        bound_holds=actual <= upper + tolerance,
    )


def metric_drift_reoptimization_certificate(
    old_demands: Mapping[Hashable, int],
    new_demands: Mapping[Hashable, int],
    old_costs: Mapping[tuple[Hashable, Hashable], float],
    new_costs: Mapping[tuple[Hashable, Hashable], float],
    *,
    old_start: Hashable,
    new_start: Hashable,
    sample_cost: float = 1.0,
    tolerance: float = 1e-12,
) -> MetricDriftReoptimizationCertificate:
    """Compose P55 residual release with P56 start motion and P57 metric drift.

    Let Delta_fixed be the P55 release computed under the old metric and old
    start. If delta is the sup metric perturbation on the new active support plus
    both starts, then the new route perturbation is bounded in two valid orders:

        c(old_start,new_start) + q(new_start) delta,
        q(old_start) delta + c'(old_start,new_start).

    Taking the smaller gives the deterministic P57 penalty.
    """
    _validate_tolerance(tolerance)
    if not componentwise_nonincreasing(old_demands, new_demands):
        raise ValueError("new residual demands must be componentwise nonincreasing")

    old = shortest_block_schedule(
        old_demands,
        old_costs,
        start=old_start,
        sample_cost=sample_cost,
    )
    new_fixed = shortest_block_schedule(
        new_demands,
        old_costs,
        start=old_start,
        sample_cost=sample_cost,
    )
    new = shortest_block_schedule(
        new_demands,
        new_costs,
        start=new_start,
        sample_cost=sample_cost,
    )

    support = positive_support(new_demands)
    fixed_release = old.total_cost - new_fixed.total_cost
    if not support:
        delta = 0.0
        old_distance = old_costs[(old_start, new_start)]
        new_distance = new_costs[(old_start, new_start)]
        old_edges = 0
        new_edges = 0
        penalty = 0.0
    else:
        points = list(support)
        for point in (old_start, new_start):
            if point not in points:
                points.append(point)
        delta = metric_sup_distance(points, old_costs, new_costs)
        old_distance = old_costs[(old_start, new_start)]
        new_distance = new_costs[(old_start, new_start)]
        old_edges = rooted_route_edge_count(support, start=old_start)
        new_edges = rooted_route_edge_count(support, start=new_start)
        penalty = min(
            old_distance + new_edges * delta,
            old_edges * delta + new_distance,
        )

    lower = fixed_release - penalty
    actual = old.total_cost - new.total_cost
    return MetricDriftReoptimizationCertificate(
        old_total_cost=old.total_cost,
        new_fixed_old_geometry_cost=new_fixed.total_cost,
        new_total_cost=new.total_cost,
        fixed_geometry_release=fixed_release,
        metric_sup_distance=delta,
        old_metric_start_distance=old_distance,
        new_metric_start_distance=new_distance,
        old_start_route_edges=old_edges,
        new_start_route_edges=new_edges,
        perturbation_penalty=penalty,
        guaranteed_release_lower_bound=lower,
        actual_release=actual,
        lower_bound_holds=actual + tolerance >= lower,
        strict_decrease_certified=lower > tolerance,
    )


def _validate_tolerance(tolerance: float) -> None:
    if not isfinite(tolerance) or tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative and finite")
