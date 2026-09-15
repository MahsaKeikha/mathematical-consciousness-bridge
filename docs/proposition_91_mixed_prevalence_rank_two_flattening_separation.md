# Proposition 91: Mixed-Prevalence Rank-Two Flattening Separation

## Purpose

P90 proves an exact nonlinear separation on the strict P75 parameter-box face where the latent prevalence is fixed at zero. On that face the four-view law reduces to one product Bernoulli component, so a two-by-two slice must have rank one.

P91 removes that prevalence restriction.

For arbitrary latent prevalence, including genuinely nonzero mixing, the P75 law is a mixture of two product Bernoulli components. A suitable four-by-four flattening of the observable probability tensor is therefore a sum of two rank-one matrices and must have matrix rank at most two. P91 uses one exact three-by-three minor of that flattening to certify separation from the **entire P75 model cube**, not only the single-component face used by P90.

For the established empirical witness, P91 proves the exact certified bracket

\[
\boxed{
\frac{1}{42}
<
d_\infty\!\left(P_{\mathrm{emp}},\mathcal M_{75}\right)
\le
\frac{1}{24}.
}
\]

The lower side is a strict exclusion result for the closed radius-\(1/42\) ball. The upper side is attained by an explicit rational P75 point with prevalence \(4/5\), so both latent components have positive mixture weight.

P91 does **not** claim that \(1/24\) is the exact global optimum. Closing the remaining gap is a separate problem.

---

## P91A. Arbitrary P75 mixing gives rank at most two after bipartite flattening

Write the P75 four-view observable law as

\[
P(x_1,x_2,x_3,x_4)
=
(1-\pi_+)\prod_{j=1}^4 P(X_j=x_j\mid S=-1)
+
\pi_+\prod_{j=1}^4 P(X_j=x_j\mid S=+1).
\]

No extreme-prevalence assumption is made. The parameter \(\pi_+\) may be any value in \([0,1]\).

Flatten the four-way probability tensor by grouping \((X_1,X_4)\) as the row index and \((X_2,X_3)\) as the column index. Let

\[
F_{14\mid 23}(P)\in\mathbb R^{4\times4}
\]

use lexicographic state order \(00,01,10,11\) on both axes.

For each latent state \(s\in\{-1,+1\}\), define the row vector

\[
u_s(x_1,x_4)
=
P(X_1=x_1\mid S=s)P(X_4=x_4\mid S=s)
\]

and the column vector

\[
v_s(x_2,x_3)
=
P(X_2=x_2\mid S=s)P(X_3=x_3\mid S=s).
\]

Then

\[
\boxed{
F_{14\mid23}(P)
=
(1-\pi_+)u_-v_-^{\mathsf T}
+
\pi_+u_+v_+^{\mathsf T}.
}
\]

Each summand has rank at most one. Therefore

\[
\boxed{
\operatorname{rank}F_{14\mid23}(P)\le2
}
\]

for **every** P75 parameter vector, including arbitrary nonzero latent mixing.

Consequently every three-by-three minor of this flattening must have determinant zero.

---

## P91B. The established empirical law has a nonzero rank-two minor

The established exact empirical law is

```text
(0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3) / 24
```

Its \((X_1,X_4)\mid(X_2,X_3)\) flattening is

\[
F_{14\mid23}(P_{\mathrm{emp}})
=
\begin{pmatrix}
0 & 0 & 0 & 1/24\\
1/24 & 1/12 & 1/12 & 1/8\\
1/8 & 0 & 0 & 0\\
1/24 & 5/24 & 1/8 & 1/8
\end{pmatrix}.
\]

Select row states \(01,10,11\) and column states \(00,01,11\). The resulting three-by-three minor is

\[
A
=
\begin{pmatrix}
1/24 & 1/12 & 1/8\\
1/8 & 0 & 0\\
1/24 & 5/24 & 1/8
\end{pmatrix}.
\]

Direct exact arithmetic gives

\[
\boxed{
\det A=\frac{1}{512}>0.
}
\]

Thus the empirical flattening itself has rank at least three and cannot be an exact P75 law.

The remaining question is quantitative: how far can the empirical law move before this selected minor is allowed to vanish?

---

## P91C. Exact nonnegative interval certificate at radius 1/42

Suppose a candidate probability law \(Q\) obeys

\[
\lVert Q-P_{\mathrm{emp}}\rVert_\infty
\le\varepsilon.
\]

Every entry of the selected minor then lies in the interval

\[
\left[
\max(0,a_{ij}-\varepsilon),
\min(1,a_{ij}+\varepsilon)
\right].
\]

The clipping at zero is essential because probability entries cannot become negative.

The determinant of a three-by-three matrix is multi-affine in its nine entries. Therefore its minimum and maximum over this rectangular entry box occur at box vertices. There are exactly

\[
2^9=512
\]

such vertices.

Set

\[
\varepsilon_{91}=\frac{1}{42}.
\]

Exact rational enumeration of all 512 determinant vertices gives

\[
\boxed{
\min \det
=
\frac{23}{677376}>0
}
\]

and

\[
\max \det
=
\frac{2939}{677376}>0.
\]

Therefore **every** nonnegative three-by-three matrix within entrywise radius \(1/42\) of the empirical minor has strictly positive determinant.

But every P75 law has flattening rank at most two and hence selected-minor determinant zero. This is impossible inside the closed radius-\(1/42\) ball.

Therefore

\[
\boxed{
 d_\infty\!\left(P_{\mathrm{emp}},\mathcal M_{75}\right)
>
\frac{1}{42}.
}
\]

This lower certificate is global over the full P75 parameter cube. It does not assume \(\pi_+=0\), \(\pi_+=1\), or any other prevalence restriction.

As a useful guard on the exact calculation, the same selected-minor relaxation no longer certifies rank-two exclusion at radius \(1/41\): exact enumeration gives

\[
\min\det=-\frac{7}{860672}<0,
\qquad
\max\det=\frac{3793}{860672}>0.
\]

Thus the published radius \(1/42\) is not being obtained from a loose sign mistake that would also certify the nearby larger radius \(1/41\).

---

## P91D. Explicit genuinely mixed upper certificate at 1/24

Consider the exact rational P75 parameter vector

\[
\left(
\frac45,
\frac9{10},\frac58,
\frac16,\frac12,
\frac16,\frac23,
0,1
\right).
\]

The prevalence is

\[
\pi_+=\frac45,
\]

so both latent components have strictly positive weights \(1/5\) and \(4/5\). This is genuinely mixed prevalence and is not the single-component P90 face.

Exact P75 evaluation gives the sixteen-cell model law

\[
\left(
\frac1{72},
\frac1{20},
\frac1{360},
\frac1{10},
\frac1{360},
\frac1{20},
\frac1{1800},
\frac1{10},
\frac18,
\frac1{12},
\frac1{40},
\frac16,
\frac1{40},
\frac1{12},
\frac1{200},
\frac16
\right).
\]

Comparing all sixteen cells with the empirical law gives

\[
\boxed{
\left\|P_{\mathrm{emp}}-P_{\mathrm{model}}\right\|_\infty
=
\frac1{24}.
}
\]

All sixteen three-by-three minors of its \((X_1,X_4)\mid(X_2,X_3)\) flattening vanish exactly, as required by the rank-at-most-two theorem.

Hence

\[
\boxed{
 d_\infty\!\left(P_{\mathrm{emp}},\mathcal M_{75}\right)
\le
\frac1{24}.
}
\]

---

## P91E. Certified mixed-prevalence global bracket

Combining P91C and P91D yields

\[
\boxed{
\frac1{42}
<
d_\infty\!\left(P_{\mathrm{emp}},\mathcal M_{75}\right)
\le
\frac1{24}.
}
\]

Numerically,

\[
0.0238095\ldots
<
d_\infty
\le
0.0416666\ldots.
\]

This is a different statement from P90.

P90 proves the exact value \(5/72\) after restricting the declared parameter box to a single latent component. P91 allows the full two-component mixture family. Enlarging the model family can reduce distance, so the P90 and P91 numerical bounds must not be compared as if they optimized over the same model set.

The substantive advance is structural: the nonlinear separation survives arbitrary latent prevalence. It is therefore not merely an artifact of fixing \(\pi_+\) at an extreme value.

---

## What P91 establishes

For the established exact empirical witness, P91 establishes that:

1. every four-view two-component P75 mixture has rank at most two under the declared bipartite flattening;
2. the selected empirical three-by-three minor has determinant exactly \(1/512\);
3. every nonnegative entrywise perturbation of that minor with radius at most \(1/42\) still has strictly positive determinant;
4. the complete P75 model family is therefore strictly farther than \(1/42\) in full-law L-infinity distance;
5. an explicit rational P75 point with prevalence \(4/5\) lies at full-law distance exactly \(1/24\); and
6. the global mixed-prevalence distance is rigorously bracketed between those two values.

---

## What P91 does not establish

P91 does **not** prove that \(1/24\) is the exact distance from the empirical law to the full P75 model cube. The current theorem gives a certified strict lower exclusion radius and a separate constructive upper bound.

P91 also does not identify the latent variable with consciousness, prove that consciousness is nonphysical, show that consciousness is an additional dimension, validate a replacement theory, or convert model rejection into evidence for any particular ontology.

The physical-to-experiential bridge remains open.

---

## Reproducibility record

- Implementation: `src/consciousness_bridge/mixed_prevalence_rank_two_flattening_separation.py`
- Exact tests: `tests/test_mixed_prevalence_rank_two_flattening_separation.py`
- Equation provenance: `docs/p91_equation_provenance.md`
- Previous frontier: [P90 exact nonlinear rank-one slice separation](proposition_90_exact_nonlinear_rank_one_separation.md)
