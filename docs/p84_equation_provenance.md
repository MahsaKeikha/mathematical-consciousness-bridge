# P84 Equation and Provenance Record

## Scope

This record classifies the equations used in [Proposition 84](proposition_84_exact_projection_parity_contrast.md), **Exact Joint Projection-Parity Contrast Certificate**.

P84 is a downstream computational-certification theorem for the same four-view binary latent family introduced in P75 and the same full-law $L_\infty$ rejection architecture developed through P77-P83.

The new mathematical step is to retain the shared response-parameter coupling between two P83 parity events instead of checking their exact scalar ranges separately. The resulting event-probability contrast is multi-affine, so its exact rational box interval is available by common endpoint evaluation. The contrast mismatch is then transferred to a full-law $L_\infty$ lower bound.

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

## 2. Imported P83 parity event

For a selected view set $J\subseteq\{1,2,3,4\}$ and $b\in\{0,1\}$,

\[
H(J,b)
=
\left\{x:\bigoplus_{j\in J}x_j=b\right\}.
\]

P83 uses both parity values on every two-, three-, and four-view subset, giving 22 standard parity events.

**Classification:** imported P83 observable family based on the standard finite binary parity definition.

---

## 3. Imported branchwise parity identity

Inside one P75 latent branch,

\[
P_s(H(J,b))
=
\frac{1+(-1)^b\prod_{j\in J}(1-2q_{j,s})}{2}.
\]

**Classification:** standard Bernoulli parity/Fourier-character identity, imported from P83.

---

## 4. P84 coupled contrast

For two P83 parity events with different view sets,

\[
H_1=H(J_1,b_1),
\qquad
H_2=H(J_2,b_2),
\]

P84 defines

\[
\boxed{
C=P(H_1)-P(H_2).
}
\]

Inside one latent branch,

\[
\boxed{
C_s
=
\frac12
\left[
(-1)^{b_1}\prod_{j\in J_1}(1-2q_{j,s})
-
(-1)^{b_2}\prod_{j\in J_2}(1-2q_{j,s})
\right].
}
\]

**Classification:** new P84 joint observable formed from two imported P83 parity events.

The scientific purpose is to test shared-parameter compatibility. P84 does not interpret this contrast as consciousness.

---

## 5. Exact common-vertex extremization

Let

\[
U=J_1\cup J_2.
\]

The branch contrast is multi-affine in the response coordinates indexed by $U$. Therefore

\[
\boxed{
[c_s^L,c_s^U]
=
\left[
\min_{v\in V_U} C_s(v),
\max_{v\in V_U} C_s(v)
\right],
}
\]

where $V_U$ contains the endpoint assignments of the common response-coordinate box.

Since there are four observed views,

\[
|V_U|\le2^4=16.
\]

**Classification:** standard multi-affine box-extremum principle used in a new P84 shared-parameter construction.

**Important distinction:** the two parity-event probabilities are optimized at the same response-coordinate vertex. Subtracting two independently optimized P83 intervals would generally lose this coupling and would not produce the P84 exact interval.

---

## 6. Exact latent-mixture interval

The full contrast is

\[
C(\pi)
=(1-\pi)C_-+\pi C_+.
\]

Minus-branch and plus-branch response coordinates are disjoint, and prevalence is a separate coordinate. Once the exact branch intervals are known, the lower and upper mixture envelopes are affine in prevalence. Their extrema therefore occur at the two prevalence endpoints.

**Classification:** new P84 exact mixture-extremum consequence built from branchwise exact intervals and standard affine endpoint extremization.

**Numerical status:** exact rational arithmetic for rational parameter-box endpoints.

---

## 7. Signed event-difference functional

Define

\[
c_x=1_{H_1}(x)-1_{H_2}(x).
\]

Then

\[
C(p)-C(q)
=
\sum_x c_x\bigl(p_x-q_x\bigr).
\]

By the triangle inequality,

\[
|C(p)-C(q)|
\le
\left(\sum_x|c_x|\right)\|p-q\|_\infty.
\]

**Classification:** standard finite-dimensional norm inequality specialized to the P84 contrast.

---

## 8. Eight-cell coefficient support

For every retained standard P84 contrast, the event-difference coefficients are nonzero on eight of the sixteen full outcomes, each with magnitude one. Hence

\[
\boxed{
\sum_x|c_x|=8.
}
\]

Therefore an empirical contrast gap $g$ outside the exact model interval yields

\[
\boxed{
\|\widehat p-q\|_\infty\ge\frac{g}{8}.
}
\]

**Classification:** P84 finite combinatorial property plus the imported $L_\infty$ transfer inequality.

The named strict witness and the standard-family implementation verify the support calculation exactly.

---

## 9. Standard family size

P83 has 22 standard parity events. P84 considers unordered event pairs and retains the genuinely coupled pairs with different view sets after excluding algebraic redundancies and contrasts already represented by the nested residual structure.

The executable family contains

\[
\boxed{220}
\]

standard contrasts.

**Classification:** project-defined finite P84 audit family with an executable exact count.

---

## 10. Combined P84 certificate

Let $L_{\mathrm{joint-parity}}(B)$ be the strongest retained exact contrast lower bound on P75 parameter box $B$. P84 defines

\[
\boxed{
L_{84}(B)
=
\max\{L_{83}(B),L_{\mathrm{joint-parity}}(B)\}.
}
\]

Hence

\[
L_{84}(B)
\ge L_{83}(B)
\ge L_{82}(B)
\ge L_{81}(B)
\ge L_{80}(B)
\ge L_{78}(B).
\]

**Classification:** new P84 combination theorem.

---

## 11. Strict improvement witness

The exact rational regression witness satisfies

\[
L_{83}(B)=0.
\]

For the named standard pair

\[
H_1=H(\{1,3\},0),
\qquad
H_2=H(\{1,2,3\},1),
\]

using zero-based implementation indices, the exact P75 box interval is

\[
C(B)\in[0,1/2],
\]

while the empirical contrast is

\[
\widehat C=-1/4.
\]

The gap is therefore

\[
g=1/4.
\]

With coefficient support size eight,

\[
L_{\mathrm{joint-parity}}(B)
=
\frac{1/4}{8}
=
\frac1{32}.
\]

Thus

\[
\boxed{L_{84}(B)=\frac1{32}>0=L_{83}(B).}
\]

**Classification:** project-derived exact-rational constructive witness verified by the authoritative P84 regression suite.

---

## 12. Global partition certificate

For an active partition $\mathcal B$ of the complete P75 parameter cube,

\[
L_{84}(\mathcal B)
=
\min_{B\in\mathcal B}L_{84}(B)
\le
d_\infty(\widehat p,\mathcal M_{4,2}).
\]

**Classification:** branch-and-bound lower-envelope logic inherited from P78-P83 with the stronger P84 box lower bound.

P84 deliberately retains the P78 mesh-width upper certificate. No new P84 convergence-rate theorem is assumed.

---

## 13. P79 rejection gate

With P79 certified sampling-radius upper envelope $\overline\varepsilon_{79}$,

\[
L_{84}(\mathcal B)>\overline\varepsilon_{79}
\]

is sufficient for the P77 full-law rejection conclusion under the declared assumptions.

**Classification:** imported P77/P79 rejection logic with the stronger P84 model-distance lower bound.

Failure of the strict inequality is inconclusive and is not model validation.

---

## 14. Executable provenance

Implementation:

- [`joint_projection_parity_contrast_separation.py`](../src/consciousness_bridge/joint_projection_parity_contrast_separation.py)

Regression tests:

- [`test_joint_projection_parity_contrast_separation.py`](../tests/test_joint_projection_parity_contrast_separation.py)

Canonical proof:

- [Proposition 84](proposition_84_exact_projection_parity_contrast.md)

---

## 15. Scientific boundary

Every P84 equation is conditional on the declared P75 target-view model, the declared P78 parameter box, and the declared $L_\infty$ observed-law metric.

P84 can strengthen evidence that an observed law is incompatible with that declared model because separately compatible parity events may still be jointly incompatible with one shared parameter assignment. It cannot assign experiential meaning to the latent variable, cannot turn non-rejection into model truth, cannot establish a new physical dimension, cannot show that consciousness is nonphysical, and does not close the physical-to-experiential bridge.
