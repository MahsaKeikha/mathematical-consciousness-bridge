"""P83 exact signed cylinder-contrast certificates for continuous P75 separation.

P81 tests each nonempty observed cylinder event separately. P82 strengthens that
record with exact probabilities of nested residual events ``A \\ B``. Both are
one-event certificates: they compare one empirical event probability with one
parameter-box interval at a time.

P83 adds dependency-aware signed contrasts between *non-nested* cylinder events,

    phi_{A,B}(x) = 1_A(x) - 1_B(x).

For every pair of probability laws ``p`` and ``q``,

    |E_p phi - E_q phi| <= ||p-q||_inf * sum_x |phi(x)|.

For two event indicators, the coefficient L1 norm is exactly the cardinality of
the symmetric difference ``|A triangle B|``. Therefore, if the empirical signed
contrast lies outside the exact P75 parameter-box interval ``[L,U]``,

    ||p-q||_inf >= d(E_p phi, [L,U]) / |A triangle B|.

The model-side interval is exact. Inside one latent branch of P75, each cylinder
probability is a product of Bernoulli response factors. Their difference is a
multi-affine function of at most four branch-specific response coordinates, so
its extrema over an axis-aligned rational box occur at the corresponding box
vertices. The minus and plus latent branches use disjoint response coordinates.
After exact branchwise minimization/maximization, prevalence enters affinely, so
its two rational endpoints complete the exact global interval.

The standard P83 family contains every unordered pair of distinct nonempty
cylinders that is non-nested in both directions. There are 2,696 such pairs for
four binary views. Nested pairs are deliberately excluded from the new family:
when one cylinder contains the other, the signed contrast is (up to sign) a
nested residual already covered by P81/P82. The final P83 certificate is

    max(P82 lower bound, strongest non-nested signed-cylinder lower bound).

Hence P83 is never weaker than P82. A clean exact-rational witness has
``P80=P81=P82=0`` while ``P83=5/128``.

The P78 mesh-width upper certificate remains the global branch-and-bound upper
certificate. P83 does not claim a new convergence theorem. This proposition is
a conditional computational theorem for the declared P75 target-measurement
family; it does not validate that family, identify a latent state with
consciousness, or close the physical-to-experiential bridge.
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


def _validate_projection(spec: ProjectionSpec, *, name: str) -> None:
    views, assignment = spec
    if not views:
        raise ValueError(f"{name} must be a nonempty cylinder")
    if len(views) != len(assignment):
        raise ValueError(f"{name} views and assignment must have equal length")
    if tuple(sorted(views)) != views or len(set(views)) != len(views):
        raise ValueError(f"{name} views must be distinct and sorted")
    if any(view < 0 or view >= _VIEW_COUNT for view in views):
        raise ValueError(f"{name} views must lie in range(4)")
    if any(value not in (0, 1) for value in assignment):
        raise ValueError(f"{name} assignment must be binary")


def _projection_map(spec: ProjectionSpec) -> dict[int, int]:
    return dict(zip(spec[0], spec[1], strict=True))


def _is_projection_subset(left: ProjectionSpec, right: ProjectionSpec) -> bool:
    """Return whether cylinder ``left`` is a subset of cylinder ``right``."""

    left_map = _projection_map(left)
    right_map = _projection_map(right)
    return all(left_map.get(view) == observed for view, observed in right_map.items())


def _is_non_nested_pair(left: ProjectionSpec, right: ProjectionSpec) -> bool:
    return not _is_projection_subset(left, right) and not _is_projection_subset(
        right,
        left,
    )


_PROJECTIONS = _projection_specs()
_STANDARD_SIGNED_PAIRS = tuple(
    (_PROJECTIONS[left_index], _PROJECTIONS[right_index])
    for left_index in range(len(_PROJECTIONS))
    for right_index in range(left_index + 1, len(_PROJECTIONS))
    if _is_non_nested_pair(_PROJECTIONS[left_index], _PROJECTIONS[right_index])
)


@dataclass(frozen=True)
class P83SignedContrastWitness:
    """Strongest exact non-nested signed-cylinder witness on one parameter box."""

    lower_bound: Fraction
    positive_views: tuple[int, ...]
    positive_assignment: tuple[int, ...]
    negative_views: tuple[int, ...]
    negative_assignment: tuple[int, ...]
    coefficient_l1_norm: int
    empirical_contrast: Fraction
    interval_lower: Fraction
    interval_upper: Fraction
    minus_branch_lower: Fraction
    minus_branch_upper: Fraction
    plus_branch_lower: Fraction
    plus_branch_upper: Fraction
    positive_empirical_probability: Fraction
    negative_empirical_probability: Fraction
    positive_interval_lower: Fraction
    positive_interval_upper: Fraction
    negative_interval_lower: Fraction
    negative_interval_upper: Fraction


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
    root_signed_contrast_bound: Fraction
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


def _projection_probability_from_values(
    spec: ProjectionSpec,
    response_values: dict[int, Fraction],
) -> Fraction:
    views, assignment = spec
    probability = Fraction(1)
    for view, observed in zip(views, assignment, strict=True):
        response = response_values[view]
        probability *= response if observed else 1 - response
    return probability


def _branch_signed_contrast_interval_exact(
    box: P78ParameterBox,
    positive: ProjectionSpec,
    negative: ProjectionSpec,
    *,
    plus_branch: bool,
) -> tuple[Fraction, Fraction]:
    """Return the exact branchwise range of ``P(A)-P(B)``.

    The signed cylinder contrast is multi-affine in the union of response
    coordinates used by the two cylinders. Exact extrema therefore occur at the
    rational endpoint vertices of those coordinates.
    """

    union_views = tuple(sorted(set(positive[0]) | set(negative[0])))
    branch_offset = 2 if plus_branch else 1
    endpoint_choices: list[tuple[Fraction, ...]] = []
    for view in union_views:
        index = branch_offset + 2 * view
        lower = box.lower[index]
        upper = box.upper[index]
        endpoint_choices.append((lower,) if lower == upper else (lower, upper))

    values: list[Fraction] = []
    for vertex in product(*endpoint_choices):
        response_values = dict(zip(union_views, vertex, strict=True))
        positive_probability = _projection_probability_from_values(
            positive,
            response_values,
        )
        negative_probability = _projection_probability_from_values(
            negative,
            response_values,
        )
        values.append(positive_probability - negative_probability)

    if not values:
        raise RuntimeError("signed contrast vertex family unexpectedly empty")
    return min(values), max(values)


def p83_standard_signed_contrast_count() -> int:
    """Return the number of genuinely new non-nested signed contrasts."""

    return len(_STANDARD_SIGNED_PAIRS)


def p75_signed_cylinder_contrast_interval_exact(
    box: P78ParameterBox,
    positive_views: tuple[int, ...],
    positive_assignment: tuple[int, ...],
    negative_views: tuple[int, ...],
    negative_assignment: tuple[int, ...],
) -> tuple[Fraction, Fraction]:
    """Return the exact P75 box range of ``P(A)-P(B)`` for two cylinders."""

    positive = (positive_views, positive_assignment)
    negative = (negative_views, negative_assignment)
    _validate_projection(positive, name="positive")
    _validate_projection(negative, name="negative")
    if positive == negative:
        raise ValueError("positive and negative cylinders must be distinct")

    minus_lower, minus_upper = _branch_signed_contrast_interval_exact(
        box,
        positive,
        negative,
        plus_branch=False,
    )
    plus_lower, plus_upper = _branch_signed_contrast_interval_exact(
        box,
        positive,
        negative,
        plus_branch=True,
    )

    prevalence_lower = box.lower[0]
    prevalence_upper = box.upper[0]
    lower_candidates = tuple(
        (1 - prevalence) * minus_lower + prevalence * plus_lower
        for prevalence in (prevalence_lower, prevalence_upper)
    )
    upper_candidates = tuple(
        (1 - prevalence) * minus_upper + prevalence * plus_upper
        for prevalence in (prevalence_lower, prevalence_upper)
    )
    return min(lower_candidates), max(upper_candidates)


def empirical_signed_cylinder_contrast_exact(
    empirical_law: tuple[Fraction, ...],
    positive_views: tuple[int, ...],
    positive_assignment: tuple[int, ...],
    negative_views: tuple[int, ...],
    negative_assignment: tuple[int, ...],
) -> Fraction:
    """Return the exact empirical value of ``1_A-1_B``."""

    positive = (positive_views, positive_assignment)
    negative = (negative_views, negative_assignment)
    _validate_projection(positive, name="positive")
    _validate_projection(negative, name="negative")
    if positive == negative:
        raise ValueError("positive and negative cylinders must be distinct")

    positive_mass = empirical_projection_probability_exact(
        empirical_law,
        positive_views,
        positive_assignment,
    )
    negative_mass = empirical_projection_probability_exact(
        empirical_law,
        negative_views,
        negative_assignment,
    )
    return positive_mass - negative_mass


def _projection_intersection_size(
    left: ProjectionSpec,
    right: ProjectionSpec,
) -> int:
    constraints = _projection_map(left)
    for view, observed in _projection_map(right).items():
        if view in constraints and constraints[view] != observed:
            return 0
        constraints[view] = observed
    return 1 << (_VIEW_COUNT - len(constraints))


def signed_cylinder_coefficient_l1_norm(
    positive_views: tuple[int, ...],
    positive_assignment: tuple[int, ...],
    negative_views: tuple[int, ...],
    negative_assignment: tuple[int, ...],
) -> int:
    """Return ``sum_x |1_A(x)-1_B(x)| = |A triangle B|`` exactly."""

    positive = (positive_views, positive_assignment)
    negative = (negative_views, negative_assignment)
    _validate_projection(positive, name="positive")
    _validate_projection(negative, name="negative")
    if positive == negative:
        return 0

    positive_size = 1 << (_VIEW_COUNT - len(positive_views))
    negative_size = 1 << (_VIEW_COUNT - len(negative_views))
    intersection_size = _projection_intersection_size(positive, negative)
    return positive_size + negative_size - 2 * intersection_size


def p75_box_signed_cylinder_contrast_witness_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> P83SignedContrastWitness:
    """Return the strongest exact standard P83 signed-cylinder witness."""

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

    best: P83SignedContrastWitness | None = None
    for positive, negative in _STANDARD_SIGNED_PAIRS:
        positive_views, positive_assignment = positive
        negative_views, negative_assignment = negative
        empirical_contrast = empirical_by_projection[positive] - empirical_by_projection[
            negative
        ]
        interval_lower, interval_upper = p75_signed_cylinder_contrast_interval_exact(
            box,
            positive_views,
            positive_assignment,
            negative_views,
            negative_assignment,
        )
        coefficient_l1_norm = signed_cylinder_coefficient_l1_norm(
            positive_views,
            positive_assignment,
            negative_views,
            negative_assignment,
        )
        if coefficient_l1_norm <= 0:
            raise RuntimeError("non-nested signed contrast must have positive L1 norm")

        lower_bound = _distance_to_interval(
            empirical_contrast,
            interval_lower,
            interval_upper,
        ) / coefficient_l1_norm

        minus_lower, minus_upper = _branch_signed_contrast_interval_exact(
            box,
            positive,
            negative,
            plus_branch=False,
        )
        plus_lower, plus_upper = _branch_signed_contrast_interval_exact(
            box,
            positive,
            negative,
            plus_branch=True,
        )
        positive_interval = interval_by_projection[positive]
        negative_interval = interval_by_projection[negative]
        candidate = P83SignedContrastWitness(
            lower_bound=lower_bound,
            positive_views=positive_views,
            positive_assignment=positive_assignment,
            negative_views=negative_views,
            negative_assignment=negative_assignment,
            coefficient_l1_norm=coefficient_l1_norm,
            empirical_contrast=empirical_contrast,
            interval_lower=interval_lower,
            interval_upper=interval_upper,
            minus_branch_lower=minus_lower,
            minus_branch_upper=minus_upper,
            plus_branch_lower=plus_lower,
            plus_branch_upper=plus_upper,
            positive_empirical_probability=empirical_by_projection[positive],
            negative_empirical_probability=empirical_by_projection[negative],
            positive_interval_lower=positive_interval[0],
            positive_interval_upper=positive_interval[1],
            negative_interval_lower=negative_interval[0],
            negative_interval_upper=negative_interval[1],
        )
        if best is None or candidate.lower_bound > best.lower_bound:
            best = candidate

    if best is None:
        raise RuntimeError("P83 signed-contrast family unexpectedly empty")
    return best


def p75_box_signed_cylinder_contrast_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the strongest exact standard P83 signed-cylinder lower bound."""

    return p75_box_signed_cylinder_contrast_witness_exact(
        empirical_law,
        box,
    ).lower_bound


def p75_box_p83_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return ``max(P82, strongest non-nested signed-cylinder certificate)``."""

    p82 = p75_box_p82_linf_lower_bound_exact(empirical_law, box)
    signed = p75_box_signed_cylinder_contrast_linf_lower_bound_exact(
        empirical_law,
        box,
    )
    return max(p82, signed)


def p83_dominates_p82_on_box(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> bool:
    """Return the exact dominance check ``P83(B) >= P82(B)``."""

    return p75_box_p83_linf_lower_bound_exact(
        empirical_law,
        box,
    ) >= p75_box_p82_linf_lower_bound_exact(empirical_law, box)


def certified_p75_linf_branch_and_bound_signed_contrast(
    counts: tuple[int, ...],
    *,
    max_leaves: int = 256,
    gap_tolerance: Fraction = Fraction(0),
) -> P83DistanceBracket:
    """Return a global P75 distance bracket using exact P83 box lower bounds.

    P83 lower bounds drive refinement. Explicit box centers remain valid global
    upper witnesses. The already-proved P78 mesh-width upper certificate is
    retained; no new P83 convergence theorem is assumed.
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
    root_signed = p75_box_signed_cylinder_contrast_linf_lower_bound_exact(
        empirical_law,
        root,
    )
    root_p83 = max(root_p82, root_signed)
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
        (
            root_p83,
            serial,
            root,
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
            p80_lower = p75_box_simplex_linf_lower_bound_exact(
                empirical_law,
                child,
            )
            p81_lower = p75_box_p81_linf_lower_bound_exact(empirical_law, child)
            p82_lower = p75_box_p82_linf_lower_bound_exact(empirical_law, child)
            signed_lower = p75_box_signed_cylinder_contrast_linf_lower_bound_exact(
                empirical_law,
                child,
            )
            p83_lower = max(p82_lower, signed_lower)
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
        root_signed_contrast_bound=root_signed,
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
