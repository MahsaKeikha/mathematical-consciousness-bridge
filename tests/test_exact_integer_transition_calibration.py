from itertools import product

import pytest

from consciousness_bridge.exact_integer_transition_calibration import (
    allocation_exchange_condition,
    exact_integer_calibration_allocation,
    marginal_gain,
    marginal_gain_is_decreasing,
)
from consciousness_bridge.optimal_transition_calibration import objective_value


def brute_force_optimum(coefficients, sensitivities, budget):
    keys = tuple(coefficients)
    best_value = float("inf")
    best = None
    for counts in product(range(1, budget + 1), repeat=len(keys)):
        if sum(counts) != budget:
            continue
        allocation = dict(zip(keys, counts, strict=True))
        value = objective_value(
            {key: float(count) for key, count in allocation.items()},
            coefficients,
            sensitivities,
        )
        if value < best_value:
            best_value = value
            best = allocation
    return best_value, best


def test_marginal_gains_strictly_decrease():
    assert marginal_gain_is_decreasing(3.0, 1, 2)
    assert marginal_gain_is_decreasing(3.0, 2, 10)
    assert marginal_gain(3.0, 1) > marginal_gain(3.0, 2)


def test_exact_allocation_uses_entire_budget():
    result = exact_integer_calibration_allocation(
        {"a": 1.0, "b": 2.0, "c": 4.0},
        {"a": 1.0, "b": 1.0, "c": 1.0},
        20,
    )
    assert result.total_used == 20
    assert sum(result.allocations.values()) == 20
    assert result.exchange_condition_holds


def test_minimum_budget_assigns_one_to_every_edge():
    result = exact_integer_calibration_allocation(
        {"a": 1.0, "b": 2.0, "c": 3.0},
        {"a": 1.0, "b": 1.0, "c": 1.0},
        3,
    )
    assert result.allocations == {"a": 1, "b": 1, "c": 1}
    assert result.last_selected_gain is None
    assert result.exchange_condition_holds


def test_equal_edges_are_balanced_to_within_one_count():
    result = exact_integer_calibration_allocation(
        {"a": 1.0, "b": 1.0, "c": 1.0},
        {"a": 1.0, "b": 1.0, "c": 1.0},
        20,
    )
    values = tuple(result.allocations.values())
    assert max(values) - min(values) <= 1


@pytest.mark.parametrize("budget", [3, 4, 5, 6, 7, 8])
def test_greedy_matches_bruteforce_on_small_three_edge_instances(budget):
    coefficients = {"a": 1.0, "b": 1.7, "c": 2.6}
    sensitivities = {"a": 1.3, "b": 0.8, "c": 1.1}
    result = exact_integer_calibration_allocation(
        coefficients,
        sensitivities,
        budget,
    )
    brute_value, _ = brute_force_optimum(coefficients, sensitivities, budget)
    assert result.objective_value == pytest.approx(brute_value)


def test_exchange_condition_detects_nonoptimal_allocation():
    coefficients = {"a": 1.0, "b": 8.0}
    sensitivities = {"a": 1.0, "b": 1.0}
    bad = {"a": 4, "b": 1}
    good = exact_integer_calibration_allocation(
        coefficients,
        sensitivities,
        5,
    )
    assert not allocation_exchange_condition(bad, coefficients, sensitivities)
    assert allocation_exchange_condition(
        good.allocations,
        coefficients,
        sensitivities,
    )


def test_stronger_effective_edge_gets_at_least_as_many_units():
    result = exact_integer_calibration_allocation(
        {"small": 1.0, "large": 8.0},
        {"small": 1.0, "large": 1.0},
        20,
    )
    assert result.allocations["large"] >= result.allocations["small"]


def test_invalid_budget_and_counts_are_rejected():
    with pytest.raises(ValueError):
        exact_integer_calibration_allocation(
            {"a": 1.0, "b": 1.0},
            {"a": 1.0, "b": 1.0},
            1,
        )
    with pytest.raises(TypeError):
        marginal_gain(1.0, 1.5)
    with pytest.raises(ValueError):
        marginal_gain(1.0, 0)
