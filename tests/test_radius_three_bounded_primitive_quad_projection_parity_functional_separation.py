from fractions import Fraction
from functools import lru_cache

import pytest

from consciousness_bridge.certified_continuous_model_separation import P78ParameterBox
from consciousness_bridge.bounded_primitive_quad_projection_parity_functional_separation import (
    p75_box_p87_linf_lower_bound_exact,
)
from consciousness_bridge.radius_three_bounded_primitive_quad_projection_parity_functional_separation import (
    empirical_radius_three_primitive_parity_quad_exact,
    p75_box_p88_linf_lower_bound_exact,
    p75_box_radius_three_bounded_primitive_quad_parity_witness_exact,
    p75_radius_three_primitive_parity_quad_interval_exact,
    p88_dominates_p87_on_box,
    p88_standard_primitive_quad_count,
    p88_standard_primitive_weight_pattern_count,
    radius_three_primitive_parity_quad_centered_coefficient_norm_exact,
)

# This regression file is also a watched source for the guarded P88 publication sync.


def _strict_box() -> P78ParameterBox:
    return P78ParameterBox(
        lower=(
            Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1, 4),
            Fraction(3, 4), Fraction(1, 2), Fraction(1, 2), Fraction(1, 4), Fraction(3, 4),
        ),
        upper=(
            Fraction(0), Fraction(1), Fraction(1), Fraction(1),
            Fraction(3, 4), Fraction(1), Fraction(3, 4), Fraction(1), Fraction(1),
        ),
    )


def _strict_empirical_law() -> tuple[Fraction, ...]:
    counts = (0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
    return tuple(Fraction(count, 24) for count in counts)


def _strict_terms():
    return (
        ((0, 2), 1),
        ((1, 3), -1),
        ((1, 2, 3), -3),
        ((0, 1, 2, 3), 2),
    )


@lru_cache(maxsize=1)
def _exhaustive_p88_witness():
    return p75_box_radius_three_bounded_primitive_quad_parity_witness_exact(
        _strict_empirical_law(), _strict_box()
    )


def test_p88_family_has_632_patterns_and_208560_functionals():
    assert p88_standard_primitive_weight_pattern_count() == 632
    assert p88_standard_primitive_quad_count() == 208560


def test_p88_strict_functional_has_exact_value_interval_and_norm():
    empirical = _strict_empirical_law()
    box = _strict_box()
    terms = _strict_terms()
    assert empirical_radius_three_primitive_parity_quad_exact(empirical, terms) == Fraction(-11, 8)
    assert p75_radius_three_primitive_parity_quad_interval_exact(box, terms) == (Fraction(-1), Fraction(2))
    assert radius_three_primitive_parity_quad_centered_coefficient_norm_exact(terms) == (Fraction(24), Fraction(-1))


def test_p88_exhaustive_family_attains_exact_1_over_64_witness():
    witness = _exhaustive_p88_witness()
    assert witness.lower_bound == Fraction(1, 64)
    assert witness.terms == _strict_terms()
    assert witness.empirical_value == Fraction(-11, 8)
    assert witness.interval_lower == Fraction(-1)
    assert witness.interval_upper == Fraction(2)
    assert witness.interval_gap == Fraction(3, 8)
    assert witness.centered_coefficient_norm == Fraction(24)
    assert witness.centering_constant == Fraction(-1)


def test_p88_is_strictly_stronger_than_p87_on_same_box():
    empirical = _strict_empirical_law()
    box = _strict_box()
    p87 = p75_box_p87_linf_lower_bound_exact(empirical, box)
    p88 = p75_box_p88_linf_lower_bound_exact(empirical, box)
    assert p87 == Fraction(1, 96)
    assert p88 == Fraction(1, 64)
    assert p88 > p87
    assert p88_dominates_p87_on_box(empirical, box)


def test_p88_rejects_nonprimitive_all_three_coefficients():
    terms = (
        ((0, 1), 3), ((0, 2), -3), ((1, 3), 3), ((0, 1, 2, 3), -3)
    )
    with pytest.raises(ValueError, match="primitive"):
        p75_radius_three_primitive_parity_quad_interval_exact(_strict_box(), terms)


def test_p88_source_keeps_scientific_interpretation_boundary():
    source = (
        __import__(
            "consciousness_bridge.radius_three_bounded_primitive_quad_projection_parity_functional_separation",
            fromlist=["dummy"],
        ).__doc__
        or ""
    ).lower()
    assert "conditional" in source
    assert "does not identify" in source
    assert "consciousness" in source
    assert "physical-to-experiential bridge" in source
