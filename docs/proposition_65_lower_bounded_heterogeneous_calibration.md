# Proposition 65: lower-bounded heterogeneous calibration

## Status

**Proved lower-bounded continuous allocation theorem with a certified integer corollary.**

P64 gives a fast floor approximation only when the unconstrained P62 continuous optimum already assigns at least one observation to every calibrated edge. P65 removes that regime restriction by solving the continuous problem with the executable baseline constraint built into the optimization:

\[
n_e\ge 1.
\]

The resulting exact continuous solution has a thresholded water-filling form. Some edges can be pinned at one mandatory observation while the remaining budget is allocated optimally over the free edges. Flooring this lower-bounded optimum is therefore always baseline-safe and budget-feasible.

P65 then proves two approximation certificates for that floor construction:

\[
\frac{U(k^{\rm floor})}{U_{\rm int}^*(B)}
\le
\frac{1}{\sqrt{r_{\min}}}
\le
\sqrt 2.
\]

The first factor is instance-specific. The second is universal for the declared separable surrogate.

P65 does **not** claim that flooring is the exact P63 integer optimum. P63 remains the exact unequal-cost whole-measurement solver.

---

## 1. Setup

For every calibrated transition edge \(e\), let

\[
b_e=w_ea_e>0
\]

be the effective uncertainty coefficient and let

\[
c_e>0
\]

be the cost of one calibration observation.

The lower-bounded continuous problem is

\[
\boxed{
U_{\rm lb}^*(B)
=
\min_{n_e\ge1}
\sum_e\frac{b_e}{\sqrt{n_e}}
\quad\text{subject to}\quad
\sum_ec_en_e\le B.
}
\]

Define the mandatory baseline cost

\[
\boxed{
B_0=\sum_ec_e.
}
\]

The problem is feasible exactly when

\[
\boxed{B\ge B_0.}
\]

At \(B=B_0\), the only feasible allocation is

\[
n_e^*=1
\quad\forall e.
\]

For \(B>B_0\), the objective is strictly decreasing in every coordinate, so every optimum uses the full budget:

\[
\sum_ec_en_e^*=B.
\]

---

## 2. Strict convexity and uniqueness

For one edge,

\[
f_e(n)=b_en^{-1/2}.
\]

Its derivatives are

\[
f_e'(n)=-\frac{b_e}{2n^{3/2}},
\]

and

\[
f_e''(n)=\frac{3b_e}{4n^{5/2}}>0.
\]

Therefore each edge objective is strictly convex for \(n>0\), and

\[
U(n)=\sum_ef_e(n_e)
\]

is strictly convex on the feasible region.

The feasible set defined by the linear budget constraint and \(n_e\ge1\) is convex. Hence, whenever it is nonempty, the P65 optimum is unique.

---

## 3. KKT solution and water-filling form

For \(B>B_0\), introduce a multiplier \(\lambda>0\) for the tight budget and nonnegative multipliers \(\mu_e\ge0\) for the lower bounds \(n_e\ge1\).

The stationarity condition is

\[
-\frac{b_e}{2n_e^{3/2}}
+\lambda c_e
-\mu_e
=0.
\]

If edge \(e\) is **free**, then \(n_e>1\), so complementary slackness gives \(\mu_e=0\). Therefore

\[
\frac{b_e}{2n_e^{3/2}}=\lambda c_e,
\]

which yields

\[
n_e
=
\left(\frac{b_e}{2\lambda c_e}\right)^{2/3}.
\]

Define

\[
\boxed{
a_e=\left(\frac{b_e}{c_e}\right)^{2/3}}
\]

and

\[
\boxed{
\tau=(2\lambda)^{-2/3}.
}
\]

Then every free edge satisfies

\[
n_e=\tau a_e.
\]

If an edge would receive less than one under this free solution, its lower-bound constraint is active and it is pinned at one.

Therefore the unique optimum has the thresholded form

\[
\boxed{
n_e^*=\max\left\{1,\tau\left(\frac{b_e}{c_e}\right)^{2/3}\right\}.}
\]

The water level \(\tau\) is chosen so that

\[
\boxed{
\sum_ec_e
\max\left\{1,\tau\left(\frac{b_e}{c_e}\right)^{2/3}\right\}
=B.
}
\]

For \(B>B_0\), the left side is continuous and strictly increasing once the first edge is free. Hence the budget equation determines the relevant positive \(\tau\) uniquely at the optimum.

---

## 4. Exact active-set construction

Define each edge threshold

\[
\boxed{
t_e=\left(\frac{c_e}{b_e}\right)^{2/3}=\frac1{a_e}.}
\]

An edge is free exactly when

\[
\tau>t_e,
\]

with equality representing a boundary allocation of exactly one.

Sort the thresholds from smallest to largest. Starting from the smallest threshold, declare a prefix of edges free and the remaining edges pinned. For a proposed free set \(F\) and pinned set \(P\), the tight budget equation gives

\[
\boxed{
\tau_F
=
\frac{B-\sum_{e\in P}c_e}
{\sum_{e\in F}c_ea_e}.
}
\]

Expand the free prefix while \(\tau_F\) exceeds the next threshold. The first prefix satisfying the next-threshold condition is self-consistent and gives the unique KKT solution.

After sorting, the active-set scan is linear. Thus the implementation requires

\[
\boxed{O(m\log m)}
\]

comparison work for \(m\) edges, ignoring ordinary finite-precision arithmetic costs.

This complexity statement concerns the continuous P65 water-filling solver, not the pseudo-polynomial P63 integer dynamic program.

---

## 5. Relationship to P62

P62 solves the same continuous objective without the lower bounds \(n_e\ge1\). Its allocation is

\[
n_{e,\rm P62}^*
=
\frac{B}{T}
b_e^{2/3}c_e^{-2/3}.
\]

If the P62 solution already satisfies

\[
n_{e,\rm P62}^*\ge1
\quad\forall e,
\]

then no P65 lower bound is active. In that regime,

\[
\boxed{
n_{e,\rm P65}^*=n_{e,\rm P62}^*\quad\forall e.}
\]

Therefore P65 strictly extends the P62/P64 regime rather than replacing it with a different objective.

When some P62 counts are below one, P65 pins the appropriate low-priority or high-cost edges at the mandatory baseline and reoptimizes the remaining budget over the free edges.

---

## 6. Baseline-safe integer floor construction

Define

\[
\boxed{
k_e^{\rm floor}=\lfloor n_e^*\rfloor.}
\]

Because P65 enforces \(n_e^*\ge1\),

\[
k_e^{\rm floor}\ge1.
\]

Because

\[
k_e^{\rm floor}\le n_e^*,
\]

we also have

\[
\sum_ec_ek_e^{\rm floor}
\le
\sum_ec_en_e^*
\le B.
\]

Thus the P65 floor construction is always a valid P63-feasible integer allocation whenever \(B\ge B_0\).

This directly removes the failure mode identified in P64, where flooring an unconstrained P62 allocation below one would have produced an invalid zero count.

---

## 7. Instance-specific approximation certificate

Define

\[
\boxed{
r_e=\frac{\lfloor n_e^*\rfloor}{n_e^*}}
\]

and

\[
\boxed{
r_{\min}=\min_e r_e.}
\]

Since every \(n_e^*\ge1\), every \(r_e>0\).

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
U_{\rm lb}^*(B).
}
\]

The P63 integer-feasible set is a subset of the P65 lower-bounded continuous feasible set. Therefore

\[
\boxed{
U_{\rm lb}^*(B)
\le
U_{\rm int}^*(B).
}
\]

Combining the two inequalities gives

\[
\boxed{
U(k^{\rm floor})
\le
\frac{1}{\sqrt{r_{\min}}}
U_{\rm int}^*(B).
}
\]

This is a directly computable instance-specific certificate relative to the exact P63 optimum.

---

## 8. Universal square-root-of-two certificate

For every real \(x\ge1\),

\[
\boxed{\lfloor x\rfloor\ge\frac{x}{2}.}
\]

To verify it, split into two cases.

If \(1\le x<2\), then \(\lfloor x\rfloor=1\ge x/2\).

If \(x\ge2\), then

\[
\lfloor x\rfloor\ge x-1\ge x/2.
\]

Therefore

\[
r_e\ge\frac12
\quad\forall e,
\]

so

\[
\boxed{
r_{\min}\ge\frac12.}
\]

Hence

\[
\boxed{
U(k^{\rm floor})
\le
\sqrt2\,U_{\rm lb}^*(B)
\le
\sqrt2\,U_{\rm int}^*(B).
}
\]

Thus P65 supplies a baseline-safe, scalable integer allocation with a universal \(\sqrt2\) objective guarantee for every feasible instance of the declared separable problem.

The factor is a worst-case guarantee for this particular floor construction. P65 does not claim that \(\sqrt2\) is the best achievable approximation factor among all polynomial-time algorithms.

---

## 9. Sharper factors away from integer boundaries

The instance-specific factor

\[
\frac1{\sqrt{r_{\min}}}
\]

is usually sharper than \(\sqrt2\).

Pinned edges have

\[
n_e^*=1,
\qquad
r_e=1,
\]

so they do not worsen the approximation certificate.

If all non-pinned allocations are well above their next lower integer, the floor ratios approach one and the certificate approaches exact objective value.

For fixed problem data, sufficiently large budgets eventually move every edge away from the one-sample boundary and recover the large-budget P64 behavior.

---

## 10. What P65 solves that P64 could not

P64 required

\[
n_{e,\rm P62}^*\ge1
\quad\forall e.
\]

P65 instead incorporates the baseline into the optimization itself:

\[
\boxed{
n_e\ge1.}
\]

This changes the logic from

\[
\text{solve unconstrained continuous problem}
\to
\text{hope every count exceeds one}
\]

into

\[
\boxed{
\text{solve the correct lower-bounded continuous problem}
\to
\text{floor safely}
\to
\text{certify approximation quality}.
}
\]

The P62-P65 unequal-cost sequence is therefore

\[
\boxed{
\begin{array}{c}
\text{P62: unconstrained continuous optimum}\\
\Downarrow\\
\text{P63: exact unequal-cost integer optimum}\\
\Downarrow\\
\text{P64: fast flooring when P62 is already baseline-safe}\\
\Downarrow\\
\text{P65: lower-bounded water filling + baseline-safe flooring}
\end{array}
}
\]

---

## 11. Scientific interpretation

P65 is useful when every calibrated transition must receive at least one observation but the edge costs and uncertainty priorities differ strongly.

The theorem says that mandatory baseline observations should be treated as active constraints inside the optimization rather than patched in afterward. Edges whose marginal value is too small relative to their cost remain pinned at one observation. The remaining budget is distributed according to the same two-thirds-power structure as P62, but only across the free active set.

This is an experimental-design result. The coefficients \(b_e\), costs \(c_e\), and edge set must still be scientifically justified by the declared calibration problem.

---

## 12. What P65 does not establish

P65 does not establish:

1. exact optimality of the integer floor allocation;
2. a better-than-\(\sqrt2\) universal approximation theorem for every feasible instance;
3. an FPTAS or PTAS complexity result;
4. exact optimality of any leftover-budget filling heuristic;
5. validity of the P58 measurement-noise model itself;
6. optimality for the full robust-routing objective rather than the declared separable calibration surrogate;
7. any identification of a calibration variable with consciousness;
8. any claim that consciousness is quantum, an extra spacetime dimension, or evidence that quantum mechanics is incomplete.

---

## 13. Reproducibility

Implementation:
[`lower_bounded_heterogeneous_calibration.py`](../src/consciousness_bridge/lower_bounded_heterogeneous_calibration.py)

Regression tests:
[`test_lower_bounded_heterogeneous_calibration.py`](../tests/test_lower_bounded_heterogeneous_calibration.py)

The theorem visual is maintained alongside the proposition as
[`p65_lower_bounded_heterogeneous_calibration.svg`](figures/p65_lower_bounded_heterogeneous_calibration.svg).

---

## 14. Next research target

P65 makes a fast baseline-safe approximation available for every feasible instance of the declared separable unequal-cost problem. The next mathematical question is no longer basic feasibility.

A natural next target is to use the leftover budget after flooring more intelligently and prove whether a polynomial-time augmentation rule can improve the P65 universal certificate without reverting to the pseudo-polynomial P63 dynamic program.

Any such result should distinguish clearly between:

- an exact discrete theorem;
- an approximation-ratio theorem;
- an empirical heuristic that performs well but lacks a global guarantee.

---

## 15. Scientific boundary

P65 is a resource-allocation theorem for experimental calibration. It strengthens the executable design layer supporting the repository's broader physical-sufficiency and bridge-testing program. It does not itself provide a physical-to-experiential bridge, does not identify consciousness with any physical or information-theoretic quantity, and does not imply any incompleteness of quantum mechanics.
