# Proposition 64: fast certified heterogeneous-cost integer approximation

## Status

**Proved scalable approximation theorem.** P63 computes the exact heterogeneous-cost whole-measurement optimum by dynamic programming, but its running time grows with the numeric budget. P64 gives a much cheaper certified alternative in the regime where the P62 continuous optimum already assigns at least one measurement to every calibrated transition.

P64 does not claim an FPTAS, does not claim exactness, and does not replace P63 in small-sample regimes where some continuous allocation falls below one. Its purpose is to provide an auditable fast approximation with an explicit instance-specific multiplicative guarantee.

---

## 1. Setup

Use the P62 continuous problem

\[
\min_{n_e>0}
\sum_e\frac{b_e}{\sqrt{n_e}}
\quad\text{subject to}\quad
\sum_ec_en_e=B,
\]

with unique optimum

\[
n_e^*.
\]

Use the P63 integer problem

\[
\min_{k_e\in\{1,2,3,\ldots\}}
\sum_e\frac{b_e}{\sqrt{k_e}}
\quad\text{subject to}\quad
\sum_ec_ek_e\le B.
\]

Let

\[
U_{\rm cont}^*(B)
\]

and

\[
U_{\rm int}^*(B)
\]

denote the P62 and P63 optima respectively.

Since the integer feasible set is contained in the continuous feasible set,

\[
\boxed{U_{\rm cont}^*(B)\le U_{\rm int}^*(B).}
\]

---

## 2. P64 floor construction

Assume

\[
\boxed{n_e^*\ge1\quad\forall e.}
\]

Define the integer allocation

\[
\boxed{k_e^{\rm floor}=\lfloor n_e^*\rfloor.}
\]

Because each \(k_e^{\rm floor}\ge1\), the design is a valid whole-measurement allocation.

Also

\[
k_e^{\rm floor}\le n_e^*,
\]

so

\[
\sum_ec_ek_e^{\rm floor}
\le
\sum_ec_en_e^*
=B.
\]

Therefore the P64 construction is always budget-feasible under its stated regime condition.

---

## 3. Proposition 64A: exact instance-specific approximation factor

Define

\[
\boxed{
r_e=
\frac{\lfloor n_e^*\rfloor}{n_e^*}
}
\]

and

\[
\boxed{
r_{\min}=\min_e r_e.}
\]

Under \(n_e^*\ge1\), every \(r_e>0\).

For each edge,

\[
\frac{b_e}{\sqrt{\lfloor n_e^*\rfloor}}
=
\frac{1}{\sqrt{r_e}}
\frac{b_e}{\sqrt{n_e^*}}
\le
\frac{1}{\sqrt{r_{\min}}}
\frac{b_e}{\sqrt{n_e^*}}.
\]

Summing gives

\[
\boxed{
U(k^{\rm floor})
\le
\frac{1}{\sqrt{r_{\min}}}
U_{\rm cont}^*(B).
}
\]

Using the P62 lower bound on the P63 integer optimum,

\[
U_{\rm cont}^*(B)\le U_{\rm int}^*(B),
\]

we obtain

\[
\boxed{
U(k^{\rm floor})
\le
\frac{1}{\sqrt{r_{\min}}}
U_{\rm int}^*(B).
}
\]

Thus

\[
\boxed{
\frac{U(k^{\rm floor})}{U_{\rm int}^*(B)}
\le
\frac{1}{\sqrt{r_{\min}}}.
}
\]

This is an **instance-specific certified approximation ratio** computable directly from the P62 continuous solution.

---

## 4. Proposition 64B: uniform factor from a minimum continuous count

Suppose a stronger lower bound is known:

\[
\boxed{n_e^*\ge\nu>1\quad\forall e.}
\]

Since

\[
\lfloor n_e^*\rfloor
\ge
n_e^*-1,
\]

and

\[
n_e^*-1
\ge
\left(1-\frac1\nu\right)n_e^*,
\]

we have

\[
r_e
\ge
1-\frac1\nu.
\]

Therefore

\[
\boxed{
U(k^{\rm floor})
\le
\sqrt{\frac{\nu}{\nu-1}}
U_{\rm int}^*(B).
}
\]

This gives a simple budget-regime guarantee that does not require inspecting every individual floor ratio.

Examples:

- if every \(n_e^*\ge2\), the factor is at most \(\sqrt2\);
- if every \(n_e^*\ge4\), the factor is at most \(\sqrt{4/3}\approx1.155\);
- if every \(n_e^*\ge10\), the factor is at most \(\sqrt{10/9}\approx1.054\).

As the continuous allocations become large, the guarantee approaches one.

---

## 5. Why the approximation improves with budget

Under P62,

\[
n_e^*
=
\frac{B}{T}
b_e^{2/3}c_e^{-2/3}.
\]

For fixed edge coefficients and costs, every continuous allocation grows linearly with total budget \(B\).

Therefore

\[
\min_e n_e^*
\longrightarrow\infty
\qquad\text{as }B\to\infty.
\]

Consequently

\[
r_{\min}\longrightarrow1
\]

and the P64 approximation factor satisfies

\[
\boxed{
\frac1{\sqrt{r_{\min}}}
\longrightarrow1.
}
\]

So the simple floor construction is asymptotically exact in multiplicative objective value for fixed problem data as the calibration budget grows.

This is not a statement that the integer allocation vector itself converges uniquely to a particular rounded pattern; it is a statement about objective quality.

---

## 6. Proposition 64C: explicit budget threshold for entering the certified regime

P62 gives

\[
n_e^*
=
\frac{B}{T}b_e^{2/3}c_e^{-2/3}.
\]

To ensure

\[
n_e^*\ge\nu
\quad\forall e,
\]

it is sufficient and necessary for the P62 formula that

\[
B
\ge
\nu T
\max_e
\left(
\frac{c_e}{b_e}
\right)^{2/3}.
\]

Thus define

\[
\boxed{
B_{\nu}
=
\nu T
\max_e
\left(
\frac{c_e}{b_e}
\right)^{2/3}.
}
\]

Whenever

\[
B\ge B_{\nu},
\]

the uniform P64 approximation factor

\[
\sqrt{\frac\nu{\nu-1}}
\]

is guaranteed.

Equivalently, for a desired multiplicative factor \(1+\varepsilon>1\), solve

\[
\sqrt{\frac\nu{\nu-1}}
\le1+\varepsilon.
\]

This is equivalent to

\[
\boxed{
\nu
\ge
\frac{(1+\varepsilon)^2}
{(1+\varepsilon)^2-1}.
}
\]

Combining this with \(B_{\nu}\) yields an explicit sufficient budget for a desired approximation factor within the P64 regime.

This is a **problem-dependent budget guarantee**, not a standard FPTAS complexity theorem.

---

## 7. Computational cost

P62's closed-form solution is computed in one pass over the edges. Flooring is another one-pass operation.

Therefore, once the coefficients are available, the P64 construction requires

\[
\boxed{O(m)}
\]

arithmetic operations for \(m\) calibrated edges, ignoring ordinary finite-precision arithmetic costs.

This is fundamentally different from P63's exact dynamic program, whose straightforward running time grows pseudo-polynomially with the numeric budget.

P64 therefore provides a useful tradeoff:

\[
\boxed{
\text{exactness from P63}
\quad\text{versus}\quad
\text{speed + certified approximation from P64}.
}
\]

---

## 8. Unspent budget can only help

The floor allocation may leave some budget unused.

Any subsequent procedure that adds additional feasible measurements without removing existing ones can only decrease

\[
U(k)=\sum_e\frac{b_e}{\sqrt{k_e}}.
\]

Therefore the P64 factor remains valid after any such feasible budget-filling improvement.

P64 does not claim that a particular unequal-cost leftover-budget heuristic is optimal. The theorem only needs the initial floor allocation; any later feasible additions improve its objective and preserve the certificate.

---

## 9. When P64 must not be used

If some P62 allocation satisfies

\[
n_e^*<1,
\]

then

\[
\lfloor n_e^*\rfloor=0,
\]

which violates the P63 requirement of at least one calibration observation per edge.

P64 therefore **fails explicitly** in this regime rather than silently replacing zero by one and claiming the same proof.

The appropriate choices are then:

1. use the exact P63 dynamic program;
2. increase the calibration budget until the P64 regime is entered; or
3. derive a separate baseline-constrained approximation theorem.

This explicit failure mode is part of the scientific validity of the result.

---

## 10. P62-P64 hierarchy

The unequal-cost branch now separates three distinct questions:

\[
\boxed{
\begin{array}{c}
\text{P62: what is the ideal continuous allocation?}\\
\Downarrow\\
\text{P63: what is the exact executable integer allocation?}\\
\Downarrow\\
\text{P64: when can we get a fast certified near-optimal integer allocation?}
\end{array}
}
\]

P62 gives a lower benchmark.

P63 gives exact discrete truth for the declared surrogate.

P64 gives scalable certified approximation when the continuous design is already away from the one-measurement boundary.

---

## 11. What P64 does not establish

P64 does not establish:

1. an FPTAS in the formal complexity-theoretic sense;
2. a guarantee when some \(n_e^*<1\);
3. exact optimality of simple flooring;
4. exact optimality of any leftover-budget heuristic under unequal costs;
5. a guarantee for the full robust-route objective instead of the declared separable surrogate;
6. validity of the P58 measurement-noise model;
7. any physical, quantum-ontological, or experiential conclusion.

---

## 12. Next theorem target

P64's limitation is now sharply identified: its proof requires the continuous optimum to allocate at least one sample to every edge.

The next natural theorem should remove that regime restriction by solving the continuous problem **with lower bounds**

\[
n_e\ge1
\]

before rounding. That leads to an active-set or water-filling structure in which some edges are pinned at the one-measurement boundary while the remaining budget is optimally distributed over the free edges.

A P65 target is therefore:

\[
\boxed{
\text{lower-bounded heterogeneous continuous calibration}
\longrightarrow
\text{baseline-safe scalable integer approximation}.
}
\]

---

## 13. Reproducibility

Implementation:
[`fast_heterogeneous_integer_approximation.py`](../src/consciousness_bridge/fast_heterogeneous_integer_approximation.py)

Regression tests:
[`test_fast_heterogeneous_integer_approximation.py`](../tests/test_fast_heterogeneous_integer_approximation.py)

Theorem visual:
[`p64_fast_heterogeneous_integer_approximation.svg`](figures/p64_fast_heterogeneous_integer_approximation.svg)

---

## 14. Scientific boundary

P64 is a computational approximation theorem for an experimental calibration surrogate. It improves the scalability of measurement planning supporting the broader repository. It does not itself bridge physics to subjective experience, does not identify consciousness with any physical quantity, and makes no claim that quantum mechanics is incomplete.
