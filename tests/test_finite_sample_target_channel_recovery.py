from pathlib import Path

import numpy as np
import pytest

from consciousness_bridge.finite_sample_target_channel_recovery import (
    categorical_cell_linf_radius,
    categorical_joint_l1_radius,
    finite_sample_three_view_certificate,
    sufficient_nondegeneracy_sample_size,
)
from consciousness_bridge.target_channel_identifiability import (
    joint_distribution_from_model,
)


PREVALENCE = 0.70
CHANNELS = ((0.20, 0.80), (0.10, 0.60), (0.70, 0.30))
TRUE_GAMMA = (0.60, 0.50, 0.40)
TRUE_OFFSETS = (0.0, -0.30, 0.0)
TRUE_CHANNEL_ORBITS = ((0.20, 0.80), (0.10, 0.60), (0.30, 0.70))


def _exact_model_counts(sample_size: int) -> np.ndarray:
    joint = joint_distribution_from_model(PREVALENCE, CHANNELS)
    counts = np.rint(sample_size * joint).astype(np.int64)
    assert counts.sum() == sample_size
    assert np.asarray(counts, dtype=float) / sample_size == pytest.approx(joint)
    return counts


def test_p74_cell_and_l1_radii_match_declared_hoeffding_event() -> None:
    n = 100_000
    alpha = 0.05
    expected_cell = np.sqrt(np.log(16.0 / alpha) / (2.0 * n))

    assert categorical_cell_linf_radius(n, alpha) == pytest.approx(expected_cell)
    assert categorical_joint_l1_radius(n, alpha) == pytest.approx(
        min(2.0, 8.0 * expected_cell)
    )


def test_large_exact_population_table_certifies_true_stabilities() -> None:
    certificate = finite_sample_three_view_certificate(
        _exact_model_counts(100_000_000), alpha=0.05
    )

    assert certificate.certified_nondegenerate
    assert certificate.reason is None
    assert certificate.stability_bounds is not None
    for truth, interval in zip(TRUE_GAMMA, certificate.stability_bounds, strict=True):
        assert interval[0] <= truth <= interval[1]
        assert 0.0 <= interval[0] <= interval[1] <= 1.0


def test_large_exact_population_table_certifies_full_channel_orbits() -> None:
    certificate = finite_sample_three_view_certificate(
        _exact_model_counts(100_000_000), alpha=0.05
    )

    assert certificate.channel_offset_bounds is not None
    assert certificate.channel_probability_orbit_bounds is not None

    for truth, interval in zip(
        TRUE_OFFSETS,
        certificate.channel_offset_bounds,
        strict=True,
    ):
        assert interval[0] <= truth <= interval[1]
        assert -1.0 <= interval[0] <= interval[1] <= 1.0

    for truth_orbit, certified_orbit in zip(
        TRUE_CHANNEL_ORBITS,
        certificate.channel_probability_orbit_bounds,
        strict=True,
    ):
        smaller_interval, larger_interval = certified_orbit
        assert smaller_interval[0] <= truth_orbit[0] <= smaller_interval[1]
        assert larger_interval[0] <= truth_orbit[1] <= larger_interval[1]
        assert 0.0 <= smaller_interval[0] <= smaller_interval[1] <= 1.0
        assert 0.0 <= larger_interval[0] <= larger_interval[1] <= 1.0


def test_loading_times_latent_mean_identity_is_certified() -> None:
    certificate = finite_sample_three_view_certificate(
        _exact_model_counts(100_000_000), alpha=0.05
    )

    # m = 0.4 for prevalence 0.7. The signed P73 loadings are
    # b = (0.6, 0.5, -0.4) for the declared channel orientation.
    truth = (0.24, 0.20, -0.16)
    assert certificate.loading_times_latent_mean_bounds is not None
    for expected, interval in zip(
        truth,
        certificate.loading_times_latent_mean_bounds,
        strict=True,
    ):
        assert interval[0] <= expected <= interval[1]


def test_label_invariant_latent_prevalence_orbit_contains_both_orientations() -> None:
    certificate = finite_sample_three_view_certificate(
        _exact_model_counts(100_000_000), alpha=0.05
    )

    assert certificate.latent_abs_mean_bounds is not None
    assert certificate.latent_abs_mean_bounds[0] <= 0.40 <= certificate.latent_abs_mean_bounds[1]
    assert certificate.prevalence_orbit_intervals is not None
    low_orientation, high_orientation = certificate.prevalence_orbit_intervals
    assert low_orientation[0] <= 0.30 <= low_orientation[1]
    assert high_orientation[0] <= 0.70 <= high_orientation[1]


def test_small_sample_refuses_unstable_p73_inversion() -> None:
    certificate = finite_sample_three_view_certificate(
        _exact_model_counts(1_000), alpha=0.05
    )

    assert not certificate.certified_nondegenerate
    assert certificate.reason is not None
    assert "not certified" in certificate.reason
    assert certificate.q_bounds is None
    assert certificate.stability_bounds is None
    assert certificate.channel_offset_bounds is None
    assert certificate.channel_probability_orbit_bounds is None


def test_more_data_shrinks_stability_offset_and_channel_intervals() -> None:
    moderate = finite_sample_three_view_certificate(
        _exact_model_counts(10_000_000), alpha=0.05
    )
    large = finite_sample_three_view_certificate(
        _exact_model_counts(100_000_000), alpha=0.05
    )

    assert moderate.certified_nondegenerate
    assert large.certified_nondegenerate
    assert large.joint_l1_radius < moderate.joint_l1_radius
    assert moderate.stability_bounds is not None
    assert large.stability_bounds is not None
    assert moderate.channel_offset_bounds is not None
    assert large.channel_offset_bounds is not None
    assert moderate.channel_probability_orbit_bounds is not None
    assert large.channel_probability_orbit_bounds is not None

    for moderate_interval, large_interval in zip(
        moderate.stability_bounds, large.stability_bounds, strict=True
    ):
        moderate_width = moderate_interval[1] - moderate_interval[0]
        large_width = large_interval[1] - large_interval[0]
        assert large_width < moderate_width

    for moderate_interval, large_interval in zip(
        moderate.channel_offset_bounds,
        large.channel_offset_bounds,
        strict=True,
    ):
        moderate_width = moderate_interval[1] - moderate_interval[0]
        large_width = large_interval[1] - large_interval[0]
        assert large_width < moderate_width

    for moderate_orbit, large_orbit in zip(
        moderate.channel_probability_orbit_bounds,
        large.channel_probability_orbit_bounds,
        strict=True,
    ):
        for moderate_interval, large_interval in zip(
            moderate_orbit,
            large_orbit,
            strict=True,
        ):
            moderate_width = moderate_interval[1] - moderate_interval[0]
            large_width = large_interval[1] - large_interval[0]
            assert large_width < moderate_width


def test_joint_stability_lower_bound_dominates_certified_single_view_lowers() -> None:
    certificate = finite_sample_three_view_certificate(
        _exact_model_counts(100_000_000), alpha=0.05
    )

    assert certificate.stability_bounds is not None
    assert certificate.joint_stability_lower_bound == pytest.approx(
        max(interval[0] for interval in certificate.stability_bounds)
    )


def test_sufficient_nondegeneracy_design_bound_has_correct_monotonicity() -> None:
    n_small_covariance = sufficient_nondegeneracy_sample_size(0.10, 0.05)
    n_large_covariance = sufficient_nondegeneracy_sample_size(0.20, 0.05)
    n_higher_confidence = sufficient_nondegeneracy_sample_size(0.20, 0.01)

    assert n_large_covariance < n_small_covariance
    assert n_higher_confidence > n_large_covariance


def test_invalid_inputs_are_rejected() -> None:
    with pytest.raises(ValueError):
        categorical_cell_linf_radius(0, 0.05)
    with pytest.raises(ValueError):
        categorical_joint_l1_radius(100, 1.0)
    with pytest.raises(ValueError):
        sufficient_nondegeneracy_sample_size(0.0, 0.05)
    with pytest.raises(ValueError):
        finite_sample_three_view_certificate(np.zeros((2, 2, 2)), alpha=0.05)
    with pytest.raises(ValueError):
        finite_sample_three_view_certificate(np.ones((2, 2)), alpha=0.05)
    with pytest.raises(ValueError):
        finite_sample_three_view_certificate(np.ones((2, 2, 2)), alpha=0.0)


def test_p74_source_keeps_scientific_boundary_explicit() -> None:
    source = Path(
        "src/consciousness_bridge/finite_sample_target_channel_recovery.py"
    ).read_text(encoding="utf-8")
    required = (
        "does not validate conditional independence",
        "identify the latent state with consciousness",
        "finite data do not certify safe inversion",
        "does not prove that the population model is degenerate",
        "global latent-label swap",
    )
    for token in required:
        assert token in source
