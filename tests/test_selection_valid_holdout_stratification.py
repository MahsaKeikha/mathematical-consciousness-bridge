from fractions import Fraction

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    empirical_law_from_counts,
)
from consciousness_bridge.selection_valid_holdout_stratification import (
    P96HoldoutRegimeData,
    P96PilotSelectionPlan,
    P96SelectedRegimeDesign,
    certify_p96_balanced_holdout_95_threshold_exact,
    certify_p96_selection_valid_holdout_rejection_exact,
)


def _witness_law() -> tuple[Fraction, ...]:
    return empirical_law_from_counts(
        (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
    )


def _point_mass_law() -> tuple[Fraction, ...]:
    return (Fraction(1),) + (Fraction(0),) * 15


def _two_regime_plan() -> P96PilotSelectionPlan:
    return P96PilotSelectionPlan(
        selection_description="pilot-selected two-regime partition",
        pilot_sample_size=500,
        selected_regimes=(
            P96SelectedRegimeDesign(
                name="early",
                regime_definition="pilot-selected early regime",
                dependence_range=1,
                alpha_budget=Fraction(1, 40),
            ),
            P96SelectedRegimeDesign(
                name="late",
                regime_definition="pilot-selected late regime",
                dependence_range=1,
                alpha_budget=Fraction(1, 40),
            ),
        ),
        familywise_alpha=Fraction(1, 20),
        pilot_holdout_independent=True,
        plan_frozen_before_holdout_evaluation=True,
    )


def test_p96_independent_holdout_preserves_p95_familywise_rejection():
    certificate = certify_p96_selection_valid_holdout_rejection_exact(
        _two_regime_plan(),
        (
            P96HoldoutRegimeData(
                name="early",
                empirical_law=_witness_law(),
                sample_size=3648,
            ),
            P96HoldoutRegimeData(
                name="late",
                empirical_law=_point_mass_law(),
                sample_size=3648,
            ),
        ),
    )
    assert certificate.selected_regime_count == 2
    assert certificate.selection_complexity_alpha_penalty == 0
    assert certificate.declared_familywise_alpha == Fraction(1, 20)
    assert certificate.nested_p95_certificate.allocated_alpha == Fraction(1, 20)
    assert certificate.rejecting_regimes == ("early",)
    assert certificate.rejects_joint_p75_null


def test_p96_selection_complexity_does_not_change_balanced_holdout_threshold():
    threshold = certify_p96_balanced_holdout_95_threshold_exact(
        pilot_sample_size=500,
        regime_count=2,
        dependence_range=1,
    )
    assert threshold.holdout_threshold.first_certifying_sample_size == 3645
    assert threshold.holdout_threshold.first_exact_replication_sample_size == 3648
    assert threshold.first_certifying_holdout_observations == 7290
    assert threshold.first_exact_replication_holdout_observations == 7296
    assert threshold.first_certifying_total_observations == 7790
    assert threshold.first_exact_replication_total_observations == 7796


def test_p96_can_use_unequal_pilot_selected_error_budgets():
    plan = P96PilotSelectionPlan(
        selection_description="pilot allocated more error to the smaller regime",
        pilot_sample_size=200,
        selected_regimes=(
            P96SelectedRegimeDesign(
                name="small",
                regime_definition="small selected block",
                dependence_range=0,
                alpha_budget=Fraction(3, 100),
            ),
            P96SelectedRegimeDesign(
                name="large",
                regime_definition="large selected block",
                dependence_range=2,
                alpha_budget=Fraction(1, 100),
            ),
        ),
        familywise_alpha=Fraction(1, 20),
        pilot_holdout_independent=True,
        plan_frozen_before_holdout_evaluation=True,
    )
    certificate = certify_p96_selection_valid_holdout_rejection_exact(
        plan,
        (
            P96HoldoutRegimeData(
                name="large",
                empirical_law=_point_mass_law(),
                sample_size=200,
            ),
            P96HoldoutRegimeData(
                name="small",
                empirical_law=_point_mass_law(),
                sample_size=200,
            ),
        ),
    )
    assert certificate.nested_p95_certificate.allocated_alpha == Fraction(1, 25)
    assert certificate.nested_p95_certificate.simultaneous_confidence_lower == Fraction(
        24, 25
    )
    assert not certificate.rejects_joint_p75_null


def test_p96_refuses_reuse_or_unfrozen_selection_plan():
    base = _two_regime_plan()
    with pytest.raises(ValueError, match="independent"):
        certify_p96_selection_valid_holdout_rejection_exact(
            P96PilotSelectionPlan(
                selection_description=base.selection_description,
                pilot_sample_size=base.pilot_sample_size,
                selected_regimes=base.selected_regimes,
                familywise_alpha=base.familywise_alpha,
                pilot_holdout_independent=False,
                plan_frozen_before_holdout_evaluation=True,
            ),
            (
                P96HoldoutRegimeData("early", _point_mass_law(), 100),
                P96HoldoutRegimeData("late", _point_mass_law(), 100),
            ),
        )

    with pytest.raises(ValueError, match="frozen"):
        certify_p96_selection_valid_holdout_rejection_exact(
            P96PilotSelectionPlan(
                selection_description=base.selection_description,
                pilot_sample_size=base.pilot_sample_size,
                selected_regimes=base.selected_regimes,
                familywise_alpha=base.familywise_alpha,
                pilot_holdout_independent=True,
                plan_frozen_before_holdout_evaluation=False,
            ),
            (
                P96HoldoutRegimeData("early", _point_mass_law(), 100),
                P96HoldoutRegimeData("late", _point_mass_law(), 100),
            ),
        )


def test_p96_requires_holdout_data_to_match_selected_regimes_exactly():
    with pytest.raises(ValueError, match="match"):
        certify_p96_selection_valid_holdout_rejection_exact(
            _two_regime_plan(),
            (P96HoldoutRegimeData("early", _point_mass_law(), 100),),
        )


def test_p96_preserves_scientific_boundary_in_module_docstring():
    module = __import__(
        "consciousness_bridge.selection_valid_holdout_stratification",
        fromlist=["dummy"],
    )
    source = (module.__doc__ or "").lower()
    assert "pilot-data procedure" in source
    assert "independent holdout" in source
    assert "zero extra selection penalty" in source
    assert "not automatically an independent holdout design" in source
    assert "nonphysicality" in source
    assert "physical-to-experiential bridge" in source
