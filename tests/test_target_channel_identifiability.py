from pathlib import Path

import numpy as np
import pytest

from consciousness_bridge.target_channel_identifiability import (
    binary_channel_stability,
    joint_channel_stability,
    joint_distribution_from_model,
    recover_three_view_binary_model,
    symmetric_two_view_joint,
    three_view_moments,
)


def test_three_view_recovery_recovers_non_degenerate_model() -> None:
    prevalence = 0.70
    channels = ((0.20, 0.80), (0.10, 0.60), (0.70, 0.30))
    joint = joint_distribution_from_model(prevalence, channels)

    recovered = recover_three_view_binary_model(joint)

    assert recovered.prevalence_plus == pytest.approx(prevalence)
    assert np.asarray(recovered.conditional_plus) == pytest.approx(np.asarray(channels))
    assert recovered.single_view_stability == pytest.approx((0.60, 0.50, 0.40))


def test_three_view_moment_identities_hold_exactly() -> None:
    prevalence = 0.70
    channels = ((0.20, 0.80), (0.10, 0.60), (0.70, 0.30))
    joint = joint_distribution_from_model(prevalence, channels)
    moments = three_view_moments(joint)

    latent_mean = 2.0 * prevalence - 1.0
    latent_variance = 1.0 - latent_mean**2
    loadings = np.asarray([channel[1] - channel[0] for channel in channels])

    expected_covariances = (
        loadings[0] * loadings[1] * latent_variance,
        loadings[0] * loadings[2] * latent_variance,
        loadings[1] * loadings[2] * latent_variance,
    )
    expected_third = (
        -2.0 * latent_mean * latent_variance * float(np.prod(loadings))
    )

    assert moments.covariances == pytest.approx(expected_covariances)
    assert moments.third_central_moment == pytest.approx(expected_third)


def test_balanced_latent_prevalence_is_recoverable_when_loadings_are_nonzero() -> None:
    channels = ((0.15, 0.75), (0.20, 0.65), (0.80, 0.35))
    joint = joint_distribution_from_model(0.5, channels)

    recovered = recover_three_view_binary_model(joint)

    assert recovered.prevalence_plus == pytest.approx(0.5)
    assert recovered.latent_mean == pytest.approx(0.0, abs=1e-12)
    assert np.asarray(recovered.conditional_plus) == pytest.approx(np.asarray(channels))


def test_latent_label_swap_leaves_observable_law_and_stability_unchanged() -> None:
    prevalence = 0.70
    channels = ((0.20, 0.80), (0.10, 0.60), (0.70, 0.30))
    swapped = tuple((channel[1], channel[0]) for channel in channels)

    original_joint = joint_distribution_from_model(prevalence, channels)
    swapped_joint = joint_distribution_from_model(1.0 - prevalence, swapped)

    assert original_joint == pytest.approx(swapped_joint)
    assert tuple(binary_channel_stability(channel) for channel in channels) == pytest.approx(
        tuple(binary_channel_stability(channel) for channel in swapped)
    )
    assert joint_channel_stability(channels) == pytest.approx(
        joint_channel_stability(swapped)
    )


def test_anchor_view_selects_only_the_global_latent_orientation() -> None:
    prevalence = 0.70
    channels = ((0.20, 0.80), (0.10, 0.60), (0.70, 0.30))
    joint = joint_distribution_from_model(prevalence, channels)

    anchor_zero = recover_three_view_binary_model(joint, anchor_view=0)
    anchor_two = recover_three_view_binary_model(joint, anchor_view=2)

    assert anchor_zero.prevalence_plus == pytest.approx(1.0 - anchor_two.prevalence_plus)
    assert np.asarray(anchor_zero.conditional_plus) == pytest.approx(
        np.asarray([(channel[1], channel[0]) for channel in anchor_two.conditional_plus])
    )
    assert anchor_zero.single_view_stability == pytest.approx(
        anchor_two.single_view_stability
    )
    assert anchor_zero.joint_stability == pytest.approx(anchor_two.joint_stability)


def test_joint_three_view_stability_dominates_every_single_view() -> None:
    channels = ((0.20, 0.80), (0.10, 0.60), (0.70, 0.30))
    single = [binary_channel_stability(channel) for channel in channels]
    joint = joint_channel_stability(channels)

    assert joint >= max(single) - 1e-12
    assert joint <= 1.0


def test_recovered_joint_stability_is_observable_and_label_invariant() -> None:
    channels = ((0.20, 0.80), (0.10, 0.60), (0.70, 0.30))
    joint = joint_distribution_from_model(0.70, channels)
    recovered = recover_three_view_binary_model(joint)

    assert recovered.joint_stability == pytest.approx(joint_channel_stability(channels))


def test_two_views_do_not_identify_individual_channel_stabilities() -> None:
    first = symmetric_two_view_joint(0.60, 0.60)
    second = symmetric_two_view_joint(0.45, 0.80)

    assert first == pytest.approx(second)
    assert abs(0.60) != pytest.approx(abs(0.45))
    assert abs(0.60) != pytest.approx(abs(0.80))


def test_degenerate_three_view_model_is_rejected() -> None:
    channels = ((0.20, 0.80), (0.50, 0.50), (0.30, 0.70))
    joint = joint_distribution_from_model(0.60, channels)

    with pytest.raises(ValueError, match="three nonzero pair covariances"):
        recover_three_view_binary_model(joint)


def test_invalid_probability_inputs_are_rejected() -> None:
    with pytest.raises(ValueError):
        recover_three_view_binary_model(np.ones((2, 2)))
    with pytest.raises(ValueError):
        joint_distribution_from_model(1.2, ((0.1, 0.9),) * 3)
    with pytest.raises(ValueError):
        binary_channel_stability((-0.1, 0.9))


def test_p73_source_keeps_scientific_boundary_explicit() -> None:
    source = Path(
        "src/consciousness_bridge/target_channel_identifiability.py"
    ).read_text(encoding="utf-8")
    assert "not interpret the latent state as consciousness" in source
    assert "global latent-label swap" in source
    assert "two-view non-identifiability" in source
