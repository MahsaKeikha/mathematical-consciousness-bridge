from fractions import Fraction

from consciousness_bridge.certified_continuous_model_separation import P78ParameterBox
from consciousness_bridge.triple_projection_parity_functional_separation import (
    p75_box_p85_linf_lower_bound_exact,
)


def test_candidate_box_is_silent_under_complete_p85() -> None:
    box = P78ParameterBox(
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
    empirical = (
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

    assert p75_box_p85_linf_lower_bound_exact(empirical, box) == 0
