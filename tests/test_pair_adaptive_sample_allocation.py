import math

import pytest

from consciousness_bridge.pair_adaptive_sample_allocation import (
    bonferroni_spending,
    family_confidence_lower_bound,
    select_maximum_lower_margin,
    weighted_alpha_spending,
)


def test_weighted_alpha_spending_uses_complete_budget():
    spending = weighted_alpha_spending({"a": 1.0, "b": 3.0}, 0.08)
    assert spending["a"] == pytest.approx(0.02)
    assert spending["b"] == pytest.approx(0.06)
    assert sum(spending.values()) == pytest.approx(0.08)


def test_weighted_alpha_spending_rejects_nonpositive_weights():
    with pytest.raises(ValueError):
        weighted_alpha_spending({"a": 1.0, "b": 0.0}, 0.05)


def test_bonferroni_spending_is_equal():
    spending = bonferroni_spending(("ab", "ac", "bc", "bd"), 0.04)
    assert set(spending) == {"ab", "ac", "bc", "bd"}
    assert all(value == pytest.approx(0.01) for value in spending.values())


def test_bonferroni_spending_rejects_duplicate_candidates():
    with pytest.raises(ValueError):
        bonferroni_spending(("a", "a"), 0.05)


def test_family_confidence_uses_union_bound_without_independence():
    alpha_q = {"p1": 0.01, "p2": 0.02}
    alpha_y = {"p1": 0.015, "p2": 0.005}
    assert family_confidence_lower_bound(alpha_q, alpha_y) == pytest.approx(0.95)


def test_family_confidence_clips_at_zero():
    alpha_q = {"p1": 0.7, "p2": 0.2}
    alpha_y = {"p1": 0.2, "p2": 0.1}
    assert family_confidence_lower_bound(alpha_q, alpha_y) == 0.0


def test_family_confidence_requires_matching_candidate_sets():
    with pytest.raises(ValueError):
        family_confidence_lower_bound({"p1": 0.01}, {"p2": 0.01})


def test_maximum_lower_margin_selector_preserves_family_confidence():
    lower = {"p1": -0.01, "p2": 0.04, "p3": 0.02}
    alpha_q = {key: 0.01 for key in lower}
    alpha_y = {key: 0.005 for key in lower}
    result = select_maximum_lower_margin(lower, alpha_q, alpha_y)
    assert result.selected_candidate == "p2"
    assert result.selected_lower_margin == pytest.approx(0.04)
    assert result.family_failure_budget == pytest.approx(0.045)
    assert result.confidence_lower_bound == pytest.approx(0.955)
    assert result.certified


def test_selector_does_not_certify_nonpositive_winner():
    lower = {"p1": -0.02, "p2": 0.0}
    alpha = {"p1": 0.01, "p2": 0.01}
    result = select_maximum_lower_margin(lower, alpha, alpha)
    assert result.selected_candidate == "p2"
    assert not result.certified


def test_selector_respects_positive_tolerance():
    lower = {"p1": 1e-10, "p2": -0.1}
    alpha = {"p1": 0.01, "p2": 0.01}
    result = select_maximum_lower_margin(lower, alpha, alpha, tolerance=1e-9)
    assert not result.certified


def test_selector_rejects_nonmatching_candidates():
    with pytest.raises(ValueError):
        select_maximum_lower_margin(
            {"p1": 0.1, "p2": 0.2},
            {"p1": 0.01},
            {"p1": 0.01, "p2": 0.01},
        )


def test_spending_outputs_are_finite():
    spending = weighted_alpha_spending({"a": 1.0, "b": 2.0}, 0.05)
    assert all(math.isfinite(value) for value in spending.values())
