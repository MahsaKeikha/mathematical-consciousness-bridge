from itertools import product

import pytest

from consciousness_bridge.exact_heterogeneous_integer_calibration import (
    exact_heterogeneous_integer_allocation,
    integer_objective_value,
)


def brute_force(coefficients, sensitivities, costs, budget):
    edges = tuple(coefficients)
    best_value = float("inf")
    best = None
    ranges = [range(1, budget // costs[edge] + 1) for edge in edges]
    for counts in product(*ranges):
        allocation = dict(zip(edges, counts, strict=True))
        spend = sum(costs[edge] * allocation[edge] for edge in edges)
        if spend > budget:
            continue
        value = integer_objective_value(allocation, coefficients, sensitivities)
        if value < best_value:
            best_value = value
            best = allocation
    return best_value, best


def test_dynamic_program_matches_brute_force_small_instance():
    coefficients = {"a": 1.0, "b": 1.6, "c": 0.8}
    sensitivities = {"a": 1.0, "b": 0.9, "c": 1.5}
    costs = {"a": 2, "b": 3, "c": 5}
    budget = 26

    exact = exact_heterogeneous_integer_allocation(
        coefficients,
        sensitivities,
        costs,
        budget,
    )
    brute_value, _ = brute_force(coefficients, sensitivities, costs, budget)
    assert exact.objective_value == pytest.approx(brute_value)


def test_integer_allocation_respects_budget_and_positive_counts():
    result = exact_heterogeneous_integer_allocation(
        {"ab": 1.0, "bc": 2.0, "cd": 1.5},
        {"ab": 1.0, "bc": 1.0, "cd": 1.0},
        {"ab": 2, "bc": 4, "cd": 7},
        40,
    )
    assert result.total_spend <= 40
    assert result.unspent_budget == 40 - result.total_spend
    assert all(count >= 1 for count in result.allocations.values())


def test_continuous_p62_value_is_lower_bound():
    result = exact_heterogeneous_integer_allocation(
        {"a": 1.0, "b": 2.0, "c": 3.0},
        {"a": 1.0, "b": 1.0, "c": 0.5},
        {"a": 2, "b": 3, "c": 6},
        35,
    )
    assert result.objective_value + 1e-12 >= result.continuous_lower_bound
    assert result.additive_integrality_gap >= -1e-12
    assert result.multiplicative_integrality_gap >= 1.0 - 1e-12


def test_gcd_scaling_preserves_original_budget_accounting():
    result = exact_heterogeneous_integer_allocation(
        {"a": 1.0, "b": 1.0},
        {"a": 1.0, "b": 1.0},
        {"a": 6, "b": 10},
        49,
    )
    assert result.cost_gcd == 2
    assert result.scaled_budget == 24
    assert result.total_spend <= 49
    assert result.total_spend % 2 == 0


def test_unused_remainder_is_allowed_when_no_measurement_fits_it():
    result = exact_heterogeneous_integer_allocation(
        {"a": 1.0, "b": 1.0},
        {"a": 1.0, "b": 1.0},
        {"a": 4, "b": 6},
        11,
    )
    assert result.allocations == {"a": 1, "b": 1}
    assert result.total_spend == 10
    assert result.unspent_budget == 1


def test_equal_cost_case_matches_brute_force_and_p61_structure():
    coefficients = {"a": 1.0, "b": 3.0}
    sensitivities = {"a": 1.0, "b": 1.0}
    costs = {"a": 2, "b": 2}
    budget = 16
    result = exact_heterogeneous_integer_allocation(
        coefficients,
        sensitivities,
        costs,
        budget,
    )
    brute_value, _ = brute_force(coefficients, sensitivities, costs, budget)
    assert result.objective_value == pytest.approx(brute_value)
    assert sum(result.allocations.values()) == budget // 2


def test_infeasible_baseline_budget_rejected():
    with pytest.raises(ValueError, match="at least one measurement"):
        exact_heterogeneous_integer_allocation(
            {"a": 1.0, "b": 1.0},
            {"a": 1.0, "b": 1.0},
            {"a": 5, "b": 7},
            11,
        )


def test_noninteger_cost_rejected():
    with pytest.raises(ValueError, match="positive integers"):
        exact_heterogeneous_integer_allocation(
            {"a": 1.0},
            {"a": 1.0},
            {"a": 1.5},
            10,
        )
