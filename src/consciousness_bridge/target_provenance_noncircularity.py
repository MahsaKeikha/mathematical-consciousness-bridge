"""Proposition 71: target-provenance non-circularity.

P19 tests whether an independently declared target factors through a physical
descriptor. P71 identifies a class of targets for which that test is vacuous by
construction.

If a target is defined as ``E = h(T)``, then exact factorization through ``T``
holds identically. In the finite stochastic setting, if the target is generated
through a channel that depends on the underlying state only through ``T``, then
``I(E; Omega | T) = 0`` by construction. These facts do not establish that the
target is experiential or that ``T`` is physically complete.

The same deterministic statement applies after a learned rule has been fixed:
conditioning on the training artifact, ``E_hat = h_D(T)`` still factors through
``T`` exactly. Train/test separation can protect statistical generalization, but
it does not by itself supply independent target provenance.

This module does not infer conceptual independence from observed data. Target
provenance is a design declaration rather than a statistic of the observed
joint law. The utilities below provide finite reference constructions for the
theorem.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from math import isfinite
from typing import TypeVar

from consciousness_bridge.fundamental_physical_sufficiency import (
    conditional_mutual_information,
    factorization_collisions,
)

Omega = TypeVar("Omega", bound=Hashable)
Physical = TypeVar("Physical", bound=Hashable)
Target = TypeVar("Target", bound=Hashable)


@dataclass(frozen=True)
class DeterministicTargetVacuityCertificate:
    """Finite verification of the deterministic P71 construction."""

    target_labels: tuple[Hashable, ...]
    induced_bridge_map: dict[Hashable, Hashable]
    factorization_collisions: tuple[tuple[int, int], ...]
    conditional_mutual_information_nats: float
    structurally_vacuous: bool


@dataclass(frozen=True)
class StochasticTargetVacuityCertificate:
    """Finite verification of a descriptor-only stochastic target channel."""

    joint_distribution: dict[tuple[Hashable, Hashable, Hashable], float]
    conditional_mutual_information_nats: float
    structurally_screened_off: bool


def deterministic_descriptor_target_certificate(
    omega_labels: Sequence[Omega],
    physical_labels: Sequence[Physical],
    target_rule: Mapping[Physical, Target],
) -> DeterministicTargetVacuityCertificate:
    """Construct ``E = h(T)`` and verify the P71 deterministic consequences.

    ``omega_labels`` identify the sampled underlying states. ``physical_labels``
    contain the declared descriptor value for each sampled state, and
    ``target_rule`` is the declared descriptor-derived target construction.

    The returned certificate verifies on the supplied finite support that:

    1. the induced target has no P19 fiber collision;
    2. the bridge map is exactly the supplied target rule on the observed image;
    3. the empirical ``I(E; Omega | T)`` is zero up to floating-point tolerance.

    The zero residual is a consequence of construction, not evidence that the
    physical descriptor explains an independently specified target.
    """
    if len(omega_labels) != len(physical_labels):
        raise ValueError("omega_labels and physical_labels must have equal length")
    if not omega_labels:
        raise ValueError("omega_labels and physical_labels must be nonempty")

    targets: list[Target] = []
    observed_map: dict[Physical, Target] = {}
    for physical in physical_labels:
        if physical not in target_rule:
            raise ValueError("target_rule must define every observed physical label")
        target = target_rule[physical]
        targets.append(target)
        observed_map[physical] = target

    collisions = tuple(factorization_collisions(physical_labels, targets))
    joint: dict[tuple[Hashable, Hashable, Hashable], float] = defaultdict(float)
    for omega, physical, target in zip(omega_labels, physical_labels, targets):
        joint[(omega, physical, target)] += 1.0

    residual = conditional_mutual_information(joint)
    tolerance = 1e-12
    if abs(residual) > tolerance:
        raise RuntimeError("descriptor-derived deterministic target had nonzero residual")

    return DeterministicTargetVacuityCertificate(
        target_labels=tuple(targets),
        induced_bridge_map=dict(observed_map),
        factorization_collisions=collisions,
        conditional_mutual_information_nats=0.0,
        structurally_vacuous=True,
    )


def stochastic_descriptor_channel_certificate(
    state_descriptor_weights: Mapping[tuple[Omega, Physical], float],
    target_channel_weights: Mapping[tuple[Physical, Target], float],
) -> StochasticTargetVacuityCertificate:
    """Construct a target channel satisfying ``Omega -> T -> E`` by design.

    ``state_descriptor_weights`` specify a finite nonnegative measure on
    ``(Omega, T)``. ``target_channel_weights`` specify nonnegative target-channel
    weights for ``(T, E)`` and are normalized separately for each observed
    descriptor value.

    The resulting joint distribution is

        P(omega, t, e) = P(omega, t) P(e | t),

    so P71 predicts ``I(E; Omega | T) = 0``. The routine constructs the joint law
    and verifies that identity numerically.
    """
    state_distribution = _normalize_state_descriptor_weights(state_descriptor_weights)
    channel = _normalize_target_channels(
        target_channel_weights,
        observed_physical={physical for _, physical in state_distribution},
    )

    joint: dict[tuple[Hashable, Hashable, Hashable], float] = defaultdict(float)
    for (omega, physical), state_probability in state_distribution.items():
        for (channel_physical, target), conditional_probability in channel.items():
            if channel_physical == physical:
                joint[(omega, physical, target)] += (
                    state_probability * conditional_probability
                )

    residual = conditional_mutual_information(joint)
    tolerance = 1e-12
    if abs(residual) > tolerance:
        raise RuntimeError("descriptor-only stochastic target channel had nonzero residual")

    return StochasticTargetVacuityCertificate(
        joint_distribution=dict(joint),
        conditional_mutual_information_nats=0.0,
        structurally_screened_off=True,
    )


def independently_declared_target_residual(
    omega_labels: Sequence[Omega],
    physical_labels: Sequence[Physical],
    target_labels: Sequence[Target],
) -> float:
    """Compute the P19 empirical residual for a separately supplied target.

    This helper intentionally accepts target labels rather than constructing
    them from the physical descriptor. A positive result can expose descriptor
    insufficiency on the supplied empirical law. A zero result does not certify
    conceptual target independence or a completed experiential bridge.
    """
    if not (
        len(omega_labels) == len(physical_labels) == len(target_labels)
    ):
        raise ValueError("omega, physical, and target labels must have equal length")
    if not omega_labels:
        raise ValueError("label sequences must be nonempty")

    joint: dict[tuple[Hashable, Hashable, Hashable], float] = defaultdict(float)
    for omega, physical, target in zip(
        omega_labels,
        physical_labels,
        target_labels,
    ):
        joint[(omega, physical, target)] += 1.0
    residual = conditional_mutual_information(joint)
    return max(0.0, residual)


def _normalize_state_descriptor_weights(
    weights: Mapping[tuple[Omega, Physical], float],
) -> dict[tuple[Omega, Physical], float]:
    if not weights:
        raise ValueError("state_descriptor_weights must be nonempty")
    total = 0.0
    for value in weights.values():
        if not isfinite(value) or value < 0.0:
            raise ValueError("state_descriptor_weights must be finite and nonnegative")
        total += value
    if total <= 0.0:
        raise ValueError("state_descriptor_weights must have positive total mass")
    return {key: value / total for key, value in weights.items() if value > 0.0}


def _normalize_target_channels(
    weights: Mapping[tuple[Physical, Target], float],
    *,
    observed_physical: set[Physical],
) -> dict[tuple[Physical, Target], float]:
    if not weights:
        raise ValueError("target_channel_weights must be nonempty")

    totals: dict[Physical, float] = defaultdict(float)
    for (physical, _), value in weights.items():
        if not isfinite(value) or value < 0.0:
            raise ValueError("target_channel_weights must be finite and nonnegative")
        totals[physical] += value

    missing = observed_physical.difference(
        physical for physical, total in totals.items() if total > 0.0
    )
    if missing:
        raise ValueError("target channel must have positive mass for every observed descriptor")

    return {
        (physical, target): value / totals[physical]
        for (physical, target), value in weights.items()
        if value > 0.0 and physical in observed_physical
    }
