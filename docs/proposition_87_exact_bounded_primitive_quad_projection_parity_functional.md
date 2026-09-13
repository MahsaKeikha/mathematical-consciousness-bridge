# Proposition 87: Exact Bounded Primitive Four-Event Projection-Parity Functional Certificate

## Status

**Proved conditional computational theorem.** P87 strengthens P86 for the same declared P75 four-view binary latent target-measurement family and the same full-law $L_\infty$ distance.

P86 audits the smallest non-uniform primitive magnitude pattern, `{1,1,1,2}`. P87 asks a different and stronger question at the **same four-event order**: if all nonzero primitive integer coefficient vectors with $|c_i|\le2$ are exhausted, can that completed bounded family detect a shared-parameter incompatibility that the full P86 certificate still underestimates?

The answer is yes.

P87 is a model-separation theorem. It does not identify the P75 latent state with consciousness, validate an alternative model after rejection, or close the physical-to-experiential bridge.

---

## 1. The mathematical gap closed by P87

P86 deliberately restricts the four-event coefficient magnitudes to

\[
\{1,1,1,2\}.
\]

That is the smallest non-uniform primitive pattern, but it is not the complete primitive coefficient family with entries bounded in magnitude by two.

P87 therefore fixes the finite coefficient alphabet

\[
\{-2,-1,1,2\}
\]

and retains exactly those vectors

\[
c=(c_1,c_2,c_3,c_4)
\]

with

\[
\gcd(|c_1|,|c_2|,|c_3|,|c_4|)=1.
\]

Vectors differing only by one global sign represent the same separating direction, so one global sign is removed by requiring the first coefficient to be positive.

This closes the complete nonzero primitive coefficient box

\[
0<|c_i|\le2
\]

at four-event order.

---

## 2. Exact family size

There are

\[
4^4=256
\]

nonzero coefficient vectors over `{-2,-1,1,2}`.

A vector is non-primitive exactly when all four coefficients have magnitude two. There are

\[
2^4=16
\]

such vectors. Therefore the primitive vectors number

\[
256-16=240.
\]

Quotienting by one global sign leaves

\[
\boxed{120}
\]

standard coefficient patterns per four-event subset.

The P83 parity coordinate family contains eleven canonical even-parity events. Hence the number of unordered four-event subsets is

\[
\binom{11}{4}=330.
\]

Therefore the complete P87 bounded primitive family contains

\[
\boxed{330\times120=39{,}600}
\]

exact functionals.

---

## 3. Canonical functional

For each

\[
J\subseteq\{0,1,2,3\},\qquad |J|\in\{2,3,4\},
\]

define the even-parity event

\[
H_J=\left\{x:\sum_{j\in J}x_j\equiv0\pmod2\right\}.
\]

Choose four distinct canonical view sets $J_1,J_2,J_3,J_4$ and a primitive coefficient vector satisfying

\[
0<|c_i|\le2.
\]

Define

\[
Q(p)=\sum_{i=1}^4 c_iP_p(H_{J_i}).
\]

The P87 family is the set of all such standard sign-normalized functionals.

---

## 4. Exact P75 parameter-box interval

Inside latent branch $s\in\{-,+\}$ write

\[
a_{j,s}=1-2q_{j,s}.
\]

Conditional independence in the declared P75 model gives the inherited parity identity

\[
P_s(H_J)=\frac{1+\prod_{j\in J}a_{j,s}}2.
\]

Therefore

\[
Q_s
=
\frac12\sum_{i=1}^4c_i
+
\frac12\sum_{i=1}^4c_i\prod_{j\in J_i}a_{j,s}.
\]

Each response coordinate enters with degree at most one. Thus $Q_s$ is multi-affine. Holding all but one coordinate fixed makes $Q_s$ affine in the remaining coordinate, so its minimum and maximum over that coordinate occur at the interval endpoints. Repeating coordinate by coordinate proves that every branch extremum over an axis-aligned rational box occurs at a vertex.

For latent prevalence $\pi$,

\[
Q=(1-\pi)Q_-+\pi Q_+,
\]

which is affine in $\pi$. Hence the prevalence endpoints also suffice.

Every P87 functional therefore has an exact rational model interval

\[
I_B(Q)=[Q_B^L,Q_B^U]
\]

obtained by finite endpoint enumeration.

---

## 5. Transfer to full-law distance

Define the sixteen-cell outcome coefficient

\[
g(x)=\sum_{i=1}^4c_i\mathbf1_{H_{J_i}}(x).
\]

For probability laws $p$ and $q$,

\[
\sum_x[p(x)-q(x)]=0.
\]

Therefore for any constant $a$,

\[
Q(p)-Q(q)
=
\sum_x[g(x)-a][p(x)-q(x)].
\]

By the triangle inequality,

\[
|Q(p)-Q(q)|
\le
\left(\sum_x|g(x)-a|\right)\|p-q\|_\infty.
\]

Define

\[
D(Q)=\min_a\sum_x|g(x)-a|.
\]

The finite absolute-deviation objective is minimized by a median of the sixteen coefficient values. Thus $D(Q)$ is exactly computable in integer/rational arithmetic.

If

\[
\Delta_Q
=
\operatorname{dist}(Q(\widehat p),I_B(Q)),
\]

then every P75 law $q$ generated in $B$ satisfies

\[
\boxed{
\|\widehat p-q\|_\infty
\ge
\frac{\Delta_Q}{D(Q)}.
}
\]

---

## 6. P87 certificate and dominance

Let

\[
L_{\mathrm{bp4}}(B)
=
\max_{Q\in\mathcal Q_{87}}
\frac{\operatorname{dist}(Q(\widehat p),I_B(Q))}{D(Q)},
\]

where $\mathcal Q_{87}$ is the complete 39,600-function bounded primitive family.

Define

\[
\boxed{
L_{87}(B)=\max\{L_{86}(B),L_{\mathrm{bp4}}(B)\}.
}
\]

Then

\[
L_{87}(B)\ge L_{86}(B)
\]

for every empirical law and every admissible rational P75 box.

### Proposition 87

For every empirical sixteen-cell law $\widehat p$ and rational P75 parameter box $B$:

1. all 39,600 standard P87 functional intervals are computed exactly;
2. every interval mismatch produces a valid full-law $L_\infty$ lower bound;
3. $L_{87}(B)$ is a valid lower bound on the distance from $\widehat p$ to every P75 law generated in $B$;
4. $L_{87}(B)\ge L_{86}(B)$ pointwise;
5. there exist exact rational boxes and empirical laws for which $L_{87}(B)>L_{86}(B)$.

---

## 7. Exact strict witness

Use the same exact rational box and empirical sixteen-cell law used in the P86 strict witness.

The P86 certificate on this box is

\[
\boxed{L_{86}(B)=\frac1{192}}.
\]

P87 exhaustively selects the functional

\[
Q=
P(H_{\{0,2\}})
-P(H_{\{1,3\}})
-2P(H_{\{1,2,3\}})
+2P(H_{\{0,1,2,3\}}).
\]

Its empirical value is

\[
Q(\widehat p)=-\frac{17}{24}.
\]

Exact endpoint enumeration over the P75 box gives

\[
I_B(Q)=\left[-\frac12,2\right].
\]

Therefore the empirical value lies below the admissible interval by

\[
\Delta_Q
=
-\frac12-\left(-\frac{17}{24}\right)
=
\frac5{24}.
\]

The exact centered coefficient calculation gives

\[
D(Q)=20,
\]

with deterministic center

\[
a=0.
\]

Hence

\[
\frac{\Delta_Q}{D(Q)}
=
\frac{5/24}{20}
=
\boxed{\frac1{96}}.
\]

Exhaustion of the complete 39,600-function P87 family attains this value. Consequently

\[
\boxed{
L_{86}(B)=\frac1{192}
<
L_{87}(B)=\frac1{96}.
}
\]

Together with the same witness's P85 value,

\[
\boxed{
L_{85}(B)=0
<
L_{86}(B)=\frac1{192}
<
L_{87}(B)=\frac1{96}.
}
\]

---

## 8. Why this is not just a larger brute-force list

P87 closes a specific completeness gap left intentionally open by P86. P86 establishes that the first non-uniform primitive four-event coefficient pattern can reveal information beyond P85. P87 asks whether that one magnitude pattern already exhausts all primitive four-event relations with coefficient magnitudes bounded by two.

The strict witness answers no.

The improvement comes from the primitive coefficient pattern

\[
(1,-1,-2,2),
\]

which is not in the P86 `{1,1,1,2}` family because it contains two coefficients of magnitude two. Thus P87 adds a mathematically defined completion at the same functional order rather than merely increasing event count.

---

## 9. Reproducibility record

Implementation:

`src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py`

Regression tests:

`tests/test_bounded_primitive_quad_projection_parity_functional_separation.py`

Equation provenance:

`docs/p87_equation_provenance.md`

The implementation uses exact `fractions.Fraction` arithmetic for the empirical law, P75 box endpoints, functional intervals, centered norms, and strict witness value. The standard family is exhaustively enumerated rather than sampled.

---

## 10. Scientific interpretation boundary

P87 proves a narrower statement than an ontology of consciousness. Under the declared P75 model and exact parameter-box assumptions, completing the primitive four-event coefficient family for $0<|c_i|\le2$ yields a strictly stronger certified model-distance lower bound on an exact witness.

It does not establish that consciousness is nonphysical, that a latent variable is experience, that parity observables are privileged experiential observables, that quantum mechanics is incomplete, or that the physical-to-experiential bridge has been solved.
