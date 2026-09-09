"""Finite categorical sample-complexity helpers for Proposition 9."""

from __future__ import annotations

from math import ceil, exp, log


def uniform_tv_failure_bound(
    sample_count: int,
    physical_count: int,
    protocol_count: int,
    alphabet_size: int,
    epsilon: float,
) -> float:
    """Return the P9 union-bound failure probability for uniform TV error."""
    _validate_counts(sample_count, physical_count, protocol_count, alphabet_size)
    if epsilon <= 0.0:
        raise ValueError("epsilon must be positive.")

    cell_count = physical_count * protocol_count
    exponent = -8.0 * sample_count * epsilon**2 / alphabet_size**2
    bound = 2.0 * cell_count * alphabet_size * exp(exponent)
    return min(1.0, bound)


def required_trials_for_uniform_tv(
    physical_count: int,
    protocol_count: int,
    alphabet_size: int,
    epsilon: float,
    alpha: float,
) -> int:
    """Return sufficient repetitions per cell for uniform TV error <= epsilon."""
    _validate_positive_design(physical_count, protocol_count, alphabet_size)
    if epsilon <= 0.0:
        raise ValueError("epsilon must be positive.")
    _validate_alpha(alpha)

    cell_count = physical_count * protocol_count
    value = (
        alphabet_size**2
        / (8.0 * epsilon**2)
        * log(2.0 * cell_count * alphabet_size / alpha)
    )
    return ceil(value)


def required_trials_for_signature_recovery(
    physical_count: int,
    protocol_count: int,
    alphabet_size: int,
    signature_gap: float,
    alpha: float,
) -> int:
    """Return P9 sufficient repetitions using epsilon = signature_gap / 8."""
    _validate_positive_design(physical_count, protocol_count, alphabet_size)
    if signature_gap <= 0.0:
        raise ValueError("signature_gap must be positive.")
    _validate_alpha(alpha)

    cell_count = physical_count * protocol_count
    value = (
        8.0
        * alphabet_size**2
        / signature_gap**2
        * log(2.0 * cell_count * alphabet_size / alpha)
    )
    return ceil(value)


def midpoint_signature_threshold(
    within_spread: float,
    between_separation: float,
) -> float:
    """Return the midpoint threshold used by Proposition 9B."""
    if within_spread < 0.0 or between_separation < 0.0:
        raise ValueError("Distances must be nonnegative.")
    if not within_spread < between_separation:
        raise ValueError("between_separation must exceed within_spread.")
    return 0.5 * (within_spread + between_separation)


def _validate_counts(
    sample_count: int,
    physical_count: int,
    protocol_count: int,
    alphabet_size: int,
) -> None:
    if sample_count < 1:
        raise ValueError("sample_count must be positive.")
    _validate_positive_design(physical_count, protocol_count, alphabet_size)


def _validate_positive_design(
    physical_count: int,
    protocol_count: int,
    alphabet_size: int,
) -> None:
    if physical_count < 1:
        raise ValueError("physical_count must be positive.")
    if protocol_count < 1:
        raise ValueError("protocol_count must be positive.")
    if alphabet_size < 2:
        raise ValueError("alphabet_size must be at least two.")


def _validate_alpha(alpha: float) -> None:
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie in (0, 1).")
