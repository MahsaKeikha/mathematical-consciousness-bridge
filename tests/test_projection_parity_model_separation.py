from fractions import Fraction
from itertools import product
from pathlib import Path

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    p75_four_view_law_exact,
)
from consciousness_bridge.nested_projection_contrast_separation import (
    p75_box_p82_linf_lower_bound_exact,
)
from consciousness_bridge.projection_parity_model_separation import (
    certified_p75_linf_branch_and_bound_parity,
    empirical_projection_parity_probability_exact,
    p75_box_p83_linf_lower_bound_exact,
    p75_box_projection_parity_linf_lower_bound_exact,
    p75_box_projection_parity_witness_exact,
    p75_projection_parity_interval_exact,
    p83_dominates_p82_on_box,
    p83_standard_parity_count,
)


def _strict_witness_box() -> P78ParameterBox:
    lower = [Fraction(0)] * 9
    upper = [Fraction(1)] * 9
    for index in (5, 6):
        lower[index] = Fraction(1, 2)
        upper[index] = Fraction(1, 2)
    return P78ParameterBox(tuple(lower), tuple(upper))


def _strict_witness_empirical_law() -> tuple[Fraction, ...]:
    return tuple(
        Fraction(1, 8) if outcome[2] == outcome[3] else Fraction(0)
        for outcome in product((0, 1), repeat=4)
    )


def _all_box_vertices(box: P78ParameterBox) -> tuple[tuple[Fraction, ...], ...]:
    coordinates = tuple(
        (lower,) if lower == upper else (lower, upper)
        for lower, upper in zip(box.lower, box.upper, strict=True)
    )
    return tuple(product(*coordinates))


def test_p83_standard_family_contains_22_genuinely_new_parities() -> None:
    assert p83_standard_parity_count() == 22


def test_projection_parity_interval_matches_exhaustive_parameter_box_vertices() -> None:
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
    views = (0, 2, 3)
    parity = 1

    exact_interval = p75_projection_parity_interval_exact(box, views, parity)
    vertex_values = tuple(
        empirical_projection_parity_probability_exact(
            p75_four_view_law_exact(vertex),
            views,
            parity,
        )
        for vertex in _all_box_vertices(box)
    )

    assert exact_interval == (min(vertex_values), max(vertex_values))


def test_fair_branch_channel_forces_pair_parity_to_one_half() -> None:
    box = _strict_witness_box()

    assert p75_projection_parity_interval_exact(
        box,
        (2, 3),
        0,
    ) == (Fraction(1, 2), Fraction(1, 2))
    assert p75_projection_parity_interval_exact(
        box,
        (2, 3),
        1,
    ) == (Fraction(1, 2), Fraction(1, 2))


def test_p83_strictly_improves_p82_on_exact_rational_dependence_witness() -> None:
    box = _strict_witness_box()
    empirical = _strict_witness_empirical_law()

    p82 = p75_box_p82_linf_lower_bound_exact(empirical, box)
    parity = p75_box_projection_parity_linf_lower_bound_exact(empirical, box)
    p83 = p75_box_p83_linf_lower_bound_exact(empirical, box)
    witness = p75_box_projection_parity_witness_exact(empirical, box)

    assert p82 == Fraction(0)
    assert parity == Fraction(1, 16)
    assert p83 == Fraction(1, 16)
    assert p83 > p82
    assert witness.lower_bound == Fraction(1, 16)
    assert witness.views == (2, 3)
    assert witness.parity == 0
    assert witness.support_size == 8
    assert witness.empirical_probability == Fraction(1)
    assert witness.interval_lower == Fraction(1, 2)
    assert witness.interval_upper == Fraction(1, 2)


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


def test_projection_parity_validation_rejects_invalid_specs() -> None:
    box = P78ParameterBox.unit_cube()

    with pytest.raises(ValueError, match="between two and four"):
        p75_projection_parity_interval_exact(box, (0,), 0)

    with pytest.raises(ValueError, match="strictly increasing"):
        p75_projection_parity_interval_exact(box, (1, 0), 0)

    with pytest.raises(ValueError, match="integer 0 or 1"):
        p75_projection_parity_interval_exact(box, (0, 1), 2)


def test_p83_branch_and_bound_returns_valid_exact_rational_bracket() -> None:
    counts = tuple(
        4 if sum(pattern) % 2 == 0 else 0
        for pattern in product((0, 1), repeat=4)
    )
    certificate = certified_p75_linf_branch_and_bound_parity(
        counts,
        max_leaves=8,
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
    assert certificate.root_parity_bound <= certificate.root_p83_bound
    assert certificate.root_tightening_over_p82 >= 0
    assert certificate.leaf_count == 8
    assert certificate.evaluated_boxes == 2 * certificate.iterations + 1
    assert certificate.certified_gap == certificate.upper_bound - certificate.lower_bound


def test_p83_source_states_exactness_scope_and_scientific_boundary() -> None:
    source = Path(
        "src/consciousness_bridge/projection_parity_model_separation.py"
    ).read_text(encoding="utf-8")

    required = (
        "22",
        "exact, not merely an enclosure",
        "never weaker than P82",
        "strictly stronger",
        "P82 lower bound zero but P83 lower bound 1/16",
        "does not validate",
        "identify a latent state with consciousness",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in source
