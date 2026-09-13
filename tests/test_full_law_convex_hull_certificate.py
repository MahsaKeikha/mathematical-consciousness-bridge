from fractions import Fraction

import pytest

from consciousness_bridge.bounded_primitive_quad_projection_parity_functional_separation import (
    p75_box_p87_linf_lower_bound_exact,
)
from consciousness_bridge.full_law_convex_hull_certificate import (
    centered_full_law_coefficient_norm_exact,
    certify_p88_convex_hull_optimum_exact,
    certify_p88_hierarchy_exact,
    p75_box_full_law_linear_interval_exact,
    p75_box_full_law_linear_witness_exact,
    p75_box_law_vertices_exact,
    p88_convex_hull_point_exact,
    p88_strict_convex_hull_certificate_exact,
    p88_strict_convex_hull_weights,
    p88_strict_hierarchy_certificate_exact,
    p88_strict_linear_coefficients,
    p88_strict_witness_box,
    p88_strict_witness_empirical_law,
)


def test_p88_strict_box_has_16_distinct_full_law_vertices():
    assert len(p75_box_law_vertices_exact(p88_strict_witness_box())) == 16


def test_p88_strict_two_cell_linear_witness_is_exact():
    empirical = p88_strict_witness_empirical_law()
    box = p88_strict_witness_box()
    coefficients = p88_strict_linear_coefficients()

    assert centered_full_law_coefficient_norm_exact(coefficients) == (
        Fraction(2),
        Fraction(0),
    )
    assert p75_box_full_law_linear_interval_exact(box, coefficients) == (
        Fraction(-9, 16),
        Fraction(0),
    )

    witness = p75_box_full_law_linear_witness_exact(
        empirical,
        box,
        coefficients,
    )
    assert witness.empirical_value == Fraction(1, 8)
    assert witness.support_lower == Fraction(-9, 16)
    assert witness.support_upper == Fraction(0)
    assert witness.support_gap == Fraction(1, 8)
    assert witness.centered_coefficient_norm == Fraction(2)
    assert witness.centering_constant == Fraction(0)
    assert witness.lower_bound == Fraction(1, 16)


def test_p88_strict_convex_hull_weights_are_exact_probability_weights():
    weights = p88_strict_convex_hull_weights()
    assert len(weights) == 7
    assert sum((weight for weight, _ in weights), start=Fraction(0)) == 1
    assert all(weight > 0 for weight, _ in weights)


def test_p88_strict_convex_hull_upper_witness_is_exact():
    point = p88_convex_hull_point_exact(
        p88_strict_witness_empirical_law(),
        p88_strict_witness_box(),
        p88_strict_convex_hull_weights(),
    )
    assert point.distance == Fraction(1, 16)
    assert point.law == (
        Fraction(0),
        Fraction(5, 48),
        Fraction(0),
        Fraction(5, 48),
        Fraction(0),
        Fraction(1, 16),
        Fraction(0),
        Fraction(1, 16),
        Fraction(1, 16),
        Fraction(5, 48),
        Fraction(1, 16),
        Fraction(7, 48),
        Fraction(1, 48),
        Fraction(1, 16),
        Fraction(1, 48),
        Fraction(3, 16),
    )


def test_p88_matching_linear_and_convex_witnesses_certify_optimum():
    certificate = p88_strict_convex_hull_certificate_exact()
    assert certificate.optimum == Fraction(1, 16)
    assert certificate.linear_witness.lower_bound == Fraction(1, 16)
    assert certificate.convex_hull_point.distance == Fraction(1, 16)


def test_p88_full_hierarchy_is_strictly_stronger_than_p87_on_common_witness():
    empirical = p88_strict_witness_empirical_law()
    box = p88_strict_witness_box()
    p87 = p75_box_p87_linf_lower_bound_exact(empirical, box)
    p88 = p88_strict_hierarchy_certificate_exact()

    assert p87 == Fraction(1, 96)
    assert p88.p87_lower_bound == Fraction(1, 96)
    assert p88.convex_hull_lower_bound == Fraction(1, 16)
    assert p88.lower_bound == Fraction(1, 16)
    assert p88.lower_bound == max(p88.p87_lower_bound, p88.convex_hull_lower_bound)
    assert p88.lower_bound - p87 == Fraction(5, 96)
    assert p88.lower_bound / p87 == 6


def test_p88_direct_convex_hull_certifier_matches_strict_helper():
    direct = certify_p88_convex_hull_optimum_exact(
        p88_strict_witness_empirical_law(),
        p88_strict_witness_box(),
        p88_strict_linear_coefficients(),
        p88_strict_convex_hull_weights(),
    )
    assert direct == p88_strict_convex_hull_certificate_exact()


def test_p88_direct_hierarchy_certifier_matches_strict_helper():
    direct = certify_p88_hierarchy_exact(
        p88_strict_witness_empirical_law(),
        p88_strict_witness_box(),
        p88_strict_linear_coefficients(),
        p88_strict_convex_hull_weights(),
    )
    assert direct == p88_strict_hierarchy_certificate_exact()


def test_p88_rejects_convex_weights_that_do_not_sum_to_one():
    weights = list(p88_strict_convex_hull_weights())
    weight, vertex = weights[0]
    weights[0] = (weight + Fraction(1, 1000), vertex)
    with pytest.raises(ValueError, match="sum exactly to one"):
        p88_convex_hull_point_exact(
            p88_strict_witness_empirical_law(),
            p88_strict_witness_box(),
            tuple(weights),
        )


def test_p88_rejects_constant_linear_functional():
    with pytest.raises(ValueError, match="nonconstant"):
        centered_full_law_coefficient_norm_exact((Fraction(1),) * 16)


def test_p88_source_preserves_scientific_boundary():
    source = (
        __import__(
            "consciousness_bridge.full_law_convex_hull_certificate",
            fromlist=["dummy"],
        ).__doc__
        or ""
    ).lower()
    assert "complete *linear full-law* relaxation" in source
    assert "convex hull equals the nonlinear p75" in source
    assert "consciousness" in source
    assert "nonphysicality" in source
    assert "physical-to-experiential bridge" in source
