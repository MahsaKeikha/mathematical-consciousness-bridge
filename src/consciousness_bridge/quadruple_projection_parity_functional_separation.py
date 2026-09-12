"""P86 exact four-event projection-parity functional certificates.

P85 tests all standard sign-normalized three-event functionals built from the
11 canonical even-parity observables on two, three, or four of the four observed
views. Three-event compatibility still does not imply four-event compatibility
under one shared P75 parameter assignment. P86 closes that next finite
relaxation gap.

For four distinct canonical view sets J_1,...,J_4 and signs sigma_i in {-1,+1},
with the first sign normalized to +1, define

    Q = sum_i sigma_i P(H_Ji),

where H_J is the even-parity event on J. There are

    C(11,4) * 2^3 = 2640

standard P86 functionals.

Inside either latent branch of P75 each parity probability is a constant plus a
product of distinct response coordinates. Therefore Q is multi-affine and its
exact range on an axis-aligned rational parameter box occurs at endpoint
vertices. The final latent mixture is affine in prevalence, so the full box
interval is exact as well.

For the outcome coefficient g(x) = sum_i sigma_i 1_{H_Ji}(x), total-mass
cancellation permits the exact centered transfer denominator

    D(Q) = min_c sum_x |g(x)-c|.

If the empirical value lies Delta outside the exact P75 interval, then every
model law q in the box satisfies

    ||p-q||_infinity >= Delta / D(Q).

The final P86 box certificate is max(P85, strongest four-event bound). It is
never weaker than P85. The regression suite contains an exact rational witness
for which the complete P85 certificate is zero while a four-event functional
has empirical value 3/4, exact P75 interval [-1,1/2], interval gap 1/4, centered
coefficient norm 12, and certified L-infinity lower bound 1/48.

P86 is a conditional model-separation theorem only. It does not identify the
P75 latent state with consciousness, validate an alternative model, prove
consciousness is nonphysical, or close the physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from heapq import heappop, heappush
from itertools import combinations, product

from consciousness_bridge.certified_continuous_model_separation import (
    P78ParameterBox,
    empirical_law_from_counts,
    linf_distance_exact,
    p75_four_view_law_exact,
)
from consciousness_bridge.projection_parity_model_separation import (
    empirical_projection_parity_probability_exact,
)
from consciousness_bridge.triple_projection_parity_functional_separation import (
    p75_box_p85_linf_lower_bound_exact,
)

_VIEW_COUNT = 4
_OUTCOME_COUNT = 16
ParityQuadrupleTerm = tuple[tuple[int, ...], int]
ParityQuadrupleFunctional = tuple[
    ParityQuadrupleTerm,
    ParityQuadrupleTerm,
    ParityQuadrupleTerm,
    ParityQuadrupleTerm,
]


def _standard_even_view_sets() -> tuple[tuple[int, ...], ...]:
    return tuple(
        views
        for size in range(2, _VIEW_COUNT + 1)
        for views in combinations(range(_VIEW_COUNT), size)
    )


_STANDARD_VIEW_SETS = _standard_even_view_sets()
_STANDARD_QUADRUPLE_FUNCTIONALS: tuple[ParityQuadrupleFunctional, ...] = tuple(
    tuple((views, sign) for views, sign in zip(view_quadruple, signs, strict=True))
    for view_quadruple in combinations(_STANDARD_VIEW_SETS, 4)
    for signs in (
        (1, -1, -1, -1),
        (1, -1, -1, 1),
        (1, -1, 1, -1),
        (1, -1, 1, 1),
        (1, 1, -1, -1),
        (1, 1, -1, 1),
        (1, 1, 1, -1),
        (1, 1, 1, 1),
    )
)


@dataclass(frozen=True)
class P86QuadrupleParityWitness:
    """Strongest standard exact four-event parity witness on one P75 box."""

    lower_bound: Fraction
    terms: ParityQuadrupleFunctional
    empirical_value: Fraction
    interval_lower: Fraction
    interval_upper: Fraction
    interval_gap: Fraction
    centered_coefficient_norm: Fraction
    centering_constant: Fraction


@dataclass(frozen=True)
class P86DistanceBracket:
    """Certified global P75 distance bracket using P86 box lower bounds."""

    lower_bound: Fraction
    upper_bound: Fraction
    best_parameters: tuple[Fraction, ...]
    leaf_count: int
    evaluated_boxes: int
    iterations: int
    maximum_active_width_sum: Fraction
    certified_gap: Fraction
    root_p85_bound: Fraction
    root_quadruple_bound: Fraction
    root_p86_bound: Fraction
    root_tightening_over_p85: Fraction
    conclusion: str


def _validate_view_set(views: tuple[int, ...]) -> None:
    if len(views) < 2 or len(views) > _VIEW_COUNT:
        raise ValueError("P86 parity events must use between two and four views")
    if tuple(sorted(set(views))) != views:
        raise ValueError("views must be a strictly increasing tuple of distinct indices")
    if any(view < 0 or view >= _VIEW_COUNT for view in views):
        raise ValueError("view indices must lie in {0,1,2,3}")


def _validate_functional(terms: ParityQuadrupleFunctional) -> None:
    if len(terms) != 4:
        raise ValueError("P86 functionals must contain exactly four parity terms")
    view_sets: list[tuple[int, ...]] = []
    for views, sign in terms:
        _validate_view_set(views)
        if isinstance(sign, bool) or sign not in (-1, 1):
            raise ValueError("P86 functional signs must be integers in {-1,+1}")
        view_sets.append(views)
    if len(set(view_sets)) != 4:
        raise ValueError("P86 functional view sets must be distinct")


def _distance_to_interval(value: Fraction, lower: Fraction, upper: Fraction) -> Fraction:
    if value < lower:
        return lower - value
    if value > upper:
        return value - upper
    return Fraction(0)


def _branch_quadruple_value(
    response: dict[int, Fraction],
    terms: ParityQuadrupleFunctional,
) -> Fraction:
    value = Fraction(0)
    for views, sign in terms:
        parity_product = Fraction(1)
        for view in views:
            parity_product *= response[view]
        value += sign * (1 + parity_product) / 2
    return value


def _branch_quadruple_interval_exact(
    box: P78ParameterBox,
    terms: ParityQuadrupleFunctional,
    *,
    plus_branch: bool,
) -> tuple[Fraction, Fraction]:
    union_views = tuple(sorted({view for views, _ in terms for view in views}))
    branch_offset = 2 if plus_branch else 1
    endpoint_intervals: list[tuple[Fraction, ...]] = []
    for view in union_views:
        index = branch_offset + 2 * view
        q_lower = box.lower[index]
        q_upper = box.upper[index]
        a_lower = 1 - 2 * q_upper
        a_upper = 1 - 2 * q_lower
        endpoint_intervals.append(
            (a_lower,) if a_lower == a_upper else (a_lower, a_upper)
        )

    values = tuple(
        _branch_quadruple_value(
            dict(zip(union_views, endpoint_choice, strict=True)),
            terms,
        )
        for endpoint_choice in product(*endpoint_intervals)
    )
    return min(values), max(values)


def p86_standard_quadruple_count() -> int:
    """Return the 2640 sign-normalized standard P86 four-event functionals."""

    return len(_STANDARD_QUADRUPLE_FUNCTIONALS)


def p75_signed_parity_quadruple_interval_exact(
    box: P78ParameterBox,
    terms: ParityQuadrupleFunctional,
) -> tuple[Fraction, Fraction]:
    """Return the exact P75 box range of one signed four-event functional."""

    _validate_functional(terms)
    minus_lower, minus_upper = _branch_quadruple_interval_exact(
        box,
        terms,
        plus_branch=False,
    )
    plus_lower, plus_upper = _branch_quadruple_interval_exact(
        box,
        terms,
        plus_branch=True,
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


def empirical_signed_parity_quadruple_exact(
    empirical_law: tuple[Fraction, ...],
    terms: ParityQuadrupleFunctional,
) -> Fraction:
    """Return the exact empirical value of one signed P86 four-event functional."""

    _validate_functional(terms)
    if len(empirical_law) != _OUTCOME_COUNT:
        raise ValueError("empirical_law must contain sixteen probabilities")
    return sum(
        (
            sign
            * empirical_projection_parity_probability_exact(
                empirical_law,
                views,
                0,
            )
            for views, sign in terms
        ),
        start=Fraction(0),
    )


def parity_quadruple_centered_coefficient_norm_exact(
    terms: ParityQuadrupleFunctional,
) -> tuple[Fraction, Fraction]:
    """Return the exact minimum L1 coefficient norm and one optimal constant."""

    _validate_functional(terms)
    coefficients: list[Fraction] = []
    for outcome in product((0, 1), repeat=_VIEW_COUNT):
        coefficient = sum(
            (
                sign
                for views, sign in terms
                if sum(outcome[view] for view in views) % 2 == 0
            ),
            start=0,
        )
        coefficients.append(Fraction(coefficient))

    candidates = tuple(sorted(set(coefficients)))
    norm_and_center = tuple(
        (
            sum((abs(value - center) for value in coefficients), start=Fraction(0)),
            center,
        )
        for center in candidates
    )
    return min(norm_and_center)


def p75_box_quadruple_parity_witness_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> P86QuadrupleParityWitness:
    """Return the strongest standard exact P86 four-event parity witness."""

    best: P86QuadrupleParityWitness | None = None
    for terms in _STANDARD_QUADRUPLE_FUNCTIONALS:
        empirical_value = empirical_signed_parity_quadruple_exact(empirical_law, terms)
        interval_lower, interval_upper = p75_signed_parity_quadruple_interval_exact(
            box,
            terms,
        )
        interval_gap = _distance_to_interval(
            empirical_value,
            interval_lower,
            interval_upper,
        )
        centered_norm, center = parity_quadruple_centered_coefficient_norm_exact(terms)
        if centered_norm <= 0:
            raise RuntimeError("P86 four-event functional unexpectedly has zero norm")
        lower_bound = interval_gap / centered_norm
        candidate = P86QuadrupleParityWitness(
            lower_bound=lower_bound,
            terms=terms,
            empirical_value=empirical_value,
            interval_lower=interval_lower,
            interval_upper=interval_upper,
            interval_gap=interval_gap,
            centered_coefficient_norm=centered_norm,
            centering_constant=center,
        )
        if best is None or candidate.lower_bound > best.lower_bound:
            best = candidate

    if best is None:
        raise RuntimeError("P86 standard four-event family unexpectedly empty")
    return best


def p75_box_quadruple_parity_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the strongest exact standard P86 four-event lower bound."""

    return p75_box_quadruple_parity_witness_exact(empirical_law, box).lower_bound


def p75_box_p86_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return max(P85, strongest exact P86 four-event functional bound)."""

    p85 = p75_box_p85_linf_lower_bound_exact(empirical_law, box)
    quadruple = p75_box_quadruple_parity_linf_lower_bound_exact(empirical_law, box)
    return max(p85, quadruple)


def p86_dominates_p85_on_box(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> bool:
    """Return the exact pointwise dominance check P86(B) >= P85(B)."""

    return p75_box_p86_linf_lower_bound_exact(
        empirical_law,
        box,
    ) >= p75_box_p85_linf_lower_bound_exact(empirical_law, box)


def certified_p75_linf_branch_and_bound_quadruple_parity(
    counts: tuple[int, ...],
    *,
    max_leaves: int = 256,
    gap_tolerance: Fraction = Fraction(0),
) -> P86DistanceBracket:
    """Return a global P75 distance bracket using exact P86 box lower bounds."""

    if isinstance(max_leaves, bool) or not isinstance(max_leaves, int):
        raise TypeError("max_leaves must be an integer")
    if max_leaves < 1:
        raise ValueError("max_leaves must be positive")
    if not isinstance(gap_tolerance, Fraction):
        raise TypeError("gap_tolerance must be a fractions.Fraction")
    if gap_tolerance < 0:
        raise ValueError("gap_tolerance must be nonnegative")

    empirical_law = empirical_law_from_counts(counts)
    root = P78ParameterBox.unit_cube()
    root_p85 = p75_box_p85_linf_lower_bound_exact(empirical_law, root)
    root_quadruple = p75_box_quadruple_parity_linf_lower_bound_exact(
        empirical_law,
        root,
    )
    root_p86 = max(root_p85, root_quadruple)
    root_center = root.center
    best_parameters = root_center
    best_upper = linf_distance_exact(
        empirical_law,
        p75_four_view_law_exact(root_center),
    )

    active: list[tuple[Fraction, int, P78ParameterBox]] = []
    serial = 0
    heappush(active, (root_p86, serial, root))
    serial += 1
    evaluated_boxes = 1
    iterations = 0

    while len(active) < max_leaves:
        global_lower = active[0][0]
        if best_upper - global_lower <= gap_tolerance:
            break
        lower_bound, _, box = heappop(active)
        if lower_bound > best_upper:
            continue
        try:
            children = box.split_widest()
        except ValueError:
            heappush(active, (lower_bound, serial, box))
            serial += 1
            break

        iterations += 1
        for child in children:
            child_lower = p75_box_p86_linf_lower_bound_exact(empirical_law, child)
            center = child.center
            child_upper = linf_distance_exact(
                empirical_law,
                p75_four_view_law_exact(center),
            )
            evaluated_boxes += 1
            if child_upper < best_upper:
                best_upper = child_upper
                best_parameters = center
            if child_lower <= best_upper:
                heappush(active, (child_lower, serial, child))
                serial += 1

        if not active:
            raise RuntimeError("P86 branch-and-bound lost the active parameter cover")

    global_lower = active[0][0]
    maximum_active_width_sum = max(box.width_sum for _, _, box in active)
    certified_gap = best_upper - global_lower
    conclusion = (
        "P86 supplies a certified global P75 L-infinity distance bracket. "
        "Its lower bound strengthens P85 with exact four-event shared-parameter "
        "parity functionals; interpretation remains conditional on the P75 model."
    )
    return P86DistanceBracket(
        lower_bound=global_lower,
        upper_bound=best_upper,
        best_parameters=best_parameters,
        leaf_count=len(active),
        evaluated_boxes=evaluated_boxes,
        iterations=iterations,
        maximum_active_width_sum=maximum_active_width_sum,
        certified_gap=certified_gap,
        root_p85_bound=root_p85,
        root_quadruple_bound=root_quadruple,
        root_p86_bound=root_p86,
        root_tightening_over_p85=root_p86 - root_p85,
        conclusion=conclusion,
    )
