# Proposition 66: residual-exact augmentation of the P65 floor design

## Status

**Proved discrete optimization theorem inside a declared floor-dominating class.**

P66 strengthens the executable heterogeneous-cost calibration chain without changing the scientific boundary of the repository. It is a theorem about how to spend calibration resources under the separable uncertainty surrogate inherited from P58-P65. It is not a theorem about consciousness, subjective experience, quantum ontology, or the completeness of quantum mechanics.

---

## 1. Motivation

P65 solves the lower-bounded continuous calibration problem

\[
\min_{n_e\ge 1}
\sum_{e\in E}\frac{b_e}{\sqrt{n_e}}
\quad\text{subject to}\quad
\sum_{e\in E}c_en_e\le B,
\]

where

- \(b_e>0\) is the effective uncertainty-sensitivity coefficient for edge \(e\),
- \(c_e>0\) is its per-observation cost,
- \(B\) is the total calibration budget.

P65 proves that the unique continuous optimum has the thresholded water-filling form

\[
n_e^*=\max\left\{1,\tau\left(\frac{b_e}{c_e}\right)^{2/3}\right\}.
\]

It then gives a baseline-safe executable integer design by flooring:

\[
f_e=\lfloor n_e^*\rfloor.
\]

That construction is always feasible because \(n_e^*\ge1\), but it may leave some of the budget unused.

P66 asks:

> Can the leftover budget after P65 flooring be used optimally without returning to the full-budget P63 dynamic program?

The answer is yes, if the optimization target is stated precisely.

P66 solves the best integer allocation **among all allocations that componentwise dominate the P65 floor**. That restricted discrete problem is solved exactly on the residual budget only.

---

## 2. Setup

Assume throughout that

\[
b_e>0,
\qquad
c_e\in\{1,2,3,\ldots\},
\qquad
B\in\{1,2,3,\ldots\},
\]

and that the one-observation baseline is feasible:

\[
B\ge B_0,
\qquad
B_0:=\sum_{e\in E}c_e.
\]

Let \(n^*\) be the exact P65 lower-bounded continuous optimum and define

\[
f_e:=\lfloor n_e^*\rfloor.
\]

The P65 floor spend is

\[
B_f:=\sum_e c_ef_e,
\]

and the residual budget is

\[
R:=B-B_f.
\]

P66 introduces integer increments

\[
z_e\in\{0,1,2,\ldots\}
\]

and restricts attention to allocations

\[
k_e=f_e+z_e.
\]

The residual problem is therefore

\[
\boxed{
\min_{z_e\in\mathbb Z_{\ge0}}
\sum_e\frac{b_e}{\sqrt{f_e+z_e}}
\quad\text{subject to}\quad
\sum_ec_ez_e\le R.
}
\]

---

## 3. Residual-budget identity

### Proposition 66A

The residual budget satisfies

\[
\boxed{
R
=
\sum_e c_e\{n_e^*\}
<
\sum_e c_e
=
B_0,
}
\]

where \(\{x\}=x-\lfloor x\rfloor\) is the fractional part.

### Proof

P65's continuous optimum uses the available budget tightly whenever the problem is feasible. Hence

\[
B=\sum_ec_en_e^*.
\]

Subtract the floor spend:

\[
R
=
B-\sum_ec_e\lfloor n_e^*\rfloor
=
\sum_ec_e\left(n_e^*-\lfloor n_e^*\rfloor\right).
\]

Thus

\[
R=\sum_ec_e\{n_e^*\}.
\]

For every edge,

\[
0\le\{n_e^*\}<1.
\]

Since every \(c_e>0\),

\[
0\le R<\sum_ec_e=B_0.
\]

This proves the claim. \(\square\)

### Interpretation

The amount of budget discarded by naive flooring is bounded independently of the magnitude of the original budget. Even if \(B\) is extremely large, the residual is always smaller than one mandatory-observation baseline across all calibrated edges.

That is the key structural fact that makes P66 useful computationally.

---

## 4. Exact residual dynamic program

Order the edges as \(e_1,\ldots,e_m\). Let

\[
F_i(s)
\]

be the minimum objective contribution from the first \(i\) edges using exactly \(s\) units of residual budget.

Initialize

\[
F_0(0)=0,
\qquad
F_0(s)=+\infty\quad(s>0).
\]

For edge \(e_i\), the exact Bellman recurrence is

\[
\boxed{
F_i(s)
=
\min_{\substack{z\ge0\\c_{e_i}z\le s}}
\left[
F_{i-1}(s-c_{e_i}z)
+
\frac{b_{e_i}}{\sqrt{f_{e_i}+z}}
\right].
}
\]

The exact restricted optimum is

\[
\boxed{
U_{66}^*(B)
=
\min_{0\le s\le R}F_m(s).
}
\]

The minimizing predecessor chain reconstructs the exact increments \(z_e^*\), hence

\[
k_e^{66}=f_e+z_e^*.
\]

---

## 5. Exactness theorem inside the floor-dominating class

### Proposition 66B

The Bellman recurrence above returns the global minimum of

\[
U(k)=\sum_e\frac{b_e}{\sqrt{k_e}}
\]

over the restricted class

\[
\mathcal K_f(B)
:=
\left\{
 k\in\mathbb Z_{\ge1}^{|E|}:
 k_e\ge f_e\ \forall e,
 \sum_ec_ek_e\le B
\right\}.
\]

Equivalently,

\[
\boxed{
k^{66}\in\arg\min_{k\in\mathcal K_f(B)}U(k).}
\]

### Proof

Every \(k\in\mathcal K_f(B)\) can be written uniquely as

\[
k_e=f_e+z_e
\]

with \(z_e\in\mathbb Z_{\ge0}\). Its budget constraint becomes

\[
\sum_ec_ez_e
\le
B-\sum_ec_ef_e
=R.
\]

The objective is separable across edges once the increments are fixed. The Bellman state \(F_i(s)\) therefore satisfies the principle of optimality: any optimal allocation of exact residual spend \(s\) across the first \(i\) edges must use some increment \(z\) on edge \(e_i\), while the remaining exact spend \(s-c_{e_i}z\) must itself be optimally allocated across the first \(i-1\) edges.

The recurrence enumerates every feasible integer increment and hence every feasible member of \(\mathcal K_f(B)\). Taking the minimum over all exact residual spends \(s\le R\) gives the global restricted optimum. \(\square\)

---

## 6. Monotone improvement over P65

The zero-increment vector

\[
z_e=0\quad\forall e
\]

is feasible for the P66 residual problem. Therefore the P65 floor itself belongs to \(\mathcal K_f(B)\).

Hence

\[
\boxed{
U(k^{66})\le U(f).
}
\]

Define the exact residual improvement

\[
\Delta_{66}
:=
U(f)-U(k^{66}).
\]

Then

\[
\boxed{
\Delta_{66}\ge0.
}
\]

Whenever at least one affordable residual increment gives positive objective reduction, the inequality is strict.

Because every term \(b_e/\sqrt{k_e}\) strictly decreases with \(k_e\), any feasible positive increment strictly improves the objective.

---

## 7. Approximation certificate relative to P63

P63 solves the unrestricted heterogeneous-cost integer problem exactly:

\[
U_{\mathrm{int}}^*(B)
=
\min_{\substack{k_e\in\mathbb Z_{\ge1}\\\sum_ec_ek_e\le B}}
\sum_e\frac{b_e}{\sqrt{k_e}}.
\]

P66 does not claim that \(k^{66}\) always equals this unrestricted optimum.

Let

\[
r_{66}
:=
\min_e\frac{k_e^{66}}{n_e^*}.
\]

Since

\[
k_e^{66}\ge r_{66}n_e^*
\]

for every edge,

\[
\frac{b_e}{\sqrt{k_e^{66}}}
\le
\frac{1}{\sqrt{r_{66}}}
\frac{b_e}{\sqrt{n_e^*}}.
\]

Summing gives

\[
U(k^{66})
\le
\frac{1}{\sqrt{r_{66}}}U_{\mathrm{cont}}^*(B).
\]

Since the continuous optimum is a lower bound on the unrestricted integer optimum,

\[
U_{\mathrm{cont}}^*(B)\le U_{\mathrm{int}}^*(B),
\]

we obtain

\[
\boxed{
U(k^{66})
\le
\frac{1}{\sqrt{r_{66}}}
U_{\mathrm{int}}^*(B).
}
\]

This is a directly computable instance-specific certificate.

Because P66 only increases the P65 floor counts,

\[
r_{66}
\ge
r_{65}
:=
\min_e\frac{\lfloor n_e^*\rfloor}{n_e^*}.
\]

Therefore

\[
\boxed{
\frac{1}{\sqrt{r_{66}}}
\le
\frac{1}{\sqrt{r_{65}}}
\le
\sqrt2.
}
\]

Thus residual-exact augmentation can only improve or preserve the P65 approximation certificate.

The universal worst-case guarantee remains

\[
\boxed{
U(k^{66})\le\sqrt2\,U_{\mathrm{int}}^*(B).
}
\]

P66 does **not** claim a strictly better universal constant for every feasible instance.

---

## 8. GCD compression

Assume the costs are positive integers and define

\[
g:=\gcd\{c_e:e\in E\}.
\]

Every realizable residual spend is a multiple of \(g\). Therefore divide all costs by \(g\) and replace the residual budget by

\[
R':=\left\lfloor\frac{R}{g}\right\rfloor.
\]

This compression is exact, not approximate.

The straightforward Bellman implementation has pseudo-polynomial running time on the order of

\[
O\!\left(\frac{m(R')^2}{c'_{\min}}\right),
\]

with memory linear in \(R'\) for the current objective layer plus predecessor storage for reconstruction.

The important point is not that this is strongly polynomial. It is not.

The important structural result is

\[
R<B_0,
\]

so the dynamic-programming axis is controlled by the baseline cost rather than the potentially much larger full budget.

---

## 9. Relation to P62-P65

The heterogeneous calibration chain is now:

\[
\boxed{
\text{P62 continuous unequal-cost optimum}
\to
\text{P63 globally exact unequal-cost integer optimum}
\to
\text{P64 fast floor approximation in a large-count regime}
\to
\text{P65 baseline-safe lower-bounded floor approximation}
\to
\text{P66 residual-exact augmentation of that floor}.
}
\]

The roles are deliberately different.

- **P63** is globally exact over all positive integer allocations, but pseudo-polynomial in the full budget.
- **P65** is a fast baseline-safe continuous theorem plus floor approximation.
- **P66** is exact only after the P65 floor has been fixed as a componentwise lower bound, but its discrete optimization sees only the bounded residual budget.

This separation avoids calling a restricted exact result a globally exact integer theorem.

---

## 10. Edge cases

### Baseline-only budget

If

\[
B=B_0,
\]

then

\[
n_e^*=1,
\qquad
f_e=1,
\qquad
R=0.
\]

P66 returns the P65 floor unchanged.

### Residual smaller than every cost

If

\[
R<\min_e c_e,
\]

no positive increment is feasible. Again P66 returns the P65 floor unchanged.

### Residual can purchase several increments on one edge

The dynamic program permits

\[
z_e>1.
\]

P66 is therefore not a one-step greedy patch. It solves the complete floor-dominating residual problem.

---

## 11. What P66 proves

P66 proves all of the following under the declared separable surrogate and positive integer costs:

1. the P65 flooring residual is exactly the cost-weighted sum of continuous fractional parts;
2. that residual is strictly smaller than the mandatory one-observation baseline budget;
3. the residual augmentation problem has an exact Bellman dynamic program;
4. the reconstructed allocation is globally exact within the class that componentwise dominates the P65 floor;
5. the P66 objective can never be worse than the P65 floor objective;
6. the P66 instance-specific multiplicative certificate can never be worse than the P65 certificate;
7. the P65 universal \(\sqrt2\) guarantee is preserved;
8. integer-cost gcd compression applies exactly to the residual problem;
9. the residual dynamic-programming budget axis is bounded independently of the magnitude of the full budget \(B\).

---

## 12. What P66 does not establish

P66 does not establish:

1. that the floor-dominating restricted optimum always equals the unrestricted P63 optimum;
2. a universal approximation constant strictly smaller than \(\sqrt2\) for every feasible instance;
3. a strongly polynomial algorithm;
4. an FPTAS or PTAS;
5. optimality for the full combinatorial robust-routing design problem;
6. validity of the P58 finite-data noise assumptions in a particular experiment;
7. uniqueness or empirical correctness of the coefficients \(b_e\);
8. any physical-to-experiential bridge law;
9. any identification of consciousness with a calibration, information, thermodynamic, geometric, or quantum quantity;
10. any claim that quantum mechanics is incomplete.

---

## 13. Reproducibility

Implementation:
[`residual_exact_calibration_augmentation.py`](../src/consciousness_bridge/residual_exact_calibration_augmentation.py)

Regression tests:
[`test_residual_exact_calibration_augmentation.py`](../tests/test_residual_exact_calibration_augmentation.py)

The theorem visual is maintained as
[`p66_residual_exact_calibration_augmentation.svg`](figures/p66_residual_exact_calibration_augmentation.svg).

---

## 14. Next research target

P66 makes the leftover-budget step exact inside the P65 floor-dominating class. Two mathematically distinct directions now become possible.

The first is approximation theory: determine whether one can prove a universal constant strictly better than \(\sqrt2\) by combining lower-bounded water filling with residual optimization or a different rounding construction.

The second is algorithmic complexity: determine whether the separable unequal-cost integer calibration problem admits a fully polynomial approximation scheme, a strongly polynomial approximation under additional cost structure, or a sharper discrete-convex reformulation.

Any future proposition should continue to distinguish global exactness, restricted exactness, approximation guarantees, and empirical heuristics.

---

## 15. Scientific boundary

P66 is an experimental resource-allocation theorem. It improves how a declared calibration budget can be converted into executable whole measurements. It does not itself provide evidence for a physical theory of consciousness and does not alter the repository's central requirement that any physical-to-experiential bridge be independently defined and empirically testable.
