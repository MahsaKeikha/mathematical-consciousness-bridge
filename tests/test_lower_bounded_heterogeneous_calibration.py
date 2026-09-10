import math

import pytest

from consciousness_bridge.exact_heterogeneous_integer_calibration import (
    exact_heterogeneous_integer_allocation,
)
from consciousness_bridge.heterogeneous_cost_transition_calibration import (
    optimal_heterogeneous_cost_allocation,
)
from consciousness_bridge.lower_bounded_heterogeneous_calibration import (
    baseline_safe_floor_approximation,
    optimal_lower_bounded_heterogeneous_allocation,
)


def _problem():
    coefficients = {"a": 1.0, "b": 4.0, "c": 9.0}
    sensitivities = {"a": 1.0, "b": 1.0, "c": 1.0}
    costs = {"a": 9.0, "b": 4.0, "c": 1.0}
    return coefficients, sensitivities, costs


def test_baseline_budget_pins_every_edge_at_one():
    coefficients, sensitivities, costs = _problem()
    result = optimal_lower_bounded_heterogeneous_allocation(
        coefficients, sensitivities, costs, total_budget=sum(costs.values())
    )
    assert result.allocations == {"a": 1.0, "b": 1.0, "c": 1.0}
    assert set(result.pinned_edges) == set(coefficients)
    assert result.free_edges == ()
    assert result.water_level == 0.0
    assert result.objective_value == pytest.approx(14.0)


def test_mixed_active_set_pins_expensive_low_weight_edge():
    coefficients, sensitivities, costs = _problem()
    result = optimal_lower_bounded_heterogeneous_allocation(
        coefficients, sensitivities, costs, total_budget=20.0
    )
    assert "a" in result.pinned_edges
    assert {"b", "c"}.issubset(set(result.free_edges))
    assert result.allocations["a"] == pytest.approx(1.0)
    assert result.allocations["b"] > 1.0
    assert result.allocations["c"] > result.allocations["b"]
    assert sum(result.budget_shares.values()) == pytest.approx(20.0)


def test_free_edges_share_common_kkt_water_level():
    coefficients, sensitivities, costs = _problem()
    result = optimal_lower_bounded_heterogeneous_allocation(
        coefficients, sensitivities, costs, total_budget=20.0
    )
    for edge in result.free_edges:
        b_edge = coefficients[edge] * sensitivities[edge]
        implied = result.allocations[edge] / (b_edge / costs[edge]) ** (2.0 / 3.0)
        assert implied == pytest.approx(result.water_level)


def test_large_budget_reduces_to_p62_unconstrained_optimum():
    coefficients, sensitivities, costs = _problem()
    budget = 200.0
    p65 = optimal_lower_bounded_heterogeneous_allocation(
        coefficients, sensitivities, costs, budget
    )
    p62 = optimal_heterogeneous_cost_allocation(
        coefficients, sensitivities, costs, budget
    )
    assert not p65.pinned_edges
    assert p65.allocations == pytest.approx(p62.allocations)
    assert p65.objective_value == pytest.approx(p62.objective_value)


def test_floor_approximation_is_baseline_safe_and_budget_feasible():
    coefficients, sensitivities, costs = _problem()
    approximation = baseline_safe_floor_approximation(
        coefficients, sensitivities, costs, total_budget=20.0
    )
    assert all(count >= 1 for count in approximation.allocations.values())
    assert approximation.budget_used <= 20.0
    assert approximation.objective_value >= approximation.continuous_objective
    assert approximation.instance_factor <= math.sqrt(2.0) + 1e-12
    assert approximation.universal_factor == pytest.approx(math.sqrt(2.0))


def test_instance_factor_bounds_floor_objective_relative_to_p65_continuous():
    coefficients, sensitivities, costs = _problem()
    approximation = baseline_safe_floor_approximation(
        coefficients, sensitivities, costs, total_budget=20.0
    )
    assert approximation.objective_value <= pytest.approx(
        approximation.instance_factor * approximation.continuous_objective
    )


def test_universal_sqrt_two_factor_holds_against_exact_p63_integer_optimum():
    coefficients = {"a": 1.0, "b": 4.0, "c": 9.0}
    sensitivities = {"a": 1.0, "b": 1.0, "c": 1.0}
    integer_costs = {"a": 9, "b": 4, "c": 1}
    budget = 20
    approximation = baseline_safe_floor_approximation(
        coefficients,
        sensitivities,
        {edge: float(cost) for edge, cost in integer_costs.items()},
        float(budget),
    )
    exact = exact_heterogeneous_integer_allocation(
        coefficients, sensitivities, integer_costs, budget
    )
    assert approximation.objective_value <= math.sqrt(2.0) * exact.objective_value
    assert approximation.objective_value <= approximation.instance_factor * exact.objective_value


def test_infeasible_budget_is_rejected():
    coefficients, sensitivities, costs = _problem()
    with pytest.raises(ValueError, match="mandatory observation"):
        optimal_lower_bounded_heterogeneous_allocation(
            coefficients, sensitivities, costs, total_budget=13.9
        )


def test_invalid_keys_and_nonpositive_inputs_are_rejected():
    with pytest.raises(ValueError, match="share keys"):
        optimal_lower_bounded_heterogeneous_allocation(
            {"a": 1.0}, {"b": 1.0}, {"a": 1.0}, 2.0
        )
    with pytest.raises(ValueError, match="positive and finite"):
        optimal_lower_bounded_heterogeneous_allocation(
            {"a": 0.0}, {"a": 1.0}, {"a": 1.0}, 2.0
        )
