from math import isinf, sqrt

import pytest

from consciousness_bridge.exact_heterogeneous_integer_calibration import (
    exact_heterogeneous_integer_allocation,
)
from consciousness_bridge.global_integer_optimality_certificate import marginal_reduction
from consciousness_bridge.lagrangian_optimality_gap import (
    edge_lagrangian_minimum,
    lagrangian_dual_lower_bound,
    lagrangian_optimality_gap_certificate,
)


def _objective(allocation, coefficients, sensitivities):
    return sum(
        coefficients[edge] * sensitivities[edge] / sqrt(allocation[edge])
        for edge in allocation
    )


def test_edge_lagrangian_minimum_agrees_with_brute_force():
    for b, cost, lambda_value in [
        (1.0, 1, 0.2),
        (5.0, 3, 0.07),
        (0.8, 4, 1.2),
        (12.0, 2, 0.01),
    ]:
        result = edge_lagrangian_minimum(b, cost, lambda_value)
        brute = {
            count: b / sqrt(count) + lambda_value * cost * count
            for count in range(1, 250)
        }
        brute_value = min(brute.values())
        brute_counts = {
            count for count, value in brute.items() if value == pytest.approx(brute_value)
        }
        assert result.minimum_value == pytest.approx(brute_value)
        assert set(result.minimizing_counts) == brute_counts


def test_edge_lagrangian_minimum_retains_breakpoint_tie():
    b = 2.0
    cost = 3
    count = 4
    lambda_value = marginal_reduction(b, count) / cost
    result = edge_lagrangian_minimum(b, cost, lambda_value)
    assert set(result.minimizing_counts) == {count, count + 1}


def test_dual_lower_bound_never_exceeds_p63_exact_optimum():
    coefficients = {"a": 1.0, "b": 2.5, "c": 1.7}
    sensitivities = {"a": 1.0, "b": 0.8, "c": 1.2}
    costs = {"a": 2, "b": 3, "c": 4}
    budget = 29
    exact = exact_heterogeneous_integer_allocation(
        coefficients, sensitivities, costs, budget
    )
    for lambda_value in [0.01, 0.03, 0.08, 0.2, 0.7]:
        bound, minima = lagrangian_dual_lower_bound(
            coefficients, sensitivities, costs, budget, lambda_value
        )
        assert set(minima) == set(coefficients)
        assert bound <= exact.objective_value + 1e-10


def test_gap_certificate_upper_bounds_true_candidate_gap():
    coefficients = {"a": 1.0, "b": 3.0}
    sensitivities = {"a": 1.0, "b": 1.0}
    costs = {"a": 2, "b": 5}
    budget = 24
    candidate = {"a": 2, "b": 4}
    exact = exact_heterogeneous_integer_allocation(
        coefficients, sensitivities, costs, budget
    )
    cert = lagrangian_optimality_gap_certificate(
        candidate,
        coefficients,
        sensitivities,
        costs,
        budget,
        lambda_value=0.05,
    )
    true_gap = cert.candidate_objective - exact.objective_value
    assert true_gap >= -1e-10
    assert cert.additive_gap_upper_bound + 1e-10 >= true_gap
    assert cert.dual_lower_bound <= exact.objective_value + 1e-10
    assert cert.lambda_source == "user-supplied multiplier"


def test_p67_success_is_recovered_as_zero_p68_gap():
    coefficients = {"a": 1.0, "b": 1.0}
    sensitivities = {"a": 1.0, "b": 1.0}
    costs = {"a": 1, "b": 1}
    cert = lagrangian_optimality_gap_certificate(
        {"a": 3, "b": 3}, coefficients, sensitivities, costs, 6
    )
    assert cert.p67_certified_global_optimum
    assert cert.zero_gap_recovered_from_p67
    assert cert.additive_gap_upper_bound == pytest.approx(0.0, abs=1e-10)
    assert cert.relative_factor_upper_bound == pytest.approx(1.0, abs=1e-10)
    assert cert.lambda_source == "P67 common-multiplier witness"


def test_failed_p67_interval_still_gets_valid_quantitative_bound():
    coefficients = {"a": 1.0, "b": 1.0}
    sensitivities = {"a": 1.0, "b": 1.0}
    costs = {"a": 1, "b": 1}
    candidate = {"a": 1, "b": 5}
    exact = exact_heterogeneous_integer_allocation(
        coefficients, sensitivities, costs, 6
    )
    cert = lagrangian_optimality_gap_certificate(
        candidate, coefficients, sensitivities, costs, 6
    )
    assert not cert.p67_certified_global_optimum
    assert not cert.zero_gap_recovered_from_p67
    assert cert.dual_lower_bound <= exact.objective_value + 1e-10
    assert cert.additive_gap_upper_bound >= (
        _objective(candidate, coefficients, sensitivities) - exact.objective_value - 1e-10
    )
    assert cert.lambda_source == "P67 endpoint geometric mean"


def test_slack_candidate_gets_bound_without_false_zero_gap_claim():
    coefficients = {"a": 1.0, "b": 1.0}
    sensitivities = {"a": 1.0, "b": 1.0}
    costs = {"a": 2, "b": 3}
    cert = lagrangian_optimality_gap_certificate(
        {"a": 1, "b": 1}, coefficients, sensitivities, costs, 8
    )
    assert cert.budget_used == 5
    assert not cert.p67_certified_global_optimum
    assert cert.additive_gap_upper_bound > 0.0


def test_nonpositive_dual_bound_reports_infinite_relative_factor():
    cert = lagrangian_optimality_gap_certificate(
        {"a": 1},
        {"a": 1.0},
        {"a": 1.0},
        {"a": 1},
        100,
        lambda_value=10.0,
    )
    assert cert.dual_lower_bound < 0.0
    assert isinf(cert.relative_factor_upper_bound)


def test_invalid_inputs_are_rejected():
    with pytest.raises(ValueError):
        edge_lagrangian_minimum(1.0, 1, 0.0)
    with pytest.raises(TypeError):
        edge_lagrangian_minimum(1.0, 1.5, 0.1)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="baseline"):
        lagrangian_dual_lower_bound(
            {"a": 1.0}, {"a": 1.0}, {"a": 3}, 2, 0.1
        )
    with pytest.raises(ValueError, match="exceeds"):
        lagrangian_optimality_gap_certificate(
            {"a": 3}, {"a": 1.0}, {"a": 1.0}, {"a": 2}, 5
        )
