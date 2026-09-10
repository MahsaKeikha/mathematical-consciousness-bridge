"""Proposition 56: moving-start metric reoptimization stability.

P55 proves monotone residual execution cost when the metric and current setup
state are fixed. P56 removes the fixed-start restriction. Under the same metric,
the optimal switching path is 1-Lipschitz in its start point, and the resulting
start displacement can erode a P55 cost saving by at most the metric distance
between the two setup states.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from math import isclose

from consciousness_bridge.metric_switching_residual_schedule import (
    shortest_block_schedule,
)
from consciousness_bridge.pruning_aware_switching_monotonicity import (
    componentwise_nonincreasing,
)


@dataclass(frozen=True)
class StartLipschitzCertificate:
    """Exact route values and the metric start-perturbation bound."""

    support: tuple[Hashable, ...]
    first_start: Hashable
    second_start: Hashable
    first_route_cost: float
    second_route_cost: float
    start_distance: float
    absolute_route_change: float
    bound_holds: bool


@dataclass(frozen=True)
class MovingStartCertificate:
    """P55 fixed-start saving corrected for movement of the setup state."""

    old_start: Hashable
    new_start: Hashable
    old_total_cost: float
    new_fixed_start_cost: float
    new_moving_start_cost: float
    fixed_start_release: float
    start_distance: float
    guaranteed_release_lower_bound: float
    actual_release: float
    lower_bound_holds: bool
    strict_decrease_certified: bool


def _unit_demands(support: tuple[Hashable, ...]) -> dict[Hashable, int]:
    if not support:
        raise ValueError("support must be nonempty")
    if len(set(support)) != len(support):
        raise ValueError("support must contain unique preparations")
    return {vertex: 1 for vertex in support}


def start_lipschitz_certificate(
    support: tuple[Hashable, ...],
    costs: Mapping[tuple[Hashable, Hashable], float],
    *,
    first_start: Hashable,
    second_start: Hashable,
    tolerance: float = 1e-12,
) -> StartLipschitzCertificate:
    """Certify |L*(S;s)-L*(S;s')| <= c(s,s')."""
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")
    demands = _unit_demands(support)
    first = shortest_block_schedule(demands, costs, start=first_start)
    second = shortest_block_schedule(demands, costs, start=second_start)
    distance = costs[(first_start, second_start)]
    change = abs(first.switching_cost - second.switching_cost)
    return StartLipschitzCertificate(
        support=support,
        first_start=first_start,
        second_start=second_start,
        first_route_cost=first.switching_cost,
        second_route_cost=second.switching_cost,
        start_distance=distance,
        absolute_route_change=change,
        bound_holds=change <= distance + tolerance,
    )


def moving_start_reoptimization_certificate(
    old_demands: Mapping[Hashable, int],
    new_demands: Mapping[Hashable, int],
    costs: Mapping[tuple[Hashable, Hashable], float],
    *,
    old_start: Hashable,
    new_start: Hashable,
    sample_cost: float = 1.0,
    tolerance: float = 1e-12,
) -> MovingStartCertificate:
    """Certify the P56 residual/start perturbation inequality.

    For r' <= r, P55 gives a nonnegative fixed-start release

        Delta_fixed = C*(r; s) - C*(r'; s).

    P56 proves that replacing the new start s by s' changes the new switching
    optimum by at most c(s, s'). Hence

        C*(r; s) - C*(r'; s') >= Delta_fixed - c(s, s').
    """
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")
    if not componentwise_nonincreasing(old_demands, new_demands):
        raise ValueError("new residual demands must be componentwise nonincreasing")

    old = shortest_block_schedule(
        old_demands,
        costs,
        start=old_start,
        sample_cost=sample_cost,
    )
    new_fixed = shortest_block_schedule(
        new_demands,
        costs,
        start=old_start,
        sample_cost=sample_cost,
    )
    new_moving = shortest_block_schedule(
        new_demands,
        costs,
        start=new_start,
        sample_cost=sample_cost,
    )

    distance = costs[(old_start, new_start)]
    fixed_release = old.total_cost - new_fixed.total_cost
    lower_bound = fixed_release - distance
    actual_release = old.total_cost - new_moving.total_cost

    return MovingStartCertificate(
        old_start=old_start,
        new_start=new_start,
        old_total_cost=old.total_cost,
        new_fixed_start_cost=new_fixed.total_cost,
        new_moving_start_cost=new_moving.total_cost,
        fixed_start_release=fixed_release,
        start_distance=distance,
        guaranteed_release_lower_bound=lower_bound,
        actual_release=actual_release,
        lower_bound_holds=actual_release + tolerance >= lower_bound,
        strict_decrease_certified=lower_bound > tolerance,
    )


def fixed_support_start_change(
    residual_demands: Mapping[Hashable, int],
    costs: Mapping[tuple[Hashable, Hashable], float],
    *,
    first_start: Hashable,
    second_start: Hashable,
    sample_cost: float = 1.0,
) -> tuple[float, float]:
    """Return actual total-cost change and its metric upper bound for fixed demand."""
    first = shortest_block_schedule(
        residual_demands,
        costs,
        start=first_start,
        sample_cost=sample_cost,
    )
    second = shortest_block_schedule(
        residual_demands,
        costs,
        start=second_start,
        sample_cost=sample_cost,
    )
    change = abs(first.total_cost - second.total_cost)
    bound = costs[(first_start, second_start)]
    return change, bound


def release_identity_check(
    certificate: MovingStartCertificate,
    *,
    tolerance: float = 1e-12,
) -> bool:
    """Check the exact bookkeeping identity for actual moving-start release."""
    return isclose(
        certificate.actual_release,
        certificate.old_total_cost - certificate.new_moving_start_cost,
        rel_tol=0.0,
        abs_tol=tolerance,
    )
