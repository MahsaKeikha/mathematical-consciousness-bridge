# P85 Equation and Provenance Record

## Scope

This record classifies the equations used in [Proposition 85](proposition_85_exact_triple_projection_parity_functional.md), **Exact Three-Event Projection-Parity Functional Certificate**.

P85 is a downstream computational-certification theorem for the same four-view binary latent family introduced in P75 and the same full-law $L_\infty$ rejection architecture developed through P77-P84.

The new mathematical step is to retain one shared P75 parameter assignment across three canonical even-parity observables at once. P84 already tests exact shared-parameter compatibility for pairs. P85 tests signed three-event functionals whose branchwise form is multi-affine, so exact rational box intervals remain available by common endpoint evaluation. A functional mismatch is then transferred to a full-law $L_\infty$ lower bound using the exact centered coefficient norm.

P85 introduces no consciousness variable and no new physical postulate. The physical-to-experiential bridge remains open.

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

**Dependencies:** [P75](proposition_75_target_model_adequacy_overidentification.md), [P78](proposition_78_certified_continuous_model_separation.md), and the P83-P84 parity hierarchy.

---

## 2. Canonical even-parity observables

For a selected view set $J\subseteq\{1,2,3,4\}$ with $|J|\ge2$, define

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

Inside one P75 latent branch,

\[
P_s(H_J)
=
\frac{1+\prod_{j\in J}(1-2q_{j,s})}{2}.
\]

**Classification:** standard finite Bernoulli parity/Fourier-character identity, inherited from P83 and specialized to the canonical even-parity family used by P84-P85.

---

## 3. P85 signed three-event functional

For three distinct canonical view sets $J_1,J_2,J_3$ and signs $\sigma_i\in\{-1,+1\}$, with the first sign normalized to $+1$, P85 defines

\[
\boxed{
T
=
\sigma_1 P(H_{J_1})
+
\sigma_2 P(H_{J_2})
+
\sigma_3 P(H_{J_3}).
}
\]

Inside one latent branch,

\[
\boxed{
T_s
=
\frac12\sum_{i=1}^3
\sigma_i
\left[1+\prod_{j\in J_i}(1-2q_{j,s})\right].
}
\]

The sign normalization removes the redundant global sign flip without changing the absolute separation certificate.

**Classification:** new P85 joint observable formed from three imported parity events.

The functional is a model-checking device. It is not defined as a measure of consciousness or experience.

---

## 4. Standard family size

P85 chooses an unordered triple from the eleven canonical even-parity events and four normalized sign patterns:

\[
\boxed{
\binom{11}{3}\,2^2=165\cdot4=660.
}
\]

**Classification:** project-defined finite P85 audit family with an executable exact count.

---

## 5. Exact common-vertex extremization

Let

\[
U=J_1\cup J_2\cup J_3.
\]

The branch functional is multi-affine in the response coordinates indexed by $U$. Therefore

\[
\boxed{
[t_s^L,t_s^U]
=
\left[
\min_{v\in V_U}T_s(v),
\max_{v\in V_U}T_s(v)
\right],
}
\]

where $V_U$ contains the endpoint assignments of the common response-coordinate box. Since there are four observed views,

\[
|V_U|\le2^4=16.
\]

**Classification:** standard multi-affine box-extremum principle used in the P85 three-event shared-parameter construction.

**Important distinction:** all three parity probabilities are evaluated at one common response-coordinate vertex. Combining three separately optimized scalar intervals would discard the shared-parameter constraint that P85 is designed to test.

---

## 6. Exact latent-mixture interval

The full functional is

\[
T(\pi)=(1-\pi)T_-+\pi T_+.
\]

Minus-branch and plus-branch response coordinates are disjoint, and prevalence is a separate coordinate. Once the exact branch intervals are known, the lower and upper mixture envelopes are affine in prevalence, so their extrema occur at prevalence endpoints.

**Classification:** exact mixture-extremum consequence built from branchwise exact intervals and standard affine endpoint extremization.

**Numerical status:** exact rational arithmetic for rational parameter-box endpoints.

---

## 7. Centered coefficient transfer

For one triple functional define the outcome coefficient

\[
g(x)=\sum_{i=1}^3\sigma_i1_{H_{J_i}}(x).
\]

Then for probability laws $p$ and $q$,

\[
T(p)-T(q)=\sum_x g(x)(p_x-q_x).
\]

Because both laws have total mass one,

\[
\sum_x(p_x-q_x)=0,
\]

so subtracting any constant $c$ from every coefficient leaves the functional difference unchanged:

\[
T(p)-T(q)=\sum_x(g(x)-c)(p_x-q_x).
\]

Hence

\[
|T(p)-T(q)|
\le
\left(\sum_x|g(x)-c|\right)\|p-q\|_\infty.
\]

P85 uses the exact best centered coefficient norm

\[
\boxed{
D(T)=\min_c\sum_x|g(x)-c|.
}
\]

For the sixteen finite coefficient values, any median is an $L_1$-minimizing center. The implementation evaluates the finite exact candidate set and returns an exact rational norm and one optimal center.

**Classification:** standard finite-dimensional norm transfer plus standard median minimization of absolute deviations, specialized to the P85 coefficient vector.

---

## 8. P85 full-law lower bound

Let $\widehat T$ be the empirical functional and let $[T_B^L,T_B^U]$ be its exact P75 box interval. Define

\[
\Delta_T
=
\operatorname{dist}\left(\widehat T,[T_B^L,T_B^U]\right).
\]

Then every P75 model law $q$ generated inside box $B$ satisfies

\[
\boxed{
\|\widehat p-q\|_\infty
\ge
\frac{\Delta_T}{D(T)}.
}
\]

Let $L_{\mathrm{triple}}(B)$ be the maximum of this quantity over the 660 standard functionals. P85 defines

\[
\boxed{
L_{85}(B)=\max\{L_{84}(B),L_{\mathrm{triple}}(B)\}.
}
\]

Therefore

\[
L_{85}(B)\ge L_{84}(B)
\]

for every audited P75 box.

**Classification:** new P85 combination theorem.

---

## 9. Exact strict-improvement witness

The authoritative exact-rational regression witness uses P75 parameter order

\[
(\pi,q_{1,-},q_{1,+},q_{2,-},q_{2,+},q_{3,-},q_{3,+},q_{4,-},q_{4,+}).
\]

Its box lower endpoint is

\[
\left(0,0,0,\frac12,\frac12,0,0,0,1\right),
\]

and its box upper endpoint is

\[
\left(\frac12,1,1,1,1,1,1,\frac12,1\right).
\]

Using zero-based implementation view indices, the empirical law has nonzero masses

\[
\widehat p(0,0,1,0)=\frac14,
\quad
\widehat p(0,1,0,0)=\frac18,
\quad
\widehat p(1,0,0,0)=\frac18,
\]

\[
\widehat p(1,1,0,1)=\frac18,
\qquad
\widehat p(1,1,1,0)=\frac38.
\]

All other cells have mass zero.

The strict witness functional is

\[
T=P(H_{\{0,2\}})+P(H_{\{0,1,2\}})+P(H_{\{0,1,2,3\}}).
\]

The empirical value is

\[
\widehat T=\frac58,
\]

while exact common-parameter extremization over the declared P75 box gives

\[
T(B)\in[1,2].
\]

Thus

\[
\Delta_T=1-\frac58=\frac38.
\]

The exact centered coefficient norm is

\[
D(T)=12,
\]

with center $c=1$ as one deterministic optimum. Therefore

\[
\boxed{
L_{\mathrm{triple}}(B)
=
\frac{3/8}{12}
=
\frac1{32}.
}
\]

On the same box and empirical law the complete P84 certificate gives

\[
L_{84}(B)=0.
\]

Consequently

\[
\boxed{L_{85}(B)=\frac1{32}>0=L_{84}(B).}
\]

**Classification:** project-derived exact-rational constructive witness verified by the authoritative P85 regression suite.

**Interpretive limit:** $L_{84}(B)=0$ means that the P84 certificate is silent on this example. It does not assert that every possible pairwise property or every alternative model is valid.

---

## 10. Global partition certificate

For an active partition $\mathcal B$ of the complete P75 parameter cube,

\[
L_{85}(\mathcal B)
=
\min_{B\in\mathcal B}L_{85}(B)
\le
d_\infty(\widehat p,\mathcal M_{4,2}).
\]

**Classification:** branch-and-bound lower-envelope logic inherited from P78-P84 with the stronger P85 box lower bound.

P85 retains the established mesh-width upper certificate; no new convergence-rate theorem is assumed.

---

## 11. P79 rejection gate

With P79 certified sampling-radius upper envelope $\overline\varepsilon_{79}$,

\[
L_{85}(\mathcal B)>\overline\varepsilon_{79}
\]

is sufficient for the P77 full-law rejection conclusion under the declared assumptions.

**Classification:** imported P77/P79 rejection logic with the stronger P85 model-distance lower bound.

Failure of the strict inequality is inconclusive and is not model validation.

---

## 12. Executable provenance

Implementation:

- [`triple_projection_parity_functional_separation.py`](../src/consciousness_bridge/triple_projection_parity_functional_separation.py)

Regression tests:

- [`test_triple_projection_parity_functional_separation.py`](../tests/test_triple_projection_parity_functional_separation.py)

Canonical proof:

- [Proposition 85](proposition_85_exact_triple_projection_parity_functional.md)

Canonical visual:

- [P85 exact triple projection-parity functional certificate](figures/p85_exact_triple_projection_parity_functional.svg)

The visual is source-authored vector content. The repository-wide figure pipeline validates every SVG and preserves substantive authored metadata during enrichment.

---

## 13. Scientific boundary

Every P85 equation is conditional on the declared P75 target-view model, the declared parameter box, and the declared $L_\infty$ observed-law metric.

P85 can strengthen evidence that an observed law is incompatible with that declared model because one-event and two-event certificates can be silent while a three-event shared-parameter functional is incompatible. It cannot assign experiential meaning to the latent variable, cannot turn non-rejection into model truth, cannot validate an alternative model, cannot establish a new physical dimension, cannot show that consciousness is nonphysical, and does not close the physical-to-experiential bridge.
