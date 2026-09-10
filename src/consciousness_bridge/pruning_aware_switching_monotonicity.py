"""Proposition 55: pruning-aware metric switching-cost monotonicity.

P54 decomposes the optimal deterministic residual execution cost into fixed
acquisition burden plus the shortest metric Hamiltonian path through the active
preparation support. P55 studies how that optimum changes when P53 residual
demands decrease after further sampling or valid safe pruning.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from math import isclose

from consciousness_bridge.metric_switching_residual_schedule import (
    shortest_block_schedule,
    switching_path_cost,
)


@dataclass(frozen=True)
class MonotonicityCertificate:
    """Exact decomposition of deterministic cost released between two states."""

    old_support: tuple[Hashable, ...]
    new_support: tuple[Hashable, ...]
    old_acquisition_cost: float
    new_acquisition_cost: float
    old_switching_cost: float
    new_switching_cost: float
    acquisition_release: float
    route_release: float
    total_release: float
    support_nested: bool
    cost_nonincreasing: bool


@dataclass(frozen=True)
class ShortcutCertificate:
    """A metric shortcut certificate obtained from an old optimal route."""

    old_order: tuple[Hashable, ...]
    retained_order: tuple[Hashable, ...]
    old_path_cost: float
    shortcut_path_cost: float
    certified_route_release: float


def _validate_residual_demands(
    residual_demands: Mapping[Hashable, int],
) -> dict[Hashable, int]:
    if not residual_demands:
        raise ValueError("residual_demands must be nonempty")
    normalized: dict[Hashable, int] = {}
    for vertex, demand in residual_demands.items():
        if not isinstance(demand, int) or isinstance(demand, bool) or demand < 0:
            raise ValueError("residual demands must be nonnegative integers")
        normalized[vertex] = demand
    return normalized


def positive_support(
    residual_demands: Mapping[Hashable, int],
) -> tuple[Hashable, ...]:
    """Return the positive-demand support in mapping iteration order."""
    demands = _validate_residual_demands(residual_demands)
    return tuple(vertex for vertex, demand in demands.items() if demand > 0)


def componentwise_nonincreasing(
    old_demands: Mapping[Hashable, int],
    new_demands: Mapping[Hashable, int],
) -> bool:
    """Return whether the new state has no larger residual demand at any vertex."""
    old = _validate_residual_demands(old_demands)
    new = _validate_residual_demands(new_demands)
    vertices = set(old) | set(new)
    return all(new.get(vertex, 0) <= old.get(vertex, 0) for vertex in vertices)


def pruning_monotonicity_certificate(
    old_demands: Mapping[Hashable, int],
    new_demands: Mapping[Hashable, int],
    costs: Mapping[tuple[Hashable, Hashable], float],
    *,
    start: Hashable | None = None,
    sample_cost: float = 1.0,
    tolerance: float = 1e-12,
) -> MonotonicityCertificate:
    """Certify the exact P55 cost-release decomposition.

    The function requires componentwise nonincreasing residual demand. Under the
    same metric and start state, the new positive support is then a subset of the
    old support. P54 is solved exactly at both states.
    """
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")
    if not componentwise_nonincreasing(old_demands, new_demands):
        raise ValueError("new residual demands must be componentwise nonincreasing")

    old = _validate_residual_demands(old_demands)
    new = _validate_residual_demands(new_demands)
    all_vertices = tuple(dict.fromkeys((*old, *new)))
    old_full = {vertex: old.get(vertex, 0) for vertex in all_vertices}
    new_full = {vertex: new.get(vertex, 0) for vertex in all_vertices}

    old_result = shortest_block_schedule(
        old_full,
        costs,
        start=start,
        sample_cost=sample_cost,
    )
    new_result = shortest_block_schedule(
        new_full,
        costs,
        start=start,
        sample_cost=sample_cost,
    )

    old_support = tuple(vertex for vertex in all_vertices if old_full[vertex] > 0)
    new_support = tuple(vertex for vertex in all_vertices if new_full[vertex] > 0)
    support_nested = set(new_support).issubset(old_support)

    acquisition_release = old_result.acquisition_cost - new_result.acquisition_cost
    route_release = old_result.switching_cost - new_result.switching_cost
    total_release = old_result.total_cost - new_result.total_cost

    if not isclose(
        total_release,
        acquisition_release + route_release,
        rel_tol=0.0,
        abs_tol=max(tolerance, 1e-12),
    ):
        raise RuntimeError("P55 cost decomposition failed numerically")

    return MonotonicityCertificate(
        old_support=old_support,
        new_support=new_support,
        old_acquisition_cost=old_result.acquisition_cost,
        new_acquisition_cost=new_result.acquisition_cost,
        old_switching_cost=old_result.switching_cost,
        new_switching_cost=new_result.switching_cost,
        acquisition_release=acquisition_release,
        route_release=route_release,
        total_release=total_release,
        support_nested=support_nested,
        cost_nonincreasing=(
            acquisition_release >= -tolerance
            and route_release >= -tolerance
            and total_release >= -tolerance
        ),
    )


def shortcut_certificate_from_old_optimum(
    old_demands: Mapping[Hashable, int],
    new_demands: Mapping[Hashable, int],
    costs: Mapping[tuple[Hashable, Hashable], float],
    *,
    start: Hashable | None = None,
) -> ShortcutCertificate:
    """Certify a route-saving lower bound by deleting vanished preparations.

    The retained route is feasible for the new support. Triangle inequality makes
    its path no longer than the old optimal path. Since the new optimum can only
    be shorter still, this shortcut saving is a certified lower bound on the
    optimal switching-cost release.
    """
    if not componentwise_nonincreasing(old_demands, new_demands):
        raise ValueError("new residual demands must be componentwise nonincreasing")

    old = _validate_residual_demands(old_demands)
    new = _validate_residual_demands(new_demands)
    all_vertices = tuple(dict.fromkeys((*old, *new)))
    old_full = {vertex: old.get(vertex, 0) for vertex in all_vertices}
    new_support = {vertex for vertex in all_vertices if new.get(vertex, 0) > 0}

    old_result = shortest_block_schedule(old_full, costs, start=start)
    retained = tuple(vertex for vertex in old_result.order if vertex in new_support)
    shortcut_cost = switching_path_cost(retained, costs, start=start)
    certified_release = old_result.switching_cost - shortcut_cost

    return ShortcutCertificate(
        old_order=old_result.order,
        retained_order=retained,
        old_path_cost=old_result.switching_cost,
        shortcut_path_cost=shortcut_cost,
        certified_route_release=certified_release,
    )


def support_preserving_release(
    old_demands: Mapping[Hashable, int],
    new_demands: Mapping[Hashable, int],
    *,
    sample_cost: float = 1.0,
) -> float:
    """Return the exact total release when positive support is unchanged.

    With the same support, P54's metric route term is identical, so every cost
    reduction comes from reduced acquisition demand.
    """
    if not componentwise_nonincreasing(old_demands, new_demands):
        raise ValueError("new residual demands must be componentwise nonincreasing")
    old = _validate_residual_demands(old_demands)
    new = _validate_residual_demands(new_demands)
    if set(positive_support(old)) != set(positive_support(new)):
        raise ValueError("positive support must be unchanged")
    return sample_cost * (sum(old.values()) - sum(new.values()))


def retained_order_after_pruning(
    old_order: Sequence[Hashable],
    retained_support: Sequence[Hashable],
) -> tuple[Hashable, ...]:
    """Delete vanished preparations while preserving the old route order."""
    retained = set(retained_support)
    return tuple(vertex for vertex in old_order if vertex in retained)
