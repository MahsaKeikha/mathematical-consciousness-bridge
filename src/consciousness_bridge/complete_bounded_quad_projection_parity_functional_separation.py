"""Candidate P87 complete bounded-weight four-event parity certificates.

P86 audits the smallest non-uniform primitive four-event coefficient multiset
``{1, 1, 1, 2}``.  The candidate P87 step closes a different gap without
increasing functional order: it exhausts every primitive nonzero four-event
integer coefficient vector with ``|c_i| <= 2``, modulo one global sign.

There are 120 standard coefficient patterns for each four-element subset of the
eleven canonical even-parity view sets, hence

    C(11, 4) * 120 = 39,600

standard bounded-weight four-event functionals.  The P86 family is an exact
subset of this family.

Every functional is multi-affine in each latent-branch response coordinate, so
its exact P75 box range is attained at endpoint vertices and prevalence
endpoints.  Full-law L-infinity transfer uses the exact mass-conservation
centered coefficient norm.

This is a conditional model-separation construction.  It does not identify the
P75 latent state with consciousness, validate an alternative model, establish
nonphysicality, or solve the physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from math import gcd

from consciousness_bridge.certified_continuous_model_separation import P78ParameterBox
from consciousness_bridge.triple_projection_parity_functional_separation import (
    p75_box_p85_linf_lower_bound_exact,
)

_VIEW_COUNT = 4
_OUTCOME_COUNT = 16
ParityBoundedQuadTerm = tuple[tuple[int, ...], int]
ParityBoundedQuadFunctional = tuple[
    ParityBoundedQuadTerm,
    ParityBoundedQuadTerm,
    ParityBoundedQuadTerm,
    ParityBoundedQuadTerm,
]


def _standard_even_view_sets() -> tuple[tuple[int, ...], ...]:
    return tuple(
        views
        for size in range(2, _VIEW_COUNT + 1)
        for views in combinations(range(_VIEW_COUNT), size)
    )


def _standard_bounded_weight_patterns() -> tuple[tuple[int, int, int, int], ...]:
    patterns: set[tuple[int, int, int, int]] = set()
    for raw in product((-2, -1, 1, 2), repeat=4):
        if gcd(*(abs(value) for value in raw)) != 1:
            continue
        coefficients = raw
        if coefficients[0] < 0:
            coefficients = tuple(-value for value in coefficients)
        patterns.add(coefficients)
    return tuple(sorted(patterns))


_STANDARD_VIEW_SETS = _standard_even_view_sets()
_STANDARD_BOUNDED_WEIGHT_PATTERNS = _standard_bounded_weight_patterns()
_OUTCOMES = tuple(product((0, 1), repeat=_VIEW_COUNT))
_EVENT_INDICATORS: dict[tuple[int, ...], tuple[int, ...]] = {
    views: tuple(
        int(sum(outcome[view] for view in views) % 2 == 0)
        for outcome in _OUTCOMES
    )
    for views in _STANDARD_VIEW_SETS
}


@dataclass(frozen=True)
class P87BoundedWeightQuadParityWitness:
    """Strongest standard exact primitive bounded-weight four-event witness."""

    lower_bound: Fraction
    terms: ParityBoundedQuadFunctional
    empirical_value: Fraction
    interval_lower: Fraction
    interval_upper: Fraction
    interval_gap: Fraction
    centered_coefficient_norm: Fraction
    centering_constant: Fraction


def _validate_view_set(views: tuple[int, ...]) -> None:
    if len(views) < 2 or len(views) > _VIEW_COUNT:
        raise ValueError("P87 parity events must use between two and four views")
    if tuple(sorted(set(views))) != views:
        raise ValueError("views must be a strictly increasing tuple of distinct indices")
    if any(view < 0 or view >= _VIEW_COUNT for view in views):
        raise ValueError("view indices must lie in {0,1,2,3}")


def _validate_functional(terms: ParityBoundedQuadFunctional) -> None:
    if len(terms) != 4:
        raise ValueError("P87 functionals must contain exactly four parity terms")

    view_sets: list[tuple[int, ...]] = []
    coefficients: list[int] = []
    for views, coefficient in terms:
        _validate_view_set(views)
        if isinstance(coefficient, bool) or not isinstance(coefficient, int):
            raise TypeError("P87 functional coefficients must be nonzero integers")
        if coefficient == 0 or abs(coefficient) > 2:
            raise ValueError("P87 coefficient magnitudes must lie in {1,2}")
        view_sets.append(views)
        coefficients.append(coefficient)

    if len(set(view_sets)) != 4:
        raise ValueError("P87 functional view sets must be distinct")
    if gcd(*(abs(value) for value in coefficients)) != 1:
        raise ValueError("P87 bounded coefficient vector must be primitive")


def _distance_to_interval(value: Fraction, lower: Fraction, upper: Fraction) -> Fraction:
    if value < lower:
        return lower - value
    if value > upper:
        return value - upper
    return Fraction(0)


def _branch_parity_rows_exact(
    box: P78ParameterBox,
    *,
    plus_branch: bool,
) -> dict[tuple[int, ...], tuple[Fraction, ...]]:
    branch_offset = 2 if plus_branch else 1
    response_choices: list[tuple[Fraction, ...]] = []
    for view in range(_VIEW_COUNT):
        index = branch_offset + 2 * view
        q_lower = box.lower[index]
        q_upper = box.upper[index]
        a_lower = 1 - 2 * q_upper
        a_upper = 1 - 2 * q_lower
        response_choices.append(
            (a_lower,) if a_lower == a_upper else (a_lower, a_upper)
        )

    vertices = tuple(product(*response_choices))
    rows: dict[tuple[int, ...], tuple[Fraction, ...]] = {}
    for views in _STANDARD_VIEW_SETS:
        values: list[Fraction] = []
        for response in vertices:
            parity_product = Fraction(1)
            for view in views:
                parity_product *= response[view]
            values.append((1 + parity_product) / 2)
        rows[views] = tuple(values)
    return rows


def _functional_branch_interval_from_rows(
    rows: dict[tuple[int, ...], tuple[Fraction, ...]],
    terms: ParityBoundedQuadFunctional,
) -> tuple[Fraction, Fraction]:
    row_count = len(rows[terms[0][0]])
    values = tuple(
        sum(
            (
                coefficient * rows[views][index]
                for views, coefficient in terms
            ),
            start=Fraction(0),
        )
        for index in range(row_count)
    )
    return min(values), max(values)


def _functional_interval_from_rows(
    box: P78ParameterBox,
    terms: ParityBoundedQuadFunctional,
    minus_rows: dict[tuple[int, ...], tuple[Fraction, ...]],
    plus_rows: dict[tuple[int, ...], tuple[Fraction, ...]],
) -> tuple[Fraction, Fraction]:
    minus_lower, minus_upper = _functional_branch_interval_from_rows(
        minus_rows,
        terms,
    )
    plus_lower, plus_upper = _functional_branch_interval_from_rows(
        plus_rows,
        terms,
    )
    prevalences = (
        (box.lower[0],)
        if box.lower[0] == box.upper[0]
        else (box.lower[0], box.upper[0])
    )
    lower_candidates = tuple(
        (1 - prevalence) * minus_lower + prevalence * plus_lower
        for prevalence in prevalences
    )
    upper_candidates = tuple(
        (1 - prevalence) * minus_upper + prevalence * plus_upper
        for prevalence in prevalences
    )
    return min(lower_candidates), max(upper_candidates)


def _empirical_parity_probabilities_exact(
    empirical_law: tuple[Fraction, ...],
) -> dict[tuple[int, ...], Fraction]:
    if len(empirical_law) != _OUTCOME_COUNT:
        raise ValueError("empirical_law must contain sixteen probabilities")
    return {
        views: sum(
            (
                probability * indicator
                for probability, indicator in zip(
                    empirical_law,
                    _EVENT_INDICATORS[views],
                    strict=True,
                )
            ),
            start=Fraction(0),
        )
        for views in _STANDARD_VIEW_SETS
    }


def _centered_coefficient_norm_int(
    terms: ParityBoundedQuadFunctional,
) -> tuple[int, int]:
    outcome_coefficients = sorted(
        sum(
            coefficient * _EVENT_INDICATORS[views][index]
            for views, coefficient in terms
        )
        for index in range(_OUTCOME_COUNT)
    )
    center = outcome_coefficients[_OUTCOME_COUNT // 2 - 1]
    norm = sum(abs(value - center) for value in outcome_coefficients)
    return norm, center


def p87_standard_weight_pattern_count() -> int:
    """Return the 120 sign-normalized primitive coefficient patterns."""

    return len(_STANDARD_BOUNDED_WEIGHT_PATTERNS)


def p87_standard_bounded_quad_count() -> int:
    """Return the 39,600 standard P87 bounded-weight four-event functionals."""

    return len(tuple(combinations(_STANDARD_VIEW_SETS, 4))) * len(
        _STANDARD_BOUNDED_WEIGHT_PATTERNS
    )


def p87_contains_p86_weight_family() -> bool:
    """Return whether every P86 {1,1,1,2} pattern is contained in P87."""

    p86_patterns = {
        pattern
        for pattern in _STANDARD_BOUNDED_WEIGHT_PATTERNS
        if sorted(abs(value) for value in pattern) == [1, 1, 1, 2]
    }
    return len(p86_patterns) == 32


def p75_bounded_weight_parity_quad_interval_exact(
    box: P78ParameterBox,
    terms: ParityBoundedQuadFunctional,
) -> tuple[Fraction, Fraction]:
    """Return the exact P75 box interval of one primitive bounded functional."""

    _validate_functional(terms)
    minus_rows = _branch_parity_rows_exact(box, plus_branch=False)
    plus_rows = _branch_parity_rows_exact(box, plus_branch=True)
    return _functional_interval_from_rows(
        box,
        terms,
        minus_rows,
        plus_rows,
    )


def empirical_bounded_weight_parity_quad_exact(
    empirical_law: tuple[Fraction, ...],
    terms: ParityBoundedQuadFunctional,
) -> Fraction:
    """Return the exact empirical value of one P87 four-event functional."""

    _validate_functional(terms)
    probabilities = _empirical_parity_probabilities_exact(empirical_law)
    return sum(
        (
            coefficient * probabilities[views]
            for views, coefficient in terms
        ),
        start=Fraction(0),
    )


def bounded_weight_parity_quad_centered_coefficient_norm_exact(
    terms: ParityBoundedQuadFunctional,
) -> tuple[Fraction, Fraction]:
    """Return the exact centered L1 coefficient norm and deterministic center."""

    _validate_functional(terms)
    norm, center = _centered_coefficient_norm_int(terms)
    return Fraction(norm), Fraction(center)


def p75_box_bounded_weight_quad_parity_witness_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> P87BoundedWeightQuadParityWitness:
    """Return the strongest exact P87 bounded-weight four-event witness."""

    empirical_probabilities = _empirical_parity_probabilities_exact(empirical_law)
    minus_rows = _branch_parity_rows_exact(box, plus_branch=False)
    plus_rows = _branch_parity_rows_exact(box, plus_branch=True)

    best: P87BoundedWeightQuadParityWitness | None = None
    for view_quad in combinations(_STANDARD_VIEW_SETS, 4):
        for coefficients in _STANDARD_BOUNDED_WEIGHT_PATTERNS:
            terms: ParityBoundedQuadFunctional = tuple(
                (views, coefficient)
                for views, coefficient in zip(
                    view_quad,
                    coefficients,
                    strict=True,
                )
            )  # type: ignore[assignment]
            empirical_value = sum(
                (
                    coefficient * empirical_probabilities[views]
                    for views, coefficient in terms
                ),
                start=Fraction(0),
            )
            interval_lower, interval_upper = _functional_interval_from_rows(
                box,
                terms,
                minus_rows,
                plus_rows,
            )
            interval_gap = _distance_to_interval(
                empirical_value,
                interval_lower,
                interval_upper,
            )
            centered_norm_int, center_int = _centered_coefficient_norm_int(terms)
            if centered_norm_int <= 0:
                raise RuntimeError("P87 bounded functional unexpectedly has zero norm")
            centered_norm = Fraction(centered_norm_int)
            lower_bound = interval_gap / centered_norm
            candidate = P87BoundedWeightQuadParityWitness(
                lower_bound=lower_bound,
                terms=terms,
                empirical_value=empirical_value,
                interval_lower=interval_lower,
                interval_upper=interval_upper,
                interval_gap=interval_gap,
                centered_coefficient_norm=centered_norm,
                centering_constant=Fraction(center_int),
            )
            if best is None or candidate.lower_bound > best.lower_bound:
                best = candidate

    if best is None:
        raise RuntimeError("P87 standard bounded-weight family unexpectedly empty")
    return best


def p75_box_bounded_weight_quad_parity_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the strongest exact P87 bounded-four-event lower bound."""

    return p75_box_bounded_weight_quad_parity_witness_exact(
        empirical_law,
        box,
    ).lower_bound


def p75_box_p87_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return max(P85, complete primitive |c_i|<=2 four-event bound).

    This dominates P86 by family inclusion: the complete bounded-weight family
    contains every standard P86 {1,1,1,2} functional, while the explicit P85
    term preserves the other component of the P86 maximum.
    """

    p85 = p75_box_p85_linf_lower_bound_exact(empirical_law, box)
    bounded_quad = p75_box_bounded_weight_quad_parity_linf_lower_bound_exact(
        empirical_law,
        box,
    )
    return max(p85, bounded_quad)
