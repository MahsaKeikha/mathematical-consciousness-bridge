"""P79 three-way full-law decision certificate for the P77-P78 interface.

P77 rejects a declared observed-law model set when the complete confidence
region around the empirical law is disjoint from that model set. P78 supplies
a certified bracket on the empirical L-infinity distance to the continuous P75
four-view latent family.

P79 uses both sides of that bracket without reversing their logical roles. Let

    L <= d_inf(P_hat, M_P75) <= U

be a valid P78 distance bracket and let

    eps_lower <= eps_n <= eps_upper

be mathematically valid bounds on the P77 sampling radius. Then

    L > eps_upper

certifies rejection, while

    U <= eps_lower

certifies that the P77 confidence ball intersects the declared model family.
The second conclusion is a certified non-separation result for this test at the
current data and confidence level. It is not model acceptance.

The unresolved case is the only one in which more optimization refinement on
the same empirical law can change the P77/P78 computational conclusion.
Standard confidence-set inversion and branch-and-bound bracketing are not new.
The repository-specific contribution is their directionally correct assembly
at the P77-P78 interface, including two-sided radius certification and an
explicit three-way stopping rule.

This module does not identify the P75 latent state with consciousness.
It does not validate the target-measurement model after non-separation.
It does not solve the physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from consciousness_bridge.certified_continuous_model_separation import (
    P78DistanceBracket,
)


@dataclass(frozen=True)
class P79ThreeWayDecisionCertificate:
    """Certified sign bracket for empirical model distance minus sampling radius."""

    distance_lower_bound: Fraction
    distance_upper_bound: Fraction
    sampling_radius_lower_bound: Fraction
    sampling_radius_upper_bound: Fraction
    signed_margin_lower_bound: Fraction
    signed_margin_upper_bound: Fraction
    certified_rejection: bool
    certified_nonseparation: bool
    unresolved: bool
    decision: str
    conclusion: str


def _validate_nonnegative_fraction(value: Fraction, *, name: str) -> Fraction:
    if not isinstance(value, Fraction):
        raise TypeError(f"{name} must be a fractions.Fraction")
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")
    return value


def three_way_full_law_decision(
    *,
    distance_lower_bound: Fraction,
    distance_upper_bound: Fraction,
    sampling_radius_lower_bound: Fraction,
    sampling_radius_upper_bound: Fraction,
) -> P79ThreeWayDecisionCertificate:
    """Return the rigorous P79 rejection/non-separation/unresolved decision.

    The distance bounds must satisfy

        distance_lower_bound <= d_inf(P_hat, M) <= distance_upper_bound,

    and the radius bounds must satisfy

        sampling_radius_lower_bound <= eps_n <= sampling_radius_upper_bound.

    The model family must be one for which the upper distance bound is
    attainable or otherwise witnessed by an admissible model law. The P75
    model family used by P78 is the continuous image of the compact cube
    ``[0,1]^9``, so its L-infinity distance is attained.

    The interval

        [distance_lower_bound - sampling_radius_upper_bound,
         distance_upper_bound - sampling_radius_lower_bound]

    contains the exact signed quantity ``d_inf(P_hat,M) - eps_n``.

    Rejection requires the entire signed interval to be positive. Certified
    non-separation requires the entire signed interval to be nonpositive. In
    the remaining case the current computational bracket is unresolved.
    """

    distance_lower = _validate_nonnegative_fraction(
        distance_lower_bound,
        name="distance_lower_bound",
    )
    distance_upper = _validate_nonnegative_fraction(
        distance_upper_bound,
        name="distance_upper_bound",
    )
    radius_lower = _validate_nonnegative_fraction(
        sampling_radius_lower_bound,
        name="sampling_radius_lower_bound",
    )
    radius_upper = _validate_nonnegative_fraction(
        sampling_radius_upper_bound,
        name="sampling_radius_upper_bound",
    )

    if distance_lower > distance_upper:
        raise ValueError("distance bounds must satisfy lower <= upper")
    if radius_lower > radius_upper:
        raise ValueError("sampling-radius bounds must satisfy lower <= upper")

    signed_lower = distance_lower - radius_upper
    signed_upper = distance_upper - radius_lower

    reject = signed_lower > 0
    nonseparation = signed_upper <= 0
    unresolved = not reject and not nonseparation

    if reject:
        decision = "reject"
        conclusion = (
            "certified P77 full-law rejection: the global model-distance lower "
            "bound exceeds the certified sampling-radius upper bound"
        )
    elif nonseparation:
        decision = "nonseparation"
        conclusion = (
            "certified P77 non-separation at the current data and confidence level: "
            "the model-distance upper bound lies inside the certified sampling radius; "
            "this is not model acceptance"
        )
    else:
        decision = "unresolved"
        conclusion = (
            "current certified distance and sampling-radius brackets overlap the "
            "P77 decision boundary; further computation or new statistical "
            "information may be required"
        )

    return P79ThreeWayDecisionCertificate(
        distance_lower_bound=distance_lower,
        distance_upper_bound=distance_upper,
        sampling_radius_lower_bound=radius_lower,
        sampling_radius_upper_bound=radius_upper,
        signed_margin_lower_bound=signed_lower,
        signed_margin_upper_bound=signed_upper,
        certified_rejection=reject,
        certified_nonseparation=nonseparation,
        unresolved=unresolved,
        decision=decision,
        conclusion=conclusion,
    )


def p78_three_way_full_law_decision(
    bracket: P78DistanceBracket,
    *,
    sampling_radius_lower_bound: Fraction,
    sampling_radius_upper_bound: Fraction,
) -> P79ThreeWayDecisionCertificate:
    """Apply the P79 three-way rule directly to a certified P78 bracket."""

    if not isinstance(bracket, P78DistanceBracket):
        raise TypeError("bracket must be a P78DistanceBracket")
    return three_way_full_law_decision(
        distance_lower_bound=bracket.lower_bound,
        distance_upper_bound=bracket.upper_bound,
        sampling_radius_lower_bound=sampling_radius_lower_bound,
        sampling_radius_upper_bound=sampling_radius_upper_bound,
    )


def total_decision_uncertainty_width(
    certificate: P79ThreeWayDecisionCertificate,
) -> Fraction:
    """Return the width of the certified signed decision interval.

    Algebraically this is the sum of the optimization-gap width and the
    sampling-radius enclosure width. It measures computational/numerical
    uncertainty around the P77 threshold, not statistical evidence strength.
    """

    if not isinstance(certificate, P79ThreeWayDecisionCertificate):
        raise TypeError("certificate must be a P79ThreeWayDecisionCertificate")
    return certificate.signed_margin_upper_bound - certificate.signed_margin_lower_bound


def margin_resolution_is_guaranteed(
    *,
    exact_signed_margin_magnitude: Fraction,
    optimization_gap_upper_bound: Fraction,
    sampling_radius_gap_upper_bound: Fraction = Fraction(0),
) -> bool:
    """Return whether bracket uncertainty is strictly below a nonzero true margin.

    If ``m = |d_inf(P_hat,M) - eps_n| > 0`` and the total bracket width is
    strictly smaller than ``m``, then a valid bracket enclosing both quantities
    cannot continue to straddle the decision boundary. This is a deterministic
    stopping statement. The exact margin is generally unknown in applications,
    so this helper records theorem logic rather than an operational estimator.
    """

    margin = _validate_nonnegative_fraction(
        exact_signed_margin_magnitude,
        name="exact_signed_margin_magnitude",
    )
    optimization_gap = _validate_nonnegative_fraction(
        optimization_gap_upper_bound,
        name="optimization_gap_upper_bound",
    )
    radius_gap = _validate_nonnegative_fraction(
        sampling_radius_gap_upper_bound,
        name="sampling_radius_gap_upper_bound",
    )
    if margin == 0:
        return False
    return optimization_gap + radius_gap < margin
