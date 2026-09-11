"""P78 certified continuous separation for the P75 four-view latent model.

P77 requires a mathematically sound *lower* bound on distance from an empirical
law to the complete declared model set before a full-law rejection can be
certified. A local numerical best fit is an upper bound on that distance and is
not enough.

P78 exploits the special structure of the P75 four-view binary latent model.
Its sixteen observed cell probabilities are multi-affine functions of nine
parameters: one latent prevalence and two conditional probabilities for each of
four binary views. On any axis-aligned parameter box, each component therefore
has exact coordinatewise extrema that can be computed from the box endpoints.
These enclosures give a rigorous lower bound on L-infinity distance to every
model law generated inside the box.

A finite box partition of the full parameter cube gives a certified global
lower bound by taking the minimum box lower bound. Any explicit parameter
vector gives an upper bound. The implementation uses exact ``Fraction`` arithmetic
for empirical count laws and dyadic branch points, so the returned optimization
bracket is algebraic rather than a floating-point optimizer claim.

This module does not identify the latent state with consciousness, does not
validate the target-measurement model when the lower bound is small, and does
not solve the physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from heapq import heappop, heappush
from itertools import product

_PARAMETER_DIMENSION = 9
_OUTCOME_DIMENSION = 16
_PATTERNS = tuple(product((0, 1), repeat=4))


@dataclass(frozen=True)
class P78ParameterBox:
    """Axis-aligned box in the nine-dimensional P75 parameter cube."""

    lower: tuple[Fraction, ...]
    upper: tuple[Fraction, ...]

    def __post_init__(self) -> None:
        if len(self.lower) != _PARAMETER_DIMENSION or len(self.upper) != _PARAMETER_DIMENSION:
            raise ValueError("P75 parameter boxes must have exactly nine coordinates")
        for lower, upper in zip(self.lower, self.upper, strict=True):
            if lower < 0 or upper > 1 or lower > upper:
                raise ValueError("parameter-box coordinates must satisfy 0 <= lower <= upper <= 1")

    @classmethod
    def unit_cube(cls) -> P78ParameterBox:
        """Return the full admissible P75 parameter cube [0,1]^9."""

        return cls(
            lower=(Fraction(0),) * _PARAMETER_DIMENSION,
            upper=(Fraction(1),) * _PARAMETER_DIMENSION,
        )

    @property
    def width_sum(self) -> Fraction:
        """Return the L1 diameter bound obtained by summing side widths."""

        return sum(
            (upper - lower for lower, upper in zip(self.lower, self.upper, strict=True)),
            start=Fraction(0),
        )

    @property
    def center(self) -> tuple[Fraction, ...]:
        """Return the exact dyadic center of the box."""

        return tuple(
            (lower + upper) / 2
            for lower, upper in zip(self.lower, self.upper, strict=True)
        )

    def split_widest(self) -> tuple[P78ParameterBox, P78ParameterBox]:
        """Bisect the widest coordinate, breaking ties by coordinate order."""

        widths = tuple(
            upper - lower
            for lower, upper in zip(self.lower, self.upper, strict=True)
        )
        index = max(range(_PARAMETER_DIMENSION), key=widths.__getitem__)
        if widths[index] == 0:
            raise ValueError("cannot split a zero-width parameter box")

        midpoint = (self.lower[index] + self.upper[index]) / 2
        left_upper = list(self.upper)
        right_lower = list(self.lower)
        left_upper[index] = midpoint
        right_lower[index] = midpoint
        return (
            P78ParameterBox(self.lower, tuple(left_upper)),
            P78ParameterBox(tuple(right_lower), self.upper),
        )


@dataclass(frozen=True)
class P78DistanceBracket:
    """Certified global L-infinity distance bracket for the continuous P75 model."""

    lower_bound: Fraction
    upper_bound: Fraction
    best_parameters: tuple[Fraction, ...]
    leaf_count: int
    evaluated_boxes: int
    iterations: int
    maximum_active_width_sum: Fraction
    mesh_upper_bound: Fraction
    certified_gap: Fraction
    conclusion: str


@dataclass(frozen=True)
class _BoxEvaluation:
    lower_bound: Fraction
    upper_bound: Fraction
    best_parameters: tuple[Fraction, ...]


def _validate_fraction_probability(value: Fraction, *, name: str) -> Fraction:
    if not isinstance(value, Fraction):
        raise TypeError(f"{name} must be a fractions.Fraction")
    if value < 0 or value > 1:
        raise ValueError(f"{name} must lie in [0, 1]")
    return value


def empirical_law_from_counts(counts: tuple[int, ...]) -> tuple[Fraction, ...]:
    """Return the exact sixteen-cell empirical law from nonnegative counts."""

    if len(counts) != _OUTCOME_DIMENSION:
        raise ValueError("exactly sixteen cell counts are required")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in counts):
        raise TypeError("cell counts must be integers")
    if any(value < 0 for value in counts):
        raise ValueError("cell counts must be nonnegative")
    total = sum(counts)
    if total <= 0:
        raise ValueError("cell counts must have positive total mass")
    return tuple(Fraction(value, total) for value in counts)


def p75_four_view_law_exact(
    parameters: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    """Evaluate the P75 four-view latent model exactly in rational arithmetic.

    Parameter order is

    ``(pi_plus, q1_minus, q1_plus, q2_minus, q2_plus, ..., q4_minus, q4_plus)``,

    where ``qj_s`` is the probability that view ``j`` equals one conditional on
    latent state ``s``.
    """

    if len(parameters) != _PARAMETER_DIMENSION:
        raise ValueError("exactly nine P75 model parameters are required")
    for index, value in enumerate(parameters):
        _validate_fraction_probability(value, name=f"parameter[{index}]")

    prevalence_plus = parameters[0]
    law = []
    for pattern in _PATTERNS:
        minus_product = Fraction(1)
        plus_product = Fraction(1)
        for view, observed in enumerate(pattern):
            q_minus = parameters[1 + 2 * view]
            q_plus = parameters[2 + 2 * view]
            minus_product *= q_minus if observed else 1 - q_minus
            plus_product *= q_plus if observed else 1 - q_plus
        law.append(
            (1 - prevalence_plus) * minus_product
            + prevalence_plus * plus_product
        )
    return tuple(law)


def p75_box_cell_intervals_exact(
    box: P78ParameterBox,
) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    """Return exact coordinatewise cell ranges over one parameter box.

    Each cell probability has the form

    ``(1-pi) A(theta_minus) + pi B(theta_plus)``,

    where ``A`` and ``B`` are products of four independent factors in [0,1].
    For a fixed observed pattern, the exact range of each factor is obtained at
    an endpoint, the product extrema are therefore endpoint products, and the
    remaining affine dependence on ``pi`` is extremized at a prevalence
    endpoint. This is equivalent to the standard multi-affine vertex-extremum
    property but avoids enumerating all 2^9 parameter vertices.
    """

    prevalence_lower = box.lower[0]
    prevalence_upper = box.upper[0]
    cell_lower = []
    cell_upper = []

    for pattern in _PATTERNS:
        minus_min = Fraction(1)
        minus_max = Fraction(1)
        plus_min = Fraction(1)
        plus_max = Fraction(1)

        for view, observed in enumerate(pattern):
            minus_lower = box.lower[1 + 2 * view]
            minus_upper = box.upper[1 + 2 * view]
            plus_lower = box.lower[2 + 2 * view]
            plus_upper = box.upper[2 + 2 * view]

            if observed:
                minus_factor_min, minus_factor_max = minus_lower, minus_upper
                plus_factor_min, plus_factor_max = plus_lower, plus_upper
            else:
                minus_factor_min, minus_factor_max = 1 - minus_upper, 1 - minus_lower
                plus_factor_min, plus_factor_max = 1 - plus_upper, 1 - plus_lower

            minus_min *= minus_factor_min
            minus_max *= minus_factor_max
            plus_min *= plus_factor_min
            plus_max *= plus_factor_max

        minimum_at_prevalence_endpoints = (
            (1 - prevalence_lower) * minus_min + prevalence_lower * plus_min,
            (1 - prevalence_upper) * minus_min + prevalence_upper * plus_min,
        )
        maximum_at_prevalence_endpoints = (
            (1 - prevalence_lower) * minus_max + prevalence_lower * plus_max,
            (1 - prevalence_upper) * minus_max + prevalence_upper * plus_max,
        )
        cell_lower.append(min(minimum_at_prevalence_endpoints))
        cell_upper.append(max(maximum_at_prevalence_endpoints))

    return tuple(cell_lower), tuple(cell_upper)


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


def linf_distance_exact(
    first: tuple[Fraction, ...],
    second: tuple[Fraction, ...],
) -> Fraction:
    """Return exact L-infinity distance between two equal-length rational vectors."""

    if len(first) != len(second) or not first:
        raise ValueError("vectors must be nonempty and have equal length")
    return max(abs(left - right) for left, right in zip(first, second, strict=True))


def p75_box_linf_lower_bound_exact(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> Fraction:
    """Return a certified lower bound over all model laws generated in ``box``."""

    if len(empirical_law) != _OUTCOME_DIMENSION:
        raise ValueError("empirical_law must contain sixteen probabilities")
    cell_lower, cell_upper = p75_box_cell_intervals_exact(box)
    return max(
        _distance_to_interval(observed, lower, upper)
        for observed, lower, upper in zip(
            empirical_law,
            cell_lower,
            cell_upper,
            strict=True,
        )
    )


def _evaluate_box(
    empirical_law: tuple[Fraction, ...],
    box: P78ParameterBox,
) -> _BoxEvaluation:
    lower_bound = p75_box_linf_lower_bound_exact(empirical_law, box)
    center = box.center
    center_law = p75_four_view_law_exact(center)
    upper_bound = linf_distance_exact(empirical_law, center_law)
    return _BoxEvaluation(lower_bound, upper_bound, center)


def certified_p75_linf_branch_and_bound(
    counts: tuple[int, ...],
    *,
    max_leaves: int = 256,
    gap_tolerance: Fraction = Fraction(0),
) -> P78DistanceBracket:
    """Return a certified global distance bracket for the continuous P75 model.

    The active boxes always form a partition of ``[0,1]^9``. For each box ``B``,
    ``L(B)`` is a rigorous lower bound on the distance to every model law inside
    that box. Therefore

    ``min_B L(B) <= d_inf(P_hat, M_P75)``.

    Every evaluated box center is an admissible parameter vector and therefore
    supplies an upper bound. The routine always bisects an active box with the
    smallest current lower bound. It may stop because the requested leaf budget
    is exhausted or because the explicit upper-lower gap reaches
    ``gap_tolerance``.

    The returned bracket is valid at every finite iteration. It is an
    optimization certificate only; P77 statistical rejection additionally
    requires comparing its lower bound with a valid sampling-radius upper bound.
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
    root_evaluation = _evaluate_box(empirical_law, root)

    serial = 0
    active: list[tuple[Fraction, int, P78ParameterBox]] = []
    heappush(active, (root_evaluation.lower_bound, serial, root))
    serial += 1

    best_upper = root_evaluation.upper_bound
    best_parameters = root_evaluation.best_parameters
    evaluated_boxes = 1
    iterations = 0

    while len(active) < max_leaves:
        global_lower = active[0][0]
        if best_upper - global_lower <= gap_tolerance:
            break

        lower_bound, _, box = heappop(active)
        del lower_bound
        if box.width_sum == 0:
            heappush(active, (global_lower, serial, box))
            break

        left, right = box.split_widest()
        for child in (left, right):
            evaluation = _evaluate_box(empirical_law, child)
            evaluated_boxes += 1
            if evaluation.upper_bound < best_upper:
                best_upper = evaluation.upper_bound
                best_parameters = evaluation.best_parameters
            heappush(active, (evaluation.lower_bound, serial, child))
            serial += 1
        iterations += 1

    global_lower = active[0][0]
    maximum_width_sum = max(box.width_sum for _, _, box in active)
    mesh_upper = global_lower + maximum_width_sum
    certified_upper = min(best_upper, mesh_upper)
    certified_gap = certified_upper - global_lower

    if global_lower == certified_upper:
        conclusion = "exact global L-infinity model distance certified"
    elif len(active) >= max_leaves:
        conclusion = "valid global distance bracket; leaf budget exhausted before exact closure"
    else:
        conclusion = "valid global distance bracket; requested gap tolerance reached"

    return P78DistanceBracket(
        lower_bound=global_lower,
        upper_bound=certified_upper,
        best_parameters=best_parameters,
        leaf_count=len(active),
        evaluated_boxes=evaluated_boxes,
        iterations=iterations,
        maximum_active_width_sum=maximum_width_sum,
        mesh_upper_bound=mesh_upper,
        certified_gap=certified_gap,
        conclusion=conclusion,
    )


def p77_rejection_from_certified_radius(
    bracket: P78DistanceBracket,
    *,
    sampling_radius_upper: Fraction,
) -> bool:
    """Return whether P78 certifies the strict P77 separation inequality.

    ``sampling_radius_upper`` must itself be a mathematically valid upper bound
    on the P77 sampling radius. Passing an ordinary floating approximation as a
    rational value does not make that approximation certified.
    """

    if not isinstance(sampling_radius_upper, Fraction):
        raise TypeError("sampling_radius_upper must be a fractions.Fraction")
    if sampling_radius_upper < 0:
        raise ValueError("sampling_radius_upper must be nonnegative")
    return bracket.lower_bound > sampling_radius_upper
