from math import isclose

import pytest

from consciousness_bridge.optimal_quantum_target_allocation import (
    continuous_weighted_cost,
    minimum_continuous_weighted_cost,
    optimal_gap_fraction,
    optimal_quantum_target_allocation,
    p42_quantum_coefficient,
    p42_target_coefficient,
)


def test_optimal_gap_fraction_is_half_for_equal_weighted_coefficients():
    lam = optimal_gap_fraction(
        target_coefficient=7.0,
        quantum_coefficient=7.0,
    )
    assert lam == pytest.approx(0.5)


def test_optimal_gap_fraction_follows_cube_root_rule():
    lam = optimal_gap_fraction(
        target_coefficient=8.0,
        quantum_coefficient=1.0,
    )
    assert lam == pytest.approx(2.0 / 3.0)


def test_sample_costs_enter_the_same_cube_root_rule():
    lam = optimal_gap_fraction(
        target_coefficient=1.0,
        quantum_coefficient=1.0,
        target_sample_cost=8.0,
        quantum_sample_cost=1.0,
    )
    assert lam == pytest.approx(2.0 / 3.0)


def test_closed_form_minimum_matches_cost_at_optimizer():
    a_y = 13.0
    a_q = 41.0
    c_y = 2.5
    c_q = 0.7
    lam = optimal_gap_fraction(
        target_coefficient=a_y,
        quantum_coefficient=a_q,
        target_sample_cost=c_y,
        quantum_sample_cost=c_q,
    )
    direct = continuous_weighted_cost(
        target_coefficient=a_y,
        quantum_coefficient=a_q,
        target_gap_fraction=lam,
        target_sample_cost=c_y,
        quantum_sample_cost=c_q,
    )
    closed = minimum_continuous_weighted_cost(
        target_coefficient=a_y,
        quantum_coefficient=a_q,
        target_sample_cost=c_y,
        quantum_sample_cost=c_q,
    )
    assert direct == pytest.approx(closed)


def test_optimizer_beats_nearby_allocations():
    a_y = 5.0
    a_q = 20.0
    lam = optimal_gap_fraction(
        target_coefficient=a_y,
        quantum_coefficient=a_q,
    )
    optimum = continuous_weighted_cost(
        target_coefficient=a_y,
        quantum_coefficient=a_q,
        target_gap_fraction=lam,
    )
    for candidate in (lam - 0.1, lam - 0.03, lam + 0.03, lam + 0.1):
        if 0.0 < candidate < 1.0:
            cost = continuous_weighted_cost(
                target_coefficient=a_y,
                quantum_coefficient=a_q,
                target_gap_fraction=candidate,
            )
            assert optimum < cost


def test_p42_coefficients_match_their_sample_size_factors():
    target = p42_target_coefficient(
        preparation_count=4,
        target_outcomes=3,
        population_regularity_gap=0.4,
        alpha_target=0.025,
    )
    quantum = p42_quantum_coefficient(
        preparation_count=4,
        measurement_outcomes=6,
        population_regularity_gap=0.4,
        lipschitz_constant=1.25,
        reconstruction_stability=0.8,
        alpha_quantum=0.025,
    )
    assert target > 0.0
    assert quantum > 0.0
    assert isclose(target / 0.5**2, 4.0 * target)
    assert isclose(quantum / (1.0 - 0.5) ** 2, 4.0 * quantum)


def test_integer_rounding_cost_is_within_stated_overhead():
    result = optimal_quantum_target_allocation(
        preparation_count=5,
        measurement_outcomes=4,
        target_outcomes=2,
        population_regularity_gap=0.3,
        lipschitz_constant=1.1,
        reconstruction_stability=0.9,
        alpha_quantum=0.025,
        alpha_target=0.025,
        target_sample_cost=3.0,
        quantum_sample_cost=7.0,
    )
    assert result.integer_weighted_cost >= result.continuous_weighted_cost
    assert (
        result.integer_weighted_cost - result.continuous_weighted_cost
        <= result.integer_rounding_overhead_bound + 1e-12
    )
    assert result.integer_rounding_overhead_bound == pytest.approx(10.0)


def test_balanced_allocation_is_optimal_only_when_weighted_coefficients_match():
    equal = optimal_quantum_target_allocation(
        preparation_count=2,
        measurement_outcomes=1,
        target_outcomes=2,
        population_regularity_gap=0.5,
        lipschitz_constant=1.0,
        reconstruction_stability=1.0,
        alpha_quantum=0.05,
        alpha_target=0.05,
        quantum_sample_cost=0.125,
    )
    assert 1.0 <= equal.balanced_to_optimal_continuous_cost_ratio <= 4.0


def test_balanced_allocation_is_never_more_than_factor_four_from_continuous_optimum():
    for target_coefficient, quantum_coefficient in (
        (1.0, 1.0),
        (1.0, 1000.0),
        (1000.0, 1.0),
        (3.0, 17.0),
    ):
        optimum = minimum_continuous_weighted_cost(
            target_coefficient=target_coefficient,
            quantum_coefficient=quantum_coefficient,
        )
        balanced = continuous_weighted_cost(
            target_coefficient=target_coefficient,
            quantum_coefficient=quantum_coefficient,
            target_gap_fraction=0.5,
        )
        ratio = balanced / optimum
        assert 1.0 <= ratio <= 4.0


def test_larger_target_cost_moves_more_gap_budget_to_target_side():
    baseline = optimal_gap_fraction(
        target_coefficient=4.0,
        quantum_coefficient=9.0,
        target_sample_cost=1.0,
        quantum_sample_cost=1.0,
    )
    expensive_target = optimal_gap_fraction(
        target_coefficient=4.0,
        quantum_coefficient=9.0,
        target_sample_cost=8.0,
        quantum_sample_cost=1.0,
    )
    assert expensive_target > baseline


def test_invalid_parameters_are_rejected():
    with pytest.raises(ValueError):
        optimal_gap_fraction(target_coefficient=0.0, quantum_coefficient=1.0)
    with pytest.raises(ValueError):
        continuous_weighted_cost(
            target_coefficient=1.0,
            quantum_coefficient=1.0,
            target_gap_fraction=1.0,
        )
    with pytest.raises(ValueError):
        p42_quantum_coefficient(
            preparation_count=2,
            measurement_outcomes=4,
            population_regularity_gap=0.3,
            lipschitz_constant=0.0,
            reconstruction_stability=1.0,
            alpha_quantum=0.05,
        )
