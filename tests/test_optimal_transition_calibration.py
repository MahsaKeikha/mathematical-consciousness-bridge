from math import isclose, log, sqrt

import pytest

from consciousness_bridge.optimal_transition_calibration import (
    hoeffding_coefficient,
    objective_value,
    optimal_continuous_calibration_allocation,
    sufficient_budget_for_target,
)


def test_equal_edges_receive_equal_budget():
    result = optimal_continuous_calibration_allocation(
        {"ab": 2.0, "bc": 2.0, "cd": 2.0},
        {"ab": 1.0, "bc": 1.0, "cd": 1.0},
        90.0,
    )
    assert result.allocations == pytest.approx({"ab": 30.0, "bc": 30.0, "cd": 30.0})


def test_allocation_follows_two_thirds_power_law():
    result = optimal_continuous_calibration_allocation(
        {"a": 1.0, "b": 8.0},
        {"a": 1.0, "b": 1.0},
        50.0,
    )
    assert result.allocations["b"] / result.allocations["a"] == pytest.approx(4.0)
    assert sum(result.allocations.values()) == pytest.approx(50.0)


def test_closed_form_objective_matches_direct_evaluation():
    coefficients = {"a": 1.2, "b": 0.7, "c": 2.1}
    sensitivities = {"a": 1.0, "b": 3.0, "c": 0.5}
    result = optimal_continuous_calibration_allocation(
        coefficients,
        sensitivities,
        120.0,
    )
    direct = objective_value(result.allocations, coefficients, sensitivities)
    assert direct == pytest.approx(result.objective_value)


def test_optimum_beats_nearby_budget_preserving_perturbation():
    coefficients = {"a": 1.0, "b": 2.0, "c": 3.0}
    sensitivities = {"a": 1.0, "b": 1.5, "c": 0.7}
    result = optimal_continuous_calibration_allocation(
        coefficients,
        sensitivities,
        100.0,
    )
    perturbed = dict(result.allocations)
    perturbed["a"] += 1.0
    perturbed["b"] -= 1.0
    assert objective_value(
        result.allocations,
        coefficients,
        sensitivities,
    ) < objective_value(perturbed, coefficients, sensitivities)


def test_target_budget_formula_is_sufficient():
    coefficients = {"a": 1.0, "b": 1.5, "c": 0.8}
    sensitivities = {"a": 1.0, "b": 2.0, "c": 0.5}
    target = 0.4
    budget = sufficient_budget_for_target(coefficients, sensitivities, target)
    result = optimal_continuous_calibration_allocation(
        coefficients,
        sensitivities,
        float(budget),
    )
    assert result.objective_value <= target


def test_hoeffding_coefficient_matches_radius_scaling():
    coefficient = hoeffding_coefficient(3.0, 0.05)
    expected = 3.0 * sqrt(log(2.0 / 0.05) / 2.0)
    assert coefficient == pytest.approx(expected)
    assert isclose((coefficient / 10.0) * 10.0, coefficient)


def test_invalid_inputs_rejected():
    with pytest.raises(ValueError):
        optimal_continuous_calibration_allocation({}, {}, 10.0)
    with pytest.raises(ValueError):
        optimal_continuous_calibration_allocation({"a": 1.0}, {"b": 1.0}, 10.0)
    with pytest.raises(ValueError):
        sufficient_budget_for_target({"a": 1.0}, {"a": 1.0}, 0.0)
