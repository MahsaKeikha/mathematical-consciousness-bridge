import pytest

from consciousness_bridge.robust_experiment_design import (
    optimal_protocol_family,
    protocol_addition_effect,
    robust_signature_gap,
)


def _predictions():
    return {
        "p1": {
            "A": {"yes": 0.80, "no": 0.20},
            "B": {"yes": 0.75, "no": 0.25},
            "C": {"yes": 0.60, "no": 0.40},
        },
        "p2": {
            "A": {"yes": 0.75, "no": 0.25},
            "B": {"yes": 0.25, "no": 0.75},
            "C": {"yes": 0.58, "no": 0.42},
        },
        "p3": {
            "A": {"yes": 0.20, "no": 0.80},
            "B": {"yes": 0.17, "no": 0.83},
            "C": {"yes": 0.42, "no": 0.58},
        },
    }


def _feature():
    return {"p1": "zA", "p2": "zA", "p3": "zB"}


def test_adding_protocol_can_reduce_robust_signature_gap():
    predictions = _predictions()
    feature = _feature()

    gap_a = robust_signature_gap(predictions, feature, ("A",))
    gap_ab = robust_signature_gap(predictions, feature, ("A", "B"))

    assert gap_a == pytest.approx(0.50)
    assert gap_ab == pytest.approx(0.05)
    assert gap_ab < gap_a


def test_marginal_effect_equals_between_gain_minus_within_inflation():
    between_gain, within_inflation, gap_change = protocol_addition_effect(
        _predictions(),
        _feature(),
        current=("A",),
        added="B",
    )

    assert between_gain == pytest.approx(0.00)
    assert within_inflation == pytest.approx(0.45)
    assert gap_change == pytest.approx(-0.45)
    assert gap_change == pytest.approx(between_gain - within_inflation)


def test_exact_optimizer_prefers_best_robust_family_not_largest_family():
    family, gap = optimal_protocol_family(
        _predictions(),
        _feature(),
        max_protocol_count=3,
    )

    assert family == ("A",)
    assert gap == pytest.approx(0.50)


def test_low_signal_protocol_has_smaller_gap_than_best_protocol():
    predictions = _predictions()
    feature = _feature()

    gap_a = robust_signature_gap(predictions, feature, ("A",))
    gap_c = robust_signature_gap(predictions, feature, ("C",))

    assert gap_a > gap_c


def test_protocol_budget_must_be_positive():
    with pytest.raises(ValueError):
        optimal_protocol_family(_predictions(), _feature(), 0)
