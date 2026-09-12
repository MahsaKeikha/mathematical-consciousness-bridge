"""P83 exact projection-parity certificates for continuous P75 separation.

P82 strengthens projected-event separation with exact residual events formed from
nested cylinders. Those residuals still do not exhaust simple dependency-aware
observables. P83 retains the complete P82 certificate and adds every nontrivial
binary parity event on two, three, or four observed views.

For a selected view set J and parity b in {0,1}, define

    H(J,b) = {x : XOR_{j in J} x_j = b}.

Inside one latent branch s of P75, conditional independence gives the exact
parity identity

    P_s(H(J,b))
      = [1 + (-1)^b product_{j in J}(1 - 2 q_{j,s})] / 2.

On an axis-aligned rational parameter box, each factor (1 - 2 q_{j,s}) lies in
a rational interval. The product is multi-affine in the response coordinates,
so its extrema occur at endpoint vertices. The minus-branch coordinates,
plus-branch coordinates, and prevalence are disjoint; after exact branchwise
extremization, the latent mixture is affine in prevalence and its extrema occur
at the two prevalence endpoints. Therefore every P83 parity interval is exact, not merely an enclosure.

If ||p-q||_inf <= r, every event S obeys

    |p(S)-q(S)| <= |S| r.

Every parity event on at least two of the four binary views contains exactly
eight of the sixteen observed cells, so empirical separation from its exact P75
box interval divided by eight is a valid full-law L-infinity lower bound.

There are

    2 * [C(4,2) + C(4,3) + C(4,4)] = 22

standard P83 parity events. One-view parities are omitted because they are
ordinary P81 cylinders.

The final P83 box certificate is

    max(P82 lower bound, exact projection-parity lower bound).

It is therefore never weaker than P82 and can be strictly stronger. A clean
exact-rational witness fixes one observed channel to Bernoulli(1/2) in both
latent branches while leaving another channel unrestricted. P75 then forces
their even and odd parities to probability 1/2, although the separate joint
cylinder intervals remain broad. An empirical law supported only on equal-bit
pairs has P82 lower bound zero but P83 lower bound 1/16.

The P78 mesh-width upper certificate is retained unchanged for global
branch-and-bound. P83 does not claim a new convergence theorem. This certificate does not validate the P75 model, does not identify a latent
state with consciousness, and does not close the physical-to-experiential bridge.
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
from consciousness_bridge.simplex_coupled_model_separation import (
    p75_box_simplex_linf_lower_bound_exact,
)

_VIEW_COUNT = 4
_PARITY_SUPPORT_SIZE = 1 << (_VIEW_COUNT - 1)
ParitySpec = tuple[tuple[int, ...], int]


def _standard_parity_specs() -> tuple[ParitySpec, ...]:
    return tuple(
        (views, parity)
        for size in range(2, _VIEW_COUNT + 1)
        for views in combinations(range(_VIEW_COUNT), size)
        for parity in (0, 1)
    )


_STANDARD_PARITY_SPECS = _standard_parity_specs()


@dataclass(frozen=True)
class P83ParityWitness:
    """Strongest exact projection-parity witness on one P75 parameter box."""

    lower_bound: Fraction
    views: tuple[int, ...]
    parity: int
    support_size: int
    empirical_probability: Fraction
    interval_lower: Fraction
    interval_upper: Fraction
    minus_branch_lower: Fraction
    minus_branch_upper: Fraction
    plus_branch_lower: Fraction
    plus_branch_upper: Fraction


@dataclass(frozen=True)
class P83DistanceBracket:
    """Certified global L-infinity bracket using P83 box lower bounds."""

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
    p78_mesh_upper_bound: Fraction
    certified_gap: Fraction
    root_p78_bound: Fraction
    root_p80_bound: Fraction
    root_p81_bound: Fraction
    root_p82_bound: Fraction
    root_parity_bound: Fraction
    root_p83_bound: Fraction
    root_tightening_over_p82: Fraction
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


def _validate_parity_spec(views: tuple[int, ...], parity: int) -> None:
    if isinstance(parity, bool) or not isinstance(parity, int) or parity not in (0, 1):
        raise ValueError("parity must be the integer 0 or 1")
    if len(views) < 2 or len(views) > _VIEW_COUNT:
        raise ValueError("P83 parity events must use between two and four views")
    if tuple(sorted(set(views))) != views:
        raise ValueError("views must be a strictly increasing tuple of distinct indices")
    if any(view < 0 or view >= _VIEW_COUNT for view in views):
        raise ValueError("view indices must lie in {0,1,2,3}")


def p83_standard_parity_count() -> int:
    """Return the number of genuinely new standard projection-parity events."""

    return len(_STANDARD_PARITY_SPECS)


def _branch_parity_interval_exact(
    box: P78ParameterBox,
    views: tuple[int, ...],
    parity: int,
    *,
    plus_branch: bool,
) -> tuple[Fraction, Fraction]:
    """Return the exact branchwise probability interval of one parity event."""

    branch_offset = 2 if plus_branch else 1
    factor_endpoints: list[tuple[Fraction, Fraction]] = []
    for view in views:
        index = branch_offset + 2 * view
        q_lower = box.lower[index]
        q_upper = box.upper[index]
        factor_endpoints.append((1 - 2 * q_upper, 1 - 2 * q_lower))

    product_values = tuple(
        _product_exact(endpoint_choice)
        for endpoint_choice in product(*factor_endpoints)
    )
    product_lower = min(product_values)
    product_upper = max(product_values)

    sign = 1 if parity == 0 else -1
    values = (
        (1 + sign * product_lower) / 2,
        (1 + sign * product_upper) / 2,
    )
    return min(values), max(values)


def _product_exact(values: tuple[Fraction, ...]) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= value
    return result


def p75_projection_parity_interval_exact(
    box: P78ParameterBox,
    views: tuple[int, ...],
    parity: int,
) -> tuple[Fraction, Fraction]:
    """Return the exact P75 parameter-box range of a projection parity event."""

    _validate_parity_spec(views, parity)
    minus_lower, minus_upper = _branch_parity_interval_exact(
        box,
        views,
        parity,
        plus_branch=False,
    )
    plus_lower, plus_upper = _branch_parity_interval_exact(
        box,
        views,
        parity,
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


def empirical_projection_parity_probability_exact(
    empirical_law: tuple[Fraction, ...],
    views: tuple[int, ...],
    parity: int,
) -> Fraction:
    """Return the exact empirical probability of one projection parity event."""

    _validate_parity_spec(views, parity)
    if len(empirical_law) != 1 << _VIEW_COUNT:
        raise ValueError("empirical law must contain sixteen observed-cell masses")

    total = Fraction(0)
    for outcome, mass in zip(
        product((0, 1), repeat=_VIEW_COUNT),
        empirical_law,
        strict=True,
    ):
        if sum(outcome[view] for view in views) % 2 == parity:
            total += mass
    return total


def p75_box_projection_parity_witness_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> P83ParityWitness:
    """Return the strongest standard exact P83 projection-parity witness."""

    best: P83ParityWitness | None = None
    for views, parity in _STANDARD_PARITY_SPECS:
        empirical_probability = empirical_projection_parity_probability_exact(
            empirical_law,
            views,
            parity,
        )
        interval_lower, interval_upper = p75_projection_parity_interval_exact(
            box,
            views,
            parity,
        )
        minus_lower, minus_upper = _branch_parity_interval_exact(
            box,
            views,
            parity,
            plus_branch=False,
        )
        plus_lower, plus_upper = _branch_parity_interval_exact(
            box,
            views,
            parity,
            plus_branch=True,
        )
        lower_bound = (
            _distance_to_interval(
                empirical_probability,
                interval_lower,
                interval_upper,
            )
            / _PARITY_SUPPORT_SIZE
        )
        candidate = P83ParityWitness(
            lower_bound=lower_bound,
            views=views,
            parity=parity,
            support_size=_PARITY_SUPPORT_SIZE,
            empirical_probability=empirical_probability,
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
        raise RuntimeError("P83 projection-parity family unexpectedly empty")
    return best


def p75_box_projection_parity_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the strongest standard exact P83 projection-parity lower bound."""

    return p75_box_projection_parity_witness_exact(empirical_law, box).lower_bound


def p75_box_p83_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the P83 box certificate ``max(P82, exact projection parity)``."""

    p82 = p75_box_p82_linf_lower_bound_exact(empirical_law, box)
    parity = p75_box_projection_parity_linf_lower_bound_exact(empirical_law, box)
    return max(p82, parity)


def p83_dominates_p82_on_box(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> bool:
    """Return the exact dominance check P83(B) >= P82(B)."""

    return p75_box_p83_linf_lower_bound_exact(
        empirical_law,
        box,
    ) >= p75_box_p82_linf_lower_bound_exact(empirical_law, box)


def certified_p75_linf_branch_and_bound_parity(
    counts: tuple[int, ...],
    *,
    max_leaves: int = 256,
    gap_tolerance: Fraction = Fraction(0),
) -> P83DistanceBracket:
    """Return a global P75 distance bracket using exact P83 box lower bounds.

    Active boxes partition the complete P75 parameter cube. P83 lower bounds
    drive refinement. Explicit box centers remain valid global upper witnesses.
    The already-proved P78 mesh-width upper certificate is retained unchanged;
    no new P83 convergence-rate theorem is assumed.
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
    root_parity = p75_box_projection_parity_linf_lower_bound_exact(
        empirical_law,
        root,
    )
    root_p83 = max(root_p82, root_parity)
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
        ]
    ] = []
    heappush(
        active,
        (root_p83, serial, root, root_p82, root_p81, root_p80, root_p78),
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

        _, _, box, _, _, _, _ = heappop(active)
        if box.width_sum == 0:
            p78_lower = p75_box_linf_lower_bound_exact(empirical_law, box)
            p80_lower = p75_box_simplex_linf_lower_bound_exact(empirical_law, box)
            p81_lower = p75_box_p81_linf_lower_bound_exact(empirical_law, box)
            p82_lower = p75_box_p82_linf_lower_bound_exact(empirical_law, box)
            p83_lower = p75_box_p83_linf_lower_bound_exact(empirical_law, box)
            heappush(
                active,
                (
                    p83_lower,
                    serial,
                    box,
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
            p83_lower = max(
                p82_lower,
                p75_box_projection_parity_linf_lower_bound_exact(
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
                    p83_lower,
                    serial,
                    child,
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
    p82_active_lower = min(entry[3] for entry in active)
    p81_active_lower = min(entry[4] for entry in active)
    p80_active_lower = min(entry[5] for entry in active)
    p78_active_lower = min(entry[6] for entry in active)
    maximum_width_sum = max(entry[2].width_sum for entry in active)
    p78_mesh_upper = p78_active_lower + maximum_width_sum
    certified_upper = min(best_upper, p78_mesh_upper)
    certified_gap = certified_upper - global_lower

    if certified_gap < 0:
        raise RuntimeError("certified upper bound fell below the P83 lower bound")

    if global_lower == certified_upper:
        conclusion = "exact global L-infinity model distance certified"
    elif len(active) >= max_leaves:
        conclusion = (
            "valid P83 global distance bracket; leaf budget exhausted before exact closure"
        )
    else:
        conclusion = "valid P83 global distance bracket; requested gap tolerance reached"

    return P83DistanceBracket(
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
        p78_mesh_upper_bound=p78_mesh_upper,
        certified_gap=certified_gap,
        root_p78_bound=root_p78,
        root_p80_bound=root_p80,
        root_p81_bound=root_p81,
        root_p82_bound=root_p82,
        root_parity_bound=root_parity,
        root_p83_bound=root_p83,
        root_tightening_over_p82=root_p83 - root_p82,
        conclusion=conclusion,
    )


def p83_rejection_with_p79_radius(
    bracket: P83DistanceBracket,
    radius: P79SamplingRadiusCertificate,
) -> bool:
    """Apply the strict P77 rejection gate with P83/P79 certified directions."""

    return bracket.lower_bound > radius.cell_linf_radius_upper
