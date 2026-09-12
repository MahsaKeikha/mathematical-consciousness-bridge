"""P85 exact three-event projection-parity functional certificates.

P83 tests one projection-parity observable at a time. P84 strengthens that
certificate by testing all genuinely coupled pairs of parity observables under
one shared P75 parameter assignment. Pairwise compatibility still does not imply
three-way compatibility. P85 closes that next relaxation gap for the standard
four-view parity family.

Use the eleven canonical even-parity events

    H_J = {x : sum_{j in J} x_j mod 2 = 0},

for all view sets J of size two, three, or four. For every unordered triple of
distinct view sets and every sign pattern with the first sign normalized to +1,
P85 studies the sparse functional

    T = sigma_1 P(H_J1) + sigma_2 P(H_J2) + sigma_3 P(H_J3).

There are C(11,3) * 4 = 660 standard sign-normalized triple functionals.
Inside either latent branch of P75,

    P_s(H_J) = [1 + product_{j in J}(1 - 2 q_{j,s})] / 2.

Therefore every P85 triple functional is multi-affine in the branch response
coordinates. Its exact range over an axis-aligned rational parameter box occurs
at endpoint vertices. The final latent mixture is affine in prevalence, so the
full P75 box interval is also exact.

For a triple functional let

    g(x) = sum_i sigma_i 1_{H_Ji}(x).

Because both laws have total mass one, subtracting any constant c from g does
not change T(p)-T(q). P85 therefore uses the exact centered coefficient norm

    D = min_c sum_x |g(x)-c|,

where a median of the sixteen integer coefficient values is optimal. If the
empirical triple functional lies Delta outside its exact P75 box interval, then

    ||p-q||_infinity >= Delta / D

for every model law q generated in that box.

The final P85 box certificate is

    max(P84 lower bound, strongest exact triple-functional lower bound).

It is never weaker than P84 and can be strictly stronger. A deterministic
exact-rational regression witness has P84 lower bound zero while the triple

    H_(0,2) + H_(0,1,2) + H_(0,1,2,3)

has empirical value 5/8 and exact P75 box range [1,2]. The gap is 3/8 and the
centered coefficient norm is 12, producing the certified L-infinity lower bound
1/32. Thus the example isolates a genuine three-event constraint that the full
P84 certificate does not detect on the same box.

P85 remains a conditional model-separation theorem. It rejects only the
declared P75 latent measurement family under its stated assumptions. It does
not identify the latent state with consciousness, validate an alternative
model, prove consciousness is nonphysical, or solve the physical-to-
experiential bridge.
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
from consciousness_bridge.joint_projection_parity_contrast_separation import (
    p75_box_p84_linf_lower_bound_exact,
)
from consciousness_bridge.projection_parity_model_separation import (
    empirical_projection_parity_probability_exact,
)

_VIEW_COUNT = 4
_OUTCOME_COUNT = 16
ParityTripleTerm = tuple[tuple[int, ...], int]
ParityTripleFunctional = tuple[ParityTripleTerm, ParityTripleTerm, ParityTripleTerm]


def _standard_even_view_sets() -> tuple[tuple[int, ...], ...]:
    return tuple(
        views
        for size in range(2, _VIEW_COUNT + 1)
        for views in combinations(range(_VIEW_COUNT), size)
    )


_STANDARD_VIEW_SETS = _standard_even_view_sets()
_STANDARD_TRIPLE_FUNCTIONALS: tuple[ParityTripleFunctional, ...] = tuple(
    tuple((views, sign) for views, sign in zip(view_triple, signs, strict=True))
    for view_triple in combinations(_STANDARD_VIEW_SETS, 3)
    for signs in ((1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1))
)


@dataclass(frozen=True)
class P85TripleParityWitness:
    """Strongest standard exact three-event parity witness on one P75 box."""

    lower_bound: Fraction
    terms: ParityTripleFunctional
    empirical_value: Fraction
    interval_lower: Fraction
    interval_upper: Fraction
    interval_gap: Fraction
    centered_coefficient_norm: Fraction
    centering_constant: Fraction


@dataclass(frozen=True)
class P85DistanceBracket:
    """Certified global P75 distance bracket using P85 box lower bounds."""

    lower_bound: Fraction
    upper_bound: Fraction
    best_parameters: tuple[Fraction, ...]
    leaf_count: int
    evaluated_boxes: int
    iterations: int
    maximum_active_width_sum: Fraction
    certified_gap: Fraction
    root_p84_bound: Fraction
    root_triple_bound: Fraction
    root_p85_bound: Fraction
    root_tightening_over_p84: Fraction
    conclusion: str


def _validate_view_set(views: tuple[int, ...]) -> None:
    if len(views) < 2 or len(views) > _VIEW_COUNT:
        raise ValueError("P85 parity events must use between two and four views")
    if tuple(sorted(set(views))) != views:
        raise ValueError("views must be a strictly increasing tuple of distinct indices")
    if any(view < 0 or view >= _VIEW_COUNT for view in views):
        raise ValueError("view indices must lie in {0,1,2,3}")


def _validate_functional(terms: ParityTripleFunctional) -> None:
    if len(terms) != 3:
        raise ValueError("P85 functionals must contain exactly three parity terms")
    view_sets: list[tuple[int, ...]] = []
    for views, sign in terms:
        _validate_view_set(views)
        if isinstance(sign, bool) or sign not in (-1, 1):
            raise ValueError("P85 functional signs must be integers in {-1,+1}")
        view_sets.append(views)
    if len(set(view_sets)) != 3:
        raise ValueError("P85 functional view sets must be distinct")


def _distance_to_interval(value: Fraction, lower: Fraction, upper: Fraction) -> Fraction:
    if value < lower:
        return lower - value
    if value > upper:
        return value - upper
    return Fraction(0)


def _branch_triple_value(
    response: dict[int, Fraction],
    terms: ParityTripleFunctional,
) -> Fraction:
    value = Fraction(0)
    for views, sign in terms:
        parity_product = Fraction(1)
        for view in views:
            parity_product *= response[view]
        value += sign * (1 + parity_product) / 2
    return value


def _branch_triple_interval_exact(
    box: P78ParameterBox,
    terms: ParityTripleFunctional,
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
        _branch_triple_value(
            dict(zip(union_views, endpoint_choice, strict=True)),
            terms,
        )
        for endpoint_choice in product(*endpoint_intervals)
    )
    return min(values), max(values)


def p85_standard_triple_count() -> int:
    """Return the 660 sign-normalized standard P85 triple functionals."""

    return len(_STANDARD_TRIPLE_FUNCTIONALS)


def p75_signed_parity_triple_interval_exact(
    box: P78ParameterBox,
    terms: ParityTripleFunctional,
) -> tuple[Fraction, Fraction]:
    """Return the exact P75 box range of one signed three-event functional."""

    _validate_functional(terms)
    minus_lower, minus_upper = _branch_triple_interval_exact(
        box,
        terms,
        plus_branch=False,
    )
    plus_lower, plus_upper = _branch_triple_interval_exact(
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


def empirical_signed_parity_triple_exact(
    empirical_law: tuple[Fraction, ...],
    terms: ParityTripleFunctional,
) -> Fraction:
    """Return the exact empirical value of one signed P85 triple functional."""

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


def parity_triple_centered_coefficient_norm_exact(
    terms: ParityTripleFunctional,
) -> tuple[Fraction, Fraction]:
    """Return the exact minimum L1 coefficient norm and one optimal constant.

    For probability laws p and q, adding a constant to the outcome coefficient
    vector does not change the functional difference because both laws have
    total mass one. The L1-minimizing constant is any median of the sixteen
    coefficient values. Exhausting the finitely many integer coefficient values
    is exact and keeps the implementation transparent.
    """

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


def p75_box_triple_parity_witness_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> P85TripleParityWitness:
    """Return the strongest standard exact P85 three-event parity witness."""

    best: P85TripleParityWitness | None = None
    for terms in _STANDARD_TRIPLE_FUNCTIONALS:
        empirical_value = empirical_signed_parity_triple_exact(empirical_law, terms)
        interval_lower, interval_upper = p75_signed_parity_triple_interval_exact(
            box,
            terms,
        )
        interval_gap = _distance_to_interval(
            empirical_value,
            interval_lower,
            interval_upper,
        )
        centered_norm, center = parity_triple_centered_coefficient_norm_exact(terms)
        if centered_norm <= 0:
            raise RuntimeError("P85 triple functional unexpectedly has zero norm")
        lower_bound = interval_gap / centered_norm
        candidate = P85TripleParityWitness(
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
        raise RuntimeError("P85 standard triple family unexpectedly empty")
    return best


def p75_box_triple_parity_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the strongest exact standard P85 triple-functional lower bound."""

    return p75_box_triple_parity_witness_exact(empirical_law, box).lower_bound


def p75_box_p85_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return max(P84, strongest exact P85 triple-functional bound)."""

    p84 = p75_box_p84_linf_lower_bound_exact(empirical_law, box)
    triple = p75_box_triple_parity_linf_lower_bound_exact(empirical_law, box)
    return max(p84, triple)


def p85_dominates_p84_on_box(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> bool:
    """Return the exact pointwise dominance check P85(B) >= P84(B)."""

    return p75_box_p85_linf_lower_bound_exact(
        empirical_law,
        box,
    ) >= p75_box_p84_linf_lower_bound_exact(empirical_law, box)


def certified_p75_linf_branch_and_bound_triple_parity(
    counts: tuple[int, ...],
    *,
    max_leaves: int = 256,
    gap_tolerance: Fraction = Fraction(0),
) -> P85DistanceBracket:
    """Return a global P75 distance bracket using exact P85 box lower bounds."""

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
    root_p84 = p75_box_p84_linf_lower_bound_exact(empirical_law, root)
    root_triple = p75_box_triple_parity_linf_lower_bound_exact(empirical_law, root)
    root_p85 = max(root_p84, root_triple)
    root_center = root.center
    best_parameters = root_center
    best_upper = linf_distance_exact(
        empirical_law,
        p75_four_view_law_exact(root_center),
    )

    active: list[tuple[Fraction, int, P78ParameterBox]] = []
    serial = 0
    heappush(active, (root_p85, serial, root))
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
            child_lower = p75_box_p85_linf_lower_bound_exact(empirical_law, child)
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
            raise RuntimeError("P85 branch-and-bound lost the active parameter cover")

    global_lower = active[0][0]
    maximum_active_width_sum = max(box.width_sum for _, _, box in active)
    certified_gap = best_upper - global_lower
    conclusion = (
        "P85 supplies a certified global P75 L-infinity distance bracket. "
        "Its lower bound strengthens P84 with exact three-event shared-parameter "
        "parity functionals; interpretation remains conditional on the P75 model."
    )
    return P85DistanceBracket(
        lower_bound=global_lower,
        upper_bound=best_upper,
        best_parameters=best_parameters,
        leaf_count=len(active),
        evaluated_boxes=evaluated_boxes,
        iterations=iterations,
        maximum_active_width_sum=maximum_active_width_sum,
        certified_gap=certified_gap,
        root_p84_bound=root_p84,
        root_triple_bound=root_triple,
        root_p85_bound=root_p85,
        root_tightening_over_p84=root_p85 - root_p84,
        conclusion=conclusion,
    )
