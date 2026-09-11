from fractions import Fraction
from math import log, sqrt
from pathlib import Path

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    P78DistanceBracket,
)
from consciousness_bridge.certified_sampling_radius import (
    certified_finite_alphabet_sampling_radius,
    natural_log_rational_bracket,
    p78_rejection_with_p79_radius,
)


def _synthetic_bracket(lower_bound: Fraction) -> P78DistanceBracket:
    return P78DistanceBracket(
        lower_bound=lower_bound,
        upper_bound=lower_bound + Fraction(1, 100),
        best_parameters=(Fraction(1, 2),) * 9,
        leaf_count=1,
        evaluated_boxes=1,
        iterations=0,
        maximum_active_width_sum=Fraction(0),
        mesh_upper_bound=lower_bound + Fraction(1, 100),
        certified_gap=Fraction(1, 100),
        conclusion="synthetic test bracket",
    )


def test_log_bracket_contains_reference_values() -> None:
    for value in (Fraction(3, 2), Fraction(7), Fraction(640), Fraction(1, 3)):
        bracket = natural_log_rational_bracket(value, series_terms=12)
        truth = log(float(value))
        assert float(bracket.lower) <= truth <= float(bracket.upper)
        assert bracket.lower <= bracket.upper


def test_more_series_terms_tighten_log_bracket() -> None:
    coarse = natural_log_rational_bracket(Fraction(640), series_terms=6)
    fine = natural_log_rational_bracket(Fraction(640), series_terms=12)

    assert fine.lower >= coarse.lower
    assert fine.upper <= coarse.upper
    assert fine.width <= coarse.width


def test_sampling_radius_encloses_standard_p77_value() -> None:
    certificate = certified_finite_alphabet_sampling_radius(
        sample_size=100_000,
        alphabet_size=16,
        alpha=Fraction(1, 20),
        series_terms=12,
        sqrt_bits=48,
    )
    truth = sqrt(log(640.0) / 200_000.0)

    assert float(certificate.cell_linf_radius_lower) <= truth
    assert truth <= float(certificate.cell_linf_radius_upper)
    assert certificate.cell_linf_radius_lower <= certificate.cell_linf_radius_upper
    assert certificate.joint_l1_radius_upper == min(
        Fraction(2),
        16 * certificate.cell_linf_radius_upper,
    )


def test_higher_sqrt_precision_tightens_radius_envelope() -> None:
    coarse = certified_finite_alphabet_sampling_radius(
        sample_size=10_000,
        alphabet_size=16,
        alpha=Fraction(1, 20),
        series_terms=10,
        sqrt_bits=16,
    )
    fine = certified_finite_alphabet_sampling_radius(
        sample_size=10_000,
        alphabet_size=16,
        alpha=Fraction(1, 20),
        series_terms=14,
        sqrt_bits=48,
    )

    assert fine.cell_linf_radius_lower >= coarse.cell_linf_radius_lower
    assert fine.cell_linf_radius_upper <= coarse.cell_linf_radius_upper
    assert fine.cell_linf_width <= coarse.cell_linf_width


def test_p79_closes_strict_p78_radius_handoff() -> None:
    radius = certified_finite_alphabet_sampling_radius(
        sample_size=100_000,
        alphabet_size=16,
        alpha=Fraction(1, 20),
    )

    assert p78_rejection_with_p79_radius(
        _synthetic_bracket(Fraction(1, 20)),
        radius,
    )
    assert not p78_rejection_with_p79_radius(
        _synthetic_bracket(Fraction(1, 1000)),
        radius,
    )


def test_p79_validation_rejects_nonexact_or_invalid_inputs() -> None:
    with pytest.raises(TypeError):
        certified_finite_alphabet_sampling_radius(
            sample_size=100,
            alphabet_size=16,
            alpha=0.05,
        )
    with pytest.raises(ValueError):
        certified_finite_alphabet_sampling_radius(
            sample_size=0,
            alphabet_size=16,
            alpha=Fraction(1, 20),
        )
    with pytest.raises(ValueError):
        certified_finite_alphabet_sampling_radius(
            sample_size=100,
            alphabet_size=0,
            alpha=Fraction(1, 20),
        )
    with pytest.raises(ValueError):
        certified_finite_alphabet_sampling_radius(
            sample_size=100,
            alphabet_size=16,
            alpha=Fraction(1),
        )
    with pytest.raises(ValueError):
        natural_log_rational_bracket(Fraction(0))


def test_p79_source_keeps_certification_and_scientific_boundaries_explicit() -> None:
    source = Path("src/consciousness_bridge/certified_sampling_radius.py").read_text(
        encoding="utf-8"
    )

    required = (
        "mathematically valid *upper bound*",
        "ordinary floating-point approximation",
        "exact rational arithmetic",
        "explicit convergent series remainder",
        "does not identify any latent state with consciousness",
        "does not solve the physical-to-experiential bridge",
    )
    for token in required:
        assert token in source
