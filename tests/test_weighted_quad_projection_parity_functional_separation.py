from fractions import Fraction
from itertools import product

from consciousness_bridge.certified_continuous_model_separation import P78ParameterBox
from consciousness_bridge.triple_projection_parity_functional_separation import (
    p75_box_p85_linf_lower_bound_exact,
)
from consciousness_bridge.weighted_quad_projection_parity_functional_separation import (
    empirical_weighted_parity_quad_exact,
    p75_box_p86_linf_lower_bound_exact,
    p75_box_weighted_quad_parity_witness_exact,
    p75_weighted_parity_quad_interval_exact,
    p86_dominates_p85_on_box,
    p86_standard_weight_pattern_count,
    p86_standard_weighted_quad_count,
    weighted_parity_quad_centered_coefficient_norm_exact,
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


def _strict_terms():
    return (
        ((0, 2), 1),
        ((1, 3), -1),
        ((1, 2, 3), -2),
        ((0, 1, 2, 3), 1),
    )


def _vertex_functional_value(parameters, terms):
    prevalence = parameters[0]
    value = Fraction(0)
    for views, coefficient in terms:
        minus_product = Fraction(1)
        plus_product = Fraction(1)
        for view in views:
            minus_product *= 1 - 2 * parameters[1 + 2 * view]
            plus_product *= 1 - 2 * parameters[2 + 2 * view]
        minus_probability = (1 + minus_product) / 2
        plus_probability = (1 + plus_product) / 2
        value += coefficient * (
            (1 - prevalence) * minus_probability + prevalence * plus_probability
        )
    return value


def test_p86_standard_family_has_10560_minimally_weighted_functionals():
    assert p86_standard_weight_pattern_count() == 32
    assert p86_standard_weighted_quad_count() == 10560


def test_p86_strict_functional_has_exact_empirical_value_interval_and_norm():
    empirical = _strict_empirical_law()
    box = _strict_box()
    terms = _strict_terms()

    assert empirical_weighted_parity_quad_exact(empirical, terms) == Fraction(-13, 12)
    assert p75_weighted_parity_quad_interval_exact(box, terms) == (
        Fraction(-1),
        Fraction(1),
    )
    assert weighted_parity_quad_centered_coefficient_norm_exact(terms) == (
        Fraction(16),
        Fraction(-1),
    )


def test_p86_interval_matches_exhaustive_parameter_vertex_evaluation():
    box = _strict_box()
    terms = _strict_terms()
    endpoints = tuple(
        (lower,) if lower == upper else (lower, upper)
        for lower, upper in zip(box.lower, box.upper, strict=True)
    )
    values = tuple(
        _vertex_functional_value(parameters, terms)
        for parameters in product(*endpoints)
    )
    assert p75_weighted_parity_quad_interval_exact(box, terms) == (
        min(values),
        max(values),
    )


def test_p86_is_strictly_stronger_than_complete_p85_on_exact_witness():
    empirical = _strict_empirical_law()
    box = _strict_box()

    p85 = p75_box_p85_linf_lower_bound_exact(empirical, box)
    witness = p75_box_weighted_quad_parity_witness_exact(empirical, box)
    p86 = p75_box_p86_linf_lower_bound_exact(empirical, box)

    assert p85 == 0
    assert witness.lower_bound == Fraction(1, 192)
    assert witness.terms == _strict_terms()
    assert witness.empirical_value == Fraction(-13, 12)
    assert witness.interval_lower == Fraction(-1)
    assert witness.interval_upper == Fraction(1)
    assert witness.interval_gap == Fraction(1, 12)
    assert witness.centered_coefficient_norm == Fraction(16)
    assert witness.centering_constant == Fraction(-1)
    assert p86 == Fraction(1, 192)
    assert p86_dominates_p85_on_box(empirical, box)


def test_p86_source_keeps_scientific_interpretation_boundary():
    source = (
        __import__(
            "consciousness_bridge.weighted_quad_projection_parity_functional_separation",
            fromlist=["dummy"],
        ).__doc__
        or ""
    ).lower()
    assert "does not identify" in source
    assert "consciousness" in source
    assert "physical-to-experiential bridge" in source
