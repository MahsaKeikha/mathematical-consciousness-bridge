from itertools import pairwise
from math import pi

import pytest

from consciousness_bridge.anytime_refinement_certification import (
    alpha_spending_level,
    alpha_spending_mass_through,
    anytime_base_tv_radius,
    certify_anytime_adaptive_selection_at_time,
    certify_anytime_adaptive_selection_path,
    first_time_selected_gain_is_certified_positive,
)
from consciousness_bridge.finite_sample_residual_certification import (
    hoeffding_joint_tv_radius,
)

OMEGA = (0, 1, 2, 3)
COARSE = {state: 0 for state in OMEGA}
GOOD = {0: 0, 1: 1, 2: 0, 3: 1}
PARTIAL = {0: 0, 1: 1, 2: 1, 3: 1}
BAD = {state: 0 for state in OMEGA}
CANDIDATES = {"good": GOOD, "partial": PARTIAL, "bad": BAD}
CANDIDATE_SIZES = {"good": 2, "partial": 2, "bad": 1}


def balanced_records(repetitions: int = 100) -> list[tuple[int, int]]:
    return [
        (omega, omega % 2)
        for _ in range(repetitions)
        for omega in OMEGA
    ]


def snapshot(records, alpha=0.05):
    return certify_anytime_adaptive_selection_at_time(
        records,
        omega_states=OMEGA,
        coarse_descriptor=COARSE,
        coarse_size=1,
        candidate_descriptors=CANDIDATES,
        candidate_sizes=CANDIDATE_SIZES,
        target_size=2,
        alpha=alpha,
    )


def path(records, inspection_times, alpha=0.05):
    return certify_anytime_adaptive_selection_path(
        records,
        inspection_times=inspection_times,
        omega_states=OMEGA,
        coarse_descriptor=COARSE,
        coarse_size=1,
        candidate_descriptors=CANDIDATES,
        candidate_sizes=CANDIDATE_SIZES,
        target_size=2,
        alpha=alpha,
    )


def test_alpha_spending_level_has_exact_declared_formula():
    alpha = 0.05
    for time_index in (1, 2, 7, 100):
        expected = 6.0 * alpha / (pi * pi * time_index * time_index)
        assert alpha_spending_level(time_index, alpha) == pytest.approx(expected)


def test_alpha_spending_sequence_sums_to_total_budget():
    alpha = 0.05
    spent = alpha_spending_mass_through(10_000, alpha)

    assert 0.0 < spent < alpha
    assert alpha - spent < 4e-6


def test_spending_levels_are_positive_and_strictly_decreasing():
    levels = [alpha_spending_level(index) for index in range(1, 20)]

    assert all(level > 0.0 for level in levels)
    assert all(left > right for left, right in pairwise(levels))


def test_anytime_radius_equals_fixed_time_radius_at_allocated_alpha():
    sample_size = 137
    alphabet_size = 8
    alpha = 0.05
    local_alpha = alpha_spending_level(sample_size, alpha)

    expected = hoeffding_joint_tv_radius(
        sample_size=sample_size,
        alphabet_size=alphabet_size,
        alpha=local_alpha,
    )
    assert anytime_base_tv_radius(sample_size, alphabet_size, alpha) == pytest.approx(
        expected
    )


def test_snapshot_uses_time_indexed_alpha_spending_level():
    records = balanced_records(250)
    result = snapshot(records)

    assert result.time_index == len(records)
    assert result.alpha_spending_level == pytest.approx(
        alpha_spending_level(len(records))
    )
    assert result.selection.alpha == pytest.approx(result.alpha_spending_level)
    assert result.base_tv_radius == pytest.approx(result.selection.base_tv_radius)


def test_path_exposes_declared_time_uniform_coverage():
    records = balanced_records(1_000)
    result = path(records, inspection_times=(100, 1_000, 4_000))

    assert result.time_uniform_coverage == pytest.approx(0.95)
    assert result.spending_mass_through_last_snapshot < result.alpha
    assert result.remaining_spending_mass > 0.0


def test_path_materializes_only_requested_times_but_spending_is_global():
    records = balanced_records(500)
    result = path(records, inspection_times=(100, 700, 2_000))

    assert tuple(item.time_index for item in result.snapshots) == (100, 700, 2_000)
    assert result.spending_mass_through_last_snapshot == pytest.approx(
        alpha_spending_mass_through(2_000)
    )


def test_large_balanced_sample_certifies_good_selected_gain():
    records = balanced_records(25_000)
    result = snapshot(records)

    assert result.selection.selected_name == "good"
    assert result.selection.selected_gain_certified_positive


def test_stopping_helper_returns_first_certified_positive_inspection():
    records = balanced_records(25_000)
    result = path(records, inspection_times=(40, 400, 4_000, 100_000))
    stopped = first_time_selected_gain_is_certified_positive(result)

    assert stopped is not None
    assert stopped.selection.selected_gain_certified_positive
    assert all(
        not earlier.selection.selected_gain_certified_positive
        for earlier in result.snapshots
        if earlier.time_index < stopped.time_index
    )


def test_stopping_helper_returns_none_without_positive_certificate():
    records = [(omega, 0) for _ in range(100) for omega in OMEGA]
    result = path(records, inspection_times=(40, 100, 400))

    assert first_time_selected_gain_is_certified_positive(result) is None


def test_inspection_times_must_be_strictly_increasing_and_available():
    records = balanced_records(100)

    with pytest.raises(ValueError, match="strictly increasing"):
        path(records, inspection_times=(100, 50))
    with pytest.raises(ValueError, match="strictly increasing"):
        path(records, inspection_times=(100, 100))
    with pytest.raises(ValueError, match="cannot exceed"):
        path(records, inspection_times=(500,))


def test_invalid_time_alpha_and_empty_inputs_are_rejected():
    with pytest.raises(TypeError, match="integer"):
        alpha_spending_level(1.5)
    with pytest.raises(ValueError, match="positive integer"):
        alpha_spending_level(0)
    with pytest.raises(ValueError, match="alpha"):
        alpha_spending_level(1, 0.0)
    with pytest.raises(ValueError, match="positive integer"):
        anytime_base_tv_radius(10, 0)
    with pytest.raises(ValueError, match="at least one sample"):
        snapshot([])
    with pytest.raises(ValueError, match="at least one time"):
        path(balanced_records(10), inspection_times=())
