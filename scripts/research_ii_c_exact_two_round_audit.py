"""Exact audit of the idealized two-fold e-process. No Monte Carlo and no external deps.

This checks only the Bernoulli aggregation example, not the P94-P99 witness.
"""
from fractions import Fraction
from math import comb

ALPHA = Fraction(1, 25)  # 0.04 per-fold null rejection bound
STAKE = Fraction(1, 2)
BOUNDARY = Fraction(20, 1)


def binomial_probability(k: int) -> Fraction:
    return Fraction(comb(2, k)) * ALPHA**k * (1 - ALPHA)**(2 - k)


def e_round(k: int) -> Fraction:
    return Fraction(k, 2) / ALPHA


def factor(k: int) -> Fraction:
    return 1 - STAKE + STAKE * e_round(k)


def main() -> None:
    expected_e = sum((binomial_probability(k) * e_round(k) for k in range(3)), Fraction(0))
    expected_factor = sum((binomial_probability(k) * factor(k) for k in range(3)), Fraction(0))
    two_round_crossing = sum(
        (binomial_probability(j) * binomial_probability(k)
         for j in range(3) for k in range(3) if factor(j) * factor(k) >= BOUNDARY),
        Fraction(0),
    )
    assert expected_e == 1
    assert expected_factor == 1
    assert factor(0) == Fraction(1, 2)
    assert factor(1) == Fraction(27, 4)
    assert factor(2) == 13
    assert factor(1)**2 == Fraction(729, 16)
    assert two_round_crossing == Fraction(38416, 6250000)
    assert two_round_crossing < Fraction(1, 20)
    print(f"E[E_round]={expected_e}; E[F_round]={expected_factor}")
    print(f"factors: {[str(factor(k)) for k in range(3)]}")
    print(f"two_round_crossing={two_round_crossing}={float(two_round_crossing):.8f}")
    print("These exact results assume independent Bernoulli(0.04) indicators.")


if __name__ == "__main__":
    main()
