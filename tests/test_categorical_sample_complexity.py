from math import isclose

import pytest

from consciousness_bridge.categorical_sample_complexity import (
    midpoint_signature_threshold,
    required_trials_for_signature_recovery,
    required_trials_for_uniform_tv,
    uniform_tv_failure_bound,
)


def test_uniform_tv_failure_bound_decreases_with_sample_count():
    small = uniform_tv_failure_bound(
        sample_count=100,
        physical_count=4,
        protocol_count=3,
        alphabet_size=2,
        epsilon=0.10,
    )
    large = uniform_tv_failure_bound(
        sample_count=1000,
        physical_count=4,
        protocol_count=3,
        alphabet_size=2,
        epsilon=0.10,
    )

    assert large < small


def test_required_uniform_trials_achieve_declared_bound():
    physical_count = 5
    protocol_count = 4
    alphabet_size = 3
    epsilon = 0.08
    alpha = 0.05

    n = required_trials_for_uniform_tv(
        physical_count,
        protocol_count,
        alphabet_size,
        epsilon,
        alpha,
    )

    failure = uniform_tv_failure_bound(
        n,
        physical_count,
        protocol_count,
        alphabet_size,
        epsilon,
    )

    assert failure <= alpha


def test_signature_recovery_formula_matches_epsilon_gap_over_eight():
    physical_count = 6
    protocol_count = 3
    alphabet_size = 2
    gap = 0.40
    alpha = 0.05

    direct = required_trials_for_signature_recovery(
        physical_count,
        protocol_count,
        alphabet_size,
        gap,
        alpha,
    )
    via_uniform = required_trials_for_uniform_tv(
        physical_count,
        protocol_count,
        alphabet_size,
        gap / 8.0,
        alpha,
    )

    assert direct == via_uniform


def test_midpoint_threshold_is_center_of_population_gap():
    threshold = midpoint_signature_threshold(0.12, 0.52)
    assert isclose(threshold, 0.32)


def test_invalid_design_parameters_are_rejected():
    with pytest.raises(ValueError):
        required_trials_for_signature_recovery(0, 1, 2, 0.4, 0.05)
    with pytest.raises(ValueError):
        required_trials_for_signature_recovery(1, 1, 1, 0.4, 0.05)
    with pytest.raises(ValueError):
        required_trials_for_signature_recovery(1, 1, 2, 0.0, 0.05)
    with pytest.raises(ValueError):
        required_trials_for_signature_recovery(1, 1, 2, 0.4, 1.0)
