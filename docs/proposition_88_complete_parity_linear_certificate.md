# Proposition 88: Complete Parity-Linear Primal-Dual Certificate

## Status

**Proved conditional computational theorem with exact rational optimality certificate.** P88 strengthens P87 for the same declared P75 four-view binary latent target-measurement family and the same full-law $L_\infty$ distance.

P83-P87 build a hierarchy of increasingly strong exact linear combinations of the eleven nontrivial parity coordinates on four binary views. P87 completes one important finite family: every primitive four-event integer coefficient vector with $0<|c_i|\le2$.

P88 removes the remaining **sparsity and coefficient-box restriction altogether**. It optimizes over every real linear combination of all eleven parity coordinates and derives an exact finite-dimensional primal-dual linear program. A matching rational primal witness and rational dual feasible point certify the optimum without trusting floating-point optimization.

On the same exact rational witness used for P86 and P87,

\[
\boxed{
L_{87}(B)=\frac1{96}
<
L_{88}^{\mathrm{par}}(B)=\frac5{168}.
}
\]

P88 is a model-separation theorem. It does not identify the P75 latent state with consciousness, prove that parity observables are complete for the full law, establish nonphysicality, or close the physical-to-experiential bridge.

---

## 1. The gap left after P87

P87 closes the bounded primitive four-event family

\[
0<|c_i|\le2.
\]

That is a mathematically complete finite box, but it still imposes two restrictions:

1. only four of the eleven canonical parity coordinates may appear at once;
2. coefficients are restricted to a finite integer alphabet.

Neither restriction is intrinsic to the transfer inequality used by P85-P87. The full class of linear parity witnesses is finite-dimensional, so the natural next question is:

> What is the strongest certified full-law $L_\infty$ lower bound obtainable from **any** linear combination of the eleven parity observables?

P88 answers this question exactly.

---

## 2. The eleven-dimensional parity feature map

Use the canonical view-set order

\[
\mathcal J=
(01,02,03,12,13,23,012,013,023,123,0123).
\]

For a probability law $p$ on the sixteen four-bit outcomes, define

\[
h_J(p)=P_p(H_J),
\qquad
H_J=\left\{x:\sum_{j\in J}x_j\equiv0\pmod2\right\},
\]

and collect the eleven coordinates into

\[
h(p)\in\mathbb R^{11}.
\]

For any coefficient vector

\[
c\in\mathbb R^{11},
\]

define the parity-linear functional

\[
Q_c(p)=c^\top h(p).
\]

Let $A\in\{0,1\}^{16\times11}$ be the parity-incidence matrix,

\[
A_{x,J}=\mathbf1_{H_J}(x).
\]

Then the sixteen outcome coefficients of $Q_c$ are

\[
g_c=Ac.
\]

---

## 3. Exact centered transfer norm

For probability laws $p$ and $q$,

\[
\mathbf1^\top(p-q)=0.
\]

Therefore for every scalar $a$,

\[
Q_c(p)-Q_c(q)
=
\sum_x\bigl[(Ac)_x-a\bigr](p_x-q_x).
\]

Hence

\[
|Q_c(p)-Q_c(q)|
\le
\left(\sum_x|(Ac)_x-a|\right)
\|p-q\|_\infty.
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

### Why $D$ is a genuine norm

For each nonempty parity view set $J$, write the Walsh character

\[
\chi_J(x)=(-1)^{\sum_{j\in J}x_j}.
\]

Because

\[
\mathbf1_{H_J}(x)=\frac{1+\chi_J(x)}2,
\]

$Ac$ can be constant only if

\[
\sum_{J\in\mathcal J}c_J\chi_J
\]

is constant. The eleven nonempty Walsh characters used here are mutually orthogonal and orthogonal to the constant character on the sixteen-point hypercube. Therefore $Ac$ is constant only when $c=0$.

Thus

\[
\boxed{D(c)>0\quad\text{for every }c\ne0.}
\]

The normalization $D(c)\le1$ is therefore well posed.

---

## 4. Exact support over a P75 parameter box

Inside latent branch $s\in\{-,+\}$, write

\[
a_{j,s}=1-2q_{j,s}.
\]

For each canonical even-parity event,

\[
P_s(H_J)=\frac{1+\prod_{j\in J}a_{j,s}}2.
\]

For fixed $c$,

\[
Q_c
=
(1-\pi)Q_{c,-}+\pi Q_{c,+}
\]

is multi-affine in the nine P75 parameters: prevalence and the eight branchwise response probabilities. Consequently every minimum and maximum over an axis-aligned rational box $B$ occurs at a parameter-box vertex.

Let $V(B)$ be that finite vertex set and let

\[
z_v=h(p_v),\qquad v\in V(B).
\]

Then

\[
\boxed{
\max_{p\in\mathcal M_{75}(B)}Q_c(p)
=
\max_{v\in V(B)}c^\top z_v
}
\]

and analogously for the minimum.

No numerical enclosure is needed for the support function.

---

## 5. The complete P88 primal program

Let

\[
\widehat h=h(\widehat p).
\]

Because both $c$ and $-c$ are allowed, two-sided interval separation is captured by one oriented support problem. Define

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

The zero vector is feasible, so the optimum is nonnegative.

Introduce auxiliary variables $a$, $u_x\ge0$, and $t$. The optimization is exactly the finite linear program

\[
\begin{aligned}
\text{maximize }&t\\
\text{subject to }&
 t\le c^\top(\widehat h-z_v),
 &&v\in V(B),\\
&-u_x\le (Ac)_x-a\le u_x,
 &&x\in\{0,1\}^4,\\
&\sum_xu_x\le1.
\end{aligned}
\]

For every feasible $c$ and every P75 law $q$ generated inside $B$,

\[
Q_c(\widehat p)-Q_c(q)
\le
D(c)\|\widehat p-q\|_\infty.
\]

Therefore

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

Finite-dimensional linear-program duality gives the exact dual representation

\[
\boxed{
L_{88}^{\mathrm{par}}(B)
=
\min_{\lambda,r,\mu}\mu
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
\sum_{v\in V(B)}\lambda_v z_v,
}
\]

and

\[
|r_x|\le\mu
\qquad
\text{for every observed cell }x.
\]

Equivalently,

\[
\boxed{
L_{88}^{\mathrm{par}}(B)
=
\min_{\lambda\in\Delta(V(B))}
\min_{\substack{\mathbf1^\top r=0\\
A^\top r=\widehat h-\sum_v\lambda_vz_v}}
\|r\|_\infty.
}
\]

This dual has a useful interpretation. It asks how small a zero-mass sixteen-cell perturbation can reproduce the empirical parity-feature discrepancy after comparing the empirical feature vector with the convex hull of the P75 box-vertex feature vectors.

It is a **parity-feature quotient distance**, not the full-law distance itself.

---

## 7. Exact rational optimality certification

P88 does not require trusting a floating-point optimizer to establish a reported optimum.

A rational primal witness supplies a coefficient vector $c$ and therefore an exact lower bound

\[
\ell
=
\frac{
\operatorname{dist}(Q_c(\widehat p),I_B(Q_c))
}{D(c)}.
\]

A rational dual feasible point $(\lambda,r,\mu)$ supplies an exact upper bound

\[
L_{88}^{\mathrm{par}}(B)\le\mu.
\]

If

\[
\ell=\mu,
\]

then weak duality alone certifies

\[
\boxed{
L_{88}^{\mathrm{par}}(B)=\ell=\mu
}
\]

exactly.

The repository implementation verifies both sides using `fractions.Fraction` arithmetic.

---

## 8. Pointwise dominance over P87

Every P87 functional is an eleven-dimensional parity coefficient vector with seven zero coordinates and four primitive nonzero integer coordinates satisfying $|c_i|\le2$.

Therefore the P87 family is a subset of the P88 optimization domain after homogeneous normalization. Hence for every empirical law and every admissible rational P75 box,

\[
\boxed{
L_{88}^{\mathrm{par}}(B)
\ge
L_{87}(B).
}
\]

The same inclusion also subsumes the linear parity-functional families introduced in P83-P86.

P88 therefore closes the entire **linear parity-witness hierarchy** built in P83-P87. It does not close the full-law model-separation problem because the eleven parity coordinates do not constitute all fifteen independent coordinates of a general four-bit probability law.

---

## 9. Exact strict witness

Use the same exact rational P75 box and empirical sixteen-cell law used for the P86 and P87 strict witnesses.

The P87 value is

\[
\boxed{L_{87}(B)=\frac1{96}}.
\]

In canonical coordinate order

\[
(01,02,03,12,13,23,012,013,023,123,0123),
\]

choose

\[
\boxed{
c=(0,2,1,-1,-1,-1,2,1,3,-2,3).}
\]

Thus

\[
\begin{aligned}
Q_c={}&
2P(H_{02})+P(H_{03})
-P(H_{12})-P(H_{13})-P(H_{23})\\
&+2P(H_{012})+P(H_{013})+3P(H_{023})\\
&-2P(H_{123})+3P(H_{0123}).
\end{aligned}
\]

The exact empirical value is

\[
\boxed{Q_c(\widehat p)=\frac{13}{6}.}
\]

Exact parameter-box vertex enumeration gives

\[
\boxed{
I_B(Q_c)=\left[3,\frac{51}{8}\right].
}
\]

The empirical value lies below the model interval by

\[
\Delta_c
=3-\frac{13}{6}
=\boxed{\frac56}.
\]

The exact centered outcome-coefficient calculation gives

\[
\boxed{D(c)=28}
\]

with minimizing center

\[
\boxed{a=3}.
\]

Therefore this primal witness gives

\[
\frac{\Delta_c}{D(c)}
=
\frac{5/6}{28}
=
\boxed{\frac5{168}}.
\]

---

## 10. Exact dual certificate for the same witness

The implementation stores a sparse rational dual feasible point supported on seven P75 parameter-box vertices with weights

\[
\boxed{
\left(
\frac4{189},
\frac{16}{189},
\frac{16}{189},
\frac5{42},
\frac{22}{63},
\frac{40}{189},
\frac7{54}
\right),
}
\]

which sum exactly to one.

It also stores the exact zero-mass residual vector, in lexicographic four-bit outcome order,

\[
\begin{aligned}
r=(&-5/168,-5/168,5/168,5/168,\\
&-5/168,1/84,5/168,0,\\
&5/168,-5/168,-5/168,5/168,\\
&-5/168,2/189,11/504,-11/756).
\end{aligned}
\]

The regression suite verifies exactly that

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

The primal witness in Section 9 attains the same value, so

\[
\boxed{
L_{88}^{\mathrm{par}}(B)=\frac5{168}
}
\]

is the exact optimum over **all real linear combinations of the eleven parity coordinates**.

---

## 11. Strict hierarchy on the common exact witness

For the same box and empirical law,

\[
\boxed{
L_{85}(B)=0
<
L_{86}(B)=\frac1{192}
<
L_{87}(B)=\frac1{96}
<
L_{88}^{\mathrm{par}}(B)=\frac5{168}.
}
\]

The P88 improvement over P87 is

\[
\boxed{
\frac5{168}-\frac1{96}
=\frac{13}{672}.
}
\]

The multiplicative improvement is

\[
\boxed{
\frac{L_{88}^{\mathrm{par}}}{L_{87}}
=\frac{20}{7}.
}
\]

So the gain is not produced by merely adding one more bounded coefficient pattern. It comes from removing the finite four-term search restriction and solving the complete linear parity support problem.

---

## 12. Proposition 88

For every empirical sixteen-cell law $\widehat p$ and rational P75 parameter box $B$:

1. the eleven canonical nontrivial even-parity probabilities define a finite feature map $h$;
2. the centered transfer quantity $D(c)=\min_a\|Ac-a\mathbf1\|_1$ is a norm on parity coefficient space;
3. every parity-linear P75 box support extremum occurs at a parameter-box vertex;
4. the strongest parity-linear full-law $L_\infty$ lower bound is the finite primal linear program in Section 5;
5. its exact dual is the zero-mass parity-residual program in Section 6;
6. every P87 witness is feasible inside the P88 class, so $L_{88}^{\mathrm{par}}(B)\ge L_{87}(B)$ pointwise;
7. there exist exact rational boxes and empirical laws for which the dominance is strict;
8. on the explicit common P86-P88 witness, matching exact rational primal and dual certificates prove

\[
\boxed{
L_{88}^{\mathrm{par}}(B)=\frac5{168}>\frac1{96}=L_{87}(B).
}
\]

---

## 13. Why P88 is a conceptual step rather than another enumeration

P86 and P87 answer finite-family questions. P88 changes the mathematical object.

Instead of asking which coefficient box to enumerate next, P88 asks for the support-function optimum over the entire real eleven-dimensional parity-linear space. The dual then exposes the geometry hidden by the earlier enumerations: the certificate is a distance between the empirical parity feature vector and the convex hull of box-vertex parity features, measured through the smallest zero-mass sixteen-cell perturbation compatible with those feature differences.

This gives a natural stopping point for the P83-P87 linear parity hierarchy. Future strengthening must add genuinely new observable information or leave the linear parity class, rather than merely increasing an integer coefficient bound.

---

## 14. Reproducibility record

Implementation:

`src/consciousness_bridge/complete_parity_linear_certificate.py`

Regression tests:

`tests/test_complete_parity_linear_certificate.py`

Equation provenance:

`docs/p88_equation_provenance.md`

The implementation uses exact `fractions.Fraction` arithmetic for empirical features, parameter-box vertices, parity-functional intervals, centered norms, dual weights, dual residuals, and the strict optimality certificate.

---

## 15. Scientific interpretation boundary

P88 is a conditional theorem about the declared P75 target-measurement family and the information carried by eleven parity observables. It establishes the strongest lower bound available from their linear span under the exact centered transfer norm.

It does **not** show that parity observables are complete for consciousness, that the P75 latent variable is experience, that every physical description has been exhausted, that quantum mechanics is incomplete, that consciousness is nonphysical, or that the physical-to-experiential bridge has been solved.
