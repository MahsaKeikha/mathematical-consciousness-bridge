from pathlib import Path

import numpy as np
import pytest

from consciousness_bridge.target_model_adequacy import (
    binary_latent_independent_model_parameter_dimension,
    binary_observed_simplex_dimension,
    four_view_joint_distribution_from_model,
    four_view_overidentification_diagnostics,
    generic_overidentifying_dimension,
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
    """Mix in direct X3-X4 coupling not explained by the declared latent state."""

    coupled = np.zeros((2, 2, 2, 2), dtype=float)
    for first in (0, 1):
        for second in (0, 1):
            for third in (0, 1):
                coupled[first, second, third, third] = 1.0 / 8.0
    return 0.90 * _valid_four_view_law() + 0.10 * coupled


def test_three_views_are_just_identified_but_four_views_are_overidentified() -> None:
    assert binary_observed_simplex_dimension(3) == 7
    assert binary_latent_independent_model_parameter_dimension(3) == 7
    assert generic_overidentifying_dimension(3) == 0

    assert binary_observed_simplex_dimension(4) == 15
    assert binary_latent_independent_model_parameter_dimension(4) == 9
    assert generic_overidentifying_dimension(4) == 6


def test_exact_four_view_model_satisfies_overidentifying_moment_relations() -> None:
    diagnostics = four_view_overidentification_diagnostics(_valid_four_view_law())

    assert diagnostics.compatible_with_declared_model
    assert diagnostics.reason is None
    assert diagnostics.observed_dimension == 15
    assert diagnostics.model_parameter_dimension == 9
    assert diagnostics.generic_overidentifying_dimension == 6
    assert diagnostics.tetrad_residuals == pytest.approx((0.0, 0.0), abs=1e-12)
    assert diagnostics.triple_q_values is not None
    assert diagnostics.triple_q_values == pytest.approx(
        (16.0 / 21.0,) * 4,
        abs=1e-12,
    )
    assert diagnostics.triple_q_spread == pytest.approx(0.0, abs=1e-12)
    assert diagnostics.fourth_consistency_residuals is not None
    assert diagnostics.fourth_consistency_residuals == pytest.approx(
        (0.0, 0.0, 0.0),
        abs=1e-12,
    )
    assert diagnostics.reconstruction_error == pytest.approx(0.0, abs=1e-12)


def test_fourth_centered_moment_matches_common_q_tetrad_relation() -> None:
    diagnostics = four_view_overidentification_diagnostics(_valid_four_view_law())

    assert diagnostics.triple_q_values is not None
    q_value = diagnostics.triple_q_values[0]
    expected = (1.0 + q_value) * diagnostics.tetrad_products[0]
    assert diagnostics.moments.fourth_central_moment == pytest.approx(
        expected,
        abs=1e-12,
    )


def test_residual_view_dependence_is_detected_by_four_view_diagnostics() -> None:
    diagnostics = four_view_overidentification_diagnostics(_dependent_four_view_law())

    assert not diagnostics.compatible_with_declared_model
    assert diagnostics.reason is not None
    assert diagnostics.reconstruction_error is not None
    assert diagnostics.reconstruction_error > 1e-4
    assert max(abs(value) for value in diagnostics.tetrad_residuals) > 1e-4
    assert diagnostics.triple_q_spread is not None
    assert diagnostics.triple_q_spread > 1e-3


def test_dimension_and_probability_inputs_are_validated() -> None:
    with pytest.raises(ValueError):
        binary_observed_simplex_dimension(0)
    with pytest.raises(ValueError):
        binary_latent_independent_model_parameter_dimension(1.5)
    with pytest.raises(ValueError):
        four_view_joint_distribution_from_model(1.2, CHANNELS)
    with pytest.raises(ValueError):
        four_view_joint_distribution_from_model(PREVALENCE, CHANNELS[:3])
    with pytest.raises(ValueError):
        four_view_overidentification_diagnostics(np.ones((2, 2, 2)))
    with pytest.raises(ValueError):
        four_view_overidentification_diagnostics(_valid_four_view_law(), tolerance=0.0)


def test_p75_source_keeps_scientific_boundary_explicit() -> None:
    source = Path("src/consciousness_bridge/target_model_adequacy.py").read_text(
        encoding="utf-8"
    )
    required = (
        "does not identify a latent state with consciousness",
        "validate conditional independence from three-view fit alone",
        "Three binary views are generically just-identified",
        "a fourth view creates observable overidentifying restrictions",
    )
    for token in required:
        assert token in source
