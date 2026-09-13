# Proposition 87: Exact Bounded-Primitive Four-Event Projection-Parity Functional Certificate

## Status

**Proved conditional computational theorem.** P87 strengthens P86 for the same declared P75 four-view binary latent family and the same full-law $L_\infty$ distance.

P86 audits the smallest non-uniform primitive magnitude multiset $\{1,1,1,2\}$ across four distinct canonical parity observables. P87 closes the next finite combinatorial gap: it exhausts **every** primitive nonzero integer coefficient vector satisfying

\[
0<|c_i|\le 2,
\]

modulo one irrelevant global sign.

The resulting standard family contains **39,600 exact four-event functionals**. On an exact rational witness, the complete P86 lower bound is $1/192$ while P87 certifies $1/96$.

P87 is a model-separation theorem. It does not identify the P75 latent state with consciousness, validate an alternative model after rejection, prove consciousness is nonphysical, or close the physical-to-experiential bridge.

---

## 1. Scientific question

Can the complete P86 certificate remain suboptimal because its four-event coefficient family contains only the magnitude pattern $\{1,1,1,2\}$, even though a different primitive weighting with the same coefficient cap $|c_i|\le2$ gives a strictly stronger exact separation certificate?

The answer is yes.

P87 therefore replaces a single hand-selected magnitude pattern with the complete primitive four-coefficient box at radius two.

---

## 2. Canonical parity coordinates

For

\[
J\subseteq\{0,1,2,3\},\qquad |J|\in\{2,3,4\},
\]

define the canonical even-parity event

\[
H_J=\left\{x:\sum_{j\in J}x_j\equiv0\pmod2\right\}.
\]

There are

\[
\binom42+\binom43+\binom44=6+4+1=11
\]

such coordinates.

Choose four distinct view sets $J_1,J_2,J_3,J_4$ and a primitive coefficient vector

\[
c=(c_1,c_2,c_3,c_4)\in\{-2,-1,1,2\}^4,
\qquad
\gcd(|c_1|,|c_2|,|c_3|,|c_4|)=1.
\]

Define

\[
Q_c(p)=\sum_{i=1}^4 c_iP_p(H_{J_i}).
\]

Multiplying all coefficients by $-1$ changes neither the interval-distance numerator nor the centered transfer denominator, so one global sign is redundant. P87 fixes the first coefficient positive.

---

## 3. Exact enumeration of the P87 family

There are $4^4=256$ nonzero vectors in $\{-2,-1,1,2\}^4$. A vector is non-primitive exactly when all four magnitudes equal two. There are $2^4=16$ such vectors. Hence the number of primitive vectors before global-sign normalization is

\[
256-16=240.
\]

Every primitive vector occurs in a distinct pair $\{c,-c\}$, so fixing one global sign gives

\[
\boxed{240/2=120}
\]

standard coefficient patterns per four-event subset.

There are

\[
\binom{11}{4}=330
\]

four-element subsets of the canonical parity coordinates. Therefore the complete P87 family has

\[
\boxed{330\times120=39{,}600}
\]

standard functionals.

This is exhaustive for the declared class: four distinct canonical even-parity observables, four nonzero primitive integer coefficients, and coefficient cap $|c_i|\le2$.

---

## 4. Exact P75 box interval

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
Q_{c,s}
=
\frac12\sum_{i=1}^4c_i
+
\frac12\sum_{i=1}^4c_i\prod_{j\in J_i}a_{j,s}.
\]

Each response coordinate appears with degree at most one, so $Q_{c,s}$ is multi-affine. Holding all but one coordinate fixed leaves an affine function of the remaining coordinate; its extrema on an interval occur at the endpoints. Repeating coordinate by coordinate proves that every branch extremum on an axis-aligned rational response box occurs at a vertex.

For latent prevalence $\pi$,

\[
Q_c=(1-\pi)Q_{c,-}+\pi Q_{c,+}.
\]

After branchwise extremization, both lower and upper envelopes are affine in $\pi$, so prevalence endpoints suffice as well.

Therefore every P87 functional has an exact rational P75 box interval

\[
I_B(Q_c)=[Q_{c,B}^L,Q_{c,B}^U].
\]

No local floating-point optimizer is used.

---

## 5. Exact transfer to full-law $L_\infty$ distance

Define the sixteen-cell outcome coefficient

\[
g_c(x)=\sum_{i=1}^4c_i\mathbf1_{H_{J_i}}(x).
\]

For probability laws $p$ and $q$,

\[
\sum_x[p(x)-q(x)]=0.
\]

Hence for any constant $a$,

\[
Q_c(p)-Q_c(q)
=
\sum_x[g_c(x)-a][p(x)-q(x)].
\]

The triangle inequality gives

\[
|Q_c(p)-Q_c(q)|
\le
\left(\sum_x|g_c(x)-a|\right)\|p-q\|_\infty.
\]

Define

\[
D(Q_c)=\min_a\sum_x|g_c(x)-a|.
\]

For finitely many scalar values the absolute-deviation objective is minimized by any median; evaluating the finitely many exact integer coefficient values therefore gives $D(Q_c)$ exactly.

If the empirical functional value lies a distance

\[
\Delta_c=
\operatorname{dist}\!\left(Q_c(\widehat p),I_B(Q_c)\right)
\]

outside the P75 box interval, then every P75 law $q$ generated in $B$ obeys

\[
\boxed{
\|\widehat p-q\|_\infty\ge\frac{\Delta_c}{D(Q_c)}.
}
\]

---

## 6. Complete P87 certificate

Let

\[
L_{\mathrm{bp4}}(B)=
\max_{Q_c\in\mathcal Q_{87}}
\frac{\operatorname{dist}(Q_c(\widehat p),I_B(Q_c))}{D(Q_c)},
\]

where $\mathcal Q_{87}$ is the complete 39,600-function family.

Define

\[
\boxed{L_{87}(B)=\max\{L_{86}(B),L_{\mathrm{bp4}}(B)\}.}
\]

The explicit maximum retains the full inherited P86 chain, including the lower-order P83-P85 certificates, while adding the complete bounded-primitive four-event family.

Therefore

\[
\boxed{L_{87}(B)\ge L_{86}(B)}
\]

for every empirical law and every admissible rational P75 box.

### Proposition 87

For every empirical sixteen-cell law $\widehat p$ and rational P75 parameter box $B$:

1. the standard P87 family contains exactly 39,600 sign-normalized primitive four-event functionals with $0<|c_i|\le2$;
2. every P87 functional has an exact rational P75 box interval obtained by endpoint enumeration;
3. every interval mismatch transfers to a valid full-law $L_\infty$ lower bound through the exact centered coefficient norm;
4. $L_{87}(B)$ is a valid lower bound on the distance from $\widehat p$ to every P75 law generated in $B$;
5. $L_{87}(B)\ge L_{86}(B)$ pointwise;
6. there exist exact rational boxes and empirical laws for which $L_{87}(B)>L_{86}(B)$.

---

## 7. Exact rational strict witness

Use the P75 parameter order

\[
(\pi,q_{1,-},q_{1,+},q_{2,-},q_{2,+},q_{3,-},q_{3,+},q_{4,-},q_{4,+}).
\]

Take

\[
B_L=
\left(
0,\frac14,\frac12,\frac14,\frac34,\frac12,\frac12,\frac14,\frac34
\right),
\]

\[
B_U=
\left(
0,1,1,1,\frac34,1,\frac34,1,1
\right).
\]

Let the empirical sixteen-cell law be the exact count law

\[
(0,1,0,2,0,2,1,3,3,1,0,5,0,3,0,3)/24.
\]

The complete P86 certificate on this box is

\[
\boxed{L_{86}(B)=\frac1{192}}.
\]

Now use the primitive P87 functional

\[
Q=
P(H_{\{0,2\}})
-P(H_{\{1,3\}})
-2P(H_{\{1,2,3\}})
+2P(H_{\{0,1,2,3\}}).
\]

Its coefficient magnitudes are $\{1,1,2,2\}$, so it is outside the P86 $\{1,1,1,2\}$ family while remaining primitive and inside the P87 coefficient box.

For the empirical law,

\[
Q(\widehat p)=-\frac{17}{24}.
\]

Exact endpoint enumeration gives

\[
I_B(Q)=\left[-\frac12,2\right].
\]

Hence

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
\qquad a=0
\]

for the deterministic minimizing center returned by the implementation. Therefore

\[
L_{\mathrm{bp4}}(B)
\ge
\frac{5/24}{20}
=
\boxed{\frac1{96}}.
\]

Exhausting all 39,600 P87 functionals attains this value, so

\[
\boxed{
L_{86}(B)=\frac1{192}
<
L_{87}(B)=\frac1{96}.
}
\]

This is an exact factor-of-two improvement on the same box and empirical law.

---

## 8. Why P87 is not merely a larger search

P87 closes a precisely declared finite family rather than adding an isolated successful functional. Every primitive nonzero four-coefficient vector with maximum magnitude two is included, and global-sign duplicates are removed exactly.

The strict witness uses the magnitude pattern $\{1,1,2,2\}$, which P86 does not contain. Thus the improvement demonstrates a genuine gap in the P86 coefficient family rather than numerical retuning of the same certificate.

At the same time P87 makes no claim of optimality over arbitrary integer coefficients. Primitive patterns such as $\{1,1,1,3\}$ lie outside the declared coefficient cap and remain available for later study. The proposition is complete for its stated bounded family, not for all linear functionals.

---

## 9. Global branch-and-bound use

P87 can be inserted into the same certified P78-P86 parameter-box branch-and-bound architecture. At every finite iteration, active boxes cover all unpruned candidate minimizer regions; each active box has a rigorous P87 lower bound; and evaluated parameter points provide valid upper bounds.

P87 changes only the box lower-bound oracle. It does not alter the P75 model family, the P78 coverage invariant, the P79 one-sided sampling-radius direction, or the global convergence logic.

---

## 10. Scientific interpretation boundary

P87 does **not** prove that:

- consciousness is nonphysical;
- the P75 latent variable is a conscious state;
- parity coordinates are privileged experiential observables;
- failure of the P75 latent model validates another latent model;
- a stronger four-event certificate implies an extra physical or experiential dimension;
- quantum mechanics is incomplete;
- the physical-to-experiential bridge has been solved.

It proves a narrower statement: under the declared P75 model and exact rational box assumptions, the complete primitive four-event coefficient family with $0<|c_i|\le2$ can expose shared-parameter incompatibility more strongly than the complete P86 certificate.

---

## 11. Executable record

Implementation:

`src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py`

Regression tests:

`tests/test_bounded_primitive_quad_projection_parity_functional_separation.py`

Equation provenance:

`docs/p87_equation_provenance.md`

Frontier figure:

`docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg`
