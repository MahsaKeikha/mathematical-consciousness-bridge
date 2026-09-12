from fractions import Fraction
from itertools import product
from pathlib import Path

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    p75_four_view_law_exact,
)
from consciousness_bridge.nested_projection_contrast_separation import (
    p75_box_p82_linf_lower_bound_exact,
)
from consciousness_bridge.projection_event_model_separation import (
    p75_box_p81_linf_lower_bound_exact,
)
from consciousness_bridge.signed_cylinder_contrast_separation import (
    certified_p75_linf_branch_and_bound_signed_contrast,
    empirical_signed_cylinder_contrast_exact,
    p75_box_p83_linf_lower_bound_exact,
    p75_box_signed_cylinder_contrast_linf_lower_bound_exact,
    p75_box_signed_cylinder_contrast_witness_exact,
    p75_signed_cylinder_contrast_interval_exact,
    p83_dominates_p82_on_box,
    p83_standard_signed_contrast_count,
    signed_cylinder_coefficient_l1_norm,
)
from consciousness_bridge.simplex_coupled_model_separation import (
    p75_box_simplex_linf_lower_bound_exact,
)


def _strict_witness_box() -> P78ParameterBox:
    return P78ParameterBox(
        lower=(
            Fraction(0),
            Fraction(1, 4),
            Fraction(0),
            Fraction(1),
            Fraction(3, 4),
            Fraction(0),
            Fraction(3, 4),
            Fraction(1, 2),
            Fraction(3, 4),
        ),
        upper=(
            Fraction(1),
            Fraction(1, 4),
            Fraction(0),
            Fraction(1),
            Fraction(3, 4),
            Fraction(0),
            Fraction(3, 4),
            Fraction(1, 2),
            Fraction(3, 4),
        ),
    )


def _strict_witness_empirical_law() -> tuple[Fraction, ...]:
    return (
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(5, 64),
        Fraction(9, 32),
        Fraction(19, 64),
        Fraction(1, 64),
        Fraction(5, 32),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(1, 8),
        Fraction(3, 64),
        Fraction(0),
        Fraction(0),
    )


def _all_box_vertices(box: P78ParameterBox) -> tuple[tuple[Fraction, ...], ...]:
    coordinates = tuple(
        (lower,) if lower == upper else (lower, upper)
        for lower, upper in zip(box.lower, box.upper, strict=True)
    )
    return tuple(product(*coordinates))


def test_p83_standard_family_contains_2696_genuinely_new_non_nested_pairs() -> None:
    assert p83_standard_signed_contrast_count() == 2696


def test_signed_contrast_interval_matches_exhaustive_parameter_box_vertices() -> None:
    box = P78ParameterBox(
        lower=(
            Fraction(1, 5),
            Fraction(1, 6),
            Fraction(1, 4),
            Fraction(1, 7),
            Fraction(1, 3),
            Fraction(1, 8),
            Fraction(2, 5),
            Fraction(1, 9),
            Fraction(3, 8),
        ),
        upper=(
            Fraction(4, 5),
            Fraction(2, 3),
            Fraction(3, 4),
            Fraction(5, 7),
            Fraction(4, 5),
            Fraction(3, 5),
            Fraction(7, 8),
            Fraction(2, 3),
            Fraction(8, 9),
        ),
    )
    positive_views = (0, 2)
    positive_assignment = (1, 0)
    negative_views = (1, 3)
    negative_assignment = (0, 1)

    exact_interval = p75_signed_cylinder_contrast_interval_exact(
        box,
        positive_views,
        positive_assignment,
        negative_views,
        negative_assignment,
    )
    vertex_values = tuple(
        empirical_signed_cylinder_contrast_exact(
            p75_four_view_law_exact(vertex),
            positive_views,
            positive_assignment,
            negative_views,
            negative_assignment,
        )
        for vertex in _all_box_vertices(box)
    )

    assert exact_interval == (min(vertex_values), max(vertex_values))


def test_signed_contrast_l1_norm_is_symmetric_difference_cardinality() -> None:
    assert signed_cylinder_coefficient_l1_norm(
        (0,),
        (1,),
        (1,),
        (1,),
    ) == 8
    assert signed_cylinder_coefficient_l1_norm(
        (0, 1, 2, 3),
        (1, 1, 0, 0),
        (0, 1, 2, 3),
        (1, 1, 0, 1),
    ) == 2


def test_p83_strictly_improves_p82_on_clean_exact_rational_witness() -> None:
    box = _strict_witness_box()
    empirical = _strict_witness_empirical_law()

    p80 = p75_box_simplex_linf_lower_bound_exact(empirical, box)
    p81 = p75_box_p81_linf_lower_bound_exact(empirical, box)
    p82 = p75_box_p82_linf_lower_bound_exact(empirical, box)
    signed = p75_box_signed_cylinder_contrast_linf_lower_bound_exact(empirical, box)
    p83 = p75_box_p83_linf_lower_bound_exact(empirical, box)
    witness = p75_box_signed_cylinder_contrast_witness_exact(empirical, box)

    assert p80 == 0
    assert p81 == 0
    assert p82 == 0
    assert signed == Fraction(5, 128)
    assert p83 == Fraction(5, 128)
    assert p83 > p82

    assert witness.lower_bound == Fraction(5, 128)
    assert witness.positive_views == (0, 1, 2, 3)
    assert witness.positive_assignment == (1, 1, 0, 0)
    assert witness.negative_views == (0, 1, 2, 3)
    assert witness.negative_assignment == (1, 1, 0, 1)
    assert witness.coefficient_l1_norm == 2
    assert witness.empirical_contrast == Fraction(5, 64)
    assert witness.interval_lower == 0
    assert witness.interval_upper == 0
    assert witness.positive_empirical_probability == Fraction(1, 8)
    assert witness.negative_empirical_probability == Fraction(3, 64)
    assert witness.positive_interval_lower <= witness.positive_empirical_probability
    assert witness.positive_empirical_probability <= witness.positive_interval_upper
    assert witness.negative_interval_lower <= witness.negative_empirical_probability
    assert witness.negative_empirical_probability <= witness.negative_interval_upper


def test_p83_always_dominates_p82_on_same_box() -> None:
    empirical = tuple(Fraction(1, 16) for _ in range(16))
    box = P78ParameterBox(
        lower=(Fraction(1, 8),) * 9,
        upper=(Fraction(7, 8),) * 9,
    )

    p82 = p75_box_p82_linf_lower_bound_exact(empirical, box)
    p83 = p75_box_p83_linf_lower_bound_exact(empirical, box)

    assert p83 >= p82
    assert p83_dominates_p82_on_box(empirical, box)


def test_p83_branch_and_bound_returns_valid_exact_rational_bracket() -> None:
    counts = tuple(
        4 if sum(pattern) % 2 == 0 else 0
        for pattern in product((0, 1), repeat=4)
    )
    certificate = certified_p75_linf_branch_and_bound_signed_contrast(
        counts,
        max_leaves=4,
    )

    assert Fraction(0) <= certificate.lower_bound <= certificate.upper_bound <= 1
    assert certificate.p78_active_lower_bound <= certificate.p80_active_lower_bound
    assert certificate.p80_active_lower_bound <= certificate.p81_active_lower_bound
    assert certificate.p81_active_lower_bound <= certificate.p82_active_lower_bound
    assert certificate.p82_active_lower_bound <= certificate.lower_bound
    assert certificate.root_p78_bound <= certificate.root_p80_bound
    assert certificate.root_p80_bound <= certificate.root_p81_bound
    assert certificate.root_p81_bound <= certificate.root_p82_bound
    assert certificate.root_p82_bound <= certificate.root_p83_bound
    assert certificate.root_signed_contrast_bound <= certificate.root_p83_bound
    assert certificate.root_tightening_over_p82 >= 0
    assert certificate.leaf_count == 4
    assert certificate.evaluated_boxes == 2 * certificate.iterations + 1
    assert certificate.certified_gap == certificate.upper_bound - certificate.lower_bound


def test_p83_source_states_exactness_scope_and_scientific_boundary() -> None:
    source = Path(
        "src/consciousness_bridge/signed_cylinder_contrast_separation.py"
    ).read_text(encoding="utf-8")

    required = (
        "multi-affine",
        "2,696",
        "never weaker than P82",
        "P80=P81=P82=0",
        "P83=5/128",
        "does not validate",
        "latent state with consciousness",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in source
