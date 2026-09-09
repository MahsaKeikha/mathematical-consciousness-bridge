"""Finite helpers for experiment-class bridge identifiability.

The functions implement discrete versions of quantities used in Proposition 2.
They compare observable probability laws induced by complete bridge theories;
they do not assign consciousness to a physical system.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from math import exp, isclose
from typing import TypeVar

Y = TypeVar("Y", bound=Hashable)
Protocol = TypeVar("Protocol", bound=Hashable)


def _validate_distribution(distribution: Mapping[Y, float]) -> None:
    if any(probability < 0.0 for probability in distribution.values()):
        raise ValueError("Probabilities must be nonnegative.")
    if not isclose(sum(distribution.values()), 1.0, rel_tol=1e-9, abs_tol=1e-12):
        raise ValueError("Probabilities must sum to one.")


def total_variation_discrete(
    first: Mapping[Y, float],
    second: Mapping[Y, float],
) -> float:
    """Return total-variation distance between two finite distributions."""
    _validate_distribution(first)
    _validate_distribution(second)
    outcomes = set(first) | set(second)
    return 0.5 * sum(
        abs(first.get(outcome, 0.0) - second.get(outcome, 0.0))
        for outcome in outcomes
    )


def experiment_class_discriminability(
    first: Mapping[Protocol, Mapping[Y, float]],
    second: Mapping[Protocol, Mapping[Y, float]],
) -> float:
    """Return maximum total variation over a finite common protocol class."""
    if set(first) != set(second):
        raise ValueError("Theories must be compared on the same protocol class.")
    if not first:
        raise ValueError("Protocol class must be nonempty.")
    return max(
        total_variation_discrete(first[protocol], second[protocol])
        for protocol in first
    )


def optimal_equal_prior_error(total_variation: float) -> float:
    """Return optimal one-shot Bayes error for equal prior probabilities."""
    if not 0.0 <= total_variation <= 1.0:
        raise ValueError("Total variation must lie in [0, 1].")
    return 0.5 * (1.0 - total_variation)


def repeated_event_error_bound(sample_count: int, eta: float) -> float:
    """Return Proposition 2 Hoeffding bound exp(-n eta^2 / 2)."""
    if sample_count < 1:
        raise ValueError("sample_count must be positive.")
    if not 0.0 < eta <= 1.0:
        raise ValueError("eta must lie in (0, 1].")
    return exp(-0.5 * sample_count * eta**2)
