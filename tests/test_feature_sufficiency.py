import pytest

from consciousness_bridge.feature_sufficiency import (
    feature_counterexamples,
    feature_is_bridge_complete,
    feature_is_bridge_sufficient,
    induced_bridge_from_feature,
)


def test_feature_sufficiency_constructs_unique_factor_map():
    feature = {
        "p1": "zA",
        "p2": "zA",
        "p3": "zB",
    }
    bridge = {
        "p1": "e1",
        "p2": "e1",
        "p3": "e2",
    }

    assert feature_is_bridge_sufficient(feature, bridge)
    assert induced_bridge_from_feature(feature, bridge) == {
        "zA": "e1",
        "zB": "e2",
    }
    assert feature_counterexamples(feature, bridge) == ()


def test_single_feature_matched_bridge_different_pair_refutes_sufficiency():
    feature = {
        "p1": "same_feature",
        "p2": "same_feature",
    }
    bridge = {
        "p1": "experience_A",
        "p2": "experience_B",
    }

    assert not feature_is_bridge_sufficient(feature, bridge)
    assert feature_counterexamples(feature, bridge) == (("p1", "p2"),)
    with pytest.raises(ValueError):
        induced_bridge_from_feature(feature, bridge)


def test_sufficient_feature_need_not_be_bridge_complete():
    feature = {
        "p1": "fine_1",
        "p2": "fine_2",
        "p3": "fine_3",
    }
    bridge = {
        "p1": "same_experience",
        "p2": "same_experience",
        "p3": "different_experience",
    }

    assert feature_is_bridge_sufficient(feature, bridge)
    assert not feature_is_bridge_complete(feature, bridge)


def test_complete_feature_matches_bridge_fibers_exactly():
    feature = {
        "p1": "zA",
        "p2": "zA",
        "p3": "zB",
        "p4": "zB",
    }
    bridge = {
        "p1": "eA",
        "p2": "eA",
        "p3": "eB",
        "p4": "eB",
    }

    assert feature_is_bridge_sufficient(feature, bridge)
    assert feature_is_bridge_complete(feature, bridge)


def test_feature_and_bridge_domains_must_match():
    with pytest.raises(ValueError):
        feature_is_bridge_sufficient({"p1": "z"}, {"p2": "e"})
