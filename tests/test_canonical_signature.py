import pytest

from consciousness_bridge.canonical_signature import (
    canonical_bridge_signature,
    canonical_class_to_bridge_image,
    canonical_factor_is_bijective,
    sufficient_feature_to_canonical_signature,
)


def test_canonical_signature_matches_bridge_fibers_exactly():
    bridge = {
        "p1": "eA",
        "p2": "eA",
        "p3": "eB",
    }

    signature = canonical_bridge_signature(bridge)

    assert signature["p1"] == signature["p2"]
    assert signature["p1"] != signature["p3"]
    assert signature["p1"] == frozenset({"p1", "p2"})
    assert signature["p3"] == frozenset({"p3"})


def test_canonical_classes_are_bijective_with_realized_bridge_image():
    bridge = {
        "p1": "eA",
        "p2": "eA",
        "p3": "eB",
        "p4": "eC",
    }

    factor = canonical_class_to_bridge_image(bridge)

    assert set(factor.values()) == {"eA", "eB", "eC"}
    assert len(factor) == 3


def test_any_sufficient_feature_determines_canonical_signature():
    feature = {
        "p1": "fine_1",
        "p2": "fine_2",
        "p3": "fine_3",
    }
    bridge = {
        "p1": "eA",
        "p2": "eA",
        "p3": "eB",
    }

    factor = sufficient_feature_to_canonical_signature(feature, bridge)

    assert factor["fine_1"] == factor["fine_2"]
    assert factor["fine_1"] != factor["fine_3"]
    assert not canonical_factor_is_bijective(feature, bridge)


def test_complete_feature_is_isomorphic_to_canonical_signature():
    feature = {
        "p1": "zA",
        "p2": "zA",
        "p3": "zB",
    }
    bridge = {
        "p1": "eA",
        "p2": "eA",
        "p3": "eB",
    }

    assert canonical_factor_is_bijective(feature, bridge)


def test_nonsufficient_feature_has_no_canonical_factor_map():
    feature = {
        "p1": "same",
        "p2": "same",
    }
    bridge = {
        "p1": "eA",
        "p2": "eB",
    }

    assert not canonical_factor_is_bijective(feature, bridge)
    with pytest.raises(ValueError):
        sufficient_feature_to_canonical_signature(feature, bridge)
