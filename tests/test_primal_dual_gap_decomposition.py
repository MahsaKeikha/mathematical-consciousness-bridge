from math import sqrt

import pytest

from consciousness_bridge.exact_heterogeneous_integer_calibration import (
    exact_heterogeneous_integer_allocation,
)
from consciousness_bridge.global_integer_optimality_certificate import (
    global_integer_optimality_certificate,
)
from consciousness_bridge.primal_dual_gap_decomposition import (
    primal_dual_gap_decomposition,
    ranked_edge_regrets,
    strongest_dual_gap_diagnostic,
)


def test_exact_gap_identity_with_budget_slack():
    coefficients = {"a": 1.0, "b": 2.0}
    sensitivities = {"a": 1.0, "b": 0.8}
    costs = {"a": 2, "b": 3}
    candidate = {"a": 2, "b": 2}
    budget = 13
    lambda_value = 0.1

    result = primal_dual_gap_decomposition(
        candidate,
        coefficients,
        sensitivities,
        costs,
        budget,
        lambda_value,
    )

    assert result.budget_used == 10
    assert result.budget_slack == 3
    assert result.slack_penalty == pytest.approx(0.3)
    assert result.edge_regret_sum >= 0.0
    assert result.certificate_gap == pytest.approx(result.reconstructed_gap, abs=1e-12)
    assert result.reconstructed_gap == pytest.approx(
        result.edge_regret_sum + result.slack_penalty,
        abs=1e-12,
    )
    assert not result.zero_decomposition


def test_tight_budget_mismatch_is_entirely_edgewise():
    coefficients = {"a": 1.0, "b": 1.0}
    sensitivities = {"a": 1.0, "b": 1.0}
    costs = {"a": 1, "b": 1}
    candidate = {"a": 1, "b": 5}

    result = primal_dual_gap_decomposition(
        candidate,
        coefficients,
        sensitivities,
        costs,
        6,
        0.1,
    )

    assert result.budget_slack == 0
    assert result.slack_penalty == 0.0
    assert result.certificate_gap == pytest.approx(result.edge_regret_sum, abs=1e-12)
    assert result.edge_regret_sum > 0.0


def test_p67_common_multiplier_is_exact_zero_decomposition():
    coefficients = {"a": 1.0, "b": 1.0}
    sensitivities = {"a": 1.0, "b": 1.0}
    costs = {"a": 1, "b": 1}
    candidate = {"a": 3, "b": 3}
    p67 = global_integer_optimality_certificate(
        candidate, coefficients, sensitivities, costs, 6
    )
    assert p67.certified_global_optimum
    assert p67.witness_lambda is not None

    result = primal_dual_gap_decomposition(
        candidate,
        coefficients,
        sensitivities,
        costs,
        6,
        p67.witness_lambda,
    )

    assert result.zero_decomposition
    assert result.p67_certified_global_optimum
    assert result.budget_slack == 0
    assert result.edge_regret_sum == pytest.approx(0.0, abs=1e-12)
    assert result.certificate_gap == pytest.approx(0.0, abs=1e-10)
    assert all(item.regret == pytest.approx(0.0, abs=1e-12) for item in result.edge_regrets.values())


def test_zero_decomposition_requires_tight_budget_and_edgewise_minima():
    coefficients = {"a": 1.0, "b": 1.0}
    sensitivities = {"a": 1.0, "b": 1.0}
    costs = {"a": 1, "b": 1}

    slack = primal_dual_gap_decomposition(
        {"a": 2, "b": 2}, coefficients, sensitivities, costs, 5, 0.08
    )
    assert not slack.zero_decomposition
    assert slack.slack_penalty > 0.0

    mismatched = primal_dual_gap_decomposition(
        {"a": 1, "b": 4}, coefficients, sensitivities, costs, 5, 0.08
    )
    assert not mismatched.zero_decomposition
    assert mismatched.edge_regret_sum > 0.0


def test_strongest_dual_diagnostic_contains_best_candidate_to_dual_gap():
    coefficients = {"a": 1.0, "b": 2.7, "c": 1.3}
    sensitivities = {"a": 1.0, "b": 0.8, "c": 1.2}
    costs = {"a": 2, "b": 5, "c": 3}
    budget = 41
    candidate = {"a": 4, "b": 4, "c": 4}

    diagnostic = strongest_dual_gap_diagnostic(
        candidate,
        coefficients,
        sensitivities,
        costs,
        budget,
        dual_tolerance=1e-9,
    )

    candidate_objective = sum(
        coefficients[e] * sensitivities[e] / sqrt(candidate[e]) for e in candidate
    )
    assert diagnostic.decomposition.candidate_objective == pytest.approx(candidate_objective)
    assert diagnostic.strongest_dual_gap_lower_bound <= (
        diagnostic.strongest_dual_gap_upper_bound + 1e-12
    )
    assert diagnostic.strongest_dual_gap_upper_bound == pytest.approx(
        diagnostic.decomposition.certificate_gap,
        abs=1e-10,
    )
    assert (
        diagnostic.strongest_dual_gap_upper_bound
        - diagnostic.strongest_dual_gap_lower_bound
        <= 1e-9 + 1e-10
    )


def test_true_p63_candidate_gap_is_bounded_by_p70_upper_diagnostic():
    coefficients = {"a": 1.0, "b": 2.7, "c": 1.3}
    sensitivities = {"a": 1.0, "b": 0.8, "c": 1.2}
    costs = {"a": 2, "b": 5, "c": 3}
    budget = 41
    candidate = {"a": 4, "b": 4, "c": 4}

    diagnostic = strongest_dual_gap_diagnostic(
        candidate,
        coefficients,
        sensitivities,
        costs,
        budget,
        dual_tolerance=1e-9,
    )
    exact = exact_heterogeneous_integer_allocation(
        coefficients, sensitivities, costs, budget
    )
    true_primal_gap = diagnostic.decomposition.candidate_objective - exact.objective_value
    assert true_primal_gap >= -1e-10
    assert true_primal_gap <= diagnostic.strongest_dual_gap_upper_bound + 1e-10


def test_ranked_edge_regrets_are_nonincreasing_and_complete():
    result = primal_dual_gap_decomposition(
        {"a": 1, "b": 3, "c": 7},
        {"a": 1.0, "b": 2.0, "c": 1.5},
        {"a": 1.0, "b": 1.0, "c": 1.0},
        {"a": 1, "b": 1, "c": 1},
        11,
        0.07,
    )
    ranked = ranked_edge_regrets(result)
    assert {edge for edge, _ in ranked} == {"a", "b", "c"}
    regrets = [item.regret for _, item in ranked]
    assert regrets == sorted(regrets, reverse=True)


def test_candidate_objective_matches_direct_formula():
    result = primal_dual_gap_decomposition(
        {"a": 2, "b": 5},
        {"a": 1.5, "b": 3.0},
        {"a": 0.8, "b": 1.2},
        {"a": 2, "b": 3},
        20,
        0.05,
    )
    expected = 1.5 * 0.8 / sqrt(2) + 3.0 * 1.2 / sqrt(5)
    assert result.candidate_objective == pytest.approx(expected)


def test_invalid_inputs_are_rejected():
    with pytest.raises(ValueError, match="lambda_value"):
        primal_dual_gap_decomposition(
            {"a": 1}, {"a": 1.0}, {"a": 1.0}, {"a": 1}, 1, 0.0
        )
    with pytest.raises(ValueError, match="share keys"):
        primal_dual_gap_decomposition(
            {"a": 1}, {"b": 1.0}, {"a": 1.0}, {"a": 1}, 1, 0.1
        )
    with pytest.raises(ValueError, match="exceeds"):
        primal_dual_gap_decomposition(
            {"a": 3}, {"a": 1.0}, {"a": 1.0}, {"a": 2}, 5, 0.1
        )
