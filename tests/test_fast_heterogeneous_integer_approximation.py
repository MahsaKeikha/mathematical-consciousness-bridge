import pytest

from consciousness_bridge.exact_heterogeneous_integer_calibration import (
    exact_heterogeneous_integer_allocation,
)
from consciousness_bridge.fast_heterogeneous_integer_approximation import (
    fast_floor_approximation,
    uniform_factor_from_minimum_continuous_count,
)


def test_floor_approximation_is_budget_feasible():
    result = fast_floor_approximation(
        {"a": 1.0, "b": 2.0, "c": 1.5},
        {"a": 1.0, "b": 1.0, "c": 0.8},
        {"a": 2.0, "b": 3.0, "c": 5.0},
        200.0,
    )
    assert result.total_spend <= 200.0 + 1e-12
    assert all(count >= 1 for count in result.integer_allocations.values())


def test_instance_certificate_bounds_floor_objective():
    result = fast_floor_approximation(
        {"a": 1.0, "b": 1.7, "c": 0.9},
        {"a": 1.0, "b": 1.2, "c": 1.5},
        {"a": 1.0, "b": 4.0, "c": 2.0},
        160.0,
    )
    assert result.objective_value <= result.certified_upper_bound + 1e-12
    assert result.certified_factor >= 1.0


def test_certificate_is_relative_to_exact_p63_optimum():
    coefficients = {"a": 1.0, "b": 2.0, "c": 1.3}
    sensitivities = {"a": 1.0, "b": 0.9, "c": 1.4}
    integer_costs = {"a": 2, "b": 3, "c": 5}
    budget = 90

    fast = fast_floor_approximation(
        coefficients,
        sensitivities,
        {edge: float(cost) for edge, cost in integer_costs.items()},
        float(budget),
    )
    exact = exact_heterogeneous_integer_allocation(
        coefficients,
        sensitivities,
        integer_costs,
        budget,
    )
    assert fast.objective_value <= fast.certified_factor * exact.objective_value + 1e-12


def test_uniform_factor_matches_closed_form():
    assert uniform_factor_from_minimum_continuous_count(4.0) == pytest.approx(
        (4.0 / 3.0) ** 0.5
    )


def test_uniform_factor_controls_instance_factor_when_all_counts_large():
    result = fast_floor_approximation(
        {"a": 1.0, "b": 1.0},
        {"a": 1.0, "b": 1.0},
        {"a": 1.0, "b": 1.0},
        40.0,
    )
    minimum_continuous = min(result.continuous_allocations.values())
    uniform = uniform_factor_from_minimum_continuous_count(minimum_continuous)
    assert result.certified_factor <= uniform + 1e-12


def test_large_budget_makes_factor_approach_one():
    small = fast_floor_approximation(
        {"a": 1.0, "b": 2.0},
        {"a": 1.0, "b": 1.0},
        {"a": 1.0, "b": 3.0},
        100.0,
    )
    large = fast_floor_approximation(
        {"a": 1.0, "b": 2.0},
        {"a": 1.0, "b": 1.0},
        {"a": 1.0, "b": 3.0},
        10000.0,
    )
    assert large.certified_factor <= small.certified_factor + 1e-12
    assert large.certified_factor < 1.01


def test_regime_failure_is_reported_instead_of_overclaiming():
    with pytest.raises(ValueError, match="at least one measurement"):
        fast_floor_approximation(
            {"important": 10.0, "tiny": 0.01},
            {"important": 1.0, "tiny": 1.0},
            {"important": 1.0, "tiny": 100.0},
            110.0,
        )


def test_uniform_factor_requires_strictly_more_than_one():
    with pytest.raises(ValueError):
        uniform_factor_from_minimum_continuous_count(1.0)
