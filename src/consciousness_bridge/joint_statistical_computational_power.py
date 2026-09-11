"""P79 joint statistical-computational power for P77-P78 full-law rejection.

P77 controls finite-sample Type I error through a simultaneous empirical-law
radius. P78 controls deterministic optimization error through a certified
lower-bound gap. P79 keeps those two error sources separate and asks a planning
question: how much population model separation is sufficient to achieve a
declared rejection level and a declared power level when optimization remains
approximate but certified?

For a finite alphabet of size K, let

    eps_alpha = sqrt(log(2 K / alpha) / (2 n))
    eps_beta  = sqrt(log(2 K / beta) / (2 n)).

If the true population law is separated from the declared model set by at least
Delta_0 in L-infinity distance and a P78 lower bound is at most eta below the
exact empirical model distance, then

    Delta_0 > eps_alpha + eps_beta + eta

is sufficient for the P77 rejection rule to have power at least 1-beta while
retaining the P77 Type I guarantee alpha.

The concentration inequality and global-optimization bound logic are standard.
The repository-specific role of P79 is their explicit assembly into a joint
sample-size and certified-computation budget for the P77-P78 interface.

A planning margin Delta_0 must be prespecified or justified independently of
the test data if it is used as a guaranteed population-separation lower bound.
The numerical Hoeffding helper below is a planning calculation, not a formal
floating-point proof. Formal handoff uses externally certified radius upper
bounds and exact ``Fraction`` comparisons.

P79 does not validate the P75 target-measurement model when rejection fails,
does not identify any latent state with consciousness, and does not solve the
physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import floor, log, sqrt

from .full_law_model_set_separation import finite_alphabet_cell_linf_radius


@dataclass(frozen=True)
class P79ThreeWayDecision:
    """Certified empirical decision from a P78 distance bracket and P77 radius."""

    distance_lower_bound: Fraction
    candidate_distance_upper_bound: Fraction
    rejection_radius_upper: Fraction
    status: str
    conclusion: str


@dataclass(frozen=True)
class P79PowerMarginCertificate:
    """Exact sufficient power-margin certificate from certified upper bounds."""

    population_separation_lower: Fraction
    rejection_radius_upper: Fraction
    alternative_radius_upper: Fraction
    optimization_gap_upper: Fraction
    required_separation: Fraction
    slack: Fraction
    certified: bool
    conclusion: str


@dataclass(frozen=True)
class P79NumericalPowerPlan:
    """Numerical planning summary for the Hoeffding specialization."""

    sample_size: int
    alphabet_size: int
    alpha: float
    beta: float
    population_separation_margin: float
    optimization_gap_upper: float
    rejection_radius: float
    alternative_radius: float
    required_separation: float
    power_lower_bound: float


def _validate_fraction_nonnegative(value: Fraction, *, name: str) -> Fraction:
    if not isinstance(value, Fraction):
        raise TypeError(f"{name} must be a fractions.Fraction")
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")
    return value


def certified_three_way_full_law_decision(
    *,
    distance_lower_bound: Fraction,
    candidate_distance_upper_bound: Fraction,
    rejection_radius_upper: Fraction,
) -> P79ThreeWayDecision:
    """Return reject, overlap-witness, or unresolved from certified quantities.

    ``distance_lower_bound`` must not exceed the exact empirical distance to the
    model set. ``candidate_distance_upper_bound`` must come from an admissible
    model candidate, so it is an upper bound on that distance. The radius must
    be a mathematically valid upper bound on the P77 rejection radius.

    Strict lower-bound separation certifies rejection. A candidate inside the
    closed confidence ball certifies overlap. The remaining case is unresolved
    at the current optimization precision and should not be converted into a
    model-acceptance statement.
    """

    lower = _validate_fraction_nonnegative(
        distance_lower_bound,
        name="distance_lower_bound",
    )
    upper = _validate_fraction_nonnegative(
        candidate_distance_upper_bound,
        name="candidate_distance_upper_bound",
    )
    radius = _validate_fraction_nonnegative(
        rejection_radius_upper,
        name="rejection_radius_upper",
    )
    if lower > upper:
        raise ValueError("distance_lower_bound cannot exceed candidate_distance_upper_bound")

    if lower > radius:
        status = "reject"
        conclusion = "certified P77 rejection: the global distance lower bound exceeds the radius"
    elif upper <= radius:
        status = "overlap_witness"
        conclusion = "explicit admissible model candidate lies inside the closed P77 confidence ball"
    else:
        status = "unresolved"
        conclusion = (
            "current certified bracket straddles the P77 radius; refine optimization or collect data"
        )

    return P79ThreeWayDecision(
        distance_lower_bound=lower,
        candidate_distance_upper_bound=upper,
        rejection_radius_upper=radius,
        status=status,
        conclusion=conclusion,
    )


def certified_joint_power_margin(
    *,
    population_separation_lower: Fraction,
    rejection_radius_upper: Fraction,
    alternative_radius_upper: Fraction,
    optimization_gap_upper: Fraction,
) -> P79PowerMarginCertificate:
    """Certify the sufficient P79 population-separation inequality exactly.

    The theorem requires

        Delta_0 > eps_alpha + eps_beta + eta.

    The two radius arguments and the optimization-gap argument must already be
    rigorous upper bounds. This function performs only the exact final
    comparison and does not manufacture rigor from floating approximations.
    """

    separation = _validate_fraction_nonnegative(
        population_separation_lower,
        name="population_separation_lower",
    )
    rejection_radius = _validate_fraction_nonnegative(
        rejection_radius_upper,
        name="rejection_radius_upper",
    )
    alternative_radius = _validate_fraction_nonnegative(
        alternative_radius_upper,
        name="alternative_radius_upper",
    )
    optimization_gap = _validate_fraction_nonnegative(
        optimization_gap_upper,
        name="optimization_gap_upper",
    )

    required = rejection_radius + alternative_radius + optimization_gap
    slack = separation - required
    certified = slack > 0
    if certified:
        conclusion = (
            "joint statistical-computational margin is sufficient for the declared power guarantee"
        )
    else:
        conclusion = (
            "sufficient P79 margin is not certified; this does not prove low power or model adequacy"
        )

    return P79PowerMarginCertificate(
        population_separation_lower=separation,
        rejection_radius_upper=rejection_radius,
        alternative_radius_upper=alternative_radius,
        optimization_gap_upper=optimization_gap,
        required_separation=required,
        slack=slack,
        certified=certified,
        conclusion=conclusion,
    )


def joint_linf_required_population_separation(
    *,
    sample_size: int,
    alphabet_size: int,
    alpha: float,
    beta: float,
    optimization_gap_upper: float = 0.0,
) -> float:
    """Return the numerical P79 separation threshold eps_alpha+eps_beta+eta."""

    gap = float(optimization_gap_upper)
    if not 0.0 <= gap <= 1.0:
        raise ValueError("optimization_gap_upper must lie in [0, 1]")
    if not 0.0 < beta < 1.0:
        raise ValueError("beta must lie strictly between zero and one")

    rejection_radius = finite_alphabet_cell_linf_radius(
        sample_size,
        alphabet_size,
        alpha,
    )
    alternative_radius = finite_alphabet_cell_linf_radius(
        sample_size,
        alphabet_size,
        beta,
    )
    return rejection_radius + alternative_radius + gap


def sufficient_joint_linf_sample_size(
    *,
    population_separation_margin: float,
    alphabet_size: int,
    alpha: float = 0.05,
    beta: float = 0.20,
    optimization_gap_upper: float = 0.0,
) -> int:
    """Return the smallest integer n satisfying the numerical P79 inequality.

    This is a planning helper based on ordinary floating-point evaluation of
    logarithms and square roots. It is not a substitute for the exact final
    certificate when a formal rejection or power claim is required.
    """

    separation = float(population_separation_margin)
    gap = float(optimization_gap_upper)
    if not 0.0 < separation <= 1.0:
        raise ValueError("population_separation_margin must lie in (0, 1]")
    if not 0.0 <= gap < separation:
        raise ValueError(
            "optimization_gap_upper must be nonnegative and smaller than the population margin"
        )
    if isinstance(alphabet_size, bool) or int(alphabet_size) != alphabet_size:
        raise ValueError("alphabet_size must be a positive integer")
    alphabet_size = int(alphabet_size)
    if alphabet_size <= 0:
        raise ValueError("alphabet_size must be positive")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie strictly between zero and one")
    if not 0.0 < beta < 1.0:
        raise ValueError("beta must lie strictly between zero and one")

    remaining = separation - gap
    numerator = (
        sqrt(log(2.0 * alphabet_size / alpha))
        + sqrt(log(2.0 * alphabet_size / beta))
    ) ** 2
    threshold = numerator / (2.0 * remaining**2)
    sample_size = max(1, int(floor(threshold)) + 1)

    while (
        joint_linf_required_population_separation(
            sample_size=sample_size,
            alphabet_size=alphabet_size,
            alpha=alpha,
            beta=beta,
            optimization_gap_upper=gap,
        )
        >= separation
    ):
        sample_size += 1

    while sample_size > 1:
        previous_required = joint_linf_required_population_separation(
            sample_size=sample_size - 1,
            alphabet_size=alphabet_size,
            alpha=alpha,
            beta=beta,
            optimization_gap_upper=gap,
        )
        if previous_required >= separation:
            break
        sample_size -= 1

    return sample_size


def numerical_joint_power_plan(
    *,
    population_separation_margin: float,
    alphabet_size: int,
    alpha: float = 0.05,
    beta: float = 0.20,
    optimization_gap_upper: float = 0.0,
) -> P79NumericalPowerPlan:
    """Return a numerical sample-size plan for a declared separation margin."""

    sample_size = sufficient_joint_linf_sample_size(
        population_separation_margin=population_separation_margin,
        alphabet_size=alphabet_size,
        alpha=alpha,
        beta=beta,
        optimization_gap_upper=optimization_gap_upper,
    )
    rejection_radius = finite_alphabet_cell_linf_radius(
        sample_size,
        alphabet_size,
        alpha,
    )
    alternative_radius = finite_alphabet_cell_linf_radius(
        sample_size,
        alphabet_size,
        beta,
    )
    required = rejection_radius + alternative_radius + float(optimization_gap_upper)
    return P79NumericalPowerPlan(
        sample_size=sample_size,
        alphabet_size=int(alphabet_size),
        alpha=float(alpha),
        beta=float(beta),
        population_separation_margin=float(population_separation_margin),
        optimization_gap_upper=float(optimization_gap_upper),
        rejection_radius=float(rejection_radius),
        alternative_radius=float(alternative_radius),
        required_separation=float(required),
        power_lower_bound=float(1.0 - beta),
    )
