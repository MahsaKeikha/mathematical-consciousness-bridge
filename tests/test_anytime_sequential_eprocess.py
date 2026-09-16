from fractions import Fraction

import pytest

from consciousness_bridge.anytime_sequential_eprocess import (
    P100SequentialRoundInput,
    certify_p100_anytime_sequential_eprocess_exact,
    certify_p100_balanced_moderate_evidence_95_checkpoint_exact,
)
from consciousness_bridge.certified_continuous_model_separation import (
    empirical_law_from_counts,
)
from consciousness_bridge.cross_fitted_evalue_aggregation import (
    P99CrossFitFoldInput,
    P99SelectedRegimeDesign,
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
    sample_size: int = 3792,
) -> P99CrossFitFoldInput:
    return P99CrossFitFoldInput(
        name=name,
        selection_description=f"past-only plan for {name}",
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
        threshold_alphas=(Fraction(1, 25),),
        threshold_mixture_weights=(Fraction(1),),
        fold_weight=Fraction(1, 2),
        plan_frozen_before_own_block_evaluation=True,
        calibration_frozen_before_own_block_evaluation=True,
    )


def _moderate_round(name: str, *, stake: Fraction = Fraction(1, 2)) -> P100SequentialRoundInput:
    return P100SequentialRoundInput(
        name=name,
        folds=(
            _fold(f"{name}-rejecting", _witness_law()),
            _fold(f"{name}-nonrejecting", _point_mass_law()),
        ),
        stake=stake,
        choices_predictable_from_past_only=True,
        certification_data_conditionally_fresh_given_past=True,
    )


def test_p100_balanced_checkpoint_accumulates_two_nondecisive_p99_rounds():
    checkpoint = certify_p100_balanced_moderate_evidence_95_checkpoint_exact()
    assert checkpoint.global_alpha == Fraction(1, 20)
    assert checkpoint.fold_test_alpha == Fraction(1, 25)
    assert checkpoint.rejecting_folds_per_round == 1
    assert checkpoint.round_e_value == Fraction(25, 2)
    assert checkpoint.round_e_value < checkpoint.global_rejection_e_value
    assert checkpoint.stake == Fraction(1, 2)
    assert checkpoint.betting_factor == Fraction(27, 4)
    assert checkpoint.first_crossing_round == 2
    assert checkpoint.cumulative_at_first_crossing == Fraction(729, 16)
    assert checkpoint.cumulative_at_first_crossing > 20
    assert checkpoint.first_certifying_sample_size_per_regime == 3774
    assert checkpoint.first_exact_replication_sample_size_per_regime == 3792
    assert checkpoint.unique_observations_per_round == 15096
    assert checkpoint.exact_unique_observations_per_round == 15168
    assert checkpoint.unique_observations_at_first_crossing == 30192
    assert checkpoint.exact_unique_observations_at_first_crossing == 30336


def test_p100_one_moderate_round_does_not_reject_but_two_do():
    one = certify_p100_anytime_sequential_eprocess_exact(
        (_moderate_round("round-1"),),
        global_alpha=Fraction(1, 20),
        within_round_certification_blocks_mutually_independent=True,
        own_block_excluded_from_within_round_selection=True,
    )
    assert one.round_certificates[0].round_e_value == Fraction(25, 2)
    assert one.round_certificates[0].betting_factor == Fraction(27, 4)
    assert one.final_e_process == Fraction(27, 4)
    assert one.first_crossing_round is None
    assert not one.rejects_sequential_joint_p75_null

    two = certify_p100_anytime_sequential_eprocess_exact(
        (_moderate_round("round-1"), _moderate_round("round-2")),
        global_alpha=Fraction(1, 20),
        within_round_certification_blocks_mutually_independent=True,
        own_block_excluded_from_within_round_selection=True,
    )
    assert [r.round_e_value for r in two.round_certificates] == [
        Fraction(25, 2),
        Fraction(25, 2),
    ]
    assert two.final_e_process == Fraction(729, 16)
    assert two.maximum_e_process == Fraction(729, 16)
    assert two.first_crossing_round == 2
    assert two.rejects_sequential_joint_p75_null


def test_p100_reserve_stake_prevents_zero_round_from_annihilating_process():
    zero_round = P100SequentialRoundInput(
        name="zero",
        folds=(
            _fold("zero-a", _point_mass_law()),
            _fold("zero-b", _point_mass_law()),
        ),
        stake=Fraction(1, 2),
        choices_predictable_from_past_only=True,
        certification_data_conditionally_fresh_given_past=True,
    )
    certificate = certify_p100_anytime_sequential_eprocess_exact(
        (zero_round,),
        global_alpha=Fraction(1, 20),
        within_round_certification_blocks_mutually_independent=True,
        own_block_excluded_from_within_round_selection=True,
    )
    assert certificate.round_certificates[0].round_e_value == 0
    assert certificate.round_certificates[0].betting_factor == Fraction(1, 2)
    assert certificate.final_e_process == Fraction(1, 2)


def test_p100_requires_predictable_choices_and_fresh_current_round_data():
    base = _moderate_round("round")
    bad_predictable = P100SequentialRoundInput(
        name=base.name,
        folds=base.folds,
        stake=base.stake,
        choices_predictable_from_past_only=False,
        certification_data_conditionally_fresh_given_past=True,
    )
    with pytest.raises(ValueError, match="predictable"):
        certify_p100_anytime_sequential_eprocess_exact(
            (bad_predictable,),
            global_alpha=Fraction(1, 20),
            within_round_certification_blocks_mutually_independent=True,
            own_block_excluded_from_within_round_selection=True,
        )

    bad_freshness = P100SequentialRoundInput(
        name=base.name,
        folds=base.folds,
        stake=base.stake,
        choices_predictable_from_past_only=True,
        certification_data_conditionally_fresh_given_past=False,
    )
    with pytest.raises(ValueError, match="conditionally fresh"):
        certify_p100_anytime_sequential_eprocess_exact(
            (bad_freshness,),
            global_alpha=Fraction(1, 20),
            within_round_certification_blocks_mutually_independent=True,
            own_block_excluded_from_within_round_selection=True,
        )


def test_p100_rejects_invalid_stakes_and_duplicate_round_names():
    with pytest.raises(ValueError, match="stake"):
        certify_p100_anytime_sequential_eprocess_exact(
            (_moderate_round("bad", stake=Fraction(3, 2)),),
            global_alpha=Fraction(1, 20),
            within_round_certification_blocks_mutually_independent=True,
            own_block_excluded_from_within_round_selection=True,
        )

    with pytest.raises(ValueError, match="round names"):
        certify_p100_anytime_sequential_eprocess_exact(
            (_moderate_round("same"), _moderate_round("same")),
            global_alpha=Fraction(1, 20),
            within_round_certification_blocks_mutually_independent=True,
            own_block_excluded_from_within_round_selection=True,
        )


def test_p100_preserves_scientific_boundary_in_module_docstring():
    module = __import__(
        "consciousness_bridge.anytime_sequential_eprocess",
        fromlist=["dummy"],
    )
    source = (module.__doc__ or "").lower()
    assert "anytime-valid" in source
    assert "supermartingale" in source
    assert "ville" in source
    assert "nonphysicality" in source
    assert "physical-to-experiential bridge" in source
