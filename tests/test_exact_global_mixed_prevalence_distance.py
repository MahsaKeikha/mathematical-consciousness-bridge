from fractions import Fraction

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    empirical_law_from_counts,
)
from consciousness_bridge.exact_global_mixed_prevalence_distance import (
    certify_p92_empirical_sign_coherence_obstruction_exact,
    certify_p92_exact_global_distance,
    determinant_2_by_2_exact,
    determinant_sign_stability_radius_exact,
    p92_model_sign_factorization_exact,
    p92_selected_determinants_exact,
    p92_selected_minor_matrices_exact,
    p92_x1_one_subtensor_exact,
)


def _empirical_law() -> tuple[Fraction, ...]:
    return empirical_law_from_counts(
        (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
    )


def _mixed_upper_parameters() -> tuple[Fraction, ...]:
    return (
        Fraction(4, 5),
        Fraction(9, 10),
        Fraction(5, 8),
        Fraction(1, 6),
        Fraction(1, 2),
        Fraction(1, 6),
        Fraction(2, 3),
        Fraction(0),
        Fraction(1),
    )


def test_p92_x1_one_subtensor_is_exact():
    assert p92_x1_one_subtensor_exact(_empirical_law()) == (
        Fraction(1, 8),
        Fraction(1, 24),
        Fraction(0),
        Fraction(5, 24),
        Fraction(0),
        Fraction(1, 8),
        Fraction(0),
        Fraction(1, 8),
    )


def test_p92_selected_empirical_minors_are_exact():
    matrices = p92_selected_minor_matrices_exact(_empirical_law())
    assert matrices == (
        (
            (Fraction(1, 24), Fraction(5, 24)),
            (Fraction(1, 8), Fraction(1, 8)),
        ),
        (
            (Fraction(1, 8), Fraction(1, 24)),
            (Fraction(0), Fraction(1, 8)),
        ),
        (
            (Fraction(1, 8), Fraction(1, 24)),
            (Fraction(0), Fraction(5, 24)),
        ),
    )
    assert p92_selected_determinants_exact(_empirical_law()) == (
        Fraction(-1, 48),
        Fraction(1, 64),
        Fraction(5, 192),
    )


def test_p92_empirical_sign_stability_radii_are_exact():
    certificate = certify_p92_empirical_sign_coherence_obstruction_exact(
        _empirical_law()
    )
    assert certificate.sign_stability_radii == (
        Fraction(1, 24),
        Fraction(3, 56),
        Fraction(5, 72),
    )
    assert certificate.certified_radius == Fraction(1, 24)
    assert certificate.determinant_product == Fraction(-5, 589824)


def test_p92_first_minor_hits_zero_exactly_at_one_over_24():
    matrix = (
        (Fraction(1, 24), Fraction(5, 24)),
        (Fraction(1, 8), Fraction(1, 8)),
    )
    radius = determinant_sign_stability_radius_exact(matrix)
    assert radius == Fraction(1, 24)
    boundary = (
        (matrix[0][0] + radius, matrix[0][1] - radius),
        (matrix[1][0] - radius, matrix[1][1] + radius),
    )
    assert boundary == (
        (Fraction(1, 12), Fraction(1, 6)),
        (Fraction(1, 12), Fraction(1, 6)),
    )
    assert determinant_2_by_2_exact(boundary) == 0


def test_p92_p75_three_minor_factorization_is_exact_for_generic_mixture():
    parameters = (
        Fraction(2, 5),
        Fraction(3, 5),
        Fraction(4, 5),
        Fraction(1, 5),
        Fraction(3, 4),
        Fraction(2, 7),
        Fraction(5, 7),
        Fraction(1, 3),
        Fraction(6, 7),
    )
    certificate = p92_model_sign_factorization_exact(parameters)
    assert certificate.actual_determinants == certificate.factorized_determinants
    assert certificate.determinant_product >= 0
    assert certificate.sign_coherent


def test_p92_p75_sign_coherence_survives_boundary_parameters():
    parameters = (
        Fraction(1, 2),
        Fraction(1),
        Fraction(0),
        Fraction(0),
        Fraction(1),
        Fraction(1),
        Fraction(0),
        Fraction(0),
        Fraction(1),
    )
    certificate = p92_model_sign_factorization_exact(parameters)
    assert certificate.actual_determinants == certificate.factorized_determinants
    assert certificate.determinant_product == 0
    assert certificate.sign_coherent


def test_p92_explicit_mixed_upper_certificate_closes_exact_distance():
    certificate = certify_p92_exact_global_distance(
        _empirical_law(), _mixed_upper_parameters()
    )
    assert certificate.exact_distance == Fraction(1, 24)
    assert certificate.lower.certified_radius == Fraction(1, 24)
    assert certificate.upper_distance == Fraction(1, 24)
    assert certificate.upper_prevalence == Fraction(4, 5)
    assert certificate.conclusion == "exact global full-cube P75 L-infinity distance certified"


def test_p92_upper_point_reaches_sign_coherence_boundary():
    certificate = p92_model_sign_factorization_exact(_mixed_upper_parameters())
    assert certificate.actual_determinants == (
        Fraction(0),
        Fraction(1, 120),
        Fraction(3, 160),
    )
    assert certificate.determinant_product == 0


def test_p92_sign_radius_rejects_zero_determinant():
    matrix = (
        (Fraction(1, 4), Fraction(1, 4)),
        (Fraction(1, 4), Fraction(1, 4)),
    )
    with pytest.raises(ValueError, match="determinant must be nonzero"):
        determinant_sign_stability_radius_exact(matrix)


def test_p92_source_keeps_scientific_interpretation_boundary():
    source = (
        __import__(
            "consciousness_bridge.exact_global_mixed_prevalence_distance",
            fromlist=["dummy"],
        ).__doc__
        or ""
    ).lower()
    assert "conditional" in source
    assert "does not identify" in source
    assert "consciousness" in source
    assert "nonphysicality" in source
    assert "physical-to-experiential bridge" in source
