# Proposition 68: Lagrangian lower bounds and quantitative integer optimality gaps

## Status

**Proved for the declared heterogeneous-cost separable calibration problem.**

P67 gives a sufficient certificate that can sometimes prove a candidate allocation is exactly the unrestricted P63 integer optimum. P68 addresses the complementary case: when P67 does not close the proof, can the candidate still receive a rigorous quantitative quality certificate without solving the full P63 dynamic program?

The answer is yes. Every positive Lagrange multiplier gives a valid lower bound on the unrestricted P63 optimum. Comparing a feasible candidate with that lower bound gives a rigorous additive optimality-gap upper bound and, when the lower bound is positive, a multiplicative factor bound.

P68 does **not** claim that its automatic multiplier selection maximizes the Lagrangian dual. The lower-bound theorem is valid for every declared positive multiplier. A better multiplier can tighten the certificate, but the certificate remains valid even when the selected multiplier is not dual-optimal.

---

## 1. Integer calibration problem

Let the calibrated edge set be finite. For each edge \(e\), let

- \(b_e>0\) denote the effective uncertainty coefficient,
- \(c_e\in\mathbb N\) denote the positive integer cost of one observation,
- \(k_e\in\mathbb N\), \(k_e\ge1\), denote the integer number of observations.

The P63 problem is

\[
\boxed{
U_{\rm int}^*(B)
=
\min_{k_e\in\mathbb N,\ k_e\ge1}
\left\{
U(k)=\sum_e\frac{b_e}{\sqrt{k_e}}
:\
\sum_ec_ek_e\le B
\right\}.
}
\]

The budget is assumed feasible:

\[
B\ge B_0:=\sum_ec_e.
\]

As in P62 through P67, the implementation may construct

\[
b_e=(\text{coefficient}_e)(\text{sensitivity}_e).
\]

The theorem itself depends only on positive \(b_e\), positive integer \(c_e\), and the integer budget constraint.

---

## 2. Lagrangian relaxation

For any multiplier

\[
\lambda>0,
\]

define the Lagrangian

\[
\mathcal L(k,\lambda)
=
\sum_e\frac{b_e}{\sqrt{k_e}}
+
\lambda\left(\sum_ec_ek_e-B\right).
\]

Because the objective and cost term are separable across edges,

\[
\inf_{k_e\in\mathbb N,\ k_e\ge1}
\mathcal L(k,\lambda)
=
\sum_e
\min_{j\in\mathbb N,\ j\ge1}
\left(
\frac{b_e}{\sqrt j}+\lambda c_ej
\right)
-
\lambda B.
\]

Define

\[
\boxed{
q(\lambda)
:=
\sum_e
\min_{j\ge1,\ j\in\mathbb N}
\left(
\frac{b_e}{\sqrt j}+\lambda c_ej
\right)
-
\lambda B.
}
\]

This is the P68 dual lower bound.

---

## 3. Exact one-edge integer minimization

For a fixed edge, consider the real extension

\[
h_e(x)
=
\frac{b_e}{\sqrt x}+\lambda c_ex,
\qquad x\ge1.
\]

Its derivatives are

\[
h_e'(x)
=
-\frac{b_e}{2x^{3/2}}+\lambda c_e,
\]

and

\[
h_e''(x)
=
\frac{3b_e}{4x^{5/2}}>0.
\]

Therefore \(h_e\) is strictly convex on \([1,\infty)\). Its unconstrained stationary point is

\[
\boxed{
x_e^{(0)}
=
\left(\frac{b_e}{2\lambda c_e}\right)^{2/3}.
}
\]

After imposing \(x\ge1\), the real minimizer is

\[
\bar x_e=\max\{1,x_e^{(0)}\}.
\]

Strict convexity implies that an integer minimizer must be one of the neighboring integers

\[
\boxed{
\left\lfloor\bar x_e\right\rfloor
\quad\text{or}\quad
\left\lceil\bar x_e\right\rceil,
}
\]

with the lower endpoint clipped at one. Evaluating those neighboring counts therefore solves each one-edge integer Lagrangian problem exactly. At a discrete marginal breakpoint, two adjacent counts can tie; both are valid minimizers.

This makes evaluation of \(q(\lambda)\) linear in the number of edges once \(\lambda\) is fixed.

---

## 4. Weak-duality theorem

### Proposition 68A

For every \(\lambda>0\),

\[
\boxed{
q(\lambda)\le U_{\rm int}^*(B).
}
\]

### Proof

Let \(k\) be any feasible integer allocation. Then

\[
\sum_ec_ek_e-B\le0.
\]

Since \(\lambda>0\),

\[
\lambda\left(\sum_ec_ek_e-B\right)\le0,
\]

so

\[
\mathcal L(k,\lambda)\le U(k).
\]

By definition,

\[
q(\lambda)
=
\inf_j\mathcal L(j,\lambda)
\le
\mathcal L(k,\lambda)
\le
U(k).
\]

This is true for every feasible integer \(k\). Taking the minimum over the feasible set gives

\[
q(\lambda)\le U_{\rm int}^*(B).
\]

This proves the claim. \(\square\)

---

## 5. Additive candidate-gap certificate

Let \(\widehat k\) be any feasible integer candidate. Because

\[
q(\lambda)\le U_{\rm int}^*(B)\le U(\widehat k),
\]

we immediately obtain

\[
\boxed{
0
\le
U(\widehat k)-U_{\rm int}^*(B)
\le
U(\widehat k)-q(\lambda).
}
\]

Define

\[
\boxed{
G_{\lambda}(\widehat k)
:=
U(\widehat k)-q(\lambda).
}
\]

Then \(G_{\lambda}(\widehat k)\) is a rigorous upper bound on the unknown additive suboptimality of \(\widehat k\).

This statement requires no assumption that \(\lambda\) is a dual maximizer.

---

## 6. Multiplicative certificate

When

\[
q(\lambda)>0,
\]

weak duality also yields

\[
U_{\rm int}^*(B)\ge q(\lambda)>0.
\]

Therefore

\[
\boxed{
\frac{U(\widehat k)}{U_{\rm int}^*(B)}
\le
\frac{U(\widehat k)}{q(\lambda)}.
}
\]

So P68 reports the computable factor

\[
\boxed{
F_{\lambda}(\widehat k)
:=
\frac{U(\widehat k)}{q(\lambda)}.
}
\]

If \(q(\lambda)\le0\), the additive certificate remains valid, but this lower bound cannot produce a finite positive multiplicative ratio. The implementation therefore reports an infinite multiplicative factor in that case rather than inventing a finite guarantee.

---

## 7. P67 is the zero-gap special case

P67 defines the discrete marginal reduction

\[
\Delta_e(j)
=
b_e\left(j^{-1/2}-(j+1)^{-1/2}\right).
\]

For a candidate count \(k_e>1\), P67 proves that \(k_e\) minimizes the one-edge Lagrangian term exactly when

\[
\frac{\Delta_e(k_e)}{c_e}
\le
\lambda
\le
\frac{\Delta_e(k_e-1)}{c_e}.
\]

For \(k_e=1\), only the lower condition is required.

Suppose P67 succeeds for a candidate \(\widehat k\). Then

1. the budget is tight:
   \[
   \sum_ec_e\widehat k_e=B,
   \]
2. one common positive \(\lambda\) makes every \(\widehat k_e\) an exact one-edge Lagrangian minimizer.

Hence

\[
q(\lambda)
=
\mathcal L(\widehat k,\lambda).
\]

Budget tightness removes the penalty term:

\[
\mathcal L(\widehat k,\lambda)=U(\widehat k).
\]

Therefore

\[
\boxed{
q(\lambda)=U(\widehat k)=U_{\rm int}^*(B),
}
\]

and the P68 additive certificate becomes

\[
\boxed{
G_{\lambda}(\widehat k)=0.
}
\]

Thus P67 is recovered exactly as the zero-duality-gap special case of P68.

---

## 8. What P68 adds when P67 fails

P67 failure is deliberately inconclusive. It can occur because

- the candidate does not spend the budget exactly, or
- the edgewise multiplier intervals do not share a common value.

Neither event proves the candidate is suboptimal.

P68 replaces that binary dead end with a quantitative statement. For any selected \(\lambda>0\), it computes

\[
q(\lambda),
\]

then reports

\[
U(\widehat k)-q(\lambda)
\]

as a rigorous upper bound on the candidate's possible additive suboptimality.

A poor multiplier may give a loose bound. A better multiplier may tighten it. The validity of the bound is unchanged.

---

## 9. Automatic multiplier selection in the implementation

The implementation allows the multiplier to be supplied explicitly. If no multiplier is supplied, it uses a transparent rule based on the P67 interval endpoints:

- if P67 succeeds, use the P67 common-multiplier witness;
- if the P67 interval endpoints overlap but the budget is slack, use their midpoint when finite;
- if the endpoints are disjoint and finite, use their geometric mean;
- if the upper endpoint is infinite, use the positive lower endpoint.

This rule is designed to provide a reproducible witness near the P67 marginal scale.

It is **not** claimed to solve

\[
\sup_{\lambda\ge0}q(\lambda).
\]

P68's theorem requires only that the selected multiplier be positive.

---

## 10. Computational cost

For fixed \(\lambda\), each edge requires only

1. one continuous stationary-point calculation,
2. evaluation of at most two neighboring integer counts.

Therefore evaluating the P68 dual lower bound is

\[
\boxed{O(m)}
\]

for \(m\) calibrated edges.

The candidate objective and P67 interval information are also linear in \(m\). Thus the complete P68 certificate is linear-time after the candidate allocation is known.

This is distinct from P63's pseudo-polynomial dynamic program in the integer budget scale.

---

## 11. Relationship to P63, P66, and P67

The roles are now sharply separated:

| Result | Role | Exactness statement |
| --- | --- | --- |
| P63 | unrestricted heterogeneous-cost integer optimization | globally exact by pseudo-polynomial dynamic programming |
| P66 | bounded-residual optimization above the P65 floor | exact only inside the floor-dominating class |
| P67 | common-multiplier test | sufficient certificate that a candidate is the unrestricted P63 optimum |
| P68 | Lagrangian dual lower bound | quantitative additive and multiplicative certificate for any feasible candidate and any positive multiplier |

P68 does not make P66 globally exact when P67 fails. It quantifies the remaining uncertainty in objective quality through a valid lower bound.

---

## 12. Scientific boundary

P68 is an optimization theorem about allocation of measurements under a declared separable uncertainty surrogate.

It does **not** prove that

- the surrogate is itself a law of consciousness,
- an optimized measurement schedule identifies subjective experience,
- a small optimization gap is evidence for a physical-to-experiential bridge,
- consciousness is quantum,
- consciousness is a state of matter,
- consciousness is a new spacetime dimension, or
- quantum mechanics is incomplete.

Those are separate scientific questions requiring separate definitions, assumptions, and empirical evidence.

The only proved P68 claim is the optimization statement: the Lagrangian value \(q(\lambda)\) is a lower bound on the unrestricted P63 optimum, and therefore the candidate-minus-bound difference is a rigorous upper bound on candidate suboptimality for the declared integer calibration problem.

---

## 13. Implementation and tests

Implementation:

- [`src/consciousness_bridge/lagrangian_optimality_gap.py`](../src/consciousness_bridge/lagrangian_optimality_gap.py)

Regression tests:

- [`tests/test_lagrangian_optimality_gap.py`](../tests/test_lagrangian_optimality_gap.py)

The tests compare one-edge minimizers against brute force, compare P68 dual bounds against P63 exact optima, verify true candidate gaps lie below the P68 reported gap, recover P67 as a zero-gap case, and exercise explicit P67-failure cases without converting certificate failure into a suboptimality claim.
