"""Proposition 38: quantum operational sufficiency and factorization tests.

The implementation works with hashable quantum-state fingerprints representing a
declared tomographically complete operational state. It tests whether deterministic
or stochastic targets are constant on fibers of that descriptor. It does not infer
that any target is consciousness or that quantum theory is physically incomplete.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from typing import TypeVar

Preparation = TypeVar("Preparation", bound=Hashable)
QuantumState = TypeVar("QuantumState", bound=Hashable)
Target = TypeVar("Target", bound=Hashable)


@dataclass(frozen=True)
class DeterministicQuantumSufficiencyCertificate:
    sufficient: bool
    collision_count: int


@dataclass(frozen=True)
class StochasticQuantumSufficiencyCertificate:
    sufficient: bool
    maximum_within_state_target_tv: float


def deterministic_quantum_sufficiency(
    preparations: Sequence[Preparation],
    quantum_state: Mapping[Preparation, QuantumState],
    target: Mapping[Preparation, Target],
) -> DeterministicQuantumSufficiencyCertificate:
    """Check whether a deterministic target factors through the quantum state."""
    preps = tuple(preparations)
    _validate_domains(preps, quantum_state, target)
    collisions = 0
    for i, first in enumerate(preps):
        for second in preps[i + 1 :]:
            if quantum_state[first] == quantum_state[second] and target[first] != target[second]:
                collisions += 1
    return DeterministicQuantumSufficiencyCertificate(
        sufficient=collisions == 0,
        collision_count=collisions,
    )


def deterministic_nonfactorization_witnesses(
    preparations: Sequence[Preparation],
    quantum_state: Mapping[Preparation, QuantumState],
    target: Mapping[Preparation, Target],
) -> list[tuple[Preparation, Preparation]]:
    """Return preparation pairs with equal quantum state but unequal target."""
    preps = tuple(preparations)
    _validate_domains(preps, quantum_state, target)
    witnesses: list[tuple[Preparation, Preparation]] = []
    for i, first in enumerate(preps):
        for second in preps[i + 1 :]:
            if quantum_state[first] == quantum_state[second] and target[first] != target[second]:
                witnesses.append((first, second))
    return witnesses


def stochastic_quantum_sufficiency(
    preparations: Sequence[Preparation],
    quantum_state: Mapping[Preparation, QuantumState],
    target_distributions: Mapping[Preparation, Mapping[Target, float]],
    *,
    tolerance: float = 1e-12,
) -> StochasticQuantumSufficiencyCertificate:
    """Check fiberwise equality of stochastic target laws."""
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")
    preps = tuple(preparations)
    _validate_domains(preps, quantum_state, target_distributions)
    maximum = 0.0
    for i, first in enumerate(preps):
        for second in preps[i + 1 :]:
            if quantum_state[first] == quantum_state[second]:
                maximum = max(
                    maximum,
                    _total_variation(
                        target_distributions[first], target_distributions[second]
                    ),
                )
    return StochasticQuantumSufficiencyCertificate(
        sufficient=maximum <= tolerance,
        maximum_within_state_target_tv=maximum,
    )


def _total_variation(
    first: Mapping[Target, float], second: Mapping[Target, float]
) -> float:
    support = set(first) | set(second)
    if any(first.get(key, 0.0) < 0.0 or second.get(key, 0.0) < 0.0 for key in support):
        raise ValueError("probabilities must be nonnegative")
    if abs(sum(first.values()) - 1.0) > 1e-9 or abs(sum(second.values()) - 1.0) > 1e-9:
        raise ValueError("target distributions must sum to one")
    return 0.5 * sum(abs(first.get(key, 0.0) - second.get(key, 0.0)) for key in support)


def _validate_domains(
    preparations: tuple[Preparation, ...],
    quantum_state: Mapping[Preparation, object],
    target: Mapping[Preparation, object],
) -> None:
    if not preparations:
        raise ValueError("preparations must be nonempty")
    if len(set(preparations)) != len(preparations):
        raise ValueError("preparations must be unique")
    if set(quantum_state) != set(preparations):
        raise ValueError("quantum_state must be defined on every and only declared preparation")
    if set(target) != set(preparations):
        raise ValueError("target must be defined on every and only declared preparation")
