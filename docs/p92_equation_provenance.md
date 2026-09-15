# P92 Equation Provenance

## Scope

This record documents the mathematical origin of Proposition 92, the exact global mixed-prevalence distance theorem for the declared P75 four-view binary latent model.

P92 closes the P91 bracket

\[
\frac1{42}<d_\infty(P_{\mathrm{emp}},\mathcal M_{75})\le\frac1{24}
\]

by proving

\[
\boxed{d_\infty(P_{\mathrm{emp}},\mathcal M_{75})=\frac1{24}}.
\]

The theorem remains conditional on the P75 model definition and the established exact empirical count law.

---

## 1. P75 observable law

The P75 model is the repository's established two-component conditional-product Bernoulli family. In parameter order

```text
(pi_plus,
 q1_minus, q1_plus,
 q2_minus, q2_plus,
 q3_minus, q3_plus,
 q4_minus, q4_plus)
```

the observable law is

\[
P(x_1,x_2,x_3,x_4)
=
(1-\pi_+)\prod_{j=1}^4P(X_j=x_j\mid S=-)
+
\pi_+\prod_{j=1}^4P(X_j=x_j\mid S=+).
\]

Repository implementation:

- `src/consciousness_bridge/certified_continuous_model_separation.py`
- function `p75_four_view_law_exact`

P92 does not alter the P75 family.

---

## 2. X1 = 1 subtensor reduction

P92 restricts only the observable cells with `X1 = 1` and renames

\[
A=X_2,
\qquad
B=X_3,
\qquad
C=X_4.
\]

For latent state \(s\), define

\[
\lambda_s=P(S=s)P(X_1=1\mid S=s).
\]

Then

\[
T(a,b,c)
=
\sum_s\lambda_s
P(A=a\mid S=s)
P(B=b\mid S=s)
P(C=c\mid S=s).
\]

This follows directly from the P75 conditional-product factorization. It is not an additional modeling assumption.

---

## 3. Two-rank-one determinant identity

For vectors \(u_-,u_+,v_-,v_+\in\mathbb R^2\) and scalars \(\alpha,\beta\),

\[
M=\alpha u_-v_-^{\mathsf T}+\beta u_+v_+^{\mathsf T}
\]

satisfies

\[
\det M
=
\alpha\beta
\det[u_-,u_+]
\det[v_-,v_+].
\]

This is an elementary two-by-two determinant expansion.

For a Bernoulli response probability \(q_s\), use the probability vector

\[
(1-q_s,q_s)^{\mathsf T}.
\]

Then

\[
\det
\begin{pmatrix}
1-q_- & 1-q_+\\
q_- & q_+
\end{pmatrix}
=
q_+-q_-.
\]

Applying this identity to the three P92 conditional tables gives the exact factorizations used in the theorem.

---

## 4. P92 selected determinant factorizations

Let

\[
a_s=P(A=1\mid S=s),
\quad
b_s=P(B=1\mid S=s),
\quad
c_s=P(C=1\mid S=s),
\]

with

\[
\Delta_A=a_+-a_-,
\quad
\Delta_B=b_+-b_-,
\quad
\Delta_C=c_+-c_-.
\]

Then exact expansion gives

\[
D_{AB\mid C=1}
=
\lambda_-\lambda_+c_-c_+\Delta_A\Delta_B,
\]

\[
D_{AC\mid B=0}
=
\lambda_-\lambda_+(1-b_-)(1-b_+)\Delta_A\Delta_C,
\]

and

\[
D_{BC\mid A=0}
=
\lambda_-\lambda_+(1-a_-)(1-a_+)\Delta_B\Delta_C.
\]

The implementation verifies these identities against direct exact evaluation of the full P75 observable law.

Repository implementation:

- `src/consciousness_bridge/exact_global_mixed_prevalence_distance.py`
- function `p92_model_sign_factorization_exact`

Exact regression tests:

- `tests/test_exact_global_mixed_prevalence_distance.py`

---

## 5. Sign-coherence consequence

Multiplication yields

\[
D_{AB\mid C=1}D_{AC\mid B=0}D_{BC\mid A=0}
=
K(\Delta_A\Delta_B\Delta_C)^2,
\]

where

\[
K
=
(\lambda_-\lambda_+)^3
c_-c_+
(1-b_-)(1-b_+)
(1-a_-)(1-a_+)
\ge0.
\]

Therefore

\[
\boxed{
D_{AB\mid C=1}D_{AC\mid B=0}D_{BC\mid A=0}\ge0
}
\]

for every P75 parameter vector.

This is the central nonlinear invariant used by P92.

---

## 6. Established empirical witness

The exact empirical count vector is

```text
(0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3)
```

with total count `24`.

The X1 = 1 subtensor is

\[
\left(
\frac18,
\frac1{24},
0,
\frac5{24},
0,
\frac18,
0,
\frac18
\right).
\]

Direct exact arithmetic gives

\[
D_{AB\mid C=1}=-\frac1{48},
\qquad
D_{AC\mid B=0}=\frac1{64},
\qquad
D_{BC\mid A=0}=\frac5{192}.
\]

Their product is

\[
-\frac5{589824}<0.
\]

These values are repository-original exact calculations for the established witness.

---

## 7. Entrywise determinant sign radius

For a nonnegative matrix

\[
M=\begin{pmatrix}a&b\\c&d\end{pmatrix}
\]

with nonzero determinant, compare the smallest possible product supporting the empirical determinant sign with the largest possible opposing product under entrywise perturbation \(\varepsilon\).

The quadratic \(\varepsilon^2\) terms cancel. When the supporting positive factors remain above zero, the exact sign-stability radius is

\[
\boxed{
r(M)=\frac{|ad-bc|}{a+b+c+d}.
}
\]

For the three P92 empirical matrices this gives

\[
\frac1{24},
\qquad
\frac3{56},
\qquad
\frac5{72}.
\]

The first value is the minimum.

Repository implementation:

- function `determinant_sign_stability_radius_exact`
- function `certify_p92_empirical_sign_coherence_obstruction_exact`

---

## 8. Exact lower theorem

Any law at full-law L-infinity distance strictly less than `1/24` from the empirical witness keeps the selected determinant sign pattern

```text
(-, +, +)
```

and therefore has negative determinant product.

Every P75 law has nonnegative determinant product by Section 5. Hence no P75 law can lie strictly inside that radius.

Therefore

\[
d_\infty(P_{\mathrm{emp}},\mathcal M_{75})\ge\frac1{24}.
\]

---

## 9. Matching upper certificate inherited from P91

The exact rational P75 point

\[
\left(
\frac45,
\frac9{10},\frac58,
\frac16,\frac12,
\frac16,\frac23,
0,1
\right)
\]

has full-law L-infinity distance exactly

\[
\frac1{24}.
\]

Its prevalence is `4/5`, so both latent states have positive mixture weight.

P92 re-verifies this point directly with the established P75 evaluator rather than treating the P91 upper value as an unchecked constant.

At this point the three P92 determinants are

\[
0,
\qquad
\frac1{120},
\qquad
\frac3{160}.
\]

Thus the model point lies exactly on the sign-coherence boundary selected by the lower proof.

---

## 10. Exact equality

The lower and upper certificates match:

\[
\boxed{
d_\infty(P_{\mathrm{emp}},\mathcal M_{75})=\frac1{24}.
}
\]

No floating-point optimizer is needed for the published theorem.

---

## 11. Linear-separation boundary

The full P75 cube contains all sixteen deterministic observable laws. Their convex hull is the entire sixteen-cell probability simplex.

Therefore the empirical probability law lies in the convex hull of the full P75 model image. No global linear functional of the complete observable law can strictly separate it from that convex hull.

P92's exact lower certificate is consequently nonlinear in an essential geometric sense.

---

## Scientific interpretation boundary

P92 is a conditional model-separation theorem for one declared latent-variable family and one exact empirical witness.

It does not identify the latent state with consciousness, establish nonphysicality, prove an additional dimension of reality, validate a replacement theory, or solve the physical-to-experiential bridge.
