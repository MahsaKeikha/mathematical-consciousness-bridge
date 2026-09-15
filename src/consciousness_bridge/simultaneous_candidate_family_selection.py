"""P97 same-data selection-valid certification over a finite candidate family.

P96 permits arbitrarily complicated pilot selection without an extra alpha
penalty when selection information is separated from independent holdout
certification. P97 treats the complementary case in which the same data may be
used to compare and select among a finite family of candidate regime plans.

The candidate family itself, including every candidate's regime definitions,
dependence ranges, and error budgets, must be fixed before the certification
statistics are inspected. Each candidate receives a familywise error budget and
is certified with P95. A second union bound across candidates gives a
simultaneous event on which every candidate certificate is valid. Therefore an
arbitrary data-dependent rule may select one of those already certified
candidates after inspection without invalidating the selected certificate.

Unlike P96, P97 pays an explicit multiplicity cost for same-data selection. It
does not validate an unbounded or newly generated post-inspection candidate,
unknown within-regime drift, misspecified dependence ranges, model acceptance
under non-rejection, consciousness identification, nonphysicality, or a
completed physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from consciousness_bridge.drift_aware_stratified_sign_coherence import (
    P95DriftAwareRejectionCertificate,
    P95RegimeInput,
    certify_p95_drift_aware_rejection_exact,
)
from consciousness_bridge.finite_range_dependent_sign_coherence import (
    P94DependentRadiusCertificate,
    certified_p94_dependent_squared_radius,
)

_ALPHA_95 = Fraction(1, 20)
_WITNESS_RADIUS = Fraction(1, 24)
_BASE_PROFILE_SAMPLE_SIZE = 24


@dataclass(frozen=True)
class P97CandidatePlan:
    """One member of the finite candidate family fixed before inspection."""

    name: str
    description: str
    familywise_alpha: Fraction
    regimes: tuple[P95RegimeInput, ...]


@dataclass(frozen=True)
class P97CandidateCertificate:
    """Nested P95 certificate for one predeclared candidate plan."""

    name: str
    familywise_alpha: Fraction
    nested_p95_certificate: P95DriftAwareRejectionCertificate


@dataclass(frozen=True)
class P97SameDataSelectionCertificate:
    """Simultaneous certificate supporting post-inspection candidate selection."""

    candidate_count: int
    global_alpha: Fraction
    allocated_candidate_alpha: Fraction
    simultaneous_confidence_lower: Fraction
    candidate_certificates: tuple[P97CandidateCertificate, ...]
    selected_candidate_name: str
    rejecting_candidates: tuple[str, ...]
    rejects_selected_joint_p75_null: bool
    conclusion: str


@dataclass(frozen=True)
class P97BalancedCandidateThresholdCertificate:
    """Exact balanced threshold for finite same-data candidate-family selection."""

    candidate_count: int
    regime_count: int
    dependence_range: int
    global_alpha: Fraction
    candidate_alpha_budget: Fraction
    local_alpha_budget: Fraction
    witness_radius: Fraction
    last_noncertifying_sample_size: int
    first_certifying_sample_size: int
    last_radius: P94DependentRadiusCertificate
    first_radius: P94DependentRadiusCertificate
    base_profile_sample_size: int
    first_exact_replication_sample_size: int
    first_balanced_dataset_observations: int
    first_exact_balanced_dataset_observations: int


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


def certify_p97_same_data_candidate_family_exact(
    candidates: tuple[P97CandidatePlan, ...],
    *,
    global_alpha: Fraction,
    selected_candidate_name: str,
    candidate_family_predeclared: bool,
    series_terms: int = 20,
) -> P97SameDataSelectionCertificate:
    """Certify arbitrary post-inspection selection from a fixed finite family.

    Candidate certificates may be arbitrarily dependent because they may reuse
    exactly the same observations. The guarantee uses a union bound first
    within each P95 candidate and then across the finite candidate family.
    """

    if candidate_family_predeclared is not True:
        raise ValueError("candidate family must be fixed before certification statistics are inspected")
    if not isinstance(candidates, tuple) or not candidates:
        raise ValueError("candidates must be a nonempty tuple")
    global_alpha = _alpha(global_alpha, name="global_alpha")
    selected_candidate_name = _nonempty_text(
        selected_candidate_name,
        name="selected_candidate_name",
    )
    _positive_integer(series_terms, name="series_terms")

    names: list[str] = []
    allocated = Fraction(0)
    for candidate in candidates:
        if not isinstance(candidate, P97CandidatePlan):
            raise TypeError("every candidate must be a P97CandidatePlan")
        names.append(_nonempty_text(candidate.name, name="candidate name"))
        _nonempty_text(candidate.description, name="candidate description")
        allocated += _alpha(candidate.familywise_alpha, name="candidate familywise_alpha")
        if not isinstance(candidate.regimes, tuple) or not candidate.regimes:
            raise ValueError("every candidate must contain a nonempty regime tuple")

    if len(set(names)) != len(names):
        raise ValueError("candidate names must be unique")
    if selected_candidate_name not in set(names):
        raise ValueError("selected_candidate_name must name a predeclared candidate")
    if allocated > global_alpha:
        raise ValueError("allocated candidate alpha budgets exceed global_alpha")

    certificates: list[P97CandidateCertificate] = []
    for name, candidate in zip(names, candidates, strict=True):
        nested = certify_p95_drift_aware_rejection_exact(
            candidate.regimes,
            familywise_alpha=candidate.familywise_alpha,
            series_terms=series_terms,
        )
        certificates.append(
            P97CandidateCertificate(
                name=name,
                familywise_alpha=candidate.familywise_alpha,
                nested_p95_certificate=nested,
            )
        )

    certificate_tuple = tuple(certificates)
    by_name = {certificate.name: certificate for certificate in certificate_tuple}
    selected = by_name[selected_candidate_name]
    rejecting = tuple(
        certificate.name
        for certificate in certificate_tuple
        if certificate.nested_p95_certificate.rejects_joint_p75_null
    )
    rejects_selected = selected.nested_p95_certificate.rejects_joint_p75_null
    return P97SameDataSelectionCertificate(
        candidate_count=len(candidates),
        global_alpha=global_alpha,
        allocated_candidate_alpha=allocated,
        simultaneous_confidence_lower=1 - allocated,
        candidate_certificates=certificate_tuple,
        selected_candidate_name=selected_candidate_name,
        rejecting_candidates=rejecting,
        rejects_selected_joint_p75_null=rejects_selected,
        conclusion=(
            "Selected candidate joint P75 null rejected under simultaneous finite-family accounting"
            if rejects_selected
            else "Selected candidate joint P75 null not rejected by the simultaneous finite-family certificate"
        ),
    )


def certify_p97_balanced_candidate_family_95_threshold_exact(
    *,
    candidate_count: int,
    regime_count: int,
    dependence_range: int,
    series_terms: int = 20,
) -> P97BalancedCandidateThresholdCertificate:
    """Locate the exact balanced threshold under equal candidate/regime spending.

    At global alpha 0.05, equal spending gives candidate alpha
    ``0.05 / candidate_count`` and local regime alpha
    ``0.05 / (candidate_count * regime_count)``. Candidate plans reuse the same
    underlying dataset, so balanced unique-observation accounting multiplies the
    per-regime threshold by ``regime_count`` rather than by candidate count.
    """

    candidate_count = _positive_integer(candidate_count, name="candidate_count")
    regime_count = _positive_integer(regime_count, name="regime_count")
    if (
        isinstance(dependence_range, bool)
        or not isinstance(dependence_range, int)
        or dependence_range < 0
    ):
        raise ValueError("dependence_range must be a nonnegative integer")
    _positive_integer(series_terms, name="series_terms")

    candidate_alpha = _ALPHA_95 / candidate_count
    local_alpha = candidate_alpha / regime_count
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
    return P97BalancedCandidateThresholdCertificate(
        candidate_count=candidate_count,
        regime_count=regime_count,
        dependence_range=dependence_range,
        global_alpha=_ALPHA_95,
        candidate_alpha_budget=candidate_alpha,
        local_alpha_budget=local_alpha,
        witness_radius=_WITNESS_RADIUS,
        last_noncertifying_sample_size=low,
        first_certifying_sample_size=high,
        last_radius=low_radius,
        first_radius=high_radius,
        base_profile_sample_size=_BASE_PROFILE_SAMPLE_SIZE,
        first_exact_replication_sample_size=exact,
        first_balanced_dataset_observations=regime_count * high,
        first_exact_balanced_dataset_observations=regime_count * exact,
    )
