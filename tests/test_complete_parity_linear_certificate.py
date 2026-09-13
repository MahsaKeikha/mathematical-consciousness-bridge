from dataclasses import replace
from fractions import Fraction

from consciousness_bridge.bounded_primitive_quad_projection_parity_functional_separation import (
    p75_box_p87_linf_lower_bound_exact,
)
from consciousness_bridge.complete_parity_linear_certificate import (
    P88DualCertificate,
    certify_p88_optimality_exact,
    empirical_even_parity_feature_vector_exact,
    p75_box_parity_feature_vertices_exact,
    p75_box_parity_linear_interval_exact,
    p75_box_parity_linear_witness_exact,
    p88_dominates_p87_for_certified_optimum,
    p88_standard_even_view_sets,
    p88_standard_parity_dimension,
    p88_strict_dual_certificate,
    p88_strict_optimality_certificate_exact,
    p88_strict_witness_box,
    p88_strict_witness_coefficients,
    p88_strict_witness_empirical_law,
    parity_linear_centered_coefficient_norm_exact,
    verify_p88_dual_certificate_exact,
)


def test_p88_uses_all_11_nontrivial_even_parity_coordinates():
    assert p88_standard_parity_dimension() == 11
    assert p88_standard_even_view_sets() == (
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


def test_p88_strict_empirical_feature_vector_is_exact():
    assert empirical_even_parity_feature_vector_exact(
        p88_strict_witness_empirical_law()
    ) == (
        Fraction(3, 8),
        Fraction(11, 24),
        Fraction(13, 24),
        Fraction(1, 2),
        Fraction(7, 12),
        Fraction(2, 3),
        Fraction(13, 24),
        Fraction(11, 24),
        Fraction(3, 8),
        Fraction(2, 3),
        Fraction(3, 8),
    )


def test_p88_strict_functional_has_exact_interval_gap_norm_and_bound():
    empirical = p88_strict_witness_empirical_law()
    box = p88_strict_witness_box()
    coefficients = p88_strict_witness_coefficients()

    assert p75_box_parity_linear_interval_exact(box, coefficients) == (
        Fraction(3),
        Fraction(51, 8),
    )
    assert parity_linear_centered_coefficient_norm_exact(coefficients) == (
        Fraction(28),
        Fraction(3),
    )

    witness = p75_box_parity_linear_witness_exact(empirical, box, coefficients)
    assert witness.empirical_value == Fraction(13, 6)
    assert witness.interval_lower == Fraction(3)
    assert witness.interval_upper == Fraction(51, 8)
    assert witness.interval_gap == Fraction(5, 6)
    assert witness.centered_coefficient_norm == Fraction(28)
    assert witness.centering_constant == Fraction(3)
    assert witness.lower_bound == Fraction(5, 168)


def test_p88_dual_certificate_is_exactly_feasible():
    assert verify_p88_dual_certificate_exact(
        p88_strict_witness_empirical_law(),
        p88_strict_witness_box(),
        p88_strict_dual_certificate(),
    )


def test_p88_matching_primal_and_dual_certify_complete_optimum():
    certificate = p88_strict_optimality_certificate_exact()
    assert certificate.optimum == Fraction(5, 168)
    assert certificate.primal.lower_bound == certificate.dual.bound


def test_p88_is_strictly_stronger_than_p87_on_same_exact_witness():
    empirical = p88_strict_witness_empirical_law()
    box = p88_strict_witness_box()
    p87 = p75_box_p87_linf_lower_bound_exact(empirical, box)
    p88 = p88_strict_optimality_certificate_exact()

    assert p87 == Fraction(1, 96)
    assert p88.optimum == Fraction(5, 168)
    assert p88.optimum > p87
    assert p88.optimum - p87 == Fraction(13, 672)
    assert p88_dominates_p87_for_certified_optimum(empirical, box, p88)


def test_p88_feature_vertices_are_exact_and_finite():
    vertices = p75_box_parity_feature_vertices_exact(p88_strict_witness_box())
    assert len(vertices) == 16
    assert all(len(vertex) == 11 for vertex in vertices)


def test_p88_rejects_corrupted_dual_residual():
    dual = p88_strict_dual_certificate()
    corrupted_residual = list(dual.residual)
    corrupted_residual[0] += Fraction(1, 1000)
    corrupted = replace(dual, residual=tuple(corrupted_residual))
    assert not verify_p88_dual_certificate_exact(
        p88_strict_witness_empirical_law(),
        p88_strict_witness_box(),
        corrupted,
    )


def test_p88_rejects_corrupted_dual_weight():
    dual = p88_strict_dual_certificate()
    weight, vertex = dual.vertex_weights[0]
    corrupted = P88DualCertificate(
        bound=dual.bound,
        vertex_weights=((weight + Fraction(1, 1000), vertex),) + dual.vertex_weights[1:],
        residual=dual.residual,
    )
    assert not verify_p88_dual_certificate_exact(
        p88_strict_witness_empirical_law(),
        p88_strict_witness_box(),
        corrupted,
    )


def test_p88_direct_certifier_matches_strict_helper():
    direct = certify_p88_optimality_exact(
        p88_strict_witness_empirical_law(),
        p88_strict_witness_box(),
        p88_strict_witness_coefficients(),
        p88_strict_dual_certificate(),
    )
    assert direct == p88_strict_optimality_certificate_exact()


def test_p88_source_keeps_scientific_interpretation_boundary():
    source = (
        __import__(
            "consciousness_bridge.complete_parity_linear_certificate",
            fromlist=["dummy"],
        ).__doc__
        or ""
    ).lower()
    assert "conditional model-separation theorem" in source
    assert "linear parity-witness class" in source
    assert "does not prove" in source
    assert "consciousness" in source
    assert "physical-to-experiential bridge" in source
