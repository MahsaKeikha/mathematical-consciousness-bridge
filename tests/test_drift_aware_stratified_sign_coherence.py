from fractions import Fraction

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    empirical_law_from_counts,
)
from consciousness_bridge.drift_aware_stratified_sign_coherence import (
    P95RegimeInput,
    certify_p95_balanced_witness_95_threshold_exact,
    certify_p95_drift_aware_rejection_exact,
)


def _witness_law() -> tuple[Fraction, ...]:
    return empirical_law_from_counts(
        (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
    )


def _point_mass_law() -> tuple[Fraction, ...]:
    return (Fraction(1),) + (Fraction(0),) * 15


def test_p95_single_regime_reduces_to_p94_familywise_threshold():
    threshold = certify_p95_balanced_witness_95_threshold_exact(
        regime_count=1,
        dependence_range=1,
    )
    assert threshold.local_alpha_budget == Fraction(1, 20)
    assert threshold.last_noncertifying_sample_size == 3245
    assert threshold.first_certifying_sample_size == 3246
    assert threshold.first_exact_replication_sample_size == 3264


def test_p95_two_regime_balanced_threshold_is_3645():
    threshold = certify_p95_balanced_witness_95_threshold_exact(
        regime_count=2,
        dependence_range=1,
    )
    assert threshold.local_alpha_budget == Fraction(1, 40)
    assert threshold.last_noncertifying_sample_size == 3644
    assert threshold.first_certifying_sample_size == 3645
    assert threshold.first_exact_replication_sample_size == 3648
    target_squared = Fraction(1, 24) ** 2
    assert threshold.last_radius.squared_radius_lower >= target_squared
    assert threshold.first_radius.squared_radius_upper < target_squared


def test_p95_rejects_joint_null_when_one_predeclared_regime_rejects():
    certificate = certify_p95_drift_aware_rejection_exact(
        (
            P95RegimeInput(
                name="witness",
                empirical_law=_witness_law(),
                sample_size=3648,
                dependence_range=1,
                alpha_budget=Fraction(1, 40),
            ),
            P95RegimeInput(
                name="compatible-control",
                empirical_law=_point_mass_law(),
                sample_size=3648,
                dependence_range=1,
                alpha_budget=Fraction(1, 40),
            ),
        ),
        familywise_alpha=Fraction(1, 20),
    )
    assert certificate.regime_count == 2
    assert certificate.allocated_alpha == Fraction(1, 20)
    assert certificate.declared_confidence_lower == Fraction(19, 20)
    assert certificate.simultaneous_confidence_lower == Fraction(19, 20)
    assert certificate.rejecting_regimes == ("witness",)
    assert certificate.rejects_joint_p75_null
    assert certificate.regime_certificates[0].local_certificate.rejects_p75
    assert not certificate.regime_certificates[1].local_certificate.rejects_p75


def test_p95_allows_unequal_regime_budgets_and_stronger_actual_confidence():
    certificate = certify_p95_drift_aware_rejection_exact(
        (
            P95RegimeInput(
                name="a",
                empirical_law=_point_mass_law(),
                sample_size=100,
                dependence_range=0,
                alpha_budget=Fraction(1, 100),
            ),
            P95RegimeInput(
                name="b",
                empirical_law=_point_mass_law(),
                sample_size=100,
                dependence_range=2,
                alpha_budget=Fraction(1, 100),
            ),
        ),
        familywise_alpha=Fraction(1, 20),
    )
    assert certificate.allocated_alpha == Fraction(1, 50)
    assert certificate.simultaneous_confidence_lower == Fraction(49, 50)
    assert certificate.declared_confidence_lower == Fraction(19, 20)
    assert not certificate.rejects_joint_p75_null


def test_p95_rejects_alpha_overspend_duplicate_names_and_empty_regimes():
    with pytest.raises(ValueError, match="nonempty"):
        certify_p95_drift_aware_rejection_exact(
            (),
            familywise_alpha=Fraction(1, 20),
        )

    duplicate = P95RegimeInput(
        name="same",
        empirical_law=_point_mass_law(),
        sample_size=100,
        dependence_range=0,
        alpha_budget=Fraction(1, 40),
    )
    with pytest.raises(ValueError, match="unique"):
        certify_p95_drift_aware_rejection_exact(
            (duplicate, duplicate),
            familywise_alpha=Fraction(1, 20),
        )

    with pytest.raises(ValueError, match="exceed"):
        certify_p95_drift_aware_rejection_exact(
            (
                P95RegimeInput(
                    name="a",
                    empirical_law=_point_mass_law(),
                    sample_size=100,
                    dependence_range=0,
                    alpha_budget=Fraction(3, 100),
                ),
                P95RegimeInput(
                    name="b",
                    empirical_law=_point_mass_law(),
                    sample_size=100,
                    dependence_range=0,
                    alpha_budget=Fraction(3, 100),
                ),
            ),
            familywise_alpha=Fraction(1, 20),
        )


def test_p95_preserves_scientific_boundary_in_module_docstring():
    module = __import__(
        "consciousness_bridge.drift_aware_stratified_sign_coherence",
        fromlist=["dummy"],
    )
    source = (module.__doc__ or "").lower()
    assert "predeclared regimes" in source
    assert "does not justify pooling" in source
    assert "data-dependent segmentation" in source
    assert "nonphysicality" in source
    assert "physical-to-experiential bridge" in source
