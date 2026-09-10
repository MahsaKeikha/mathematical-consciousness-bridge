"""Proposition 49: dyadic certification schedules for P48 stopping bounds.

P49 reduces the number of certification evaluations by checking only when a
common local sample count reaches 1, 2, 4, 8, ... .  If P48 says that an edge
is guaranteed to have a sign certificate by local count N_e, the first dyadic
checkpoint at or above N_e is strictly less than 2 N_e.  Hence dyadic batching
uses only logarithmically many looks and loses less than a factor of two in the
sample-count stopping bound.

The theorem inherits statistical validity from P47.  It is a deterministic
scheduling theorem, not an adaptive-optimality result.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from math import isfinite, log2

from .gap_stopping_complexity import EdgeStoppingComplexity

Edge = tuple[object, object]


@dataclass(frozen=True)
class DyadicEdgeBound:
    """Dyadic checkpoint corresponding to one finite P48 edge threshold."""

    edge: Edge
    p48_samples: int | None
    dyadic_samples: int | None
    checkpoints: int | None
    overhead_ratio: float | None


@dataclass(frozen=True)
class DyadicStoppingBound:
    """Finite-family stopping bound under dyadic certification checks."""

    status: str
    p48_epochs: int | None
    dyadic_epochs: int | None
    certification_looks: int | None
    controlling_edges: tuple[Edge, ...]


def first_dyadic_at_or_above(samples: int) -> int:
    """Return the smallest power of two greater than or equal to ``samples``."""
    if samples < 1:
        raise ValueError("samples must be a positive integer")
    return 1 << (samples - 1).bit_length()


def dyadic_checkpoint_count(samples: int) -> int:
    """Return the number of dyadic looks through the first checkpoint >= samples.

    The schedule includes the initial look at local count one, so a threshold of
    one requires one look and a threshold in (2**(k-1), 2**k] requires k+1
    looks.
    """
    if samples < 1:
        raise ValueError("samples must be a positive integer")
    checkpoint = first_dyadic_at_or_above(samples)
    return checkpoint.bit_length()


def dyadic_edge_bound(bound: EdgeStoppingComplexity) -> DyadicEdgeBound:
    """Convert one P48 edge threshold into its dyadic scheduling bound."""
    if bound.local_samples is None:
        return DyadicEdgeBound(
            edge=bound.edge,
            p48_samples=None,
            dyadic_samples=None,
            checkpoints=None,
            overhead_ratio=None,
        )

    threshold = bound.local_samples
    if threshold < 1:
        raise ValueError("finite P48 local_samples must be positive")
    dyadic = first_dyadic_at_or_above(threshold)
    return DyadicEdgeBound(
        edge=bound.edge,
        p48_samples=threshold,
        dyadic_samples=dyadic,
        checkpoints=dyadic.bit_length(),
        overhead_ratio=dyadic / threshold,
    )


def dyadic_edge_bounds(
    bounds: Mapping[Edge, EdgeStoppingComplexity],
) -> dict[Edge, DyadicEdgeBound]:
    """Convert a finite P48 edge family into dyadic thresholds."""
    if not bounds:
        raise ValueError("bounds must be nonempty")
    result: dict[Edge, DyadicEdgeBound] = {}
    for edge, bound in bounds.items():
        if edge != bound.edge:
            raise ValueError("bound edge must match its mapping key")
        result[edge] = dyadic_edge_bound(bound)
    return result


def dyadic_stopping_epoch_bound(
    bounds: Mapping[Edge, EdgeStoppingComplexity],
) -> DyadicStoppingBound:
    """Return P49 positive or all-negative dyadic stopping bounds.

    Positive case: the first certifiable positive edge controls stopping, so we
    minimize over positive edges.

    All-negative case: every edge must be eliminated, so we maximize over the
    finite negative edge family.

    If there is no positive edge and at least one zero-margin edge, P48 already
    has no generic finite sign-gap bound and P49 correctly preserves that
    boundary.
    """
    if not bounds:
        raise ValueError("bounds must be nonempty")

    positive = [bound for bound in bounds.values() if bound.margin > 0.0]
    if positive:
        finite = [bound for bound in positive if bound.local_samples is not None]
        if len(finite) != len(positive):
            raise ValueError("positive-margin P48 bounds must be finite")
        selected = min(
            finite,
            key=lambda bound: first_dyadic_at_or_above(bound.local_samples or 1),
        )
        dyadic = first_dyadic_at_or_above(selected.local_samples or 1)
        controllers = tuple(
            bound.edge
            for bound in finite
            if first_dyadic_at_or_above(bound.local_samples or 1) == dyadic
        )
        p48 = min(bound.local_samples or 1 for bound in finite)
        return DyadicStoppingBound(
            status="positive-witness",
            p48_epochs=p48,
            dyadic_epochs=dyadic,
            certification_looks=dyadic.bit_length(),
            controlling_edges=controllers,
        )

    zeros = tuple(bound.edge for bound in bounds.values() if bound.margin == 0.0)
    if zeros:
        return DyadicStoppingBound(
            status="no-finite-sign-gap-bound",
            p48_epochs=None,
            dyadic_epochs=None,
            certification_looks=None,
            controlling_edges=zeros,
        )

    finite_negative = list(bounds.values())
    if any(bound.local_samples is None for bound in finite_negative):
        raise ValueError("strictly negative P48 bounds must be finite")
    p48 = max(bound.local_samples or 1 for bound in finite_negative)
    dyadic = max(
        first_dyadic_at_or_above(bound.local_samples or 1)
        for bound in finite_negative
    )
    controllers = tuple(
        bound.edge
        for bound in finite_negative
        if first_dyadic_at_or_above(bound.local_samples or 1) == dyadic
    )
    return DyadicStoppingBound(
        status="certified-no-positive-edge",
        p48_epochs=p48,
        dyadic_epochs=dyadic,
        certification_looks=dyadic.bit_length(),
        controlling_edges=controllers,
    )


def dyadic_overhead_ratio(samples: int) -> float:
    """Return dyadic threshold divided by the original P48 threshold."""
    if samples < 1:
        raise ValueError("samples must be a positive integer")
    return first_dyadic_at_or_above(samples) / samples


def logarithmic_look_bound(samples: int) -> int:
    """Return ``ceil(log2(samples)) + 1`` without floating-point ambiguity."""
    if samples < 1:
        raise ValueError("samples must be a positive integer")
    return first_dyadic_at_or_above(samples).bit_length()


def geometric_cost_upper_bound(
    p48_cost: float,
    p48_epochs: int,
    dyadic_epochs: int,
) -> float:
    """Scale a P48 full-family cost by the dyadic epoch overhead.

    When a cost bound is linear in the common epoch count, this returns the
    corresponding P49 dyadic cost upper bound.  The result is always strictly
    below twice the P48 bound when ``p48_epochs`` is positive and
    ``dyadic_epochs`` is the first power of two at or above it.
    """
    if not isfinite(p48_cost) or p48_cost < 0.0:
        raise ValueError("p48_cost must be nonnegative and finite")
    if p48_epochs < 1:
        raise ValueError("p48_epochs must be positive")
    if dyadic_epochs < p48_epochs:
        raise ValueError("dyadic_epochs cannot precede the P48 threshold")
    return p48_cost * dyadic_epochs / p48_epochs


def analytic_checkpoint_bound(samples: int) -> float:
    """Return the real-valued analytic look bound ``log2(samples) + 2``.

    For every positive integer threshold, the integer number of dyadic looks is
    strictly smaller than this quantity.  This helper is mainly for figures and
    reporting.
    """
    if samples < 1:
        raise ValueError("samples must be a positive integer")
    return log2(samples) + 2.0
