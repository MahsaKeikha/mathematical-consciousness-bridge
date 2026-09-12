# P84 Equation and Provenance Record

## Scope

This record classifies the equations used in [Proposition 84](proposition_84_exact_joint_projection_parity_contrast.md), **Exact Joint Projection-Parity Contrast Certificate for Continuous P75 Separation**.

P84 is a downstream computational-certification theorem for the same four-view binary latent family introduced in P75 and the same full-law $L_\infty$ rejection architecture developed through P77-P83.

The new mathematical step is exact common-endpoint extremization of pairwise projection-parity contrasts under one shared P75 parameter assignment. P84 then transfers contrast separation to a full-law $L_\infty$ lower bound and combines that lower bound with the complete P83 certificate.

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

## 2. Imported P83 parity identity

For a nontrivial view set $J$ and parity bit $b$, define

\[
H(J,b)
=
\left\{x:\bigoplus_{j\in J}x_j=b\right\}.
\]

Inside latent branch $s$, conditional independence gives

\[
\boxed{
P_s(H(J,b))
=
\frac{1+(-1)^b\prod_{j\in J}(1-2q_{j,s})}{2}.
}
\]

**Classification:** imported P83 consequence of the standard Bernoulli parity-character identity.

**Dependency:** [P83](proposition_83_exact_projection_parity.md).

---

## 3. Joint projection-parity contrast

For two parity events

\[
H_1=H(J_1,b_1),
\qquad
H_2=H(J_2,b_2),
\]

with $J_1\ne J_2$, P84 defines

\[
\boxed{C_{12}=P(H_1)-P(H_2).}
\]

With

\[
a_{j,s}=1-2q_{j,s},
\]

the branchwise contrast is

\[
\boxed{
C_{12,s}
=
\frac12
\left[
(-1)^{b_1}\prod_{j\in J_1}a_{j,s}
-
(-1)^{b_2}\prod_{j\in J_2}a_{j,s}
\right].
}
\]

**Classification:** new P84 observable obtained algebraically from the imported P83 parity identity.

The constant terms in the two parity probabilities cancel exactly.

---

## 4. Shared-coordinate union

Let

\[
U=J_1\cup J_2.
\]

Both parity products are functions of the same coordinates $a_{j,s}$ for $j\in U$. P84 does not optimize the two parity probabilities separately and then subtract independent scalar intervals.

**Classification:** bookkeeping step required to preserve common-parameter compatibility.

This shared-coordinate dependence is the mathematical reason P84 can be strictly stronger than P83.

---

## 5. Exact branchwise interval by common endpoint enumeration

Define

\[
F_s(a_U)
=
\frac12
\left[
(-1)^{b_1}\prod_{j\in J_1}a_{j,s}
-
(-1)^{b_2}\prod_{j\in J_2}a_{j,s}
\right].
\]

Each union coordinate occurs with degree at most one. Therefore $F_s$ is multi-affine on the rectangular transformed-response box.

The exact interval is

\[
\boxed{
[c_s^L,c_s^U]
=
\left[
\min_{v\in V_U}F_s(v),
\max_{v\in V_U}F_s(v)
\right].
}
\]

Because there are only four observed views,

\[
|V_U|\le2^4=16.
\]

**Classification:** standard multi-affine vertex-extremum principle applied in a new P84 shared-observable construction.

**Implementation status:** exact `fractions.Fraction` endpoint enumeration, with no floating optimizer.

---

## 6. Why independent P83 interval subtraction is not exact in general

Suppose P83 gives exact scalar intervals

\[
P(H_1)\in[a,b],
\qquad
P(H_2)\in[c,d].
\]

The interval difference

\[
[a-d,b-c]
\]

is a sound enclosure of the contrast, but it treats the two extrema as independently attainable. Shared response coordinates can prevent the endpoint combinations needed for that full interval from occurring together.

P84 instead evaluates

\[
P(H_1)-P(H_2)
\]

directly at common response-coordinate endpoint assignments.

**Classification:** standard interval-analysis distinction between a dependency-discarding enclosure and exact common-variable extremization.

---

## 7. Exact latent-mixture interval

Write the exact branch intervals as

\[
C_{12,-}\in[c_-^L,c_-^U],
\qquad
C_{12,+}\in[c_+^L,c_+^U].
\]

The P75 mixture contrast is

\[
C_{12}(\theta)
=(1-\pi)C_{12,-}+\pi C_{12,+}.
\]

The branch coordinate sets are disjoint, so their lower extrema are jointly attainable and their upper extrema are jointly attainable. Define

\[
L(\pi)=(1-\pi)c_-^L+\pi c_+^L,
\]

\[
U(\pi)=(1-\pi)c_-^U+\pi c_+^U.
\]

Both are affine in $\pi$. Thus

\[
\boxed{
\ell_{12}
=
\min_{\pi\in\{\pi_L,\pi_U\}}L(\pi),
\qquad
u_{12}
=
\max_{\pi\in\{\pi_L,\pi_U\}}U(\pi).
}
\]

**Classification:** new P84 exact mixture-extremum consequence using the disjoint-branch logic already established in the P83 chain.

---

## 8. Signed contrast coefficient norm

Define

\[
c_x
=
\mathbf 1_{H_1}(x)-\mathbf 1_{H_2}(x).
\]

For different nonzero parity forms on four binary coordinates, the two forms are linearly independent over $\mathbb F_2$. Each parity event contains eight of the sixteen cells, and the intersection contains four cells. Their symmetric difference therefore contains

\[
8+8-2(4)=8
\]

cells. Hence

\[
\boxed{
\sum_x|c_x|=8.
}
\]

**Classification:** elementary finite-vector-space counting specialized to the P84 signed observable.

The implementation independently enumerates all sixteen outcome patterns and verifies the coefficient support size for each requested contrast.

---

## 9. Signed-observable $L_\infty$ transfer

For any laws $p$ and $q$,

\[
\begin{aligned}
|C_{12}(p)-C_{12}(q)|
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
\widehat C_{12},
[\ell_{12},u_{12}]
\right)
}{8}.
}
\]

**Classification:** standard triangle inequality applied to the new P84 signed observable.

---

## 10. Standard family size

P83 has 22 parity events: both parity values for the 11 nontrivial view sets of sizes two, three, and four.

The number of unordered pairs of all 22 events is

\[
{22\choose2}=231.
\]

Exactly 11 of those pairs use the same view set with opposite parity labels. Those pairs are algebraic complements and add no genuinely new common-parameter relation beyond P83. Removing them leaves

\[
\boxed{231-11=220.}
\]

**Classification:** new P84 finite-family definition plus direct combinatorial count.

---

## 11. Combined P84 certificate

Define

\[
L_{\mathrm{joint-parity}}(B)
=
\max_{(H_1,H_2)\in\mathcal C_{84}}
\frac{
d\!\left(
\widehat C_{12},
[\ell_{12}(B),u_{12}(B)]
\right)
}{8}.
\]

P84 then defines

\[
\boxed{
L_{84}(B)
=
\max\{L_{83}(B),L_{\mathrm{joint-parity}}(B)\}.
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

The P84 regression suite records a rational parameter box and rational empirical law for which

\[
L_{83}(B)=0.
\]

For the named pair

\[
H_1=H(\{2,4\},0),
\qquad
H_2=H(\{2,3,4\},1),
\]

exact common-endpoint enumeration gives

\[
C_{12}(B)\in\left[0,\frac12\right],
\]

while the empirical contrast is

\[
\widehat C_{12}=-\frac14.
\]

The contrast therefore lies $1/4$ outside the exact feasible interval. The signed coefficient support has size eight, so

\[
\boxed{
L_{84}(B)=\frac1{32}>0=L_{83}(B).
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
