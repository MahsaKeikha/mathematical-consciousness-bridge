# Proposition 67: a Lagrangian certificate for unrestricted integer optimality

## 1. Purpose

P63 solves the heterogeneous-cost whole-measurement calibration problem exactly by a pseudo-polynomial dynamic program over the full budget. P65 provides a scalable baseline-safe floor construction. P66 then spends the residual budget exactly inside the class of integer allocations that componentwise dominate the P65 floor.

P67 asks a different question:

> When can a candidate integer allocation, including the output of P66, be certified as globally optimal for the unrestricted P63 problem without rerunning the full P63 dynamic program?

P67 gives a sufficient certificate based on one common Lagrange multiplier. The certificate is exact when it succeeds. Failure is inconclusive.

This proposition concerns the declared separable experimental-calibration surrogate. It is not a consciousness theorem and carries no quantum-ontological conclusion.

---

## 2. Integer calibration problem

Let the calibrated edge set be finite. For each edge \(e\), let

\[
b_e>0
\]

be its effective uncertainty coefficient and let

\[
c_e\in\mathbb Z_{>0}
\]

be its integer per-observation cost. The unrestricted P63 problem is

\[
\boxed{
U_{\mathrm{int}}^*(B)
=
\min_{k_e\in\mathbb Z_{\ge1}}
\sum_e\frac{b_e}{\sqrt{k_e}}
\quad
\text{subject to}
\quad
\sum_e c_e k_e\le B.
}
\]

For a candidate feasible allocation \(k\), define

\[
U(k)=\sum_e\frac{b_e}{\sqrt{k_e}}.
\]

---

## 3. Discrete marginal reductions

Define the reduction in the objective obtained by increasing edge \(e\) from \(j\) to \(j+1\) observations:

\[
\boxed{
\Delta_e(j)
=
b_e\left(\frac1{\sqrt j}-\frac1{\sqrt{j+1}}\right),
\qquad j\ge1.
}
\]

Because \(x\mapsto b_e x^{-1/2}\) is strictly convex and decreasing on \(x>0\), the sequence

\[
\Delta_e(1),\Delta_e(2),\ldots
\]

is strictly positive and strictly decreasing.

The cost-normalized marginal reduction is

\[
\boxed{
q_e(j)=\frac{\Delta_e(j)}{c_e}.
}
\]

It measures the objective reduction per unit cost associated with the next observation on edge \(e\).

---

## 4. One-edge Lagrangian problem

For a multiplier \(\lambda>0\), define the one-edge Lagrangian term

\[
\ell_e(j;\lambda)
=
\frac{b_e}{\sqrt j}+\lambda c_ej,
\qquad
j\in\mathbb Z_{\ge1}.
\]

The forward difference is

\[
\ell_e(j+1;\lambda)-\ell_e(j;\lambda)
=
-\Delta_e(j)+\lambda c_e.
\]

Therefore the sequence decreases while

\[
\Delta_e(j)>\lambda c_e
\]

and increases once

\[
\Delta_e(j)<\lambda c_e.
\]

Since the marginal reductions decrease strictly, a count \(k_e>1\) minimizes \(\ell_e(\cdot;\lambda)\) exactly when

\[
\boxed{
\frac{\Delta_e(k_e)}{c_e}
\le
\lambda
\le
\frac{\Delta_e(k_e-1)}{c_e}.
}
\]

For \(k_e=1\), there is no admissible decrement, so the exact condition is one-sided:

\[
\boxed{
\lambda
\ge
\frac{\Delta_e(1)}{c_e}.
}
\]

Define the edge interval

\[
I_e(k_e)=
\begin{cases}
[\Delta_e(k_e)/c_e,\,\Delta_e(k_e-1)/c_e], & k_e>1,\\[4pt]
[\Delta_e(1)/c_e,\,\infty), & k_e=1.
\end{cases}
\]

Then \(k_e\) is an exact minimizer of the one-edge Lagrangian term if and only if

\[
\lambda\in I_e(k_e).
\]

---

## 5. Proposition

Let \(k\) be any feasible positive-integer allocation satisfying the tight-budget condition

\[
\boxed{
\sum_e c_e k_e=B.
}
\]

Define

\[
\lambda_{\mathrm{low}}
=
\max_e \frac{\Delta_e(k_e)}{c_e}
\]

and

\[
\lambda_{\mathrm{high}}
=
\min_e
\begin{cases}
\Delta_e(k_e-1)/c_e, & k_e>1,\\
\infty, & k_e=1.
\end{cases}
\]

If

\[
\boxed{
\lambda_{\mathrm{low}}
\le
\lambda_{\mathrm{high}},
}
\]

then every

\[
\lambda\in
[\lambda_{\mathrm{low}},\lambda_{\mathrm{high}}]
\]

is a common multiplier for which every coordinate \(k_e\) minimizes its one-edge Lagrangian term. Consequently,

\[
\boxed{
U(k)=U_{\mathrm{int}}^*(B).
}
\]

Thus the candidate is globally optimal for the unrestricted P63 integer problem.

The certificate can be checked in \(O(m)\) time after the candidate allocation is available, where \(m\) is the number of calibrated edges.

---

## 6. Proof

Choose any common multiplier

\[
\lambda\in\bigcap_e I_e(k_e).
\]

By the one-edge result,

\[
\frac{b_e}{\sqrt{k_e}}+\lambda c_ek_e
\le
\frac{b_e}{\sqrt{j_e}}+\lambda c_ej_e
\]

for every positive integer \(j_e\). Summing over edges gives

\[
U(k)+\lambda\sum_ec_ek_e
\le
U(j)+\lambda\sum_ec_ej_e
\]

for every positive-integer allocation \(j\).

The candidate spends the budget exactly, so

\[
\sum_ec_ek_e=B.
\]

Any feasible competitor satisfies

\[
\sum_ec_ej_e\le B.
\]

Therefore

\[
U(k)+\lambda B
\le
U(j)+\lambda\sum_ec_ej_e
\le
U(j)+\lambda B.
\]

Subtracting \(\lambda B\) gives

\[
\boxed{U(k)\le U(j)}
\]

for every feasible positive-integer competitor \(j\). Hence \(k\) is a global optimum of the unrestricted P63 problem.

No relaxation gap assumption is used. The proof works directly on the integer coordinate domains.

---

## 7. Why the certificate is useful after P66

P66 returns the exact optimizer within

\[
\mathcal K_f
=
\{k\in\mathbb Z_{\ge1}^m:k_e\ge f_e,\ c^\top k\le B\},
\]

where \(f\) is the P65 floor.

P67 can be applied directly to that output.

If the P66 solution spends the entire budget and its edge intervals intersect, then P67 upgrades the status from

> exact inside the P65 floor-dominating class

to

> globally exact for the unrestricted P63 integer problem.

This upgrade requires no full-budget P63 dynamic program.

If the P67 certificate fails, the P66 guarantee remains unchanged. The candidate is still exact within its restricted class and still carries the P66 approximation certificate.

---

## 8. Why failure is inconclusive

P67 is a sufficient certificate, not a necessary characterization of all global integer optima.

There are two important failure modes.

### 8.1 Slack budget

A globally optimal integer allocation can leave unused budget if the remaining amount is smaller than every affordable next increment. The present P67 proof uses a positive Lagrange multiplier together with exact budget tightness, so such an optimum may fail the certificate.

Therefore

\[
\boxed{
\text{not certified by P67}
\not\Rightarrow
\text{suboptimal}.
}
\]

### 8.2 Empty common multiplier intersection

Integer knapsack-type problems can have a duality gap for a simple one-multiplier Lagrangian relaxation. A globally optimal allocation can therefore fail to admit a common multiplier satisfying every coordinate interval.

Again, failure means only that this particular certificate did not prove global optimality.

---

## 9. Relation to P61

For equal unit costs, the cost-normalized marginal reductions reduce to the ordinary marginal reductions used in P61.

P61 proves global optimality constructively by repeatedly assigning the next unit-cost observation to the largest available marginal reduction. P67 instead certifies a completed allocation by checking whether a common threshold separates every chosen last increment from every unchosen next increment.

Thus P67 recovers the familiar marginal-threshold structure in the equal-cost case while remaining valid as a sufficient certificate for heterogeneous integer costs.

---

## 10. Computational form

For a candidate \(k\), compute for every edge

\[
L_e=\frac{\Delta_e(k_e)}{c_e}
\]

and

\[
H_e=
\begin{cases}
\Delta_e(k_e-1)/c_e, & k_e>1,\\
\infty, & k_e=1.
\end{cases}
\]

Then

\[
\lambda_{\mathrm{low}}=\max_eL_e,
\qquad
\lambda_{\mathrm{high}}=\min_eH_e.
\]

The certificate succeeds exactly when

1. the candidate is feasible;
2. the candidate spends the full budget;
3. \(\lambda_{\mathrm{low}}\le\lambda_{\mathrm{high}}\).

A witness multiplier can be any point in that interval.

The implementation reports the interval for every edge, the global intersection, a witness multiplier when one exists, the budget-tightness status, and an explicit reason string.

---

## 11. What P67 establishes

P67 establishes:

1. an exact one-edge multiplier interval for each candidate integer count;
2. an \(O(m)\) common-multiplier test;
3. a sufficient unrestricted global-optimality theorem under budget tightness;
4. a direct route for upgrading a P66 restricted-exact solution to a P63 unrestricted global optimum when the certificate succeeds;
5. an explicit inconclusive status when the sufficient conditions fail.

---

## 12. What P67 does not establish

P67 does not establish:

1. that every P66 output is globally optimal;
2. that every P63 global optimum must satisfy the P67 certificate;
3. that certificate failure implies suboptimality;
4. that a slack-budget optimum cannot be globally optimal;
5. elimination of the pseudo-polynomial P63 solver for all instances;
6. an FPTAS or PTAS result;
7. optimality for the full robust-routing problem rather than the declared separable calibration surrogate;
8. any identification of a calibration variable with consciousness;
9. any claim that consciousness is quantum, an extra spacetime dimension, or evidence that quantum mechanics is incomplete.

---

## 13. Reproducibility

Implementation:
[`global_integer_optimality_certificate.py`](../src/consciousness_bridge/global_integer_optimality_certificate.py)

Regression tests:
[`test_global_integer_optimality_certificate.py`](../tests/test_global_integer_optimality_certificate.py)

The theorem visual will be maintained alongside the proposition as
[`p67_global_integer_optimality_certificate.svg`](figures/p67_global_integer_optimality_certificate.svg).

---

## 14. Next research target

P67 gives an inexpensive exact certificate when a common integer Lagrangian threshold exists. The next mathematical target is to strengthen certification in the cases P67 leaves inconclusive.

A natural direction is a bounded exchange certificate that permits coordinated downward and upward reallocations around the P66 solution and proves global optimality under a wider class of integer-cost instances without reverting immediately to the full P63 budget axis.

Any extension must keep separate:

- sufficient global-optimality certificates;
- exact algorithms;
- approximation guarantees;
- empirical heuristics.

---

## 15. Scientific boundary

P67 is a resource-allocation theorem for experimental calibration. It strengthens the executable design layer supporting the repository's broader physical-sufficiency and bridge-testing program. It does not itself provide a physical-to-experiential bridge, does not identify consciousness with any physical or information-theoretic quantity, and does not imply any incompleteness of quantum mechanics.
