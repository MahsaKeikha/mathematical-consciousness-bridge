from math import exp

import pytest

from consciousness_bridge.identifiability import (
    experiment_class_discriminability,
    optimal_equal_prior_error,
    repeated_event_error_bound,
    total_variation_discrete,
)


def test_total_variation_discrete_matches_half_l1_distance():
    first = {"yes": 0.8, "no": 0.2}
    second = {"yes": 0.5, "no": 0.5}

    assert total_variation_discrete(first, second) == pytest.approx(0.3)


def test_identical_theories_are_nonidentifiable_on_protocol_class():
    first = {
        "passive": {"a": 0.6, "b": 0.4},
        "intervention": {"a": 0.2, "b": 0.8},
    }
    second = {
        "passive": {"a": 0.6, "b": 0.4},
        "intervention": {"a": 0.2, "b": 0.8},
    }

    delta = experiment_class_discriminability(first, second)
    assert delta == pytest.approx(0.0)
    assert optimal_equal_prior_error(delta) == pytest.approx(0.5)


def test_richer_intervention_class_can_make_theories_identifiable():
    first = {
        "passive": {"a": 0.5, "b": 0.5},
        "perturb_recurrence": {"a": 0.9, "b": 0.1},
    }
    second = {
        "passive": {"a": 0.5, "b": 0.5},
        "perturb_recurrence": {"a": 0.4, "b": 0.6},
    }

    delta = experiment_class_discriminability(first, second)
    assert delta == pytest.approx(0.5)
    assert optimal_equal_prior_error(delta) == pytest.approx(0.25)


def test_repeated_experiment_error_bound_decays_exponentially():
    eta = 0.2
    assert repeated_event_error_bound(100, eta) == pytest.approx(exp(-2.0))
    assert repeated_event_error_bound(200, eta) < repeated_event_error_bound(100, eta)


def test_invalid_probability_distribution_is_rejected():
    with pytest.raises(ValueError):
        total_variation_discrete({"a": 0.8}, {"a": 1.0})
