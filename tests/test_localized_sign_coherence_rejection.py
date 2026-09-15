from fractions import Fraction

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    empirical_law_from_counts,
)
from consciousness_bridge.localized_sign_coherence_rejection import (
    certify_p93_localized_rejection_exact,
    certify_p93_witness_95_threshold_exact,
)


def _witness_law() -> tuple[Fraction, ...]:
    return empirical_law_from_counts(
        (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
    )


def test_p93_replicated_witness_rejects_at_n_1632_with_95_percent_confidence():
    certificate = certify_p93_localized_rejection_exact(
        _witness_law(),
        sample_size=1632,
        alpha=Fraction(1, 20),
    )
    assert certificate.selected_cell_count == 7
    assert certificate.confidence_lower == Fraction(19, 20)
    assert certificate.determinants == (
        Fraction(-1, 48),
        Fraction(1, 64),
        Fraction(5, 192),
    )
    assert certificate.sign_stability_radii == (
        Fraction(1, 24),
        Fraction(3, 56),
        Fraction(5, 72),
    )
    assert certificate.minimum_sign_stability_radius == Fraction(1, 24)
    assert certificate.determinant_product == Fraction(-5, 589824)
    assert certificate.sampling_radius.log_argument == 280
    assert certificate.sampling_radius.cell_linf_radius_upper < Fraction(1, 24)
    assert certificate.rejects_p75


def test_p93_previous_exact_replication_n_1608_does_not_clear_radius():
    certificate = certify_p93_localized_rejection_exact(
        _witness_law(),
        sample_size=1608,
        alpha=Fraction(1, 20),
    )
    assert certificate.minimum_sign_stability_radius == Fraction(1, 24)
    assert certificate.sampling_radius.cell_linf_radius_upper > Fraction(1, 24)
    assert not certificate.rejects_p75


def test_p93_exact_95_percent_integer_threshold_is_1623():
    threshold = certify_p93_witness_95_threshold_exact()
    assert threshold.alpha == Fraction(1, 20)
    assert threshold.witness_radius == Fraction(1, 24)
    assert threshold.last_noncertifying_sample_size == 1622
    assert threshold.first_certifying_sample_size == 1623
    assert threshold.last_radius.log_argument == 280
    assert threshold.first_radius.log_argument == 280
    assert threshold.last_radius.cell_linf_radius_lower > Fraction(1, 24)
    assert threshold.first_radius.cell_linf_radius_upper < Fraction(1, 24)


def test_p93_first_exact_replication_is_68_times_the_original_profile():
    threshold = certify_p93_witness_95_threshold_exact()
    assert threshold.base_profile_sample_size == 24
    assert threshold.first_exact_replication_sample_size == 1632
    assert threshold.first_exact_replication_sample_size == 68 * 24


def test_p93_generic_p77_comparison_crosses_at_7444():
    threshold = certify_p93_witness_95_threshold_exact()
    assert threshold.generic_p77_last_noncertifying_sample_size == 7443
    assert threshold.generic_p77_first_certifying_sample_size == 7444
    assert threshold.generic_p77_last_radius.log_argument == 640
    assert threshold.generic_p77_first_radius.log_argument == 640
    assert threshold.generic_p77_last_radius.cell_linf_radius_lower > Fraction(1, 48)
    assert threshold.generic_p77_first_radius.cell_linf_radius_upper < Fraction(1, 48)
    assert (
        threshold.generic_p77_first_certifying_sample_size
        > 4 * threshold.first_certifying_sample_size
    )


def test_p93_requires_empirical_probabilities_compatible_with_sample_size():
    with pytest.raises(ValueError, match="not compatible"):
        certify_p93_localized_rejection_exact(
            _witness_law(),
            sample_size=1623,
            alpha=Fraction(1, 20),
        )


def test_p93_zero_determinant_profile_does_not_reject():
    uniform = tuple(Fraction(1, 16) for _ in range(16))
    certificate = certify_p93_localized_rejection_exact(
        uniform,
        sample_size=1600,
        alpha=Fraction(1, 20),
    )
    assert certificate.determinant_product == 0
    assert certificate.minimum_sign_stability_radius == 0
    assert not certificate.rejects_p75


def test_p93_source_preserves_scientific_boundary():
    module = __import__(
        "consciousness_bridge.localized_sign_coherence_rejection",
        fromlist=["dummy"],
    )
    source = (module.__doc__ or "").lower()
    assert "conditional statistical theorem" in source
    assert "does not identify" in source
    assert "nonphysicality" in source
    assert "physical-to-experiential bridge" in source
