from math import inf

import pytest

from consciousness_bridge.exact_heterogeneous_integer_calibration import (
    exact_heterogeneous_integer_allocation,
)
from consciousness_bridge.global_integer_optimality_certificate import (
    global_integer_optimality_certificate,
    marginal_reduction,
)
from consciousness_bridge.residual_exact_calibration_augmentation import (
    residual_exact_augmentation,
)


def test_marginal_reduction_is_positive_and_decreasing():
    values = [marginal_reduction(2.0, count) for count in range(1, 8)]
    assert all(value > 0.0 for value in values)
    assert all(left > right for left, right in zip(values, values[1:], strict=True))


def test_balanced_tight_allocation_is_globally_certified():
    result = global_integer_optimality_certificate(
        {"a": 3, "b": 3},
        {"a": 1.0, "b": 1.0},
        {"a": 1.0, "b": 1.0},
        {"a": 1, "b": 1},
        6,
    )
    assert result.certified_global_optimum
    assert result.budget_tight
    assert result.witness_lambda is not None
    assert result.lambda_lower <= result.witness_lambda <= result.lambda_upper


def test_certified_candidate_matches_p63_exact_objective():
    coefficients = {"a": 1.0, "b": 1.0}
    sensitivities = {"a": 1.0, "b": 1.0}
    costs = {"a": 1, "b": 1}
    candidate = {"a": 3, "b": 3}
    cert = global_integer_optimality_certificate(
        candidate, coefficients, sensitivities, costs, 6
    )
    exact = exact_heterogeneous_integer_allocation(
        coefficients, sensitivities, costs, 6
    )
    assert cert.certified_global_optimum
    assert cert.objective_value == pytest.approx(exact.objective_value)


def test_p66_solution_can_receive_unrestricted_global_certificate():
    coefficients = {"a": 1.0, "b": 1.0}
    sensitivities = {"a": 1.0, "b": 1.0}
    costs = {"a": 1, "b": 1}
    p66 = residual_exact_augmentation(
        coefficients, sensitivities, costs, 6
    )
    cert = global_integer_optimality_certificate(
        p66.allocations, coefficients, sensitivities, costs, 6
    )
    assert cert.certified_global_optimum


def test_slack_budget_is_not_certified_but_not_called_suboptimal():
    result = global_integer_optimality_certificate(
        {"a": 2, "b": 2},
        {"a": 1.0, "b": 1.0},
        {"a": 1.0, "b": 1.0},
        {"a": 2, "b": 3},
        12,
    )
    assert not result.certified_global_optimum
    assert not result.budget_tight
    assert result.witness_lambda is None
    assert "failure is inconclusive" in result.reason


def test_nonoverlapping_multiplier_intervals_are_not_certified():
    result = global_integer_optimality_certificate(
        {"a": 1, "b": 5},
        {"a": 1.0, "b": 1.0},
        {"a": 1.0, "b": 1.0},
        {"a": 1, "b": 1},
        6,
    )
    assert result.budget_tight
    assert not result.certified_global_optimum
    assert result.lambda_lower > result.lambda_upper
    assert result.witness_lambda is None


def test_count_one_has_one_sided_infinite_upper_interval():
    result = global_integer_optimality_certificate(
        {"a": 1},
        {"a": 2.0},
        {"a": 1.0},
        {"a": 3},
        3,
    )
    assert result.certified_global_optimum
    assert result.edge_intervals["a"][1] == inf
    assert result.witness_lambda == pytest.approx(result.lambda_lower)


def test_infeasible_candidate_is_rejected():
    with pytest.raises(ValueError, match="exceeds"):
        global_integer_optimality_certificate(
            {"a": 3}, {"a": 1.0}, {"a": 1.0}, {"a": 2}, 5
        )


def test_invalid_types_and_keys_are_rejected():
    with pytest.raises(TypeError):
        global_integer_optimality_certificate(
            {"a": 1}, {"a": 1.0}, {"a": 1.0}, {"a": 1}, 2.0  # type: ignore[arg-type]
        )
    with pytest.raises(ValueError, match="share keys"):
        global_integer_optimality_certificate(
            {"a": 1}, {"b": 1.0}, {"a": 1.0}, {"a": 1}, 1
        )
