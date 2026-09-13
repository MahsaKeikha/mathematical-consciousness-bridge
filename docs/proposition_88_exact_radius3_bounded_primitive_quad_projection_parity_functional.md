# Proposition 88: Exact Radius-3 Bounded Primitive Four-Event Projection-Parity Functional Certificate

## Status

**Proved conditional computational theorem.** P88 strengthens P87 for the same declared P75 four-view binary latent target-measurement family and the same full-law $L_\infty$ distance.

P87 completes the nonzero primitive four-event coefficient box with

\[
0<|c_i|\le2.
\]

P88 asks the next exact same-order question: if that coefficient box is enlarged to

\[
0<|c_i|\le3,
\]

does the complete primitive radius-3 family certify a strictly larger distance from the same declared P75 model family?

The answer is yes.

P88 is a model-separation theorem. It does not identify the P75 latent state with consciousness, validate an alternative model after rejection, or close the physical-to-experiential bridge.

---

## 1. The mathematical gap left by P87

P87 proves that coefficient completeness matters even when the number of parity events is held fixed at four. It exhausts all primitive vectors over

\[
\{-2,-1,1,2\}.
\]

That closes the radius-2 coefficient box, but it leaves open whether larger primitive integer contrasts at the same event order can expose additional shared-parameter incompatibility.

P88 therefore fixes the radius-3 alphabet

\[
\{-3,-2,-1,1,2,3\}
\]

and retains exactly those vectors

\[
c=(c_1,c_2,c_3,c_4)
\]

with

\[
\gcd(|c_1|,|c_2|,|c_3|,|c_4|)=1.
\]

Vectors differing only by a global sign describe the same separating direction. P88 uses the standard normalization that the first coefficient is positive.

---

## 2. Exact family size

There are

\[
6^4=1296
\]

nonzero coefficient vectors over the radius-3 alphabet.

A vector is nonprimitive only if all four coefficients share a nontrivial common divisor. With the allowed magnitudes $1,2,3$, the only possibilities are:

- all four coefficients have magnitude $2$, giving $2^4=16$ vectors divisible by $2$;
- all four coefficients have magnitude $3$, giving $2^4=16$ vectors divisible by $3$.

These two sets are disjoint. Hence the primitive vectors number

\[
1296-16-16=1264.
\]

Quotienting by global sign leaves

\[
\boxed{632}
\]

standard primitive coefficient patterns per four-event subset.

The P83 parity coordinate family contains eleven canonical even-parity events. There are therefore

\[
\binom{11}{4}=330
\]

unordered four-event subsets. The complete P88 family contains

\[
\boxed{330\times632=208{,}560}
\]

exact functionals.

---

## 3. Canonical P88 functional

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
0<|c_i|\le3.
\]

Define

\[
Q(p)=\sum_{i=1}^4c_iP_p(H_{J_i}).
\]

P88 exhausts the complete standard sign-normalized radius-3 family.

---

## 4. Exact P75 parameter-box interval

Inside latent branch $s\in\{-,+\}$ write

\[
a_{j,s}=1-2q_{j,s}.
\]

Conditional independence in the declared P75 model gives

\[
P_s(H_J)=\frac{1+\prod_{j\in J}a_{j,s}}2.
\]

Thus

\[
Q_s
=
\frac12\sum_{i=1}^4c_i
+
\frac12\sum_{i=1}^4c_i\prod_{j\in J_i}a_{j,s}.
\]

Each response coordinate enters with degree at most one. Therefore $Q_s$ is multi-affine, and every minimum or maximum over an axis-aligned rational response box occurs at a vertex.

For latent prevalence $\pi$,

\[
Q=(1-\pi)Q_-+\pi Q_+,
\]

which is affine in $\pi$. The prevalence endpoints therefore suffice as well.

Every P88 functional has an exact rational model interval

\[
I_B(Q)=[Q_B^L,Q_B^U]
\]

computed by finite endpoint enumeration.

---

## 5. Transfer to full-law $L_\infty$ distance

Define the sixteen-cell outcome coefficient

\[
g(x)=\sum_{i=1}^4c_i\mathbf1_{H_{J_i}}(x).
\]

For probability laws $p$ and $q$,

\[
\sum_x[p(x)-q(x)]=0.
\]

Hence for any constant $a$,

\[
Q(p)-Q(q)
=
\sum_x[g(x)-a][p(x)-q(x)].
\]

Therefore

\[
|Q(p)-Q(q)|
\le
\left(\sum_x|g(x)-a|\right)\|p-q\|_\infty.
\]

Define

\[
D(Q)=\min_a\sum_x|g(x)-a|.
\]

A median of the sixteen coefficient values minimizes this finite absolute-deviation objective, so $D(Q)$ is exactly computable.

If

\[
\Delta_Q=\operatorname{dist}(Q(\widehat p),I_B(Q)),
\]

then every P75 law $q$ generated in $B$ satisfies

\[
\boxed{
\|\widehat p-q\|_\infty\ge\frac{\Delta_Q}{D(Q)}.
}
\]

---

## 6. P88 certificate and dominance

Let

\[
L_{\mathrm{bp4},3}(B)
=
\max_{Q\in\mathcal Q_{88}}
\frac{\operatorname{dist}(Q(\widehat p),I_B(Q))}{D(Q)},
\]

where $\mathcal Q_{88}$ is the complete 208,560-function radius-3 primitive family.

Define

\[
\boxed{
L_{88}(B)=\max\{L_{87}(B),L_{\mathrm{bp4},3}(B)\}.
}
\]

Because the complete radius-2 primitive family is a subset of the radius-3 family,

\[
L_{88}(B)\ge L_{87}(B)
\]

for every empirical law and every admissible rational P75 box.

### Proposition 88

For every empirical sixteen-cell law $\widehat p$ and rational P75 parameter box $B$:

1. all 208,560 standard radius-3 primitive four-event functional intervals are computed exactly;
2. every interval mismatch gives a valid full-law $L_\infty$ lower bound;
3. $L_{88}(B)$ is a valid lower bound on the distance from $\widehat p$ to every P75 law generated in $B$;
4. $L_{88}(B)\ge L_{87}(B)$ pointwise;
5. there exist exact rational boxes and empirical laws for which $L_{88}(B)>L_{87}(B)$.

---

## 7. Exact strict witness

Use the same exact rational P75 box and empirical sixteen-cell law used for the P86 and P87 strict witnesses.

The earlier certified values are

\[
L_{86}(B)=\frac1{192},
\qquad
L_{87}(B)=\frac1{96}.
\]

Exhaustion of the complete P88 family selects

\[
\boxed{
Q=
P(H_{\{0,2\}})
-P(H_{\{1,3\}})
-3P(H_{\{1,2,3\}})
+2P(H_{\{0,1,2,3\}}).
}
\]

Its empirical value is

\[
Q(\widehat p)=-\frac{11}{8}.
\]

Exact P75 endpoint enumeration gives

\[
I_B(Q)=[-1,2].
\]

The empirical value lies below that interval by

\[
\Delta_Q
=
-1-\left(-\frac{11}{8}\right)
=
\frac38.
\]

The exact centered coefficient calculation gives

\[
D(Q)=24
\]

with a minimizing center

\[
a=-1.
\]

Therefore

\[
\frac{\Delta_Q}{D(Q)}
=
\frac{3/8}{24}
=
\boxed{\frac1{64}}.
\]

Exhaustion of all 208,560 standard P88 functionals attains this value. Hence

\[
\boxed{
L_{87}(B)=\frac1{96}
<
L_{88}(B)=\frac1{64}.
}
\]

Together with the earlier exact witness values,

\[
\boxed{
L_{85}(B)=0
<
L_{86}(B)=\frac1{192}
<
L_{87}(B)=\frac1{96}
<
L_{88}(B)=\frac1{64}.
}
\]

---

## 8. Why P88 is not merely a larger search

P88 closes a mathematically specified coefficient-radius gap. P87 established completeness only inside the radius-2 primitive box. P88 enlarges that box by exactly one integer radius while keeping the event order, target family, distance metric, exact interval method, and transfer inequality fixed.

The strict improvement is produced by the primitive coefficient pattern

\[
(1,-1,-3,2),
\]

which is unavailable to P87 because one coefficient has magnitude three.

Therefore the gain isolates a genuine new degree of separating power from coefficient amplitude, rather than confounding it with higher event order or a changed model family.

---

## 9. Reproducibility record

Implementation:

`src/consciousness_bridge/bounded_primitive_radius3_quad_projection_parity_functional_separation.py`

Regression tests:

`tests/test_bounded_primitive_radius3_quad_projection_parity_functional_separation.py`

Equation provenance:

`docs/p88_equation_provenance.md`

The implementation uses exact `fractions.Fraction` arithmetic for empirical probabilities, parameter-box endpoint evaluation, interval gaps, centered transfer norms, and the strict witness. The declared 208,560-function family is exhaustively enumerated rather than sampled.

---

## 10. Scientific interpretation boundary

P88 proves a narrower statement than an ontology of consciousness. Under the declared P75 model and exact rational parameter-box assumptions, expanding the complete primitive four-event coefficient family from radius two to radius three yields a strictly stronger certified model-distance lower bound on an exact witness.

It does not establish that consciousness is nonphysical, that a latent variable is experience, that parity observables are privileged experiential observables, that quantum mechanics is incomplete, or that the physical-to-experiential bridge has been solved.
