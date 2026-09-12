from fractions import Fraction
from itertools import product
from pathlib import Path

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    p75_four_view_law_exact,
)
from consciousness_bridge.joint_projection_parity_contrast_separation import (
    p75_box_p84_linf_lower_bound_exact,
)
from consciousness_bridge.triple_projection_parity_functional_separation import (
    certified_p75_linf_branch_and_bound_triple_parity,
    empirical_signed_parity_triple_exact,
    p75_box_p85_linf_lower_bound_exact,
    p75_box_triple_parity_linf_lower_bound_exact,
    p75_box_triple_parity_witness_exact,
    p75_signed_parity_triple_interval_exact,
    p85_dominates_p84_on_box,
    p85_standard_triple_count,
    parity_triple_centered_coefficient_norm_exact,
)


STRICT_TERMS = (
    ((0, 2), 1),
    ((0, 1, 2), 1),
    ((0, 1, 2, 3), 1),
)


def _strict_witness_box() -> P78ParameterBox:
    return P78ParameterBox(
        lower=(
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction(1, 2),
            Fraction(1, 2),
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction(1),
        ),
        upper=(
            Fraction(1, 2),
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(1, 2),
            Fraction(1),
        ),
    )


def _strict_witness_empirical_law() -> tuple[Fraction, ...]:
    masses = {
        (0, 0, 1, 0): Fraction(1, 4),
        (0, 1, 0, 0): Fraction(1, 8),
        (1, 0, 0, 0): Fraction(1, 8),
        (1, 1, 0, 1): Fraction(1, 8),
        (1, 1, 1, 0): Fraction(3, 8),
    }
    return tuple(masses.get(outcome, Fraction(0)) for outcome in product((0, 1), repeat=4))


def _all_box_vertices(box: P78ParameterBox) -> tuple[tuple[Fraction, ...], ...]:
    coordinates = tuple(
        (lower,) if lower == upper else (lower, upper)
        for lower, upper in zip(box.lower, box.upper, strict=True)
    )
    return tuple(product(*coordinates))


def test_p85_standard_family_contains_660_sign_normalized_triples() -> None:
    assert p85_standard_triple_count() == 660


def test_p85_triple_interval_matches_exhaustive_parameter_vertices() -> None:
    box = P78ParameterBox(
        lower=(
            Fraction(1, 4),
            Fraction(1, 5),
            Fraction(1, 3),
            Fraction(1, 7),
            Fraction(1, 2),
            Fraction(1, 4),
            Fraction(2, 5),
            Fraction(1, 6),
            Fraction(3, 8),
        ),
        upper=(
            Fraction(3, 4),
            Fraction(2, 5),
            Fraction(2, 3),
            Fraction(3, 7),
            Fraction(4, 5),
            Fraction(3, 5),
            Fraction(3, 4),
            Fraction(1, 2),
            Fraction(7, 8),
        ),
    )
    terms = (((0, 1), 1), ((0, 2, 3), -1), ((1, 2, 3), 1))

    exact_interval = p75_signed_parity_triple_interval_exact(box, terms)
    vertex_values = tuple(
        empirical_signed_parity_triple_exact(
            p75_four_view_law_exact(vertex),
            terms,
        )
        for vertex in _all_box_vertices(box)
    )

    assert exact_interval == (min(vertex_values), max(vertex_values))


def test_centered_coefficient_transfer_is_exact_on_named_strict_functional() -> None:
    norm, center = parity_triple_centered_coefficient_norm_exact(STRICT_TERMS)
    assert norm == Fraction(12)
    assert center == Fraction(1)


def test_p85_is_strictly_stronger_than_p84_on_exact_rational_witness() -> None:
    box = _strict_witness_box()
    empirical = _strict_witness_empirical_law()

    p84 = p75_box_p84_linf_lower_bound_exact(empirical, box)
    triple = p75_box_triple_parity_linf_lower_bound_exact(empirical, box)
    p85 = p75_box_p85_linf_lower_bound_exact(empirical, box)
    witness = p75_box_triple_parity_witness_exact(empirical, box)

    assert p84 == Fraction(0)
    assert triple == Fraction(1, 32)
    assert p85 == Fraction(1, 32)
    assert p85 > p84
    assert witness.lower_bound == Fraction(1, 32)
    assert witness.terms == STRICT_TERMS
    assert witness.empirical_value == Fraction(5, 8)
    assert (witness.interval_lower, witness.interval_upper) == (
        Fraction(1),
        Fraction(2),
    )
    assert witness.interval_gap == Fraction(3, 8)
    assert witness.centered_coefficient_norm == Fraction(12)
    assert witness.centering_constant == Fraction(1)


def test_named_strict_triple_has_exact_five_over_eight_vs_one_to_two_gap() -> None:
    box = _strict_witness_box()
    empirical = _strict_witness_empirical_law()

    interval = p75_signed_parity_triple_interval_exact(box, STRICT_TERMS)
    observed = empirical_signed_parity_triple_exact(empirical, STRICT_TERMS)

    assert interval == (Fraction(1), Fraction(2))
    assert observed == Fraction(5, 8)
    assert interval[0] - observed == Fraction(3, 8)


def test_p85_always_dominates_p84_on_same_box() -> None:
    empirical = tuple(Fraction(1, 16) for _ in range(16))
    box = P78ParameterBox(
        lower=(Fraction(1, 8),) * 9,
        upper=(Fraction(7, 8),) * 9,
    )

    p84 = p75_box_p84_linf_lower_bound_exact(empirical, box)
    p85 = p75_box_p85_linf_lower_bound_exact(empirical, box)

    assert p85 >= p84
    assert p85_dominates_p84_on_box(empirical, box)


def test_p85_validation_rejects_duplicate_views_and_invalid_sign() -> None:
    box = P78ParameterBox.unit_cube()

    with pytest.raises(ValueError, match="view sets must be distinct"):
        p75_signed_parity_triple_interval_exact(
            box,
            (((0, 1), 1), ((0, 1), -1), ((1, 2), 1)),
        )

    with pytest.raises(ValueError, match="signs must be integers"):
        p75_signed_parity_triple_interval_exact(
            box,
            (((0, 1), 1), ((0, 2), 0), ((1, 2), 1)),
        )


def test_p85_branch_and_bound_returns_valid_exact_rational_bracket() -> None:
    counts = tuple(
        4 if sum(pattern) % 2 == 0 else 0
        for pattern in product((0, 1), repeat=4)
    )
    certificate = certified_p75_linf_branch_and_bound_triple_parity(
        counts,
        max_leaves=2,
    )

    assert Fraction(0) <= certificate.lower_bound <= certificate.upper_bound <= 1
    assert certificate.root_p84_bound <= certificate.root_p85_bound
    assert certificate.root_triple_bound <= certificate.root_p85_bound
    assert certificate.root_tightening_over_p84 >= 0
    assert certificate.certified_gap == certificate.upper_bound - certificate.lower_bound
    assert certificate.leaf_count <= 2
    assert certificate.evaluated_boxes >= 1


def test_p85_source_states_exactness_strictness_and_scientific_boundary() -> None:
    source = Path(
        "src/consciousness_bridge/triple_projection_parity_functional_separation.py"
    ).read_text(encoding="utf-8")

    required = (
        "660 standard",
        "exact P75 box interval",
        "never weaker than P84",
        "strictly stronger",
        "5/8",
        "3/8",
        "1/32",
        "rejects only the",
        "identify the latent state with consciousness",
        "prove consciousness is nonphysical",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in source
