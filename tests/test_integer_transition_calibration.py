from math import ceil, sqrt

import pytest

from consciousness_bridge.integer_transition_calibration import (
    relative_overhead_bound,
    rounded_integer_calibration_allocation,
    sufficient_integer_budget_for_target,
)
from consciousness_bridge.optimal_transition_calibration import (
    optimal_continuous_calibration_allocation,
)


def test_integer_construction_respects_hard_budget():
    result = rounded_integer_calibration_allocation(
        {"ab": 1.0, "bc": 2.0, "cd": 3.0},
        {"ab": 1.0, "bc": 1.5, "cd": 0.5},
        100,
    )
    assert result.total_used <= result.total_budget
    assert all(isinstance(value, int) and value >= 1 for value in result.allocations.values())


def test_integer_objective_is_no_worse_than_effective_continuous_optimum():
    coefficients = {"a": 1.0, "b": 2.0, "c": 4.0}
    sensitivities = {"a": 1.0, "b": 0.5, "c": 2.0}
    budget = 80
    result = rounded_integer_calibration_allocation(
        coefficients,
        sensitivities,
        budget,
    )
    effective = optimal_continuous_calibration_allocation(
        coefficients,
        sensitivities,
        float(budget - len(coefficients)),
    )
    assert result.objective_value <= effective.objective_value + 1e-12


def test_reported_multiplicative_overhead_matches_formula():
    result = rounded_integer_calibration_allocation(
        {"a": 1.0, "b": 3.0},
        {"a": 2.0, "b": 1.0},
        50,
    )
    expected = sqrt(50.0 / 48.0)
    assert result.multiplicative_overhead_bound == pytest.approx(expected)
    assert result.overhead_bound_holds
    assert result.objective_value <= result.continuous_reference_value * expected + 1e-12


def test_equal_edge_case_has_nearly_equal_integer_counts():
    result = rounded_integer_calibration_allocation(
        {"a": 1.0, "b": 1.0, "c": 1.0},
        {"a": 1.0, "b": 1.0, "c": 1.0},
        33,
    )
    values = list(result.allocations.values())
    assert max(values) - min(values) <= 1
    assert result.total_used <= 33


def test_target_budget_guarantees_requested_uncertainty():
    coefficients = {"a": 1.0, "b": 1.7, "c": 0.8}
    sensitivities = {"a": 1.0, "b": 2.0, "c": 0.6}
    target = 0.45
    budget = sufficient_integer_budget_for_target(
        coefficients,
        sensitivities,
        target,
    )
    result = rounded_integer_calibration_allocation(
        coefficients,
        sensitivities,
        budget,
    )
    assert result.objective_value <= target + 1e-12


def test_target_budget_is_continuous_requirement_plus_edge_reserve():
    coefficients = {"a": 1.0, "b": 2.0}
    sensitivities = {"a": 1.0, "b": 1.0}
    target = 0.5
    normalization = sum(
        (coefficients[key] * sensitivities[key]) ** (2.0 / 3.0)
        for key in coefficients
    )
    continuous_requirement = normalization**3 / target**2
    expected = len(coefficients) + ceil(continuous_requirement)
    assert sufficient_integer_budget_for_target(
        coefficients,
        sensitivities,
        target,
    ) == expected


def test_relative_overhead_tends_to_one_for_large_budget():
    small = relative_overhead_bound(20, 5)
    large = relative_overhead_bound(1000, 5)
    assert large < small
    assert large > 1.0
    assert large == pytest.approx(sqrt(1000.0 / 995.0))


def test_invalid_budget_and_edge_count_are_rejected():
    with pytest.raises(ValueError):
        rounded_integer_calibration_allocation(
            {"a": 1.0, "b": 1.0},
            {"a": 1.0, "b": 1.0},
            2,
        )
    with pytest.raises(ValueError):
        relative_overhead_bound(5, 5)
    with pytest.raises(ValueError):
        relative_overhead_bound(10, 0)
