from math import isclose

import pytest

from consciousness_bridge.ic_povm_sample_complexity import (
    p42_sample_complexity_certificate,
    simultaneous_ic_povm_trace_radius,
    simultaneous_target_tv_radius,
    sufficient_quantum_sample_size,
    sufficient_target_sample_size,
)


def test_target_radius_shrinks_as_inverse_square_root():
    r1 = simultaneous_target_tv_radius(1000, 4, 3, 0.05)
    r4 = simultaneous_target_tv_radius(4000, 4, 3, 0.05)
    assert isclose(r4, 0.5 * r1, rel_tol=1e-12)


def test_quantum_radius_shrinks_as_inverse_square_root():
    r1 = simultaneous_ic_povm_trace_radius(2000, 3, 4, 1.5, 0.05)
    r4 = simultaneous_ic_povm_trace_radius(8000, 3, 4, 1.5, 0.05)
    assert isclose(r4, 0.5 * r1, rel_tol=1e-12)


def test_sample_sizes_certify_corrected_p41_population_budget():
    certificate = p42_sample_complexity_certificate(
        target_population_distance=0.55,
        quantum_population_distance=0.10,
        lipschitz_constant=1.5,
        preparation_count=3,
        target_outcome_count=2,
        povm_outcome_count=4,
        reconstruction_stability=1.2,
        alpha_target=0.025,
        alpha_quantum=0.025,
    )
    assert certificate.population_gap == pytest.approx(0.40)
    assert certificate.certified_by_bound
    assert certificate.uncertainty_budget <= certificate.population_gap


def test_balanced_target_formula_has_inverse_gap_squared_scaling():
    n = sufficient_target_sample_size(0.4, 3, 2, 0.05)
    n_half_gap = sufficient_target_sample_size(0.2, 3, 2, 0.05)
    assert n_half_gap >= 4 * n - 3


def test_quantum_formula_has_lipschitz_squared_scaling_up_to_ceiling():
    n = sufficient_quantum_sample_size(0.4, 1.0, 3, 4, 1.2, 0.05)
    n_double_l = sufficient_quantum_sample_size(0.4, 2.0, 3, 4, 1.2, 0.05)
    assert n_double_l >= 4 * n - 3


def test_zero_lipschitz_bridge_needs_no_quantum_precision_for_this_bound():
    n = sufficient_quantum_sample_size(0.3, 0.0, 3, 4, 2.0, 0.05)
    assert n == 1


def test_more_conservative_confidence_requires_more_samples():
    n_loose = sufficient_target_sample_size(0.3, 4, 3, 0.10)
    n_strict = sufficient_target_sample_size(0.3, 4, 3, 0.01)
    assert n_strict > n_loose


def test_larger_ic_reconstruction_instability_costs_quadratically():
    n1 = sufficient_quantum_sample_size(0.3, 1.0, 3, 4, 1.0, 0.05)
    n2 = sufficient_quantum_sample_size(0.3, 1.0, 3, 4, 2.0, 0.05)
    assert n2 >= 4 * n1 - 3


def test_nonpositive_population_gap_is_not_certifiable_by_p42():
    with pytest.raises(ValueError):
        p42_sample_complexity_certificate(
            target_population_distance=0.20,
            quantum_population_distance=0.20,
            lipschitz_constant=1.0,
            preparation_count=2,
            target_outcome_count=2,
            povm_outcome_count=4,
            reconstruction_stability=1.0,
            alpha_target=0.05,
            alpha_quantum=0.05,
        )


def test_invalid_parameters_are_rejected():
    with pytest.raises(ValueError):
        simultaneous_target_tv_radius(0, 2, 2, 0.05)
    with pytest.raises(ValueError):
        simultaneous_ic_povm_trace_radius(100, 2, 4, 0.0, 0.05)
    with pytest.raises(ValueError):
        sufficient_target_sample_size(0.3, 2, 2, 0.05, target_budget_fraction=1.0)
