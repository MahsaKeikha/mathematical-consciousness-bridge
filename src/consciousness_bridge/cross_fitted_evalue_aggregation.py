"""P99 cross-fitted e-value aggregation of selection-valid fold certificates.

P98 controls several cross-fitted certification statements by allocating a
familywise alpha budget across folds and applying a union bound. That construction
is exact and robust, but it is naturally oriented toward a sparse pattern in
which one fold becomes individually decisive.

P99 develops a complementary exact finite-sample aggregation rule for distributed
evidence. For fold k and a level tau fixed without using fold k's own certification
statistics, let R_k(tau) be the P96/P95 rejection indicator. Under the fold null,
conditional on the information used to select the fold plan,

    P(R_k(tau)=1 | selection information) <= tau.

Therefore R_k(tau)/tau is a nonnegative conditional e-value. Any exact rational
convex mixture across a finite threshold grid remains a fold e-value. A fixed
convex average across folds remains an e-value even though the cross-fitted fold
certificates may be dependent, because only linearity of expectation is used.
Markov's inequality then gives a global level-alpha rejection rule at aggregate
e-value at least 1/alpha.

This construction does not assume fold independence at the aggregation stage and
does not require a Bonferroni split of the global alpha across folds. It can
accumulate moderate evidence from several folds. It does not uniformly dominate
P98: a sparse configuration with one very strong fold can favor P98, while a
distributed configuration can favor P99.

P99 still requires genuinely independent certification blocks for the P96
selection-valid step, exclusion of each fold's own certification statistics from
that fold's plan and calibration choices, correct within-regime dependence
assumptions, and a finite threshold mixture fixed before own-fold evaluation. It
does not establish model acceptance, consciousness identification, nonphysicality,
or completion of the physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from consciousness_bridge.finite_range_dependent_sign_coherence import (
    P94DependentRadiusCertificate,
    certified_p94_dependent_squared_radius,
)
from consciousness_bridge.selection_valid_holdout_stratification import (
    P96HoldoutRegimeData,
    P96PilotSelectionPlan,
    P96SelectedRegimeDesign,
    P96SelectionValidRejectionCertificate,
    certify_p96_selection_valid_holdout_rejection_exact,
)

_ALPHA_95 = Fraction(1, 20)
_WITNESS_RADIUS = Fraction(1, 24)
_BASE_PROFILE_SAMPLE_SIZE = 24


@dataclass(frozen=True)
class P99SelectedRegimeDesign:
    """One selected regime with an exact share of a fold test level."""

    name: str
    regime_definition: str
    dependence_range: int
    alpha_weight: Fraction


@dataclass(frozen=True)
class P99CrossFitFoldInput:
    """One cross-fitted fold together with its finite e-value calibration grid."""

    name: str
    selection_description: str
    selection_information_sample_size: int
    selected_regimes: tuple[P99SelectedRegimeDesign, ...]
    certification_data: tuple[P96HoldoutRegimeData, ...]
    threshold_alphas: tuple[Fraction, ...]
    threshold_mixture_weights: tuple[Fraction, ...]
    fold_weight: Fraction
    plan_frozen_before_own_block_evaluation: bool
    calibration_frozen_before_own_block_evaluation: bool


@dataclass(frozen=True)
class P99ThresholdEvidenceCertificate:
    """One level-tau rejection indicator converted into an exact e-value."""

    threshold_alpha: Fraction
    mixture_weight: Fraction
    nested_p96_certificate: P96SelectionValidRejectionCertificate
    rejects_fold_null: bool
    threshold_e_value: Fraction
    weighted_e_value_contribution: Fraction


@dataclass(frozen=True)
class P99FoldEvidenceCertificate:
    """Finite threshold-mixture e-value for one cross-fitted fold."""

    name: str
    fold_weight: Fraction
    selection_information_sample_size: int
    certification_observations: int
    threshold_certificates: tuple[P99ThresholdEvidenceCertificate, ...]
    rejecting_thresholds: tuple[Fraction, ...]
    fold_e_value: Fraction
    weighted_global_contribution: Fraction


@dataclass(frozen=True)
class P99CrossFittedEValueCertificate:
    """Exact aggregate e-value and global rejection decision."""

    fold_count: int
    global_alpha: Fraction
    global_rejection_e_value: Fraction
    fold_weight_sum: Fraction
    fold_certificates: tuple[P99FoldEvidenceCertificate, ...]
    aggregate_e_value: Fraction
    rejects_cross_fitted_joint_p75_null: bool
    conclusion: str


@dataclass(frozen=True)
class P99BalancedDistributedEvidenceThresholdCertificate:
    """Exact 95 percent checkpoint for the symmetric distributed-evidence design."""

    fold_count: int
    regime_count: int
    dependence_range: int
    global_alpha: Fraction
    fold_test_alpha: Fraction
    equal_fold_weight: Fraction
    equal_regime_alpha_weight: Fraction
    local_alpha_budget: Fraction
    witness_radius: Fraction
    minimum_rejecting_folds: int
    e_value_per_rejecting_fold: Fraction
    aggregate_e_value_at_minimum_rejecting_folds: Fraction
    global_rejection_e_value: Fraction
    last_noncertifying_sample_size: int
    first_certifying_sample_size: int
    last_radius: P94DependentRadiusCertificate
    first_radius: P94DependentRadiusCertificate
    base_profile_sample_size: int
    first_exact_replication_sample_size: int
    first_certifying_observations_per_fold: int
    first_exact_observations_per_fold: int
    first_cross_fitted_unique_observations: int
    first_exact_cross_fitted_unique_observations: int


def _nonempty_text(value: str, *, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a nonempty string")
    return value.strip()


def _positive_integer(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def _probability(value: Fraction, *, name: str) -> Fraction:
    if not isinstance(value, Fraction):
        raise TypeError(f"{name} must be a fractions.Fraction")
    if value <= 0 or value >= 1:
        raise ValueError(f"{name} must lie strictly between zero and one")
    return value


def _positive_weight(value: Fraction, *, name: str) -> Fraction:
    if not isinstance(value, Fraction):
        raise TypeError(f"{name} must be a fractions.Fraction")
    if value <= 0 or value > 1:
        raise ValueError(f"{name} must lie in (0, 1]")
    return value


def certify_p99_cross_fitted_evalue_aggregation_exact(
    folds: tuple[P99CrossFitFoldInput, ...],
    *,
    global_alpha: Fraction,
    certification_blocks_mutually_independent: bool,
    own_block_excluded_from_selection: bool,
    series_terms: int = 20,
) -> P99CrossFittedEValueCertificate:
    """Aggregate cross-fitted P96 rejection indicators as exact e-values.

    For every fold and every threshold tau, the nested P96 certificate is a
    conditional level-tau test because the plan and calibration are frozen before
    the fold's own independent certification block is evaluated. Hence
    R(tau)/tau has conditional expectation at most one under the fold null.
    Convex mixtures across thresholds and folds preserve expectation at most one
    without any independence requirement among the final fold e-values.
    """

    if certification_blocks_mutually_independent is not True:
        raise ValueError("cross-fitted certification blocks must be mutually independent")
    if own_block_excluded_from_selection is not True:
        raise ValueError("each fold must exclude its own certification block from plan selection")
    if not isinstance(folds, tuple) or len(folds) < 2:
        raise ValueError("folds must be a tuple containing at least two folds")
    global_alpha = _probability(global_alpha, name="global_alpha")
    _positive_integer(series_terms, name="series_terms")

    names: list[str] = []
    fold_weight_sum = Fraction(0)
    validated: list[P99CrossFitFoldInput] = []
    for fold in folds:
        if not isinstance(fold, P99CrossFitFoldInput):
            raise TypeError("every fold must be a P99CrossFitFoldInput")
        name = _nonempty_text(fold.name, name="fold name")
        names.append(name)
        _nonempty_text(fold.selection_description, name="selection_description")
        _positive_integer(
            fold.selection_information_sample_size,
            name="selection_information_sample_size",
        )
        if fold.plan_frozen_before_own_block_evaluation is not True:
            raise ValueError("every fold plan must be frozen before own-block evaluation")
        if fold.calibration_frozen_before_own_block_evaluation is not True:
            raise ValueError("every fold e-value calibration must be frozen before own-block evaluation")
        if not isinstance(fold.selected_regimes, tuple) or not fold.selected_regimes:
            raise ValueError("every fold must contain selected regimes")
        if not isinstance(fold.certification_data, tuple) or not fold.certification_data:
            raise ValueError("every fold must contain certification data")
        if not isinstance(fold.threshold_alphas, tuple) or not fold.threshold_alphas:
            raise ValueError("threshold_alphas must be a nonempty tuple")
        if not isinstance(fold.threshold_mixture_weights, tuple):
            raise TypeError("threshold_mixture_weights must be a tuple")
        if len(fold.threshold_alphas) != len(fold.threshold_mixture_weights):
            raise ValueError("threshold_alphas and threshold_mixture_weights must have equal length")
        thresholds = tuple(
            _probability(value, name="threshold alpha") for value in fold.threshold_alphas
        )
        if len(set(thresholds)) != len(thresholds):
            raise ValueError("threshold_alphas must be unique within each fold")
        mixture_weights = tuple(
            _positive_weight(value, name="threshold mixture weight")
            for value in fold.threshold_mixture_weights
        )
        if sum(mixture_weights, Fraction(0)) != 1:
            raise ValueError("threshold mixture weights must sum exactly to one")

        regime_names: list[str] = []
        regime_weight_sum = Fraction(0)
        for design in fold.selected_regimes:
            if not isinstance(design, P99SelectedRegimeDesign):
                raise TypeError("every selected regime must be a P99SelectedRegimeDesign")
            regime_names.append(_nonempty_text(design.name, name="regime name"))
            _nonempty_text(design.regime_definition, name="regime_definition")
            if (
                isinstance(design.dependence_range, bool)
                or not isinstance(design.dependence_range, int)
                or design.dependence_range < 0
            ):
                raise ValueError("dependence_range must be a nonnegative integer")
            regime_weight_sum += _positive_weight(
                design.alpha_weight,
                name="regime alpha weight",
            )
        if len(set(regime_names)) != len(regime_names):
            raise ValueError("regime names must be unique within each fold")
        if regime_weight_sum > 1:
            raise ValueError("regime alpha weights may not sum above one")

        data_names: list[str] = []
        for data in fold.certification_data:
            if not isinstance(data, P96HoldoutRegimeData):
                raise TypeError("every certification item must be P96HoldoutRegimeData")
            data_names.append(_nonempty_text(data.name, name="certification regime name"))
            _positive_integer(data.sample_size, name="certification sample_size")
        if len(set(data_names)) != len(data_names):
            raise ValueError("certification regime names must be unique within each fold")
        if set(data_names) != set(regime_names):
            raise ValueError("certification regime names must match selected regime names")

        fold_weight = _positive_weight(fold.fold_weight, name="fold weight")
        fold_weight_sum += fold_weight
        validated.append(fold)

    if len(set(names)) != len(names):
        raise ValueError("fold names must be unique")
    if fold_weight_sum != 1:
        raise ValueError("fold weights must sum exactly to one")

    fold_certificates: list[P99FoldEvidenceCertificate] = []
    for fold in validated:
        threshold_certificates: list[P99ThresholdEvidenceCertificate] = []
        fold_e_value = Fraction(0)
        for threshold_alpha, mixture_weight in zip(
            fold.threshold_alphas,
            fold.threshold_mixture_weights,
            strict=True,
        ):
            selected_regimes = tuple(
                P96SelectedRegimeDesign(
                    name=design.name.strip(),
                    regime_definition=design.regime_definition.strip(),
                    dependence_range=design.dependence_range,
                    alpha_budget=threshold_alpha * design.alpha_weight,
                )
                for design in fold.selected_regimes
            )
            plan = P96PilotSelectionPlan(
                selection_description=fold.selection_description.strip(),
                pilot_sample_size=fold.selection_information_sample_size,
                selected_regimes=selected_regimes,
                familywise_alpha=threshold_alpha,
                pilot_holdout_independent=True,
                plan_frozen_before_holdout_evaluation=True,
            )
            nested = certify_p96_selection_valid_holdout_rejection_exact(
                plan,
                fold.certification_data,
                series_terms=series_terms,
            )
            rejects = nested.rejects_joint_p75_null
            threshold_e_value = Fraction(1, 1) / threshold_alpha if rejects else Fraction(0)
            contribution = mixture_weight * threshold_e_value
            fold_e_value += contribution
            threshold_certificates.append(
                P99ThresholdEvidenceCertificate(
                    threshold_alpha=threshold_alpha,
                    mixture_weight=mixture_weight,
                    nested_p96_certificate=nested,
                    rejects_fold_null=rejects,
                    threshold_e_value=threshold_e_value,
                    weighted_e_value_contribution=contribution,
                )
            )

        certification_observations = sum(
            data.sample_size for data in fold.certification_data
        )
        rejecting_thresholds = tuple(
            certificate.threshold_alpha
            for certificate in threshold_certificates
            if certificate.rejects_fold_null
        )
        weighted_global = fold.fold_weight * fold_e_value
        fold_certificates.append(
            P99FoldEvidenceCertificate(
                name=fold.name.strip(),
                fold_weight=fold.fold_weight,
                selection_information_sample_size=fold.selection_information_sample_size,
                certification_observations=certification_observations,
                threshold_certificates=tuple(threshold_certificates),
                rejecting_thresholds=rejecting_thresholds,
                fold_e_value=fold_e_value,
                weighted_global_contribution=weighted_global,
            )
        )

    certificate_tuple = tuple(fold_certificates)
    aggregate = sum(
        (certificate.weighted_global_contribution for certificate in certificate_tuple),
        Fraction(0),
    )
    rejection_e_value = Fraction(1, 1) / global_alpha
    rejects = aggregate >= rejection_e_value
    return P99CrossFittedEValueCertificate(
        fold_count=len(folds),
        global_alpha=global_alpha,
        global_rejection_e_value=rejection_e_value,
        fold_weight_sum=fold_weight_sum,
        fold_certificates=certificate_tuple,
        aggregate_e_value=aggregate,
        rejects_cross_fitted_joint_p75_null=rejects,
        conclusion=(
            "Cross-fitted joint P75 null rejected by exact e-value aggregation"
            if rejects
            else "Cross-fitted joint P75 null not rejected by the exact e-value aggregate"
        ),
    )


def certify_p99_balanced_distributed_evidence_95_threshold_exact(
    *,
    fold_count: int,
    regime_count: int,
    dependence_range: int,
    fold_test_alpha: Fraction = Fraction(1, 25),
    series_terms: int = 20,
) -> P99BalancedDistributedEvidenceThresholdCertificate:
    """Exact symmetric P99 checkpoint at 95 percent global confidence.

    Every fold uses the same level ``fold_test_alpha`` rather than receiving a
    Bonferroni share of the global alpha. If q folds reject, equal fold weighting
    produces aggregate e-value q/(K*tau). The smallest q meeting the global
    threshold 1/alpha is recorded together with the exact P94/P95 per-regime
    sample threshold for level tau.
    """

    fold_count = _positive_integer(fold_count, name="fold_count")
    if fold_count < 2:
        raise ValueError("fold_count must be at least two")
    regime_count = _positive_integer(regime_count, name="regime_count")
    if (
        isinstance(dependence_range, bool)
        or not isinstance(dependence_range, int)
        or dependence_range < 0
    ):
        raise ValueError("dependence_range must be a nonnegative integer")
    fold_test_alpha = _probability(fold_test_alpha, name="fold_test_alpha")
    if fold_test_alpha > _ALPHA_95:
        raise ValueError("balanced distributed checkpoint requires fold_test_alpha <= global alpha")
    _positive_integer(series_terms, name="series_terms")

    fold_weight = Fraction(1, fold_count)
    regime_weight = Fraction(1, regime_count)
    local_alpha = fold_test_alpha * regime_weight
    target_squared = _WITNESS_RADIUS * _WITNESS_RADIUS

    ratio = Fraction(fold_count, 1) * fold_test_alpha / _ALPHA_95
    minimum_rejecting = (ratio.numerator + ratio.denominator - 1) // ratio.denominator
    if minimum_rejecting > fold_count:
        raise RuntimeError("declared fold test level cannot reach the global e-value threshold")

    def radius(sample_size: int) -> P94DependentRadiusCertificate:
        return certified_p94_dependent_squared_radius(
            sample_size=sample_size,
            dependence_range=dependence_range,
            alpha=local_alpha,
            series_terms=series_terms,
        )

    low = 1
    low_radius = radius(low)
    if low_radius.squared_radius_lower < target_squared:
        raise RuntimeError("unexpected certifying lower endpoint at sample size one")

    high = 1
    high_radius = low_radius
    while high_radius.squared_radius_upper >= target_squared:
        low = high
        low_radius = high_radius
        high *= 2
        high_radius = radius(high)

    while high - low > 1:
        mid = (low + high) // 2
        mid_radius = radius(mid)
        if mid_radius.squared_radius_upper < target_squared:
            high = mid
            high_radius = mid_radius
        elif mid_radius.squared_radius_lower >= target_squared:
            low = mid
            low_radius = mid_radius
        else:
            raise RuntimeError("log bracket is too wide to classify threshold candidate")

    exact = (
        (high + _BASE_PROFILE_SAMPLE_SIZE - 1) // _BASE_PROFILE_SAMPLE_SIZE
    ) * _BASE_PROFILE_SAMPLE_SIZE
    per_fold = regime_count * high
    exact_per_fold = regime_count * exact
    unique_total = fold_count * per_fold
    exact_unique_total = fold_count * exact_per_fold
    e_per_reject = Fraction(1, 1) / fold_test_alpha
    aggregate_at_minimum = Fraction(minimum_rejecting, fold_count) * e_per_reject
    return P99BalancedDistributedEvidenceThresholdCertificate(
        fold_count=fold_count,
        regime_count=regime_count,
        dependence_range=dependence_range,
        global_alpha=_ALPHA_95,
        fold_test_alpha=fold_test_alpha,
        equal_fold_weight=fold_weight,
        equal_regime_alpha_weight=regime_weight,
        local_alpha_budget=local_alpha,
        witness_radius=_WITNESS_RADIUS,
        minimum_rejecting_folds=minimum_rejecting,
        e_value_per_rejecting_fold=e_per_reject,
        aggregate_e_value_at_minimum_rejecting_folds=aggregate_at_minimum,
        global_rejection_e_value=Fraction(1, 1) / _ALPHA_95,
        last_noncertifying_sample_size=low,
        first_certifying_sample_size=high,
        last_radius=low_radius,
        first_radius=high_radius,
        base_profile_sample_size=_BASE_PROFILE_SAMPLE_SIZE,
        first_exact_replication_sample_size=exact,
        first_certifying_observations_per_fold=per_fold,
        first_exact_observations_per_fold=exact_per_fold,
        first_cross_fitted_unique_observations=unique_total,
        first_exact_cross_fitted_unique_observations=exact_unique_total,
    )
