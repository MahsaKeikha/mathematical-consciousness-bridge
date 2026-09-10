from math import ceil, log

import pytest

from consciousness_bridge.quantum_regular_bridge_sample_complexity import (
    categorical_target_tv_radius,
    coordinate_hoeffding_radius,
    empirical_lipschitz_obstruction_margin,
    population_margin_lower_bound,
    quantum_linear_inversion_trace_radius,
    regularity_gap_sample_sizes,
)


def test_coordinate_hoeffding_radius_matches_formula():
    radius = coordinate_hoeffding_radius(
        preparation_count=3,
        outcome_count=4,
        samples_per_preparation=200,
        alpha=0.05,
    )
    expected = (log(2 * 3 * 4 / 0.05) / (2 * 200)) ** 0.5
    assert radius == pytest.approx(expected)


def test_quantum_linear_inversion_radius_matches_declared_stability_bound():
    radius = quantum_linear_inversion_trace_radius(
        preparation_count=3,
        measurement_outcomes=4,
        samples_per_preparation=400,
        alpha_quantum=0.025,
        reconstruction_stability=1.5,
    )
    coordinate = coordinate_hoeffding_radius(
        preparation_count=3,
        outcome_count=4,
        samples_per_preparation=400,
        alpha=0.025,
    )
    assert radius == pytest.approx(1.5 * 4 * coordinate)


def test_target_tv_radius_matches_coordinate_union_bound_and_clips():
    radius = categorical_target_tv_radius(
        preparation_count=2,
        target_outcomes=3,
        samples_per_preparation=1000,
        alpha_target=0.025,
    )
    coordinate = coordinate_hoeffding_radius(
        preparation_count=2,
        outcome_count=3,
        samples_per_preparation=1000,
        alpha=0.025,
    )
    assert radius == pytest.approx(1.5 * coordinate)

    clipped = categorical_target_tv_radius(
        preparation_count=20,
        target_outcomes=20,
        samples_per_preparation=1,
        alpha_target=0.01,
    )
    assert clipped == 1.0


def test_empirical_margin_uses_two_quantum_and_two_target_radii():
    margin = empirical_lipschitz_obstruction_margin(
        estimated_quantum_pair_trace_norm_half=0.10,
        quantum_radius=0.03,
        estimated_target_tv=0.70,
        target_radius=0.04,
        lipschitz_constant=2.0,
    )
    assert margin == pytest.approx((0.70 - 0.08) - 2.0 * (0.10 + 0.06))


def test_empirical_quantum_envelope_is_clipped_at_one():
    margin = empirical_lipschitz_obstruction_margin(
        estimated_quantum_pair_trace_norm_half=1.4,
        quantum_radius=0.2,
        estimated_target_tv=0.9,
        target_radius=0.0,
        lipschitz_constant=0.5,
    )
    assert margin == pytest.approx(0.4)


def test_population_margin_exposes_factor_four_uncertainty_cost():
    bound = population_margin_lower_bound(
        population_regularity_gap=0.80,
        target_radius=0.05,
        quantum_radius=0.04,
        lipschitz_constant=1.5,
    )
    assert bound == pytest.approx(0.80 - 4 * 0.05 - 4 * 1.5 * 0.04)


def test_general_sample_complexity_matches_closed_form():
    result = regularity_gap_sample_sizes(
        preparation_count=4,
        measurement_outcomes=6,
        target_outcomes=3,
        population_regularity_gap=0.4,
        lipschitz_constant=1.25,
        reconstruction_stability=0.8,
        alpha_quantum=0.025,
        alpha_target=0.025,
        target_gap_fraction=0.3,
    )
    expected_target = ceil(
        2
        * 3**2
        * log(2 * 4 * 3 / 0.025)
        / (0.3**2 * 0.4**2)
    )
    expected_quantum = ceil(
        8
        * 1.25**2
        * 0.8**2
        * 6**2
        * log(2 * 4 * 6 / 0.025)
        / (0.7**2 * 0.4**2)
    )
    assert result.target_samples_per_preparation == expected_target
    assert result.quantum_samples_per_preparation == expected_quantum
    assert result.confidence_lower_bound == pytest.approx(0.95)


def test_balanced_allocation_reduces_to_stated_p42_corollary():
    result = regularity_gap_sample_sizes(
        preparation_count=5,
        measurement_outcomes=4,
        target_outcomes=2,
        population_regularity_gap=0.25,
        lipschitz_constant=1.5,
        reconstruction_stability=1.2,
        alpha_quantum=0.02,
        alpha_target=0.03,
    )
    expected_target = ceil(
        8 * 2**2 * log(2 * 5 * 2 / 0.03) / 0.25**2
    )
    expected_quantum = ceil(
        32
        * 1.5**2
        * 1.2**2
        * 4**2
        * log(2 * 5 * 4 / 0.02)
        / 0.25**2
    )
    assert result.target_samples_per_preparation == expected_target
    assert result.quantum_samples_per_preparation == expected_quantum
    assert result.target_gap_fraction == 0.5
    assert result.quantum_gap_fraction == 0.5


def test_sample_complexity_has_inverse_square_gap_scaling_before_ceiling():
    large_gap = regularity_gap_sample_sizes(
        preparation_count=3,
        measurement_outcomes=4,
        target_outcomes=2,
        population_regularity_gap=0.4,
        lipschitz_constant=1.0,
        reconstruction_stability=1.0,
        alpha_quantum=0.025,
        alpha_target=0.025,
    )
    small_gap = regularity_gap_sample_sizes(
        preparation_count=3,
        measurement_outcomes=4,
        target_outcomes=2,
        population_regularity_gap=0.2,
        lipschitz_constant=1.0,
        reconstruction_stability=1.0,
        alpha_quantum=0.025,
        alpha_target=0.025,
    )
    assert small_gap.target_samples_per_preparation >= 4 * large_gap.target_samples_per_preparation - 3
    assert small_gap.quantum_samples_per_preparation >= 4 * large_gap.quantum_samples_per_preparation - 3


def test_quantum_sample_complexity_scales_quadratically_with_reconstruction_conditioning():
    first = regularity_gap_sample_sizes(
        preparation_count=2,
        measurement_outcomes=4,
        target_outcomes=2,
        population_regularity_gap=0.4,
        lipschitz_constant=1.0,
        reconstruction_stability=1.0,
        alpha_quantum=0.025,
        alpha_target=0.025,
    )
    second = regularity_gap_sample_sizes(
        preparation_count=2,
        measurement_outcomes=4,
        target_outcomes=2,
        population_regularity_gap=0.4,
        lipschitz_constant=1.0,
        reconstruction_stability=2.0,
        alpha_quantum=0.025,
        alpha_target=0.025,
    )
    assert second.quantum_samples_per_preparation >= 4 * first.quantum_samples_per_preparation - 3


def test_zero_lipschitz_or_zero_reconstruction_stability_needs_no_quantum_precision_for_gap_budget():
    result = regularity_gap_sample_sizes(
        preparation_count=2,
        measurement_outcomes=4,
        target_outcomes=2,
        population_regularity_gap=0.3,
        lipschitz_constant=0.0,
        reconstruction_stability=1.0,
        alpha_quantum=0.05,
        alpha_target=0.05,
    )
    assert result.quantum_samples_per_preparation == 1


def test_invalid_arguments_are_rejected():
    with pytest.raises(ValueError):
        coordinate_hoeffding_radius(
            preparation_count=0,
            outcome_count=2,
            samples_per_preparation=10,
            alpha=0.05,
        )
    with pytest.raises(ValueError):
        regularity_gap_sample_sizes(
            preparation_count=2,
            measurement_outcomes=4,
            target_outcomes=2,
            population_regularity_gap=0.0,
            lipschitz_constant=1.0,
            reconstruction_stability=1.0,
            alpha_quantum=0.05,
            alpha_target=0.05,
        )
    with pytest.raises(ValueError):
        regularity_gap_sample_sizes(
            preparation_count=2,
            measurement_outcomes=4,
            target_outcomes=2,
            population_regularity_gap=0.3,
            lipschitz_constant=1.0,
            reconstruction_stability=1.0,
            alpha_quantum=0.05,
            alpha_target=0.05,
            target_gap_fraction=1.0,
        )
