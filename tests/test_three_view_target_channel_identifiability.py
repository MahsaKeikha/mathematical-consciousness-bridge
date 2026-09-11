import math

import pytest

from consciousness_bridge.three_view_target_channel_identifiability import (
    better_than_chance_error_rates,
    empirical_pairwise_moments,
    finite_three_view_stability_certificate,
    identify_three_view_stabilities,
    two_view_compatible_stabilities,
)


def test_three_heterogeneous_views_identify_stability_magnitudes():
    r_1, r_2, r_3 = 0.8, 0.6, 0.5
    result = identify_three_view_stabilities(
        r_1 * r_2,
        r_1 * r_3,
        r_2 * r_3,
    )
    assert result.stability_1 == pytest.approx(abs(r_1))
    assert result.stability_2 == pytest.approx(abs(r_2))
    assert result.stability_3 == pytest.approx(abs(r_3))
    assert result.global_sign_ambiguity is True


def test_global_sign_flip_leaves_identified_stabilities_unchanged():
    positive = identify_three_view_stabilities(0.48, 0.40, 0.30)
    negative_reliabilities = (-0.8, -0.6, -0.5)
    flipped = identify_three_view_stabilities(
        negative_reliabilities[0] * negative_reliabilities[1],
        negative_reliabilities[0] * negative_reliabilities[2],
        negative_reliabilities[1] * negative_reliabilities[2],
    )
    assert flipped.stability_1 == pytest.approx(positive.stability_1)
    assert flipped.stability_2 == pytest.approx(positive.stability_2)
    assert flipped.stability_3 == pytest.approx(positive.stability_3)


def test_mixed_signed_pair_moments_can_still_have_one_global_orientation_ambiguity():
    r_1, r_2, r_3 = 0.8, -0.6, -0.5
    result = identify_three_view_stabilities(
        r_1 * r_2,
        r_1 * r_3,
        r_2 * r_3,
    )
    assert result.stability_1 == pytest.approx(0.8)
    assert result.stability_2 == pytest.approx(0.6)
    assert result.stability_3 == pytest.approx(0.5)


def test_better_than_chance_orientation_recovers_binary_error_rates():
    error_rates = better_than_chance_error_rates(0.48, 0.40, 0.30)
    assert error_rates == pytest.approx((0.1, 0.2, 0.25))


def test_two_heterogeneous_views_are_not_individually_identifiable():
    first = two_view_compatible_stabilities(0.36, 0.6)
    second = two_view_compatible_stabilities(0.36, 0.9)
    assert first == pytest.approx((0.6, 0.6))
    assert second == pytest.approx((0.9, 0.4))
    assert math.prod(first) == pytest.approx(0.36)
    assert math.prod(second) == pytest.approx(0.36)
    assert first != second


def test_incompatible_sign_pattern_is_rejected():
    with pytest.raises(ValueError, match="incompatible"):
        identify_three_view_stabilities(0.2, 0.3, -0.4)


def test_incompatible_magnitude_pattern_is_rejected():
    with pytest.raises(ValueError, match="invalid binary channel stability"):
        identify_three_view_stabilities(0.9, 0.9, 0.1)


def test_zero_pair_moment_is_a_degenerate_exact_identification_boundary():
    with pytest.raises(ValueError, match="nonzero pairwise moments"):
        identify_three_view_stabilities(0.0, 0.4, 0.3)


def test_empirical_pairwise_moments_use_sign_products():
    observations = [
        (1, 1, 1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
    ]
    assert empirical_pairwise_moments(observations) == pytest.approx((0.5, 0.5, 0.0))


def test_finite_certificate_is_nontrivial_for_three_highly_agreeing_views():
    observations = [(1, 1, 1), (-1, -1, -1)] * 2500
    certificate = finite_three_view_stability_certificate(observations, alpha=0.05)
    assert certificate.confidence_level == pytest.approx(0.95)
    assert certificate.sample_size == 5000
    for interval in (
        certificate.stability_1,
        certificate.stability_2,
        certificate.stability_3,
    ):
        assert 0.0 < interval.lower <= 1.0
        assert interval.upper == pytest.approx(1.0)
        assert interval.lower <= 1.0 <= interval.upper


def test_finite_certificate_radius_shrinks_with_more_repeated_views():
    small = [(1, 1, 1), (-1, -1, -1)] * 100
    large = small * 10
    small_certificate = finite_three_view_stability_certificate(small, alpha=0.05)
    large_certificate = finite_three_view_stability_certificate(large, alpha=0.05)
    assert large_certificate.moment_radius < small_certificate.moment_radius
    assert large_certificate.stability_1.lower > small_certificate.stability_1.lower


def test_finite_certificate_validates_binary_encoding_and_alpha():
    with pytest.raises(ValueError, match=r"encoded as -1 or \+1"):
        finite_three_view_stability_certificate([(1, 0, 1)], alpha=0.05)
    with pytest.raises(ValueError, match="strictly between zero and one"):
        finite_three_view_stability_certificate([(1, 1, 1)], alpha=1.0)


def test_two_view_constructor_rejects_incompatible_requested_stability():
    with pytest.raises(ValueError, match="incompatible"):
        two_view_compatible_stabilities(0.8, 0.5)
