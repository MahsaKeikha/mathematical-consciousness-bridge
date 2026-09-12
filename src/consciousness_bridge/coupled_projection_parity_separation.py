"""P84 exact coupled projection-parity certificates for continuous P75 separation.

P83 checks each nontrivial projection-parity probability separately. Separate
interval compatibility does not require two parity observables to be realized
by one common assignment of the P75 response parameters. P84 keeps the complete
P83 certificate and adds exact signed contrasts between pairs of even-parity
observables.

For distinct nontrivial view sets J and K, define

    D(J,K) = P(XOR_{j in J} X_j = 0) - P(XOR_{j in K} X_j = 0).

Inside one latent branch s of P75, write a_{j,s} = 1 - 2 q_{j,s}. Conditional
independence gives

    D_s(J,K)
      = [product_{j in J} a_{j,s} - product_{j in K} a_{j,s}] / 2.

This contrast is multi-affine in the response coordinates indexed by J union K.
Its exact minimum and maximum on an axis-aligned parameter box therefore occur
at vertices of that union box. Crucially, both products are evaluated at the
same endpoint assignment. This is the coupling information that separate P83
parity intervals discard.

The minus-branch coordinates, plus-branch coordinates, and prevalence are
disjoint. After exact branchwise extremization, the latent-mixture contrast is
affine in prevalence, so its extrema occur at the prevalence endpoints.

There are 11 nontrivial parity view sets of sizes two, three, and four, hence

    C(11,2) = 55

standard unordered P84 pairwise contrasts. For two distinct nonzero parity
forms on four binary variables, the indicator difference has exactly eight
nonzero coefficients. Consequently, if ||p-q||_inf <= r,

    |D_p(J,K) - D_q(J,K)| <= 8 r.

Distance from an empirical contrast to its exact P75 box interval divided by
eight is therefore a rigorous full-law L-infinity lower bound.

The final P84 box certificate is

    max(P83 lower bound, exact coupled parity-contrast lower bound).

It is never weaker than P83 and can be strictly stronger. An exact-rational
witness included in the test suite has P81 = P82 = P83 = 0 while P84 = 1/64.
The P78 mesh-width upper certificate is retained unchanged for global
branch-and-bound. P84 does not claim a new convergence theorem.

This certificate does not validate the P75 model, does not identify a latent
state with consciousness, and does not close the physical-to-experiential
bridge.
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
ParityViews = tuple[int, ...]
ParityContrastSpec = tuple[ParityViews, ParityViews]


def _standard_parity_view_sets() -> tuple[ParityViews, ...]:
    return tuple(
        views
        for size in range(2, _VIEW_COUNT + 1)
        for views in combinations(range(_VIEW_COUNT), size)
    )


_STANDARD_PARITY_VIEW_SETS = _standard_parity_view_sets()
_STANDARD_PARITY_CONTRASTS = tuple(combinations(_STANDARD_PARITY_VIEW_SETS, 2))


@dataclass(frozen=True)
class P84ParityContrastWitness:
    """Strongest exact coupled parity-contrast witness on one P75 box."""

    lower_bound: Fraction
    left_views: ParityViews
    right_views: ParityViews
    support_size: int
    empirical_contrast: Fraction
    interval_lower: Fraction
    interval_upper: Fraction
    minus_branch_lower: Fraction
    minus_branch_upper: Fraction
    plus_branch_lower: Fraction
    plus_branch_upper: Fraction


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


def _distance_to_interval(
    value: Fraction,
    lower: Fraction,
    upper: Fraction,
) -> Fraction:
    if value < lower:
        return lower - value
    if value > upper:
        return value - upper
    return Fraction(0)


def _validate_parity_views(views: ParityViews, *, name: str) -> None:
    if len(views) < 2 or len(views) > _VIEW_COUNT:
        raise ValueError(f"{name} must use between two and four views")
    if tuple(sorted(set(views))) != views:
        raise ValueError(
            f"{name} must be a strictly increasing tuple of distinct indices"
        )
    if any(
        isinstance(view, bool) or not isinstance(view, int)
        for view in views
    ):
        raise TypeError(f"{name} indices must be integers")
    if any(view < 0 or view >= _VIEW_COUNT for view in views):
        raise ValueError(f"{name} indices must lie in {{0,1,2,3}}")


def _validate_contrast_spec(
    left_views: ParityViews,
    right_views: ParityViews,
) -> None:
    _validate_parity_views(left_views, name="left_views")
    _validate_parity_views(right_views, name="right_views")
    if left_views == right_views:
        raise ValueError("P84 parity contrast requires two distinct view sets")


def p84_standard_parity_contrast_count() -> int:
    """Return the number of standard unordered coupled parity contrasts."""

    return len(_STANDARD_PARITY_CONTRASTS)


def p84_projection_parity_contrast_support_size(
    left_views: ParityViews,
    right_views: ParityViews,
) -> int:
    """Return the L1 norm of the signed contrast indicator coefficients."""

    _validate_contrast_spec(left_views, right_views)
    return sum(
        1
        for outcome in product((0, 1), repeat=_VIEW_COUNT)
        if (
            sum(outcome[view] for view in left_views) % 2
            != sum(outcome[view] for view in right_views) % 2
        )
    )


def _spin_product(
    spin_by_view: dict[int, Fraction],
    views: ParityViews,
) -> Fraction:
    value = Fraction(1)
    for view in views:
        value *= spin_by_view[view]
    return value


def _branch_parity_contrast_interval_exact(
    box: P78ParameterBox,
    left_views: ParityViews,
    right_views: ParityViews,
    *,
    plus_branch: bool,
) -> tuple[Fraction, Fraction]:
    """Return the exact branchwise interval of one coupled parity contrast."""

    union_views = tuple(sorted(set(left_views) | set(right_views)))
    branch_offset = 2 if plus_branch else 1
    spin_endpoints = []
    for view in union_views:
        index = branch_offset + 2 * view
        q_lower = box.lower[index]
        q_upper = box.upper[index]
        spin_endpoints.append((1 - 2 * q_lower, 1 - 2 * q_upper))

    values = []
    for endpoint_choice in product(*spin_endpoints):
        spin_by_view = dict(zip(union_views, endpoint_choice, strict=True))
        left_product = _spin_product(spin_by_view, left_views)
        right_product = _spin_product(spin_by_view, right_views)
        values.append((left_product - right_product) / 2)

    return min(values), max(values)


def p75_projection_parity_contrast_interval_exact(
    box: P78ParameterBox,
    left_views: ParityViews,
    right_views: ParityViews,
) -> tuple[Fraction, Fraction]:
    """Return the exact P75 box range of an even-parity probability contrast."""

    _validate_contrast_spec(left_views, right_views)
    minus_lower, minus_upper = _branch_parity_contrast_interval_exact(
        box,
        left_views,
        right_views,
        plus_branch=False,
    )
    plus_lower, plus_upper = _branch_parity_contrast_interval_exact(
        box,
        left_views,
        right_views,
        plus_branch=True,
    )

    prevalence_endpoints = (box.lower[0], box.upper[0])
    lower_candidates = tuple(
        (1 - prevalence) * minus_lower + prevalence * plus_lower
        for prevalence in prevalence_endpoints
    )
    upper_candidates = tuple(
        (1 - prevalence) * minus_upper + prevalence * plus_upper
        for prevalence in prevalence_endpoints
    )
    return min(lower_candidates), max(upper_candidates)


def empirical_projection_parity_contrast_exact(
    empirical_law: tuple[Fraction, ...],
    left_views: ParityViews,
    right_views: ParityViews,
) -> Fraction:
    """Return the exact empirical difference of two even-parity probabilities."""

    _validate_contrast_spec(left_views, right_views)
    return empirical_projection_parity_probability_exact(
        empirical_law,
        left_views,
        0,
    ) - empirical_projection_parity_probability_exact(
        empirical_law,
        right_views,
        0,
    )


def p75_box_projection_parity_contrast_witness_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> P84ParityContrastWitness:
    """Return the strongest standard exact P84 coupled parity witness."""

    best: P84ParityContrastWitness | None = None
    for left_views, right_views in _STANDARD_PARITY_CONTRASTS:
        empirical_contrast = empirical_projection_parity_contrast_exact(
            empirical_law,
            left_views,
            right_views,
        )
        interval_lower, interval_upper = (
            p75_projection_parity_contrast_interval_exact(
                box,
                left_views,
                right_views,
            )
        )
        minus_lower, minus_upper = _branch_parity_contrast_interval_exact(
            box,
            left_views,
            right_views,
            plus_branch=False,
        )
        plus_lower, plus_upper = _branch_parity_contrast_interval_exact(
            box,
            left_views,
            right_views,
            plus_branch=True,
        )
        support_size = p84_projection_parity_contrast_support_size(
            left_views,
            right_views,
        )
        lower_bound = (
            _distance_to_interval(
                empirical_contrast,
                interval_lower,
                interval_upper,
            )
            / support_size
        )
        candidate = P84ParityContrastWitness(
            lower_bound=lower_bound,
            left_views=left_views,
            right_views=right_views,
            support_size=support_size,
            empirical_contrast=empirical_contrast,
            interval_lower=interval_lower,
            interval_upper=interval_upper,
            minus_branch_lower=minus_lower,
            minus_branch_upper=minus_upper,
            plus_branch_lower=plus_lower,
            plus_branch_upper=plus_upper,
        )
        if best is None or candidate.lower_bound > best.lower_bound:
            best = candidate

    if best is None:
        raise RuntimeError("P84 coupled parity-contrast family unexpectedly empty")
    return best


def p75_box_projection_parity_contrast_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the strongest standard exact P84 parity-contrast lower bound."""

    return p75_box_projection_parity_contrast_witness_exact(
        empirical_law,
        box,
    ).lower_bound


def p75_box_p84_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the P84 box certificate ``max(P83, coupled parity contrast)``."""

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


def certified_p75_linf_branch_and_bound_coupled_parity(
    counts: tuple[int, ...],
    *,
    max_leaves: int = 256,
    gap_tolerance: Fraction = Fraction(0),
) -> P84DistanceBracket:
    """Return a global P75 distance bracket using exact P84 box lower bounds.

    Active boxes partition the complete P75 parameter cube. P84 lower bounds
    drive refinement. Explicit box centers remain valid global upper witnesses.
    The already-proved P78 mesh-width upper certificate is retained unchanged;
    no new P84 convergence-rate theorem is assumed.
    """

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
            p84_lower = max(
                p83_lower,
                p75_box_projection_parity_contrast_linf_lower_bound_exact(
                    empirical_law,
                    child,
                ),
            )
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
