import math

import pytest

from consciousness_bridge.finite_sample_residual_certification import (
    binary_entropy,
    certify_cmi_from_records,
    conditional_information_continuity_bound,
    entropy_continuity_bound,
    finite_sample_cmi_certificate,
    hoeffding_joint_tv_radius,
    maximum_conditional_mutual_information,
)


def test_binary_entropy_uses_natural_logarithms():
    assert binary_entropy(0.0) == 0.0
    assert binary_entropy(1.0) == 0.0
    assert binary_entropy(0.5) == pytest.approx(math.log(2.0))


def test_entropy_continuity_bound_is_zero_at_zero_radius():
    assert entropy_continuity_bound(0.0, 7) == pytest.approx(0.0)
    assert entropy_continuity_bound(0.8, 1) == pytest.approx(0.0)


def test_entropy_continuity_bound_is_uniform_for_large_radius():
    assert entropy_continuity_bound(0.75, 4) == pytest.approx(math.log(4.0))
    assert entropy_continuity_bound(1.0, 4) == pytest.approx(math.log(4.0))


def test_hoeffding_joint_tv_radius_decreases_with_sample_size():
    small = hoeffding_joint_tv_radius(500, alphabet_size=8, alpha=0.05)
    large = hoeffding_joint_tv_radius(5000, alphabet_size=8, alpha=0.05)

    assert 0.0 < large < small <= 1.0


def test_cmi_continuity_bound_vanishes_at_zero_radius():
    assert conditional_information_continuity_bound(
        0.0,
        omega_size=2,
        physical_size=3,
        target_size=2,
    ) == pytest.approx(0.0)


def test_cmi_continuity_bound_never_exceeds_full_information_range():
    bound = conditional_information_continuity_bound(
        1.0,
        omega_size=4,
        physical_size=5,
        target_size=3,
    )

    assert bound == pytest.approx(math.log(3.0))
    assert maximum_conditional_mutual_information(4, 3) == pytest.approx(math.log(3.0))


def test_strong_binary_residual_is_certified_with_enough_samples():
    certificate = finite_sample_cmi_certificate(
        estimate=math.log(2.0),
        sample_size=10_000,
        omega_size=2,
        physical_size=1,
        target_size=2,
        alpha=0.05,
    )

    assert certificate.lower > 0.0
    assert certificate.upper == pytest.approx(math.log(2.0))
    assert certificate.certified_positive


def test_zero_empirical_residual_is_not_certified_positive():
    certificate = finite_sample_cmi_certificate(
        estimate=0.0,
        sample_size=100_000,
        omega_size=2,
        physical_size=1,
        target_size=2,
        alpha=0.05,
    )

    assert certificate.lower == 0.0
    assert not certificate.certified_positive


def test_record_level_certificate_recovers_binary_residual():
    records = ["placeholder"]
    records = [("omega0", "same_t", "e0")] * 5000 + [
        ("omega1", "same_t", "e1")
    ] * 5000
    certificate = certify_cmi_from_records(
        records,
        omega_size=2,
        physical_size=1,
        target_size=2,
        alpha=0.05,
    )

    assert certificate.estimate == pytest.approx(math.log(2.0))
    assert certificate.certified_positive


def test_declared_alphabet_must_cover_observed_labels():
    records = [
        ("omega0", "t", "e"),
        ("omega1", "t", "e"),
    ]

    with pytest.raises(ValueError, match="exceed the declared"):
        certify_cmi_from_records(
            records,
            omega_size=1,
            physical_size=1,
            target_size=1,
        )


def test_invalid_certificate_inputs_are_rejected():
    with pytest.raises(ValueError, match="sample_size"):
        hoeffding_joint_tv_radius(0, 4, 0.05)
    with pytest.raises(ValueError, match="alpha"):
        hoeffding_joint_tv_radius(100, 4, 1.0)
    with pytest.raises(ValueError, match="positive integer"):
        entropy_continuity_bound(0.1, 0)
    with pytest.raises(ValueError, match="valid conditional-information range"):
        finite_sample_cmi_certificate(
            estimate=1.0,
            sample_size=100,
            omega_size=2,
            physical_size=1,
            target_size=2,
        )
