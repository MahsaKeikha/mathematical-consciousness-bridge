# Proposition 63: exact heterogeneous-cost integer transition calibration

## Status

**Proved exact pseudo-polynomial discrete optimization theorem.** P62 gives the unique continuous transition-calibration allocation when different transition measurements have different positive costs. P63 converts that model to executable whole-measurement counts when costs and the total budget are positive integers.

The key point is structural: P61's largest-marginal-gain rule is exact only because every additional measurement consumes the same unit of budget. Once measurement costs differ, comparing marginal uncertainty reductions alone is not enough. P63 therefore uses an exact Bellman dynamic program rather than extending the equal-cost greedy proof beyond its valid assumptions.

---

## 1. Integer heterogeneous-cost problem

For every calibrated transition edge \(e\), define

\[
b_e=w_ea_e>0
\]

as in P59-P62, and let

\[
c_e\in\{1,2,3,\ldots\}
\]

be the integer cost of one additional calibration observation.

Choose whole measurement counts

\[
k_e\in\{1,2,3,\ldots\}
\]

under a hard integer budget

\[
B\in\{1,2,3,\ldots\}.
\]

P63 solves

\[
\boxed{
\min_k
U(k)=\sum_{e\in E}\frac{b_e}{\sqrt{k_e}}
}
\]

subject to

\[
\boxed{
\sum_{e\in E}c_ek_e\le B,
\qquad
k_e\ge1\text{ integer}.
}
\]

The problem is feasible exactly when

\[
\boxed{
B\ge\sum_ec_e.
}
\]

---

## 2. Why P61 greedy cannot simply be reused

Under P61, every new measurement costs one budget unit. Selecting the largest currently available uncertainty reduction is therefore equivalent to selecting the best gain per identical unit.

Under P63, one candidate measurement can cost \(2\) units while another costs \(7\). The raw marginal gains

\[
\Delta_e(k)
=
b_e\left(k^{-1/2}-(k+1)^{-1/2}\right)
\]

are no longer directly comparable as interchangeable choices because they consume different amounts of the constrained resource.

Even ranking by \(\Delta_e(k)/c_e\) does not inherit P61's exchange proof: choosing one expensive increment can prevent a different combination of cheaper increments from fitting inside the remaining budget.

P63 therefore does not claim a greedy theorem where none has been proved.

---

## 3. Exact-spend Bellman states

Order the calibrated edges as

\[
e_1,\ldots,e_m.
\]

For

\[
i\in\{0,1,\ldots,m\}
\]

and integer spend

\[
s\in\{0,1,\ldots,B\},
\]

define

\[
F_i(s)
\]

as the minimum uncertainty contributed by the first \(i\) edges among allocations whose **exact** total cost is \(s\).

Initialize

\[
\boxed{
F_0(0)=0,
\qquad
F_0(s)=+\infty\quad(s>0).
}
\]

---

## 4. Proposition 63A: exact Bellman recurrence

For \(i\ge1\),

\[
\boxed{
F_i(s)
=
\min_{\substack{k\ge1\\c_{e_i}k\le s}}
\left[
F_{i-1}(s-c_{e_i}k)
+
\frac{b_{e_i}}{\sqrt{k}}
\right].
}
\]

The exact P63 optimum is

\[
\boxed{
U_{\rm int}^*(B)
=
\min_{0\le s\le B}F_m(s).
}
\]

The minimizing predecessor states reconstruct an exact optimal integer allocation.

### Proof

Take any feasible allocation for the first \(i\) edges with exact total spend \(s\). Suppose its count on edge \(e_i\) is \(k\). Then the first \(i-1\) edges spend exactly

\[
s-c_{e_i}k.
\]

By definition, their uncertainty cannot be smaller than

\[
F_{i-1}(s-c_{e_i}k).
\]

Therefore every feasible allocation at state \((i,s)\) has value at least the right-hand side of the recurrence for its chosen \(k\), hence at least the displayed minimum.

Conversely, every finite predecessor state combined with its candidate integer \(k\ge1\) is a feasible allocation for the first \(i\) edges with exact spend \(s\). Thus every term admitted by the recurrence is achievable.

The recurrence is therefore exact. Induction over \(i\) proves that all Bellman states are exact, and minimizing the final exact-spend states over \(s\le B\) yields the hard-budget optimum. \(\square\)

---

## 5. Proposition 63B: gcd budget compression

Let

\[
g=\gcd(c_{e_1},\ldots,c_{e_m}).
\]

Every feasible total spend is a multiple of \(g\). Therefore define

\[
\widetilde c_e=\frac{c_e}{g}
\]

and

\[
\widetilde B=\left\lfloor\frac Bg\right\rfloor.
\]

Then the original allocation problem is exactly equivalent to the scaled integer problem

\[
\sum_e\widetilde c_ek_e\le\widetilde B.
\]

Any remainder

\[
B-g\widetilde B<g
\]

is unusable under the declared cost lattice and therefore cannot change the optimum.

This compression is exact, not approximate.

---

## 6. Proposition 63C: pseudo-polynomial exact complexity

Let

\[
B'=\left\lfloor\frac Bg\right\rfloor
\]

and

\[
c'_{\min}=\min_e\widetilde c_e.
\]

A direct implementation examines at most \(B'+1\) predecessor spend states for each edge and, from any predecessor, at most

\[
\left\lfloor\frac{B'}{c'_{\min}}\right\rfloor
\]

candidate counts.

Hence a valid worst-case bound for the straightforward Bellman implementation is

\[
\boxed{
O\left(
 m B'\frac{B'}{c'_{\min}}
\right).
}
\]

Since \(c'_{\min}\ge1\), this is also

\[
\boxed{O(mB'^2).}
\]

The objective-value arrays require

\[
O(B')
\]

working memory. Reconstructing an optimal allocation additionally requires predecessor information across the processed edge layers.

The running time is polynomial in the **numeric budget** \(B'\), not necessarily in the bit length of \(B'\). That is why P63 is described as pseudo-polynomial rather than polynomial-time in the standard binary-input sense.

P63 does not infer an NP-hardness classification from this fact alone.

---

## 7. Proposition 63D: P62 provides a rigorous lower bound

P62 allows arbitrary positive real counts \(n_e>0\) and therefore optimizes over a superset of the P63 feasible integer allocations.

Let

\[
U_{\rm cont}^*(B)
\]

be the P62 continuous optimum under the same coefficients, costs, and total budget.

Then

\[
\boxed{
U_{\rm cont}^*(B)
\le
U_{\rm int}^*(B).
}
\]

Thus the exact P63 solution comes with a directly computable additive integrality gap

\[
\boxed{
G_{\rm add}
=
U_{\rm int}^*(B)-U_{\rm cont}^*(B)
\ge0,
}
\]

and multiplicative gap

\[
\boxed{
G_{\rm mult}
=
\frac{U_{\rm int}^*(B)}{U_{\rm cont}^*(B)}
\ge1.
}
\]

These are instance-specific certificates. No universal small-gap claim is made.

---

## 8. Unspent budget is legitimate

Because costs are discrete and heterogeneous, an optimal allocation need not spend every last budget unit.

For example, if all feasible increments cost an even number of units and the total budget is odd, one unit can never be used.

P63 therefore solves

\[
\sum_ec_ek_e\le B
\]

rather than artificially forcing equality.

Since every objective term decreases when \(k_e\) increases, any unspent amount at an optimum must be too small, or have the wrong arithmetic structure, to fund another admissible increment without violating the budget.

---

## 9. Equal-cost special case

If

\[
c_e=c
\qquad\forall e,
\]

then after scaling by \(g=c\), every additional observation consumes one common scaled budget unit.

The P63 dynamic program remains exact, but the stronger P61 diminishing-return theorem becomes available and gives a much faster exact priority-queue solution.

Thus

\[
\boxed{
\text{P61 is the efficient equal-cost specialization of the P63 discrete problem.}
}
\]

P63 is needed because that equal-cost exchange structure disappears when costs differ.

---

## 10. Complete calibration chain

The calibration branch now has a clean continuous/discrete hierarchy:

\[
\boxed{
\begin{array}{c}
\text{P58: finite-data transition uncertainty}\\
\Downarrow\\
\text{P59: equal-cost continuous optimum}\\
\Downarrow\\
\text{P60: certified equal-cost integer rounding}\\
\Downarrow\\
\text{P61: exact equal-cost integer optimum}\\
\Downarrow\\
\text{P62: heterogeneous-cost continuous optimum}\\
\Downarrow\\
\text{P63: exact heterogeneous-cost integer dynamic program.}
\end{array}
}
\]

This sequence makes the assumptions progressively more realistic without silently carrying an optimization theorem beyond the conditions under which it was proved.

---

## 11. What P63 does not establish

P63 does not establish:

1. a strongly polynomial algorithm for arbitrary binary-encoded budgets;
2. NP-hardness or NP-completeness of the heterogeneous integer problem;
3. that a gain-per-cost greedy rule is exact;
4. a universal approximation ratio between the P62 and P63 optima;
5. validity for noninteger transition costs without a declared discretization;
6. validity of the underlying P58 uncertainty model;
7. optimality for the full robust-route uncertainty rather than the declared separable surrogate;
8. any statement about consciousness, subjective experience, quantum incompleteness, or extra physical dimensions.

---

## 12. Next theorem target

P63 gives an exact solver whose complexity grows with the numeric budget. The next useful question is whether the same heterogeneous integer problem admits a faster approximation scheme with a rigorous error guarantee when \(B\) is large.

A natural P64 target is therefore a certified approximation algorithm or discretization theorem that compares a computationally cheaper solution against the exact P63 optimum while preserving an explicit uncertainty-loss bound.

Such a result would move the calibration branch from exact small-to-moderate budget optimization toward scalable experimental design without giving up quantitative certification.

---

## 13. Reproducibility

Implementation:
[`exact_heterogeneous_integer_calibration.py`](../src/consciousness_bridge/exact_heterogeneous_integer_calibration.py)

Regression tests:
[`test_exact_heterogeneous_integer_calibration.py`](../tests/test_exact_heterogeneous_integer_calibration.py)

Theorem visual:
[`p63_exact_heterogeneous_integer_calibration.svg`](figures/p63_exact_heterogeneous_integer_calibration.svg)

---

## 14. Scientific boundary

P63 is an exact discrete resource-allocation theorem for an experimental calibration surrogate. Its purpose is to make the measurement design supporting the broader physical-to-experiential research program executable under unequal real-world costs. It does not itself provide a bridge from physical description to experience and makes no claim that consciousness has been mathematically derived or that quantum mechanics is incomplete.
