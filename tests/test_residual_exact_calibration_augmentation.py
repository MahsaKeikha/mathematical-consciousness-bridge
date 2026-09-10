from itertools import product
from math import sqrt

import pytest

from consciousness_bridge.residual_exact_calibration_augmentation import (
    residual_exact_augmentation,
)


def _objective(allocation, coefficients, sensitivities):
    return sum(
        coefficients[e] * sensitivities[e] / sqrt(allocation[e])
        for e in allocation
    )


def test_residual_is_strictly_below_baseline_budget():
    result = residual_exact_augmentation(
        {"a": 1.0, "b": 2.0, "c": 3.0},
        {"a": 1.0, "b": 1.0, "c": 1.0},
        {"a": 2, "b": 3, "c": 5},
        37,
    )
    assert 0 <= result.residual_budget < 10


def test_augmentation_preserves_floor_and_budget_feasibility():
    costs = {"a": 2, "b": 3, "c": 5}
    result = residual_exact_augmentation(
        {"a": 1.0, "b": 2.0, "c": 4.0},
        {"a": 1.0, "b": 1.0, "c": 1.0},
        costs,
        41,
    )
    for edge in result.allocations:
        assert result.allocations[edge] >= result.floor_allocations[edge] >= 1
    assert result.total_spend <= 41
    assert result.unspent_budget >= 0


def test_residual_dp_is_exact_within_floor_dominating_class():
    coefficients = {"a": 1.0, "b": 2.5, "c": 1.7}
    sensitivities = {"a": 1.0, "b": 1.0, "c": 1.0}
    costs = {"a": 2, "b": 3, "c": 4}
    budget = 29
    result = residual_exact_augmentation(
        coefficients, sensitivities, costs, budget
    )

    floor_alloc = result.floor_allocations
    max_increments = {
        e: result.residual_budget // costs[e] for e in costs
    }
    brute_best = float("inf")
    for increments in product(
        *[range(max_increments[e] + 1) for e in floor_alloc]
    ):
        inc = dict(zip(floor_alloc, increments, strict=True))
        if sum(costs[e] * inc[e] for e in inc) > result.residual_budget:
            continue
        candidate = {
            e: floor_alloc[e] + inc[e] for e in floor_alloc
        }
        brute_best = min(
            brute_best, _objective(candidate, coefficients, sensitivities)
        )

    assert result.objective_value == pytest.approx(brute_best)


def test_augmentation_never_worsens_p65_floor_objective():
    result = residual_exact_augmentation(
        {"a": 1.0, "b": 5.0},
        {"a": 1.0, "b": 1.0},
        {"a": 2, "b": 5},
        26,
    )
    assert result.objective_value <= result.floor_objective
    assert result.objective_improvement >= 0.0


def test_augmented_instance_factor_never_worsens_floor_factor():
    result = residual_exact_augmentation(
        {"a": 1.0, "b": 4.0, "c": 7.0},
        {"a": 1.0, "b": 1.0, "c": 1.0},
        {"a": 1, "b": 3, "c": 6},
        34,
    )
    assert result.augmented_instance_factor <= result.floor_instance_factor
    assert result.augmented_instance_factor <= sqrt(2.0)


def test_zero_residual_returns_floor_exactly():
    result = residual_exact_augmentation(
        {"a": 1.0, "b": 1.0},
        {"a": 1.0, "b": 1.0},
        {"a": 2, "b": 3},
        5,
    )
    assert result.residual_budget == 0
    assert result.residual_spend == 0
    assert result.allocations == result.floor_allocations == {"a": 1, "b": 1}
    assert result.objective_value == pytest.approx(result.floor_objective)
    assert result.augmented_instance_factor == pytest.approx(1.0)


def test_gcd_compresses_residual_budget_exactly():
    result = residual_exact_augmentation(
        {"a": 1.0, "b": 3.0},
        {"a": 1.0, "b": 1.0},
        {"a": 4, "b": 6},
        31,
    )
    assert result.cost_gcd == 2
    assert result.scaled_residual_budget == result.residual_budget // 2
    assert result.residual_spend % 2 == 0


def test_invalid_inputs_are_rejected():
    with pytest.raises(ValueError):
        residual_exact_augmentation({}, {}, {}, 10)
    with pytest.raises(ValueError):
        residual_exact_augmentation(
            {"a": 1.0}, {"a": 1.0}, {"a": 2}, 1
        )
    with pytest.raises(ValueError):
        residual_exact_augmentation(
            {"a": 1.0}, {"a": 1.0}, {"a": 1.5}, 10  # type: ignore[arg-type]
        )
