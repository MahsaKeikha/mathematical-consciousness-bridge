"""P88 exact radius-three bounded primitive four-event parity certificates.

P88 extends the completed P87 primitive coefficient box from 0 < |c_i| <= 2 to
0 < |c_i| <= 3 at the same four-event order. The declared finite family contains
632 sign-normalized primitive coefficient patterns per four-event subset and
208,560 exact functionals across the 330 four-event subsets of the eleven
canonical P83 parity coordinates.

All calculations are exact over fractions.Fraction. P88 is a conditional
model-separation theorem inside the declared P75 target-measurement family; it
does not identify the latent state with consciousness or solve the
physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from itertools import combinations, product
from math import gcd

from consciousness_bridge.certified_continuous_model_separation import P78ParameterBox
from consciousness_bridge.projection_parity_model_separation import (
    empirical_projection_parity_probability_exact,
)
from consciousness_bridge.bounded_primitive_quad_projection_parity_functional_separation import (
    p75_box_p87_linf_lower_bound_exact,
)

_VIEW_COUNT = 4
_OUTCOME_COUNT = 16
_COEFFICIENT_VALUES = (-3, -2, -1, 1, 2, 3)

PrimitiveQuadTerm = tuple[tuple[int, ...], int]
PrimitiveQuadFunctional = tuple[PrimitiveQuadTerm, PrimitiveQuadTerm, PrimitiveQuadTerm, PrimitiveQuadTerm]


def _standard_even_view_sets() -> tuple[tuple[int, ...], ...]:
    return tuple(v for size in range(2, _VIEW_COUNT + 1) for v in combinations(range(_VIEW_COUNT), size))


def _coefficient_gcd(coefficients: tuple[int, int, int, int]) -> int:
    return reduce(gcd, (abs(c) for c in coefficients))


def _standard_primitive_weight_patterns() -> tuple[tuple[int, int, int, int], ...]:
    patterns: set[tuple[int, int, int, int]] = set()
    for coefficients in product(_COEFFICIENT_VALUES, repeat=4):
        if _coefficient_gcd(coefficients) != 1:
            continue
        if coefficients[0] < 0:
            coefficients = tuple(-c for c in coefficients)
        patterns.add(coefficients)
    return tuple(sorted(patterns))


_STANDARD_VIEW_SETS = _standard_even_view_sets()
_STANDARD_PRIMITIVE_WEIGHT_PATTERNS = _standard_primitive_weight_patterns()
_STANDARD_PRIMITIVE_QUAD_COUNT = len(tuple(combinations(_STANDARD_VIEW_SETS, 4))) * len(_STANDARD_PRIMITIVE_WEIGHT_PATTERNS)


@dataclass(frozen=True)
class P88PrimitiveQuadParityWitness:
    """Strongest exact witness in the radius-three bounded primitive P88 family."""

    lower_bound: Fraction
    terms: PrimitiveQuadFunctional
    empirical_value: Fraction
    interval_lower: Fraction
    interval_upper: Fraction
    interval_gap: Fraction
    centered_coefficient_norm: Fraction
    centering_constant: Fraction


def _validate_view_set(views: tuple[int, ...]) -> None:
    if len(views) < 2 or len(views) > _VIEW_COUNT:
        raise ValueError("P88 parity events must use between two and four views")
    if tuple(sorted(set(views))) != views:
        raise ValueError("views must be a strictly increasing tuple of distinct indices")
    if any(view < 0 or view >= _VIEW_COUNT for view in views):
        raise ValueError("view indices must lie in {0,1,2,3}")


def _validate_functional(terms: PrimitiveQuadFunctional) -> None:
    if len(terms) != 4:
        raise ValueError("P88 functionals must contain exactly four parity terms")
    view_sets: list[tuple[int, ...]] = []
    coefficients: list[int] = []
    for views, coefficient in terms:
        _validate_view_set(views)
        if isinstance(coefficient, bool) or not isinstance(coefficient, int):
            raise TypeError("P88 coefficients must be nonzero integers")
        if coefficient == 0 or abs(coefficient) > 3:
            raise ValueError("P88 coefficients must satisfy 0 < |c_i| <= 3")
        view_sets.append(views)
        coefficients.append(coefficient)
    if len(set(view_sets)) != 4:
        raise ValueError("P88 functional view sets must be distinct")
    if reduce(gcd, (abs(c) for c in coefficients)) != 1:
        raise ValueError("P88 coefficient vector must be primitive")


def _distance_to_interval(value: Fraction, lower: Fraction, upper: Fraction) -> Fraction:
    if value < lower:
        return lower - value
    if value > upper:
        return value - upper
    return Fraction(0)


def _parity_probability_from_responses(responses: tuple[Fraction, ...], views: tuple[int, ...]) -> Fraction:
    parity_product = Fraction(1)
    for view in views:
        parity_product *= responses[view]
    return (1 + parity_product) / 2


def _branch_probability_vectors_exact(box: P78ParameterBox, view_quad: tuple[tuple[int, ...], ...], *, plus_branch: bool) -> tuple[tuple[Fraction, ...], ...]:
    branch_offset = 2 if plus_branch else 1
    response_endpoints: list[tuple[Fraction, ...]] = []
    for view in range(_VIEW_COUNT):
        index = branch_offset + 2 * view
        q_lower, q_upper = box.lower[index], box.upper[index]
        response_lower, response_upper = 1 - 2 * q_upper, 1 - 2 * q_lower
        response_endpoints.append((response_lower,) if response_lower == response_upper else (response_lower, response_upper))
    return tuple(
        tuple(_parity_probability_from_responses(responses, views) for views in view_quad)
        for responses in product(*response_endpoints)
    )


def _functional_interval_from_probability_vectors(box: P78ParameterBox, coefficients: tuple[int, ...], minus_vectors: tuple[tuple[Fraction, ...], ...], plus_vectors: tuple[tuple[Fraction, ...], ...]) -> tuple[Fraction, Fraction]:
    def values(vectors: tuple[tuple[Fraction, ...], ...]) -> tuple[Fraction, ...]:
        return tuple(sum((c * value for c, value in zip(coefficients, vector, strict=True)), start=Fraction(0)) for vector in vectors)
    minus_values, plus_values = values(minus_vectors), values(plus_vectors)
    minus_lower, minus_upper = min(minus_values), max(minus_values)
    plus_lower, plus_upper = min(plus_values), max(plus_values)
    prevalences = (box.lower[0],) if box.lower[0] == box.upper[0] else (box.lower[0], box.upper[0])
    lower_candidates = tuple((1 - pi) * minus_lower + pi * plus_lower for pi in prevalences)
    upper_candidates = tuple((1 - pi) * minus_upper + pi * plus_upper for pi in prevalences)
    return min(lower_candidates), max(upper_candidates)


def _outcome_incidence_vectors(view_quad: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(int(sum(outcome[v] for v in views) % 2 == 0) for views in view_quad)
        for outcome in product((0, 1), repeat=_VIEW_COUNT)
    )


def _centered_norm_from_incidence_vectors(coefficients: tuple[int, ...], incidence_vectors: tuple[tuple[int, ...], ...]) -> tuple[Fraction, Fraction]:
    outcome_coefficients = tuple(Fraction(sum(c * i for c, i in zip(coefficients, vector, strict=True))) for vector in incidence_vectors)
    candidates = tuple(sorted(set(outcome_coefficients)))
    return min((sum((abs(value - center) for value in outcome_coefficients), start=Fraction(0)), center) for center in candidates)


def p88_standard_primitive_weight_pattern_count() -> int:
    """Return the 632 sign-normalized primitive radius-three patterns."""
    return len(_STANDARD_PRIMITIVE_WEIGHT_PATTERNS)


def p88_standard_primitive_quad_count() -> int:
    """Return the 208,560 radius-three bounded primitive P88 functionals."""
    return _STANDARD_PRIMITIVE_QUAD_COUNT


def p75_radius_three_primitive_parity_quad_interval_exact(box: P78ParameterBox, terms: PrimitiveQuadFunctional) -> tuple[Fraction, Fraction]:
    """Return the exact P75 box interval for one P88 functional."""
    _validate_functional(terms)
    view_quad = tuple(views for views, _ in terms)
    coefficients = tuple(c for _, c in terms)
    return _functional_interval_from_probability_vectors(
        box,
        coefficients,
        _branch_probability_vectors_exact(box, view_quad, plus_branch=False),
        _branch_probability_vectors_exact(box, view_quad, plus_branch=True),
    )


def empirical_radius_three_primitive_parity_quad_exact(empirical_law: tuple[Fraction, ...], terms: PrimitiveQuadFunctional) -> Fraction:
    """Return the exact empirical value of one P88 functional."""
    _validate_functional(terms)
    if len(empirical_law) != _OUTCOME_COUNT:
        raise ValueError("empirical_law must contain sixteen probabilities")
    return sum((c * empirical_projection_parity_probability_exact(empirical_law, views, 0) for views, c in terms), start=Fraction(0))


def radius_three_primitive_parity_quad_centered_coefficient_norm_exact(terms: PrimitiveQuadFunctional) -> tuple[Fraction, Fraction]:
    """Return the exact centered L1 transfer norm and one minimizing center."""
    _validate_functional(terms)
    view_quad = tuple(views for views, _ in terms)
    coefficients = tuple(c for _, c in terms)
    return _centered_norm_from_incidence_vectors(coefficients, _outcome_incidence_vectors(view_quad))


def p75_box_radius_three_bounded_primitive_quad_parity_witness_exact(empirical_law: tuple[Fraction, ...], box: P78ParameterBox) -> P88PrimitiveQuadParityWitness:
    """Exhaust the 208,560-function P88 family and return its strongest witness."""
    if len(empirical_law) != _OUTCOME_COUNT:
        raise ValueError("empirical_law must contain sixteen probabilities")
    empirical_probabilities = {views: empirical_projection_parity_probability_exact(empirical_law, views, 0) for views in _STANDARD_VIEW_SETS}
    best: P88PrimitiveQuadParityWitness | None = None
    for view_quad in combinations(_STANDARD_VIEW_SETS, 4):
        minus_vectors = _branch_probability_vectors_exact(box, view_quad, plus_branch=False)
        plus_vectors = _branch_probability_vectors_exact(box, view_quad, plus_branch=True)
        incidence_vectors = _outcome_incidence_vectors(view_quad)
        empirical_vector = tuple(empirical_probabilities[views] for views in view_quad)
        for coefficients in _STANDARD_PRIMITIVE_WEIGHT_PATTERNS:
            empirical_value = sum((c * value for c, value in zip(coefficients, empirical_vector, strict=True)), start=Fraction(0))
            interval_lower, interval_upper = _functional_interval_from_probability_vectors(box, coefficients, minus_vectors, plus_vectors)
            interval_gap = _distance_to_interval(empirical_value, interval_lower, interval_upper)
            centered_norm, center = _centered_norm_from_incidence_vectors(coefficients, incidence_vectors)
            if centered_norm <= 0:
                raise RuntimeError("P88 functional unexpectedly has zero centered norm")
            lower_bound = interval_gap / centered_norm
            terms: PrimitiveQuadFunctional = tuple((views, c) for views, c in zip(view_quad, coefficients, strict=True))
            witness = P88PrimitiveQuadParityWitness(lower_bound, terms, empirical_value, interval_lower, interval_upper, interval_gap, centered_norm, center)
            if best is None or witness.lower_bound > best.lower_bound:
                best = witness
    if best is None:
        raise RuntimeError("P88 family unexpectedly empty")
    return best


def p75_box_radius_three_bounded_primitive_quad_parity_linf_lower_bound_exact(empirical_law: tuple[Fraction, ...], box: P78ParameterBox) -> Fraction:
    return p75_box_radius_three_bounded_primitive_quad_parity_witness_exact(empirical_law, box).lower_bound


def p75_box_p88_linf_lower_bound_exact(empirical_law: tuple[Fraction, ...], box: P78ParameterBox) -> Fraction:
    """Return max(P87, radius-three bounded primitive P88 lower bound)."""
    p87 = p75_box_p87_linf_lower_bound_exact(empirical_law, box)
    p88_family = p75_box_radius_three_bounded_primitive_quad_parity_linf_lower_bound_exact(empirical_law, box)
    return max(p87, p88_family)


def p88_dominates_p87_on_box(empirical_law: tuple[Fraction, ...], box: P78ParameterBox) -> bool:
    """Return the exact pointwise dominance check P88(B) >= P87(B)."""
    return p75_box_p88_linf_lower_bound_exact(empirical_law, box) >= p75_box_p87_linf_lower_bound_exact(empirical_law, box)
