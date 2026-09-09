import pytest

from consciousness_bridge.experimental_recovery import (
    bridge_decoder_from_recoverable_feature,
    feature_decoder_from_fingerprint,
    feature_is_recoverable_from_fingerprint,
    unresolved_feature_pairs,
)


def test_observable_fingerprint_can_contain_extra_detail_and_still_recover_feature():
    fingerprint = {
        "p1": "obs_1",
        "p2": "obs_2",
        "p3": "obs_3",
    }
    feature = {
        "p1": "zA",
        "p2": "zA",
        "p3": "zB",
    }

    assert feature_is_recoverable_from_fingerprint(fingerprint, feature)
    assert feature_decoder_from_fingerprint(fingerprint, feature) == {
        "obs_1": "zA",
        "obs_2": "zA",
        "obs_3": "zB",
    }


def test_signature_different_observational_collision_blocks_recovery():
    fingerprint = {
        "p1": "same_observation",
        "p2": "same_observation",
    }
    feature = {
        "p1": "zA",
        "p2": "zB",
    }

    assert not feature_is_recoverable_from_fingerprint(fingerprint, feature)
    assert unresolved_feature_pairs(fingerprint, feature) == (("p1", "p2"),)
    with pytest.raises(ValueError):
        feature_decoder_from_fingerprint(fingerprint, feature)


def test_recoverable_complete_feature_yields_bridge_decoder():
    fingerprint = {
        "p1": "obs_1",
        "p2": "obs_2",
        "p3": "obs_3",
    }
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

    decoder = bridge_decoder_from_recoverable_feature(fingerprint, feature, bridge)

    assert decoder == {
        "obs_1": "eA",
        "obs_2": "eA",
        "obs_3": "eB",
    }


def test_recoverable_feature_that_is_not_bridge_sufficient_cannot_decode_bridge():
    fingerprint = {
        "p1": "obs_1",
        "p2": "obs_2",
    }
    feature = {
        "p1": "same_feature",
        "p2": "same_feature",
    }
    bridge = {
        "p1": "eA",
        "p2": "eB",
    }

    with pytest.raises(ValueError):
        bridge_decoder_from_recoverable_feature(fingerprint, feature, bridge)
