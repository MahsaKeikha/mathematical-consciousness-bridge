from fractions import Fraction
from functools import lru_cache
from itertools import product

import pytest

from consciousness_bridge.bounded_primitive_quad_projection_parity_functional_separation import (
    empirical_primitive_parity_quad_exact,
    p75_box_bounded_primitive_quad_parity_witness_exact,
    p75_primitive_parity_quad_interval_exact,
    p87_standard_primitive_quad_count,
    p87_standard_primitive_weight_pattern_count,
    primitive_parity_quad_centered_coefficient_norm_exact,
)
from consciousness_bridge.certified_continuous_model_separation import P78ParameterBox
from consciousness_bridge.weighted_quad_projection_parity_functional_separation import (
    p75_box_p86_linf_lower_bound_exact,
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
        ((0, 1, 2, 3), 2),
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


@lru_cache(maxsize=1)
def _exhaustive_candidate_witness():
    return p75_box_bounded_primitive_quad_parity_witness_exact(
        _strict_empirical_law(),
        _strict_box(),
    )


def test_p87_candidate_family_has_120_patterns_and_39600_functionals():
    assert p87_standard_primitive_weight_pattern_count() == 120
    assert p87_standard_primitive_quad_count() == 39600


def test_p87_candidate_strict_functional_has_exact_value_interval_and_norm():
    empirical = _strict_empirical_law()
    box = _strict_box()
    terms = _strict_terms()

    assert empirical_primitive_parity_quad_exact(empirical, terms) == Fraction(-17, 24)
    assert p75_primitive_parity_quad_interval_exact(box, terms) == (
        Fraction(-1, 2),
        Fraction(2),
    )
    assert primitive_parity_quad_centered_coefficient_norm_exact(terms) == (
        Fraction(20),
        Fraction(0),
    )


def test_p87_candidate_interval_matches_exhaustive_parameter_vertices():
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
    assert p75_primitive_parity_quad_interval_exact(box, terms) == (
        min(values),
        max(values),
    )


def test_p87_candidate_exhaustive_family_attains_exact_1_over_96_witness():
    witness = _exhaustive_candidate_witness()

    assert witness.lower_bound == Fraction(1, 96)
    assert witness.terms == _strict_terms()
    assert witness.empirical_value == Fraction(-17, 24)
    assert witness.interval_lower == Fraction(-1, 2)
    assert witness.interval_upper == Fraction(2)
    assert witness.interval_gap == Fraction(5, 24)
    assert witness.centered_coefficient_norm == Fraction(20)
    assert witness.centering_constant == Fraction(0)


def test_p87_candidate_is_strictly_stronger_than_complete_p86_on_same_box():
    empirical = _strict_empirical_law()
    box = _strict_box()
    p86 = p75_box_p86_linf_lower_bound_exact(empirical, box)
    candidate = _exhaustive_candidate_witness().lower_bound

    assert p86 == Fraction(1, 192)
    assert candidate == Fraction(1, 96)
    assert candidate > p86


def test_p87_candidate_rejects_nonprimitive_all_even_coefficients():
    terms = (
        ((0, 1), 2),
        ((0, 2), -2),
        ((1, 3), 2),
        ((0, 1, 2, 3), -2),
    )
    with pytest.raises(ValueError, match="primitive"):
        p75_primitive_parity_quad_interval_exact(_strict_box(), terms)


def test_p87_candidate_source_keeps_scientific_interpretation_boundary():
    source = (
        __import__(
            "consciousness_bridge.bounded_primitive_quad_projection_parity_functional_separation",
            fromlist=["dummy"],
        ).__doc__
        or ""
    ).lower()
    assert "candidate research extension" in source
    assert "not yet the public theorem frontier" in source
    assert "does not identify" in source
    assert "consciousness" in source
    assert "physical-to-experiential bridge" in source
