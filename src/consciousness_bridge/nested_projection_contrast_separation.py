"""P82 exact nested projection-contrast certificates for continuous P75 separation.

P81 strengthens the P80 box relaxation by testing every nonempty cylinder event
on the four observed binary views. Each event is still tested separately. P82
retains P81 and adds a finite family of residual events formed from nested
cylinders.

Let B be a strict child cylinder of A. Then

    1_A - 1_B = 1_{A \\ B}.

The residual is generally not itself a cylinder when the child fixes at least
two additional views. The key P82 observation is that its model-box interval can
be computed exactly, rather than by conservatively subtracting the separate P81
intervals for A and B.

Write the child as the parent constraints plus an added-view event D. Under one
latent branch s of P75, conditional independence gives

    P_s(A \\ B) = P_s(A) [1 - P_s(D)].

The parent and added-view products use disjoint response coordinates. Therefore,
on an axis-aligned parameter box, if

    P_s(A) in [a_s^L, a_s^U],
    P_s(D) in [d_s^L, d_s^U],

then the exact branchwise residual range is

    [a_s^L (1-d_s^U), a_s^U (1-d_s^L)].

The remaining dependence on latent prevalence is affine, so evaluating the two
prevalence endpoints gives the exact global residual interval on the box.

If ``||p-q||_inf <= r``, every finite event S satisfies

    |p(S)-q(S)| <= |S| r.

Therefore empirical separation of a nested residual event from its exact model
interval, divided by the residual support size, is a valid lower bound on the
full-law L-infinity distance.

The standard P82 contrast family uses every nested parent/child cylinder pair
for which the child fixes at least two additional views. There are 256 such
pairs for four binary views. One-view refinements are deliberately omitted:
their residual is exactly the sibling cylinder and is already present in P81.

The final P82 box certificate is

    max(P81 lower bound, exact nested-contrast lower bound).

It is therefore never weaker than P81 and can be strictly stronger. The P78
mesh-width upper certificate is retained unchanged for global branch-and-bound;
P82 does not silently claim a new convergence theorem.

This is a computational certificate for the declared P75 latent model. It does
not validate that model, identify any latent state with consciousness, or solve
the physical-to-experiential bridge.
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
from consciousness_bridge.projection_event_model_separation import (
    empirical_projection_probability_exact,
    p75_box_p81_linf_lower_bound_exact,
    p75_projection_event_interval_exact,
)
from consciousness_bridge.simplex_coupled_model_separation import (
    p75_box_simplex_linf_lower_bound_exact,
)

_VIEW_COUNT = 4

ProjectionSpec = tuple[tuple[int, ...], tuple[int, ...]]


def _projection_specs() -> tuple[ProjectionSpec, ...]:
    specs: list[ProjectionSpec] = []
    for size in range(1, _VIEW_COUNT + 1):
        for views in combinations(range(_VIEW_COUNT), size):
            for assignment in product((0, 1), repeat=size):
                specs.append((views, assignment))
    return tuple(specs)


def _is_nested_projection(
    parent: ProjectionSpec,
    child: ProjectionSpec,
    *,
    minimum_added_views: int = 1,
) -> bool:
    parent_views, parent_assignment = parent
    child_views, child_assignment = child
    if len(child_views) - len(parent_views) < minimum_added_views:
        return False
    child_map = dict(zip(child_views, child_assignment, strict=True))
    return all(
        view in child_map and child_map[view] == observed
        for view, observed in zip(parent_views, parent_assignment, strict=True)
    )


_PROJECTIONS = _projection_specs()
_STANDARD_NESTED_PAIRS = tuple(
    (parent, child)
    for parent in _PROJECTIONS
    for child in _PROJECTIONS
    if _is_nested_projection(parent, child, minimum_added_views=2)
)


@dataclass(frozen=True)
class P82ContrastWitness:
    """Strongest exact nested-cylinder residual witness on one parameter box."""

    lower_bound: Fraction
    parent_views: tuple[int, ...]
    parent_assignment: tuple[int, ...]
    child_views: tuple[int, ...]
    child_assignment: tuple[int, ...]
    support_size: int
    empirical_residual_probability: Fraction
    interval_lower: Fraction
    interval_upper: Fraction
    subtraction_interval_lower: Fraction
    subtraction_interval_upper: Fraction
    parent_empirical_probability: Fraction
    child_empirical_probability: Fraction
    parent_interval_lower: Fraction
    parent_interval_upper: Fraction
    child_interval_lower: Fraction
    child_interval_upper: Fraction


@dataclass(frozen=True)
class P82DistanceBracket:
    """Certified global L-infinity bracket using P82 box lower bounds."""

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
    p78_mesh_upper_bound: Fraction
    certified_gap: Fraction
    root_p78_bound: Fraction
    root_p80_bound: Fraction
    root_p81_bound: Fraction
    root_contrast_bound: Fraction
    root_p82_bound: Fraction
    root_tightening_over_p81: Fraction
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


def _event_size(views: tuple[int, ...]) -> int:
    return 1 << (_VIEW_COUNT - len(views))


def _validate_nested_pair(
    parent_views: tuple[int, ...],
    parent_assignment: tuple[int, ...],
    child_views: tuple[int, ...],
    child_assignment: tuple[int, ...],
) -> None:
    parent = (parent_views, parent_assignment)
    child = (child_views, child_assignment)

    if parent not in _PROJECTIONS:
        raise ValueError("parent must be a valid nonempty four-view cylinder")
    if child not in _PROJECTIONS:
        raise ValueError("child must be a valid nonempty four-view cylinder")
    if not _is_nested_projection(parent, child):
        raise ValueError("child cylinder must be a strict subset of parent cylinder")


def _branch_projection_product_interval_exact(
    box: P78ParameterBox,
    views: tuple[int, ...],
    assignment: tuple[int, ...],
    *,
    plus_branch: bool,
) -> tuple[Fraction, Fraction]:
    """Return the exact branchwise product range for one cylinder."""

    lower_product = Fraction(1)
    upper_product = Fraction(1)
    branch_offset = 2 if plus_branch else 1

    for view, observed in zip(views, assignment, strict=True):
        index = branch_offset + 2 * view
        lower = box.lower[index]
        upper = box.upper[index]
        if observed:
            factor_lower, factor_upper = lower, upper
        else:
            factor_lower, factor_upper = 1 - upper, 1 - lower
        lower_product *= factor_lower
        upper_product *= factor_upper

    return lower_product, upper_product


def _added_projection(parent: ProjectionSpec, child: ProjectionSpec) -> ProjectionSpec:
    """Return the child constraints not already fixed by the parent."""

    parent_views, _ = parent
    child_views, child_assignment = child
    child_map = dict(zip(child_views, child_assignment, strict=True))
    added_views = tuple(view for view in child_views if view not in parent_views)
    added_assignment = tuple(child_map[view] for view in added_views)
    return added_views, added_assignment


def p82_standard_contrast_count() -> int:
    """Return the number of genuinely new nested contrasts used by P82."""

    return len(_STANDARD_NESTED_PAIRS)


def p75_nested_projection_contrast_subtraction_enclosure_exact(
    box: P78ParameterBox,
    parent_views: tuple[int, ...],
    parent_assignment: tuple[int, ...],
    child_views: tuple[int, ...],
    child_assignment: tuple[int, ...],
) -> tuple[Fraction, Fraction]:
    """Return the sound but generally conservative P81-interval subtraction bound."""

    _validate_nested_pair(
        parent_views,
        parent_assignment,
        child_views,
        child_assignment,
    )
    parent_lower, parent_upper = p75_projection_event_interval_exact(
        box,
        parent_views,
        parent_assignment,
    )
    child_lower, child_upper = p75_projection_event_interval_exact(
        box,
        child_views,
        child_assignment,
    )
    return (
        max(Fraction(0), parent_lower - child_upper),
        min(Fraction(1), parent_upper - child_lower),
    )


def p75_nested_projection_contrast_interval_exact(
    box: P78ParameterBox,
    parent_views: tuple[int, ...],
    parent_assignment: tuple[int, ...],
    child_views: tuple[int, ...],
    child_assignment: tuple[int, ...],
) -> tuple[Fraction, Fraction]:
    """Return the exact P75 parameter-box range of ``P(A \\ B)``.

    For a nested child ``B=A intersect D``, conditional independence inside each
    latent branch gives ``P_s(A\\B)=P_s(A)(1-P_s(D))``. ``A`` and ``D`` use
    disjoint response coordinates, so their branchwise extrema can be combined
    independently and are attained simultaneously. The mixture prevalence is a
    separate coordinate and enters affinely, so its two box endpoints complete
    the exact extremization.
    """

    _validate_nested_pair(
        parent_views,
        parent_assignment,
        child_views,
        child_assignment,
    )
    parent = (parent_views, parent_assignment)
    child = (child_views, child_assignment)
    added_views, added_assignment = _added_projection(parent, child)

    branch_lower: list[Fraction] = []
    branch_upper: list[Fraction] = []
    for plus_branch in (False, True):
        parent_lower, parent_upper = _branch_projection_product_interval_exact(
            box,
            parent_views,
            parent_assignment,
            plus_branch=plus_branch,
        )
        added_lower, added_upper = _branch_projection_product_interval_exact(
            box,
            added_views,
            added_assignment,
            plus_branch=plus_branch,
        )
        branch_lower.append(parent_lower * (1 - added_upper))
        branch_upper.append(parent_upper * (1 - added_lower))

    prevalence_lower = box.lower[0]
    prevalence_upper = box.upper[0]
    lower_candidates = tuple(
        (1 - prevalence) * branch_lower[0] + prevalence * branch_lower[1]
        for prevalence in (prevalence_lower, prevalence_upper)
    )
    upper_candidates = tuple(
        (1 - prevalence) * branch_upper[0] + prevalence * branch_upper[1]
        for prevalence in (prevalence_lower, prevalence_upper)
    )
    return min(lower_candidates), max(upper_candidates)


def p75_nested_projection_contrast_enclosure_exact(
    box: P78ParameterBox,
    parent_views: tuple[int, ...],
    parent_assignment: tuple[int, ...],
    child_views: tuple[int, ...],
    child_assignment: tuple[int, ...],
) -> tuple[Fraction, Fraction]:
    """Compatibility name for the exact P82 nested-residual interval."""

    return p75_nested_projection_contrast_interval_exact(
        box,
        parent_views,
        parent_assignment,
        child_views,
        child_assignment,
    )


def empirical_nested_projection_contrast_exact(
    empirical_law: tuple[Fraction, ...],
    parent_views: tuple[int, ...],
    parent_assignment: tuple[int, ...],
    child_views: tuple[int, ...],
    child_assignment: tuple[int, ...],
) -> Fraction:
    """Return the exact empirical probability of ``A \\ B``."""

    _validate_nested_pair(
        parent_views,
        parent_assignment,
        child_views,
        child_assignment,
    )
    parent_mass = empirical_projection_probability_exact(
        empirical_law,
        parent_views,
        parent_assignment,
    )
    child_mass = empirical_projection_probability_exact(
        empirical_law,
        child_views,
        child_assignment,
    )
    residual = parent_mass - child_mass
    if residual < 0:
        raise RuntimeError("empirical child mass exceeded parent mass")
    return residual


def p75_box_nested_projection_contrast_witness_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> P82ContrastWitness:
    """Return the strongest standard exact P82 nested-contrast witness."""

    empirical_by_projection: dict[ProjectionSpec, Fraction] = {}
    interval_by_projection: dict[ProjectionSpec, tuple[Fraction, Fraction]] = {}

    for spec in _PROJECTIONS:
        views, assignment = spec
        empirical_by_projection[spec] = empirical_projection_probability_exact(
            empirical_law,
            views,
            assignment,
        )
        interval_by_projection[spec] = p75_projection_event_interval_exact(
            box,
            views,
            assignment,
        )

    best: P82ContrastWitness | None = None
    for parent, child in _STANDARD_NESTED_PAIRS:
        parent_views, parent_assignment = parent
        child_views, child_assignment = child
        parent_empirical = empirical_by_projection[parent]
        child_empirical = empirical_by_projection[child]
        parent_lower, parent_upper = interval_by_projection[parent]
        child_lower, child_upper = interval_by_projection[child]

        empirical_residual = parent_empirical - child_empirical
        interval_lower, interval_upper = p75_nested_projection_contrast_interval_exact(
            box,
            parent_views,
            parent_assignment,
            child_views,
            child_assignment,
        )
        subtraction_lower = max(Fraction(0), parent_lower - child_upper)
        subtraction_upper = min(Fraction(1), parent_upper - child_lower)
        if interval_lower < subtraction_lower or interval_upper > subtraction_upper:
            raise RuntimeError("exact residual interval escaped subtraction enclosure")

        support_size = _event_size(parent_views) - _event_size(child_views)
        if support_size <= 0:
            raise RuntimeError("nested residual support must be positive")

        lower_bound = (
            _distance_to_interval(
                empirical_residual,
                interval_lower,
                interval_upper,
            )
            / support_size
        )
        candidate = P82ContrastWitness(
            lower_bound=lower_bound,
            parent_views=parent_views,
            parent_assignment=parent_assignment,
            child_views=child_views,
            child_assignment=child_assignment,
            support_size=support_size,
            empirical_residual_probability=empirical_residual,
            interval_lower=interval_lower,
            interval_upper=interval_upper,
            subtraction_interval_lower=subtraction_lower,
            subtraction_interval_upper=subtraction_upper,
            parent_empirical_probability=parent_empirical,
            child_empirical_probability=child_empirical,
            parent_interval_lower=parent_lower,
            parent_interval_upper=parent_upper,
            child_interval_lower=child_lower,
            child_interval_upper=child_upper,
        )
        if best is None or candidate.lower_bound > best.lower_bound:
            best = candidate

    if best is None:
        raise RuntimeError("P82 nested-contrast family unexpectedly empty")
    return best


def p75_box_nested_projection_contrast_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the strongest standard exact P82 nested-contrast lower bound."""

    return p75_box_nested_projection_contrast_witness_exact(
        empirical_law,
        box,
    ).lower_bound


def p75_box_p82_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the P82 box certificate ``max(P81, exact nested contrast)``."""

    p81 = p75_box_p81_linf_lower_bound_exact(empirical_law, box)
    contrast = p75_box_nested_projection_contrast_linf_lower_bound_exact(
        empirical_law,
        box,
    )
    return max(p81, contrast)


def p82_dominates_p81_on_box(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> bool:
    """Return the exact dominance check P82(B) >= P81(B)."""

    return p75_box_p82_linf_lower_bound_exact(
        empirical_law,
        box,
    ) >= p75_box_p81_linf_lower_bound_exact(empirical_law, box)


def certified_p75_linf_branch_and_bound_contrast(
    counts: tuple[int, ...],
    *,
    max_leaves: int = 256,
    gap_tolerance: Fraction = Fraction(0),
) -> P82DistanceBracket:
    """Return a global P75 distance bracket using exact P82 box lower bounds.

    Active boxes always partition the full P75 parameter cube. P82 lower bounds
    drive refinement. Explicit box centers provide valid global upper bounds.
    As in P80 and P81, the already-proved P78 mesh-width upper certificate is
    retained rather than assuming a new convergence theorem for P82.
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
    root_contrast = p75_box_nested_projection_contrast_linf_lower_bound_exact(
        empirical_law,
        root,
    )
    root_p82 = max(root_p81, root_contrast)
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
        ]
    ] = []
    heappush(
        active,
        (root_p82, serial, root, root_p81, root_p80, root_p78),
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

        _, _, box, _, _, _ = heappop(active)
        if box.width_sum == 0:
            p78_lower = p75_box_linf_lower_bound_exact(empirical_law, box)
            p80_lower = p75_box_simplex_linf_lower_bound_exact(empirical_law, box)
            p81_lower = p75_box_p81_linf_lower_bound_exact(empirical_law, box)
            p82_lower = p75_box_p82_linf_lower_bound_exact(empirical_law, box)
            heappush(
                active,
                (
                    p82_lower,
                    serial,
                    box,
                    p81_lower,
                    p80_lower,
                    p78_lower,
                ),
            )
            break

        left, right = box.split_widest()
        for child in (left, right):
            p78_lower = p75_box_linf_lower_bound_exact(empirical_law, child)
            p80_lower = p75_box_simplex_linf_lower_bound_exact(
                empirical_law,
                child,
            )
            p81_lower = p75_box_p81_linf_lower_bound_exact(empirical_law, child)
            p82_lower = max(
                p81_lower,
                p75_box_nested_projection_contrast_linf_lower_bound_exact(
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
                    p82_lower,
                    serial,
                    child,
                    p81_lower,
                    p80_lower,
                    p78_lower,
                ),
            )
            serial += 1
            evaluated_boxes += 1
        iterations += 1

    global_lower = active[0][0]
    p81_active_lower = min(entry[3] for entry in active)
    p80_active_lower = min(entry[4] for entry in active)
    p78_active_lower = min(entry[5] for entry in active)
    maximum_width_sum = max(entry[2].width_sum for entry in active)
    p78_mesh_upper = p78_active_lower + maximum_width_sum
    certified_upper = min(best_upper, p78_mesh_upper)
    certified_gap = certified_upper - global_lower

    if certified_gap < 0:
        raise RuntimeError("certified upper bound fell below the P82 lower bound")

    if global_lower == certified_upper:
        conclusion = "exact global L-infinity model distance certified"
    elif len(active) >= max_leaves:
        conclusion = (
            "valid P82 global distance bracket; leaf budget exhausted before exact closure"
        )
    else:
        conclusion = "valid P82 global distance bracket; requested gap tolerance reached"

    return P82DistanceBracket(
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
        p78_mesh_upper_bound=p78_mesh_upper,
        certified_gap=certified_gap,
        root_p78_bound=root_p78,
        root_p80_bound=root_p80,
        root_p81_bound=root_p81,
        root_contrast_bound=root_contrast,
        root_p82_bound=root_p82,
        root_tightening_over_p81=root_p82 - root_p81,
        conclusion=conclusion,
    )


def p82_rejection_with_p79_radius(
    bracket: P82DistanceBracket,
    radius: P79SamplingRadiusCertificate,
) -> bool:
    """Apply the strict P77 rejection gate with P82/P79 certified directions."""

    return bracket.lower_bound > radius.cell_linf_radius_upper
