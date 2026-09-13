# P86 Equation and Provenance Record

## Scope

This record classifies the equations used in [Proposition 86](proposition_86_exact_quadruple_projection_parity_functional.md), **Exact Four-Event Projection-Parity Functional Certificate**.

P86 is a downstream computational-certification theorem for the same four-view binary latent family introduced in P75 and the same full-law $L_\infty$ separation architecture developed through P77-P85.

The new mathematical step is to retain one shared P75 parameter assignment across four canonical even-parity observables at once. P85 already tests all standard sign-normalized three-event functionals. P86 tests signed four-event functionals whose branchwise form remains multi-affine, so exact rational box intervals are available by common endpoint evaluation. A functional mismatch is transferred to a full-law $L_\infty$ lower bound with the exact centered coefficient norm.

P86 introduces no consciousness variable and no new physical postulate. The physical-to-experiential bridge remains open.

---

## 1. Imported P75 observed-law model

For observed binary pattern $x=(x_1,x_2,x_3,x_4)$,

\[
q_x(\theta)
=
(1-\pi)\prod_{j=1}^4 f(q_{j,-},x_j)
+
\pi\prod_{j=1}^4 f(q_{j,+},x_j),
\]

where

\[
f(q,1)=q,
\qquad
f(q,0)=1-q.
\]

**Classification:** imported project definition from P75.

**Dependencies:** P75 model adequacy, P78 continuous box certification, and the exact parity hierarchy P83-P85.

---

## 2. Canonical even-parity events

For $J\subseteq\{1,2,3,4\}$ with $|J|\ge2$,

\[
H_J
=
\left\{x:\bigoplus_{j\in J}x_j=0\right\}.
\]

There are

\[
\binom42+\binom43+\binom44=11
\]

canonical even-parity events.

Inside latent branch $s$,

\[
\boxed{
P_s(H_J)
=
\frac{1+\prod_{j\in J}(1-2q_{j,s})}{2}.
}
\]

**Classification:** standard Bernoulli parity/Fourier-character identity inherited from P83-P85.

---

## 3. P86 signed four-event functional

For four distinct canonical view sets $J_1,J_2,J_3,J_4$ and signs $\sigma_i\in\{-1,+1\}$, with the first sign normalized to $+1$, define

\[
\boxed{
Q
=
\sum_{i=1}^4\sigma_i P(H_{J_i}).
}
\]

Inside one latent branch,

\[
\boxed{
Q_s
=
\frac12\sum_{i=1}^4
\sigma_i
\left[1+\prod_{j\in J_i}(1-2q_{j,s})\right].
}
\]

The sign normalization removes the redundant global sign flip because replacing $Q$ with $-Q$ leaves the absolute distance-to-interval certificate unchanged.

**Classification:** new P86 joint observable formed from four imported parity events.

The functional is a model-checking device. It is not defined as a measure of consciousness or experience.

---

## 4. Standard family size

P86 chooses an unordered four-element subset from the eleven canonical even-parity events and eight normalized sign patterns:

\[
\boxed{
\binom{11}{4}2^3
=330\cdot8
=2640.
}
\]

**Classification:** project-defined finite P86 audit family with an executable exact count.

---

## 5. Exact common-vertex extremization

Let

\[
U=J_1\cup J_2\cup J_3\cup J_4.
\]

The branch functional $Q_s$ is multi-affine in the response coordinates indexed by $U$. Therefore

\[
\boxed{
[q_s^L,q_s^U]
=
\left[
\min_{v\in V_U}Q_s(v),
\max_{v\in V_U}Q_s(v)
\right],
}
\]

where $V_U$ contains the common endpoint assignments of the relevant response-coordinate box.

Since only four observed views exist,

\[
|V_U|\le2^4=16.
\]

**Classification:** standard multi-affine box-extremum principle specialized to the P86 four-event shared-parameter construction.

**Important distinction:** all four parity probabilities are evaluated at one common response-coordinate vertex. Four separately optimized scalar intervals would discard the shared-parameter dependence that P86 is designed to retain.

---

## 6. Exact latent-mixture interval

The full functional is

\[
Q(\pi)=(1-\pi)Q_-+\pi Q_+.
\]

Minus-branch and plus-branch response coordinates are disjoint, and prevalence is a separate coordinate. Once exact branch intervals are known, the lower and upper mixture envelopes are affine in prevalence. Their extrema occur at prevalence endpoints.

**Classification:** exact consequence of branchwise multi-affine extremization plus affine endpoint extremization in prevalence.

**Numerical status:** exact rational arithmetic for rational box endpoints.

---

## 7. Centered coefficient transfer

For one four-event functional define

\[
g_Q(x)=\sum_{i=1}^4\sigma_i\mathbf1_{H_{J_i}}(x).
\]

Then

\[
Q(p)-Q(q)
=
\sum_x g_Q(x)[p(x)-q(x)].
\]

Because $p$ and $q$ both have total mass one,

\[
\sum_x[p(x)-q(x)]=0.
\]

For every constant $c$,

\[
Q(p)-Q(q)
=
\sum_x[g_Q(x)-c][p(x)-q(x)].
\]

Hence

\[
|Q(p)-Q(q)|
\le
\left(\sum_x|g_Q(x)-c|\right)\|p-q\|_\infty.
\]

P86 uses

\[
\boxed{
D(Q)=\min_c\sum_x|g_Q(x)-c|.
}
\]

For a finite coefficient vector, every median is an $L_1$-minimizing center. The implementation checks the finite set of distinct exact coefficient values and returns a deterministic exact minimum.

**Classification:** standard finite-dimensional norm transfer plus standard median minimization of absolute deviations, specialized to P86.

---

## 8. P86 full-law lower bound

Let $Q(\widehat p)$ be the empirical value and let

\[
I_B(Q)=[Q_B^L,Q_B^U]
\]

be the exact P75 box interval. Define

\[
\Delta_Q
=
\operatorname{dist}\left(Q(\widehat p),I_B(Q)\right).
\]

Then every P75 law $q$ generated in $B$ satisfies

\[
\boxed{
\|\widehat p-q\|_\infty
\ge
\frac{\Delta_Q}{D(Q)}.
}
\]

Let $L_{\mathrm{quad}}(B)$ be the maximum over the 2640 standard four-event functionals. P86 defines

\[
\boxed{
L_{86}(B)=\max\{L_{85}(B),L_{\mathrm{quad}}(B)\}.
}
\]

Therefore

\[
L_{86}(B)\ge L_{85}(B)
\]

for every audited P75 box.

**Classification:** new P86 combination theorem.

---

## 9. Exact strict-improvement witness

The authoritative exact-rational witness uses P75 parameter order

\[
(\pi,q_{1,-},q_{1,+},q_{2,-},q_{2,+},q_{3,-},q_{3,+},q_{4,-},q_{4,+}).
\]

Its lower endpoint is

\[
\left(0,\frac12,0,0,0,\frac12,\frac12,0,0\right),
\]

and its upper endpoint is

\[
\left(0,1,\frac12,\frac12,1,\frac12,\frac12,1,0\right).
\]

Using zero-based implementation outcome labels, the empirical law has nonzero masses

\[
\widehat p(0011)=\frac3{16},
\qquad
\widehat p(1000)=\frac38,
\]

\[
\widehat p(1100)=\frac3{16},
\qquad
\widehat p(1101)=\frac14.
\]

The complete implemented P85 certificate on this box is

\[
\boxed{L_{85}=\frac5{48}}.
\]

The P86 strict functional is

\[
\boxed{
Q
=P(H_{\{0,2\}})
-P(H_{\{2,3\}})
+P(H_{\{0,1,2\}})
-P(H_{\{1,2,3\}}).
}
\]

The empirical parity probabilities are

\[
0,\quad\frac34,\quad\frac7{16},\quad\frac{13}{16},
\]

so

\[
\boxed{Q(\widehat p)=-\frac98}.
\]

The box fixes $\pi=0$ and fixes zero-based view $2$ at

\[
q_{3,-}=\frac12.
\]

Thus

\[
1-2q_{3,-}=0.
\]

Every selected parity set contains view $2$, so all four branch parity products vanish identically. Each parity event therefore has probability $1/2$ throughout the box and the signs $+,-,+,-$ cancel exactly:

\[
\boxed{I_B(Q)=[0,0]}.
\]

Hence

\[
\boxed{\Delta_Q=\frac98}.
\]

The sixteen outcome coefficients consist of twelve zeros, two $+2$ values, and two $-2$ values. Their exact median center is zero and

\[
\boxed{D(Q)=8}.
\]

Therefore

\[
\boxed{
L_{\mathrm{quad}}=\frac{9/8}{8}=\frac9{64}.
}
\]

The full standard P86 audit attains this value, giving

\[
\boxed{
L_{85}=\frac5{48}
<
L_{86}=\frac9{64}.
}
\]

The exact strict gain is

\[
\boxed{
L_{86}-L_{85}=\frac7{192}.
}
\]

**Classification:** project-specific exact regression witness establishing strict P86-over-P85 hierarchy separation.

---

## 10. Branch-and-bound inheritance

P86 inserts $L_{86}(B)$ into the existing exact rational P75 branch-and-bound architecture. The active-box cover, explicit center upper bounds, and finite-iteration bracketing logic are inherited from the previous certified search hierarchy.

**Classification:** inherited optimization architecture with a stronger box lower-bound oracle.

P86 does not claim a new convergence theorem.

---

## 11. Interpretation boundary

The following statements are **not** consequences of P86:

- the P75 latent variable is consciousness;
- consciousness is nonphysical;
- parity observables are uniquely meaningful for experience;
- a four-event mismatch identifies a new physical degree of freedom;
- another latent model is validated by rejecting P75;
- the physical-to-experiential bridge is solved.

The supported conclusion is narrower: within the declared P75 family, the exact four-event audit can certify a strictly larger full-law $L_\infty$ lower bound than the complete P85 hierarchy on the same parameter box.

---

## 12. Executable provenance

Implementation:

`src/consciousness_bridge/quadruple_projection_parity_functional_separation.py`

Tests:

`tests/test_quadruple_projection_parity_functional_separation.py`

Deterministic witness search:

`scripts/search_p86_strict_witness.py`

All theorem-critical numerical quantities in the regression witness are represented with `fractions.Fraction`; no floating-point optimizer is used to establish the P86 strictness claim.
