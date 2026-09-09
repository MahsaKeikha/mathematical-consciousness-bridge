import pytest

from consciousness_bridge.temporal_causal_structure import (
    apply_relabeling,
    endpoint_distance,
    identity_action,
    maximum_step_distance,
    path_variation,
    quotient_distance,
    weighted_component_distance,
)


def _base():
    return (
        (0.1, 0.8),
        (0.2, 0.7),
        (0.4,),
    )


def _swap_action():
    return (
        (1, 0),
        (1, 0),
        (0,),
    )


def _actions():
    return (
        identity_action(_base()),
        _swap_action(),
    )


def test_weighted_component_distance_is_symmetric_and_separating():
    left = _base()
    right = (
        (0.2, 0.8),
        (0.2, 0.5),
        (0.6,),
    )

    forward = weighted_component_distance(left, right, weights=(1.0, 2.0, 0.5))
    backward = weighted_component_distance(right, left, weights=(1.0, 2.0, 0.5))

    assert forward == pytest.approx(0.4)
    assert backward == pytest.approx(forward)
    assert weighted_component_distance(left, left) == pytest.approx(0.0)


def test_weighted_component_distance_satisfies_triangle_inequality():
    a = ((0.0,), (0.0,), (0.0,))
    b = ((0.2,), (0.4,), (0.1,))
    c = ((0.5,), (0.7,), (0.2,))

    assert weighted_component_distance(a, c) <= pytest.approx(
        weighted_component_distance(a, b) + weighted_component_distance(b, c)
    )


def test_quotient_distance_removes_pure_relabeling_jump():
    original = _base()
    relabeled = apply_relabeling(original, _swap_action())

    raw = weighted_component_distance(original, relabeled)
    quotient = quotient_distance(original, relabeled, _actions())

    assert raw > 0.0
    assert quotient == pytest.approx(0.0)


def test_temporal_path_variation_is_invariant_to_time_dependent_relabeling():
    first = _base()
    second = (
        (0.15, 0.75),
        (0.25, 0.65),
        (0.45,),
    )
    third = (
        (0.2, 0.7),
        (0.3, 0.6),
        (0.5,),
    )
    path = (first, second, third)
    relabeled_path = (
        apply_relabeling(first, _swap_action()),
        second,
        apply_relabeling(third, _swap_action()),
    )

    assert path_variation(path, _actions()) == pytest.approx(
        path_variation(relabeled_path, _actions())
    )
    assert maximum_step_distance(path, _actions()) == pytest.approx(
        maximum_step_distance(relabeled_path, _actions())
    )


def test_path_variation_bounds_endpoint_distance():
    path = (
        ((0.0,), (0.0,), (0.0,)),
        ((0.2,), (0.1,), (0.3,)),
        ((0.4,), (0.3,), (0.5,)),
    )
    actions = (identity_action(path[0]),)

    assert endpoint_distance(path, actions) <= path_variation(path, actions)


def test_equal_endpoints_can_hide_large_intermediate_excursion():
    quiet = ((0.0,), (0.0,), (0.0,))
    excursion = ((1.0,), (0.8,), (0.6,))
    path = (quiet, excursion, quiet)
    actions = (identity_action(quiet),)

    assert endpoint_distance(path, actions) == pytest.approx(0.0)
    assert path_variation(path, actions) == pytest.approx(2.0)
    assert maximum_step_distance(path, actions) == pytest.approx(1.0)


def test_invalid_weights_are_rejected():
    with pytest.raises(ValueError):
        weighted_component_distance(_base(), _base(), weights=(1.0, 0.0, 1.0))
