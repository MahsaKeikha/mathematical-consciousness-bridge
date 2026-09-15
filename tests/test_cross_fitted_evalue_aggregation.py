from fractions import Fraction

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    empirical_law_from_counts,
)
from consciousness_bridge.cross_fitted_evalue_aggregation import (
    P99CrossFitFoldInput,
    P99SelectedRegimeDesign,
    certify_p99_balanced_distributed_evidence_95_threshold_exact,
    certify_p99_cross_fitted_evalue_aggregation_exact,
)
from consciousness_bridge.cross_fitted_selection_valid_certification import (
    certify_p98_balanced_cross_fit_95_threshold_exact,
)
from consciousness_bridge.selection_valid_holdout_stratification import (
    P96HoldoutRegimeData,
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
    *,
    thresholds: tuple[Fraction, ...] = (Fraction(1, 25),),
    mixture_weights: tuple[Fraction, ...] = (Fraction(1),),
    sample_size: int = 3792,
) -> P99CrossFitFoldInput:
    return P99CrossFitFoldInput(
        name=name,
        selection_description=f"plan learned from the other independent block for {name}",
        selection_information_sample_size=2 * sample_size,
        selected_regimes=(
            P99SelectedRegimeDesign(
                name=f"{name}-a",
                regime_definition="first independently certified regime",
                dependence_range=1,
                alpha_weight=Fraction(1, 2),
            ),
            P99SelectedRegimeDesign(
                name=f"{name}-b",
                regime_definition="second independently certified regime",
                dependence_range=1,
                alpha_weight=Fraction(1, 2),
            ),
        ),
        certification_data=(
            P96HoldoutRegimeData(
                name=f"{name}-a",
                empirical_law=first_law,
                sample_size=sample_size,
            ),
            P96HoldoutRegimeData(
                name=f"{name}-b",
                empirical_law=_point_mass_law(),
                sample_size=sample_size,
            ),
        ),
        threshold_alphas=thresholds,
        threshold_mixture_weights=mixture_weights,
        fold_weight=Fraction(1, 2),
        plan_frozen_before_own_block_evaluation=True,
        calibration_frozen_before_own_block_evaluation=True,
    )


def test_p99_balanced_distributed_checkpoint_is_3774():
    threshold = certify_p99_balanced_distributed_evidence_95_threshold_exact(
        fold_count=2,
        regime_count=2,
        dependence_range=1,
    )
    assert threshold.global_alpha == Fraction(1, 20)
    assert threshold.fold_test_alpha == Fraction(1, 25)
    assert threshold.equal_fold_weight == Fraction(1, 2)
    assert threshold.equal_regime_alpha_weight == Fraction(1, 2)
    assert threshold.local_alpha_budget == Fraction(1, 50)
    assert threshold.minimum_rejecting_folds == 2
    assert threshold.e_value_per_rejecting_fold == 25
    assert threshold.aggregate_e_value_at_minimum_rejecting_folds == 25
    assert threshold.global_rejection_e_value == 20
    assert threshold.last_noncertifying_sample_size == 3773
    assert threshold.first_certifying_sample_size == 3774
    assert threshold.first_exact_replication_sample_size == 3792
    assert threshold.first_certifying_observations_per_fold == 7548
    assert threshold.first_exact_observations_per_fold == 7584
    assert threshold.first_cross_fitted_unique_observations == 15096
    assert threshold.first_exact_cross_fitted_unique_observations == 15168
    target_squared = Fraction(1, 24) ** 2
    assert threshold.last_radius.squared_radius_lower >= target_squared
    assert threshold.first_radius.squared_radius_upper < target_squared


def test_p99_distributed_checkpoint_is_strictly_earlier_than_equal_split_p98():
    p99 = certify_p99_balanced_distributed_evidence_95_threshold_exact(
        fold_count=2,
        regime_count=2,
        dependence_range=1,
    )
    p98 = certify_p98_balanced_cross_fit_95_threshold_exact(
        fold_count=2,
        regime_count=2,
        dependence_range=1,
    )
    assert p99.first_certifying_sample_size == 3774
    assert p98.first_certifying_sample_size == 4045
    assert p98.first_certifying_sample_size - p99.first_certifying_sample_size == 271
    assert p99.first_cross_fitted_unique_observations == 15096
    assert p98.first_cross_fitted_unique_observations == 16180


def test_p99_two_moderate_fold_rejections_aggregate_to_global_rejection():
    certificate = certify_p99_cross_fitted_evalue_aggregation_exact(
        (_fold("fold-a", _witness_law()), _fold("fold-b", _witness_law())),
        global_alpha=Fraction(1, 20),
        certification_blocks_mutually_independent=True,
        own_block_excluded_from_selection=True,
    )
    assert certificate.fold_count == 2
    assert certificate.fold_weight_sum == 1
    assert certificate.global_rejection_e_value == 20
    assert certificate.aggregate_e_value == 25
    assert certificate.rejects_cross_fitted_joint_p75_null
    assert all(fold.fold_e_value == 25 for fold in certificate.fold_certificates)
    assert all(fold.rejecting_thresholds == (Fraction(1, 25),) for fold in certificate.fold_certificates)


def test_p99_one_moderate_fold_rejection_is_not_enough_under_equal_weighting():
    certificate = certify_p99_cross_fitted_evalue_aggregation_exact(
        (_fold("fold-a", _witness_law()), _fold("fold-b", _point_mass_law())),
        global_alpha=Fraction(1, 20),
        certification_blocks_mutually_independent=True,
        own_block_excluded_from_selection=True,
    )
    assert certificate.aggregate_e_value == Fraction(25, 2)
    assert not certificate.rejects_cross_fitted_joint_p75_null


def test_p99_finite_threshold_mixture_is_exact_and_selection_valid():
    thresholds = (Fraction(1, 40), Fraction(1, 25))
    weights = (Fraction(1, 5), Fraction(4, 5))
    certificate = certify_p99_cross_fitted_evalue_aggregation_exact(
        (
            _fold("fold-a", _witness_law(), thresholds=thresholds, mixture_weights=weights),
            _fold("fold-b", _witness_law(), thresholds=thresholds, mixture_weights=weights),
        ),
        global_alpha=Fraction(1, 20),
        certification_blocks_mutually_independent=True,
        own_block_excluded_from_selection=True,
    )
    # At n=3792 the witness clears tau=1/25 but not the stricter tau=1/40 gate.
    for fold in certificate.fold_certificates:
        assert fold.rejecting_thresholds == (Fraction(1, 25),)
        assert fold.fold_e_value == 20
        assert fold.weighted_global_contribution == 10
    assert certificate.aggregate_e_value == 20
    assert certificate.rejects_cross_fitted_joint_p75_null


def test_p99_requires_independent_blocks_and_no_own_fold_leakage():
    folds = (_fold("a", _point_mass_law()), _fold("b", _point_mass_law()))
    with pytest.raises(ValueError, match="mutually independent"):
        certify_p99_cross_fitted_evalue_aggregation_exact(
            folds,
            global_alpha=Fraction(1, 20),
            certification_blocks_mutually_independent=False,
            own_block_excluded_from_selection=True,
        )
    with pytest.raises(ValueError, match="exclude its own"):
        certify_p99_cross_fitted_evalue_aggregation_exact(
            folds,
            global_alpha=Fraction(1, 20),
            certification_blocks_mutually_independent=True,
            own_block_excluded_from_selection=False,
        )


def test_p99_rejects_unfrozen_calibration_and_invalid_weight_sums():
    fold = _fold("a", _point_mass_law())
    bad_calibration = P99CrossFitFoldInput(
        name=fold.name,
        selection_description=fold.selection_description,
        selection_information_sample_size=fold.selection_information_sample_size,
        selected_regimes=fold.selected_regimes,
        certification_data=fold.certification_data,
        threshold_alphas=fold.threshold_alphas,
        threshold_mixture_weights=fold.threshold_mixture_weights,
        fold_weight=fold.fold_weight,
        plan_frozen_before_own_block_evaluation=True,
        calibration_frozen_before_own_block_evaluation=False,
    )
    with pytest.raises(ValueError, match="calibration"):
        certify_p99_cross_fitted_evalue_aggregation_exact(
            (bad_calibration, _fold("b", _point_mass_law())),
            global_alpha=Fraction(1, 20),
            certification_blocks_mutually_independent=True,
            own_block_excluded_from_selection=True,
        )

    bad_mix = _fold(
        "mix",
        _point_mass_law(),
        thresholds=(Fraction(1, 40), Fraction(1, 25)),
        mixture_weights=(Fraction(1, 2), Fraction(1, 4)),
    )
    with pytest.raises(ValueError, match="mixture weights"):
        certify_p99_cross_fitted_evalue_aggregation_exact(
            (bad_mix, _fold("b", _point_mass_law())),
            global_alpha=Fraction(1, 20),
            certification_blocks_mutually_independent=True,
            own_block_excluded_from_selection=True,
        )


def test_p99_preserves_scientific_boundary_in_module_docstring():
    module = __import__(
        "consciousness_bridge.cross_fitted_evalue_aggregation",
        fromlist=["dummy"],
    )
    source = (module.__doc__ or "").lower()
    assert "e-value" in source
    assert "does not uniformly dominate" in source
    assert "dependent" in source
    assert "nonphysicality" in source
    assert "physical-to-experiential bridge" in source
