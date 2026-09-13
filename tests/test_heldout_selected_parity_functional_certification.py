from fractions import Fraction
from pathlib import Path

import pytest

from consciousness_bridge.bounded_primitive_quad_projection_parity_functional_separation import (
    p75_box_p87_linf_lower_bound_exact,
)
from consciousness_bridge.certified_continuous_model_separation import P78ParameterBox
from consciousness_bridge.certified_sampling_radius import (
    certified_finite_alphabet_sampling_radius,
)
from consciousness_bridge.heldout_selected_parity_functional_certification import (
    p88_heldout_selected_p87_certificate_exact,
    primitive_parity_quad_score_range_exact,
)


def _strict_box() -> P78ParameterBox:
    return P78ParameterBox(
        lower=(
            Fraction(0),
            Fraction(1, 4),
            Fraction(1, 2),
            Fraction(1, 4),
            Fraction(3, 4),
            Fraction(1, 2),
            Fraction(1, 2),
            Fraction(1, 4),
            Fraction(3, 4),
        ),
        upper=(
            Fraction(0),
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(3, 4),
            Fraction(1),
            Fraction(3, 4),
            Fraction(1),
            Fraction(1),
        ),
    )


def _validation_empirical_law() -> tuple[Fraction, ...]:
    counts = (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
    return tuple(Fraction(count, 24) for count in counts)


def _selected_terms():
    return (
        ((0, 2), 1),
        ((1, 3), -1),
        ((1, 2, 3), -2),
        ((0, 1, 2, 3), 2),
    )


def test_selected_p87_score_has_exact_range_minus3_to2() -> None:
    assert primitive_parity_quad_score_range_exact(_selected_terms()) == (
        Fraction(-3),
        Fraction(2),
    )


def test_p88_heldout_witness_has_exact_certified_values() -> None:
    certificate = p88_heldout_selected_p87_certificate_exact(
        _validation_empirical_law(),
        validation_sample_size=2400,
        box=_strict_box(),
        terms=_selected_terms(),
        alpha=Fraction(1, 20),
        series_terms=12,
        sqrt_bits=24,
    )

    assert certificate.empirical_value == Fraction(-17, 24)
    assert (certificate.interval_lower, certificate.interval_upper) == (
        Fraction(-1, 2),
        Fraction(2),
    )
    assert certificate.empirical_interval_gap == Fraction(5, 24)
    assert certificate.score_width == Fraction(5)
    assert certificate.unit_hoeffding_radius_upper == Fraction(465101, 16777216)
    assert certificate.functional_radius_upper == Fraction(2325505, 16777216)
    assert certificate.population_interval_gap_lower == Fraction(3509245, 50331648)
    assert certificate.centered_coefficient_norm == Fraction(20)
    assert certificate.linf_distance_lower_confidence_bound == Fraction(
        701849,
        201326592,
    )
    assert certificate.rejects_box
    assert "independent" in certificate.validity_statement


def test_p88_can_trigger_when_p87_global_radius_handoff_is_inconclusive() -> None:
    empirical = _validation_empirical_law()
    box = _strict_box()
    p87_empirical_distance_lower = p75_box_p87_linf_lower_bound_exact(empirical, box)
    global_radius = certified_finite_alphabet_sampling_radius(
        sample_size=2400,
        alphabet_size=16,
        alpha=Fraction(1, 20),
        series_terms=12,
        sqrt_bits=24,
    ).cell_linf_radius_upper
    heldout = p88_heldout_selected_p87_certificate_exact(
        empirical,
        validation_sample_size=2400,
        box=box,
        terms=_selected_terms(),
        alpha=Fraction(1, 20),
        series_terms=12,
        sqrt_bits=24,
    )

    assert p87_empirical_distance_lower == Fraction(1, 96)
    assert global_radius == Fraction(615553, 16777216)
    assert p87_empirical_distance_lower < global_radius
    assert heldout.rejects_box
    assert heldout.linf_distance_lower_confidence_bound > 0


def test_p88_requires_validation_law_compatible_with_sample_size() -> None:
    with pytest.raises(ValueError, match="incompatible"):
        p88_heldout_selected_p87_certificate_exact(
            _validation_empirical_law(),
            validation_sample_size=100,
            box=_strict_box(),
            terms=_selected_terms(),
            alpha=Fraction(1, 20),
        )


def test_p88_rejects_nonexact_validation_probabilities() -> None:
    empirical = list(_validation_empirical_law())
    empirical[0] = 0.0
    with pytest.raises(TypeError, match="fractions.Fraction"):
        p88_heldout_selected_p87_certificate_exact(
            tuple(empirical),
            validation_sample_size=2400,
            box=_strict_box(),
            terms=_selected_terms(),
            alpha=Fraction(1, 20),
        )


def test_p88_source_keeps_selection_and_scientific_boundaries_explicit() -> None:
    source = Path(
        "src/consciousness_bridge/heldout_selected_parity_functional_certification.py"
    ).read_text(encoding="utf-8")
    required = (
        "independent discovery sample",
        "no union bound over the 39,600 candidate functionals",
        "cannot verify that discovery and validation data were actually independent",
        "does not identify a latent state with consciousness",
        "does not solve the physical-to-experiential bridge",
    )
    for token in required:
        assert token in source
