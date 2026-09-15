"""P95 drift-aware stratified extension of the P94 sign-coherence gate.

P94 proves that a pooled drifting marginal can manufacture the same negative
three-minor sign pattern used to reject the P75 family. P95 therefore changes
the population target instead of pretending that a drifting stream has one
stationary marginal law.

The observation stream is partitioned into predeclared regimes. Within each
regime, observations share one regime-specific marginal law and satisfy a
declared finite-range dependence model. Different regimes may have different
marginal laws, sample sizes, and dependence ranges. No independence assumption
between regimes is required.

Each regime receives an exact rational error budget. P94 is applied locally and
a union bound controls all regime-specific confidence events simultaneously. If
at least one regime rejects P75, then the joint null that every predeclared
regime has a P75-compatible marginal law is rejected with familywise confidence
at least one minus the total allocated error budget.

Regime boundaries and error budgets must be fixed independently of the selected
P92 sign-coherence witness. Data-dependent segmentation requires separate
selection accounting and is not covered by this theorem.

P95 does not justify pooling drifting regimes, prove model acceptance under
non-rejection, identify a latent state with consciousness, establish
nonphysicality, or close the physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from consciousness_bridge.finite_range_dependent_sign_coherence import (
    P94DependentRadiusCertificate,
    P94FiniteRangeRejectionCertificate,
    certified_p94_dependent_squared_radius,
    certify_p94_finite_range_rejection_exact,
)

_WITNESS_RADIUS = Fraction(1, 24)
_ALPHA_95 = Fraction(1, 20)
_BASE_PROFILE_SAMPLE_SIZE = 24


@dataclass(frozen=True)
class P95RegimeInput:
    """One predeclared regime for the drift-aware familywise certificate."""

    name: str
    empirical_law: tuple[Fraction, ...]
    sample_size: int
    dependence_range: int
    alpha_budget: Fraction


@dataclass(frozen=True)
class P95RegimeCertificate:
    """The local P94 certificate attached to one P95 regime."""

    name: str
    alpha_budget: Fraction
    local_certificate: P94FiniteRangeRejectionCertificate


@dataclass(frozen=True)
class P95DriftAwareRejectionCertificate:
    """Familywise drift-aware rejection certificate across predeclared regimes."""

    regime_count: int
    familywise_alpha: Fraction
    allocated_alpha: Fraction
    declared_confidence_lower: Fraction
    simultaneous_confidence_lower: Fraction
    regime_certificates: tuple[P95RegimeCertificate, ...]
    rejecting_regimes: tuple[str, ...]
    rejects_joint_p75_null: bool
    conclusion: str


@dataclass(frozen=True)
class P95BalancedWitnessThresholdCertificate:
    """Exact threshold for equal error allocation across P95 regimes."""

    regime_count: int
    dependence_range: int
    familywise_alpha: Fraction
    local_alpha_budget: Fraction
    witness_radius: Fraction
    last_noncertifying_sample_size: int
    first_certifying_sample_size: int
    last_radius: P94DependentRadiusCertificate
    first_radius: P94DependentRadiusCertificate
    base_profile_sample_size: int
    first_exact_replication_sample_size: int


def _positive_integer(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def _familywise_alpha(value: Fraction) -> Fraction:
    if not isinstance(value, Fraction):
        raise TypeError("familywise_alpha must be a fractions.Fraction")
    if value <= 0 or value >= 1:
        raise ValueError("familywise_alpha must lie strictly between zero and one")
    return value


def _regime_name(value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("every regime must have a nonempty name")
    return value.strip()


def certify_p95_drift_aware_rejection_exact(
    regimes: tuple[P95RegimeInput, ...],
    *,
    familywise_alpha: Fraction,
    series_terms: int = 20,
) -> P95DriftAwareRejectionCertificate:
    """Certify the joint null that every predeclared regime belongs to P75.

    The regime-specific confidence events may be arbitrarily dependent across
    regimes. The familywise guarantee uses only the union bound.
    """

    if not isinstance(regimes, tuple) or not regimes:
        raise ValueError("regimes must be a nonempty tuple")
    familywise_alpha = _familywise_alpha(familywise_alpha)
    _positive_integer(series_terms, name="series_terms")

    names = tuple(_regime_name(regime.name) for regime in regimes)
    if len(set(names)) != len(names):
        raise ValueError("regime names must be unique")

    allocated_alpha = sum(
        (regime.alpha_budget for regime in regimes),
        Fraction(0),
    )
    if any(not isinstance(regime.alpha_budget, Fraction) for regime in regimes):
        raise TypeError("every alpha_budget must be a fractions.Fraction")
    if any(
        regime.alpha_budget <= 0 or regime.alpha_budget >= 1
        for regime in regimes
    ):
        raise ValueError("every alpha_budget must lie strictly between zero and one")
    if allocated_alpha > familywise_alpha:
        raise ValueError("allocated regime alpha budgets exceed familywise_alpha")

    certificates: list[P95RegimeCertificate] = []
    for name, regime in zip(names, regimes, strict=True):
        local = certify_p94_finite_range_rejection_exact(
            regime.empirical_law,
            sample_size=regime.sample_size,
            dependence_range=regime.dependence_range,
            alpha=regime.alpha_budget,
            series_terms=series_terms,
        )
        certificates.append(
            P95RegimeCertificate(
                name=name,
                alpha_budget=regime.alpha_budget,
                local_certificate=local,
            )
        )

    certificate_tuple = tuple(certificates)
    rejecting = tuple(
        certificate.name
        for certificate in certificate_tuple
        if certificate.local_certificate.rejects_p75
    )
    rejects = bool(rejecting)
    return P95DriftAwareRejectionCertificate(
        regime_count=len(regimes),
        familywise_alpha=familywise_alpha,
        allocated_alpha=allocated_alpha,
        declared_confidence_lower=1 - familywise_alpha,
        simultaneous_confidence_lower=1 - allocated_alpha,
        regime_certificates=certificate_tuple,
        rejecting_regimes=rejecting,
        rejects_joint_p75_null=rejects,
        conclusion=(
            "Joint P75 null rejected: at least one predeclared regime is outside P75 under its declared within-regime model"
            if rejects
            else "Joint P75 null not rejected by the P95 stratified certificate"
        ),
    )


def certify_p95_balanced_witness_95_threshold_exact(
    *,
    regime_count: int,
    dependence_range: int,
    series_terms: int = 20,
) -> P95BalancedWitnessThresholdCertificate:
    """Locate the first local sample size clearing the P92 witness at 95 percent.

    The total familywise failure budget is 0.05 and is split equally across the
    declared regimes. The local P94 radius is therefore evaluated at
    alpha_b = 0.05 / regime_count.
    """

    regime_count = _positive_integer(regime_count, name="regime_count")
    if (
        isinstance(dependence_range, bool)
        or not isinstance(dependence_range, int)
        or dependence_range < 0
    ):
        raise ValueError("dependence_range must be a nonnegative integer")
    _positive_integer(series_terms, name="series_terms")

    local_alpha = _ALPHA_95 / regime_count
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

    first_replication = (
        (high + _BASE_PROFILE_SAMPLE_SIZE - 1) // _BASE_PROFILE_SAMPLE_SIZE
    ) * _BASE_PROFILE_SAMPLE_SIZE
    return P95BalancedWitnessThresholdCertificate(
        regime_count=regime_count,
        dependence_range=dependence_range,
        familywise_alpha=_ALPHA_95,
        local_alpha_budget=local_alpha,
        witness_radius=_WITNESS_RADIUS,
        last_noncertifying_sample_size=low,
        first_certifying_sample_size=high,
        last_radius=low_radius,
        first_radius=high_radius,
        base_profile_sample_size=_BASE_PROFILE_SAMPLE_SIZE,
        first_exact_replication_sample_size=first_replication,
    )
