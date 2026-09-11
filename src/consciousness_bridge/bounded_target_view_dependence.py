"""P79 robustness to bounded target-view local dependence.

P75-P78 use a four-view binary latent model with conditional independence of
the observed target views given the latent target state. P79 weakens that
assumption quantitatively instead of silently replacing it.

For each latent state, compare the true conditional joint view law with the
product of its own one-view marginals. A declared upper bound on the weighted
conditional dependence defect produces a corresponding neighborhood around the
P75 observed-law model. Therefore a P77/P78 model-distance lower bound can still
certify rejection when it exceeds sampling uncertainty plus the declared local
dependence allowance.

The dependence allowance must be justified independently or declared before the
rejection test. It must not be tuned from the same observed discrepancy merely
to avoid rejection.

This module does not identify a latent state with consciousness and does not
solve the physical-to-experiential bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Literal, Sequence

import numpy as np

Metric = Literal["linf", "l1"]


@dataclass(frozen=True)
class BoundedDependenceCertificate:
    """P79 rejection certificate under a declared local-dependence budget."""

    metric: Metric
    model_distance_lower_bound: float
    sampling_radius_upper_bound: float
    dependence_budget: float
    required_threshold: float
    excess_margin: float
    certified_incompatible: bool
    conclusion: str


def _probability_vector(values: Sequence[float], *, name: str) -> np.ndarray:
    array = np.asarray(values, dtype=float)
    if array.shape != (16,):
        raise ValueError(f"{name} must contain exactly sixteen cell masses")
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values")
    if np.any(array < 0.0):
        raise ValueError(f"{name} must be nonnegative")
    total = float(array.sum())
    if total <= 0.0:
        raise ValueError(f"{name} must have positive total mass")
    return array / total


def _metric_distance(first: np.ndarray, second: np.ndarray, metric: Metric) -> float:
    delta = np.abs(first - second)
    if metric == "linf":
        return float(np.max(delta))
    if metric == "l1":
        return float(np.sum(delta))
    raise ValueError("metric must be 'linf' or 'l1'")


def product_projection_from_conditional_law(
    conditional_law: Sequence[float],
) -> np.ndarray:
    """Return the four-view product law with the same one-view marginals.

    Cell order is lexicographic over ``product((0, 1), repeat=4)``.
    """

    law = _probability_vector(conditional_law, name="conditional_law")
    states = np.asarray(list(product((0, 1), repeat=4)), dtype=int)
    marginals = np.asarray(
        [float(law[states[:, index] == 1].sum()) for index in range(4)],
        dtype=float,
    )

    projected = np.empty(16, dtype=float)
    for row_index, state in enumerate(states):
        mass = 1.0
        for view_index, value in enumerate(state):
            probability_one = marginals[view_index]
            mass *= probability_one if value else 1.0 - probability_one
        projected[row_index] = mass
    return projected


def conditional_dependence_defect(
    conditional_law: Sequence[float],
    *,
    metric: Metric = "linf",
) -> float:
    """Measure local dependence from conditional independence at one latent state."""

    law = _probability_vector(conditional_law, name="conditional_law")
    projection = product_projection_from_conditional_law(law)
    return _metric_distance(law, projection, metric)


def observed_mixture_law(
    prevalence_plus: float,
    conditional_minus: Sequence[float],
    conditional_plus: Sequence[float],
) -> np.ndarray:
    """Return the observed four-view mixture law."""

    prevalence_plus = float(prevalence_plus)
    if not np.isfinite(prevalence_plus) or not 0.0 <= prevalence_plus <= 1.0:
        raise ValueError("prevalence_plus must lie in [0, 1]")
    minus = _probability_vector(conditional_minus, name="conditional_minus")
    plus = _probability_vector(conditional_plus, name="conditional_plus")
    return (1.0 - prevalence_plus) * minus + prevalence_plus * plus


def conditionally_independent_counterpart(
    prevalence_plus: float,
    conditional_minus: Sequence[float],
    conditional_plus: Sequence[float],
) -> np.ndarray:
    """Return the P75 law obtained by product-projecting each latent condition."""

    prevalence_plus = float(prevalence_plus)
    if not np.isfinite(prevalence_plus) or not 0.0 <= prevalence_plus <= 1.0:
        raise ValueError("prevalence_plus must lie in [0, 1]")
    minus_product = product_projection_from_conditional_law(conditional_minus)
    plus_product = product_projection_from_conditional_law(conditional_plus)
    return (1.0 - prevalence_plus) * minus_product + prevalence_plus * plus_product


def weighted_conditional_dependence_budget(
    prevalence_plus: float,
    conditional_minus: Sequence[float],
    conditional_plus: Sequence[float],
    *,
    metric: Metric = "linf",
) -> float:
    """Return the prevalence-weighted conditional dependence defect."""

    prevalence_plus = float(prevalence_plus)
    if not np.isfinite(prevalence_plus) or not 0.0 <= prevalence_plus <= 1.0:
        raise ValueError("prevalence_plus must lie in [0, 1]")
    minus_defect = conditional_dependence_defect(conditional_minus, metric=metric)
    plus_defect = conditional_dependence_defect(conditional_plus, metric=metric)
    return (1.0 - prevalence_plus) * minus_defect + prevalence_plus * plus_defect


def observed_distance_to_independent_counterpart(
    prevalence_plus: float,
    conditional_minus: Sequence[float],
    conditional_plus: Sequence[float],
    *,
    metric: Metric = "linf",
) -> float:
    """Return the observed-law distance to the constructed P75 counterpart."""

    observed = observed_mixture_law(
        prevalence_plus,
        conditional_minus,
        conditional_plus,
    )
    counterpart = conditionally_independent_counterpart(
        prevalence_plus,
        conditional_minus,
        conditional_plus,
    )
    return _metric_distance(observed, counterpart, metric)


def bounded_dependence_rejection_certificate(
    *,
    model_distance_lower_bound: float,
    sampling_radius_upper_bound: float,
    dependence_budget: float,
    metric: Metric = "linf",
) -> BoundedDependenceCertificate:
    """Apply the P79 robust P77/P78 rejection gate.

    If ``L`` is a certified lower bound on distance from the empirical law to
    the P75 conditionally independent model, ``eps`` is a valid upper bound on
    the sampling radius in the same norm, and ``rho`` is an independently
    justified upper bound on the allowed target-view dependence defect, then

        L > eps + rho

    rejects every population law satisfying that dependence budget.
    """

    if metric not in ("linf", "l1"):
        raise ValueError("metric must be 'linf' or 'l1'")

    values = {
        "model_distance_lower_bound": float(model_distance_lower_bound),
        "sampling_radius_upper_bound": float(sampling_radius_upper_bound),
        "dependence_budget": float(dependence_budget),
    }
    for name, value in values.items():
        if not np.isfinite(value) or value < 0.0:
            raise ValueError(f"{name} must be finite and nonnegative")

    threshold = values["sampling_radius_upper_bound"] + values["dependence_budget"]
    margin = values["model_distance_lower_bound"] - threshold
    reject = margin > 0.0

    if reject:
        conclusion = (
            "certified incompatible with the P75 model even after the declared "
            "target-view dependence allowance and sampling uncertainty are included"
        )
    else:
        conclusion = (
            "not rejected under the declared dependence allowance; non-rejection "
            "is inconclusive and is not model validation"
        )

    return BoundedDependenceCertificate(
        metric=metric,
        model_distance_lower_bound=values["model_distance_lower_bound"],
        sampling_radius_upper_bound=values["sampling_radius_upper_bound"],
        dependence_budget=values["dependence_budget"],
        required_threshold=threshold,
        excess_margin=margin,
        certified_incompatible=reject,
        conclusion=conclusion,
    )
