"""P96 selection-valid holdout extension of P95 stratified rejection.

P95 permits arbitrary marginal drift across predeclared regimes, but its regime
boundaries and error budgets must be fixed independently of the certification
witness. P96 closes one precise post-selection gap by separating selection from
certification.

An arbitrary pilot-data procedure may choose the number of regimes, regime
definitions, declared within-regime dependence ranges, and exact rational error
budgets. The resulting plan is then frozen. A separate certification sample,
independent of the pilot-selection information, is evaluated with the P95
regime-wise certificate. Conditional on the pilot information, the selected
plan is fixed, so the P95 familywise guarantee applies conditionally. Taking an
expectation over the pilot information preserves the same unconditional error
bound. No additional alpha penalty is required for the complexity of the pilot
selection rule itself.

This zero extra selection penalty is paid for by data separation: pilot data
are not reused as certification data. The certification observations must still
satisfy the selected regime-specific P94 assumptions, including a common
marginal law inside each selected regime and the declared finite dependence
range. Ordinary splitting of one dependent time series is not automatically an
independent holdout design.

P96 does not validate reuse of certification observations for segmentation,
unknown within-regime drift, misspecified dependence ranges, model acceptance
under non-rejection, consciousness identification, nonphysicality, or a
completed physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from consciousness_bridge.drift_aware_stratified_sign_coherence import (
    P95BalancedWitnessThresholdCertificate,
    P95DriftAwareRejectionCertificate,
    P95RegimeInput,
    certify_p95_balanced_witness_95_threshold_exact,
    certify_p95_drift_aware_rejection_exact,
)


@dataclass(frozen=True)
class P96SelectedRegimeDesign:
    """One regime design chosen using pilot information only."""

    name: str
    regime_definition: str
    dependence_range: int
    alpha_budget: Fraction


@dataclass(frozen=True)
class P96PilotSelectionPlan:
    """A pilot-selected plan that must be frozen before holdout evaluation."""

    selection_description: str
    pilot_sample_size: int
    selected_regimes: tuple[P96SelectedRegimeDesign, ...]
    familywise_alpha: Fraction
    pilot_holdout_independent: bool
    plan_frozen_before_holdout_evaluation: bool


@dataclass(frozen=True)
class P96HoldoutRegimeData:
    """Certification data for one selected regime."""

    name: str
    empirical_law: tuple[Fraction, ...]
    sample_size: int


@dataclass(frozen=True)
class P96SelectionValidRejectionCertificate:
    """Selection-valid P96 certificate with the nested P95 holdout audit."""

    selection_description: str
    pilot_sample_size: int
    selected_regime_count: int
    selection_complexity_alpha_penalty: Fraction
    declared_familywise_alpha: Fraction
    nested_p95_certificate: P95DriftAwareRejectionCertificate
    rejecting_regimes: tuple[str, ...]
    rejects_joint_p75_null: bool
    conclusion: str


@dataclass(frozen=True)
class P96BalancedHoldoutThresholdCertificate:
    """Bookkeeping for a balanced P96 holdout design at 95 percent confidence."""

    pilot_sample_size: int
    regime_count: int
    dependence_range: int
    holdout_threshold: P95BalancedWitnessThresholdCertificate
    first_certifying_holdout_observations: int
    first_exact_replication_holdout_observations: int
    first_certifying_total_observations: int
    first_exact_replication_total_observations: int


def _nonempty_text(value: str, *, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a nonempty string")
    return value.strip()


def _positive_integer(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def _validate_plan(plan: P96PilotSelectionPlan) -> None:
    if not isinstance(plan, P96PilotSelectionPlan):
        raise TypeError("plan must be a P96PilotSelectionPlan")
    _nonempty_text(plan.selection_description, name="selection_description")
    _positive_integer(plan.pilot_sample_size, name="pilot_sample_size")
    if not isinstance(plan.selected_regimes, tuple) or not plan.selected_regimes:
        raise ValueError("selected_regimes must be a nonempty tuple")
    if not isinstance(plan.familywise_alpha, Fraction):
        raise TypeError("familywise_alpha must be a fractions.Fraction")
    if plan.familywise_alpha <= 0 or plan.familywise_alpha >= 1:
        raise ValueError("familywise_alpha must lie strictly between zero and one")
    if plan.pilot_holdout_independent is not True:
        raise ValueError("pilot and holdout information must be declared independent")
    if plan.plan_frozen_before_holdout_evaluation is not True:
        raise ValueError("pilot-selected plan must be frozen before holdout evaluation")

    names: list[str] = []
    allocated = Fraction(0)
    for design in plan.selected_regimes:
        if not isinstance(design, P96SelectedRegimeDesign):
            raise TypeError("every selected regime must be a P96SelectedRegimeDesign")
        names.append(_nonempty_text(design.name, name="regime name"))
        _nonempty_text(design.regime_definition, name="regime_definition")
        if (
            isinstance(design.dependence_range, bool)
            or not isinstance(design.dependence_range, int)
            or design.dependence_range < 0
        ):
            raise ValueError("dependence_range must be a nonnegative integer")
        if not isinstance(design.alpha_budget, Fraction):
            raise TypeError("every alpha_budget must be a fractions.Fraction")
        if design.alpha_budget <= 0 or design.alpha_budget >= 1:
            raise ValueError("every alpha_budget must lie strictly between zero and one")
        allocated += design.alpha_budget

    if len(set(names)) != len(names):
        raise ValueError("selected regime names must be unique")
    if allocated > plan.familywise_alpha:
        raise ValueError("selected regime alpha budgets exceed familywise_alpha")


def certify_p96_selection_valid_holdout_rejection_exact(
    plan: P96PilotSelectionPlan,
    holdout_data: tuple[P96HoldoutRegimeData, ...],
    *,
    series_terms: int = 20,
) -> P96SelectionValidRejectionCertificate:
    """Certify a pilot-selected regime plan on independent holdout data.

    Conditional on the pilot-selection information, ``plan`` is fixed. The
    function therefore applies P95 exactly to the holdout sample. Under the
    declared pilot-holdout independence and conditional P94 assumptions, the
    conditional familywise error bound integrates to the same unconditional
    bound.
    """

    _validate_plan(plan)
    _positive_integer(series_terms, name="series_terms")
    if not isinstance(holdout_data, tuple) or not holdout_data:
        raise ValueError("holdout_data must be a nonempty tuple")

    by_name: dict[str, P96HoldoutRegimeData] = {}
    for data in holdout_data:
        if not isinstance(data, P96HoldoutRegimeData):
            raise TypeError("every holdout item must be a P96HoldoutRegimeData")
        name = _nonempty_text(data.name, name="holdout regime name")
        if name in by_name:
            raise ValueError("holdout regime names must be unique")
        _positive_integer(data.sample_size, name="holdout sample_size")
        by_name[name] = data

    selected_names = tuple(design.name.strip() for design in plan.selected_regimes)
    if set(by_name) != set(selected_names):
        raise ValueError("holdout regime names must match the pilot-selected regime names")

    p95_inputs = tuple(
        P95RegimeInput(
            name=design.name.strip(),
            empirical_law=by_name[design.name.strip()].empirical_law,
            sample_size=by_name[design.name.strip()].sample_size,
            dependence_range=design.dependence_range,
            alpha_budget=design.alpha_budget,
        )
        for design in plan.selected_regimes
    )
    nested = certify_p95_drift_aware_rejection_exact(
        p95_inputs,
        familywise_alpha=plan.familywise_alpha,
        series_terms=series_terms,
    )
    return P96SelectionValidRejectionCertificate(
        selection_description=plan.selection_description.strip(),
        pilot_sample_size=plan.pilot_sample_size,
        selected_regime_count=len(plan.selected_regimes),
        selection_complexity_alpha_penalty=Fraction(0),
        declared_familywise_alpha=plan.familywise_alpha,
        nested_p95_certificate=nested,
        rejecting_regimes=nested.rejecting_regimes,
        rejects_joint_p75_null=nested.rejects_joint_p75_null,
        conclusion=(
            "Pilot-selected joint P75 null rejected on independent holdout data"
            if nested.rejects_joint_p75_null
            else "Pilot-selected joint P75 null not rejected by the independent holdout certificate"
        ),
    )


def certify_p96_balanced_holdout_95_threshold_exact(
    *,
    pilot_sample_size: int,
    regime_count: int,
    dependence_range: int,
    series_terms: int = 20,
) -> P96BalancedHoldoutThresholdCertificate:
    """Report holdout and total sample accounting for the balanced P95 gate.

    Pilot selection complexity does not alter the holdout alpha threshold under
    independence. Pilot observations remain an additional sample cost and are
    not counted toward the certification sample size.
    """

    pilot_sample_size = _positive_integer(
        pilot_sample_size,
        name="pilot_sample_size",
    )
    threshold = certify_p95_balanced_witness_95_threshold_exact(
        regime_count=regime_count,
        dependence_range=dependence_range,
        series_terms=series_terms,
    )
    first_holdout = regime_count * threshold.first_certifying_sample_size
    exact_holdout = regime_count * threshold.first_exact_replication_sample_size
    return P96BalancedHoldoutThresholdCertificate(
        pilot_sample_size=pilot_sample_size,
        regime_count=regime_count,
        dependence_range=dependence_range,
        holdout_threshold=threshold,
        first_certifying_holdout_observations=first_holdout,
        first_exact_replication_holdout_observations=exact_holdout,
        first_certifying_total_observations=pilot_sample_size + first_holdout,
        first_exact_replication_total_observations=pilot_sample_size + exact_holdout,
    )
