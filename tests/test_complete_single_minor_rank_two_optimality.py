from fractions import Fraction

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    empirical_law_from_counts,
    p75_four_view_law_exact,
)
from consciousness_bridge.complete_single_minor_rank_two_optimality import (
    MinorIndex,
    all_bipartite_minor_determinants_exact,
    all_single_minor_indices,
    certify_p92_complete_single_minor_optimality_exact,
    complete_minor_box_audit_exact,
    p75_bipartite_rank_two_factorization_exact,
)


def _empirical_law() -> tuple[Fraction, ...]:
    return empirical_law_from_counts(
        (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
    )


def _mixed_parameters() -> tuple[Fraction, ...]:
    return (
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


@pytest.fixture(scope="module")
def p92_certificate():
    return certify_p92_complete_single_minor_optimality_exact(_empirical_law())


def test_p92_complete_single_minor_class_has_exactly_48_members():
    indices = all_single_minor_indices()
    assert len(indices) == 48
    assert len(set(indices)) == 48


def test_p75_rank_two_structure_is_explicit_for_all_three_bipartitions():
    parameters = _mixed_parameters()
    law = p75_four_view_law_exact(parameters)
    for row_views in ((0, 1), (0, 2), (0, 3)):
        factorization = p75_bipartite_rank_two_factorization_exact(parameters, row_views)
        assert factorization.weights == (Fraction(3, 5), Fraction(2, 5))
        assert factorization.row_views == row_views
        assert factorization.flattening
        assert sum(factorization.row_factors[0]) == 1
        assert sum(factorization.row_factors[1]) == 1
        assert sum(factorization.column_factors[0]) == 1
        assert sum(factorization.column_factors[1]) == 1

    minors = all_bipartite_minor_determinants_exact(law)
    assert len(minors) == 48
    assert all(value == 0 for _, value in minors)


def test_p91_minor_is_unique_single_minor_certificate_at_one_over_42():
    audits = complete_minor_box_audit_exact(_empirical_law(), radius=Fraction(1, 42))
    certifying = [certificate for certificate in audits if certificate.excludes_rank_two]
    assert len(certifying) == 1
    winner = certifying[0]
    assert winner.index == MinorIndex(
        row_views=(0, 3),
        column_views=(1, 2),
        rows=(1, 2, 3),
        columns=(0, 1, 3),
    )
    assert winner.empirical_determinant == Fraction(1, 512)
    assert winner.minimum_vertex_determinant == Fraction(23, 677376)
    assert winner.maximum_vertex_determinant == Fraction(2939, 677376)
    assert winner.vertex_count == 512


def test_complete_single_minor_ranges_expand_monotonically_past_p91_radius():
    at_p91 = complete_minor_box_audit_exact(_empirical_law(), radius=Fraction(1, 42))
    at_probe = complete_minor_box_audit_exact(_empirical_law(), radius=Fraction(1, 41))

    by_index_at_p91 = {certificate.index: certificate for certificate in at_p91}
    by_index_at_probe = {certificate.index: certificate for certificate in at_probe}
    assert set(by_index_at_p91) == set(by_index_at_probe)
    assert len(by_index_at_p91) == 48

    for index, published in by_index_at_p91.items():
        probe = by_index_at_probe[index]
        assert probe.minimum_vertex_determinant <= published.minimum_vertex_determinant
        assert probe.maximum_vertex_determinant >= published.maximum_vertex_determinant

    assert sum(certificate.excludes_rank_two for certificate in at_p91) == 1
    assert all(not certificate.excludes_rank_two for certificate in at_probe)


def test_p92_selected_minor_active_vertex_polynomial_is_exact(p92_certificate):
    assert p92_certificate.active_vertex == (1, 1, 0, 0, 0, 1, 0, 0, 1)
    assert p92_certificate.active_vertex_polynomial == (
        Fraction(1, 512),
        Fraction(-17, 192),
        Fraction(1, 3),
    )
    assert p92_certificate.active_root_count_below_ceiling == 1
    assert p92_certificate.other_vertex_root_count_below_ceiling == 0


def test_p92_exact_algebraic_relaxation_ceiling_is_between_p91_probes(p92_certificate):
    ceiling = p92_certificate.exact_relaxation_ceiling
    assert (ceiling.a, ceiling.radicand, ceiling.denominator) == (17, 193, 128)
    assert ceiling.greater_than_fraction(Fraction(1, 42))
    assert ceiling.less_than_fraction(Fraction(1, 41))
    assert p92_certificate.root_audit_ceiling == Fraction(1, 41)


def test_p92_complete_certificate_states_unique_optimality(p92_certificate):
    assert p92_certificate.total_minor_count == 48
    assert p92_certificate.certifying_minor_count == 1
    assert p92_certificate.selected_empirical_determinant == Fraction(1, 512)
    assert p92_certificate.selected_minimum_at_published_radius == Fraction(23, 677376)
    assert "uniquely optimal" in p92_certificate.conclusion
    assert "(17 - sqrt(193)) / 128" in p92_certificate.conclusion


def test_p92_source_preserves_scientific_interpretation_boundary():
    source = (
        __import__(
            "consciousness_bridge.complete_single_minor_rank_two_optimality",
            fromlist=["dummy"],
        ).__doc__
        or ""
    ).lower()
    assert "not an exact solution" in source
    assert "full nonlinear p75 distance" in source
    assert "does not identify" in source
    assert "consciousness" in source
    assert "physical-to-experiential bridge" in source
