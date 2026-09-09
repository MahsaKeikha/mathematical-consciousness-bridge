import math

import pytest

from consciousness_bridge.fundamental_physical_sufficiency import (
    conditional_mutual_information,
    empirical_joint_from_records,
    factorization_collisions,
    factors_through_physical_descriptor,
    induced_bridge_map,
)


def test_exact_factorization_holds_when_target_is_constant_on_physical_fibers():
    physical = ["a", "a", "b", "b"]
    target = [0, 0, 1, 1]

    assert factors_through_physical_descriptor(physical, target)
    assert factorization_collisions(physical, target) == []
    assert induced_bridge_map(physical, target) == {"a": 0, "b": 1}


def test_exact_collision_rules_out_factorization():
    physical = ["same", "same"]
    target = ["e0", "e1"]

    assert not factors_through_physical_descriptor(physical, target)
    assert factorization_collisions(physical, target) == [(0, 1)]
    with pytest.raises(ValueError, match="does not factor"):
        induced_bridge_map(physical, target)


def test_factorization_inputs_require_equal_length():
    with pytest.raises(ValueError, match="equal length"):
        factorization_collisions([0], [0, 1])


def test_conditional_information_is_zero_for_markov_sufficiency():
    weights = {
        ("omega0", "t", "e0"): 1.0,
        ("omega0", "t", "e1"): 1.0,
        ("omega1", "t", "e0"): 1.0,
        ("omega1", "t", "e1"): 1.0,
    }

    assert conditional_mutual_information(weights) == pytest.approx(0.0, abs=1e-12)


def test_conditional_information_detects_residual_target_dependence():
    weights = {
        ("omega0", "t", "e0"): 1.0,
        ("omega1", "t", "e1"): 1.0,
    }

    assert conditional_mutual_information(weights) == pytest.approx(math.log(2.0))


def test_complete_physical_label_can_screen_off_fundamental_label():
    weights = {
        ("omega0", "t0", "e0"): 2.0,
        ("omega1", "t1", "e1"): 3.0,
    }

    assert conditional_mutual_information(weights) == pytest.approx(0.0, abs=1e-12)


def test_empirical_records_convert_to_joint_count_weights():
    records = [
        ("omega0", "t0", "e0"),
        ("omega0", "t0", "e0"),
        ("omega1", "t1", "e1"),
    ]

    assert empirical_joint_from_records(records) == {
        ("omega0", "t0", "e0"): 2.0,
        ("omega1", "t1", "e1"): 1.0,
    }


def test_probability_inputs_are_validated():
    with pytest.raises(ValueError, match="non-empty"):
        conditional_mutual_information({})
    with pytest.raises(ValueError, match="non-negative"):
        conditional_mutual_information({("o", "t", "e"): -1.0})
    with pytest.raises(ValueError, match="positive total"):
        conditional_mutual_information({("o", "t", "e"): 0.0})
    with pytest.raises(ValueError, match="non-empty"):
        empirical_joint_from_records([])
