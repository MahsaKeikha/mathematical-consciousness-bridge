# Proposition 60: integer transition-calibration allocation with hard-budget overhead control

## Status

**Proved constructive integer-rounding theorem.** P59 gives the unique optimal continuous allocation for a declared inverse-square-root transition-calibration uncertainty surrogate. P60 converts that fractional design into whole measurement counts while respecting a hard integer budget and quantifying the worst-case loss relative to the P59 continuous optimum.

P60 is an implementation theorem for experimental resource allocation. It does not solve the full combinatorial robust-routing design problem, does not justify the sensitivity weights, and does not make a consciousness or quantum-incompleteness claim.

---

## 1. The continuous design that must be implemented

P59 considers positive edge coefficients

\[
b_e=w_ea_e>0
\]

and the uncertainty surrogate

\[
\boxed{
U(n)=\sum_{e\in E}\frac{b_e}{\sqrt{n_e}}
}
\]

under

\[
\sum_e n_e=N,
\qquad n_e>0.
\]

Writing

\[
S=\sum_e b_e^{2/3},
\]

the unique continuous optimum is

\[
\boxed{
n_e^*(N)=N\frac{b_e^{2/3}}{S}}
\]

with value

\[
\boxed{
U^*(N)=\frac{S^{3/2}}{\sqrt N}.
}
\]

Real experiments cannot generally take a fractional number of calibration measurements. P60 therefore asks for a constructive integer allocation.

---

## 2. Hard integer budget

Let

\[
m=|E|
\]

be the number of calibrated transition edges, and let

\[
B\in\mathbb N
\]

be a hard total integer budget satisfying

\[
\boxed{B>m.}
\]

Define the effective continuous budget

\[
\boxed{N_0=B-m.}
\]

Compute the P59 continuous optimum at budget \(N_0\):

\[
\widetilde n_e
=N_0\frac{b_e^{2/3}}{S}.
\]

Then choose the implementable integer allocation

\[
\boxed{k_e=\lceil\widetilde n_e\rceil.}
\]

---

## 3. Proposition 60A: the ceiling construction respects the hard budget

For every real \(x\),

\[
\lceil x\rceil<x+1.
\]

Therefore

\[
\sum_e k_e
<
\sum_e\widetilde n_e+m.
\]

But

\[
\sum_e\widetilde n_e=N_0=B-m.
\]

Hence

\[
\sum_e k_e<B.
\]

Because the left side is an integer,

\[
\boxed{
\sum_e k_e\le B-1<B.
}
\]

In particular,

\[
\boxed{
\sum_e k_e\le B.
}
\]

So the construction always respects the declared hard budget.

This leaves at least one unused unit under the strict \(B>m\) construction. That slack is a consequence of the conservative reserve of one potential rounding unit per calibrated edge.

---

## 4. Proposition 60B: rounding upward cannot worsen the surrogate

Every term

\[
b_en_e^{-1/2}
\]

is strictly decreasing in \(n_e\). Since

\[
k_e\ge\widetilde n_e,
\]

we have

\[
\frac{b_e}{\sqrt{k_e}}
\le
\frac{b_e}{\sqrt{\widetilde n_e}}.
\]

Summing over edges gives

\[
\boxed{
U(k)
\le
U^*(B-m).
}
\]

Using the P59 closed form,

\[
\boxed{
U(k)
\le
\frac{S^{3/2}}{\sqrt{B-m}}.
}
\]

This is a deterministic implementability guarantee. The integer design never performs worse than the continuous optimum evaluated at the deliberately reduced budget \(B-m\).

---

## 5. Proposition 60C: multiplicative overhead relative to the full-budget continuous optimum

The ideal continuous optimum using the entire hard budget \(B\) is

\[
U^*(B)=\frac{S^{3/2}}{\sqrt B}.
\]

Therefore

\[
\frac{U(k)}{U^*(B)}
\le
\frac{U^*(B-m)}{U^*(B)}.
\]

Substituting the closed form yields

\[
\boxed{
\frac{U(k)}{U^*(B)}
\le
\sqrt{\frac{B}{B-m}}.
}
\]

Equivalently,

\[
\boxed{
U(k)
\le
U^*(B)
\sqrt{\frac{B}{B-m}}.
}
\]

This gives a transparent finite-budget price for requiring whole calibration measurements.

---

## 6. The overhead vanishes at large budget

For fixed edge count \(m\),

\[
\sqrt{\frac{B}{B-m}}
=
\left(1-\frac mB\right)^{-1/2}.
\]

Thus

\[
\boxed{
\sqrt{\frac{B}{B-m}}\to1
\qquad\text{as }B\to\infty.
}
\]

So the conservative integer construction becomes asymptotically as efficient as the ideal continuous allocation when the total calibration budget is large compared with the number of calibrated edges.

For small \(m/B\), the expansion

\[
(1-x)^{-1/2}
=1+\frac{x}{2}+O(x^2)
\]

gives

\[
\boxed{
\frac{U(k)}{U^*(B)}
\lesssim
1+\frac{m}{2B}
}
\]

at first order.

This approximation is explanatory only. The exact certified bound remains the square-root ratio above.

---

## 7. Proposition 60D: sufficient integer budget for a target uncertainty

Suppose the experiment requires

\[
U(k)\le\varepsilon,
\qquad\varepsilon>0.
\]

P60B shows it is sufficient that

\[
U^*(B-m)
\le\varepsilon.
\]

Using P59,

\[
\frac{S^{3/2}}{\sqrt{B-m}}
\le\varepsilon
\]

whenever

\[
B-m
\ge
\frac{S^3}{\varepsilon^2}.
\]

Therefore the explicit hard integer budget

\[
\boxed{
B
=
m+\left\lceil\frac{S^3}{\varepsilon^2}\right\rceil
}
\]

is sufficient.

More generally,

\[
\boxed{
B
\ge
m+\left\lceil\frac{S^3}{\varepsilon^2}\right\rceil
}
\]

guarantees that the P60 construction attains the declared target uncertainty.

This separates two unavoidable design scales:

\[
\boxed{
\text{continuous statistical burden}
+
\text{finite integer implementation reserve}.
}
\]

---

## 8. Why this is a guarantee, not an exact integer optimum

P60 does **not** claim that

\[
k_e=\lceil n_e^*(B-m)\rceil
\]

is the globally optimal integer solution under total budget \(B\).

The exact integer program is

\[
\min_{k_e\in\mathbb N}
\sum_e\frac{b_e}{\sqrt{k_e}}
\quad\text{subject to}\quad
\sum_e k_e\le B.
\]

Because the objective is separable and decreasing, unused budget can generally be assigned to improve the P60 construction further. A discrete marginal-gain allocation algorithm can therefore sharpen the result.

P60 deliberately proves a simpler statement first: a closed-form, auditable integer construction whose budget feasibility and worst-case loss are explicit.

---

## 9. Relationship to P58 and P59

The calibration chain is now

\[
\boxed{
\begin{array}{c}
\text{P58: finite-data transition uncertainty}\\
\Downarrow\\
\text{P59: exact continuous calibration allocation}\\
\Downarrow\\
\text{P60: implementable integer allocation with overhead control.}
\end{array}
}
\]

P58 quantifies how uncertain measured transitions are.

P59 decides how an idealized divisible calibration budget should be distributed.

P60 converts that fractional design into whole measurement counts without violating a hard total budget.

---

## 10. Next theorem target

P60 leaves budget unused in some instances and does not claim exact integer optimality.

The next natural theorem is therefore to characterize the exact discrete optimum using marginal uncertainty reduction per additional calibration measurement.

For edge \(e\), the reduction obtained by increasing its integer count from \(k\) to \(k+1\) is

\[
\boxed{
\Delta_e(k)
=
b_e\left(
\frac1{\sqrt{k}}-
\frac1{\sqrt{k+1}}
\right).
}
\]

Because these marginal gains decrease with \(k\), a P61 target is to prove that allocating each remaining measurement to the currently largest marginal gain solves the exact integer resource-allocation problem.

That would close the continuous-to-integer calibration design chain exactly.

---

## 11. Reproducibility

Implementation:
[`integer_transition_calibration.py`](../src/consciousness_bridge/integer_transition_calibration.py)

Regression tests:
[`test_integer_transition_calibration.py`](../tests/test_integer_transition_calibration.py)

Theorem visual:
[`p60_integer_transition_calibration.svg`](figures/p60_integer_transition_calibration.svg)

---

## 12. Scientific boundary

P60 is a deterministic rounding and experimental-budget theorem. It does not establish that the P59 sensitivity weights are physically privileged, does not validate the P58 observation model, does not infer consciousness from a transition metric, and does not claim that quantum mechanics is incomplete.
