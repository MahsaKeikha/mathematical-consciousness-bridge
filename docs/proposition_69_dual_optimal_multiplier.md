# Proposition 69: certified dual-optimal multiplier search

**Status:** proved optimization theorem for the declared P63/P68 calibration surrogate.

## 1. Purpose

P68 proves that every positive Lagrange multiplier gives a valid lower bound on the unrestricted P63 integer calibration optimum. That raises a precise next question:

> Among all positive multipliers, how strong can that P68 lower bound become, and how can we certify that a numerical multiplier search is close to the best possible value in this dual family?

P69 answers that question without assuming strong duality. It optimizes the **dual certificate itself**. The strongest P68 lower bound can still be strictly below the P63 primal optimum.

This distinction is essential. P69 can tighten an optimization certificate. It cannot turn a nonzero primal-dual gap into a proof of primal exactness.

---

## 2. Integer calibration problem inherited from P63

Let the calibrated edge set be finite. For every edge \(e\), let

- \(b_e>0\) denote its effective uncertainty-sensitivity coefficient,
- \(c_e\in\mathbb N\) denote the positive integer cost of one observation,
- \(k_e\in\mathbb N\), \(k_e\ge1\), denote the integer observation count,
- \(B\in\mathbb N\) denote the total budget.

The unrestricted P63 problem is

\[
\boxed{
U_{\rm int}^*(B)
=
\min_{k_e\ge1,\; k_e\in\mathbb N}
\left\{
\sum_e\frac{b_e}{\sqrt{k_e}}
:\;
\sum_e c_ek_e\le B
\right\}.
}
\]

Feasibility requires

\[
\boxed{B\ge B_0:=\sum_e c_e.}
\]

P69 does not change this primal problem.

---

## 3. P68 Lagrangian dual family

For \(\lambda>0\), define the edgewise Lagrangian term

\[
\ell_e(j;\lambda)
=
\frac{b_e}{\sqrt j}+\lambda c_ej,
\qquad j\in\mathbb N,\;j\ge1.
\]

Define

\[
\phi_e(\lambda)
=
\min_{j\ge1}\ell_e(j;\lambda)
\]

and the P68 dual function

\[
\boxed{
q(\lambda)
=
\sum_e\phi_e(\lambda)-\lambda B.
}
\]

P68 proves weak duality:

\[
\boxed{
q(\lambda)\le U_{\rm int}^*(B)
\qquad\forall\lambda>0.
}
\]

P69 studies

\[
\boxed{
q^*:=\sup_{\lambda>0}q(\lambda).
}
\]

The quantity \(q^*\) is the strongest lower bound available from this declared one-dimensional Lagrangian relaxation.

---

## 4. Exact edgewise minimizer sets

For fixed \(\lambda>0\), the real extension

\[
f_e(x;\lambda)=\frac{b_e}{\sqrt x}+\lambda c_ex,
\qquad x\ge1,
\]

has

\[
f_e''(x;\lambda)=\frac{3b_e}{4x^{5/2}}>0.
\]

Hence it is strictly convex. Its unconstrained stationary point is

\[
\boxed{
x_e^{(0)}(\lambda)
=
\left(\frac{b_e}{2\lambda c_e}\right)^{2/3}.
}
\]

After imposing \(x\ge1\), the real minimizer is

\[
x_e^*(\lambda)=\max\{1,x_e^{(0)}(\lambda)\}.
\]

Therefore the exact integer minimizer set

\[
M_e(\lambda)
=
\arg\min_{j\in\mathbb N,\;j\ge1}\ell_e(j;\lambda)
\]

is contained in the two neighboring integers around \(x_e^*(\lambda)\). At a discrete breakpoint both adjacent counts can minimize exactly.

This is the P68 coordinate result reused by P69.

---

## 5. Concavity theorem

For every fixed positive integer \(j\),

\[
\ell_e(j;\lambda)
=
\frac{b_e}{\sqrt j}+\lambda c_ej
\]

is affine in \(\lambda\). The pointwise infimum of affine functions is concave. Therefore each \(\phi_e\) is concave on \((0,\infty)\).

A finite sum of concave functions plus an affine function remains concave. Hence:

\[
\boxed{
q:(0,\infty)\to\mathbb R
\text{ is concave.}
}
\]

For every fixed \(\lambda>0\), the linear penalty \(\lambda c_ej\) makes \(\ell_e(j;\lambda)\to\infty\) as \(j\to\infty\), so the integer minimum is attained. Locally around any fixed positive multiplier only finitely many counts can compete, which gives local piecewise-linearity and continuity of \(q\) on \((0,\infty)\).

The breakpoints for one edge occur when adjacent counts tie:

\[
\frac{b_e}{\sqrt j}+\lambda c_ej
=
\frac{b_e}{\sqrt{j+1}}+\lambda c_e(j+1).
\]

Thus

\[
\boxed{
\lambda
=
\frac{\Delta_e(j)}{c_e},
\qquad
\Delta_e(j)
=
b_e\left(\frac1{\sqrt j}-\frac1{\sqrt{j+1}}\right).
}
\]

These breakpoints accumulate only toward \(\lambda=0\).

---

## 6. Exact supergradient interval

For a concave function, a supergradient \(g\) at \(\lambda\) satisfies

\[
q(\mu)
\le
q(\lambda)+g(\mu-\lambda)
\qquad\forall\mu>0.
\]

For one edge, every minimizing count \(j\in M_e(\lambda)\) contributes affine slope \(c_ej\). Therefore

\[
\partial^+\phi_e(\lambda)
=
\operatorname{conv}\{c_ej:j\in M_e(\lambda)\}.
\]

Because the problem is one-dimensional, this is the interval

\[
\boxed{
\partial^+\phi_e(\lambda)
=
\left[
c_e\min M_e(\lambda),
c_e\max M_e(\lambda)
\right].
}
\]

Summing the edge intervals and subtracting the budget slope \(B\) gives

\[
\boxed{
\partial^+q(\lambda)
=
\left[
S_{\min}(\lambda)-B,
S_{\max}(\lambda)-B
\right],
}
\]

where

\[
S_{\min}(\lambda)
=
\sum_e c_e\min M_e(\lambda),
\]

\[
S_{\max}(\lambda)
=
\sum_e c_e\max M_e(\lambda).
\]

This interval is exact: edgewise minimizers combine independently in the separable Lagrangian.

---

## 7. Exact dual-optimality condition

For a concave function on an open interval, an interior point \(\lambda^*>0\) is a global maximizer whenever

\[
0\in\partial^+q(\lambda^*).
\]

Using the exact interval above,

\[
\boxed{
S_{\min}(\lambda^*)
\le B
\le
S_{\max}(\lambda^*).
}
\]

is therefore a sufficient and, for an attained interior maximum, exact first-order optimality condition.

Equivalently, the budget lies between the smallest and largest total spend obtainable by independently selecting exact edgewise Lagrangian minimizers at the same multiplier.

When the interval collapses to one slope, this condition reduces to exact budget matching.

---

## 8. Monotonicity of minimizing spend

Let \(0<\lambda_1<\lambda_2\). Choose any

\[
j_1\in M_e(\lambda_1),
\qquad
j_2\in M_e(\lambda_2).
\]

Optimality gives

\[
\frac{b_e}{\sqrt{j_1}}+\lambda_1c_ej_1
\le
\frac{b_e}{\sqrt{j_2}}+\lambda_1c_ej_2,
\]

and

\[
\frac{b_e}{\sqrt{j_2}}+\lambda_2c_ej_2
\le
\frac{b_e}{\sqrt{j_1}}+\lambda_2c_ej_1.
\]

Adding and cancelling the nonlinear terms yields

\[
(\lambda_2-\lambda_1)c_e(j_2-j_1)\le0.
\]

Since \(\lambda_2-\lambda_1>0\) and \(c_e>0\),

\[
\boxed{j_2\le j_1.}
\]

Thus every edgewise minimizing count is nonincreasing with \(\lambda\), and therefore both

\[
\boxed{S_{\min}(\lambda),\;S_{\max}(\lambda)}
\]

are nonincreasing functions of the multiplier.

This monotonicity supplies the search direction:

- if \(S_{\min}(\lambda)>B\), every supergradient is positive, so a maximizer lies to the right;
- if \(S_{\max}(\lambda)<B\), every supergradient is negative, so a maximizer lies to the left;
- if \(S_{\min}(\lambda)\le B\le S_{\max}(\lambda)\), the multiplier is dual-optimal.

---

## 9. Existence of a finite sign-changing bracket when \(B>B_0\)

For sufficiently large \(\lambda\), every edge minimizes at \(j=1\). Hence the eventual dual slope is

\[
B_0-B<0
\]

when \(B>B_0\).

As \(\lambda\downarrow0\), the stationary scale

\[
x_e^{(0)}(\lambda)
=
\left(\frac{b_e}{2\lambda c_e}\right)^{2/3}
\]

diverges. Therefore every edgewise minimizing count, and hence total minimizing spend, eventually exceeds any fixed finite budget. The dual slope is then positive.

Consequently there exist finite multipliers

\[
0<\lambda_L<\lambda_R<\infty
\]

such that

\[
\boxed{
S_{\min}(\lambda_L)-B>0,
\qquad
S_{\max}(\lambda_R)-B<0.
}
\]

A multiplicative expansion/contraction search therefore brackets a dual maximizer.

---

## 10. Baseline-budget boundary case

If

\[
B=B_0=\sum_e c_e,
\]

then the only primal-feasible integer allocation is

\[
k_e=1\quad\forall e.
\]

For any multiplier satisfying

\[
\lambda
\ge
\max_e\frac{\Delta_e(1)}{c_e},
\]

count one is an edgewise Lagrangian minimizer for every edge. Therefore

\[
q(\lambda)
=
\sum_e b_e
+\lambda\sum_e c_e
-\lambda B
=
\sum_e b_e.
\]

Hence

\[
\boxed{
q^*=U_{\rm int}^*(B_0)=\sum_e b_e.
}
\]

P69 handles this boundary case directly.

---

## 11. Supporting-line upper certificate

Suppose a sign-changing bracket has been established:

\[
0<\lambda_L<\lambda_R,
\]

with a chosen positive supergradient \(g_L>0\) at \(\lambda_L\) and a chosen negative supergradient \(g_R<0\) at \(\lambda_R\).

Concavity gives the global supporting inequalities

\[
q(\lambda)
\le
q(\lambda_L)+g_L(\lambda-\lambda_L),
\]

\[
q(\lambda)
\le
q(\lambda_R)+g_R(\lambda-\lambda_R).
\]

Define the two affine supports

\[
L(\lambda)
=q(\lambda_L)+g_L(\lambda-\lambda_L),
\]

\[
R(\lambda)
=q(\lambda_R)+g_R(\lambda-\lambda_R).
\]

Inside the bracket,

\[
q(\lambda)\le\min\{L(\lambda),R(\lambda)\}.
\]

Because \(L\) increases and \(R\) decreases, the maximum of their minimum occurs at their intersection, clipped to the bracket. Let that computable value be \(Q_{\rm up}\). Then

\[
\boxed{
q^*\le Q_{\rm up}.
}
\]

If \(Q_{\rm low}\) is the largest actually evaluated dual value so far, then

\[
\boxed{
Q_{\rm low}\le q^*\le Q_{\rm up}.
}
\]

Therefore

\[
\boxed{
0\le q^*-Q_{\rm low}
\le Q_{\rm up}-Q_{\rm low}.
}
\]

This is the P69 **dual-value certificate**.

The implementation stops only when

\[
\boxed{
Q_{\rm up}-Q_{\rm low}\le\varepsilon_{\rm dual}.
}
\]

Thus the returned multiplier is certified to achieve a P68 lower bound within \(\varepsilon_{\rm dual}\) of the strongest possible value in the declared Lagrangian family.

---

## 12. Relation to a feasible primal candidate

Let \(\widehat k\) be any feasible P63 candidate. Using the best evaluated P69 dual value \(Q_{\rm low}\), weak duality still gives

\[
Q_{\rm low}\le q^*\le U_{\rm int}^*(B).
\]

Therefore

\[
\boxed{
0
\le
U(\widehat k)-U_{\rm int}^*(B)
\le
U(\widehat k)-Q_{\rm low}.
}
\]

P69 makes the right-hand side as strong as the P68 dual family permits, up to the declared dual-value tolerance.

However, even an exact dual maximizer only establishes

\[
q^*\le U_{\rm int}^*(B).
\]

P69 does **not** generally establish equality.

---

## 13. P67 as the zero primal-dual gap case

P67 provides an additional primal statement. If a feasible integer allocation \(\widehat k\) spends the budget exactly and a common multiplier makes every \(\widehat k_e\) an edgewise Lagrangian minimizer, then

\[
q(\lambda)
=
U(\widehat k)
=
U_{\rm int}^*(B).
\]

In that case P69 also recognizes \(\lambda\) as dual-optimal because zero belongs to its supergradient interval.

Thus the logical relationship is

\[
\boxed{
\text{P67 primal exactness}
\Longrightarrow
\text{zero duality gap and P69 dual optimality}.
}
\]

The converse is not asserted without an independently constructed primal allocation satisfying the P67 conditions.

---

## 14. Computational structure

Each multiplier evaluation requires one exact P68 coordinate minimization per edge. After the continuous stationary count is formed, only neighboring integers are checked. Therefore one dual evaluation is

\[
\boxed{O(m)}
\]

for \(m\) calibrated edges.

The bracketing phase changes \(\lambda\) geometrically until opposite supergradient signs are found. The refinement phase is one-dimensional bisection. If \(N_{\rm eval}\) multiplier evaluations are required, total work is

\[
\boxed{O(mN_{\rm eval}).}
\]

P69 reports the number of refinement iterations and a certified dual-value error. It does not claim a bit-complexity bound independent of the numerical tolerance.

---

## 15. Scientific boundary

P69 is a theorem about optimizing an experimental resource-allocation certificate. It establishes:

- concavity of the declared P68 Lagrangian dual,
- exact supergradient intervals from minimizing integer spends,
- monotone multiplier bracketing,
- exact dual-optimality recognition when zero enters the supergradient interval,
- a certified lower/upper bracket on the strongest P68 dual value.

It does **not** establish:

- that the calibration surrogate is consciousness,
- that a small optimization gap validates an experiential theory,
- that dual optimality implies primal exactness in general,
- that consciousness is quantum,
- that quantum mechanics is incomplete,
- that consciousness is a new state of matter or spacetime dimension.

Those are separate scientific questions requiring independent definitions, derivations, and empirical evidence.

---

## 16. Provenance

P69 is a repository-original optimization theorem built from:

- the P63 unrestricted heterogeneous-cost integer calibration problem,
- P67 discrete marginal/common-multiplier optimality logic,
- P68 exact one-edge integer Lagrangian minimization and weak-duality bound,
- standard concave-analysis supporting-line arguments.

The executable implementation is in [`dual_optimal_multiplier.py`](../src/consciousness_bridge/dual_optimal_multiplier.py), with regression tests in [`test_dual_optimal_multiplier.py`](../tests/test_dual_optimal_multiplier.py).
