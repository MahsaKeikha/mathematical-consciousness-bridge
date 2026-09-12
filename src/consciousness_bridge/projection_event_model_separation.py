"""P81 projection-event certificates for continuous P75 model separation.

P80 strengthens the P78 coordinatewise box relaxation by enforcing probability
normalization. That still discards additional linear structure that every P75
law generated inside a parameter box must satisfy: probabilities of projected
(or cylinder) events have their own exact parameter-box ranges.

For a nonempty subset of the four observed binary views and a fixed assignment
on that subset, the corresponding event probability is again a two-component
latent mixture of products. Its exact minimum and maximum over a P78 parameter
box are therefore available in rational arithmetic by the same endpoint
argument used for P78 cell probabilities.

If an empirical sixteen-cell law ``p`` and a model law ``q`` satisfy
``||p-q||_inf <= r``, then a cylinder event containing ``m`` cells satisfies

    |p(C) - q(C)| <= m r.

Consequently, distance from the empirical event mass to its exact model-box
interval, divided by the number of cells in the event, is a rigorous lower
bound on full-law L-infinity distance. Maximizing over all nontrivial cylinder
events gives the P81 projection lower bound. The final P81 box certificate is

    max(P80 simplex-coupled lower bound, P81 projection lower bound).

Because four-view cylinder events are individual cells, the projection family
already contains the P78 coordinatewise bound. Combining it with P80 therefore
gives a certificate that is never weaker than P80 and can be strictly stronger.

All certification arithmetic uses ``fractions.Fraction``. This is a numerical and statistical certification result for the declared P75
latent model.
It does not validate that model.
It does not identify any latent state with consciousness.
It does not solve the physical-to-experiential bridge.
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
from consciousness_bridge.simplex_coupled_model_separation import (
    p75_box_simplex_linf_lower_bound_exact,
)

_VIEW_COUNT = 4
_OUTCOME_DIMENSION = 16
_PATTERNS = tuple(product((0, 1), repeat=_VIEW_COUNT))


@dataclass(frozen=True)
class P81ProjectionWitness:
    """Strongest cylinder-event lower-bound witness on one parameter box."""

    lower_bound: Fraction
    views: tuple[int, ...]
    assignment: tuple[int, ...]
    event_size: int
    empirical_probability: Fraction
    interval_lower: Fraction
    interval_upper: Fraction


@dataclass(frozen=True)
class P81DistanceBracket:
    """Certified global L-infinity bracket using P81 box lower bounds."""

    lower_bound: Fraction
    upper_bound: Fraction
    best_parameters: tuple[Fraction, ...]
    leaf_count: int
    evaluated_boxes: int
    iterations: int
    maximum_active_width_sum: Fraction
    p78_active_lower_bound: Fraction
    p80_active_lower_bound: Fraction
    p78_mesh_upper_bound: Fraction
    certified_gap: Fraction
    root_p78_bound: Fraction
    root_p80_bound: Fraction
    root_projection_bound: Fraction
    root_p81_bound: Fraction
    root_tightening_over_p80: Fraction
    conclusion: str


def _validate_empirical_law(empirical_law: tuple[Fraction, ...]) -> None:
    if len(empirical_law) != _OUTCOME_DIMENSION:
        raise ValueError("empirical_law must contain sixteen probabilities")
    for index, value in enumerate(empirical_law):
        if not isinstance(value, Fraction):
            raise TypeError(
                f"empirical_law[{index}] must be a fractions.Fraction"
            )
        if value < 0 or value > 1:
            raise ValueError(f"empirical_law[{index}] must lie in [0, 1]")
    if sum(empirical_law, start=Fraction(0)) != 1:
        raise ValueError("empirical_law must sum exactly to one")


def _validate_projection(
    views: tuple[int, ...],
    assignment: tuple[int, ...],
) -> None:
    if not views:
        raise ValueError("views must be nonempty")
    if len(views) != len(assignment):
        raise ValueError("views and assignment must have equal length")
    if len(set(views)) != len(views):
        raise ValueError("views must not contain duplicates")
    if tuple(sorted(views)) != views:
        raise ValueError("views must be strictly increasing")
    for view in views:
        if isinstance(view, bool) or not isinstance(view, int):
            raise TypeError("view indices must be integers")
        if view < 0 or view >= _VIEW_COUNT:
            raise ValueError("view indices must lie in {0, 1, 2, 3}")
    for observed in assignment:
        if observed not in (0, 1) or isinstance(observed, bool):
            raise ValueError("assignment entries must be binary integers 0 or 1")


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


def p75_projection_event_interval_exact(
    box: P78ParameterBox,
    views: tuple[int, ...],
    assignment: tuple[int, ...],
) -> tuple[Fraction, Fraction]:
    """Return the exact P75 probability interval for one cylinder event.

    ``views`` identifies a nonempty subset of the four observed binary views and
    ``assignment`` gives their fixed observed values. Unselected views are
    marginalized out. The resulting event probability is

        (1-pi) prod_j f(q_{j,-}, a_j)
        + pi prod_j f(q_{j,+}, a_j),

    where ``f(q, 1)=q`` and ``f(q, 0)=1-q``. Each factor is monotone on a
    parameter interval, so each latent-state product attains its exact extrema
    at endpoints. The remaining dependence on prevalence is affine, hence its
    exact extrema occur at prevalence endpoints as well.
    """

    _validate_projection(views, assignment)

    minus_min = Fraction(1)
    minus_max = Fraction(1)
    plus_min = Fraction(1)
    plus_max = Fraction(1)

    for view, observed in zip(views, assignment, strict=True):
        minus_lower = box.lower[1 + 2 * view]
        minus_upper = box.upper[1 + 2 * view]
        plus_lower = box.lower[2 + 2 * view]
        plus_upper = box.upper[2 + 2 * view]

        if observed == 1:
            minus_factor_min, minus_factor_max = minus_lower, minus_upper
            plus_factor_min, plus_factor_max = plus_lower, plus_upper
        else:
            minus_factor_min, minus_factor_max = 1 - minus_upper, 1 - minus_lower
            plus_factor_min, plus_factor_max = 1 - plus_upper, 1 - plus_lower

        minus_min *= minus_factor_min
        minus_max *= minus_factor_max
        plus_min *= plus_factor_min
        plus_max *= plus_factor_max

    prevalence_lower = box.lower[0]
    prevalence_upper = box.upper[0]

    lower_candidates = (
        (1 - prevalence_lower) * minus_min + prevalence_lower * plus_min,
        (1 - prevalence_upper) * minus_min + prevalence_upper * plus_min,
    )
    upper_candidates = (
        (1 - prevalence_lower) * minus_max + prevalence_lower * plus_max,
        (1 - prevalence_upper) * minus_max + prevalence_upper * plus_max,
    )
    return min(lower_candidates), max(upper_candidates)


def empirical_projection_probability_exact(
    empirical_law: tuple[Fraction, ...],
    views: tuple[int, ...],
    assignment: tuple[int, ...],
) -> Fraction:
    """Return the exact empirical mass of one cylinder event."""

    _validate_empirical_law(empirical_law)
    _validate_projection(views, assignment)
    return sum(
        (
            probability
            for pattern, probability in zip(_PATTERNS, empirical_law, strict=True)
            if all(pattern[view] == observed for view, observed in zip(views, assignment, strict=True))
        ),
        start=Fraction(0),
    )


def p75_box_projection_witness_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> P81ProjectionWitness:
    """Return the strongest exact cylinder-event L-infinity witness on ``box``."""

    _validate_empirical_law(empirical_law)
    best: P81ProjectionWitness | None = None

    for projection_size in range(1, _VIEW_COUNT + 1):
        event_size = 1 << (_VIEW_COUNT - projection_size)
        for views in combinations(range(_VIEW_COUNT), projection_size):
            for assignment in product((0, 1), repeat=projection_size):
                empirical_probability = empirical_projection_probability_exact(
                    empirical_law,
                    views,
                    assignment,
                )
                interval_lower, interval_upper = p75_projection_event_interval_exact(
                    box,
                    views,
                    assignment,
                )
                interval_distance = _distance_to_interval(
                    empirical_probability,
                    interval_lower,
                    interval_upper,
                )
                lower_bound = interval_distance / event_size
                candidate = P81ProjectionWitness(
                    lower_bound=lower_bound,
                    views=views,
                    assignment=assignment,
                    event_size=event_size,
                    empirical_probability=empirical_probability,
                    interval_lower=interval_lower,
                    interval_upper=interval_upper,
                )
                if best is None or candidate.lower_bound > best.lower_bound:
                    best = candidate

    if best is None:
        raise RuntimeError("projection family unexpectedly empty")
    return best


def p75_box_projection_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the strongest P81 projection-event lower bound on one box."""

    return p75_box_projection_witness_exact(empirical_law, box).lower_bound


def p75_box_p81_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the P81 box certificate ``max(P80, projection)``."""

    p80 = p75_box_simplex_linf_lower_bound_exact(empirical_law, box)
    projection = p75_box_projection_linf_lower_bound_exact(empirical_law, box)
    return max(p80, projection)


def p81_dominates_p80_on_box(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> bool:
    """Return the exact dominance check P81(B) >= P80(B)."""

    return p75_box_p81_linf_lower_bound_exact(
        empirical_law,
        box,
    ) >= p75_box_simplex_linf_lower_bound_exact(empirical_law, box)


def certified_p75_linf_branch_and_bound_projection(
    counts: tuple[int, ...],
    *,
    max_leaves: int = 256,
    gap_tolerance: Fraction = Fraction(0),
) -> P81DistanceBracket:
    """Return a global P75 distance bracket using P81 box lower bounds.

    Active boxes always partition the full P75 parameter cube. P81 lower bounds
    drive refinement. Explicit box centers provide valid global upper bounds.
    The already-proved P78 mesh-width upper certificate remains the conservative
    convergence certificate: the routine retains the P78 lower bound on every
    active box and combines its minimum with the maximum active width sum.
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
    root_projection = p75_box_projection_linf_lower_bound_exact(empirical_law, root)
    root_p81 = max(root_p80, root_projection)
    root_center = root.center
    root_upper = linf_distance_exact(
        empirical_law,
        p75_four_view_law_exact(root_center),
    )

    serial = 0
    active: list[
        tuple[Fraction, int, P78ParameterBox, Fraction, Fraction]
    ] = []
    heappush(active, (root_p81, serial, root, root_p80, root_p78))
    serial += 1

    best_upper = root_upper
    best_parameters = root_center
    evaluated_boxes = 1
    iterations = 0

    while len(active) < max_leaves:
        global_lower = active[0][0]
        if best_upper - global_lower <= gap_tolerance:
            break

        _, _, box, _, _ = heappop(active)
        if box.width_sum == 0:
            p78_lower = p75_box_linf_lower_bound_exact(empirical_law, box)
            p80_lower = p75_box_simplex_linf_lower_bound_exact(empirical_law, box)
            p81_lower = p75_box_p81_linf_lower_bound_exact(empirical_law, box)
            heappush(
                active,
                (p81_lower, serial, box, p80_lower, p78_lower),
            )
            break

        left, right = box.split_widest()
        for child in (left, right):
            p78_lower = p75_box_linf_lower_bound_exact(empirical_law, child)
            p80_lower = p75_box_simplex_linf_lower_bound_exact(empirical_law, child)
            p81_lower = max(
                p80_lower,
                p75_box_projection_linf_lower_bound_exact(empirical_law, child),
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
                (p81_lower, serial, child, p80_lower, p78_lower),
            )
            serial += 1
            evaluated_boxes += 1
        iterations += 1

    global_lower = active[0][0]
    p80_active_lower = min(entry[3] for entry in active)
    p78_active_lower = min(entry[4] for entry in active)
    maximum_width_sum = max(entry[2].width_sum for entry in active)
    p78_mesh_upper = p78_active_lower + maximum_width_sum
    certified_upper = min(best_upper, p78_mesh_upper)
    certified_gap = certified_upper - global_lower

    if certified_gap < 0:
        raise RuntimeError("certified upper bound fell below the P81 lower bound")

    if global_lower == certified_upper:
        conclusion = "exact global L-infinity model distance certified"
    elif len(active) >= max_leaves:
        conclusion = (
            "valid P81 global distance bracket; leaf budget exhausted before exact closure"
        )
    else:
        conclusion = "valid P81 global distance bracket; requested gap tolerance reached"

    return P81DistanceBracket(
        lower_bound=global_lower,
        upper_bound=certified_upper,
        best_parameters=best_parameters,
        leaf_count=len(active),
        evaluated_boxes=evaluated_boxes,
        iterations=iterations,
        maximum_active_width_sum=maximum_width_sum,
        p78_active_lower_bound=p78_active_lower,
        p80_active_lower_bound=p80_active_lower,
        p78_mesh_upper_bound=p78_mesh_upper,
        certified_gap=certified_gap,
        root_p78_bound=root_p78,
        root_p80_bound=root_p80,
        root_projection_bound=root_projection,
        root_p81_bound=root_p81,
        root_tightening_over_p80=root_p81 - root_p80,
        conclusion=conclusion,
    )


def p81_rejection_with_p79_radius(
    bracket: P81DistanceBracket,
    radius: P79SamplingRadiusCertificate,
) -> bool:
    """Apply the strict P77 rejection gate with P81/P79 certified directions."""

    return bracket.lower_bound > radius.cell_linf_radius_upper
