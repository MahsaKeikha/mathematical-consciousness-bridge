"""Proposition 39: finite-data quantum model-set non-factorization.

The module certifies failure of P38 stochastic factorization relative to a declared
finite confidence set of quantum operational hypotheses. Each hypothesis encodes
which preparations have exactly the same operational quantum-state label. Target
uncertainty is supplied as simultaneous total-variation radii.

The result is descriptor and model-class relative. It does not infer that quantum
mechanics is incomplete or that any target is consciousness.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from dataclasses import dataclass
from typing import TypeVar

from consciousness_bridge.identifiability import total_variation_discrete

Preparation = TypeVar("Preparation", bound=Hashable)
QuantumModel = TypeVar("QuantumModel", bound=Hashable)
QuantumState = TypeVar("QuantumState", bound=Hashable)
Target = TypeVar("Target", bound=Hashable)


@dataclass(frozen=True)
class QuantumModelSetNonfactorizationCertificate:
    """Finite-data certificate relative to a declared quantum confidence set."""

    model_count: int
    violating_model_count: int
    robust_violation_margin: float
    confidence_lower_bound: float
    certified: bool


def target_separation_lower_bound(
    first: Mapping[Target, float],
    second: Mapping[Target, float],
    first_radius: float,
    second_radius: float,
) -> float:
    """Lower-bound the true target-law TV separation on the confidence event."""
    _validate_radius(first_radius)
    _validate_radius(second_radius)
    empirical_tv = total_variation_discrete(first, second)
    return max(0.0, empirical_tv - first_radius - second_radius)


def quantum_model_violation_margin(
    preparations: Sequence[Preparation],
    state_labels: Mapping[Preparation, QuantumState],
    target_estimates: Mapping[Preparation, Mapping[Target, float]],
    target_tv_radii: Mapping[Preparation, float],
) -> float:
    """Return the strongest certified same-state target separation for one model.

    A positive value means this candidate quantum operational hypothesis contains
    at least one exact same-state pair whose true target distributions must differ
    on the declared simultaneous target-confidence event.
    """
    preps = tuple(preparations)
    _validate_inputs(preps, state_labels, target_estimates, target_tv_radii)

    margin = 0.0
    for index, first in enumerate(preps):
        for second in preps[index + 1 :]:
            if state_labels[first] != state_labels[second]:
                continue
            margin = max(
                margin,
                target_separation_lower_bound(
                    target_estimates[first],
                    target_estimates[second],
                    target_tv_radii[first],
                    target_tv_radii[second],
                ),
            )
    return margin


def model_set_nonfactorization_certificate(
    preparations: Sequence[Preparation],
    quantum_models: Mapping[
        QuantumModel, Mapping[Preparation, QuantumState]
    ],
    confidence_models: Sequence[QuantumModel],
    target_estimates: Mapping[Preparation, Mapping[Target, float]],
    target_tv_radii: Mapping[Preparation, float],
    *,
    alpha_quantum: float,
    alpha_target: float,
    tolerance: float = 1e-12,
) -> QuantumModelSetNonfactorizationCertificate:
    """Certify P38 non-factorization for every model in a confidence set.

    Assumptions external to this deterministic audit are:

    1. the true declared quantum operational hypothesis lies in confidence_models
       with probability at least 1 - alpha_quantum;
    2. every true target distribution lies inside its supplied TV ball
       simultaneously with probability at least 1 - alpha_target.

    By the union bound, both events hold with probability at least
    1 - alpha_quantum - alpha_target. Certification requires a positive violation
    margin for every candidate quantum hypothesis in the declared confidence set.
    """
    if tolerance < 0.0:
        raise ValueError("tolerance must be nonnegative")
    _validate_alpha(alpha_quantum, "alpha_quantum")
    _validate_alpha(alpha_target, "alpha_target")

    preps = tuple(preparations)
    models = tuple(confidence_models)
    if not models:
        raise ValueError("confidence_models must be nonempty")
    if len(set(models)) != len(models):
        raise ValueError("confidence_models must contain unique labels")
    if any(model not in quantum_models for model in models):
        raise ValueError("every confidence model must be declared in quantum_models")

    margins = [
        quantum_model_violation_margin(
            preps,
            quantum_models[model],
            target_estimates,
            target_tv_radii,
        )
        for model in models
    ]
    robust_margin = min(margins)
    violating_count = sum(margin > tolerance for margin in margins)
    confidence = max(0.0, 1.0 - alpha_quantum - alpha_target)

    return QuantumModelSetNonfactorizationCertificate(
        model_count=len(models),
        violating_model_count=violating_count,
        robust_violation_margin=robust_margin,
        confidence_lower_bound=confidence,
        certified=robust_margin > tolerance,
    )


def _validate_inputs(
    preparations: tuple[Preparation, ...],
    state_labels: Mapping[Preparation, QuantumState],
    target_estimates: Mapping[Preparation, Mapping[Target, float]],
    target_tv_radii: Mapping[Preparation, float],
) -> None:
    if not preparations:
        raise ValueError("preparations must be nonempty")
    if len(set(preparations)) != len(preparations):
        raise ValueError("preparations must be unique")
    expected = set(preparations)
    if set(state_labels) != expected:
        raise ValueError("state_labels must cover every and only preparation")
    if set(target_estimates) != expected:
        raise ValueError("target_estimates must cover every and only preparation")
    if set(target_tv_radii) != expected:
        raise ValueError("target_tv_radii must cover every and only preparation")
    for preparation in preparations:
        _validate_radius(target_tv_radii[preparation])
        total_variation_discrete(
            target_estimates[preparation], target_estimates[preparation]
        )


def _validate_radius(radius: float) -> None:
    if not 0.0 <= radius <= 1.0:
        raise ValueError("total-variation radii must lie in [0, 1]")


def _validate_alpha(alpha: float, name: str) -> None:
    if not 0.0 <= alpha < 1.0:
        raise ValueError(f"{name} must lie in [0, 1)")
