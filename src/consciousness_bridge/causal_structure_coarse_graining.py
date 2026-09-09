"""Coarse-graining tools for Proposition 17.

The module studies deterministic pushforward of intervention-conditioned response laws
when physical or observational block granularity is reduced. It does not identify
coarse-graining with physical fusion or with any experiential change.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from typing import TypeVar

from consciousness_bridge.identifiability import total_variation_discrete

FineOutcome = TypeVar("FineOutcome", bound=Hashable)
CoarseOutcome = TypeVar("CoarseOutcome", bound=Hashable)
Intervention = TypeVar("Intervention", bound=Hashable)
Delay = TypeVar("Delay", bound=Hashable)


def pushforward_distribution(
    distribution: Mapping[FineOutcome, float],
    coarse_map: Mapping[FineOutcome, CoarseOutcome],
) -> dict[CoarseOutcome, float]:
    """Push a finite distribution through a deterministic coarse-graining map."""
    if not distribution:
        raise ValueError("Distribution must be nonempty.")
    if not set(distribution).issubset(coarse_map):
        raise ValueError("Coarse map must cover every observed fine outcome.")

    result: dict[CoarseOutcome, float] = {}
    for outcome, probability in distribution.items():
        coarse_outcome = coarse_map[outcome]
        result[coarse_outcome] = result.get(coarse_outcome, 0.0) + probability
    total_variation_discrete(result, result)
    return result


def pushforward_response_table(
    responses: Mapping[Intervention, Mapping[Delay, Mapping[FineOutcome, float]]],
    coarse_map: Mapping[FineOutcome, CoarseOutcome],
) -> dict[Intervention, dict[Delay, dict[CoarseOutcome, float]]]:
    """Push every intervention-delay response law through one coarse map."""
    if not responses:
        raise ValueError("Response table must be nonempty.")
    return {
        intervention: {
            delay: pushforward_distribution(distribution, coarse_map)
            for delay, distribution in delay_table.items()
        }
        for intervention, delay_table in responses.items()
    }


def pushforward_tv_pair(
    first: Mapping[FineOutcome, float],
    second: Mapping[FineOutcome, float],
    coarse_map: Mapping[FineOutcome, CoarseOutcome],
) -> tuple[float, float]:
    """Return fine and coarse TV distances for one declared coarse map."""
    fine_distance = total_variation_discrete(first, second)
    coarse_distance = total_variation_discrete(
        pushforward_distribution(first, coarse_map),
        pushforward_distribution(second, coarse_map),
    )
    return fine_distance, coarse_distance


def is_injective_on_observed_support(
    coarse_map: Mapping[FineOutcome, CoarseOutcome],
    observed_support: set[FineOutcome],
) -> bool:
    """Return whether the coarse map is injective on the declared observed support."""
    if not observed_support.issubset(coarse_map):
        raise ValueError("Coarse map must cover the declared observed support.")
    images = [coarse_map[outcome] for outcome in observed_support]
    return len(images) == len(set(images))


def collapsed_fiber_witness(
    coarse_map: Mapping[FineOutcome, CoarseOutcome],
) -> tuple[FineOutcome, FineOutcome] | None:
    """Return two distinct fine outcomes that collapse to the same coarse outcome."""
    representative: dict[CoarseOutcome, FineOutcome] = {}
    for fine_outcome, coarse_outcome in coarse_map.items():
        if coarse_outcome in representative:
            first = representative[coarse_outcome]
            if first != fine_outcome:
                return first, fine_outcome
        else:
            representative[coarse_outcome] = fine_outcome
    return None
