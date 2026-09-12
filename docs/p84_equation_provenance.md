# P84 Equation and Provenance Record

## Scope

This record classifies the equations used in [Proposition 84](proposition_84_exact_coupled_projection_parity.md), **Exact Coupled Projection-Parity Certificate for Continuous P75 Separation**.

P84 is a downstream computational-certification theorem for the same four-view binary latent family introduced in P75 and the same full-law $L_\infty$ rejection architecture developed through P77-P83.

The new mathematical step is an exact common-endpoint parameter-box extremization of pairwise parity contrasts. P84 then transfers contrast separation to a full-law $L_\infty$ lower bound and combines it with the complete P83 certificate.

P84 introduces no consciousness variable and no new physical postulate.

---

## 1. Imported P75 model

The observed sixteen-cell law is

\[
q_x(\theta)
=
(1-\pi)\prod_{j=1}^4 f(q_{j,-},x_j)
+
\pi\prod_{j=1}^4 f(q_{j,+},x_j),
\]

with

\[
f(q,1)=q,
\qquad
f(q,0)=1-q.
\]

**Classification:** imported project definition from P75.

**Dependencies:** [P75](proposition_75_target_model_adequacy_overidentification.md), [P78](proposition_78_certified_continuous_model_separation.md).

---

## 2. Imported P83 even-parity identity

For a nontrivial view set $J$, define

\[
E_J
=
\left\{x:\bigoplus_{j\in J}x_j=0\right\}.
\]

Inside latent branch $s$, conditional independence gives

\[
\boxed{
P_s(E_J)
=
\frac{1+\prod_{j\in J}(1-2q_{j,s})}{2}.
}
\]

**Classification:** imported P83 consequence of the standard Bernoulli parity-character identity.

**Dependency:** [P83](proposition_83_exact_projection_parity.md).

---

## 3. Coupled parity contrast

For distinct nontrivial view sets $J$ and $K$, P84 defines

\[
D_{J,K}=P(E_J)-P(E_K).
\]

With

\[
a_{j,s}=1-2q_{j,s},
\]

the branchwise contrast is

\[
\boxed{
D_{J,K,s}
=
\frac12
\left(
\prod_{j\in J}a_{j,s}
-
\prod_{j\in K}a_{j,s}
\right).
}
\]

**Classification:** new P84 observable obtained algebraically from the imported P83 parity identity.

The constant $1/2$ terms in the two even-parity probabilities cancel exactly.

---

## 4. Common-coordinate union

Let

\[
U=J\cup K.
\]

The two products in $D_{J,K,s}$ are functions of the same coordinates $a_{j,s}$ for $j\in U$. P84 does not replace them by two independently optimized scalar intervals.

**Classification:** bookkeeping step required to preserve shared-parameter compatibility.

This distinction is the mathematical reason P84 can be strictly stronger than P83.

---

## 5. Exact branchwise interval by common endpoint enumeration

Define

\[
F_{J,K,s}(a_U)
=
\frac12
\left(
\prod_{j\in J}a_{j,s}
-
\prod_{j\in K}a_{j,s}
\right).
\]

Each union coordinate occurs with degree at most one. Therefore $F_{J,K,s}$ is multi-affine on the rectangular transformed-response box.

The exact interval is

\[
\boxed{
[d_s^L,d_s^U]
=
\left[
\min_{v\in V_U}F_{J,K,s}(v),
\max_{v\in V_U}F_{J,K,s}(v)
\right].
}
\]

Because there are only four observed views,

\[
|V_U|\le2^4=16.
\]

**Classification:** standard multi-affine vertex-extremum principle applied in a new P84 coupled-observable construction.

**Implementation status:** exact `fractions.Fraction` endpoint enumeration; no floating optimizer.

---

## 6. Why independent P83 interval subtraction is not exact in general

Suppose P83 gives exact marginal intervals

\[
P(E_J)\in[a,b],
\qquad
P(E_K)\in[c,d].
\]

The interval subtraction

\[
[a-d,b-c]
\]

is always a sound enclosure of the contrast, but it treats the two extrema as independently attainable. Shared response coordinates can prevent those endpoint combinations from occurring together.

P84 instead evaluates

\[
P(E_J)-P(E_K)
\]

directly at one common response-coordinate endpoint assignment.

**Classification:** interval-analysis distinction between a dependency-discarding enclosure and exact common-variable extremization.

---

## 7. Exact latent-mixture interval

Write the exact branch intervals as

\[
D_{J,K,-}\in[d_-^L,d_-^U],
\qquad
D_{J,K,+}\in[d_+^L,d_+^U].
\]

The P75 mixture contrast is

\[
D_{J,K}(\theta)
=(1-\pi)D_{J,K,-}+\pi D_{J,K,+}.
\]

The branch coordinate sets are disjoint, so their lower extrema are jointly attainable and their upper extrema are jointly attainable. Therefore

\[
L(\pi)=(1-\pi)d_-^L+\pi d_+^L,
\]

\[
U(\pi)=(1-\pi)d_-^U+\pi d_+^U.
\]

Both are affine in $\pi$. Thus

\[
\boxed{
\ell_{J,K}
=
\min_{\pi\in\{\pi_L,\pi_U\}}L(\pi),
\qquad
u_{J,K}
=
\max_{\pi\in\{\pi_L,\pi_U\}}U(\pi).
}
\]

**Classification:** new P84 exact mixture-extremum consequence using the same disjoint-branch logic established in P83.

---

## 8. Signed contrast coefficient norm

Define

\[
c_x
=
\mathbf 1_{E_J}(x)-\mathbf 1_{E_K}(x).
\]

For distinct nonzero parity forms $J$ and $K$ on four binary coordinates, the two forms are linearly independent over $\mathbb F_2$. Exactly one quarter of the sixteen outcomes has each ordered pair of parity values. Therefore

\[
|E_J|=|E_K|=8,
\]

\[
|E_J\cap E_K|=4,
\]

and the symmetric difference has size

\[
8+8-2(4)=8.
\]

Hence

\[
\boxed{
\sum_x|c_x|=8.
}
\]

**Classification:** elementary finite-vector-space counting specialized to the P84 signed observable.

The implementation independently enumerates the sixteen outcome patterns and verifies the same support size for each requested contrast.

---

## 9. Signed-observable $L_\infty$ transfer

For any laws $p$ and $q$,

\[
\begin{aligned}
|D_{J,K}(p)-D_{J,K}(q)|
&=
\left|\sum_xc_x(p_x-q_x)\right|\\
&\le
\sum_x|c_x||p_x-q_x|\\
&\le
\left(\sum_x|c_x|\right)\|p-q\|_\infty\\
&=
8\|p-q\|_\infty.
\end{aligned}
\]

Therefore

\[
\boxed{
\|\widehat p-q(\theta)\|_\infty
\ge
\frac{
d\!\left(
\widehat D_{J,K},
[\ell_{J,K},u_{J,K}]
\right)
}{8}.
}
\]

**Classification:** standard triangle inequality applied to the new P84 signed observable.

---

## 10. Standard family size

There are

\[
{4\choose2}+{4\choose3}+{4\choose4}=11
\]

nontrivial parity view sets after identifying even/odd complements for the purpose of pairwise probability differences.

The standard P84 family contains every unordered pair:

\[
\boxed{
|\mathcal C_{84}|
={11\choose2}=55.
}
\]

**Classification:** new P84 finite-family definition plus direct combinatorial count.

---

## 11. Combined P84 certificate

Define

\[
L_{\mathrm{cpar}}(B)
=
\max_{\{J,K\}\in\mathcal C_{84}}
\frac{
d\!\left(
\widehat D_{J,K},
[\ell_{J,K}(B),u_{J,K}(B)]
\right)
}{8}.
\]

P84 then defines

\[
\boxed{
L_{84}(B)
=
\max\{L_{83}(B),L_{\mathrm{cpar}}(B)\}.
}
\]

Consequently,

\[
L_{84}(B)
\ge L_{83}(B)
\ge L_{82}(B)
\ge L_{81}(B)
\ge L_{80}(B)
\ge L_{78}(B).
\]

**Classification:** new P84 certificate and immediate dominance consequence.

---

## 12. Exact strict-improvement witness

The P84 proposition records a rational parameter box and rational empirical law for which the exhaustive implementation gives

\[
L_{81}(B)=L_{82}(B)=L_{83}(B)=0.
\]

For

\[
J=\{1,4\},
\qquad
K=\{1,3,4\},
\]

the empirical contrast is

\[
\widehat D_{J,K}=\frac14,
\]

while exact common-endpoint enumeration gives

\[
D_{J,K}(B)
\in
\left[-\frac18,\frac18\right].
\]

Thus

\[
\boxed{
L_{84}(B)=\frac1{64}>0=L_{83}(B).
}
\]

**Classification:** new exact-rational constructive witness, mechanically checked by the P84 test suite.

This witness establishes strict improvement of the declared P84 certificate over P83. It is not an empirical claim about consciousness.

---

## 13. Global and finite-data handoff

For a finite partition $\mathcal B$ of the complete P75 parameter cube,

\[
L_{84}(\mathcal B)
=
\min_{B\in\mathcal B}L_{84}(B)
\]

is a valid global model-distance lower bound.

Explicit P75 parameter vectors remain upper-bound witnesses. P84 retains the P78 mesh-width upper certificate without modification and claims no new convergence-rate theorem.

With the P79 sampling-radius upper certificate $\overline\varepsilon_{79}$,

\[
L_{84}(\mathcal B)>\overline\varepsilon_{79}
\]

is the same strict one-sided P77 rejection gate.

**Classification:** imported P77-P79 certification architecture with a stronger P84 lower-bound component.

---

## 14. Scientific boundary

P84 proves a conditional mathematical statement about separation from a declared latent-variable model family. It does not validate P75, identify a latent state with consciousness, define a consciousness observable, or establish that experience lies outside physics.

A positive P84 certificate rejects the declared P75 family under the stated empirical and sampling assumptions. A zero or small certificate is inconclusive and does not validate the model.

The physical-to-experiential bridge remains open.
