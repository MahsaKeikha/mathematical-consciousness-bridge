# Proposition 88: Complete Parity-Linear Primal-Dual Certificate

## Status

**Proved conditional theorem with an exact rational strict-witness certificate.** P88 strengthens the published P87 hierarchy for the same declared P75 four-view binary latent target-measurement family and the same full-law $L_\infty$ distance.

P83-P87 introduce increasingly strong parity-based lower bounds, while each published proposition also retains the earlier certificate hierarchy. P87 completes the finite primitive four-event coefficient box $0<|c_i|\le2$.

P88 makes a different step: it removes the four-term sparsity and finite coefficient restrictions and optimizes over **every real linear combination of all eleven nontrivial parity coordinates**. That complete parity-linear problem is a finite linear program with an exact dual. The full P88 hierarchy is then defined by retaining the recursive P87 baseline:

\[
\boxed{
L_{88}(B)=\max\{L_{87}(B),L_{88}^{\mathrm{par}}(B)\}.
}
\]

This distinction matters. P88 closes the linear parity-witness class, but it does **not** claim that parity coordinates subsume the earlier non-parity P78-P82 certificates.

On the common exact rational P86-P88 witness,

\[
\boxed{
L_{87}(B)=\frac1{96}
<
L_{88}^{\mathrm{par}}(B)=L_{88}(B)=\frac5{168}.
}
\]

P88 is a model-separation theorem. It does not identify the P75 latent state with consciousness, prove parity completeness for the full observed law, establish nonphysicality, or close the physical-to-experiential bridge.

---

## 1. The gap left after P87

P87 closes one precisely declared finite family: four distinct parity events with primitive nonzero integer coefficients bounded by two in magnitude.

Two restrictions remain:

1. at most four of the eleven canonical parity coordinates enter one functional;
2. coefficients are restricted to a finite integer alphabet.

Neither restriction is required by the centered transfer inequality used in P85-P87. P88 therefore asks:

> What is the strongest certified full-law $L_\infty$ lower bound obtainable from any real linear combination of the eleven parity observables?

This is the **complete parity-linear subproblem**. The full P88 certificate retains P87 in parallel because the P87 hierarchy also contains earlier non-parity lower bounds.

---

## 2. Eleven-dimensional parity feature map

Use canonical view-set order

\[
\mathcal J=(01,02,03,12,13,23,012,013,023,123,0123).
\]

For a probability law $p$ on the sixteen four-bit outcomes define

\[
H_J=\left\{x:\sum_{j\in J}x_j\equiv0\pmod2\right\},
\qquad
h_J(p)=P_p(H_J),
\]

and collect the coordinates into

\[
h(p)\in\mathbb R^{11}.
\]

For arbitrary

\[
c\in\mathbb R^{11},
\]

define

\[
Q_c(p)=c^\top h(p).
\]

Let $A\in\{0,1\}^{16\times11}$ be the incidence matrix

\[
A_{x,J}=\mathbf1_{H_J}(x).
\]

Then the sixteen outcome coefficients of $Q_c$ are $Ac$.

---

## 3. Exact centered transfer norm

For probability laws $p,q$,

\[
\mathbf1^\top(p-q)=0.
\]

Hence for any scalar $a$,

\[
Q_c(p)-Q_c(q)
=(Ac-a\mathbf1)^\top(p-q).
\]

Therefore

\[
|Q_c(p)-Q_c(q)|
\le
\|Ac-a\mathbf1\|_1\|p-q\|_\infty.
\]

Define

\[
\boxed{
D(c)=\min_{a\in\mathbb R}\|Ac-a\mathbf1\|_1.
}
\]

Then

\[
\boxed{
|Q_c(p)-Q_c(q)|\le D(c)\|p-q\|_\infty.
}
\]

For finite $Ac$, a median minimizes the absolute-deviation objective.

### Positivity of $D$

For nonempty $J$, let

\[
\chi_J(x)=(-1)^{\sum_{j\in J}x_j}.
\]

Because

\[
\mathbf1_{H_J}(x)=\frac{1+\chi_J(x)}2,
\]

$Ac$ can be constant only if $\sum_Jc_J\chi_J$ is constant. The eleven nonempty Walsh characters used here are mutually orthogonal and each is orthogonal to the constant character on $\{0,1\}^4$. Thus $Ac$ is constant only for $c=0$.

Consequently

\[
\boxed{D(c)>0\quad\text{for }c\ne0.}
\]

So $D$ is a norm on the eleven-dimensional parity coefficient space.

---

## 4. Exact P75 box support

Inside latent branch $s\in\{-,+\}$ write

\[
a_{j,s}=1-2q_{j,s}.
\]

P83 gives

\[
P_s(H_J)=\frac{1+\prod_{j\in J}a_{j,s}}2.
\]

For fixed $c$, $Q_c$ is multi-affine in the eight response parameters and the latent prevalence $\pi$. Thus every extremum on an axis-aligned rational P75 box $B$ occurs at a parameter-box vertex.

Let $V(B)$ denote those vertices and

\[
z_v=h(p_v),\qquad v\in V(B).
\]

Then

\[
\boxed{
\max_{p\in\mathcal M_{75}(B)}Q_c(p)
=
\max_{v\in V(B)}c^\top z_v,
}
\]

with the analogous minimum identity.

---

## 5. Complete parity-linear primal program

Let

\[
\widehat h=h(\widehat p).
\]

Because both $c$ and $-c$ are available, two-sided interval separation can be written as one oriented support problem:

\[
\boxed{
L_{88}^{\mathrm{par}}(B)
=
\sup_{D(c)\le1}
\left[
 c^\top\widehat h
 -
 \max_{v\in V(B)}c^\top z_v
\right].
}
\]

Introducing $t$, a center $a$, and $u_x\ge0$ gives the finite LP

\[
\begin{aligned}
\text{maximize }&t\\
\text{subject to }&
 t\le c^\top(\widehat h-z_v), &&v\in V(B),\\
&-u_x\le(Ac)_x-a\le u_x, &&x\in\{0,1\}^4,\\
&\sum_xu_x\le1.
\end{aligned}
\]

Every feasible $c$ produces a valid full-law lower bound, so

\[
\boxed{
\inf_{q\in\mathcal M_{75}(B)}
\|\widehat p-q\|_\infty
\ge
L_{88}^{\mathrm{par}}(B).
}
\]

---

## 6. Exact dual program

Finite-dimensional LP duality gives

\[
\boxed{
L_{88}^{\mathrm{par}}(B)=\min_{\lambda,r,\mu}\mu
}
\]

subject to

\[
\lambda_v\ge0,
\qquad
\sum_{v\in V(B)}\lambda_v=1,
\]

\[
\mathbf1^\top r=0,
\]

\[
\boxed{
A^\top r
=
\widehat h-
\sum_{v\in V(B)}\lambda_vz_v,
}
\]

and

\[
|r_x|\le\mu
\qquad\text{for all sixteen cells.}
\]

Equivalently,

\[
L_{88}^{\mathrm{par}}(B)
=
\min_{\lambda\in\Delta(V(B))}
\min_{\substack{\mathbf1^\top r=0\\A^\top r=\widehat h-\sum_v\lambda_vz_v}}
\|r\|_\infty.
\]

This dual describes a parity-feature quotient distance. It does not assert that the convex hull of parity-feature box vertices equals the full nonlinear P75 law family.

---

## 7. Exact rational optimality certification

A rational primal coefficient vector gives an exact lower bound

\[
\ell
=
\frac{\operatorname{dist}(Q_c(\widehat p),I_B(Q_c))}{D(c)}.
\]

A rational dual feasible point $(\lambda,r,\mu)$ gives

\[
L_{88}^{\mathrm{par}}(B)\le\mu.
\]

If

\[
\ell=\mu,
\]

then weak duality alone proves the exact optimum

\[
\boxed{L_{88}^{\mathrm{par}}(B)=\ell=\mu.}
\]

The repository verifies all displayed strict-witness quantities with `fractions.Fraction` arithmetic.

---

## 8. Relationship to P87

Every parity functional used by P83-P87 embeds in the eleven-dimensional P88 parity coefficient space. Therefore the new parity component contains all of those **parity-functional** candidates.

However, the published P87 quantity is recursive:

\[
L_{87}=\max\{L_{86},L_{\mathrm{bp4}}\},
\]

and the earlier chain ultimately retains P78-P82 non-parity lower bounds. It would therefore be incorrect to infer solely from parity feasible-set inclusion that

\[
L_{88}^{\mathrm{par}}\ge L_{87}
\]

for every box.

P88 instead defines

\[
\boxed{
L_{88}(B)=\max\{L_{87}(B),L_{88}^{\mathrm{par}}(B)\}.
}
\]

Thus

\[
\boxed{L_{88}(B)\ge L_{87}(B)}
\]

pointwise by construction, while the stronger conceptual statement remains precise: $L_{88}^{\mathrm{par}}$ closes the complete **linear parity** witness class.

---

## 9. Exact strict witness

Use the same exact rational box and empirical sixteen-cell law used for the P86-P87 strict witness.

The recursive P87 certificate is

\[
\boxed{L_{87}(B)=\frac1{96}}.
\]

In canonical coordinate order

\[
(01,02,03,12,13,23,012,013,023,123,0123),
\]

choose

\[
\boxed{c=(0,2,1,-1,-1,-1,2,1,3,-2,3).}
\]

The exact empirical value is

\[
\boxed{Q_c(\widehat p)=\frac{13}{6}.}
\]

Exact parameter-box vertex enumeration gives

\[
\boxed{I_B(Q_c)=\left[3,\frac{51}{8}\right].}
\]

Hence

\[
\Delta_c
=3-\frac{13}{6}
=\boxed{\frac56}.
\]

The exact centered norm is

\[
\boxed{D(c)=28},
\qquad
\boxed{a=3}.
\]

Therefore the primal witness gives

\[
\boxed{
\frac{\Delta_c}{D(c)}
=
\frac{5/6}{28}
=
\frac5{168}.
}
\]

---

## 10. Matching exact dual witness

The stored dual certificate uses seven nonzero rational box-vertex weights

\[
\left(
\frac4{189},
\frac{16}{189},
\frac{16}{189},
\frac5{42},
\frac{22}{63},
\frac{40}{189},
\frac7{54}
\right),
\]

which sum exactly to one.

Its sixteen-cell residual vector, in lexicographic four-bit outcome order, is

\[
\begin{aligned}
r=(&-5/168,-5/168,5/168,5/168,\\
&-5/168,1/84,5/168,0,\\
&5/168,-5/168,-5/168,5/168,\\
&-5/168,2/189,11/504,-11/756).
\end{aligned}
\]

The exact verifier checks

\[
\mathbf1^\top r=0,
\]

\[
A^\top r
=
\widehat h-
\sum_v\lambda_vz_v,
\]

and

\[
\|r\|_\infty=\frac5{168}.
\]

Thus the dual gives

\[
L_{88}^{\mathrm{par}}(B)\le\frac5{168}.
\]

Together with the primal witness,

\[
\boxed{L_{88}^{\mathrm{par}}(B)=\frac5{168}.}
\]

Since this exceeds the recursive P87 baseline on the same box,

\[
\boxed{L_{88}(B)=\frac5{168}>\frac1{96}=L_{87}(B).}
\]

The exact improvement is

\[
\boxed{
L_{88}-L_{87}=\frac{13}{672}
}
\]

and

\[
\boxed{
\frac{L_{88}}{L_{87}}=\frac{20}{7}.
}
\]

---

## 11. Proposition 88

For every empirical sixteen-cell law $\widehat p$ and rational P75 parameter box $B$:

1. the eleven canonical nontrivial even-parity probabilities define a finite feature map $h$;
2. $D(c)=\min_a\|Ac-a\mathbf1\|_1$ is a norm on parity coefficient space;
3. every parity-linear P75 box support extremum occurs at a parameter-box vertex;
4. the strongest parity-linear full-law lower bound is the finite primal LP in Section 5;
5. its exact dual is the zero-mass residual program in Section 6;
6. matching exact rational primal and dual feasible points certify the parity-linear optimum without reliance on floating-point optimality claims;
7. the full hierarchy

\[
L_{88}(B)=\max\{L_{87}(B),L_{88}^{\mathrm{par}}(B)\}
\]

is a valid lower bound and satisfies $L_{88}(B)\ge L_{87}(B)$ pointwise;
8. on the explicit common P86-P88 witness,

\[
\boxed{
L_{87}(B)=\frac1{96}
<
L_{88}^{\mathrm{par}}(B)=L_{88}(B)=\frac5{168}.
}
\]

---

## 12. Why P88 is a conceptual step

P86 and P87 answer finite enumeration questions. P88 changes the mathematical object: it replaces coefficient-box enumeration with the support-function optimum over the entire eleven-dimensional real parity-linear space.

The dual exposes the geometry behind the earlier searches: the parity component is controlled by the smallest zero-mass full-law perturbation that reproduces the empirical parity-feature discrepancy relative to the convex hull of P75 box-vertex parity features.

This is a natural closure point for the **linear parity** branch. A future strengthening should add genuinely new observable information, nonlinear witnesses, or a tighter full-law relaxation rather than simply increase an integer coefficient bound.

---

## 13. Reproducibility record

Implementation:

`src/consciousness_bridge/complete_parity_linear_certificate.py`

Regression tests:

`tests/test_complete_parity_linear_certificate.py`

Equation provenance:

`docs/p88_equation_provenance.md`

Theorem figure:

`docs/figures/p88_complete_parity_linear_certificate.svg`

---

## 14. Scientific interpretation boundary

P88 is a conditional theorem about the declared P75 target-measurement family and the complete linear span of eleven parity observables. It does not show that parity observables contain all physically or experientially relevant information, that the P75 latent variable is experience, that all possible physical descriptors have been exhausted, that consciousness is nonphysical, or that the physical-to-experiential bridge has been solved.
