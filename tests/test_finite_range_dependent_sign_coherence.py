from fractions import Fraction

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    empirical_law_from_counts,
)
from consciousness_bridge.finite_range_dependent_sign_coherence import (
    certified_p94_dependent_squared_radius,
    certify_p94_finite_range_rejection_exact,
)
from consciousness_bridge.finite_range_dependent_sign_coherence_threshold import (
    certify_p94_witness_95_threshold_exact,
)
from consciousness_bridge.localized_sign_coherence_rejection import (
    certify_p93_witness_95_threshold_exact,
)


def _witness_law() -> tuple[Fraction, ...]:
    return empirical_law_from_counts(
        (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
    )


def test_p94_m_zero_reduces_to_p93_exact_threshold():
    p93 = certify_p93_witness_95_threshold_exact()
    p94 = certify_p94_witness_95_threshold_exact(dependence_range=0)
    assert p94.color_count == 1
    assert p94.last_noncertifying_sample_size == p93.last_noncertifying_sample_size
    assert p94.first_certifying_sample_size == p93.first_certifying_sample_size
    assert p94.first_exact_replication_sample_size == p93.first_exact_replication_sample_size


def test_p94_one_dependent_exact_threshold_is_3246():
    threshold = certify_p94_witness_95_threshold_exact(dependence_range=1)
    assert threshold.color_count == 2
    assert threshold.last_noncertifying_sample_size == 3245
    assert threshold.first_certifying_sample_size == 3246
    assert threshold.first_exact_replication_sample_size == 3264
    target_squared = Fraction(1, 24) ** 2
    assert threshold.last_radius.squared_radius_lower >= target_squared
    assert threshold.first_radius.squared_radius_upper < target_squared


def test_p94_two_dependent_exact_threshold_is_4869():
    threshold = certify_p94_witness_95_threshold_exact(dependence_range=2)
    assert threshold.color_count == 3
    assert threshold.last_noncertifying_sample_size == 4868
    assert threshold.first_certifying_sample_size == 4869
    assert threshold.first_exact_replication_sample_size == 4872


def test_p94_one_dependent_exact_replication_rejects_at_n_3264():
    certificate = certify_p94_finite_range_rejection_exact(
        _witness_law(),
        sample_size=3264,
        dependence_range=1,
        alpha=Fraction(1, 20),
    )
    assert certificate.confidence_lower == Fraction(19, 20)
    assert certificate.determinants == (
        Fraction(-1, 48),
        Fraction(1, 64),
        Fraction(5, 192),
    )
    assert certificate.minimum_sign_stability_radius == Fraction(1, 24)
    assert certificate.radius.log_bracket.argument == 280
    assert certificate.radius.squared_radius_upper < Fraction(1, 24) ** 2
    assert certificate.rejects_p75


def test_p94_previous_one_dependent_replication_does_not_reject():
    certificate = certify_p94_finite_range_rejection_exact(
        _witness_law(),
        sample_size=3240,
        dependence_range=1,
        alpha=Fraction(1, 20),
    )
    assert certificate.radius.squared_radius_lower > Fraction(1, 24) ** 2
    assert not certificate.rejects_p75


def test_p94_dependence_penalty_increases_squared_radius_exactly():
    iid = certified_p94_dependent_squared_radius(
        sample_size=4800,
        dependence_range=0,
        alpha=Fraction(1, 20),
    )
    one_dependent = certified_p94_dependent_squared_radius(
        sample_size=4800,
        dependence_range=1,
        alpha=Fraction(1, 20),
    )
    assert one_dependent.squared_radius_lower == 2 * iid.squared_radius_lower
    assert one_dependent.squared_radius_upper == 2 * iid.squared_radius_upper


def test_p94_requires_sample_compatible_empirical_law():
    with pytest.raises(ValueError, match="not compatible"):
        certify_p94_finite_range_rejection_exact(
            _witness_law(),
            sample_size=3246,
            dependence_range=1,
            alpha=Fraction(1, 20),
        )


def test_p94_rejects_invalid_dependence_range_and_preserves_boundary():
    with pytest.raises(ValueError, match="nonnegative"):
        certified_p94_dependent_squared_radius(
            sample_size=100,
            dependence_range=-1,
            alpha=Fraction(1, 20),
        )
    module = __import__(
        "consciousness_bridge.finite_range_dependent_sign_coherence",
        fromlist=["dummy"],
    )
    source = (module.__doc__ or "").lower()
    assert "common marginal" in source
    assert "does not establish drift robustness" in source
    assert "does not" in source
    assert "nonphysicality" in source
    assert "physical-to-experiential bridge" in source
