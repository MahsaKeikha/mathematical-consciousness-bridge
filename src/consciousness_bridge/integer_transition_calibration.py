"""Proposition 60: integer transition-calibration rounding overhead.

P59 solves a continuous calibration-allocation problem. P60 turns that solution
into an implementable integer allocation under a hard total budget. The
construction reserves one unit of budget per calibrated edge, solves the P59
continuous problem on the remaining budget, and rounds every coordinate upward.

For m calibrated edges and integer budget B > m, the construction uses at most B
samples and achieves the P59 surrogate value associated with continuous budget
B-m. Consequently its multiplicative loss relative to the continuous optimum at
budget B is at most sqrt(B/(B-m)).
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from math import ceil, isfinite, sqrt
from typing import TypeVar

from consciousness_bridge.optimal_transition_calibration import (
    objective_value,
    optimal_continuous_calibration_allocation,
)

Edge = TypeVar("Edge", bound=Hashable)


@dataclass(frozen=True)
class IntegerCalibrationAllocation:
    """Constructive P60 hard-budget integer calibration certificate."""

    allocations: dict[Hashable, int]
    total_used: int
    total_budget: int
    edge_count: int
    reserved_budget: int
    effective_continuous_budget: float
    objective_value: float
    continuous_reference_value: float
    multiplicative_overhead_bound: float
    overhead_bound_holds: bool


def rounded_integer_calibration_allocation(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    total_budget: int,
    *,
    tolerance: float = 1e-12,
) -> IntegerCalibrationAllocation:
    """Construct an integer P59 allocation using at most ``total_budget`` units.

    For ``m`` calibrated edges, require ``total_budget > m``. Let

        N0 = total_budget - m.

    Solve the continuous P59 problem using budget ``N0`` and set

        k_e = ceil(n_e^*(N0)).

    Since ``ceil(x) < x + 1``, the integer allocation uses at most the hard
    budget. Since every rounded coordinate is no smaller than its continuous
    precursor, the uncertainty surrogate cannot increase relative to the P59
    optimum at ``N0``.
    """
    _validate_inputs(coefficients, sensitivities, total_budget, tolerance)
    edge_count = len(coefficients)
    effective_budget = float(total_budget - edge_count)
    continuous = optimal_continuous_calibration_allocation(
        coefficients,
        sensitivities,
        effective_budget,
    )
    allocations = {
        edge: ceil(value)
        for edge, value in continuous.allocations.items()
    }
    total_used = sum(allocations.values())
    if total_used > total_budget:
        raise RuntimeError("P60 ceiling construction exceeded the hard budget")

    integer_as_float = {edge: float(value) for edge, value in allocations.items()}
    achieved = objective_value(integer_as_float, coefficients, sensitivities)
    continuous_at_full_budget = optimal_continuous_calibration_allocation(
        coefficients,
        sensitivities,
        float(total_budget),
    ).objective_value
    overhead = sqrt(total_budget / effective_budget)

    return IntegerCalibrationAllocation(
        allocations=dict(allocations),
        total_used=total_used,
        total_budget=total_budget,
        edge_count=edge_count,
        reserved_budget=edge_count,
        effective_continuous_budget=effective_budget,
        objective_value=achieved,
        continuous_reference_value=continuous_at_full_budget,
        multiplicative_overhead_bound=overhead,
        overhead_bound_holds=(
            achieved <= continuous_at_full_budget * overhead + tolerance
        ),
    )


def sufficient_integer_budget_for_target(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    target_uncertainty: float,
) -> int:
    """Return a sufficient hard integer budget for P60 target uncertainty.

    If P59 needs continuous budget ``N_req`` to reach the target, P60 needs at
    most ``m + ceil(N_req)`` total integer units, where ``m`` is the number of
    calibrated edges.
    """
    if not isfinite(target_uncertainty) or target_uncertainty <= 0.0:
        raise ValueError("target_uncertainty must be positive and finite")
    _validate_maps(coefficients, sensitivities)

    normalization = sum(
        (coefficients[edge] * sensitivities[edge]) ** (2.0 / 3.0)
        for edge in coefficients
    )
    required_continuous = normalization**3 / target_uncertainty**2
    return len(coefficients) + ceil(required_continuous)


def relative_overhead_bound(total_budget: int, edge_count: int) -> float:
    """Return the P60 worst-case ratio to the P59 continuous optimum at B."""
    if not isinstance(total_budget, int) or isinstance(total_budget, bool):
        raise TypeError("total_budget must be an integer")
    if not isinstance(edge_count, int) or isinstance(edge_count, bool):
        raise TypeError("edge_count must be an integer")
    if edge_count <= 0:
        raise ValueError("edge_count must be positive")
    if total_budget <= edge_count:
        raise ValueError("total_budget must be strictly larger than edge_count")
    return sqrt(total_budget / (total_budget - edge_count))


def _validate_inputs(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
    total_budget: int,
    tolerance: float,
) -> None:
    _validate_maps(coefficients, sensitivities)
    if not isinstance(total_budget, int) or isinstance(total_budget, bool):
        raise TypeError("total_budget must be an integer")
    if total_budget <= len(coefficients):
        raise ValueError("total_budget must be strictly larger than edge count")
    if not isfinite(tolerance) or tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative and finite")


def _validate_maps(
    coefficients: Mapping[Edge, float],
    sensitivities: Mapping[Edge, float],
) -> None:
    if not coefficients:
        raise ValueError("coefficients must be nonempty")
    if set(coefficients) != set(sensitivities):
        raise ValueError("sensitivities must cover exactly the coefficient keys")
    for edge, coefficient in coefficients.items():
        sensitivity = sensitivities[edge]
        if not isfinite(coefficient) or coefficient <= 0.0:
            raise ValueError("coefficients must be positive and finite")
        if not isfinite(sensitivity) or sensitivity <= 0.0:
            raise ValueError("sensitivities must be positive and finite")
