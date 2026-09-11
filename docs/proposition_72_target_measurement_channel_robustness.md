# Proposition 72: target-measurement channel robustness and noisy-witness transfer

**Status:** proved mathematical measurement-robustness theorem under a declared nondifferential target-observation channel, with a conservative finite-sample certificate.

![P72 target-measurement channel robustness](figures/p72_target_measurement_channel_robustness.svg)

**P72 theorem map.** An independently declared latent target \(E^\star\) is observed through \(Y\). Under the declared nondifferential measurement condition, the observed residual cannot exceed the latent residual. Target noise may attenuate or erase a real witness, and the amount of pairwise separation that survives can be controlled by a channel-stability coefficient.

For equation classification and external context, see the [P72 equation and provenance record](p72_equation_provenance.md).

## 1. Purpose

P71 establishes a logically prior requirement for a meaningful bridge test: the target must not be constructed from the same physical descriptor in a way that makes factorization true by definition.

That still leaves a second problem. An independently justified target may not be observed directly. Reports, behavioral responses, ratings, clinical labels, or other target-side measurements can be noisy.

P72 asks:

> If an independently declared latent target is observed through a noisy measurement channel, what conclusions about physical sufficiency survive the measurement process?

The answer is asymmetric. Under an explicit nondifferential measurement condition, target-side noise cannot create population-level residual target information that was absent from the latent target. It can, however, attenuate or completely erase a genuine latent residual.

P72 formalizes that asymmetry with conditional mutual information and total variation, then gives a finite-sample lower confidence bound for a measured target separation.

The theorem does not declare the latent target to be consciousness. The notation \(E^\star\) means only the independently declared latent target variable that the experimental protocol claims to measure.

---

## 2. Setup

Let \(\Omega\) be the underlying admissible state or history variable, let

\[
T=T(\Omega)
\]

be the declared physical descriptor, and let \(E^\star\) be an independently specified latent target satisfying the P71 provenance requirement.

The experiment observes \(Y\) through a target-measurement channel. P72 assumes the channel is nondifferential relative to the underlying state once the latent target and physical descriptor are fixed:

\[
\boxed{
Y\perp\!\!\!\perp\Omega\mid(E^\star,T).
}
\]

Equivalently, for every positive-mass configuration,

\[
\boxed{
P(y\mid\omega,e,t)=K_t(y\mid e).
}
\]

The channel may depend on \(T\). What is excluded is additional dependence on \(\Omega\) after \((E^\star,T)\) have been fixed. If that exclusion fails, the measurement mechanism itself may carry extra state information and can manufacture an apparent observed residual.

---

## 3. P72A: conditional data-processing theorem

### Proposition

Under

\[
Y\perp\!\!\!\perp\Omega\mid(E^\star,T),
\]

for finite variables,

\[
\boxed{
I(Y;\Omega\mid T)
\le
I(E^\star;\Omega\mid T).
}
\]

### Proof

Condition on a fixed \(T=t\) with positive probability. The measurement premise gives the conditional Markov chain

\[
\Omega\longrightarrow E^\star\longrightarrow Y
\qquad\text{given }T=t.
\]

The standard data-processing inequality gives

\[
I(Y;\Omega\mid T=t)
\le
I(E^\star;\Omega\mid T=t).
\]

Averaging over \(t\),

\[
\begin{aligned}
I(Y;\Omega\mid T)
&=\sum_tP(t)I(Y;\Omega\mid T=t)\\
&\le\sum_tP(t)I(E^\star;\Omega\mid T=t)\\
&=I(E^\star;\Omega\mid T).
\end{aligned}
\]

\(\square\)

The information-theoretic step is standard. P72's repository-specific role is to place it explicitly in the target-measurement layer of the P19/P71 bridge architecture. See [Cover and Thomas](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006) for standard information theory.

### Population no-false-positive corollary

Because conditional mutual information is nonnegative,

\[
I(Y;\Omega\mid T)>0
\]

implies

\[
\boxed{
I(E^\star;\Omega\mid T)>0.
}
\]

Thus, under the P72 premise, a positive observed **population** residual cannot be created solely by nondifferential target-measurement noise. It transfers to the latent target.

This does not justify a positive empirical residual without uncertainty control, and it does not imply that the declared physical descriptor is physically complete.

---

## 4. P72B: the converse fails because measurement can erase a witness

The implication

\[
I(Y;\Omega\mid T)=0
\Longrightarrow
I(E^\star;\Omega\mid T)=0
\]

is false.

Let \(T\) be constant, let

\[
\Omega\sim\operatorname{Bernoulli}(1/2),
\qquad
E^\star=\Omega,
\]

so

\[
I(E^\star;\Omega\mid T)=\log2.
\]

Now use a complete erasure channel,

\[
Y=y_0
\qquad\text{with probability }1.
\]

The P72 premise still holds, but

\[
I(Y;\Omega\mid T)=0.
\]

Therefore

\[
\boxed{
I(E^\star;\Omega\mid T)=\log2,
\qquad
I(Y;\Omega\mid T)=0.
}
\]

A null observed target residual is therefore inconclusive unless the target-measurement channel is known to preserve the distinctions relevant to the bridge test.

---

## 5. Failure of the measurement premise can create a false observed residual

P72 does not assume that every real reporting process satisfies

\[
Y\perp\!\!\!\perp\Omega\mid(E^\star,T).
\]

If the measurement mechanism retains extra dependence on the underlying state, the P72 direction can fail. Let \(T\) and \(E^\star\) both be constant, so

\[
I(E^\star;\Omega\mid T)=0.
\]

If an invalid measurement mechanism directly sets \(Y=\Omega\), then

\[
I(Y;\Omega\mid T)=H(\Omega)>0.
\]

The observed residual is now a property of the measurement mechanism rather than evidence of latent-target variation. This is why the target observation process must be modeled explicitly.

---

## 6. P72C: total-variation witness transfer

Fix a physical descriptor value \(T=t\). Let two underlying cases have latent target laws

\[
p,q\in\Delta(\mathcal E),
\]

and let their common target-measurement channel be \(K_t(y\mid e)\). The observed laws are \(K_tp\) and \(K_tq\).

Stochastic kernels contract total variation:

\[
\boxed{
\operatorname{TV}(K_tp,K_tq)
\le
\operatorname{TV}(p,q).
}
\]

Hence

\[
\boxed{
\operatorname{TV}(p,q)
\ge
\operatorname{TV}(K_tp,K_tq).
}
\]

A measured target separation is therefore a lower bound on the latent separation under the declared shared channel.

### Target-channel stability coefficient

Define the zero-sum subspace

\[
\mathcal H
=
\{v\in\mathbb R^{|\mathcal E|}:\mathbf1^\top v=0\}
\]

and

\[
\boxed{
\gamma_t
=
\inf_{\substack{v\in\mathcal H\\v\ne0}}
\frac{\|K_tv\|_1}{\|v\|_1}.
}
\]

Then \(0\le\gamma_t\le1\), and for every pair of latent target laws,

\[
\boxed{
\gamma_t\operatorname{TV}(p,q)
\le
\operatorname{TV}(K_tp,K_tq)
\le
\operatorname{TV}(p,q).
}
\]

In finite dimension,

\[
\boxed{
\gamma_t>0
\iff
\ker K_t\cap\mathcal H=\{0\}.
}
\]

If the channel is injective on zero-sum target-distribution differences, the continuous function \(v\mapsto\|K_tv\|_1\) has a strictly positive minimum on the compact unit \(L^1\) sphere in \(\mathcal H\). Conversely, a nonzero zero-sum vector in the kernel makes the infimum zero. Full column rank is sufficient, but injectivity on \(\mathcal H\) is the exact condition required here.

The coefficient is conditional on a known or justified channel. P72 does not infer an unknown general \(K_t\) from one noisy label stream.

---

## 7. Exact binary symmetric channel

For

\[
Y=E^\star\oplus N,
\qquad
N\sim\operatorname{Bernoulli}(\eta),
\]

let two latent Bernoulli targets have parameters \(p\) and \(q\). Since

\[
P(Y=1)=\eta+(1-2\eta)p,
\]

we obtain

\[
\boxed{
\operatorname{TV}_Y
=|1-2\eta|\operatorname{TV}_{E^\star}.
}
\]

Thus the exact binary stability factor is

\[
\boxed{\gamma=|1-2\eta|.}
\]

| Error rate \(\eta\) | Stability \(\gamma\) | Interpretation |
| ---: | ---: | --- |
| 0 | 1 | perfect target measurement |
| 0.10 | 0.80 | 80 percent of every binary TV witness survives |
| 0.25 | 0.50 | half of the latent TV separation survives |
| 0.50 | 0 | complete erasure |

For \(\eta>1/2\), a known symmetric channel becomes informative again because labels are systematically reversed rather than erased. The singular point is \(\eta=1/2\).

---

## 8. P72D: finite-sample lower confidence bound

Consider two same-\(T\) cases \(a,b\), with observed target \(Y\) on a predeclared alphabet of size \(d_Y\). Collect independent IID measurements of sizes \(n_a,n_b\), with empirical laws \(\widehat P_a,\widehat P_b\).

Coordinate-wise Hoeffding plus a union bound across both samples and all declared categories gives

\[
\boxed{
a_s
=\sqrt{\frac{1}{2n_s}\log\frac{4d_Y}{\alpha}},
\qquad
\tau_s
=\min\left\{1,\frac{d_Y}{2}a_s\right\},
\quad s\in\{a,b\}.
}
\]

With probability at least \(1-\alpha\), both

\[
\operatorname{TV}(P_s,\widehat P_s)\le\tau_s.
\]

The triangle inequality then yields

\[
\left|
\operatorname{TV}(P_a,P_b)
-
\operatorname{TV}(\widehat P_a,\widehat P_b)
\right|
\le\tau_a+\tau_b.
\]

Therefore

\[
\boxed{
L_Y
=
\max\left\{0,
\operatorname{TV}(\widehat P_a,\widehat P_b)-\tau_a-\tau_b
\right\}
}
\]

satisfies

\[
\Pr\left(\operatorname{TV}(P_a,P_b)\ge L_Y\right)\ge1-\alpha.
\]

By target-channel contraction, on the same event,

\[
\boxed{
\operatorname{TV}(P_{E^\star,a},P_{E^\star,b})
\ge
\operatorname{TV}(P_{Y,a},P_{Y,b})
\ge L_Y.
}
\]

A positive \(L_Y\), together with equal declared physical descriptor and a valid shared P72 channel, therefore certifies a latent target distinction behind the noisy observation process.

---

## 9. P72E: sufficient sample size under channel stability

Suppose the planned experiment assumes

\[
\operatorname{TV}(p,q)\ge\Delta_E>0,
\qquad
\gamma_t\ge\gamma_0>0.
\]

Then the population observed separation obeys

\[
D_Y\ge\gamma_0\Delta_E.
\]

For equal sample sizes \(n_a=n_b=n\), let

\[
\tau_n
=\frac{d_Y}{2}
\sqrt{\frac{1}{2n}\log\frac{4d_Y}{\alpha}}
\]

in the nontrivial uncapped regime. On the simultaneous confidence event,

\[
\widehat D_Y\ge D_Y-2\tau_n,
\]

so

\[
L_Y\ge\max\{0,\gamma_0\Delta_E-4\tau_n\}.
\]

Thus

\[
4\tau_n<\gamma_0\Delta_E
\]

is sufficient for a positive lower bound. Solving gives

\[
\boxed{
n>
\frac{2d_Y^2\log(4d_Y/\alpha)}
{\gamma_0^2\Delta_E^2}.
}
\]

This is a conservative sufficient design condition, not a minimax-optimal or necessary sample complexity.

For the binary symmetric channel, \(\gamma_0=|1-2\eta|\), so the target-measurement penalty scales as

\[
\boxed{(1-2\eta)^{-2}}
\]

away from \(\eta=1/2\).

---

## 10. Dependency and scientific role

P72 connects four established layers:

- [P17](proposition_17_coarse_graining_and_refinement.md): stochastic-map contraction and loss of distinguishability;
- [P19](proposition_19_fundamental_physical_sufficiency.md): the latent physical-sufficiency residual;
- [P20](proposition_20_finite_sample_residual_certification.md): finite-data discipline for bridge residuals;
- [P71](proposition_71_target_provenance_noncircularity.md): independent target provenance.

The target-side logical sequence is

\[
\boxed{
\text{independent target provenance}
\xrightarrow{\mathrm{P71}}
\text{declared target-measurement channel}
\xrightarrow{\mathrm{P72}}
\text{measurement-aware bridge witness}.
}
\]

P72 assumes that provenance hurdle has been addressed. It does not replace P71.

---

## 11. Channel identifiability remains separate

P72 conditions on a declared target-measurement channel or on a defensible lower bound for its stability. It does not claim that such a channel can always be inferred from noisy observations.

This is a recognized identifiability problem in noisy-label and repeated-observer models. Liu, Cheng, and Zhang, *Identifiability of Label Noise Transition Matrix*, ICML 2023, study conditions under which transition matrices are identifiable and emphasize the difficulty of instance-dependent noise without additional information or assumptions. Dawid and Skene's classical repeated-observer model estimates observer error rates when a latent response is unavailable.

These works are methodological context, not premises for the P72 proof. Their role points to a natural next theorem: identify conditions under which the target channel, or at least a certified lower bound on \(\gamma_t\), can itself be recovered from repeated or multi-view measurements.

---

## 12. Numerical implementation and tests

The implementation is [`target_measurement_channel_robustness.py`](../src/consciousness_bridge/target_measurement_channel_robustness.py).

It computes the latent and observed conditional residuals under a declared channel, verifies the data-processing inequality, pushes finite target distributions through channels, checks TV contraction, evaluates exact binary-symmetric attenuation, constructs the finite-sample TV lower bound, and returns the sufficient equal-sample-size design threshold.

The regression suite is [`test_target_measurement_channel_robustness.py`](../tests/test_target_measurement_channel_robustness.py). It checks perfect measurement, noisy attenuation, complete erasure, zero-latent-residual preservation, exact binary attenuation, finite confidence arithmetic, sample-size scaling, and malformed-input rejection.

These tests validate the executable theorem contract. They are not empirical evidence about consciousness.

---

## 13. Scientific boundary

P72 establishes a measurement theorem, not an ontology.

It does **not** prove that \(E^\star\) is consciousness. It does not prove that self-report is infallible, that behavior is experiential ground truth, or that any clinical or neural label is privileged. It does not prove that the target channel is known. It does not establish that the physical descriptor \(T\) is complete. It does not imply that a surviving residual is nonphysical.

Its contribution is narrower:

\[
\boxed{
\text{under a declared nondifferential target channel,}
\quad
\text{measurement can attenuate a bridge witness but cannot create the population residual from nothing.}
}
\]

A positive measurement-aware witness can therefore transfer to the latent target under the theorem assumptions. A null observed witness remains inconclusive unless the target channel is sufficiently informative and scientifically justified.
