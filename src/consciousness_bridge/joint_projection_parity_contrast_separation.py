"""P84 exact joint projection-parity contrast certificates for P75 separation.

P83 tests each declared projection-parity event separately. Separate interval
membership does not require two observed parity probabilities to be jointly
attainable by one common P75 parameter assignment. P84 closes that specific
relaxation gap by testing exact pairwise contrasts between parity events built
from different view sets.

For parity events H_1 and H_2, define the contrast

    C = P(H_1) - P(H_2).

Inside one latent branch of P75, each parity probability has the exact form

    P_s(H(J,b)) = [1 + (-1)^b product_{j in J}(1 - 2 q_{j,s})] / 2.

Their difference is multi-affine in the response coordinates appearing in the
union of the two view sets. Therefore its extrema over an axis-aligned rational
parameter box occur at endpoint vertices. Minus-branch and plus-branch response
coordinates are disjoint. After exact branchwise extremization, the latent
mixture is affine in prevalence, so its global extrema occur at the prevalence
endpoints. Every P84 contrast interval is therefore exact, not an enclosure.

If ||p-q||_inf <= r and c_x = 1_{H_1}(x) - 1_{H_2}(x), then

    |C(p)-C(q)| <= sum_x |c_x| r.

The denominator is exactly the symmetric-difference size of the two parity
events. P84 uses every unordered pair of the 22 P83 parity events whose view
sets differ. The 11 same-view complementary pairs are omitted because they are
algebraic rewritings of one P83 probability. This leaves 220 genuinely coupled
standard contrasts.

The final P84 box certificate is

    max(P83 lower bound, exact pairwise parity-contrast lower bound).

It is never weaker than P83 and can be strictly stronger. An exact-rational
witness in the regression suite has P83 lower bound zero while a P84 contrast
lies 1/4 outside its exact model-box range. The contrast coefficient support is
8 cells, giving a certified full-law L-infinity lower bound of 1/32.

The P78 mesh-width upper certificate is retained unchanged for global
branch-and-bound. P84 does not claim a new convergence theorem. This certificate
rejects only the declared P75 model family under the stated assumptions. It
does not validate an alternative model, identify a latent state with
consciousness, or solve the physical-to-experiential bridge.
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
    p75_box_linf_lower_bound_exact,
    p75_four_view_law_exact,
)
from consciousness_bridge.certified_sampling_radius import P79SamplingRadiusCertificate
from consciousness_bridge.nested_projection_contrast_separation import (
    p75_box_p82_linf_lower_bound_exact,
)
from consciousness_bridge.projection_event_model_separation import (
    p75_box_p81_linf_lower_bound_exact,
)
from consciousness_bridge.projection_parity_model_separation import (
    empirical_projection_parity_probability_exact,
    p75_box_p83_linf_lower_bound_exact,
)
from consciousness_bridge.simplex_coupled_model_separation import (
    p75_box_simplex_linf_lower_bound_exact,
)

_VIEW_COUNT = 4
ParitySpec = tuple[tuple[int, ...], int]


def _standard_parity_specs() -> tuple[ParitySpec, ...]:
    return tuple(
        (views, parity)
        for size in range(2, _VIEW_COUNT + 1)
        for views in combinations(range(_VIEW_COUNT), size)
        for parity in (0, 1)
    )


_STANDARD_PARITY_SPECS = _standard_parity_specs()
_STANDARD_CONTRAST_PAIRS = tuple(
    (first, second)
    for first_index, first in enumerate(_STANDARD_PARITY_SPECS)
    for second in _STANDARD_PARITY_SPECS[first_index + 1 :]
    if first[0] != second[0]
)


@dataclass(frozen=True)
class P84ParityContrastWitness:
    """Strongest exact coupled parity-contrast witness on one P75 box."""

    lower_bound: Fraction
    first_views: tuple[int, ...]
    first_parity: int
    second_views: tuple[int, ...]
    second_parity: int
    coefficient_support_size: int
    empirical_contrast: Fraction
    interval_lower: Fraction
    interval_upper: Fraction
    first_empirical_probability: Fraction
    second_empirical_probability: Fraction


@dataclass(frozen=True)
class P84DistanceBracket:
    """Certified global L-infinity bracket using P84 box lower bounds."""

    lower_bound: Fraction
    upper_bound: Fraction
    best_parameters: tuple[Fraction, ...]
    leaf_count: int
    evaluated_boxes: int
    iterations: int
    maximum_active_width_sum: Fraction
    p78_active_lower_bound: Fraction
    p80_active_lower_bound: Fraction
    p81_active_lower_bound: Fraction
    p82_active_lower_bound: Fraction
    p83_active_lower_bound: Fraction
    p78_mesh_upper_bound: Fraction
    certified_gap: Fraction
    root_p78_bound: Fraction
    root_p80_bound: Fraction
    root_p81_bound: Fraction
    root_p82_bound: Fraction
    root_p83_bound: Fraction
    root_contrast_bound: Fraction
    root_p84_bound: Fraction
    root_tightening_over_p83: Fraction
    conclusion: str


def _validate_parity_spec(views: tuple[int, ...], parity: int) -> None:
    if isinstance(parity, bool) or not isinstance(parity, int) or parity not in (0, 1):
        raise ValueError("parity must be the integer 0 or 1")
    if len(views) < 2 or len(views) > _VIEW_COUNT:
        raise ValueError("P84 parity events must use between two and four views")
    if tuple(sorted(set(views))) != views:
        raise ValueError("views must be a strictly increasing tuple of distinct indices")
    if any(view < 0 or view >= _VIEW_COUNT for view in views):
        raise ValueError("view indices must lie in {0,1,2,3}")


def _distance_to_interval(value: Fraction, lower: Fraction, upper: Fraction) -> Fraction:
    if value < lower:
        return lower - value
    if value > upper:
        return value - upper
    return Fraction(0)


def _branch_parity_contrast_interval_exact(
    box: P78ParameterBox,
    first: ParitySpec,
    second: ParitySpec,
    *,
    plus_branch: bool,
) -> tuple[Fraction, Fraction]:
    """Return the exact branchwise range of one coupled parity contrast."""

    first_views, first_parity = first
    second_views, second_parity = second
    union_views = tuple(sorted(set(first_views) | set(second_views)))
    branch_offset = 2 if plus_branch else 1
    endpoint_intervals = []
    for view in union_views:
        index = branch_offset + 2 * view
        q_lower = box.lower[index]
        q_upper = box.upper[index]
        endpoint_intervals.append((1 - 2 * q_upper, 1 - 2 * q_lower))

    values: list[Fraction] = []
    for endpoint_choice in product(*endpoint_intervals):
        factor = dict(zip(union_views, endpoint_choice, strict=True))
        first_product = Fraction(1)
        second_product = Fraction(1)
        for view in first_views:
            first_product *= factor[view]
        for view in second_views:
            second_product *= factor[view]
        first_sign = 1 if first_parity == 0 else -1
        second_sign = 1 if second_parity == 0 else -1
        values.append(
            Fraction(first_sign * first_product - second_sign * second_product, 2)
        )

    return min(values), max(values)


def p84_standard_contrast_count() -> int:
    """Return the number of genuinely coupled standard P84 contrasts."""

    return len(_STANDARD_CONTRAST_PAIRS)


def p75_projection_parity_contrast_interval_exact(
    box: P78ParameterBox,
    first_views: tuple[int, ...],
    first_parity: int,
    second_views: tuple[int, ...],
    second_parity: int,
) -> tuple[Fraction, Fraction]:
    """Return the exact P75 box range of P(H1)-P(H2)."""

    _validate_parity_spec(first_views, first_parity)
    _validate_parity_spec(second_views, second_parity)
    if first_views == second_views:
        raise ValueError("P84 standard contrasts require different parity view sets")

    first = (first_views, first_parity)
    second = (second_views, second_parity)
    minus_lower, minus_upper = _branch_parity_contrast_interval_exact(
        box,
        first,
        second,
        plus_branch=False,
    )
    plus_lower, plus_upper = _branch_parity_contrast_interval_exact(
        box,
        first,
        second,
        plus_branch=True,
    )

    lower_candidates = tuple(
        (1 - prevalence) * minus_lower + prevalence * plus_lower
        for prevalence in (box.lower[0], box.upper[0])
    )
    upper_candidates = tuple(
        (1 - prevalence) * minus_upper + prevalence * plus_upper
        for prevalence in (box.lower[0], box.upper[0])
    )
    return min(lower_candidates), max(upper_candidates)


def empirical_projection_parity_contrast_exact(
    empirical_law: tuple[Fraction, ...],
    first_views: tuple[int, ...],
    first_parity: int,
    second_views: tuple[int, ...],
    second_parity: int,
) -> Fraction:
    """Return the exact empirical contrast P(H1)-P(H2)."""

    _validate_parity_spec(first_views, first_parity)
    _validate_parity_spec(second_views, second_parity)
    return empirical_projection_parity_probability_exact(
        empirical_law,
        first_views,
        first_parity,
    ) - empirical_projection_parity_probability_exact(
        empirical_law,
        second_views,
        second_parity,
    )


def parity_contrast_coefficient_support_size(
    first_views: tuple[int, ...],
    first_parity: int,
    second_views: tuple[int, ...],
    second_parity: int,
) -> int:
    """Return sum_x |1_H1(x)-1_H2(x)| for the sixteen observed cells."""

    _validate_parity_spec(first_views, first_parity)
    _validate_parity_spec(second_views, second_parity)
    support = 0
    for outcome in product((0, 1), repeat=_VIEW_COUNT):
        first_member = sum(outcome[view] for view in first_views) % 2 == first_parity
        second_member = sum(outcome[view] for view in second_views) % 2 == second_parity
        support += int(first_member != second_member)
    return support


def p75_box_projection_parity_contrast_witness_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> P84ParityContrastWitness:
    """Return the strongest standard exact P84 pairwise parity witness."""

    best: P84ParityContrastWitness | None = None
    for first, second in _STANDARD_CONTRAST_PAIRS:
        first_views, first_parity = first
        second_views, second_parity = second
        first_empirical = empirical_projection_parity_probability_exact(
            empirical_law,
            first_views,
            first_parity,
        )
        second_empirical = empirical_projection_parity_probability_exact(
            empirical_law,
            second_views,
            second_parity,
        )
        empirical_contrast = first_empirical - second_empirical
        interval_lower, interval_upper = p75_projection_parity_contrast_interval_exact(
            box,
            first_views,
            first_parity,
            second_views,
            second_parity,
        )
        coefficient_support_size = parity_contrast_coefficient_support_size(
            first_views,
            first_parity,
            second_views,
            second_parity,
        )
        if coefficient_support_size <= 0:
            raise RuntimeError("P84 contrast unexpectedly has zero coefficient support")
        lower_bound = _distance_to_interval(
            empirical_contrast,
            interval_lower,
            interval_upper,
        ) / coefficient_support_size
        candidate = P84ParityContrastWitness(
            lower_bound=lower_bound,
            first_views=first_views,
            first_parity=first_parity,
            second_views=second_views,
            second_parity=second_parity,
            coefficient_support_size=coefficient_support_size,
            empirical_contrast=empirical_contrast,
            interval_lower=interval_lower,
            interval_upper=interval_upper,
            first_empirical_probability=first_empirical,
            second_empirical_probability=second_empirical,
        )
        if best is None or candidate.lower_bound > best.lower_bound:
            best = candidate

    if best is None:
        raise RuntimeError("P84 pairwise parity family unexpectedly empty")
    return best


def p75_box_projection_parity_contrast_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the strongest standard exact P84 contrast lower bound."""

    return p75_box_projection_parity_contrast_witness_exact(
        empirical_law,
        box,
    ).lower_bound


def p75_box_p84_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return max(P83, exact coupled parity-contrast lower bound)."""

    p83 = p75_box_p83_linf_lower_bound_exact(empirical_law, box)
    contrast = p75_box_projection_parity_contrast_linf_lower_bound_exact(
        empirical_law,
        box,
    )
    return max(p83, contrast)


def p84_dominates_p83_on_box(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> bool:
    """Return the exact dominance check P84(B) >= P83(B)."""

    return p75_box_p84_linf_lower_bound_exact(
        empirical_law,
        box,
    ) >= p75_box_p83_linf_lower_bound_exact(empirical_law, box)


def certified_p75_linf_branch_and_bound_parity_contrast(
    counts: tuple[int, ...],
    *,
    max_leaves: int = 256,
    gap_tolerance: Fraction = Fraction(0),
) -> P84DistanceBracket:
    """Return a global P75 distance bracket using exact P84 box lower bounds."""

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
    root_p78 = p75_box_linf_lower_bound_exact(empirical_law, root)
    root_p80 = p75_box_simplex_linf_lower_bound_exact(empirical_law, root)
    root_p81 = p75_box_p81_linf_lower_bound_exact(empirical_law, root)
    root_p82 = p75_box_p82_linf_lower_bound_exact(empirical_law, root)
    root_p83 = p75_box_p83_linf_lower_bound_exact(empirical_law, root)
    root_contrast = p75_box_projection_parity_contrast_linf_lower_bound_exact(
        empirical_law,
        root,
    )
    root_p84 = max(root_p83, root_contrast)
    root_center = root.center
    root_upper = linf_distance_exact(
        empirical_law,
        p75_four_view_law_exact(root_center),
    )

    serial = 0
    active: list[
        tuple[
            Fraction,
            int,
            P78ParameterBox,
            Fraction,
            Fraction,
            Fraction,
            Fraction,
            Fraction,
        ]
    ] = []
    heappush(
        active,
        (
            root_p84,
            serial,
            root,
            root_p83,
            root_p82,
            root_p81,
            root_p80,
            root_p78,
        ),
    )
    serial += 1

    best_upper = root_upper
    best_parameters = root_center
    evaluated_boxes = 1
    iterations = 0

    while len(active) < max_leaves:
        global_lower = active[0][0]
        if best_upper - global_lower <= gap_tolerance:
            break

        _, _, box, _, _, _, _, _ = heappop(active)
        if box.width_sum == 0:
            p78_lower = p75_box_linf_lower_bound_exact(empirical_law, box)
            p80_lower = p75_box_simplex_linf_lower_bound_exact(empirical_law, box)
            p81_lower = p75_box_p81_linf_lower_bound_exact(empirical_law, box)
            p82_lower = p75_box_p82_linf_lower_bound_exact(empirical_law, box)
            p83_lower = p75_box_p83_linf_lower_bound_exact(empirical_law, box)
            p84_lower = p75_box_p84_linf_lower_bound_exact(empirical_law, box)
            heappush(
                active,
                (
                    p84_lower,
                    serial,
                    box,
                    p83_lower,
                    p82_lower,
                    p81_lower,
                    p80_lower,
                    p78_lower,
                ),
            )
            break

        left, right = box.split_widest()
        for child in (left, right):
            p78_lower = p75_box_linf_lower_bound_exact(empirical_law, child)
            p80_lower = p75_box_simplex_linf_lower_bound_exact(empirical_law, child)
            p81_lower = p75_box_p81_linf_lower_bound_exact(empirical_law, child)
            p82_lower = p75_box_p82_linf_lower_bound_exact(empirical_law, child)
            p83_lower = p75_box_p83_linf_lower_bound_exact(empirical_law, child)
            contrast_lower = p75_box_projection_parity_contrast_linf_lower_bound_exact(
                empirical_law,
                child,
            )
            p84_lower = max(p83_lower, contrast_lower)
            center = child.center
            center_upper = linf_distance_exact(
                empirical_law,
                p75_four_view_law_exact(center),
            )
            if center_upper < best_upper:
                best_upper = center_upper
                best_parameters = center
            heappush(
                active,
                (
                    p84_lower,
                    serial,
                    child,
                    p83_lower,
                    p82_lower,
                    p81_lower,
                    p80_lower,
                    p78_lower,
                ),
            )
            serial += 1
            evaluated_boxes += 1
        iterations += 1

    global_lower = active[0][0]
    p83_active_lower = min(entry[3] for entry in active)
    p82_active_lower = min(entry[4] for entry in active)
    p81_active_lower = min(entry[5] for entry in active)
    p80_active_lower = min(entry[6] for entry in active)
    p78_active_lower = min(entry[7] for entry in active)
    maximum_width_sum = max(entry[2].width_sum for entry in active)
    p78_mesh_upper = p78_active_lower + maximum_width_sum
    certified_upper = min(best_upper, p78_mesh_upper)
    certified_gap = certified_upper - global_lower

    if certified_gap < 0:
        raise RuntimeError("certified upper bound fell below the P84 lower bound")

    if global_lower == certified_upper:
        conclusion = "exact global L-infinity model distance certified"
    elif len(active) >= max_leaves:
        conclusion = (
            "valid P84 global distance bracket; leaf budget exhausted before exact closure"
        )
    else:
        conclusion = "valid P84 global distance bracket; requested gap tolerance reached"

    return P84DistanceBracket(
        lower_bound=global_lower,
        upper_bound=certified_upper,
        best_parameters=best_parameters,
        leaf_count=len(active),
        evaluated_boxes=evaluated_boxes,
        iterations=iterations,
        maximum_active_width_sum=maximum_width_sum,
        p78_active_lower_bound=p78_active_lower,
        p80_active_lower_bound=p80_active_lower,
        p81_active_lower_bound=p81_active_lower,
        p82_active_lower_bound=p82_active_lower,
        p83_active_lower_bound=p83_active_lower,
        p78_mesh_upper_bound=p78_mesh_upper,
        certified_gap=certified_gap,
        root_p78_bound=root_p78,
        root_p80_bound=root_p80,
        root_p81_bound=root_p81,
        root_p82_bound=root_p82,
        root_p83_bound=root_p83,
        root_contrast_bound=root_contrast,
        root_p84_bound=root_p84,
        root_tightening_over_p83=root_p84 - root_p83,
        conclusion=conclusion,
    )


def p84_rejection_with_p79_radius(
    bracket: P84DistanceBracket,
    radius: P79SamplingRadiusCertificate,
) -> bool:
    """Apply the strict P77 rejection gate with P84/P79 certified directions."""

    return bracket.lower_bound > radius.cell_linf_radius_upper
