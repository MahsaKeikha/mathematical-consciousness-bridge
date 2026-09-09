import pytest

from consciousness_bridge.temporal_causal_structure import identity_action
from consciousness_bridge.temporal_certification import (
    bounded_coordinate_radius,
    certified_nonzero_change,
    classify_step_against_threshold,
    distance_interval,
    maximum_step_interval,
    variation_interval,
    weighted_bounded_coordinate_radius,
)


def _state(value: float):
    return ((value,), (0.5 * value,), (0.25 * value,))


def _actions():
    return (identity_action(_state(0.0)),)


def test_distance_interval_contains_known_true_distance_under_valid_radii():
    estimated_left = _state(0.05)
    estimated_right = _state(0.55)

    lower, upper = distance_interval(
        estimated_left,
        estimated_right,
        left_radius=0.05,
        right_radius=0.05,
        actions=_actions(),
    )

    true_distance = 0.6
    assert lower <= true_distance <= upper
    assert lower == pytest.approx(0.4)
    assert upper == pytest.approx(0.6)


def test_nonzero_change_requires_estimated_separation_larger_than_total_radius():
    assert certified_nonzero_change(
        _state(0.0),
        _state(0.5),
        left_radius=0.1,
        right_radius=0.1,
        actions=_actions(),
    )
    assert not certified_nonzero_change(
        _state(0.0),
        _state(0.15),
        left_radius=0.1,
        right_radius=0.1,
        actions=_actions(),
    )


def test_variation_interval_uses_double_weight_on_internal_error_radii():
    path = (_state(0.0), _state(0.4), _state(1.0))
    radii = (0.05, 0.10, 0.05)

    lower, upper = variation_interval(path, radii, _actions())

    assert lower == pytest.approx(0.7)
    assert upper == pytest.approx(1.3)


def test_maximum_step_interval_uses_largest_adjacent_error_sum():
    path = (_state(0.0), _state(0.4), _state(1.0))
    radii = (0.05, 0.10, 0.20)

    lower, upper = maximum_step_interval(path, radii, _actions())

    assert lower == pytest.approx(0.3)
    assert upper == pytest.approx(0.9)


def test_threshold_classifier_exposes_above_below_and_unresolved_regions():
    assert classify_step_against_threshold(
        _state(0.0),
        _state(0.8),
        0.05,
        0.05,
        threshold=0.5,
        actions=_actions(),
    ) == "above"
    assert classify_step_against_threshold(
        _state(0.0),
        _state(0.2),
        0.05,
        0.05,
        threshold=0.5,
        actions=_actions(),
    ) == "below"
    assert classify_step_against_threshold(
        _state(0.0),
        _state(0.5),
        0.05,
        0.05,
        threshold=0.5,
        actions=_actions(),
    ) == "unresolved"


def test_bounded_coordinate_radius_matches_hoeffding_union_bound_formula():
    radius = bounded_coordinate_radius(
        sample_count=500,
        coordinate_count=12,
        time_count=5,
        alpha=0.05,
    )

    assert radius == pytest.approx(0.0882225822, rel=1e-8)


def test_weighted_bounded_coordinate_radius_scales_by_largest_weight():
    base = bounded_coordinate_radius(500, 12, 5, 0.05)
    weighted = weighted_bounded_coordinate_radius(
        500,
        12,
        5,
        0.05,
        weights=(1.0, 2.0, 0.5),
    )

    assert weighted == pytest.approx(2.0 * base)


def test_invalid_certification_inputs_are_rejected():
    with pytest.raises(ValueError):
        distance_interval(_state(0.0), _state(0.2), -0.1, 0.1, _actions())
    with pytest.raises(ValueError):
        bounded_coordinate_radius(0, 1, 1, 0.05)
    with pytest.raises(ValueError):
        bounded_coordinate_radius(10, 1, 1, 1.0)
    with pytest.raises(ValueError):
        variation_interval((_state(0.0),), (), _actions())
