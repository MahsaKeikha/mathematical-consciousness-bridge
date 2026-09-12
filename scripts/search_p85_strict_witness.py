"""Deterministically search for an exact P85 witness missed by complete P84.

This is a temporary research script. It searches a finite seeded family of
rational P75 boxes and sparse empirical laws using the repository's actual P84
and P85 implementations. It prints the first exact witness with P84 = 0 and a
positive P85 triple-functional bound.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from random import Random

from consciousness_bridge.certified_continuous_model_separation import P78ParameterBox
from consciousness_bridge.joint_projection_parity_contrast_separation import (
    p75_box_p84_linf_lower_bound_exact,
)
from consciousness_bridge.triple_projection_parity_functional_separation import (
    p75_box_triple_parity_witness_exact,
)

OUTCOMES = tuple(product((0, 1), repeat=4))
VALUES = (Fraction(0), Fraction(1, 2), Fraction(1))
INTERVALS = tuple(
    (lower, upper)
    for lower_index, lower in enumerate(VALUES)
    for upper in VALUES[lower_index:]
)


def random_box(rng: Random) -> P78ParameterBox:
    chosen = tuple(rng.choice(INTERVALS) for _ in range(9))
    return P78ParameterBox(
        lower=tuple(interval[0] for interval in chosen),
        upper=tuple(interval[1] for interval in chosen),
    )


def random_empirical_law(rng: Random) -> tuple[Fraction, ...]:
    support_size = rng.choice((2, 3, 4, 5, 6))
    support = rng.sample(range(16), support_size)
    counts = [0] * 16
    total = rng.choice((8, 12, 16))
    for _ in range(total):
        counts[rng.choice(support)] += 1
    return tuple(Fraction(count, total) for count in counts)


def main() -> None:
    rng = Random(20260912)
    p84_zero_count = 0
    for iteration in range(1, 20001):
        box = random_box(rng)
        empirical = random_empirical_law(rng)
        p84 = p75_box_p84_linf_lower_bound_exact(empirical, box)
        if p84 != 0:
            continue
        p84_zero_count += 1
        witness = p75_box_triple_parity_witness_exact(empirical, box)
        if witness.lower_bound <= 0:
            continue

        print("FOUND_P85_STRICT_WITNESS")
        print(f"iteration={iteration}")
        print(f"p84_zero_candidates={p84_zero_count}")
        print(f"lower={box.lower!r}")
        print(f"upper={box.upper!r}")
        print(
            "masses="
            + repr(
                tuple(
                    (outcome, mass)
                    for outcome, mass in zip(OUTCOMES, empirical, strict=True)
                    if mass
                )
            )
        )
        print(f"terms={witness.terms!r}")
        print(f"empirical_value={witness.empirical_value!r}")
        print(f"interval=({witness.interval_lower!r}, {witness.interval_upper!r})")
        print(f"gap={witness.interval_gap!r}")
        print(f"norm={witness.centered_coefficient_norm!r}")
        print(f"center={witness.centering_constant!r}")
        print(f"bound={witness.lower_bound!r}")
        return

    raise RuntimeError(
        "no strict P85 witness found in deterministic search; "
        f"P84-zero candidates checked={p84_zero_count}"
    )


if __name__ == "__main__":
    main()
