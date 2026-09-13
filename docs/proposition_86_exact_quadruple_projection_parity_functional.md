# Proposition 86: Exact Four-Event Projection-Parity Functional Certificate

## Status

**Proved conditional computational theorem.** P86 strengthens P85 for the same declared P75 four-view binary latent family and the same full-law $L_\infty$ distance.

P83 tests one parity observable at a time. P84 retains shared P75 parameters across two parity observables. P85 extends the exact audit to signed three-event functionals. P86 asks the next finite question: **can a signed four-event relation yield a strictly sharper shared-parameter incompatibility certificate than the complete P85 hierarchy on the same rational parameter box?**

The answer is yes.

P86 is a model-separation result. It does not identify the P75 latent state with consciousness, does not validate an alternative model after rejection, does not prove consciousness is nonphysical, and does not close the physical-to-experiential bridge.

---

## Plain-language meaning

Passing lower-order or weaker certificates does not make the declared model maximally compatible with every larger relation among the same observables. A four-event linear relation can constrain one shared parameter assignment more strongly than the complete certificate available through P85.

P86 makes that additional constraint exact and auditable.

For the strict exact-rational witness in the repository:

- the complete P85 lower bound is $5/48$;
- one P86 four-event functional has empirical value $-9/8$;
- its exact P75 box range is the singleton $[0,0]$;
- the exact interval gap is $9/8$;
- the centered coefficient norm is $8$;
- therefore the new four-event lower bound is

\[
\frac{9/8}{8}=\boxed{\frac{9}{64}}.
\]

Since

\[
\frac{5}{48}<\frac{9}{64},
\]

P86 improves the complete P85 certificate on the same exact rational input by

\[
\boxed{\frac{7}{192}}.
\]

---

## 1. Canonical parity coordinates

For each view set

\[
J\subseteq\{0,1,2,3\},
\qquad |J|\in\{2,3,4\},
\]

define the canonical even-parity event

\[
H_J=\left\{x:\sum_{j\in J}x_j\equiv0\pmod2\right\}.
\]

There are

\[
\binom42+\binom43+\binom44=6+4+1=11
\]

canonical view sets.

P86 selects four distinct view sets $J_1,J_2,J_3,J_4$ and signs

\[
\sigma_i\in\{-1,+1\}.
\]

Multiplying every sign by $-1$ reverses the functional without changing the absolute separation certificate, so the first sign is normalized to $+1$. The standard family therefore contains

\[
\binom{11}{4}2^3
=330\cdot8
=\boxed{2640}
\]

functionals.

For one such choice define

\[
Q(p)=\sum_{i=1}^4\sigma_i P_p(H_{J_i}).
\]

---

## 2. Exact P75 branch formula

Inside latent branch $s\in\{-,+\}$ define

\[
a_{j,s}=1-2q_{j,s}.
\]

The parity identity inherited from P83-P85 is

\[
P_s(H_J)=\frac{1+\prod_{j\in J}a_{j,s}}{2}.
\]

Hence

\[
Q_s
=
\frac12\sum_{i=1}^4\sigma_i
+
\frac12\sum_{i=1}^4
\sigma_i\prod_{j\in J_i}a_{j,s}.
\]

Every response coordinate appears with degree at most one in every monomial. Therefore $Q_s$ is multi-affine in the response coordinates contained in

\[
U=J_1\cup J_2\cup J_3\cup J_4.
\]

A multi-affine function on an axis-aligned box reaches its extrema at box vertices. Because there are only four observed views, at most

\[
2^4=16
\]

common endpoint assignments are required per latent branch.

This is exact extremization, not a floating-point relaxation or local optimization claim.

---

## 3. Exact full-box interval

Let the exact branch intervals be

\[
Q_-\in[m_-,M_-],
\qquad
Q_+\in[m_+,M_+].
\]

For latent prevalence $\pi$,

\[
Q=(1-\pi)Q_-+\pi Q_+.
\]

The minus-branch and plus-branch response coordinates are disjoint, and prevalence is a separate coordinate. After branchwise exact extremization, the lower and upper envelopes are affine in $\pi$. Their extrema therefore occur at the prevalence endpoints.

For every rational P75 parameter box $B$, P86 computes an exact rational interval

\[
I_B(Q)=[Q_B^L,Q_B^U].
\]

---

## 4. Exact transfer to full-law $L_\infty$ distance

Define the sixteen-cell coefficient

\[
g_Q(x)=\sum_{i=1}^4\sigma_i\mathbf1_{H_{J_i}}(x).
\]

Then for any probability laws $p$ and $q$,

\[
Q(p)-Q(q)=\sum_x g_Q(x)[p(x)-q(x)].
\]

Because both laws have total mass one,

\[
\sum_x[p(x)-q(x)]=0.
\]

Thus for every constant $c$,

\[
Q(p)-Q(q)
=
\sum_x[g_Q(x)-c][p(x)-q(x)].
\]

Applying the triangle inequality gives

\[
|Q(p)-Q(q)|
\le
\left(\sum_x|g_Q(x)-c|\right)\|p-q\|_\infty.
\]

P86 uses the exact best centered coefficient norm

\[
\boxed{
D(Q)=\min_c\sum_x|g_Q(x)-c|.
}
\]

For finitely many coefficients, every median minimizes the sum of absolute deviations. The implementation evaluates the finite set of distinct integer coefficient values exactly and returns the minimum norm together with one deterministic optimal center.

If the empirical functional value lies a distance

\[
\Delta_Q
=
\operatorname{dist}\left(Q(\widehat p),I_B(Q)\right)
\]

outside its exact P75 box interval, every P75 law $q$ generated in $B$ obeys

\[
\boxed{
\|\widehat p-q\|_\infty
\ge
\frac{\Delta_Q}{D(Q)}.
}
\]

---

## 5. P86 box certificate

Let $\mathcal Q_{86}$ denote the 2640 standard sign-normalized four-event functionals. Define

\[
L_{\mathrm{quad}}(B)
=
\max_{Q\in\mathcal Q_{86}}
\frac{
\operatorname{dist}\left(Q(\widehat p),I_B(Q)\right)
}{D(Q)}.
\]

P86 defines

\[
\boxed{
L_{86}(B)=\max\{L_{85}(B),L_{\mathrm{quad}}(B)\}.
}
\]

Therefore

\[
\boxed{L_{86}(B)\ge L_{85}(B)}
\]

for every empirical sixteen-cell law and every admissible rational P75 parameter box.

### Proposition 86

For every empirical sixteen-cell law $\widehat p$ and every rational P75 parameter box $B$:

1. each of the 2640 standard four-event functional intervals is computed exactly;
2. each four-event mismatch yields a valid full-law $L_\infty$ lower bound through the exact centered coefficient norm;
3. $L_{86}(B)$ is a valid lower bound on the distance from $\widehat p$ to every P75 law generated in $B$;
4. $L_{86}(B)\ge L_{85}(B)$ pointwise;
5. there exist exact rational boxes and empirical laws for which $L_{86}(B)>L_{85}(B)$.

---

## 6. Proof

### Step 1: exact branch extrema

Each canonical even-parity probability is a constant plus one product of distinct branch response coordinates. A signed sum of four such probabilities is therefore multi-affine. Multi-affine extrema over a rectangular parameter domain occur at endpoint vertices. The branch intervals are exact.

### Step 2: exact latent-mixture extrema

The minus-branch and plus-branch response coordinates are disjoint. Once each branch is extremized, the latent mixture is affine in prevalence. Its extrema occur at prevalence endpoints. Therefore $I_B(Q)$ is exact.

### Step 3: centered coefficient inequality

For any constant $c$,

\[
\sum_xc[p(x)-q(x)]=0.
\]

Hence

\[
Q(p)-Q(q)
=
\sum_x[g_Q(x)-c][p(x)-q(x)].
\]

The triangle inequality yields

\[
|Q(p)-Q(q)|
\le
\sum_x|g_Q(x)-c|\,\|p-q\|_\infty.
\]

Minimizing over $c$ gives the exact transfer denominator $D(Q)$.

### Step 4: distance to the exact model interval

Every P75 law generated in $B$ produces a functional value in $I_B(Q)$. If the empirical value is $\Delta_Q$ outside that interval, every such model law must change the functional by at least $\Delta_Q$. Step 3 gives

\[
\|\widehat p-q\|_\infty\ge\Delta_Q/D(Q).
\]

### Step 5: pointwise dominance

P86 is the maximum of the complete P85 certificate and the new four-event family, so

\[
L_{86}(B)\ge L_{85}(B)
\]

identically.

### Step 6: strictness

The exact rational witness in Section 7 has

\[
L_{85}(B)=\frac5{48}
<
\frac9{64}=L_{86}(B).
\]

Therefore P86 strictly improves P85 on at least one admissible input.

$\square$

---

## 7. Exact rational strict witness

Use P75 parameter order

\[
(\pi,q_{1,-},q_{1,+},q_{2,-},q_{2,+},q_{3,-},q_{3,+},q_{4,-},q_{4,+}).
\]

Take the rational box

\[
B_L=
\left(
0,\frac12,0,0,0,\frac12,\frac12,0,0
\right),
\]

\[
B_U=
\left(
0,1,\frac12,\frac12,1,\frac12,\frac12,1,0
\right).
\]

Using zero-based observed-cell indices, let the empirical law place mass

\[
\widehat p(0011)=\frac3{16},
\qquad
\widehat p(1000)=\frac38,
\]

\[
\widehat p(1100)=\frac3{16},
\qquad
\widehat p(1101)=\frac14,
\]

and zero mass on the other twelve cells.

The complete implemented P85 hierarchy gives

\[
\boxed{L_{85}(B)=\frac5{48}}.
\]

Now use the four-event functional

\[
\boxed{
Q
=
P(H_{\{0,2\}})
-P(H_{\{2,3\}})
+P(H_{\{0,1,2\}})
-P(H_{\{1,2,3\}}).
}
\]

For the empirical law,

\[
P(H_{\{0,2\}})=0,
\qquad
P(H_{\{2,3\}})=\frac34,
\]

\[
P(H_{\{0,1,2\}})=\frac7{16},
\qquad
P(H_{\{1,2,3\}})=\frac{13}{16}.
\]

Therefore

\[
Q(\widehat p)
=0-\frac34+\frac7{16}-\frac{13}{16}
=\boxed{-\frac98}.
\]

The box fixes

\[
\pi=0,
\qquad
q_{3,-}=\frac12,
\]

where $q_{3,-}$ is the minus-branch response probability for zero-based view index $2$. Hence

\[
a_{2,-}=1-2q_{3,-}=0.
\]

Every one of the four parity events in $Q$ contains view $2$. The branch parity product for each term therefore vanishes identically, so each corresponding even-parity probability equals $1/2$ throughout the box. The signed coefficients are $+1,-1,+1,-1$, so

\[
Q(p)=\frac12-\frac12+\frac12-\frac12=0
\]

for every P75 law generated in $B$. Thus

\[
\boxed{I_B(Q)=[0,0]}.
\]

The exact functional mismatch is therefore

\[
\Delta_Q=\left|-\frac98\right|=\frac98.
\]

Across the sixteen observed cells, the coefficient $g_Q(x)$ is

\[
-2\text{ on 2 cells},
\qquad
0\text{ on 12 cells},
\qquad
+2\text{ on 2 cells}.
\]

The exact median center is $c=0$ and

\[
D(Q)=2\cdot2+12\cdot0+2\cdot2=\boxed8.
\]

Therefore

\[
L_{\mathrm{quad}}(B)
\ge
\frac{9/8}{8}
=
\boxed{\frac9{64}}.
\]

The implementation exhausts the full 2640-function standard P86 family and attains this value. Since the complete P85 lower bound on the same box is $5/48$,

\[
\boxed{
L_{85}(B)=\frac5{48}
<
L_{86}(B)=\frac9{64}.
}
\]

The exact improvement is

\[
\boxed{
L_{86}(B)-L_{85}(B)=\frac7{192}.
}
\]

This is the strict hierarchy witness used by the P86 regression tests.

---

## 8. Global branch-and-bound use

The implementation inserts $L_{86}(B)$ into the same certified parameter-box branch-and-bound architecture used from P78 onward.

At every finite iteration:

- active boxes cover every not-yet-pruned candidate region;
- each active box has a rigorous P86 lower bound;
- every evaluated box center is an admissible P75 parameter vector and supplies a valid upper bound;
- the smallest active lower bound and best evaluated upper bound form a certified global distance bracket.

P86 does not require a new convergence principle. Its lower bound contains P85, which already contains the earlier certificate hierarchy. The new contribution is a tighter exact lower-bound family on each box.

---

## 9. Why P86 is scientifically useful

P86 isolates a higher-order shared-parameter constraint that is invisible to the numerical value of the complete P85 lower bound on the strict witness box.

This does not mean the P85 certificate is zero or that every lower-order relation is exactly compatible. The strict witness instead demonstrates the stronger and more relevant hierarchy statement:

\[
\text{the complete P86 certificate can be strictly sharper than complete P85.}
\]

That distinction matters scientifically. A hierarchy should be promoted only when the new level supplies additional certified information after all inherited lower levels are included. The exact witness above verifies precisely that condition.

---

## 10. What P86 does not prove

P86 does **not** prove that:

- consciousness is nonphysical;
- the P75 latent variable is a conscious state;
- a different latent model is correct;
- parity observables are privileged experiential observables;
- four-event failure implies a new physical dimension;
- quantum mechanics is incomplete;
- the physical-to-experiential bridge has been solved.

It proves a narrower statement: under the declared P75 model and the stated exact rational box assumptions, four-event parity functionals can yield a strictly stronger certified full-law separation bound than the complete P85 hierarchy.

---

## 11. Executable record

Implementation:

`src/consciousness_bridge/quadruple_projection_parity_functional_separation.py`

Regression tests:

`tests/test_quadruple_projection_parity_functional_separation.py`

Deterministic strict-witness search:

`scripts/search_p86_strict_witness.py`

The executable tests verify:

- all 2640 standard sign-normalized four-event functionals are present;
- exact box intervals agree with exhaustive parameter-vertex evaluation on an independent audit functional;
- the centered coefficient transfer is computed exactly;
- P86 dominates P85 by construction;
- the strict rational witness has $L_{85}=5/48$ and $L_{86}=9/64$;
- the exact hierarchy gain is $7/192$;
- the scientific interpretation boundary remains present in the executable source.
