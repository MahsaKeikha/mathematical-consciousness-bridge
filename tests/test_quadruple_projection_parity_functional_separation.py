from fractions import Fraction
from itertools import product
from pathlib import Path

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    p75_four_view_law_exact,
)
from consciousness_bridge.quadruple_projection_parity_functional_separation import (
    certified_p75_linf_branch_and_bound_quadruple_parity,
    empirical_signed_parity_quadruple_exact,
    p75_box_p86_linf_lower_bound_exact,
    p75_box_quadruple_parity_witness_exact,
    p75_signed_parity_quadruple_interval_exact,
    p86_dominates_p85_on_box,
    p86_standard_quadruple_count,
    parity_quadruple_centered_coefficient_norm_exact,
)
from consciousness_bridge.triple_projection_parity_functional_separation import (
    p75_box_p85_linf_lower_bound_exact,
)

ROOT = Path(__file__).resolve().parents[1]
AUDIT_TERMS = (
    ((0, 1), 1),
    ((0, 2), -1),
    ((0, 2, 3), 1),
    ((1, 2, 3), -1),
)
STRICT_TERMS = (
    ((0, 2), 1),
    ((2, 3), -1),
    ((0, 1, 2), 1),
    ((1, 2, 3), -1),
)
STRICT_COUNTS = (0, 0, 0, 3, 0, 0, 0, 0, 6, 0, 0, 0, 3, 4, 0, 0)


def audit_box() -> P78ParameterBox:
    return P78ParameterBox(
        lower=(
            Fraction(0),
            Fraction(1, 2),
            Fraction(0),
            Fraction(1, 2),
            Fraction(1, 2),
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction(0),
        ),
        upper=(
            Fraction(1, 2),
            Fraction(1),
            Fraction(1),
            Fraction(1, 2),
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(0),
            Fraction(1),
        ),
    )


def audit_empirical_law() -> tuple[Fraction, ...]:
    return (
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(1, 4),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(3, 8),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(1, 8),
        Fraction(0),
        Fraction(0),
        Fraction(1, 4),
    )


def strict_box() -> P78ParameterBox:
    return P78ParameterBox(
        lower=(
            Fraction(0),
            Fraction(1, 2),
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction(1, 2),
            Fraction(1, 2),
            Fraction(0),
            Fraction(0),
        ),
        upper=(
            Fraction(0),
            Fraction(1),
            Fraction(1, 2),
            Fraction(1, 2),
            Fraction(1),
            Fraction(1, 2),
            Fraction(1, 2),
            Fraction(1),
            Fraction(0),
        ),
    )


def strict_empirical_law() -> tuple[Fraction, ...]:
    return (
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(3, 16),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(3, 8),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(3, 16),
        Fraction(1, 4),
        Fraction(0),
        Fraction(0),
    )


def test_p86_standard_family_has_2640_functionals() -> None:
    assert p86_standard_quadruple_count() == 2640


def test_quadruple_interval_matches_all_parameter_vertices() -> None:
    box = audit_box()
    exact_interval = p75_signed_parity_quadruple_interval_exact(box, AUDIT_TERMS)
    endpoint_coordinates = tuple(
        (lower,) if lower == upper else (lower, upper)
        for lower, upper in zip(box.lower, box.upper, strict=True)
    )
    values = []
    for parameters in product(*endpoint_coordinates):
        law = p75_four_view_law_exact(parameters)
        values.append(empirical_signed_parity_quadruple_exact(law, AUDIT_TERMS))
    assert exact_interval == (min(values), max(values))
    assert exact_interval == (Fraction(-1), Fraction(1, 2))


def test_centered_transfer_norm_is_exact_for_audit_functional() -> None:
    norm, center = parity_quadruple_centered_coefficient_norm_exact(AUDIT_TERMS)
    assert norm == 12
    assert center == 0


def test_exact_strict_functional_record() -> None:
    empirical = strict_empirical_law()
    box = strict_box()
    assert empirical_signed_parity_quadruple_exact(empirical, STRICT_TERMS) == Fraction(-9, 8)
    assert p75_signed_parity_quadruple_interval_exact(box, STRICT_TERMS) == (0, 0)
    norm, center = parity_quadruple_centered_coefficient_norm_exact(STRICT_TERMS)
    assert norm == 8
    assert center == 0


def test_p86_strictly_improves_complete_p85() -> None:
    empirical = strict_empirical_law()
    box = strict_box()
    p85 = p75_box_p85_linf_lower_bound_exact(empirical, box)
    quadruple = p75_box_quadruple_parity_witness_exact(empirical, box)
    p86 = p75_box_p86_linf_lower_bound_exact(empirical, box)

    assert p85 == Fraction(5, 48)
    assert quadruple.lower_bound == Fraction(9, 64)
    assert p86 == Fraction(9, 64)
    assert p86 - p85 == Fraction(7, 192)


def test_p86_dominates_p85_by_construction() -> None:
    assert p86_dominates_p85_on_box(strict_empirical_law(), strict_box())


def test_p86_global_wrapper_returns_a_certified_root_bracket() -> None:
    result = certified_p75_linf_branch_and_bound_quadruple_parity(
        STRICT_COUNTS,
        max_leaves=1,
    )
    assert result.leaf_count == 1
    assert result.evaluated_boxes == 1
    assert result.iterations == 0
    assert result.lower_bound == result.root_p86_bound
    assert result.root_p86_bound == max(
        result.root_p85_bound,
        result.root_quadruple_bound,
    )
    assert result.root_tightening_over_p85 >= 0
    assert result.lower_bound <= result.upper_bound


def test_p86_source_keeps_scientific_interpretation_boundary() -> None:
    source = (
        ROOT
        / "src/consciousness_bridge/quadruple_projection_parity_functional_separation.py"
    ).read_text(encoding="utf-8")
    for phrase in (
        "conditional model-separation theorem",
        "does not identify the P75 latent state with consciousness",
        "prove consciousness is nonphysical",
        "physical-to-experiential bridge",
    ):
        assert phrase in source
