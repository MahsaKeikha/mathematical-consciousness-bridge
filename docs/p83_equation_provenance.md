# P83 Equation and Provenance Record

## Scope

This record classifies the equations used in [Proposition 83](proposition_83_exact_projection_parity.md), **Exact Projection-Parity Certificate for Continuous P75 Separation**.

P83 is a downstream computational-certification theorem for the same four-view binary latent family introduced in P75 and the same full-law $L_\infty$ rejection architecture developed through P77-P82.

The new mathematical step is an exact rational parameter-box extremization of projection-parity probabilities, followed by an event-mass lower bound that is combined with the complete P82 certificate.

P83 introduces no consciousness variable and no new physical postulate.

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

## 2. Projection-parity event

For a selected view set $J\subseteq\{1,2,3,4\}$ and $b\in\{0,1\}$,

\[
H(J,b)
=
\left\{x:\bigoplus_{j\in J}x_j=b\right\}.
\]

For every nonempty $J$, exactly half of the sixteen full outcomes satisfy either parity value, so

\[
|H(J,b)|=8.
\]

**Classification:** standard finite binary parity definition, specialized as a P83 observable family.

P83 uses only $|J|\ge2$ because one-view parity events are ordinary P81 cylinders.

---

## 3. Bernoulli parity character identity

For independent Bernoulli variables in one P75 latent branch,

\[
\mathbb E_s\left[(-1)^{\sum_{j\in J}X_j}\right]
=
\prod_{j\in J}\mathbb E_s[(-1)^{X_j}]
=
\prod_{j\in J}(1-2q_{j,s}).
\]

Since the expectation equals the even-parity probability minus the odd-parity probability, while those probabilities sum to one,

\[
\boxed{
P_s(H(J,b))
=
\frac{1+(-1)^b\prod_{j\in J}(1-2q_{j,s})}{2}.
}
\]

**Classification:** standard Bernoulli parity/Fourier-character identity applied to the P75 conditional-independence branch.

**New P83 use:** the identity is used as an exact box-certification observable, not as a definition of the latent state or of experience.

---

## 4. Exact transformed-factor intervals

If

\[
q_{j,s}\in[\ell_{j,s},u_{j,s}],
\]

then the affine transform gives

\[
1-2q_{j,s}
\in
[1-2u_{j,s},1-2\ell_{j,s}].
\]

**Classification:** elementary affine interval transformation.

**Numerical status:** exact rational arithmetic for rational parameter-box endpoints.

---

## 5. Exact product interval by vertex evaluation

Define

\[
Z_s(J)=\prod_{j\in J}(1-2q_{j,s}).
\]

$Z_s(J)$ is multi-affine in the selected response coordinates. Therefore its minimum and maximum over an axis-aligned box occur at vertices:

\[
\boxed{
[z_s^L,z_s^U]
=
\left[
\min_{v\in V_J} Z_s(v),
\max_{v\in V_J} Z_s(v)
\right],
}
\]

where $V_J$ contains the $2^{|J|}$ endpoint choices.

**Classification:** standard multi-affine box-extremum principle, used here as the new exact P83 product certificate.

**Implementation:** endpoint products are evaluated with `fractions.Fraction`; no floating optimizer is used for certification.

---

## 6. Exact branchwise parity interval

Applying the affine parity transform to the exact product interval gives

\[
P_s(H(J,0))
\in
\left[
\frac{1+z_s^L}{2},
\frac{1+z_s^U}{2}
\right]
\]

for even parity, and

\[
P_s(H(J,1))
\in
\left[
\frac{1-z_s^U}{2},
\frac{1-z_s^L}{2}
\right]
\]

for odd parity.

**Classification:** new P83 exact branchwise interval consequence.

---

## 7. Exact latent-mixture interval

Write

\[
P_-(H)\in[h_-^L,h_-^U],
\qquad
P_+(H)\in[h_+^L,h_+^U].
\]

The branch response coordinates are disjoint, so branch extrema are jointly attainable. For prevalence $\pi$,

\[
q(H)=(1-\pi)P_-(H)+\pi P_+(H).
\]

The lower and upper envelopes are

\[
L(\pi)=(1-\pi)h_-^L+\pi h_+^L,
\]

\[
U(\pi)=(1-\pi)h_-^U+\pi h_+^U.
\]

Both are affine in prevalence, hence exact extrema on $[\pi_L,\pi_U]$ occur at a prevalence endpoint:

\[
\ell_H
=
\min_{\pi\in\{\pi_L,\pi_U\}}L(\pi),
\qquad
u_H
=
\max_{\pi\in\{\pi_L,\pi_U\}}U(\pi).
\]

**Classification:** new P83 exact mixture-extremum theorem.

---

## 8. Event-mass $L_\infty$ transfer

For every finite event $S$,

\[
\begin{aligned}
|\widehat p(S)-q(S)|
&=\left|\sum_{x\in S}(\widehat p_x-q_x)\right|\\
&\le\sum_{x\in S}|\widehat p_x-q_x|\\
&\le |S|\,\|\widehat p-q\|_\infty.
\end{aligned}
\]

**Classification:** standard triangle inequality and $L_\infty$ definition, imported from the P81/P82 event certificates.

---

## 9. Single parity-event lower bound

Every P83 parity event has support size eight. Therefore

\[
\boxed{
\|\widehat p-q(\theta)\|_\infty
\ge
\frac{
d\!\left(
\widehat p(H),
[\ell_H,u_H]
\right)
}{8}.
}
\]

**Classification:** new P83 certificate obtained by combining the exact parity interval with the established event-mass transfer principle.

---

## 10. Standard family size

P83 includes both parity values on every two-, three-, and four-view subset:

\[
\begin{aligned}
|\mathcal P|
&=2\left[{4\choose2}+{4\choose3}+{4\choose4}\right]\\
&=2(6+4+1)\\
&=22.
\end{aligned}
\]

**Classification:** new P83 finite-family definition plus direct combinatorial count.

---

## 11. Combined P83 certificate

P83 defines

\[
L_{\mathrm{par}}(B)
=
\max_{(J,b)\in\mathcal P}
\frac{
d\!\left(
\widehat p(H(J,b)),
[\ell_{J,b}(B),u_{J,b}(B)]
\right)
}{8},
\]

then

\[
\boxed{
L_{83}(B)=\max\{L_{82}(B),L_{\mathrm{par}}(B)\}.
}
\]

Hence

\[
L_{83}(B)
\ge L_{82}(B)
\ge L_{81}(B)
\ge L_{80}(B)
\ge L_{78}(B).
\]

**Classification:** new P83 combination theorem.

---

## 12. Strict improvement witness

The P83 witness fixes

\[
q_{3,-}=q_{3,+}=\frac12
\]

and uses

\[
\widehat p_x
=
\begin{cases}
1/8,&x_3=x_4,\\
0,&x_3\ne x_4.
\end{cases}
\]

Then

\[
q(X_3\oplus X_4=0)=\frac12
\]

for every model law in the box, whereas

\[
\widehat p(X_3\oplus X_4=0)=1.
\]

Thus

\[
L_{\mathrm{par}}=\frac{1/2}{8}=\frac1{16}.
\]

The complete exact-rational executable P82 audit on the same box gives

\[
L_{82}=0,
\]

so

\[
\boxed{L_{83}=\frac1{16}>0=L_{82}.}
\]

**Classification:** project-derived exact-rational constructive witness, verified by exhaustive evaluation of the declared finite P82 and P83 families in regression tests.

---

## 13. Global partition certificate

For an active partition $\mathcal B$ of the complete P75 parameter cube,

\[
L_{83}(\mathcal B)
=
\min_{B\in\mathcal B}L_{83}(B)
\le
d_\infty(\widehat p,\mathcal M_{4,2}).
\]

**Classification:** branch-and-bound lower-envelope logic inherited from P78-P82 with a stronger box lower bound.

P83 deliberately retains the P78 mesh-width upper certificate. No new P83 convergence-rate theorem is assumed.

---

## 14. P79 rejection gate

With P79 certified sampling-radius upper envelope $\overline\varepsilon_{79}$,

\[
L_{83}(\mathcal B)>\overline\varepsilon_{79}
\]

is sufficient for the P77 full-law rejection conclusion.

**Classification:** imported P77/P79 rejection logic with the stronger P83 model-distance lower bound.

---

## 15. Scientific boundary

Every P83 equation is conditional on the declared P75 target-view model and the declared $L_\infty$ observed-law metric.

P83 can strengthen evidence that an observed law is incompatible with that declared model. It cannot assign experiential meaning to the latent variable, cannot turn non-rejection into model truth, cannot establish a new physical dimension, and does not close the physical-to-experiential bridge.
