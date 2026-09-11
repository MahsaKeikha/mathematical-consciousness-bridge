from pathlib import Path

import numpy as np
import pytest

from consciousness_bridge.finite_sample_target_model_adequacy import (
    categorical_16_cell_l1_radius,
    categorical_16_cell_linf_radius,
    finite_sample_four_view_adequacy_certificate,
    sufficient_tetrad_rejection_sample_size,
)
from consciousness_bridge.target_model_adequacy import (
    four_view_joint_distribution_from_model,
)

PREVALENCE = 0.70
CHANNELS = (
    (0.20, 0.80),
    (0.10, 0.60),
    (0.70, 0.30),
    (0.25, 0.75),
)


def _valid_four_view_law() -> np.ndarray:
    return four_view_joint_distribution_from_model(PREVALENCE, CHANNELS)


def _dependent_four_view_law() -> np.ndarray:
    coupled = np.zeros((2, 2, 2, 2), dtype=float)
    for first in (0, 1):
        for second in (0, 1):
            for third in (0, 1):
                coupled[first, second, third, third] = 1.0 / 8.0
    return 0.50 * _valid_four_view_law() + 0.50 * coupled


def _integer_counts(probabilities: np.ndarray, sample_size: int) -> np.ndarray:
    expected = probabilities.reshape(-1) * sample_size
    counts = np.floor(expected).astype(np.int64)
    remainder = sample_size - int(counts.sum())
    if remainder:
        fractional = expected - counts
        indices = np.argsort(fractional)[-remainder:]
        counts[indices] += 1
    return counts.reshape(probabilities.shape)


def _contains_zero(interval: tuple[float, float]) -> bool:
    return interval[0] <= 0.0 <= interval[1]


def test_sixteen_cell_radii_are_valid_and_shrink_with_sample_size() -> None:
    small_linf = categorical_16_cell_linf_radius(10_000, 0.05)
    large_linf = categorical_16_cell_linf_radius(1_000_000, 0.05)
    small_l1 = categorical_16_cell_l1_radius(10_000, 0.05)
    large_l1 = categorical_16_cell_l1_radius(1_000_000, 0.05)

    assert 0.0 < large_linf < small_linf
    assert 0.0 < large_l1 < small_l1 <= 2.0


def test_valid_four_view_model_is_not_falsely_promoted_to_acceptance() -> None:
    counts = _integer_counts(_valid_four_view_law(), 100_000_000)
    certificate = finite_sample_four_view_adequacy_certificate(
        counts,
        alpha=0.05,
    )

    assert not certificate.certified_incompatible
    assert certificate.rejection_witnesses == ()
    assert "not model acceptance" in certificate.conclusion
    assert all(_contains_zero(interval) for interval in certificate.tetrad_residual_intervals)


def test_residual_dependence_is_certifiably_rejected_from_finite_data() -> None:
    counts = _integer_counts(_dependent_four_view_law(), 100_000_000)
    certificate = finite_sample_four_view_adequacy_certificate(
        counts,
        alpha=0.05,
    )

    assert certificate.certified_incompatible
    assert certificate.rejection_witnesses
    assert any(
        witness.startswith("tetrad_")
        for witness in certificate.rejection_witnesses
    )
    assert "rejected" in certificate.conclusion


def test_polynomial_intervals_are_simultaneous_and_finite() -> None:
    counts = _integer_counts(_valid_four_view_law(), 1_000_000)
    certificate = finite_sample_four_view_adequacy_certificate(counts)

    interval_groups = (
        certificate.tetrad_residual_intervals,
        certificate.cross_triple_polynomial_intervals,
        certificate.fourth_polynomial_intervals,
    )
    for group in interval_groups:
        for lower, upper in group:
            assert np.isfinite(lower)
            assert np.isfinite(upper)
            assert lower <= upper


def test_tetrad_design_bound_is_strictly_sufficient() -> None:
    alpha = 0.05
    margin = 0.10
    sample_size = sufficient_tetrad_rejection_sample_size(margin, alpha)
    delta = categorical_16_cell_l1_radius(sample_size, alpha)

    assert 24.0 * delta < margin


def test_invalid_inputs_are_rejected() -> None:
    with pytest.raises(ValueError):
        categorical_16_cell_linf_radius(0, 0.05)
    with pytest.raises(ValueError):
        categorical_16_cell_l1_radius(100, 1.0)
    with pytest.raises(ValueError):
        sufficient_tetrad_rejection_sample_size(0.0, 0.05)
    with pytest.raises(ValueError):
        finite_sample_four_view_adequacy_certificate(np.ones((2, 2, 2)))
    with pytest.raises(ValueError):
        finite_sample_four_view_adequacy_certificate(
            np.ones((2, 2, 2, 2)),
            alpha=0.0,
        )


def test_p76_source_keeps_rejection_boundary_explicit() -> None:
    source = Path(
        "src/consciousness_bridge/finite_sample_target_model_adequacy.py"
    ).read_text(encoding="utf-8")
    required = (
        "Failure to reject is not acceptance of the model",
        "does not identify any latent state with consciousness",
        "one shared sixteen-cell Hoeffding event",
        "not an acceptance test",
    )
    for token in required:
        assert token in source
