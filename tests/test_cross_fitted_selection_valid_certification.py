from fractions import Fraction

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    empirical_law_from_counts,
)
from consciousness_bridge.cross_fitted_selection_valid_certification import (
    P98CrossFitFoldInput,
    certify_p98_balanced_cross_fit_95_threshold_exact,
    certify_p98_cross_fitted_rejection_exact,
)
from consciousness_bridge.selection_valid_holdout_stratification import (
    P96HoldoutRegimeData,
    P96SelectedRegimeDesign,
)


def _witness_law() -> tuple[Fraction, ...]:
    return empirical_law_from_counts(
        (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
    )


def _point_mass_law() -> tuple[Fraction, ...]:
    return (Fraction(1),) + (Fraction(0),) * 15


def _fold(
    name: str,
    first_law: tuple[Fraction, ...],
) -> P98CrossFitFoldInput:
    return P98CrossFitFoldInput(
        name=name,
        selection_description=f"arbitrary plan learned from the other block for {name}",
        selection_information_sample_size=8112,
        selected_regimes=(
            P96SelectedRegimeDesign(
                name=f"{name}-a",
                regime_definition="first independently certified regime",
                dependence_range=1,
                alpha_budget=Fraction(1, 80),
            ),
            P96SelectedRegimeDesign(
                name=f"{name}-b",
                regime_definition="second independently certified regime",
                dependence_range=1,
                alpha_budget=Fraction(1, 80),
            ),
        ),
        certification_data=(
            P96HoldoutRegimeData(
                name=f"{name}-a",
                empirical_law=first_law,
                sample_size=4056,
            ),
            P96HoldoutRegimeData(
                name=f"{name}-b",
                empirical_law=_point_mass_law(),
                sample_size=4056,
            ),
        ),
        fold_alpha=Fraction(1, 40),
        plan_frozen_before_own_block_evaluation=True,
    )


def test_p98_two_fold_two_regime_threshold_is_4045():
    threshold = certify_p98_balanced_cross_fit_95_threshold_exact(
        fold_count=2,
        regime_count=2,
        dependence_range=1,
    )
    assert threshold.global_alpha == Fraction(1, 20)
    assert threshold.fold_alpha_budget == Fraction(1, 40)
    assert threshold.local_alpha_budget == Fraction(1, 80)
    assert threshold.last_noncertifying_sample_size == 4044
    assert threshold.first_certifying_sample_size == 4045
    assert threshold.first_exact_replication_sample_size == 4056
    assert threshold.first_certifying_observations_per_fold == 8090
    assert threshold.first_exact_observations_per_fold == 8112
    assert threshold.first_cross_fitted_unique_observations == 16180
    assert threshold.first_exact_cross_fitted_unique_observations == 16224
    assert threshold.selection_information_observations_per_fold_at_threshold == 8090
    assert threshold.exact_selection_information_observations_per_fold == 8112
    target_squared = Fraction(1, 24) ** 2
    assert threshold.last_radius.squared_radius_lower >= target_squared
    assert threshold.first_radius.squared_radius_upper < target_squared


def test_p98_cross_fitting_supports_post_inspection_fold_selection():
    certificate = certify_p98_cross_fitted_rejection_exact(
        (
            _fold("fold-a", _witness_law()),
            _fold("fold-b", _point_mass_law()),
        ),
        global_alpha=Fraction(1, 20),
        selected_fold_name="fold-a",
        certification_blocks_mutually_independent=True,
        own_block_excluded_from_selection=True,
    )
    assert certificate.fold_count == 2
    assert certificate.allocated_fold_alpha == Fraction(1, 20)
    assert certificate.simultaneous_confidence_lower == Fraction(19, 20)
    assert certificate.rejecting_folds == ("fold-a",)
    assert certificate.rejects_selected_joint_p75_null
    assert certificate.rejects_cross_fitted_joint_p75_null
    assert certificate.fold_certificates[0].certification_observations == 8112
    assert certificate.fold_certificates[0].nested_p96_certificate.selection_complexity_alpha_penalty == 0


def test_p98_can_select_a_nonrejecting_fold_without_changing_other_fold_validity():
    certificate = certify_p98_cross_fitted_rejection_exact(
        (
            _fold("fold-a", _witness_law()),
            _fold("fold-b", _point_mass_law()),
        ),
        global_alpha=Fraction(1, 20),
        selected_fold_name="fold-b",
        certification_blocks_mutually_independent=True,
        own_block_excluded_from_selection=True,
    )
    assert certificate.rejecting_folds == ("fold-a",)
    assert not certificate.rejects_selected_joint_p75_null
    assert certificate.rejects_cross_fitted_joint_p75_null


def test_p98_requires_independent_blocks_and_no_own_fold_leakage():
    folds = (_fold("a", _point_mass_law()), _fold("b", _point_mass_law()))
    with pytest.raises(ValueError, match="mutually independent"):
        certify_p98_cross_fitted_rejection_exact(
            folds,
            global_alpha=Fraction(1, 20),
            selected_fold_name="a",
            certification_blocks_mutually_independent=False,
            own_block_excluded_from_selection=True,
        )
    with pytest.raises(ValueError, match="exclude its own"):
        certify_p98_cross_fitted_rejection_exact(
            folds,
            global_alpha=Fraction(1, 20),
            selected_fold_name="a",
            certification_blocks_mutually_independent=True,
            own_block_excluded_from_selection=False,
        )


def test_p98_rejects_fold_budget_overspend_duplicate_names_and_unfrozen_plan():
    fold = _fold("same", _point_mass_law())
    with pytest.raises(ValueError, match="unique"):
        certify_p98_cross_fitted_rejection_exact(
            (fold, fold),
            global_alpha=Fraction(1, 20),
            selected_fold_name="same",
            certification_blocks_mutually_independent=True,
            own_block_excluded_from_selection=True,
        )

    oversized = P98CrossFitFoldInput(
        name="large",
        selection_description="oversized fold budget",
        selection_information_sample_size=10,
        selected_regimes=fold.selected_regimes,
        certification_data=fold.certification_data,
        fold_alpha=Fraction(3, 50),
        plan_frozen_before_own_block_evaluation=True,
    )
    with pytest.raises(ValueError, match="exceed"):
        certify_p98_cross_fitted_rejection_exact(
            (oversized,),
            global_alpha=Fraction(1, 20),
            selected_fold_name="large",
            certification_blocks_mutually_independent=True,
            own_block_excluded_from_selection=True,
        )

    unfrozen = P98CrossFitFoldInput(
        name="unfrozen",
        selection_description="invalid leakage-prone fold",
        selection_information_sample_size=10,
        selected_regimes=fold.selected_regimes,
        certification_data=fold.certification_data,
        fold_alpha=Fraction(1, 40),
        plan_frozen_before_own_block_evaluation=False,
    )
    with pytest.raises(ValueError, match="frozen"):
        certify_p98_cross_fitted_rejection_exact(
            (unfrozen,),
            global_alpha=Fraction(1, 20),
            selected_fold_name="unfrozen",
            certification_blocks_mutually_independent=True,
            own_block_excluded_from_selection=True,
        )


def test_p98_balanced_threshold_requires_at_least_two_folds():
    with pytest.raises(ValueError, match="at least two"):
        certify_p98_balanced_cross_fit_95_threshold_exact(
            fold_count=1,
            regime_count=2,
            dependence_range=1,
        )


def test_p98_preserves_scientific_boundary_in_module_docstring():
    module = __import__(
        "consciousness_bridge.cross_fitted_selection_valid_certification",
        fromlist=["dummy"],
    )
    source = (module.__doc__ or "").lower()
    assert "cross-fitted" in source
    assert "selection information" in source
    assert "union bound" in source
    assert "nonphysicality" in source
    assert "physical-to-experiential bridge" in source
