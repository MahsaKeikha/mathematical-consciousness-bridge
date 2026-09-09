# Proposition 23: adaptive physical-descriptor selection under a shared base confidence ball

## Status

**Repository proposition. Proved for a finite-alphabet IID base law at a fixed sample size.**

This proposition extends the P22 simultaneous finite-sample construction from a fixed refinement chain to data-dependent selection among candidate physical refinements. Its purpose is to control a common scientific workflow: inspect finite data, compare several physically motivated refinements, and choose the refinement that appears to remove the largest portion of the P21 residual.

The result is a post-selection theorem. It is not an optional-stopping theorem, a proof of physical completeness, or an experiential theorem.

---

## 1. Why P23 is needed

P19 defines the descriptor-relative stochastic residual

\[
R(T)=I(E;\Omega\mid T).
\]

P21 proves that if \(T_f\) refines \(T_c\), then

\[
R(T_c)
=
I(E;T_f\mid T_c)
+
R(T_f).
\]

P22 then gives simultaneous finite-sample confidence intervals along a declared refinement chain by starting from one confidence event for the base law \(P_{\Omega E}\).

A realistic refinement program is often adaptive. A researcher may compare several candidate physical descriptors using the same data and select the candidate with the largest empirical refinement gain. A theorem is therefore needed to answer:

> If the refinement is selected after inspecting the same sample used to estimate its gain, does the finite-sample certificate remain valid?

For the finite deterministic-descriptor setting studied here, the answer is yes under one crucial structural condition: every candidate is a genuine deterministic map of the same declared physical state \(\Omega\).

---

## 2. Setup

Let

\[
(\Omega,E)\sim P
\]

have finite alphabets \(\mathcal X_\Omega\) and \(\mathcal X_E\). Let

\[
Z_1,\ldots,Z_n,
\qquad
Z_i=(\Omega_i,E_i),
\]

be IID samples from \(P\), with empirical law \(\widehat P_n\).

Fix a common coarse physical descriptor

\[
T_c=c(\Omega).
\]

Let \(\mathcal F\) be a class of candidate fine descriptors. For each \(f\in\mathcal F\),

\[
T_f=f(\Omega),
\]

and assume \(T_f\) refines \(T_c\). Equivalently, there exists a deterministic map \(q_f\) such that

\[
T_c=q_f(T_f).
\]

For each candidate define the P21 refinement gain

\[
\boxed{
G_f
:=
I_P(E;T_f\mid T_c)
}
\]

and the remaining residual

\[
\boxed{
R_f
:=
I_P(E;\Omega\mid T_f).
}
\]

P21 gives the exact identity

\[
\boxed{
R_c-R_f=G_f,
\qquad
R_c:=I_P(E;\Omega\mid T_c).
}
\]

The same identity holds for the empirical distribution:

\[
\boxed{
\widehat R_c-\widehat R_f=\widehat G_f.
}
\]

---

## 3. The shared base confidence event

Let

\[
M_0
=
|\mathcal X_\Omega|\,|\mathcal X_E|.
\]

Using the same finite-alphabet Hoeffding construction as P20 and P22, define

\[
\boxed{
\tau_n(\alpha)
=
\min\left\{
1,
\frac{M_0}{2}
\sqrt{
\frac{1}{2n}
\log\frac{2M_0}{\alpha}
}
\right\}.
}
\]

Then the base event

\[
\boxed{
\mathcal A_n
=
\left\{
\|P-\widehat P_n\|_{\mathrm{TV}}
\le
\tau_n(\alpha)
\right\}
}
\]

satisfies

\[
\Pr(\mathcal A_n)\ge1-\alpha.
\]

Everything in P23 will be derived deterministically on \(\mathcal A_n\).

---

## 4. Lemma: universal deterministic-pushforward control

Let \(h\) be any deterministic map on the declared base alphabet. Then total variation contracts under pushforward:

\[
\boxed{
\|h_\#P-h_\#\widehat P_n\|_{\mathrm{TV}}
\le
\|P-\widehat P_n\|_{\mathrm{TV}}.
}
\]

Therefore, on \(\mathcal A_n\),

\[
\boxed{
\|h_\#P-h_\#\widehat P_n\|_{\mathrm{TV}}
\le
\tau_n(\alpha)
\quad
\text{for every deterministic }h.
}
\]

### Proof

For any event \(B\) in the codomain of \(h\),

\[
(h_\#P)(B)- (h_\#\widehat P_n)(B)
=
P(h^{-1}(B))-\widehat P_n(h^{-1}(B)).
\]

Taking the supremum over codomain events can only be smaller than taking the supremum over all events in the original sample space. Hence

\[
\|h_\#P-h_\#\widehat P_n\|_{\mathrm{TV}}
\le
\|P-\widehat P_n\|_{\mathrm{TV}}.
\]

The conclusion is pathwise. Once \(\mathcal A_n\) occurs, it holds for every deterministic pushforward simultaneously. \(\square\)

---

## 5. Consequence: uniform candidate control

For every candidate \(f\), define the residual pushforward

\[
\phi_f(\omega,e)
=
(\omega,f(\omega),e)
\]

and the gain pushforward

\[
\psi_f(\omega,e)
=
(f(\omega),c(\omega),e).
\]

Both are deterministic functions of the same base pair \((\Omega,E)\). Therefore, on \(\mathcal A_n\),

\[
\|P_f^R-\widehat P_f^R\|_{\mathrm{TV}}
\le
\tau_n(\alpha)
\]

and

\[
\|P_f^G-\widehat P_f^G\|_{\mathrm{TV}}
\le
\tau_n(\alpha)
\]

for **all candidates simultaneously**.

Let \(\Delta_f^R(\tau)\) and \(\Delta_f^G(\tau)\) denote the finite-alphabet conditional-information continuity bounds obtained from P20. Then

\[
\boxed{
|R_f-\widehat R_f|
\le
\Delta_f^R(\tau_n)
\quad\forall f\in\mathcal F
}
\]

and

\[
\boxed{
|G_f-\widehat G_f|
\le
\Delta_f^G(\tau_n)
\quad\forall f\in\mathcal F
}
\]

on the same event \(\mathcal A_n\).

No additional candidate-wise probabilistic union bound has been introduced. The probability statement was made once at the level of the base law.

---

## 6. Proposition 23A: post-selection validity

Let

\[
\widehat f
=
S(\widehat P_n)
\]

be any measurable data-dependent rule that returns a candidate deterministic descriptor from the admissible class. The selection rule may compare empirical gains, empirical residuals, or other sample-derived statistics.

Because the candidate inequalities in Section 5 hold simultaneously on \(\mathcal A_n\), they hold in particular for the selected candidate:

\[
\boxed{
|G_{\widehat f}-\widehat G_{\widehat f}|
\le
\Delta_{\widehat f}^G(\tau_n)
}
\]

and

\[
\boxed{
|R_{\widehat f}-\widehat R_{\widehat f}|
\le
\Delta_{\widehat f}^R(\tau_n).
}
\]

Therefore the selected-candidate confidence intervals have coverage at least \(1-\alpha\):

\[
\boxed{
\Pr\left(
G_{\widehat f}\in\mathcal I^G_{\widehat f}
\text{ and }
R_{\widehat f}\in\mathcal I^R_{\widehat f}
\right)
\ge1-\alpha.
}
\]

### Why selection does not create a new confidence penalty here

The statement is not obtained by first building one confidence event per candidate and then selecting among them. Instead, one event \(\mathcal A_n\) controls the complete base distribution, and candidate-level statements are deterministic consequences of that event.

Thus candidate selection does not consume additional confidence mass in this construction.

This does **not** imply that arbitrary model selection is free in general. The result depends on the shared-base-law structure and deterministic pushforward relation.

---

## 7. Proposition 23B: empirical-gain maximization and regret

Suppose the selection rule chooses

\[
\boxed{
\widehat f
\in
\operatorname*{arg\,max}_{f\in\mathcal F}
\widehat G_f.
}
\]

Let

\[
f^*
\in
\operatorname*{arg\,max}_{f\in\mathcal F}
G_f
\]

be a population-optimal admissible refinement.

Write

\[
\Gamma_f
=
\Delta_f^G(\tau_n),
\qquad
\Gamma_{\max}
=
\sup_{f\in\mathcal F}\Gamma_f.
\]

On \(\mathcal A_n\),

\[
\begin{aligned}
G_{f^*}-G_{\widehat f}
&\le
\widehat G_{f^*}+\Gamma_{f^*}
-
\widehat G_{\widehat f}+\Gamma_{\widehat f}\\
&\le
\Gamma_{f^*}+\Gamma_{\widehat f}\\
&\le
2\Gamma_{\max}.
\end{aligned}
\]

Hence

\[
\boxed{
0
\le
G^*-G_{\widehat f}
\le
2\Gamma_{\max}
}
\]

with probability at least \(1-\alpha\), where

\[
G^*=\max_{f\in\mathcal F}G_f.
\]

This is a finite-sample near-optimality certificate for the empirically selected physical refinement.

---

## 8. Data-dependent regret certificate

Let

\[
L_f^G
=
\max\{0,\widehat G_f-\Gamma_f\}
\]

and

\[
U_f^G
=
\min\{G_{\max,f},\widehat G_f+\Gamma_f\}
\]

be simultaneous lower and upper gain bounds.

Since every population gain lies in its interval on \(\mathcal A_n\),

\[
G^*
\le
\max_f U_f^G
\]

and

\[
G_{\widehat f}
\ge
L_{\widehat f}^G.
\]

Therefore

\[
\boxed{
G^*-G_{\widehat f}
\le
\max_f U_f^G
-
L_{\widehat f}^G.
}
\]

This quantity is observable from the simultaneous certificate and may be substantially smaller than the generic \(2\Gamma_{\max}\) bound.

---

## 9. Corollary: residual near-optimality

For every candidate refinement of the same coarse descriptor, P21 gives

\[
R_f
=
R_c-G_f.
\]

Consequently,

\[
\begin{aligned}
R_{\widehat f}
-
\min_f R_f
&=
(R_c-G_{\widehat f})
-
(R_c-G^*)\\
&=
G^*-G_{\widehat f}.
\end{aligned}
\]

Thus the same regret certificate controls how far the selected descriptor is from the smallest achievable residual in the declared candidate class:

\[
\boxed{
R_{\widehat f}
-
\min_f R_f
=
G^*-G_{\widehat f}
\le
\max_f U_f^G-L_{\widehat f}^G
\le
2\Gamma_{\max}.
}
\]

This is an important interpretation of P23. The theorem does not merely state that the selected interval is valid. It quantifies how close the selected refinement is to the best refinement available within the declared admissible class.

---

## 10. Candidate count and statistical complexity

The P23 confidence allocation does not contain a direct factor such as

\[
\log|\mathcal F|
\]

or a replacement

\[
\alpha\mapsto\alpha/|\mathcal F|.
\]

That absence is structural, not magical. The confidence event controls the finite base law itself. All candidate distributions are deterministic pushforwards of that one law.

There is still a serious complexity cost. The base radius depends on

\[
M_0
=
|\mathcal X_\Omega|\,|\mathcal X_E|.
\]

If the declared physical alphabet is enormous, the conservative P20/P22/P23 bound can become numerically weak. A large or continuous state space therefore requires sharper concentration, structural models, compression with certified sufficiency, or other estimator-specific methods.

Candidate count may be free in the confidence bookkeeping while physical-state complexity is not.

---

## 11. Synthetic checkpoint

Let

\[
\Omega\in\{0,1,2,3\}
\]

be uniform and let

\[
E=\Omega\bmod2.
\]

Take the coarse descriptor to be constant:

\[
T_c(\omega)=0.
\]

Compare the candidate refinements

\[
T_{\mathrm{good}}(\omega)=\omega\bmod2,
\]

\[
T_{\mathrm{partial}}(0)=0,
\qquad
T_{\mathrm{partial}}(1)=T_{\mathrm{partial}}(2)=T_{\mathrm{partial}}(3)=1,
\]

and

\[
T_{\mathrm{bad}}(\omega)=0.
\]

For the population law,

\[
G_{\mathrm{good}}=\log2,
\qquad
R_{\mathrm{good}}=0.
\]

The executable P23 test constructs a large balanced IID sample and verifies that empirical gain maximization selects the good refinement, the empirical gain equals \(\log2\) to numerical precision, and the remaining empirical residual is zero to numerical precision.

This is a synthetic mathematical calibration only. It is not an empirical consciousness result.

---

## 12. Statistical validity versus physical admissibility

P23 separates two questions that must not be conflated.

### Statistical question

Does selection after inspecting the sample invalidate the finite-sample interval?

Within the P23 finite deterministic-map model, no. The shared base event controls all candidate pushforwards pathwise.

### Physical question

Is the selected map a scientifically meaningful physical descriptor?

That does not follow from P23. A candidate may be statistically well certified yet physically artificial. For a candidate to enter the physical-to-experiential program, its definition must still be justified by physical variables, system boundaries, measurement models, intervention semantics, scale, and independently defensible modeling assumptions.

In particular, a lookup table engineered from target labels can still be a mathematical function of \(\Omega\) after construction. P23's probability theorem does not transform such a construction into a physically explanatory variable.

The correct interpretation is therefore

\[
\boxed{
\text{post-selection statistical validity}
\neq
\text{physical admissibility}.
}
\]

---

## 13. What P23 does not establish

P23 does not establish any of the following:

1. **Optional-stopping validity.** The theorem is for a fixed sample size \(n\). Repeatedly collecting more data and stopping when a desired certificate appears requires an anytime-valid construction.
2. **Physical completeness.** A selected refinement is optimal only relative to the declared admissible class.
3. **Experiential ontology.** A residual after adaptive physical refinement is still a descriptor-relative statistical object.
4. **Continuous-state generality.** The present certificate uses finite-alphabet entropy continuity.
5. **Causal validity from association alone.** The information gain is conditional mutual information in the declared joint law. Causal interpretation needs the physical intervention structure defined elsewhere in the repository.
6. **Protection against arbitrary target leakage in scientific model construction.** The probability statement can remain true even for a scientifically unhelpful target-engineered map. Physical admissibility is an independent requirement.

---

## 14. Falsification and failure modes

The P23 certificate should be rejected or weakened if any of the following occurs:

- the records are not adequately modeled as IID for the stated experiment;
- the declared base alphabet is incomplete or changes during analysis;
- the selected candidate is not a deterministic function of the declared \(\Omega\);
- the candidate does not refine the common coarse descriptor;
- candidate labels exceed the declared alphabet used in the continuity bound;
- the analysis repeatedly changes sample size and stops adaptively without an anytime-valid correction;
- the physical meaning of the selected descriptor cannot be defended independently of its statistical fit;
- replication fails on new samples or new systems.

---

## 15. Relation to P19-P22

The logic is now

\[
\boxed{
\begin{aligned}
&\text{P19: define and test descriptor-relative physical sufficiency}\\
&\Downarrow\\
&\text{P20: certify one residual from finite data}\\
&\Downarrow\\
&\text{P21: quantify residual change under physical refinement}\\
&\Downarrow\\
&\text{P22: certify a whole fixed refinement chain simultaneously}\\
&\Downarrow\\
&\text{P23: retain validity after data-dependent descriptor selection.}
\end{aligned}
}
\]

The next unresolved statistical problem is time-uniform validity: can a refinement program inspect the data repeatedly as sample size grows and stop at a data-dependent time while retaining a valid certificate? That requires a confidence-sequence or other anytime-valid construction and is not claimed by P23.

---

## 16. Reproducibility

Implementation:

- [`adaptive_descriptor_selection.py`](../src/consciousness_bridge/adaptive_descriptor_selection.py)

Regression tests:

- [`test_adaptive_descriptor_selection.py`](../tests/test_adaptive_descriptor_selection.py)

Predecessor results:

- [P19 fundamental physical sufficiency](proposition_19_fundamental_physical_sufficiency.md)
- [P20 finite-sample residual certification](proposition_20_finite_sample_residual_certification.md)
- [P21 descriptor refinement and residual persistence](proposition_21_descriptor_refinement_residual_persistence.md)
- [P22 simultaneous refinement-chain certification](proposition_22_simultaneous_refinement_chain_certification.md)

The theorem remains conditional on the explicitly declared finite-alphabet IID model and the physical admissibility of the candidate descriptors used in the scientific interpretation.
