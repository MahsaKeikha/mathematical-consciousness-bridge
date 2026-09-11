from math import isclose, log, sqrt

import pytest

from consciousness_bridge.target_measurement_channel_robustness import (
    apply_target_channel,
    binary_symmetric_target_transfer,
    finite_observed_tv_lower_bound,
    sufficient_equal_sample_size_for_latent_gap,
    target_channel_tv_transfer,
    target_measurement_residual_certificate,
    total_variation,
)


def _binary_measurement_channel(noise_rate: float):
    channel = {}
    for physical in (0, 1):
        channel[(physical, 0, 0)] = 1.0 - noise_rate
        channel[(physical, 0, 1)] = noise_rate
        channel[(physical, 1, 0)] = noise_rate
        channel[(physical, 1, 1)] = 1.0 - noise_rate
    return channel


def _latent_residual_example():
    return {
        (0, 0, 0): 1.0,
        (1, 1, 0): 1.0,
        (2, 0, 1): 1.0,
        (3, 1, 1): 1.0,
    }


def test_perfect_target_measurement_preserves_conditional_residual() -> None:
    certificate = target_measurement_residual_certificate(
        _latent_residual_example(),
        _binary_measurement_channel(0.0),
    )

    assert isclose(certificate.latent_residual_nats, log(2.0), abs_tol=1e-12)
    assert isclose(
        certificate.observed_residual_nats,
        certificate.latent_residual_nats,
        abs_tol=1e-12,
    )
    assert isclose(certificate.data_processing_gap_nats, 0.0, abs_tol=1e-12)
    assert certificate.data_processing_verified


def test_noisy_target_measurement_attenuates_conditional_residual() -> None:
    certificate = target_measurement_residual_certificate(
        _latent_residual_example(),
        _binary_measurement_channel(0.2),
    )

    assert 0.0 < certificate.observed_residual_nats
    assert certificate.observed_residual_nats < certificate.latent_residual_nats
    assert certificate.data_processing_gap_nats > 0.0


def test_erasing_measurement_can_hide_positive_latent_residual() -> None:
    erasure_channel = {
        (physical, latent_target, "erased"): 1.0
        for physical in (0, 1)
        for latent_target in (0, 1)
    }
    certificate = target_measurement_residual_certificate(
        _latent_residual_example(),
        erasure_channel,
    )

    assert isclose(certificate.latent_residual_nats, log(2.0), abs_tol=1e-12)
    assert isclose(certificate.observed_residual_nats, 0.0, abs_tol=1e-12)


def test_zero_latent_residual_cannot_be_created_by_declared_measurement_channel() -> None:
    latent = {
        (0, 0, 0): 1.0,
        (1, 1, 1): 1.0,
        (2, 0, 0): 1.0,
        (3, 1, 1): 1.0,
    }
    certificate = target_measurement_residual_certificate(
        latent,
        _binary_measurement_channel(0.25),
    )

    assert isclose(certificate.latent_residual_nats, 0.0, abs_tol=1e-12)
    assert isclose(certificate.observed_residual_nats, 0.0, abs_tol=1e-12)


def test_target_channel_contracts_total_variation() -> None:
    channel = {
        (0, "a"): 0.8,
        (0, "b"): 0.2,
        (1, "a"): 0.3,
        (1, "b"): 0.7,
    }
    transfer = target_channel_tv_transfer(
        {0: 0.9, 1: 0.1},
        {0: 0.2, 1: 0.8},
        channel,
    )

    assert isclose(transfer.latent_tv, 0.7, abs_tol=1e-12)
    assert transfer.observed_tv <= transfer.latent_tv
    assert isclose(transfer.observed_tv, 0.35, abs_tol=1e-12)


def test_binary_symmetric_channel_has_exact_attenuation_factor() -> None:
    transfer = binary_symmetric_target_transfer(0.9, 0.2, 0.1)

    assert isclose(transfer.latent_tv, 0.7, abs_tol=1e-12)
    assert isclose(transfer.attenuation_factor, 0.8, abs_tol=1e-12)
    assert isclose(transfer.observed_tv, 0.56, abs_tol=1e-12)


def test_binary_half_noise_erases_every_binary_tv_witness() -> None:
    transfer = binary_symmetric_target_transfer(1.0, 0.0, 0.5)

    assert isclose(transfer.latent_tv, 1.0, abs_tol=1e-12)
    assert isclose(transfer.attenuation_factor, 0.0, abs_tol=1e-12)
    assert isclose(transfer.observed_tv, 0.0, abs_tol=1e-12)


def test_apply_target_channel_normalizes_declared_weights() -> None:
    observed = apply_target_channel(
        {0: 3.0, 1: 1.0},
        {
            (0, "a"): 9.0,
            (0, "b"): 1.0,
            (1, "a"): 2.0,
            (1, "b"): 8.0,
        },
    )

    assert isclose(observed["a"], 0.725, abs_tol=1e-12)
    assert isclose(observed["b"], 0.275, abs_tol=1e-12)


def test_finite_observed_tv_lower_bound_uses_declared_alphabet() -> None:
    certificate = finite_observed_tv_lower_bound(
        {"no": 1000},
        {"yes": 1000},
        ("no", "yes"),
        alpha=0.05,
    )

    expected_coordinate = sqrt(log(160.0) / 2000.0)
    assert isclose(certificate.empirical_tv, 1.0, abs_tol=1e-12)
    assert isclose(certificate.coordinate_radius_a, expected_coordinate, abs_tol=1e-12)
    assert isclose(certificate.tv_radius_a, expected_coordinate, abs_tol=1e-12)
    assert certificate.lower_bound > 0.89
    assert isclose(certificate.confidence_level, 0.95, abs_tol=1e-12)


def test_sample_design_bound_implies_strict_positive_lcb_margin() -> None:
    d = 2
    alpha = 0.05
    latent_gap = 0.5
    gamma = 0.8
    n = sufficient_equal_sample_size_for_latent_gap(
        d,
        alpha,
        latent_gap,
        gamma,
    )

    tau = 0.5 * d * sqrt(log(4.0 * d / alpha) / (2.0 * n))
    assert 4.0 * tau < gamma * latent_gap


def test_required_samples_increase_as_channel_approaches_erasure() -> None:
    stable = sufficient_equal_sample_size_for_latent_gap(2, 0.05, 0.5, 0.8)
    weak = sufficient_equal_sample_size_for_latent_gap(2, 0.05, 0.5, 0.2)

    assert weak > stable


def test_total_variation_handles_different_finite_supports() -> None:
    assert isclose(total_variation({"a": 1.0}, {"b": 1.0}), 1.0, abs_tol=1e-12)


def test_invalid_measurement_channel_is_rejected() -> None:
    with pytest.raises(ValueError, match="cover every observed"):
        target_measurement_residual_certificate(
            _latent_residual_example(),
            {(0, 0, "x"): 1.0},
        )


def test_finite_certificate_rejects_post_hoc_alphabet_expansion() -> None:
    with pytest.raises(ValueError, match="declared_alphabet"):
        finite_observed_tv_lower_bound(
            {"a": 10, "outside": 1},
            {"b": 10},
            ("a", "b"),
            alpha=0.05,
        )


def test_sample_design_rejects_zero_stability_or_gap() -> None:
    with pytest.raises(ValueError):
        sufficient_equal_sample_size_for_latent_gap(2, 0.05, 0.5, 0.0)
    with pytest.raises(ValueError):
        sufficient_equal_sample_size_for_latent_gap(2, 0.05, 0.0, 0.5)
