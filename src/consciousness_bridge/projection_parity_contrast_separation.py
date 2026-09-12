"""P84 exact coupled projection-parity contrasts for continuous P75 separation.

P83 tests every nontrivial two-, three-, and four-view parity observable
separately. Separate interval compatibility does not imply that one common P75
parameter choice can realize all compatible parity values simultaneously.
P84 retains the complete P83 certificate and adds exact pairwise contrasts
between the eleven nontrivial parity expectations.

For a nonempty selected view set J define the signed parity observable

    chi_J(x) = (-1) ** sum_{j in J} x_j.

Inside latent branch s of P75, conditional independence gives

    Z_s(J) = E_s[chi_J] = product_{j in J}(1 - 2 q_{j,s}).

For distinct P83 view sets J and K define the coupled contrast

    D_s(J,K) = Z_s(J) - Z_s(K).

This is multi-affine in the response coordinates used by J union K. Therefore
its exact branchwise minimum and maximum on an axis-aligned rational parameter
box occur at endpoint vertices. Minus-branch and plus-branch response
coordinates are disjoint, and latent prevalence enters affinely, so the exact
mixture contrast interval follows from the two exact branch intervals and the
two prevalence endpoints.

There are eleven P83 view sets,

    C(4,2) + C(4,3) + C(4,4) = 11,

and therefore

    C(11,2) = 55

standard P84 pairwise contrasts.

For distinct J and K, chi_J - chi_K is zero on eight of the sixteen observed
cells and has magnitude two on the other eight. Hence its coefficient L1 norm
is exactly sixteen. If ||p-q||_inf <= r,

    |D_p(J,K) - D_q(J,K)| <= 16 r.

Distance from an empirical contrast to its exact P75 box interval divided by
sixteen is therefore a valid full-law L-infinity lower bound.

The final P84 box certificate is

    max(P83 lower bound, exact coupled parity-contrast lower bound).

It is never weaker than P83 and can be strictly stronger. An exact rational
witness fixes q2_minus=q3_minus=1/4 and q2_plus=q3_plus=3/4 while leaving
prevalence, view 1, and view 4 response parameters unrestricted. Every P81
cylinder, P82 nested residual, and P83 parity observable is individually
compatible with the declared box for the witness empirical law, so the complete
P83 box certificate is zero. Yet the model forces the pairwise contrast between
views (0,1) and (0,2) to zero, while the empirical contrast is 3/4. P84 therefore
certifies the strict positive lower bound 3/64.

The P78 mesh-width upper certificate is retained unchanged for global
branch-and-bound. P84 does not claim a new convergence theorem. This result
strengthens rejection of the declared P75 target-measurement family only. It
does not validate the P75 model, identify a latent state with consciousness, or
solve the physical-to-experiential bridge.
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
    p75_box_p83_linf_lower_bound_exact,
)
from consciousness_bridge.simplex_coupled_model_separation import (
    p75_box_simplex_linf_lower_bound_exact,
)

_VIEW_COUNT = 4
_OUTCOME_COUNT = 1 << _VIEW_COUNT
_CONTRAST_COEFFICIENT_L1 = 16

ParityViewSet = tuple[int, ...]
ParityContrastSpec = tuple[ParityViewSet, ParityViewSet]


def _standard_parity_view_sets() -> tuple[ParityViewSet, ...]:
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
    first_views: tuple[int, ...]
    second_views: tuple[int, ...]
    coefficient_l1_norm: int
    empirical_first_expectation: Fraction
    empirical_second_expectation: Fraction
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
    root_parity_contrast_bound: Fraction
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


def _validate_view_set(views: tuple[int, ...]) -> None:
    if views not in _STANDARD_PARITY_VIEW_SETS:
        raise ValueError(
            "P84 parity view sets must be strictly increasing two-, three-, or four-view subsets"
        )


def _validate_contrast_spec(
    first_views: tuple[int, ...],
    second_views: tuple[int, ...],
) -> None:
    _validate_view_set(first_views)
    _validate_view_set(second_views)
    if first_views == second_views:
        raise ValueError("P84 parity contrast requires two distinct view sets")


def p84_standard_contrast_count() -> int:
    """Return the number of standard pairwise parity contrasts used by P84."""

    return len(_STANDARD_PARITY_CONTRASTS)


def _branch_parity_expectation_contrast_interval_exact(
    box: P78ParameterBox,
    first_views: tuple[int, ...],
    second_views: tuple[int, ...],
    *,
    plus_branch: bool,
) -> tuple[Fraction, Fraction]:
    """Return the exact branchwise interval of one signed parity contrast."""

    branch_offset = 2 if plus_branch else 1
    union_views = tuple(sorted(set(first_views) | set(second_views)))
    factor_endpoints: list[tuple[Fraction, Fraction]] = []
    for view in union_views:
        index = branch_offset + 2 * view
        q_lower = box.lower[index]
        q_upper = box.upper[index]
        factor_endpoints.append((1 - 2 * q_upper, 1 - 2 * q_lower))

    values: list[Fraction] = []
    for endpoint_choice in product(*factor_endpoints):
        factor_by_view = dict(zip(union_views, endpoint_choice, strict=True))
        first_product = Fraction(1)
        second_product = Fraction(1)
        for view in first_views:
            first_product *= factor_by_view[view]
        for view in second_views:
            second_product *= factor_by_view[view]
        values.append(first_product - second_product)

    return min(values), max(values)


def p75_projection_parity_expectation_contrast_interval_exact(
    box: P78ParameterBox,
    first_views: tuple[int, ...],
    second_views: tuple[int, ...],
) -> tuple[Fraction, Fraction]:
    """Return the exact P75 box interval of ``Z(first)-Z(second)``."""

    _validate_contrast_spec(first_views, second_views)
    minus_lower, minus_upper = _branch_parity_expectation_contrast_interval_exact(
        box,
        first_views,
        second_views,
        plus_branch=False,
    )
    plus_lower, plus_upper = _branch_parity_expectation_contrast_interval_exact(
        box,
        first_views,
        second_views,
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


def empirical_projection_parity_expectation_exact(
    empirical_law: tuple[Fraction, ...],
    views: tuple[int, ...],
) -> Fraction:
    """Return the exact signed parity expectation for one empirical law."""

    _validate_view_set(views)
    if len(empirical_law) != _OUTCOME_COUNT:
        raise ValueError("empirical law must contain sixteen observed-cell masses")
    if any(not isinstance(mass, Fraction) for mass in empirical_law):
        raise TypeError("empirical law masses must be fractions.Fraction values")
    if any(mass < 0 or mass > 1 for mass in empirical_law):
        raise ValueError("empirical law masses must lie in [0, 1]")
    if sum(empirical_law, start=Fraction(0)) != 1:
        raise ValueError("empirical law must sum exactly to one")

    total = Fraction(0)
    for outcome, mass in zip(
        product((0, 1), repeat=_VIEW_COUNT),
        empirical_law,
        strict=True,
    ):
        sign = 1 if sum(outcome[view] for view in views) % 2 == 0 else -1
        total += sign * mass
    return total


def empirical_projection_parity_contrast_exact(
    empirical_law: tuple[Fraction, ...],
    first_views: tuple[int, ...],
    second_views: tuple[int, ...],
) -> Fraction:
    """Return the exact empirical signed parity contrast."""

    _validate_contrast_spec(first_views, second_views)
    return empirical_projection_parity_expectation_exact(
        empirical_law,
        first_views,
    ) - empirical_projection_parity_expectation_exact(
        empirical_law,
        second_views,
    )


def p75_box_projection_parity_contrast_witness_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> P84ParityContrastWitness:
    """Return the strongest standard exact P84 coupled parity witness."""

    expectation_by_views = {
        views: empirical_projection_parity_expectation_exact(empirical_law, views)
        for views in _STANDARD_PARITY_VIEW_SETS
    }

    best: P84ParityContrastWitness | None = None
    for first_views, second_views in _STANDARD_PARITY_CONTRASTS:
        empirical_first = expectation_by_views[first_views]
        empirical_second = expectation_by_views[second_views]
        empirical_contrast = empirical_first - empirical_second
        interval_lower, interval_upper = (
            p75_projection_parity_expectation_contrast_interval_exact(
                box,
                first_views,
                second_views,
            )
        )
        minus_lower, minus_upper = _branch_parity_expectation_contrast_interval_exact(
            box,
            first_views,
            second_views,
            plus_branch=False,
        )
        plus_lower, plus_upper = _branch_parity_expectation_contrast_interval_exact(
            box,
            first_views,
            second_views,
            plus_branch=True,
        )
        lower_bound = (
            _distance_to_interval(
                empirical_contrast,
                interval_lower,
                interval_upper,
            )
            / _CONTRAST_COEFFICIENT_L1
        )
        candidate = P84ParityContrastWitness(
            lower_bound=lower_bound,
            first_views=first_views,
            second_views=second_views,
            coefficient_l1_norm=_CONTRAST_COEFFICIENT_L1,
            empirical_first_expectation=empirical_first,
            empirical_second_expectation=empirical_second,
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
        raise RuntimeError("P84 parity-contrast family unexpectedly empty")
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
        root_parity_contrast_bound=root_contrast,
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
