# Proposition 24: anytime-valid adaptive physical-refinement certification

## Status

**Repository proposition. Proved for one finite-alphabet IID data stream using an explicit summable alpha-spending schedule.**

P24 converts the fixed-sample P23 post-selection theorem into a time-uniform certificate. It permits repeated inspection of the same growing data stream, adaptive choice among admissible deterministic physical refinements at each inspection, and stopping at a data-dependent finite time without invalidating the stated coverage guarantee.

The construction is intentionally conservative. It uses a countable union bound over sample sizes rather than an optimized martingale, e-process, or mixture confidence sequence.

---

## 1. Why P24 is needed

P23 establishes fixed-sample post-selection validity. At a prespecified sample size \(n\), one confidence event for the base law \((\Omega,E)\) controls every deterministic descriptor pushforward, so a candidate may be selected using the same sample without an additional candidate-count confidence penalty.

That result does not justify the following procedure:

1. collect data;
2. inspect the current refinement certificate;
3. collect more data if the result is not yet persuasive;
4. inspect again;
5. stop when a desired condition is first satisfied.

Applying a fixed-\(n\) confidence statement after such repeated inspection can invalidate its nominal error guarantee. P24 therefore asks:

> Can the physical-refinement program obtain one confidence event that is valid simultaneously over all positive sample sizes, all admissible deterministic descriptors, and any finite stopping time based on the observed history?

Within the present finite-alphabet IID model, the answer is yes.

---

## 2. Base stochastic model

Let

\[
Z_i=(\Omega_i,E_i),
\qquad
Z_1,Z_2,\ldots\overset{\mathrm{IID}}{\sim}P,
\]

on a finite alphabet

\[
\mathcal Z
=
\mathcal X_\Omega\times\mathcal X_E,
\qquad
M=|\mathcal Z|.
\]

Let \(\widehat P_n\) denote the empirical law of the first \(n\) observations.

For a fixed time \(n\), P20-P23 provide a base total-variation certificate with an assigned failure probability. P24 distributes the total failure budget across all positive integers.

---

## 3. Alpha-spending schedule

Fix a total error level

\[
0<\alpha<1.
\]

Define

\[
\boxed{
\alpha_n
=
\frac{6\alpha}{\pi^2n^2},
\qquad
n=1,2,\ldots
}
\]

Using the Basel identity

\[
\sum_{n=1}^{\infty}\frac1{n^2}
=
\frac{\pi^2}{6},
\]

we have

\[
\boxed{
\sum_{n=1}^{\infty}\alpha_n
=
\alpha.
}
\]

The error budget is therefore exactly allocated across the countably infinite sequence of sample sizes.

---

## 4. Time-indexed base-law radius

At time \(n\), apply the P20 cellwise Hoeffding construction to the base alphabet of size \(M\) using local error level \(\alpha_n\). Define

\[
\tau_n^{\mathrm{any}}(\alpha)
=
\min\left\{
1,
\frac M2
\sqrt{
\frac1{2n}
\log\frac{2M}{\alpha_n}
}
\right\}.
\]

Substituting the alpha-spending schedule gives

\[
\boxed{
\tau_n^{\mathrm{any}}(\alpha)
=
\min\left\{
1,
\frac M2
\sqrt{
\frac1{2n}
\log\left(
\frac{M\pi^2n^2}{3\alpha}
\right)
}
\right\}.
}
\]

For each \(n\), let

\[
\mathcal A_n
=
\left\{
\|P-\widehat P_n\|_{\mathrm{TV}}
\le
\tau_n^{\mathrm{any}}(\alpha)
\right\}.
\]

The P20 finite-alphabet concentration argument gives

\[
\Pr(\mathcal A_n^c)
\le
\alpha_n.
\]

---

## 5. Proposition 24A: time-uniform base-law confidence event

Define

\[
\mathcal A_{\infty}
=
\bigcap_{n=1}^{\infty}\mathcal A_n.
\]

Then

\[
\Pr(\mathcal A_{\infty}^c)
=
\Pr\left(
\bigcup_{n=1}^{\infty}\mathcal A_n^c
\right)
\le
\sum_{n=1}^{\infty}\Pr(\mathcal A_n^c)
\le
\sum_{n=1}^{\infty}\alpha_n
=
\alpha.
\]

Hence

\[
\boxed{
\Pr\left(
\forall n\ge1,
\ \|P-\widehat P_n\|_{\mathrm{TV}}
\le
\tau_n^{\mathrm{any}}(\alpha)
\right)
\ge
1-\alpha.
}
\]

This is the time-uniform event from which all subsequent P24 conclusions follow.

---

## 6. Uniform descriptor control at every time

Let \(\mathcal F\) denote an admissible class of deterministic physical descriptors

\[
T_f=f(\Omega).
\]

For any deterministic map \(h\), P23 uses total-variation contraction

\[
\|h_\#P-h_\#\widehat P_n\|_{\mathrm{TV}}
\le
\|P-\widehat P_n\|_{\mathrm{TV}}.
\]

Therefore, on \(\mathcal A_\infty\),

\[
\boxed{
\|h_\#P-h_\#\widehat P_n\|_{\mathrm{TV}}
\le
\tau_n^{\mathrm{any}}(\alpha)
\quad
\forall n\ge1,
\quad
\forall h.
}
\]

This is stronger than a collection of separately calibrated candidate-time statements. One event controls every deterministic pushforward at every positive integer time.

---

## 7. Adaptive descriptor selection at every time

Let \(T_c=c(\Omega)\) be a common coarse descriptor. For each candidate \(f\), define

\[
G_f
=
I(E;T_f\mid T_c)
\]

and

\[
R_f
=
I(E;\Omega\mid T_f).
\]

At time \(n\), let the analysis choose a descriptor using the observed history:

\[
\boxed{
\widehat f_n
=
S_n(Z_1,\ldots,Z_n).
}
\]

For example,

\[
\widehat f_n
\in
\operatorname*{arg\,max}_{f\in\mathcal F}
\widehat G_{f,n}.
\]

Because P23's selected-candidate bounds are deterministic consequences of the base-law event, on \(\mathcal A_\infty\) they hold simultaneously for every time:

\[
\boxed{
G_{\widehat f_n}
\in
\mathcal I^G_{n,\widehat f_n}
\quad\text{and}\quad
R_{\widehat f_n}
\in
\mathcal I^R_{n,\widehat f_n}
\qquad
\forall n\ge1.
}
\]

Therefore

\[
\boxed{
\Pr\left(
G_{\widehat f_n}\in\mathcal I^G_{n,\widehat f_n},
\ R_{\widehat f_n}\in\mathcal I^R_{n,\widehat f_n}
\ \forall n\ge1
\right)
\ge1-\alpha.
}
\]

Adaptive descriptor selection and repeated inspection are both covered by the same event.

---

## 8. Proposition 24B: stopping-time validity

Let

\[
\mathcal F_n
=
\sigma(Z_1,\ldots,Z_n)
\]

be the natural filtration, and let \(\tau\) be any stopping time with respect to \((\mathcal F_n)_{n\ge1}\).

Suppose first that \(\tau<\infty\) almost surely. On the event \(\mathcal A_\infty\), the selected-candidate certificate is valid at **every** positive integer time. In particular it is valid at the random time \(\tau\). Hence

\[
\boxed{
\Pr\left(
G_{\widehat f_\tau}
\in
\mathcal I^G_{\tau,\widehat f_\tau},
\quad
R_{\widehat f_\tau}
\in
\mathcal I^R_{\tau,\widehat f_\tau}
\right)
\ge1-\alpha.
}
\]

More generally, without assuming almost-sure finiteness,

\[
\boxed{
\Pr\left(
\tau<\infty
\Longrightarrow
\left[
G_{\widehat f_\tau}\in\mathcal I^G_{\tau,\widehat f_\tau}
\text{ and }
R_{\widehat f_\tau}\in\mathcal I^R_{\tau,\widehat f_\tau}
\right]
\right)
\ge1-\alpha.
}
\]

The proof does not invoke a special optional-stopping identity. It uses the stronger fact that the confidence event holds at every time simultaneously.

---

## 9. Anytime-valid refinement regret

P23 proves, at a fixed time,

\[
0
\le
G^*-G_{\widehat f}
\le
\max_fU_f^G-L_{\widehat f}^G
\le
2\Gamma_{\max}.
\]

On \(\mathcal A_\infty\), the same argument holds at every time \(n\). Therefore

\[
\boxed{
0
\le
G^*-G_{\widehat f_n}
\le
B_n
:=
\max_fU_{f,n}^G-L_{\widehat f_n,n}^G
\qquad
\forall n\ge1.
}
\]

Consequently, at any finite stopping time \(\tau\),

\[
\boxed{
0
\le
G^*-G_{\widehat f_\tau}
\le
B_\tau
}
\]

with the same global confidence level at least \(1-\alpha\).

By the P21 identity for a common coarse descriptor,

\[
R_f=R_c-G_f,
\]

so

\[
\boxed{
R_{\widehat f_n}
-
\min_fR_f
=
G^*-G_{\widehat f_n}
\le
B_n
\qquad
\forall n\ge1.
}
\]

The selected descriptor is therefore accompanied by a time-uniform near-optimality certificate relative to the declared admissible class.

---

## 10. Example stopping rules covered by P24

Because the guarantee is simultaneous in time, it applies to stopping rules such as:

\[
\tau_{\mathrm{gain}}
=
\inf\{n:L^G_{n,\widehat f_n}>0\},
\]

the first time the selected refinement gain has a positive lower confidence bound;

\[
\tau_{\mathrm{regret}}
=
\inf\{n:B_n\le\varepsilon\},
\]

the first time the selected refinement is certified to be within a desired regret tolerance \(\varepsilon\); or

\[
\tau_{\mathrm{res}}
=
\inf\{n:U^R_{n,\widehat f_n}\le\varepsilon_R\},
\]

the first time the remaining residual is certified below a prespecified threshold.

These are examples of statistical stopping criteria only. They do not define physical completeness or an experiential threshold.

---

## 11. Why P24 is conservative

The alpha-spending sequence assigns a separate local failure budget to every positive integer sample size and uses a union bound. Consequently the local level decreases approximately as

\[
\alpha_n\propto n^{-2},
\]

and the logarithmic term in the radius contains

\[
\log n^2.
\]

Thus the radius has the qualitative large-\(n\) order

\[
\tau_n^{\mathrm{any}}
=
O\left(
M\sqrt{\frac{\log n}{n}}
\right)
\]

before accounting for clipping at one and the subsequent entropy-continuity transformation.

Sharper time-uniform concentration methods may improve constants or logarithmic behavior. P24 deliberately chooses a transparent proof whose coverage can be checked directly from elementary concentration and the Basel identity.

---

## 12. What P24 does not establish

P24 does not establish:

1. **Optimal confidence sequences.** The alpha-spending construction is conservative.
2. **Validity under arbitrary temporal dependence.** The base stream is IID under the stated theorem.
3. **Continuous-state generality.** The current radius is finite-alphabet.
4. **Changing physical alphabets without accounting.** The declared \(\Omega\) and \(E\) alphabets are fixed for the theorem.
5. **Arbitrary descriptor objects.** Candidate descriptors remain deterministic functions of the declared physical state and must satisfy the P23 physical-refinement requirements.
6. **Physical admissibility from statistics alone.** Target-engineered or scientifically artificial maps remain possible mathematical descriptors but are not thereby physical explanations.
7. **Physical completeness.** A terminal residual or a vanishing residual is still relative to the declared physical state, descriptor class, and measurement model.
8. **An experiential theorem.** No bridge from physical structure to subjective experience is established by the stopping-time result.

---

## 13. Scientific interpretation boundary

P24 removes one important statistical loophole: a positive result cannot be defended by saying that the analysis merely looked repeatedly until the fixed-sample confidence interval happened to cross a desired threshold. The theorem explicitly accounts for repeated looks across all positive sample sizes.

It does **not** remove the deeper scientific requirements:

\[
\boxed{
\text{anytime statistical validity}
\neq
\text{physical completeness}
\neq
\text{experiential interpretation}.
}
\]

Those remain separate problems.

---

## 14. Relation to P19-P24

The physical-sufficiency sequence is now

\[
\boxed{
\begin{aligned}
&\text{P19: population physical sufficiency}\\
&\Downarrow\\
&\text{P20: one finite-sample residual certificate}\\
&\Downarrow\\
&\text{P21: residual behavior under physical refinement}\\
&\Downarrow\\
&\text{P22: simultaneous certification of a fixed refinement chain}\\
&\Downarrow\\
&\text{P23: fixed-sample adaptive descriptor selection}\\
&\Downarrow\\
&\text{P24: time-uniform adaptive selection and stopping-time validity.}
\end{aligned}
}
\]

This closes the most immediate optional-stopping gap in the finite-alphabet IID version of the refinement audit.

---

## 15. Next mathematical frontier

The natural next statistical improvements are no longer conceptual fixes but sharper generalizations:

- replace the conservative alpha-spending union bound with tighter time-uniform concentration;
- extend from IID categorical streams to dependent or mixing data;
- incorporate noisy or estimated physical descriptors rather than deterministic observed maps;
- develop continuous-state analogues;
- quantify model-class complexity when descriptors themselves are estimated from flexible function classes;
- connect the statistical refinement program more directly to intervention-resolved causal structure rather than purely observational conditional information.

The most scientifically important next bridge problem remains independent of these statistical refinements: how to define experiential variables without building the desired conclusion into the definition.

---

## 16. Reproducibility

Implementation:

- [`anytime_refinement_certification.py`](../src/consciousness_bridge/anytime_refinement_certification.py)

Regression tests:

- [`test_anytime_refinement_certification.py`](../tests/test_anytime_refinement_certification.py)

Predecessor results:

- [P20 finite-sample residual certification](proposition_20_finite_sample_residual_certification.md)
- [P21 descriptor refinement and residual persistence](proposition_21_descriptor_refinement_residual_persistence.md)
- [P22 simultaneous refinement-chain certification](proposition_22_simultaneous_refinement_chain_certification.md)
- [P23 adaptive descriptor selection certification](proposition_23_adaptive_descriptor_selection_certification.md)

The P24 certificate remains conditional on the declared finite-alphabet IID model and the independent scientific admissibility of the physical descriptors entering the refinement program.
