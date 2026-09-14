from fractions import Fraction

import pytest

from consciousness_bridge.certified_continuous_model_separation import P78ParameterBox
from consciousness_bridge.complete_linear_parity_duality import (
    certify_complete_linear_parity_optimum_exact,
    complete_linear_parity_centered_coefficient_norm_exact,
    empirical_complete_linear_parity_functional_exact,
    p75_box_complete_linear_parity_functional_interval_exact,
    p75_box_complete_linear_parity_functional_witness_exact,
    p75_box_parity_vertex_vectors_exact,
    p89_canonical_parity_view_sets,
    verify_complete_linear_parity_upper_certificate_exact,
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


def _strict_empirical_law() -> tuple[Fraction, ...]:
    counts = (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
    return tuple(Fraction(count, 24) for count in counts)


def _strict_coefficients() -> tuple[int, ...]:
    return (0, -2, -1, 1, 1, 1, -2, -1, -3, 2, -3)


def _strict_vertex_weights() -> tuple[Fraction, ...]:
    # Aligned to p75_box_parity_vertex_vectors_exact(_strict_box()).
    return (
        Fraction(0),
        Fraction(0),
        Fraction(4, 189),
        Fraction(4, 21),
        Fraction(0),
        Fraction(0),
        Fraction(16, 189),
        Fraction(10, 189),
        Fraction(22, 63),
        Fraction(0),
        Fraction(0),
        Fraction(5, 27),
        Fraction(0),
        Fraction(23, 252),
        Fraction(19, 756),
        Fraction(0),
    )


def _strict_perturbation() -> tuple[Fraction, ...]:
    # Outcome order is lexicographic product((0, 1), repeat=4).
    return (
        Fraction(-5, 168),
        Fraction(-5, 168),
        Fraction(5, 168),
        Fraction(-5, 168),
        Fraction(-5, 168),
        Fraction(1, 84),
        Fraction(5, 168),
        Fraction(5, 168),
        Fraction(5, 168),
        Fraction(-5, 168),
        Fraction(-5, 168),
        Fraction(5, 168),
        Fraction(-5, 168),
        Fraction(5, 168),
        Fraction(1, 336),
        Fraction(5, 336),
    )


def test_p89_uses_all_eleven_canonical_p83_parity_coordinates():
    assert p89_canonical_parity_view_sets() == (
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 3),
        (0, 1, 2),
        (0, 1, 3),
        (0, 2, 3),
        (1, 2, 3),
        (0, 1, 2, 3),
    )
    assert len(p75_box_parity_vertex_vectors_exact(_strict_box())) == 16


def test_p89_strict_functional_has_exact_value_interval_norm_and_bound():
    empirical = _strict_empirical_law()
    box = _strict_box()
    coefficients = _strict_coefficients()

    assert empirical_complete_linear_parity_functional_exact(
        empirical, coefficients
    ) == Fraction(-13, 6)
    assert p75_box_complete_linear_parity_functional_interval_exact(
        box, coefficients
    ) == (Fraction(-51, 8), Fraction(-3))
    assert complete_linear_parity_centered_coefficient_norm_exact(
        coefficients
    ) == (Fraction(28), Fraction(-3))

    witness = p75_box_complete_linear_parity_functional_witness_exact(
        empirical, box, coefficients
    )
    assert witness.interval_gap == Fraction(5, 6)
    assert witness.lower_bound == Fraction(5, 168)
    assert witness.lower_bound > Fraction(1, 64)


def test_p89_exact_upper_certificate_matches_the_same_5_over_168_radius():
    certificate = verify_complete_linear_parity_upper_certificate_exact(
        _strict_empirical_law(),
        _strict_box(),
        _strict_vertex_weights(),
        _strict_perturbation(),
    )
    assert certificate.radius == Fraction(5, 168)
    assert sum(certificate.vertex_weights, start=Fraction(0)) == 1
    assert sum(certificate.perturbation, start=Fraction(0)) == 0
    assert tuple(
        model + residual
        for model, residual in zip(
            certificate.model_parity_vector,
            certificate.residual_parity_vector,
            strict=True,
        )
    ) == certificate.empirical_parity_vector


def test_p89_matching_exact_certificates_prove_complete_linear_optimum():
    certificate = certify_complete_linear_parity_optimum_exact(
        _strict_empirical_law(),
        _strict_box(),
        _strict_coefficients(),
        _strict_vertex_weights(),
        _strict_perturbation(),
    )
    assert certificate.optimum == Fraction(5, 168)
    assert certificate.functional.lower_bound == certificate.upper.radius
    assert certificate.optimum > Fraction(1, 64)


def test_p89_rejects_a_tampered_primal_certificate():
    perturbation = list(_strict_perturbation())
    perturbation[0] += Fraction(1, 336)
    perturbation[1] -= Fraction(1, 336)
    with pytest.raises(ValueError, match="does not reconstruct"):
        verify_complete_linear_parity_upper_certificate_exact(
            _strict_empirical_law(),
            _strict_box(),
            _strict_vertex_weights(),
            tuple(perturbation),
        )


def test_p89_rejects_zero_functional():
    with pytest.raises(ValueError, match="nonzero"):
        p75_box_complete_linear_parity_functional_witness_exact(
            _strict_empirical_law(),
            _strict_box(),
            (0,) * 11,
        )


def test_p89_source_keeps_scientific_interpretation_boundary():
    source = (
        __import__(
            "consciousness_bridge.complete_linear_parity_duality",
            fromlist=["dummy"],
        ).__doc__
        or ""
    ).lower()
    assert "conditional" in source
    assert "does not identify" in source
    assert "consciousness" in source
    assert "nonphysicality" in source
    assert "physical-to-experiential bridge" in source
