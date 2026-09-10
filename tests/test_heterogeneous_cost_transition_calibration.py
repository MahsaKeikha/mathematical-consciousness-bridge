import pytest

from consciousness_bridge.heterogeneous_cost_transition_calibration import (
    budget_used,
    objective_value,
    optimal_heterogeneous_cost_allocation,
    sufficient_budget_for_target,
)
from consciousness_bridge.optimal_transition_calibration import (
    optimal_continuous_calibration_allocation,
)


def test_equal_unit_costs_reduce_exactly_to_p59():
    coefficients = {"ab": 1.2, "bc": 0.8, "cd": 2.1}
    sensitivities = {"ab": 1.0, "bc": 2.0, "cd": 0.5}
    unit_costs = {edge: 1.0 for edge in coefficients}
    budget = 120.0

    p62 = optimal_heterogeneous_cost_allocation(
        coefficients,
        sensitivities,
        unit_costs,
        budget,
    )
    p59 = optimal_continuous_calibration_allocation(
        coefficients,
        sensitivities,
        budget,
    )
    assert p62.allocations == pytest.approx(p59.allocations)
    assert p62.objective_value == pytest.approx(p59.objective_value)


def test_budget_is_used_exactly():
    result = optimal_heterogeneous_cost_allocation(
        {"a": 1.0, "b": 2.0, "c": 4.0},
        {"a": 1.0, "b": 1.5, "c": 0.5},
        {"a": 1.0, "b": 3.0, "c": 5.0},
        250.0,
    )
    assert sum(result.budget_shares.values()) == pytest.approx(250.0)
    assert budget_used(
        result.allocations,
        {"a": 1.0, "b": 3.0, "c": 5.0},
    ) == pytest.approx(250.0)


def test_sample_counts_follow_cost_minus_two_thirds_law():
    result = optimal_heterogeneous_cost_allocation(
        {"cheap": 1.0, "expensive": 1.0},
        {"cheap": 1.0, "expensive": 1.0},
        {"cheap": 1.0, "expensive": 8.0},
        90.0,
    )
    assert result.allocations["cheap"] / result.allocations["expensive"] == pytest.approx(4.0)


def test_budget_shares_follow_cost_plus_one_third_law():
    result = optimal_heterogeneous_cost_allocation(
        {"cheap": 1.0, "expensive": 1.0},
        {"cheap": 1.0, "expensive": 1.0},
        {"cheap": 1.0, "expensive": 8.0},
        90.0,
    )
    assert result.budget_shares["expensive"] / result.budget_shares["cheap"] == pytest.approx(2.0)


def test_closed_form_objective_matches_direct_evaluation():
    coefficients = {"a": 1.7, "b": 0.9, "c": 2.4}
    sensitivities = {"a": 1.0, "b": 3.0, "c": 0.8}
    unit_costs = {"a": 4.0, "b": 1.0, "c": 2.5}
    result = optimal_heterogeneous_cost_allocation(
        coefficients,
        sensitivities,
        unit_costs,
        180.0,
    )
    assert objective_value(
        result.allocations,
        coefficients,
        sensitivities,
    ) == pytest.approx(result.objective_value)


def test_optimum_beats_small_cost_preserving_perturbation():
    coefficients = {"a": 1.0, "b": 2.0, "c": 3.0}
    sensitivities = {"a": 1.0, "b": 1.2, "c": 0.7}
    unit_costs = {"a": 1.0, "b": 2.0, "c": 4.0}
    result = optimal_heterogeneous_cost_allocation(
        coefficients,
        sensitivities,
        unit_costs,
        200.0,
    )

    perturbed = dict(result.allocations)
    # Add cost 0.2 to edge a and remove exactly cost 0.2 from edge b.
    perturbed["a"] += 0.2
    perturbed["b"] -= 0.1
    assert budget_used(perturbed, unit_costs) == pytest.approx(200.0)
    assert objective_value(
        result.allocations,
        coefficients,
        sensitivities,
    ) < objective_value(perturbed, coefficients, sensitivities)


def test_target_budget_formula_is_sufficient():
    coefficients = {"a": 1.0, "b": 1.3, "c": 0.6}
    sensitivities = {"a": 1.0, "b": 2.0, "c": 0.7}
    unit_costs = {"a": 1.0, "b": 5.0, "c": 2.0}
    target = 0.5
    budget = sufficient_budget_for_target(
        coefficients,
        sensitivities,
        unit_costs,
        target,
    )
    result = optimal_heterogeneous_cost_allocation(
        coefficients,
        sensitivities,
        unit_costs,
        float(budget),
    )
    assert result.objective_value <= target + 1e-12


def test_invalid_cost_tables_are_rejected():
    with pytest.raises(ValueError):
        optimal_heterogeneous_cost_allocation(
            {"a": 1.0},
            {"a": 1.0},
            {"a": 0.0},
            10.0,
        )
    with pytest.raises(ValueError):
        optimal_heterogeneous_cost_allocation(
            {"a": 1.0},
            {"a": 1.0},
            {"b": 1.0},
            10.0,
        )
