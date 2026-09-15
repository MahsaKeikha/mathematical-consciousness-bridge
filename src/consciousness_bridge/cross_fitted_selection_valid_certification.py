"""P98 cross-fitted selection-valid certification over independent data blocks.

P96 permits an arbitrarily complicated pilot-selected regime plan to be certified
without an additional selection-complexity penalty when the certification data
are independent of the information used to select the plan. Its cost is that a
dedicated holdout block is not itself used for selection.

P98 rotates that separation across a finite collection of mutually independent
data blocks. For fold k, the regime plan may be chosen by an arbitrary procedure
using only the other blocks. The plan is frozen before the kth certification
block is inspected, and P96 is then applied to that held-out block. A union bound
across fold-level error budgets gives one simultaneous event on which every
cross-fitted certificate is valid. The fold certificates need not be independent:
their selection information overlaps heavily by construction.

Thus every independent block may serve once as certification data and elsewhere
as selection information. Cross-fitting does not remove multiplicity across the
rotated certification statements: if several fold certificates are to remain
available for post-inspection selection, their fold-level budgets must sum to the
declared global error budget.

P98 does not validate ordinary leave-one-segment-out reuse of one dependent time
series, leakage of a fold's certification statistics into its own plan selection,
within-regime drift beyond the declared P95 model, misspecified dependence ranges,
model acceptance under non-rejection, consciousness identification,
nonphysicality, or a completed physical-to-experiential bridge.
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
class P98CrossFitFoldInput:
    """One rotated certification fold and its independently selected plan."""

    name: str
    selection_description: str
    selection_information_sample_size: int
    selected_regimes: tuple[P96SelectedRegimeDesign, ...]
    certification_data: tuple[P96HoldoutRegimeData, ...]
    fold_alpha: Fraction
    plan_frozen_before_own_block_evaluation: bool


@dataclass(frozen=True)
class P98FoldCertificate:
    """One nested P96 certificate inside the cross-fitted simultaneous event."""

    name: str
    fold_alpha: Fraction
    selection_information_sample_size: int
    certification_observations: int
    nested_p96_certificate: P96SelectionValidRejectionCertificate


@dataclass(frozen=True)
class P98CrossFittedRejectionCertificate:
    """Simultaneous selection-valid certificate across rotated holdout folds."""

    fold_count: int
    global_alpha: Fraction
    allocated_fold_alpha: Fraction
    simultaneous_confidence_lower: Fraction
    fold_certificates: tuple[P98FoldCertificate, ...]
    selected_fold_name: str
    rejecting_folds: tuple[str, ...]
    rejects_selected_joint_p75_null: bool
    rejects_cross_fitted_joint_p75_null: bool
    conclusion: str


@dataclass(frozen=True)
class P98BalancedCrossFitThresholdCertificate:
    """Exact 95 percent checkpoint for equal fold and regime spending."""

    fold_count: int
    regime_count: int
    dependence_range: int
    global_alpha: Fraction
    fold_alpha_budget: Fraction
    local_alpha_budget: Fraction
    witness_radius: Fraction
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
    selection_information_observations_per_fold_at_threshold: int
    exact_selection_information_observations_per_fold: int


def _positive_integer(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def _nonempty_text(value: str, *, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a nonempty string")
    return value.strip()


def _alpha(value: Fraction, *, name: str) -> Fraction:
    if not isinstance(value, Fraction):
        raise TypeError(f"{name} must be a fractions.Fraction")
    if value <= 0 or value >= 1:
        raise ValueError(f"{name} must lie strictly between zero and one")
    return value


def certify_p98_cross_fitted_rejection_exact(
    folds: tuple[P98CrossFitFoldInput, ...],
    *,
    global_alpha: Fraction,
    selected_fold_name: str,
    certification_blocks_mutually_independent: bool,
    own_block_excluded_from_selection: bool,
    series_terms: int = 20,
) -> P98CrossFittedRejectionCertificate:
    """Certify rotated sample splitting with arbitrary leave-one-block-out selection.

    Mutual independence of the certification blocks plus exclusion of block k
    from the information used to select fold k imply the P96 selection/holdout
    independence required for each fold. Fold certificates may nevertheless be
    dependent because their selection information overlaps. The outer guarantee
    therefore uses only a union bound across the exact fold-level budgets.
    """

    if certification_blocks_mutually_independent is not True:
        raise ValueError("cross-fitted certification blocks must be mutually independent")
    if own_block_excluded_from_selection is not True:
        raise ValueError("each fold must exclude its own certification block from plan selection")
    if not isinstance(folds, tuple) or not folds:
        raise ValueError("folds must be a nonempty tuple")
    global_alpha = _alpha(global_alpha, name="global_alpha")
    selected_fold_name = _nonempty_text(selected_fold_name, name="selected_fold_name")
    _positive_integer(series_terms, name="series_terms")

    names: list[str] = []
    allocated = Fraction(0)
    for fold in folds:
        if not isinstance(fold, P98CrossFitFoldInput):
            raise TypeError("every fold must be a P98CrossFitFoldInput")
        names.append(_nonempty_text(fold.name, name="fold name"))
        _nonempty_text(fold.selection_description, name="selection_description")
        _positive_integer(
            fold.selection_information_sample_size,
            name="selection_information_sample_size",
        )
        if not isinstance(fold.selected_regimes, tuple) or not fold.selected_regimes:
            raise ValueError("every fold must contain a nonempty selected_regimes tuple")
        if not isinstance(fold.certification_data, tuple) or not fold.certification_data:
            raise ValueError("every fold must contain nonempty certification_data")
        if fold.plan_frozen_before_own_block_evaluation is not True:
            raise ValueError("every fold plan must be frozen before its own certification block is evaluated")
        allocated += _alpha(fold.fold_alpha, name="fold_alpha")

    if len(set(names)) != len(names):
        raise ValueError("fold names must be unique")
    if selected_fold_name not in set(names):
        raise ValueError("selected_fold_name must name one of the declared folds")
    if allocated > global_alpha:
        raise ValueError("allocated fold alpha budgets exceed global_alpha")

    certificates: list[P98FoldCertificate] = []
    for name, fold in zip(names, folds, strict=True):
        plan = P96PilotSelectionPlan(
            selection_description=fold.selection_description.strip(),
            pilot_sample_size=fold.selection_information_sample_size,
            selected_regimes=fold.selected_regimes,
            familywise_alpha=fold.fold_alpha,
            pilot_holdout_independent=True,
            plan_frozen_before_holdout_evaluation=True,
        )
        nested = certify_p96_selection_valid_holdout_rejection_exact(
            plan,
            fold.certification_data,
            series_terms=series_terms,
        )
        certification_observations = sum(
            data.sample_size for data in fold.certification_data
        )
        certificates.append(
            P98FoldCertificate(
                name=name,
                fold_alpha=fold.fold_alpha,
                selection_information_sample_size=fold.selection_information_sample_size,
                certification_observations=certification_observations,
                nested_p96_certificate=nested,
            )
        )

    certificate_tuple = tuple(certificates)
    by_name = {certificate.name: certificate for certificate in certificate_tuple}
    selected = by_name[selected_fold_name]
    rejecting = tuple(
        certificate.name
        for certificate in certificate_tuple
        if certificate.nested_p96_certificate.rejects_joint_p75_null
    )
    rejects_selected = selected.nested_p96_certificate.rejects_joint_p75_null
    rejects_any = bool(rejecting)
    return P98CrossFittedRejectionCertificate(
        fold_count=len(folds),
        global_alpha=global_alpha,
        allocated_fold_alpha=allocated,
        simultaneous_confidence_lower=1 - allocated,
        fold_certificates=certificate_tuple,
        selected_fold_name=selected_fold_name,
        rejecting_folds=rejecting,
        rejects_selected_joint_p75_null=rejects_selected,
        rejects_cross_fitted_joint_p75_null=rejects_any,
        conclusion=(
            "Selected cross-fitted fold rejects its pilot-selected joint P75 null under simultaneous fold accounting"
            if rejects_selected
            else "Selected cross-fitted fold does not reject its pilot-selected joint P75 null"
        ),
    )


def certify_p98_balanced_cross_fit_95_threshold_exact(
    *,
    fold_count: int,
    regime_count: int,
    dependence_range: int,
    series_terms: int = 20,
) -> P98BalancedCrossFitThresholdCertificate:
    """Locate the exact balanced P98 threshold at 95 percent global confidence.

    Equal fold spending gives alpha/K to each rotated certification block, and
    equal regime spending inside a fold gives alpha/(K B) locally. Unlike P97,
    the fold count does multiply the unique observation total because each fold
    is a different certification block. Those same observations are reused as
    selection information for the other folds and are therefore not counted a
    second time.
    """

    fold_count = _positive_integer(fold_count, name="fold_count")
    if fold_count < 2:
        raise ValueError("fold_count must be at least two for cross-fitting")
    regime_count = _positive_integer(regime_count, name="regime_count")
    if (
        isinstance(dependence_range, bool)
        or not isinstance(dependence_range, int)
        or dependence_range < 0
    ):
        raise ValueError("dependence_range must be a nonnegative integer")
    _positive_integer(series_terms, name="series_terms")

    fold_alpha = _ALPHA_95 / fold_count
    local_alpha = fold_alpha / regime_count
    target_squared = _WITNESS_RADIUS * _WITNESS_RADIUS

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
    return P98BalancedCrossFitThresholdCertificate(
        fold_count=fold_count,
        regime_count=regime_count,
        dependence_range=dependence_range,
        global_alpha=_ALPHA_95,
        fold_alpha_budget=fold_alpha,
        local_alpha_budget=local_alpha,
        witness_radius=_WITNESS_RADIUS,
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
        selection_information_observations_per_fold_at_threshold=(fold_count - 1) * per_fold,
        exact_selection_information_observations_per_fold=(fold_count - 1) * exact_per_fold,
    )
