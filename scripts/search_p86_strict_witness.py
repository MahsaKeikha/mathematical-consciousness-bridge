"""Deterministically search for an exact P86 witness that improves complete P85.

The search mirrors the finite seeded rational-box strategy used for P85, but the
acceptance condition is deliberately stronger: the best exact P86 four-event
functional must exceed the repository's complete P85 lower bound on the same
box and empirical law.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from random import Random

from consciousness_bridge.certified_continuous_model_separation import P78ParameterBox
from consciousness_bridge.quadruple_projection_parity_functional_separation import (
    p75_box_quadruple_parity_witness_exact,
)
from consciousness_bridge.triple_projection_parity_functional_separation import (
    p75_box_p85_linf_lower_bound_exact,
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
    rng = Random(20260913)
    for iteration in range(1, 1001):
        box = random_box(rng)
        empirical = random_empirical_law(rng)
        p85 = p75_box_p85_linf_lower_bound_exact(empirical, box)
        witness = p75_box_quadruple_parity_witness_exact(empirical, box)
        if witness.lower_bound <= p85:
            continue

        print("FOUND_P86_STRICT_WITNESS")
        print(f"iteration={iteration}")
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
        print(f"p85_bound={p85!r}")
        print(f"terms={witness.terms!r}")
        print(f"empirical_value={witness.empirical_value!r}")
        print(f"interval=({witness.interval_lower!r}, {witness.interval_upper!r})")
        print(f"gap={witness.interval_gap!r}")
        print(f"norm={witness.centered_coefficient_norm!r}")
        print(f"center={witness.centering_constant!r}")
        print(f"p86_quadruple_bound={witness.lower_bound!r}")
        print(f"strict_gain={witness.lower_bound - p85!r}")
        return

    raise RuntimeError("no strict complete-P85 to P86 witness found in seeded search")


if __name__ == "__main__":
    main()
