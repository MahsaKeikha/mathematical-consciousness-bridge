"""P100 anytime-valid sequential e-process for repeated P99 certification rounds.

P99 converts one cross-fitted certification round into an exact e-value E_t with
null expectation at most one. P100 permits an open-ended sequence of fresh
certification rounds whose plans, calibrations, and betting stakes may adapt to
past information but must be frozen before the current round's certification data
are inspected.

For a predictable exact-rational stake eta_t in [0, 1], define

    F_t = (1 - eta_t) + eta_t E_t.

Conditional validity of E_t gives E[F_t | past] <= 1. Therefore

    M_t = product_{s <= t} F_s

is a nonnegative supermartingale under the declared sequential global null. By
Ville's inequality, P(sup_t M_t >= 1/alpha) <= alpha. Consequently the first
crossing of 1/alpha is an anytime-valid rejection time and repeated inspection or
data-dependent stopping does not require a new alpha split across rounds.

The reserve term 1-eta_t is important operationally: when eta_t < 1, one round
with E_t = 0 reduces rather than annihilates the accumulated process. P100 does
not claim that this stake rule is optimal, and it does not make dependent or
reused certification data fresh by declaration.

P100 remains conditional on the P95-P99 model family, dependence assumptions,
selection-valid data separation, and the sequential freshness condition. It does
not turn non-rejection into model acceptance, identify a latent state with
consciousness, establish nonphysicality, or complete the
physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from consciousness_bridge.cross_fitted_evalue_aggregation import (
    P99CrossFitFoldInput,
    P99CrossFittedEValueCertificate,
    certify_p99_balanced_distributed_evidence_95_threshold_exact,
    certify_p99_cross_fitted_evalue_aggregation_exact,
)

_ALPHA_95 = Fraction(1, 20)


@dataclass(frozen=True)
class P100SequentialRoundInput:
    """One sequential P99 round and its predictable betting stake."""

    name: str
    folds: tuple[P99CrossFitFoldInput, ...]
    stake: Fraction
    choices_predictable_from_past_only: bool
    certification_data_conditionally_fresh_given_past: bool


@dataclass(frozen=True)
class P100RoundEProcessCertificate:
    """Exact contribution of one P99 round to the sequential e-process."""

    round_index: int
    name: str
    stake: Fraction
    nested_p99_certificate: P99CrossFittedEValueCertificate
    round_e_value: Fraction
    betting_factor: Fraction
    cumulative_e_process: Fraction
    crosses_global_threshold: bool


@dataclass(frozen=True)
class P100AnytimeSequentialEProcessCertificate:
    """Exact anytime-valid sequential rejection certificate."""

    round_count: int
    global_alpha: Fraction
    global_rejection_e_value: Fraction
    round_certificates: tuple[P100RoundEProcessCertificate, ...]
    final_e_process: Fraction
    maximum_e_process: Fraction
    first_crossing_round: int | None
    rejects_sequential_joint_p75_null: bool
    conclusion: str


@dataclass(frozen=True)
class P100BalancedModerateEvidenceCheckpoint:
    """Exact 95 percent two-round checkpoint built from the P99 balanced design."""

    global_alpha: Fraction
    fold_count: int
    regime_count: int
    dependence_range: int
    fold_test_alpha: Fraction
    rejecting_folds_per_round: int
    round_e_value: Fraction
    stake: Fraction
    betting_factor: Fraction
    global_rejection_e_value: Fraction
    first_crossing_round: int
    cumulative_at_first_crossing: Fraction
    first_certifying_sample_size_per_regime: int
    first_exact_replication_sample_size_per_regime: int
    unique_observations_per_round: int
    exact_unique_observations_per_round: int
    unique_observations_at_first_crossing: int
    exact_unique_observations_at_first_crossing: int


def _probability(value: Fraction, *, name: str) -> Fraction:
    if not isinstance(value, Fraction):
        raise TypeError(f"{name} must be a fractions.Fraction")
    if value <= 0 or value >= 1:
        raise ValueError(f"{name} must lie strictly between zero and one")
    return value


def _stake(value: Fraction) -> Fraction:
    if not isinstance(value, Fraction):
        raise TypeError("stake must be a fractions.Fraction")
    if value < 0 or value > 1:
        raise ValueError("stake must lie in [0, 1]")
    return value


def _nonempty_text(value: str, *, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a nonempty string")
    return value.strip()


def certify_p100_anytime_sequential_eprocess_exact(
    rounds: tuple[P100SequentialRoundInput, ...],
    *,
    global_alpha: Fraction,
    within_round_certification_blocks_mutually_independent: bool,
    own_block_excluded_from_within_round_selection: bool,
    series_terms: int = 20,
) -> P100AnytimeSequentialEProcessCertificate:
    """Build an exact sequential e-process from fresh P99 certification rounds.

    Each round may use all previous information to choose its P99 plan,
    calibration, and stake. Those choices must be predictable: they are frozen
    before the current round's fresh certification data are inspected. Under the
    sequential global null this gives conditional round e-value expectation at
    most one, so the product of the predictable-stake factors is a nonnegative
    supermartingale and is valid under arbitrary repeated inspection.
    """

    if not isinstance(rounds, tuple) or not rounds:
        raise ValueError("rounds must be a nonempty tuple")
    global_alpha = _probability(global_alpha, name="global_alpha")
    if isinstance(series_terms, bool) or not isinstance(series_terms, int) or series_terms <= 0:
        raise ValueError("series_terms must be a positive integer")
    if within_round_certification_blocks_mutually_independent is not True:
        raise ValueError("P99 certification blocks must be mutually independent within each round")
    if own_block_excluded_from_within_round_selection is not True:
        raise ValueError("each P99 fold must exclude its own certification block from selection")

    names: list[str] = []
    cumulative = Fraction(1)
    maximum = Fraction(1)
    threshold = Fraction(1, 1) / global_alpha
    first_crossing: int | None = None
    certificates: list[P100RoundEProcessCertificate] = []

    for index, round_input in enumerate(rounds, start=1):
        if not isinstance(round_input, P100SequentialRoundInput):
            raise TypeError("every round must be a P100SequentialRoundInput")
        name = _nonempty_text(round_input.name, name="round name")
        names.append(name)
        if round_input.choices_predictable_from_past_only is not True:
            raise ValueError("round plan, calibration, and stake must be predictable from past information only")
        if round_input.certification_data_conditionally_fresh_given_past is not True:
            raise ValueError("current-round certification data must be conditionally fresh given the past")
        stake = _stake(round_input.stake)

        nested = certify_p99_cross_fitted_evalue_aggregation_exact(
            round_input.folds,
            global_alpha=global_alpha,
            certification_blocks_mutually_independent=within_round_certification_blocks_mutually_independent,
            own_block_excluded_from_selection=own_block_excluded_from_within_round_selection,
            series_terms=series_terms,
        )
        round_e_value = nested.aggregate_e_value
        betting_factor = (Fraction(1) - stake) + stake * round_e_value
        cumulative *= betting_factor
        maximum = max(maximum, cumulative)
        crosses = cumulative >= threshold
        if crosses and first_crossing is None:
            first_crossing = index
        certificates.append(
            P100RoundEProcessCertificate(
                round_index=index,
                name=name,
                stake=stake,
                nested_p99_certificate=nested,
                round_e_value=round_e_value,
                betting_factor=betting_factor,
                cumulative_e_process=cumulative,
                crosses_global_threshold=crosses,
            )
        )

    if len(set(names)) != len(names):
        raise ValueError("round names must be unique")

    rejects = first_crossing is not None
    return P100AnytimeSequentialEProcessCertificate(
        round_count=len(rounds),
        global_alpha=global_alpha,
        global_rejection_e_value=threshold,
        round_certificates=tuple(certificates),
        final_e_process=cumulative,
        maximum_e_process=maximum,
        first_crossing_round=first_crossing,
        rejects_sequential_joint_p75_null=rejects,
        conclusion=(
            f"Sequential joint P75 null rejected anytime-validly at round {first_crossing}"
            if rejects
            else "Sequential joint P75 null not rejected by the anytime-valid e-process"
        ),
    )


def certify_p100_balanced_moderate_evidence_95_checkpoint_exact(
    *,
    fold_count: int = 2,
    regime_count: int = 2,
    dependence_range: int = 1,
    fold_test_alpha: Fraction = Fraction(1, 25),
    rejecting_folds_per_round: int = 1,
    stake: Fraction = Fraction(1, 2),
    series_terms: int = 20,
) -> P100BalancedModerateEvidenceCheckpoint:
    """Return the exact P100 checkpoint where moderate P99 rounds accumulate.

    The default P99 round has K=2 equal-weight folds and exactly one level-1/25
    rejecting fold, so its aggregate e-value is 25/2 and does not itself reach
    the 95 percent threshold 20. With stake 1/2, each successful moderate round
    contributes factor 27/4; two such rounds cross the anytime-valid threshold.
    """

    if isinstance(rejecting_folds_per_round, bool) or not isinstance(rejecting_folds_per_round, int):
        raise TypeError("rejecting_folds_per_round must be an integer")
    if rejecting_folds_per_round <= 0 or rejecting_folds_per_round > fold_count:
        raise ValueError("rejecting_folds_per_round must lie between one and fold_count")
    stake = _stake(stake)
    if stake == 0:
        raise ValueError("stake must be positive for a finite crossing checkpoint")

    p99 = certify_p99_balanced_distributed_evidence_95_threshold_exact(
        fold_count=fold_count,
        regime_count=regime_count,
        dependence_range=dependence_range,
        fold_test_alpha=fold_test_alpha,
        series_terms=series_terms,
    )
    round_e_value = Fraction(rejecting_folds_per_round, fold_count) / fold_test_alpha
    factor = (Fraction(1) - stake) + stake * round_e_value
    threshold = Fraction(1, 1) / _ALPHA_95
    if factor <= 1:
        raise ValueError("declared moderate-evidence factor does not accumulate toward rejection")

    cumulative = Fraction(1)
    crossing_round = 0
    while cumulative < threshold:
        cumulative *= factor
        crossing_round += 1

    return P100BalancedModerateEvidenceCheckpoint(
        global_alpha=_ALPHA_95,
        fold_count=fold_count,
        regime_count=regime_count,
        dependence_range=dependence_range,
        fold_test_alpha=fold_test_alpha,
        rejecting_folds_per_round=rejecting_folds_per_round,
        round_e_value=round_e_value,
        stake=stake,
        betting_factor=factor,
        global_rejection_e_value=threshold,
        first_crossing_round=crossing_round,
        cumulative_at_first_crossing=cumulative,
        first_certifying_sample_size_per_regime=p99.first_certifying_sample_size,
        first_exact_replication_sample_size_per_regime=p99.first_exact_replication_sample_size,
        unique_observations_per_round=p99.first_cross_fitted_unique_observations,
        exact_unique_observations_per_round=p99.first_exact_cross_fitted_unique_observations,
        unique_observations_at_first_crossing=(
            crossing_round * p99.first_cross_fitted_unique_observations
        ),
        exact_unique_observations_at_first_crossing=(
            crossing_round * p99.first_exact_cross_fitted_unique_observations
        ),
    )
