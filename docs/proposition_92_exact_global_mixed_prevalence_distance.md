# Proposition 92: Exact Global Mixed-Prevalence Distance

## Purpose

P91 removes the extreme-prevalence restriction used by P90 and proves the full-cube bracket

\[
\frac{1}{42}
<
d_\infty\!\left(P_{\mathrm{emp}},\mathcal M_{75}\right)
\le
\frac{1}{24}.
\]

P92 closes that gap exactly.

For the established empirical law and the complete P75 parameter cube,

\[
\boxed{
d_\infty\!\left(P_{\mathrm{emp}},\mathcal M_{75}\right)
=
\frac{1}{24}.
}
\]

The lower certificate is nonlinear. It uses a sign-coherence invariant shared by three conditional two-by-two determinants of every two-component product mixture. The upper certificate is the explicit genuinely mixed rational P75 point already constructed in P91.

A useful structural fact is that this exact full-cube result cannot come from a global linear separation argument. The full P75 cube contains every deterministic four-bit law, so its convex hull is the entire sixteen-cell probability simplex. The empirical law therefore lies in the convex hull of the full P75 model family. P92 instead uses a nonlinear invariant of the model image itself.

---

## P92A. Reduce to the X1 = 1 observable subtensor

Restrict the sixteen-cell observable law to the eight cells with

\[
X_1=1.
\]

Inside this subtensor write

\[
A=X_2,
\qquad
B=X_3,
\qquad
C=X_4.
\]

For one P75 parameter vector, let the latent state be

\[
S\in\{-,+\}
\]

with weights

\[
w_-=1-\pi_+,
\qquad
w_+=\pi_+.
\]

Define

\[
\lambda_s=w_s P(X_1=1\mid S=s).
\]

Then the unnormalized X1 = 1 subtensor is

\[
T(a,b,c)
=
\sum_{s\in\{-,+\}}
\lambda_s
P(A=a\mid S=s)
P(B=b\mid S=s)
P(C=c\mid S=s).
\]

Thus every P75 law induces a nonnegative two-component product mixture on this two-by-two-by-two subtensor. No restriction on latent prevalence is used.

---

## P92B. Three selected conditional minors

Let

\[
a_s=P(A=1\mid S=s),
\quad
b_s=P(B=1\mid S=s),
\quad
c_s=P(C=1\mid S=s),
\]

and define component differences

\[
\Delta_A=a_+-a_-,
\qquad
\Delta_B=b_+-b_-,
\qquad
\Delta_C=c_+-c_-.
\]

Consider the following three two-by-two determinants:

1. the A by B table at C=1;
2. the A by C table at B=0;
3. the B by C table at A=0.

Write them as

\[
D_{AB\mid C=1},
\qquad
D_{AC\mid B=0},
\qquad
D_{BC\mid A=0}.
\]

For a sum of two rank-one two-by-two matrices, the determinant factors into the product of the two mixture weights and the two component-vector determinants. Exact expansion gives

\[
\boxed{
D_{AB\mid C=1}
=
\lambda_-\lambda_+ c_-c_+\Delta_A\Delta_B,
}
\]

\[
\boxed{
D_{AC\mid B=0}
=
\lambda_-\lambda_+
(1-b_-)(1-b_+)
\Delta_A\Delta_C,
}
\]

and

\[
\boxed{
D_{BC\mid A=0}
=
\lambda_-\lambda_+
(1-a_-)(1-a_+)
\Delta_B\Delta_C.
}
\]

Multiplying the three identities gives

\[
D_{AB\mid C=1}
D_{AC\mid B=0}
D_{BC\mid A=0}
=
K
(\Delta_A\Delta_B\Delta_C)^2,
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

Therefore every P75 law satisfies the nonlinear sign-coherence constraint

\[
\boxed{
D_{AB\mid C=1}
D_{AC\mid B=0}
D_{BC\mid A=0}
\ge0.
}
\]

This includes interior mixtures, extreme prevalence, and parameter-boundary cases.

---

## P92C. Exact empirical sign violation

For the established empirical count law

```text
(0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3) / 24
```

the X1 = 1 subtensor, in A,B,C lexicographic order, is

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

The three selected matrices are

\[
M_{AB\mid C=1}
=
\begin{pmatrix}
1/24 & 5/24\\
1/8 & 1/8
\end{pmatrix},
\]

\[
M_{AC\mid B=0}
=
\begin{pmatrix}
1/8 & 1/24\\
0 & 1/8
\end{pmatrix},
\]

and

\[
M_{BC\mid A=0}
=
\begin{pmatrix}
1/8 & 1/24\\
0 & 5/24
\end{pmatrix}.
\]

Their exact determinants are

\[
\boxed{
D_{AB\mid C=1}=-\frac1{48},
\qquad
D_{AC\mid B=0}=\frac1{64},
\qquad
D_{BC\mid A=0}=\frac5{192}.
}
\]

Hence

\[
\boxed{
D_{AB\mid C=1}
D_{AC\mid B=0}
D_{BC\mid A=0}
=-\frac5{589824}<0.
}
\]

The empirical subtensor therefore violates the P75 sign-coherence invariant.

---

## P92D. Exact entrywise sign-stability lemma

Let

\[
M=
\begin{pmatrix}
a&b\\c&d
\end{pmatrix}
\]

be a nonnegative two-by-two matrix with nonzero determinant.

If

\[
ad>bc,
\]

then any nonnegative matrix within entrywise L-infinity radius \(\varepsilon\) can reach determinant zero only if

\[
(a-\varepsilon)(d-\varepsilon)
\le
(b+\varepsilon)(c+\varepsilon).
\]

Whenever the supporting diagonal entries stay above zero, expansion cancels the quadratic terms and gives the necessary condition

\[
\varepsilon
\ge
\frac{ad-bc}{a+b+c+d}.
\]

If

\[
ad<bc,
\]

the same argument with the two products exchanged gives

\[
\varepsilon
\ge
\frac{bc-ad}{a+b+c+d}.
\]

Therefore the exact unclipped sign-stability radius is

\[
\boxed{
r(M)=\frac{|ad-bc|}{a+b+c+d}.
}
\]

For the three empirical P92 minors this gives

\[
\boxed{
r_{AB\mid C=1}=\frac1{24},
\qquad
r_{AC\mid B=0}=\frac3{56},
\qquad
r_{BC\mid A=0}=\frac5{72}.
}
\]

All supporting positive entries exceed the corresponding radius, so no clipping correction is needed.

The smallest radius is exactly

\[
\boxed{\frac1{24}}.
\]

---

## P92E. Global lower bound at 1/24

Suppose a P75 model law \(Q\) satisfied

\[
\lVert Q-P_{\mathrm{emp}}\rVert_\infty
<
\frac1{24}.
\]

The same bound holds on every selected cell of the X1 = 1 subtensor. Because \(1/24\) is no larger than any of the three exact sign-stability radii, the selected determinants of \(Q\) must retain the empirical signs

\[
(-,+,+).
\]

Their product must therefore be negative.

But P92B proves that every P75 law has nonnegative product for these same three determinants. This is a contradiction.

Hence every P75 law obeys

\[
\boxed{
\left\|P_{\mathrm{emp}}-Q\right\|_\infty
\ge
\frac1{24}.
}
\]

Therefore

\[
\boxed{
d_\infty\!\left(P_{\mathrm{emp}},\mathcal M_{75}\right)
\ge
\frac1{24}.
}
\]

---

## P92F. Matching exact mixed upper certificate

Use the exact rational P75 point already constructed in P91:

\[
\left(
\frac45,
\frac9{10},\frac58,
\frac16,\frac12,
\frac16,\frac23,
0,1
\right).
\]

Its prevalence is

\[
\pi_+=\frac45,
\]

so both latent components have positive mixture weight.

Exact evaluation gives full-law distance

\[
\boxed{
\left\|P_{\mathrm{emp}}-P_{\mathrm{model}}\right\|_\infty
=
\frac1{24}.
}
\]

For this model point, the three selected determinants are

\[
\boxed{
0,
\qquad
\frac1{120},
\qquad
\frac3{160}.
}
\]

The first determinant lies exactly on the sign-coherence boundary. In fact, the empirical first minor reaches determinant zero at radius \(1/24\) through

\[
\begin{pmatrix}
1/24 & 5/24\\
1/8 & 1/8
\end{pmatrix}
\longrightarrow
\begin{pmatrix}
1/12 & 1/6\\
1/12 & 1/6
\end{pmatrix},
\]

whose determinant is exactly zero.

Thus the lower certificate is attained.

---

## P92G. Exact global theorem

Combining P92E and P92F yields

\[
\boxed{
d_\infty\!\left(P_{\mathrm{emp}},\mathcal M_{75}\right)
=
\frac1{24}.
}
\]

Numerically,

\[
\frac1{24}=0.0416666\ldots.
\]

This closes the full mixed-prevalence distance problem left open by P91.

The advance from P91 to P92 is not a larger numerical search. P92 identifies a new exact nonlinear invariant, proves its universal factorization over the full P75 cube, computes exact sign-stability radii for the empirical witness, and obtains a matching rational lower and upper certificate.

---

## Why no global linear certificate can prove P92

The complete P75 cube contains every deterministic four-bit observable law: fix prevalence to one latent component and choose each Bernoulli response probability in \(\{0,1\}\).

Therefore the convex hull of the full P75 model image contains all sixteen simplex vertices and hence equals the complete probability simplex.

The empirical law belongs to that simplex. Consequently no global linear functional of the full sixteen-cell law can strictly separate the empirical law from the convex hull of the full P75 family.

P92 is necessarily nonlinear in this precise sense.

---

## What P92 establishes

For the established exact empirical witness and the complete P75 parameter cube, P92 establishes that:

1. the X1 = 1 observable subtensor of every P75 law is a nonnegative two-component product mixture;
2. three selected conditional two-by-two determinants obey an exact sign-coherence product constraint;
3. the empirical determinants are exactly `-1/48`, `1/64`, and `5/192`;
4. their exact sign-stability radii are `1/24`, `3/56`, and `5/72`;
5. no P75 law can lie at full-law L-infinity distance strictly below `1/24`;
6. an explicit genuinely mixed rational P75 point lies at distance exactly `1/24`; and
7. the exact global full-cube distance is therefore `1/24`.

---

## What P92 does not establish

P92 is a theorem about incompatibility between one exact empirical witness and one declared latent-variable model family.

It does not identify the latent state with consciousness, prove that consciousness is nonphysical, show that consciousness is an additional dimension, validate a replacement ontology, or convert model rejection into evidence for a particular theory of consciousness.

The physical-to-experiential bridge remains open.

---

## Reproducibility record

- Implementation: `src/consciousness_bridge/exact_global_mixed_prevalence_distance.py`
- Exact tests: `tests/test_exact_global_mixed_prevalence_distance.py`
- Equation provenance: `docs/p92_equation_provenance.md`
- Previous frontier: [P91 mixed-prevalence rank-two flattening separation](proposition_91_mixed_prevalence_rank_two_flattening_separation.md)
