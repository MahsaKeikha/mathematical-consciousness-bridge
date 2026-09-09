import pytest

from consciousness_bridge.robust_signature_recovery import (
    classify_same_signature,
    max_protocol_tv_distance,
    robust_threshold_interval,
    signature_spread_and_separation,
)


def _population_predictions():
    return {
        "p1": {
            "passive": {"yes": 0.80, "no": 0.20},
            "perturb": {"yes": 0.75, "no": 0.25},
        },
        "p2": {
            "passive": {"yes": 0.76, "no": 0.24},
            "perturb": {"yes": 0.72, "no": 0.28},
        },
        "p3": {
            "passive": {"yes": 0.25, "no": 0.75},
            "perturb": {"yes": 0.20, "no": 0.80},
        },
    }


def test_population_signature_gap_separates_classes():
    predictions = _population_predictions()
    feature = {"p1": "zA", "p2": "zA", "p3": "zB"}

    within, between = signature_spread_and_separation(predictions, feature)

    assert within == pytest.approx(0.04)
    assert between == pytest.approx(0.51)
    assert between - within == pytest.approx(0.47)


def test_pair_distance_is_maximum_over_protocols():
    predictions = _population_predictions()
    distance = max_protocol_tv_distance(predictions, "p1", "p3")
    assert distance == pytest.approx(0.55)


def test_robust_threshold_interval_requires_gap_larger_than_four_epsilon():
    lower, upper = robust_threshold_interval(
        within_spread=0.04,
        between_separation=0.51,
        epsilon=0.05,
    )

    assert lower == pytest.approx(0.14)
    assert upper == pytest.approx(0.41)

    with pytest.raises(ValueError):
        robust_threshold_interval(0.20, 0.35, 0.05)


def test_threshold_classifies_estimated_pairs_correctly_under_small_perturbation():
    estimated = {
        "p1": {
            "passive": {"yes": 0.78, "no": 0.22},
            "perturb": {"yes": 0.73, "no": 0.27},
        },
        "p2": {
            "passive": {"yes": 0.75, "no": 0.25},
            "perturb": {"yes": 0.70, "no": 0.30},
        },
        "p3": {
            "passive": {"yes": 0.27, "no": 0.73},
            "perturb": {"yes": 0.22, "no": 0.78},
        },
    }

    threshold = 0.25
    assert classify_same_signature(estimated, "p1", "p2", threshold)
    assert not classify_same_signature(estimated, "p1", "p3", threshold)
    assert not classify_same_signature(estimated, "p2", "p3", threshold)


def test_at_least_two_signature_classes_are_required():
    predictions = _population_predictions()
    feature = {"p1": "zA", "p2": "zA", "p3": "zA"}

    with pytest.raises(ValueError):
        signature_spread_and_separation(predictions, feature)
