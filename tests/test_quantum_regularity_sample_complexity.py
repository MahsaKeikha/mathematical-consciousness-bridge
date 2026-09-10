import pytest

from consciousness_bridge.quantum_regularity_sample_complexity import (
    optimal_continuous_allocation,
    population_regularity_gap,
    square_root_radius,
    sufficient_sample_complexity,
)


def test_population_regularity_gap_matches_p41_definition():
    assert population_regularity_gap(0.50, 0.10, 2.0) == pytest.approx(0.30)


def test_square_root_radius_decreases_with_sample_count():
    small = square_root_radius(100, 0.05, 1.0, 2.0)
    large = square_root_radius(400, 0.05, 1.0, 2.0)
    assert large == pytest.approx(small / 2.0)


def test_sufficient_sample_complexity_satisfies_allocated_budget():
    certificate = sufficient_sample_complexity(
        0.50,
        0.10,
        2.0,
        target_radius_constant=0.8,
        quantum_radius_constant=0.6,
        target_log_factor=4.0,
        quantum_log_factor=5.0,
        alpha_target=0.025,
        alpha_quantum=0.025,
        allocation_fraction_target=0.4,
    )
    assert certificate.population_regularity_gap == pytest.approx(0.30)
    assert certificate.certified_by_bound
    assert certificate.minimum_target_samples >= 1
    assert certificate.minimum_quantum_samples >= 1
    assert certificate.uncertainty_budget_at_minimum <= 0.30 + 1e-12


def test_sample_complexity_has_inverse_square_gap_scaling_before_ceiling():
    first = sufficient_sample_complexity(
        0.50,
        0.10,
        2.0,
        target_radius_constant=1.0,
        quantum_radius_constant=1.0,
        target_log_factor=2.0,
        quantum_log_factor=2.0,
        alpha_target=0.05,
        alpha_quantum=0.05,
    )
    second = sufficient_sample_complexity(
        0.80,
        0.10,
        2.0,
        target_radius_constant=1.0,
        quantum_radius_constant=1.0,
        target_log_factor=2.0,
        quantum_log_factor=2.0,
        alpha_target=0.05,
        alpha_quantum=0.05,
    )
    assert second.population_regularity_gap == pytest.approx(
        2.0 * first.population_regularity_gap
    )
    assert second.minimum_target_samples <= first.minimum_target_samples / 4.0 + 1.0
    assert second.minimum_quantum_samples <= first.minimum_quantum_samples / 4.0 + 1.0


def test_stricter_confidence_requires_no_fewer_samples():
    loose = sufficient_sample_complexity(
        0.55,
        0.10,
        2.0,
        target_radius_constant=0.7,
        quantum_radius_constant=0.5,
        target_log_factor=4.0,
        quantum_log_factor=4.0,
        alpha_target=0.10,
        alpha_quantum=0.10,
    )
    strict = sufficient_sample_complexity(
        0.55,
        0.10,
        2.0,
        target_radius_constant=0.7,
        quantum_radius_constant=0.5,
        target_log_factor=4.0,
        quantum_log_factor=4.0,
        alpha_target=0.01,
        alpha_quantum=0.01,
    )
    assert strict.minimum_target_samples >= loose.minimum_target_samples
    assert strict.minimum_quantum_samples >= loose.minimum_quantum_samples


def test_optimal_allocation_matches_cube_root_balance():
    allocation = optimal_continuous_allocation(
        lipschitz_constant=2.0,
        target_radius_constant=1.0,
        quantum_radius_constant=0.5,
        target_log_factor=2.0,
        quantum_log_factor=2.0,
        alpha_target=0.05,
        alpha_quantum=0.05,
        target_sample_cost=1.0,
        quantum_sample_cost=1.0,
    )
    assert allocation.allocation_fraction_target == pytest.approx(0.5)


def test_more_expensive_quantum_samples_shift_more_gap_to_quantum_uncertainty():
    baseline = optimal_continuous_allocation(
        lipschitz_constant=1.0,
        target_radius_constant=1.0,
        quantum_radius_constant=1.0,
        target_log_factor=2.0,
        quantum_log_factor=2.0,
        alpha_target=0.05,
        alpha_quantum=0.05,
    )
    expensive_quantum = optimal_continuous_allocation(
        lipschitz_constant=1.0,
        target_radius_constant=1.0,
        quantum_radius_constant=1.0,
        target_log_factor=2.0,
        quantum_log_factor=2.0,
        alpha_target=0.05,
        alpha_quantum=0.05,
        quantum_sample_cost=8.0,
    )
    assert expensive_quantum.allocation_fraction_target < baseline.allocation_fraction_target


def test_nonpositive_population_gap_is_rejected():
    with pytest.raises(ValueError):
        sufficient_sample_complexity(
            0.20,
            0.10,
            2.0,
            target_radius_constant=1.0,
            quantum_radius_constant=1.0,
            target_log_factor=2.0,
            quantum_log_factor=2.0,
            alpha_target=0.05,
            alpha_quantum=0.05,
        )


def test_invalid_radius_law_parameters_are_rejected():
    with pytest.raises(ValueError):
        square_root_radius(0, 0.05, 1.0, 2.0)
    with pytest.raises(ValueError):
        square_root_radius(10, 0.0, 1.0, 2.0)
    with pytest.raises(ValueError):
        square_root_radius(10, 0.05, -1.0, 2.0)
    with pytest.raises(ValueError):
        square_root_radius(10, 0.5, 1.0, 0.4)
