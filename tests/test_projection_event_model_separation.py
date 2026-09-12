from fractions import Fraction
from itertools import product
from pathlib import Path

import pytest

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    empirical_law_from_counts,
    p75_box_linf_lower_bound_exact,
)
from consciousness_bridge.projection_event_model_separation import (
    certified_p75_linf_branch_and_bound_projection,
    empirical_projection_probability_exact,
    p75_box_p81_linf_lower_bound_exact,
    p75_box_projection_linf_lower_bound_exact,
    p75_box_projection_witness_exact,
    p75_projection_event_interval_exact,
    p81_dominates_p80_on_box,
)
from consciousness_bridge.simplex_coupled_model_separation import (
    p75_box_simplex_linf_lower_bound_exact,
)


def _strict_witness_box() -> P78ParameterBox:
    return P78ParameterBox(
        lower=(
            Fraction(1, 2),
            Fraction(3, 5),
            Fraction(3, 5),
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction(0),
        ),
        upper=(
            Fraction(1, 2),
            Fraction(3, 5),
            Fraction(3, 5),
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(1),
            Fraction(1),
        ),
    )


def test_projection_interval_recovers_fixed_view_marginal_exactly() -> None:
    box = _strict_witness_box()

    probability_zero = p75_projection_event_interval_exact(box, (0,), (0,))
    probability_one = p75_projection_event_interval_exact(box, (0,), (1,))

    assert probability_zero == (Fraction(2, 5), Fraction(2, 5))
    assert probability_one == (Fraction(3, 5), Fraction(3, 5))


def test_empirical_projection_probability_sums_the_correct_cells() -> None:
    empirical = (Fraction(1, 16),) * 16

    assert empirical_projection_probability_exact(empirical, (0,), (0,)) == Fraction(
        1, 2
    )
    assert empirical_projection_probability_exact(
        empirical,
        (0, 2),
        (1, 0),
    ) == Fraction(1, 4)


def test_p81_can_strictly_improve_p80_when_cells_overlap_but_marginal_does_not() -> None:
    empirical = (Fraction(1, 16),) * 16
    box = _strict_witness_box()

    p80 = p75_box_simplex_linf_lower_bound_exact(empirical, box)
    projection = p75_box_projection_linf_lower_bound_exact(empirical, box)
    p81 = p75_box_p81_linf_lower_bound_exact(empirical, box)
    witness = p75_box_projection_witness_exact(empirical, box)

    assert p80 == 0
    assert projection == Fraction(1, 80)
    assert p81 == Fraction(1, 80)
    assert witness.lower_bound == Fraction(1, 80)
    assert witness.views == (0,)
    assert witness.event_size == 8
    assert witness.empirical_probability == Fraction(1, 2)
    assert (witness.interval_lower, witness.interval_upper) in {
        (Fraction(2, 5), Fraction(2, 5)),
        (Fraction(3, 5), Fraction(3, 5)),
    }


def test_projection_family_contains_the_p78_full_cell_bound() -> None:
    counts = (6, 2, 1, 1, 2, 3, 1, 0, 1, 1, 2, 2, 0, 1, 2, 7)
    empirical = empirical_law_from_counts(counts)
    box = P78ParameterBox(
        lower=(
            Fraction(1, 4),
            Fraction(1, 10),
            Fraction(6, 10),
            Fraction(2, 10),
            Fraction(7, 10),
            Fraction(3, 10),
            Fraction(6, 10),
            Fraction(2, 10),
            Fraction(8, 10),
        ),
        upper=(
            Fraction(3, 4),
            Fraction(3, 10),
            Fraction(9, 10),
            Fraction(4, 10),
            Fraction(9, 10),
            Fraction(5, 10),
            Fraction(8, 10),
            Fraction(4, 10),
            Fraction(9, 10),
        ),
    )

    p78 = p75_box_linf_lower_bound_exact(empirical, box)
    projection = p75_box_projection_linf_lower_bound_exact(empirical, box)

    assert projection >= p78


def test_p81_always_dominates_p80_on_the_same_parameter_box() -> None:
    counts = (6, 2, 1, 1, 2, 3, 1, 0, 1, 1, 2, 2, 0, 1, 2, 7)
    empirical = empirical_law_from_counts(counts)
    box = P78ParameterBox(
        lower=(Fraction(1, 8),) * 9,
        upper=(Fraction(7, 8),) * 9,
    )

    p80 = p75_box_simplex_linf_lower_bound_exact(empirical, box)
    p81 = p75_box_p81_linf_lower_bound_exact(empirical, box)

    assert p81 >= p80
    assert p81_dominates_p80_on_box(empirical, box)


def test_projection_specification_validation_is_strict() -> None:
    box = P78ParameterBox.unit_cube()

    with pytest.raises(ValueError, match="nonempty"):
        p75_projection_event_interval_exact(box, (), ())
    with pytest.raises(ValueError, match="equal length"):
        p75_projection_event_interval_exact(box, (0,), (0, 1))
    with pytest.raises(ValueError, match="duplicates"):
        p75_projection_event_interval_exact(box, (0, 0), (0, 1))
    with pytest.raises(ValueError, match="strictly increasing"):
        p75_projection_event_interval_exact(box, (1, 0), (0, 1))
    with pytest.raises(ValueError, match="lie in"):
        p75_projection_event_interval_exact(box, (4,), (0,))
    with pytest.raises(ValueError, match="binary"):
        p75_projection_event_interval_exact(box, (0,), (2,))


def test_p81_branch_and_bound_returns_a_valid_exact_rational_bracket() -> None:
    counts = tuple(
        8 if sum(pattern) % 2 == 0 else 0
        for pattern in product((0, 1), repeat=4)
    )
    certificate = certified_p75_linf_branch_and_bound_projection(
        counts,
        max_leaves=64,
    )

    assert Fraction(0) <= certificate.lower_bound <= certificate.upper_bound <= 1
    assert certificate.p78_active_lower_bound <= certificate.p80_active_lower_bound
    assert certificate.p80_active_lower_bound <= certificate.lower_bound
    assert certificate.root_p78_bound <= certificate.root_p80_bound
    assert certificate.root_p80_bound <= certificate.root_p81_bound
    assert certificate.root_projection_bound <= certificate.root_p81_bound
    assert certificate.root_tightening_over_p80 >= 0
    assert certificate.leaf_count == 64
    assert certificate.evaluated_boxes == 2 * certificate.iterations + 1
    assert certificate.certified_gap == certificate.upper_bound - certificate.lower_bound


def test_p81_refinement_does_not_weaken_global_lower_bound() -> None:
    counts = tuple(
        8 if sum(pattern) % 2 == 0 else 0
        for pattern in product((0, 1), repeat=4)
    )
    coarse = certified_p75_linf_branch_and_bound_projection(counts, max_leaves=16)
    refined = certified_p75_linf_branch_and_bound_projection(counts, max_leaves=64)

    assert refined.lower_bound >= coarse.lower_bound
    assert refined.upper_bound <= coarse.upper_bound


def test_p81_source_states_scope_and_scientific_boundary() -> None:
    source = Path(
        "src/consciousness_bridge/projection_event_model_separation.py"
    ).read_text(encoding="utf-8")

    required = (
        "projected",
        "cylinder",
        "|p(C) - q(C)| <= m r",
        "never weaker than P80",
        "strictly stronger",
        "fractions.Fraction",
        "does not validate that model",
        "does not identify any latent state with consciousness",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in source
