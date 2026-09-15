"""P93 selective finite-sample certification of the P92 sign obstruction.

P92 proves that every law in the complete P75 family has a nonnegative product
of three selected conditional 2 by 2 determinants. The established empirical
witness has determinant signs (-,+,+), but a population rejection still needs
to distinguish those observed signs from sampling uncertainty.

P93 builds one finite-sample rejection gate around exactly the seven observable
cells used by the P92 minors. Each selected cell receives a fixed rational
error budget before the data are interpreted. P79 then supplies a certified
rational upper bound on the corresponding two-sided Hoeffding radius. Exact
interval arithmetic propagates the seven cell intervals through the three
P92 determinants.

If the resulting determinant intervals force a negative sign product, then the
population law cannot belong to the P75 family on the simultaneous confidence
event. The familywise error bound is the sum of the fixed cell error budgets.

This is a model rejection theorem for the declared P75 family. It does not
identify any latent state with consciousness, establish nonphysicality, or
solve the physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping

from consciousness_bridge.certified_sampling_radius import (
    certified_finite_alphabet_sampling_radius,
)
from consciousness_bridge.exact_global_mixed_prevalence_distance import (
    p92_selected_determinants_exact,
)

_SELECTED_LABELS = (
    "t000",
    "t001",
    "t010",
    "t011",
    "t100",
    "t101",
    "t111",
)

_MINOR_LABELS = (
    (("t001", "t011"), ("t101", "t111")),
    (("t000", "t001"), ("t100", "t101")),
    (("t000", "t001"), ("t010", "t011")),
)


@dataclass(frozen=True)
class P93CellInterval:
    """One selected empirical cell with a certified population interval."""

    label: str
    empirical: Fraction
    alpha: Fraction
    radius_upper: Fraction
    lower: Fraction
    upper: Fraction


@dataclass(frozen=True)
class P93DeterminantInterval:
    """Exact interval image of one P92 determinant over a cell box."""

    lower: Fraction
    upper: Fraction
    forced_sign: int


@dataclass(frozen=True)
class P93SelectiveRejectionCertificate:
    """Finite-sample certificate for the P92 three-minor sign obstruction."""

    sample_size: int
    alpha_total: Fraction
    alpha_spent: Fraction
    cell_intervals: tuple[P93CellInterval, ...]
    empirical_determinants: tuple[Fraction, Fraction, Fraction]
    determinant_intervals: tuple[P93DeterminantInterval, ...]
    forced_signs: tuple[int, int, int]
    reject_p75: bool
    conclusion: str



def p93_selected_cells_exact(
    law: tuple[Fraction, ...],
) -> dict[str, Fraction]:
    """Return the seven full-law cells used by the three P92 minors."""

    if len(law) != 16:
        raise ValueError("law must contain sixteen probabilities")
    if any(not isinstance(value, Fraction) for value in law):
        raise TypeError("law entries must be fractions.Fraction")
    if any(value < 0 or value > 1 for value in law):
        raise ValueError("law entries must lie in [0, 1]")
    if sum(law, start=Fraction(0)) != 1:
        raise ValueError("law must have total mass one")

    subtensor = law[8:16]
    return {
        "t000": subtensor[0],
        "t001": subtensor[1],
        "t010": subtensor[2],
        "t011": subtensor[3],
        "t100": subtensor[4],
        "t101": subtensor[5],
        "t111": subtensor[7],
    }



def p93_uniform_alpha_allocation(alpha: Fraction) -> dict[str, Fraction]:
    """Split a rational familywise error budget equally across seven cells."""

    if not isinstance(alpha, Fraction):
        raise TypeError("alpha must be a fractions.Fraction")
    if alpha <= 0 or alpha >= 1:
        raise ValueError("alpha must lie strictly between zero and one")
    share = alpha / len(_SELECTED_LABELS)
    return {label: share for label in _SELECTED_LABELS}



def p93_witness_alpha_allocation_95() -> dict[str, Fraction]:
    """Return the fixed 95 percent allocation used by the P93 witness record.

    The allocation is declared independently of any random table. It spends
    most of the familywise budget on the four cells controlling the tight
    negative P92 minor while retaining positive budgets for every selected
    cell. The seven fractions sum exactly to 1/20.
    """

    allocation = {
        "t000": Fraction(1, 50_000),
        "t001": Fraction(173, 10_000),
        "t010": Fraction(1, 100_000_000),
        "t011": Fraction(81, 10_000),
        "t100": Fraction(1, 50_000),
        "t101": Fraction(169, 10_000),
        "t111": Fraction(765_999, 100_000_000),
    }
    if sum(allocation.values(), start=Fraction(0)) != Fraction(1, 20):
        raise RuntimeError("P93 witness allocation must sum exactly to 1/20")
    return allocation



def _validate_empirical_law(
    law: tuple[Fraction, ...],
    *,
    sample_size: int,
) -> tuple[Fraction, ...]:
    p93_selected_cells_exact(law)
    if isinstance(sample_size, bool) or not isinstance(sample_size, int):
        raise TypeError("sample_size must be an integer")
    if sample_size <= 0:
        raise ValueError("sample_size must be positive")
    if any((value * sample_size).denominator != 1 for value in law):
        raise ValueError("law is not an empirical table for this sample_size")
    return law



def _validate_allocation(
    allocation: Mapping[str, Fraction],
    *,
    alpha_total: Fraction,
) -> dict[str, Fraction]:
    if not isinstance(alpha_total, Fraction):
        raise TypeError("alpha_total must be a fractions.Fraction")
    if alpha_total <= 0 or alpha_total >= 1:
        raise ValueError("alpha_total must lie strictly between zero and one")
    if set(allocation) != set(_SELECTED_LABELS):
        raise ValueError("allocation must contain exactly the seven P93 labels")

    result: dict[str, Fraction] = {}
    for label in _SELECTED_LABELS:
        value = allocation[label]
        if not isinstance(value, Fraction):
            raise TypeError("allocation entries must be fractions.Fraction")
        if value <= 0 or value >= 1:
            raise ValueError("allocation entries must lie strictly between zero and one")
        result[label] = value

    if sum(result.values(), start=Fraction(0)) > alpha_total:
        raise ValueError("allocation exceeds alpha_total")
    return result



def _determinant_interval_exact(
    matrix: tuple[
        tuple[P93CellInterval, P93CellInterval],
        tuple[P93CellInterval, P93CellInterval],
    ],
) -> P93DeterminantInterval:
    """Return the exact determinant range over one nonnegative interval box."""

    a, b = matrix[0]
    c, d = matrix[1]
    lower = a.lower * d.lower - b.upper * c.upper
    upper = a.upper * d.upper - b.lower * c.lower
    if upper < 0:
        sign = -1
    elif lower > 0:
        sign = 1
    else:
        sign = 0
    return P93DeterminantInterval(lower=lower, upper=upper, forced_sign=sign)



def certify_p93_selective_sign_coherence_rejection(
    empirical_law: tuple[Fraction, ...],
    *,
    sample_size: int,
    alpha_total: Fraction,
    alpha_allocation: Mapping[str, Fraction],
    series_terms: int = 16,
    sqrt_bits: int = 64,
) -> P93SelectiveRejectionCertificate:
    """Certify or refuse the selective P92 finite-sample rejection gate.

    For cell ``x`` with fixed error budget ``alpha_x``, P79 is called with
    alphabet size one. Its upper radius certifies

        |P_hat(x) - P(x)| <= r_x

    except on an event of probability at most ``alpha_x``. A union bound over
    the seven selected cells therefore gives simultaneous coverage at least
    ``1 - sum(alpha_x)`` and hence at least ``1 - alpha_total``.

    The determinant interval bounds are exact because all cell intervals are
    nonnegative and ``a*d - b*c`` is increasing in ``a,d`` and decreasing in
    ``b,c`` on the nonnegative orthant.
    """

    empirical_law = _validate_empirical_law(
        empirical_law,
        sample_size=sample_size,
    )
    allocation = _validate_allocation(
        alpha_allocation,
        alpha_total=alpha_total,
    )
    selected = p93_selected_cells_exact(empirical_law)

    interval_by_label: dict[str, P93CellInterval] = {}
    for label in _SELECTED_LABELS:
        radius = certified_finite_alphabet_sampling_radius(
            sample_size=sample_size,
            alphabet_size=1,
            alpha=allocation[label],
            series_terms=series_terms,
            sqrt_bits=sqrt_bits,
        ).cell_linf_radius_upper
        empirical = selected[label]
        interval_by_label[label] = P93CellInterval(
            label=label,
            empirical=empirical,
            alpha=allocation[label],
            radius_upper=radius,
            lower=max(Fraction(0), empirical - radius),
            upper=min(Fraction(1), empirical + radius),
        )

    determinant_intervals = tuple(
        _determinant_interval_exact(
            (
                (
                    interval_by_label[labels[0][0]],
                    interval_by_label[labels[0][1]],
                ),
                (
                    interval_by_label[labels[1][0]],
                    interval_by_label[labels[1][1]],
                ),
            )
        )
        for labels in _MINOR_LABELS
    )
    forced_signs = tuple(interval.forced_sign for interval in determinant_intervals)
    reject = 0 not in forced_signs and forced_signs[0] * forced_signs[1] * forced_signs[2] < 0
    empirical_determinants = p92_selected_determinants_exact(empirical_law)
    alpha_spent = sum(allocation.values(), start=Fraction(0))
    conclusion = (
        "P75 rejected by selective P92 sign-coherence confidence box"
        if reject
        else "P75 not rejected by the selective P93 certificate"
    )
    return P93SelectiveRejectionCertificate(
        sample_size=sample_size,
        alpha_total=alpha_total,
        alpha_spent=alpha_spent,
        cell_intervals=tuple(interval_by_label[label] for label in _SELECTED_LABELS),
        empirical_determinants=empirical_determinants,
        determinant_intervals=determinant_intervals,
        forced_signs=forced_signs,
        reject_p75=reject,
        conclusion=conclusion,
    )
