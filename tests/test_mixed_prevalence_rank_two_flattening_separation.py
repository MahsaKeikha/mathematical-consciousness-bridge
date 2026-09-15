from fractions import Fraction

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    empirical_law_from_counts,
    p75_four_view_law_exact,
)
from consciousness_bridge.mixed_prevalence_rank_two_flattening_separation import (
    all_3_by_3_flattening_minors_exact,
    certify_p91_mixed_prevalence_bracket_exact,
    determinant_3_by_3_exact,
    p91_bipartite_flattening_exact,
    p91_minor_interval_certificate_exact,
    p91_selected_minor_exact,
    verify_p91_mixed_upper_certificate_exact,
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


def test_p91_empirical_selected_minor_is_exactly_nonzero():
    minor = p91_selected_minor_exact(_empirical_law())
    assert minor == (
        (Fraction(1, 24), Fraction(1, 12), Fraction(1, 8)),
        (Fraction(1, 8), Fraction(0), Fraction(0)),
        (Fraction(1, 24), Fraction(5, 24), Fraction(1, 8)),
    )
    assert determinant_3_by_3_exact(minor) == Fraction(1, 512)


def test_p91_canonical_flattening_has_expected_empirical_layout():
    flattening = p91_bipartite_flattening_exact(_empirical_law())
    assert flattening == (
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1, 24)),
        (Fraction(1, 24), Fraction(1, 12), Fraction(1, 12), Fraction(1, 8)),
        (Fraction(1, 8), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(1, 24), Fraction(5, 24), Fraction(1, 8), Fraction(1, 8)),
    )


def test_p91_exact_radius_one_over_42_excludes_every_rank_two_flattening():
    certificate = p91_minor_interval_certificate_exact(
        _empirical_law(), radius=Fraction(1, 42)
    )
    assert certificate.empirical_determinant == Fraction(1, 512)
    assert certificate.vertex_count == 512
    assert certificate.minimum_vertex_determinant == Fraction(23, 677376)
    assert certificate.maximum_vertex_determinant == Fraction(2939, 677376)
    assert certificate.excludes_rank_two


def test_p91_one_over_41_is_not_certified_by_the_selected_minor_relaxation():
    certificate = p91_minor_interval_certificate_exact(
        _empirical_law(), radius=Fraction(1, 41)
    )
    assert certificate.minimum_vertex_determinant == Fraction(-7, 860672)
    assert certificate.maximum_vertex_determinant == Fraction(3793, 860672)
    assert not certificate.excludes_rank_two


def test_every_exact_p75_mixture_has_rank_at_most_two_in_p91_flattening():
    parameters = (
        Fraction(2, 5),
        Fraction(1, 5),
        Fraction(4, 5),
        Fraction(1, 3),
        Fraction(2, 3),
        Fraction(2, 7),
        Fraction(5, 7),
        Fraction(3, 8),
        Fraction(7, 8),
    )
    law = p75_four_view_law_exact(parameters)
    assert all(value == 0 for value in all_3_by_3_flattening_minors_exact(law))


def test_p91_explicit_genuinely_mixed_model_point_attains_one_over_24():
    certificate = verify_p91_mixed_upper_certificate_exact(
        _empirical_law(), _mixed_upper_parameters()
    )
    assert certificate.prevalence == Fraction(4, 5)
    assert certificate.radius == Fraction(1, 24)
    assert certificate.flattening_rank_at_most_two


def test_p91_global_mixed_prevalence_bracket_is_exactly_certified():
    certificate = certify_p91_mixed_prevalence_bracket_exact(
        _empirical_law(), _mixed_upper_parameters()
    )
    assert certificate.excluded_closed_radius == Fraction(1, 42)
    assert certificate.upper_bound == Fraction(1, 24)
    assert certificate.lower.minimum_vertex_determinant == Fraction(23, 677376)
    assert certificate.upper.prevalence == Fraction(4, 5)
    assert Fraction(1, 42) < Fraction(1, 24)


def test_p91_upper_certificate_requires_nonextreme_prevalence():
    parameters = list(_mixed_upper_parameters())
    parameters[0] = Fraction(0)
    with pytest.raises(ValueError, match="genuinely mixed prevalence"):
        verify_p91_mixed_upper_certificate_exact(_empirical_law(), tuple(parameters))


def test_p91_source_keeps_scientific_interpretation_boundary():
    source = (
        __import__(
            "consciousness_bridge.mixed_prevalence_rank_two_flattening_separation",
            fromlist=["dummy"],
        ).__doc__
        or ""
    ).lower()
    assert "conditional" in source
    assert "does not identify" in source
    assert "consciousness" in source
    assert "nonphysicality" in source
    assert "physical-to-experiential bridge" in source
