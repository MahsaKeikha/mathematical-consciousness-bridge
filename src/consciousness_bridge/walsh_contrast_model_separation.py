"""P84 exact pairwise Walsh-contrast certificates for continuous P75 separation.

P83 certifies every two-, three-, and four-view parity observable separately.
Separate exact intervals can still discard parameter dependence shared by two
parity characters. P84 retains the complete P83 certificate and adds a finite,
predeclared family of signed pairwise Walsh contrasts.

For a nonempty view set J define the Walsh character

    chi_J(x) = (-1) ** sum_{j in J} x_j.

For two distinct nonempty view sets A and B and sign s in {-1,+1}, define

    phi_(A,B,s)(x) = chi_A(x) + s chi_B(x).

Inside one latent branch t of P75, conditional independence gives

    E_t[chi_J(X)] = product_{j in J} (1 - 2 q_{j,t}),

and therefore

    E_t[phi_(A,B,s)(X)]
      = product_{j in A} (1 - 2 q_{j,t})
        + s product_{j in B} (1 - 2 q_{j,t}).

This expression is multi-affine in the branch response coordinates. Hence its
minimum and maximum over an axis-aligned rational parameter box occur at
endpoint vertices. The two latent branches use disjoint response coordinates,
and the final mixture is affine in prevalence, so the full P75 box interval is
exact, not merely an enclosure.

If ||p-q||_inf <= r, then for every real observable phi on the sixteen cells,

    |E_p[phi] - E_q[phi]| <= r * sum_x |phi(x)|.

Thus separation of the empirical contrast expectation from its exact P75 box
interval, divided by the discrete L1 norm of the contrast, is a sound full-law
L-infinity lower bound.

There are fifteen nonconstant Walsh characters on four binary views. P84 uses
both signs for every unordered pair, giving

    2 * C(15,2) = 210

predeclared signed pairwise contrasts. The final P84 box certificate is

    max(P83 lower bound, exact Walsh-contrast lower bound),

so it is never weaker than P83.

A strict exact-rational witness fixes views 2 and 3 to Bernoulli(1/4) in both
latent branches, fixes view 4 to Bernoulli(1/2), and lets the view-1 response
probabilities vary independently in [3/8,5/8]. The P75 family then forces

    E[chi_{1,2} - chi_{1,3}] = 0

throughout the box because views 2 and 3 have the same branchwise bias. An
explicit empirical law keeps every P82 nested-residual and every P83 parity
certificate at zero while setting the contrast expectation to 3/16. Since the
contrast L1 norm is 16, P84 certifies 3/256 on that box.

The P78 mesh-width upper certificate is retained unchanged for global
branch-and-bound. P84 does not claim a new convergence theorem. This
certificate does not validate the P75 model, does not identify a latent state
with consciousness, and does not close the physical-to-experiential bridge.
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
WalshCharacter = tuple[int, ...]
WalshContrastSpec = tuple[WalshCharacter, WalshCharacter, int]


def _walsh_characters() -> tuple[WalshCharacter, ...]:
    return tuple(
        views
        for size in range(1, _VIEW_COUNT + 1)
        for views in combinations(range(_VIEW_COUNT), size)
    )


_WALSH_CHARACTERS = _walsh_characters()
_STANDARD_CONTRAST_SPECS = tuple(
    (left, right, sign)
    for left, right in combinations(_WALSH_CHARACTERS, 2)
    for sign in (-1, 1)
)


@dataclass(frozen=True)
class P84WalshContrastWitness:
    """Strongest exact signed Walsh-contrast witness on one P75 box."""

    lower_bound: Fraction
    left_views: WalshCharacter
    right_views: WalshCharacter
    right_sign: int
    l1_norm: int
    empirical_expectation: Fraction
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
    root_walsh_contrast_bound: Fraction
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


def _validate_character(views: WalshCharacter) -> None:
    if not views or len(views) > _VIEW_COUNT:
        raise ValueError("Walsh characters must use between one and four views")
    if tuple(sorted(set(views))) != views:
        raise ValueError("views must be a strictly increasing tuple of distinct indices")
    if any(view < 0 or view >= _VIEW_COUNT for view in views):
        raise ValueError("view indices must lie in {0,1,2,3}")


def _validate_contrast_spec(
    left_views: WalshCharacter,
    right_views: WalshCharacter,
    right_sign: int,
) -> None:
    _validate_character(left_views)
    _validate_character(right_views)
    if left_views == right_views:
        raise ValueError("Walsh contrast characters must be distinct")
    if (
        isinstance(right_sign, bool)
        or not isinstance(right_sign, int)
        or right_sign not in (-1, 1)
    ):
        raise ValueError("right_sign must be the integer -1 or +1")


def p84_standard_walsh_character_count() -> int:
    """Return the number of nonconstant Walsh characters on four views."""

    return len(_WALSH_CHARACTERS)


def p84_standard_contrast_count() -> int:
    """Return the number of predeclared signed pairwise Walsh contrasts."""

    return len(_STANDARD_CONTRAST_SPECS)


def _walsh_value(outcome: tuple[int, ...], views: WalshCharacter) -> int:
    return 1 if sum(outcome[view] for view in views) % 2 == 0 else -1


def walsh_contrast_l1_norm(
    left_views: WalshCharacter,
    right_views: WalshCharacter,
    right_sign: int,
) -> int:
    """Return ``sum_x |chi_A(x) + s chi_B(x)|`` over all sixteen cells."""

    _validate_contrast_spec(left_views, right_views, right_sign)
    return sum(
        abs(
            _walsh_value(outcome, left_views)
            + right_sign * _walsh_value(outcome, right_views)
        )
        for outcome in product((0, 1), repeat=_VIEW_COUNT)
    )


def empirical_walsh_character_expectation_exact(
    empirical_law: tuple[Fraction, ...],
    views: WalshCharacter,
) -> Fraction:
    """Return the exact empirical Walsh-character expectation."""

    _validate_character(views)
    if len(empirical_law) != 1 << _VIEW_COUNT:
        raise ValueError("empirical law must contain sixteen observed-cell masses")
    return sum(
        mass * _walsh_value(outcome, views)
        for outcome, mass in zip(
            product((0, 1), repeat=_VIEW_COUNT),
            empirical_law,
            strict=True,
        )
    )


def empirical_walsh_contrast_expectation_exact(
    empirical_law: tuple[Fraction, ...],
    left_views: WalshCharacter,
    right_views: WalshCharacter,
    right_sign: int,
) -> Fraction:
    """Return the exact empirical expectation of one signed Walsh contrast."""

    _validate_contrast_spec(left_views, right_views, right_sign)
    return empirical_walsh_character_expectation_exact(
        empirical_law,
        left_views,
    ) + right_sign * empirical_walsh_character_expectation_exact(
        empirical_law,
        right_views,
    )


def _branch_walsh_contrast_interval_exact(
    box: P78ParameterBox,
    left_views: WalshCharacter,
    right_views: WalshCharacter,
    right_sign: int,
    *,
    plus_branch: bool,
) -> tuple[Fraction, Fraction]:
    """Return the exact branchwise expectation range of one Walsh contrast."""

    _validate_contrast_spec(left_views, right_views, right_sign)
    active_views = tuple(sorted(set(left_views) | set(right_views)))
    branch_offset = 2 if plus_branch else 1
    bias_endpoints: list[tuple[Fraction, Fraction]] = []
    for view in active_views:
        index = branch_offset + 2 * view
        q_lower = box.lower[index]
        q_upper = box.upper[index]
        bias_endpoints.append((1 - 2 * q_upper, 1 - 2 * q_lower))

    values: list[Fraction] = []
    for endpoint_choice in product(*bias_endpoints):
        bias = dict(zip(active_views, endpoint_choice, strict=True))
        left = Fraction(1)
        for view in left_views:
            left *= bias[view]
        right = Fraction(1)
        for view in right_views:
            right *= bias[view]
        values.append(left + right_sign * right)
    return min(values), max(values)


def p75_walsh_contrast_interval_exact(
    box: P78ParameterBox,
    left_views: WalshCharacter,
    right_views: WalshCharacter,
    right_sign: int,
) -> tuple[Fraction, Fraction]:
    """Return the exact P75 parameter-box range of one Walsh contrast."""

    _validate_contrast_spec(left_views, right_views, right_sign)
    minus_lower, minus_upper = _branch_walsh_contrast_interval_exact(
        box,
        left_views,
        right_views,
        right_sign,
        plus_branch=False,
    )
    plus_lower, plus_upper = _branch_walsh_contrast_interval_exact(
        box,
        left_views,
        right_views,
        right_sign,
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


def p75_box_walsh_contrast_witness_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> P84WalshContrastWitness:
    """Return the strongest standard exact P84 Walsh-contrast witness."""

    empirical_characters = {
        views: empirical_walsh_character_expectation_exact(empirical_law, views)
        for views in _WALSH_CHARACTERS
    }
    best: P84WalshContrastWitness | None = None
    for left_views, right_views, right_sign in _STANDARD_CONTRAST_SPECS:
        empirical_expectation = (
            empirical_characters[left_views]
            + right_sign * empirical_characters[right_views]
        )
        interval_lower, interval_upper = p75_walsh_contrast_interval_exact(
            box,
            left_views,
            right_views,
            right_sign,
        )
        minus_lower, minus_upper = _branch_walsh_contrast_interval_exact(
            box,
            left_views,
            right_views,
            right_sign,
            plus_branch=False,
        )
        plus_lower, plus_upper = _branch_walsh_contrast_interval_exact(
            box,
            left_views,
            right_views,
            right_sign,
            plus_branch=True,
        )
        l1_norm = walsh_contrast_l1_norm(
            left_views,
            right_views,
            right_sign,
        )
        if l1_norm <= 0:
            raise RuntimeError("nontrivial Walsh contrast unexpectedly has zero L1 norm")
        lower_bound = (
            _distance_to_interval(
                empirical_expectation,
                interval_lower,
                interval_upper,
            )
            / l1_norm
        )
        candidate = P84WalshContrastWitness(
            lower_bound=lower_bound,
            left_views=left_views,
            right_views=right_views,
            right_sign=right_sign,
            l1_norm=l1_norm,
            empirical_expectation=empirical_expectation,
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
        raise RuntimeError("P84 Walsh-contrast family unexpectedly empty")
    return best


def p75_box_walsh_contrast_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the strongest standard exact P84 Walsh-contrast lower bound."""

    return p75_box_walsh_contrast_witness_exact(empirical_law, box).lower_bound


def p75_box_p84_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return the P84 box certificate ``max(P83, exact Walsh contrast)``."""

    p83 = p75_box_p83_linf_lower_bound_exact(empirical_law, box)
    walsh = p75_box_walsh_contrast_linf_lower_bound_exact(empirical_law, box)
    return max(p83, walsh)


def p84_dominates_p83_on_box(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> bool:
    """Return the exact dominance check P84(B) >= P83(B)."""

    return p75_box_p84_linf_lower_bound_exact(
        empirical_law,
        box,
    ) >= p75_box_p83_linf_lower_bound_exact(empirical_law, box)


def certified_p75_linf_branch_and_bound_walsh(
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
    root_walsh = p75_box_walsh_contrast_linf_lower_bound_exact(empirical_law, root)
    root_p84 = max(root_p83, root_walsh)
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
                p75_box_walsh_contrast_linf_lower_bound_exact(
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
        root_walsh_contrast_bound=root_walsh,
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
