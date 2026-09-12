from fractions import Fraction
from itertools import product
from pathlib import Path

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    p75_four_view_law_exact,
)
from consciousness_bridge.quadruple_projection_parity_functional_separation import (
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
TERMS = (
    ((0, 1), 1),
    ((0, 2), -1),
    ((0, 2, 3), 1),
    ((1, 2, 3), -1),
)


def strict_box() -> P78ParameterBox:
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


def strict_empirical_law() -> tuple[Fraction, ...]:
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


def test_p86_standard_family_has_2640_functionals() -> None:
    assert p86_standard_quadruple_count() == 2640


def test_quadruple_interval_matches_all_parameter_vertices() -> None:
    box = strict_box()
    exact_interval = p75_signed_parity_quadruple_interval_exact(box, TERMS)
    endpoint_coordinates = tuple(
        (lower,) if lower == upper else (lower, upper)
        for lower, upper in zip(box.lower, box.upper, strict=True)
    )
    values = []
    for parameters in product(*endpoint_coordinates):
        law = p75_four_view_law_exact(parameters)
        values.append(empirical_signed_parity_quadruple_exact(law, TERMS))
    assert exact_interval == (min(values), max(values))
    assert exact_interval == (Fraction(-1), Fraction(1, 2))


def test_centered_transfer_norm_is_exact_for_strict_witness() -> None:
    norm, center = parity_quadruple_centered_coefficient_norm_exact(TERMS)
    assert norm == 12
    assert center == 0


def test_p86_strictly_improves_complete_p85_on_exact_rational_witness() -> None:
    box = strict_box()
    empirical = strict_empirical_law()
    assert p75_box_p85_linf_lower_bound_exact(empirical, box) == 0

    witness = p75_box_quadruple_parity_witness_exact(empirical, box)
    assert witness.lower_bound == Fraction(1, 48)
    assert witness.terms == TERMS
    assert witness.empirical_value == Fraction(3, 4)
    assert witness.interval_lower == -1
    assert witness.interval_upper == Fraction(1, 2)
    assert witness.interval_gap == Fraction(1, 4)
    assert witness.centered_coefficient_norm == 12
    assert witness.centering_constant == 0
    assert p75_box_p86_linf_lower_bound_exact(empirical, box) == Fraction(1, 48)


def test_p86_dominates_p85_by_construction() -> None:
    assert p86_dominates_p85_on_box(strict_empirical_law(), strict_box())


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
