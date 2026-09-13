# Proposition 88: Exact Expanded Bounded Primitive Four-Event Projection-Parity Functional Certificate

## Status

**Proved conditional computational theorem.** P88 strengthens P87 for the same declared P75 four-view binary latent target-measurement family and the same full-law $L_\infty$ distance.

P87 closes the complete primitive four-event coefficient box

\[
0<|c_i|\le2.
\]

P88 asks the next finite question at the **same four-event order**: if the complete primitive coefficient box is enlarged to

\[
0<|c_i|\le3,
\]

can the enlarged family detect a shared-parameter incompatibility that the complete P87 certificate still underestimates?

The answer is yes.

P88 is a model-separation theorem. It does not identify the P75 latent state with consciousness, validate an alternative model after rejection, or close the physical-to-experiential bridge.

---

## 1. The mathematical gap closed by P88

P87 exhausts all nonzero primitive coefficient vectors over

\[
\{-2,-1,1,2\}^4
\]

modulo one global sign. It therefore completes a mathematically defined finite coefficient box, but it does not answer whether the first larger primitive box contains strictly stronger separating directions.

P88 enlarges the alphabet to

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

Vectors differing only by one global sign represent the same separating direction, so the standard representative is chosen with first coefficient positive.

This closes the complete nonzero primitive coefficient box

\[
\boxed{0<|c_i|\le3}
\]

at four-event order.

---

## 2. Exact family size

There are

\[
6^4=1296
\]

nonzero coefficient vectors over `{-3,-2,-1,1,2,3}`.

Because the largest magnitude is three, a non-primitive vector can have common divisor only two or three.

All entries are divisible by two exactly when every coefficient is in `{-2,2}`, giving

\[
2^4=16
\]

vectors.

All entries are divisible by three exactly when every coefficient is in `{-3,3}`, giving another

\[
2^4=16
\]

vectors.

These two sets are disjoint. Hence the primitive vectors number

\[
1296-16-16=1264.
\]

Quotienting by one global sign leaves

\[
\boxed{632}
\]

standard coefficient patterns per four-event subset.

The P83 parity coordinate family contains eleven canonical even-parity events, so the number of unordered four-event subsets is

\[
\binom{11}{4}=330.
\]

Therefore the complete P88 family contains

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

Choose four distinct canonical view sets $J_1,J_2,J_3,J_4$ and a primitive integer coefficient vector satisfying

\[
0<|c_i|\le3.
\]

Define

\[
Q(p)=\sum_{i=1}^4 c_iP_p(H_{J_i}).
\]

The P88 family is the set of all such standard sign-normalized functionals.

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

Each response coordinate enters with degree at most one, so $Q_s$ is multi-affine. Every branch extremum over an axis-aligned rational box is therefore attained at a response-coordinate vertex.

For latent prevalence $\pi$,

\[
Q=(1-\pi)Q_-+\pi Q_+,
\]

which is affine in $\pi$. The prevalence endpoints therefore suffice as well.

Every P88 functional has an exact rational model interval

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

Therefore, for any constant $a$,

\[
Q(p)-Q(q)
=
\sum_x[g(x)-a][p(x)-q(x)].
\]

Hence

\[
|Q(p)-Q(q)|
\le
\left(\sum_x|g(x)-a|\right)\|p-q\|_\infty.
\]

Define

\[
D(Q)=\min_a\sum_x|g(x)-a|.
\]

For the finite sixteen-cell coefficient list, a median minimizes the absolute-deviation objective. Thus $D(Q)$ is exactly computable.

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

## 6. P88 certificate and dominance

Let

\[
L_{\mathrm{bp4},3}(B)
=
\max_{Q\in\mathcal Q_{88}}
\frac{\operatorname{dist}(Q(\widehat p),I_B(Q))}{D(Q)},
\]

where $\mathcal Q_{88}$ is the complete 208,560-function primitive family with $0<|c_i|\le3$.

Define

\[
\boxed{
L_{88}(B)=\max\{L_{87}(B),L_{\mathrm{bp4},3}(B)\}.
}
\]

Then

\[
L_{88}(B)\ge L_{87}(B)
\]

for every empirical law and every admissible rational P75 box.

In fact, the P87 coefficient family is a subset of the P88 family, so the enlarged four-event search family itself cannot be weaker.

### Proposition 88

For every empirical sixteen-cell law $\widehat p$ and rational P75 parameter box $B$:

1. all 208,560 standard P88 functional intervals are computed exactly;
2. every interval mismatch produces a valid full-law $L_\infty$ lower bound;
3. $L_{88}(B)$ is a valid lower bound on the distance from $\widehat p$ to every P75 law generated in $B$;
4. $L_{88}(B)\ge L_{87}(B)$ pointwise;
5. there exist exact rational boxes and empirical laws for which $L_{88}(B)>L_{87}(B)$.

---

## 7. Exact strict witness

Use the same rational P75 parameter box and empirical sixteen-cell law used for the P86 and P87 strict hierarchy witnesses.

The complete P87 certificate on this box is

\[
\boxed{L_{87}(B)=\frac1{96}}.
\]

P88 exhaustively selects the functional

\[
Q=
P(H_{\{0,2\}})
-P(H_{\{1,3\}})
-3P(H_{\{1,2,3\}})
+2P(H_{\{0,1,2,3\}}).
\]

Its empirical value is

\[
Q(\widehat p)=-\frac{11}{8}.
\]

Exact endpoint enumeration over the P75 box gives

\[
I_B(Q)=[-1,2].
\]

Therefore the empirical value lies below the admissible interval by

\[
\Delta_Q
=
-1-\left(-\frac{11}{8}\right)
=
\frac38.
\]

The exact centered coefficient calculation gives

\[
D(Q)=24,
\]

with a minimizing center

\[
a=-1.
\]

Hence

\[
\frac{\Delta_Q}{D(Q)}
=
\frac{3/8}{24}
=
\boxed{\frac1{64}}.
\]

Exhaustion of the complete 208,560-function P88 family attains this value. Consequently

\[
\boxed{
L_{87}(B)=\frac1{96}
<
L_{88}(B)=\frac1{64}.
}
\]

Together with the earlier exact hierarchy on the same witness,

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

## 8. Why P88 is not cosmetic coefficient inflation

P88 does not simply append arbitrary large weights. It closes the **first larger complete primitive coefficient box** after P87 while holding fixed:

- the four-event functional order;
- the eleven canonical P83 parity coordinates;
- the P75 latent measurement family;
- the exact rational box-certification method;
- the full-law $L_\infty$ target metric.

The strict witness uses coefficient pattern

\[
(1,-1,-3,2),
\]

which cannot occur in P87 because one coefficient has magnitude three. Its strict improvement proves that completing the $|c_i|\le2$ box does not exhaust the separating power available at the same four-event order.

---

## 9. Reproducibility record

Implementation:

`src/consciousness_bridge/expanded_bounded_primitive_quad_projection_parity_functional_separation.py`

Regression tests:

`tests/test_expanded_bounded_primitive_quad_projection_parity_functional_separation.py`

Equation provenance:

`docs/p88_equation_provenance.md`

Frontier figure:

`docs/figures/p88_exact_expanded_bounded_primitive_quad_projection_parity.svg`

The implementation uses exact `fractions.Fraction` arithmetic for the empirical law, P75 box endpoints, functional intervals, centered norms, and strict witness value. The complete 208,560-function family is exhaustively enumerated rather than sampled.

---

## 10. Scientific interpretation boundary

P88 proves a narrower statement than an ontology of consciousness. Under the declared P75 model and exact parameter-box assumptions, enlarging the complete primitive four-event coefficient box from $0<|c_i|\le2$ to $0<|c_i|\le3$ yields a strictly stronger certified model-distance lower bound on an exact rational witness.

It does not establish that consciousness is nonphysical, that a latent variable is experience, that parity observables are privileged experiential observables, that quantum mechanics is incomplete, or that the physical-to-experiential bridge has been solved.
