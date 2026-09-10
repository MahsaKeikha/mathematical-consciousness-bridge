"""Proposition 64: fast certified heterogeneous-cost integer approximation.

P63 solves the unequal-cost whole-measurement problem exactly with a dynamic
program whose running time depends on the numeric budget. P64 gives a much
cheaper certified alternative in the regime where the P62 continuous optimum
places at least one measurement on every calibrated edge.

The construction simply floors the P62 continuous optimum. Flooring can only
reduce heterogeneous spend, so the result is feasible. The loss in the
separable inverse-square-root uncertainty objective is controlled exactly by
the smallest retained floor ratio.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from math import floor, isfinite, sqrt
from typing import TypeVar

from consciousness_bridge.heterogeneous_cost_transition_calibration import (
    optimal_heterogeneous_cost_allocation,
)

Edge = TypeVar("Edge", bound=Hashable)


@dataclass(frozen=True)
class FastIntegerApproximation:
    """Certified P64 floor approximation to the P63 integer optimum."""

    continuous_allocations: dict[Hashable, float]
    integer_allocations: dict[Hashable, int]
    total_spend: float
    unspent_budget: float
    objective_value: float
    continuous_lower_bound: float
    min_floor_ratio: float
    certified_factor: float
    certified_upper_bound: float


def fast_floor_approximation(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    unit_costs: Mapping[Edge, float],
    total_budget: float,
    *,
    tolerance: float = 1e-12,
) -> FastIntegerApproximation:
    """Floor the exact P62 allocation and certify its P63 approximation factor.

    Let n* be the P62 continuous optimum and suppose n*_e >= 1 for every edge.
    Define k_e = floor(n*_e). Then k is integer-feasible because

        sum_e c_e k_e <= sum_e c_e n*_e = B.

    With

        r = min_e floor(n*_e) / n*_e,

    every objective term increases by at most 1/sqrt(r), so

        U(k) <= U_cont*(B) / sqrt(r)
             <= U_int*(B) / sqrt(r),

    where U_int* is the unknown exact integer optimum from P63.
    """
    _nonnegative_finite(tolerance, "tolerance")
    continuous = optimal_heterogeneous_cost_allocation(
        coefficients,
        sensitivities,
        unit_costs,
        total_budget,
    )

    too_small = [
        edge
        for edge, allocation in continuous.allocations.items()
        if allocation < 1.0 - tolerance
    ]
    if too_small:
        raise ValueError(
            "P64 floor certificate requires every P62 continuous allocation "
            "to be at least one measurement"
        )

    integers: dict[Edge, int] = {}
    floor_ratios: list[float] = []
    total_spend = 0.0
    objective = 0.0

    for edge, allocation in continuous.allocations.items():
        count = max(1, floor(allocation + tolerance))
        integers[edge] = count
        ratio = count / allocation
        floor_ratios.append(ratio)
        total_spend += unit_costs[edge] * count
        objective += coefficients[edge] * sensitivities[edge] / sqrt(count)

    if total_spend > total_budget + tolerance:
        raise RuntimeError("floor allocation unexpectedly exceeds total budget")

    min_ratio = min(floor_ratios)
    factor = 1.0 / sqrt(min_ratio)
    certified_upper = factor * continuous.objective_value

    return FastIntegerApproximation(
        continuous_allocations=dict(continuous.allocations),
        integer_allocations=dict(integers),
        total_spend=total_spend,
        unspent_budget=max(0.0, total_budget - total_spend),
        objective_value=objective,
        continuous_lower_bound=continuous.objective_value,
        min_floor_ratio=min_ratio,
        certified_factor=factor,
        certified_upper_bound=certified_upper,
    )


def uniform_factor_from_minimum_continuous_count(minimum_count: float) -> float:
    """Return the P64 uniform factor sqrt(nu/(nu-1)) for nu > 1.

    If every P62 continuous allocation satisfies n*_e >= nu > 1, then

        floor(n*_e) >= n*_e - 1 >= (1 - 1/nu) n*_e,

    and therefore the P64 floor allocation is within

        sqrt(nu / (nu - 1))

    of the exact P63 integer optimum.
    """
    if not isfinite(minimum_count) or minimum_count <= 1.0:
        raise ValueError("minimum_count must be finite and strictly greater than one")
    return sqrt(minimum_count / (minimum_count - 1.0))


def _nonnegative_finite(value: float, name: str) -> None:
    if not isfinite(value) or value < 0.0:
        raise ValueError(f"{name} must be nonnegative and finite")
