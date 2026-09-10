from math import sqrt

import pytest

from consciousness_bridge.dual_optimal_multiplier import (
    certified_dual_optimal_multiplier,
    evaluate_dual_with_supergradient,
)
from consciousness_bridge.exact_heterogeneous_integer_calibration import (
    exact_heterogeneous_integer_allocation,
)
from consciousness_bridge.global_integer_optimality_certificate import (
    marginal_reduction,
)
from consciousness_bridge.lagrangian_optimality_gap import lagrangian_dual_lower_bound


def test_supergradient_interval_matches_breakpoint_tie_spend():
    coefficients = {"a": 2.0}
    sensitivities = {"a": 1.0}
    costs = {"a": 3}
    count = 4
    lambda_value = marginal_reduction(2.0, count) / 3
    evaluation = evaluate_dual_with_supergradient(
        coefficients, sensitivities, costs, 20, lambda_value
    )
    assert set(evaluation.edge_minima["a"].minimizing_counts) == {4, 5}
    assert evaluation.minimum_spend == 12
    assert evaluation.maximum_spend == 15
    assert evaluation.supergradient_lower == -8
    assert evaluation.supergradient_upper == -5


def test_supergradient_sign_tracks_monotone_selected_spend():
    coefficients = {"a": 1.0, "b": 2.2, "c": 0.7}
    sensitivities = {"a": 1.0, "b": 0.9, "c": 1.4}
    costs = {"a": 1, "b": 3, "c": 2}
    budget = 30
    lambdas = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]
    evaluations = [
        evaluate_dual_with_supergradient(
            coefficients, sensitivities, costs, budget, value
        )
        for value in lambdas
    ]
    assert all(
        first.minimum_spend >= second.minimum_spend
        for first, second in zip(evaluations, evaluations[1:], strict=True)
    )
    assert all(
        first.maximum_spend >= second.maximum_spend
        for first, second in zip(evaluations, evaluations[1:], strict=True)
    )


def test_dual_values_are_concave_on_sampled_grid():
    coefficients = {"a": 1.0, "b": 2.5}
    sensitivities = {"a": 1.1, "b": 0.8}
    costs = {"a": 2, "b": 5}
    budget = 35
    left = 0.03
    right = 0.19
    midpoint = 0.5 * (left + right)
    q_left, _ = lagrangian_dual_lower_bound(
        coefficients, sensitivities, costs, budget, left
    )
    q_right, _ = lagrangian_dual_lower_bound(
        coefficients, sensitivities, costs, budget, right
    )
    q_mid, _ = lagrangian_dual_lower_bound(
        coefficients, sensitivities, costs, budget, midpoint
    )
    assert q_mid + 1e-12 >= 0.5 * (q_left + q_right)


def test_certified_search_bounds_dense_grid_dual_maximum():
    coefficients = {"a": 1.0, "b": 2.5, "c": 1.4}
    sensitivities = {"a": 1.0, "b": 0.8, "c": 1.3}
    costs = {"a": 2, "b": 5, "c": 3}
    budget = 47
    cert = certified_dual_optimal_multiplier(
        coefficients,
        sensitivities,
        costs,
        budget,
        dual_tolerance=1e-8,
    )
    grid = [10 ** (-4 + 6 * i / 4000) for i in range(4001)]
    grid_best = max(
        lagrangian_dual_lower_bound(
            coefficients, sensitivities, costs, budget, value
        )[0]
        for value in grid
    )
    assert cert.dual_lower_bound <= grid_best + 1e-6
    assert cert.dual_optimum_upper_bound + 1e-10 >= grid_best
    assert cert.dual_value_error_bound <= 1e-8 + 1e-12
    assert cert.dual_optimum_upper_bound - cert.dual_lower_bound == pytest.approx(
        cert.dual_value_error_bound,
        abs=1e-12,
    )


def test_strongest_evaluated_dual_bound_remains_below_exact_p63_optimum():
    coefficients = {"a": 1.0, "b": 3.0, "c": 1.2}
    sensitivities = {"a": 1.0, "b": 0.7, "c": 1.4}
    costs = {"a": 2, "b": 5, "c": 4}
    budget = 43
    exact = exact_heterogeneous_integer_allocation(
        coefficients, sensitivities, costs, budget
    )
    cert = certified_dual_optimal_multiplier(
        coefficients, sensitivities, costs, budget, dual_tolerance=1e-9
    )
    assert cert.dual_lower_bound <= exact.objective_value + 1e-10
    assert cert.dual_optimum_upper_bound + 1e-12 >= cert.dual_lower_bound


def test_zero_supergradient_interval_is_exact_dual_maximizer():
    coefficients = {"a": 1.0, "b": 1.0}
    sensitivities = {"a": 1.0, "b": 1.0}
    costs = {"a": 1, "b": 1}
    cert = certified_dual_optimal_multiplier(
        coefficients, sensitivities, costs, 6, dual_tolerance=1e-12
    )
    assert cert.exact_dual_maximizer
    assert cert.dual_value_error_bound == 0.0
    assert cert.evaluation.supergradient_lower <= 0 <= cert.evaluation.supergradient_upper
    assert cert.dual_lower_bound == pytest.approx(2 / sqrt(3), abs=1e-10)


def test_baseline_budget_case_is_exact_and_flagged():
    coefficients = {"a": 1.0, "b": 2.0}
    sensitivities = {"a": 1.5, "b": 0.5}
    costs = {"a": 3, "b": 4}
    cert = certified_dual_optimal_multiplier(
        coefficients, sensitivities, costs, 7, dual_tolerance=1e-12
    )
    expected = 1.0 * 1.5 + 2.0 * 0.5
    assert cert.baseline_budget_case
    assert cert.exact_dual_maximizer
    assert cert.dual_lower_bound == pytest.approx(expected)
    assert cert.dual_optimum_upper_bound == pytest.approx(expected)


def test_tighter_tolerance_never_weakens_reported_dual_lower_bound_materially():
    coefficients = {"a": 1.0, "b": 2.3}
    sensitivities = {"a": 1.2, "b": 0.9}
    costs = {"a": 2, "b": 5}
    budget = 31
    loose = certified_dual_optimal_multiplier(
        coefficients, sensitivities, costs, budget, dual_tolerance=1e-4
    )
    tight = certified_dual_optimal_multiplier(
        coefficients, sensitivities, costs, budget, dual_tolerance=1e-10
    )
    assert tight.dual_lower_bound + 1e-10 >= loose.dual_lower_bound
    assert tight.dual_value_error_bound <= loose.dual_value_error_bound + 1e-12


def test_invalid_search_inputs_are_rejected():
    with pytest.raises(ValueError, match="dual_tolerance"):
        certified_dual_optimal_multiplier(
            {"a": 1.0}, {"a": 1.0}, {"a": 1}, 2, dual_tolerance=0.0
        )
    with pytest.raises(TypeError, match="max_iterations"):
        certified_dual_optimal_multiplier(
            {"a": 1.0},
            {"a": 1.0},
            {"a": 1},
            2,
            max_iterations=2.5,  # type: ignore[arg-type]
        )
    with pytest.raises(ValueError, match="baseline"):
        certified_dual_optimal_multiplier(
            {"a": 1.0}, {"a": 1.0}, {"a": 3}, 2
        )
