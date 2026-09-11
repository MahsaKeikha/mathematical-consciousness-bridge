# Proposition 72: target-measurement channel robustness and noisy-witness transfer

**Status:** proved mathematical measurement-robustness theorem under a declared nondifferential target-observation channel, with a conservative finite-sample certificate.

## 1. Purpose

P71 establishes a logically prior requirement for a meaningful bridge test: the target must not be constructed from the same physical descriptor in a way that makes factorization true by definition.

That still leaves a second problem. An independently justified target may not be observed directly. Reports, behavioral responses, ratings, clinical labels, or other target-side measurements can be noisy.

P72 asks:

> If an independently declared latent target is observed through a noisy measurement channel, what conclusions about physical sufficiency survive the measurement process?

The answer is asymmetric.

Under an explicit nondifferential measurement condition, target-side noise cannot create population-level residual target information that was absent from the latent target. It can, however, attenuate or completely erase a genuine latent residual.

P72 formalizes that asymmetry with conditional mutual information and total variation, then gives a finite-sample lower confidence bound for a measured target separation.

The theorem does not declare the latent target to be consciousness. The notation \(E^\star\) means only the independently declared latent target variable that the experimental protocol claims to measure.

---

## 2. Setup

Let

\[
\Omega
\]

be the underlying admissible state or history variable, let

\[
T=T(\Omega)
\]

be the declared physical descriptor, and let

\[
E^\star
\]

be an independently specified latent target satisfying the P71 provenance requirement.

The experiment does not necessarily observe \(E^\star\) directly. Instead it observes

\[
Y
\]

through a target-measurement channel.

P72 assumes the channel is **nondifferential relative to the underlying state once the latent target and physical descriptor are fixed**:

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

The channel is allowed to depend on \(T\). This permits measurement quality or reporting noise to vary across declared physical conditions. What is excluded is additional dependence on \(\Omega\) after \((E^\star,T)\) have already been fixed.

That exclusion is scientifically consequential. If it fails, the measurement process itself can carry extra state information and can manufacture an apparent observed residual.

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

Condition on a fixed value \(T=t\) with positive probability. The P72 measurement premise gives the conditional Markov chain

\[
\Omega
\longrightarrow
E^\star
\longrightarrow
Y
\qquad\text{given }T=t.
\]

The ordinary data-processing inequality therefore gives

\[
I(Y;\Omega\mid T=t)
\le
I(E^\star;\Omega\mid T=t).
\]

Average over \(t\):

\[
\begin{aligned}
I(Y;\Omega\mid T)
&=
\sum_t P(t)I(Y;\Omega\mid T=t)\\
&\le
\sum_t P(t)I(E^\star;\Omega\mid T=t)\\
&=
I(E^\star;\Omega\mid T).
\end{aligned}
\]

Hence

\[
\boxed{
I(Y;\Omega\mid T)
\le
I(E^\star;\Omega\mid T).
}
\]

\(\square\)

The information-theoretic data-processing step is standard. P72's contribution is its explicit placement in the target-measurement layer of the repository's physical-sufficiency program.

See [Cover and Thomas](foundational_physics_mathematics_bibliography.md#cover-and-thomas-2006) for standard information theory and [P19](proposition_19_fundamental_physical_sufficiency.md) for the bridge residual used here.

---

## 4. P72A corollary: population no-false-positive transfer

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

Therefore, under the P72 measurement premise, a genuine positive **population** residual in the observed target cannot have been created solely by nondifferential target-measurement noise.

It transfers upward to a positive latent-target residual.

This is a statement about population quantities. A positive empirical estimate is not enough. Finite-sample uncertainty must still be controlled, as in P20 and the P72D certificate below.

The scientific conclusion is also descriptor-relative:

\[
I(E^\star;\Omega\mid T)>0
\]

means that the declared \(T\) does not screen off the declared latent target under the declared model. It does not show that physics in general is incomplete.

---

## 5. P72B: the converse fails because target noise can erase a real residual

The implication

\[
I(Y;\Omega\mid T)=0
\Longrightarrow
I(E^\star;\Omega\mid T)=0
\]

is false in general.

### Exact erasure counterexample

Let \(T\) be constant, let

\[
\Omega\sim\operatorname{Bernoulli}(1/2),
\]

and define

\[
E^\star=\Omega.
\]

Then

\[
I(E^\star;\Omega\mid T)
=H(\Omega)
=\log 2.
\]

Now let the measurement channel erase the target completely:

\[
Y=y_0
\qquad\text{with probability }1.
\]

This channel satisfies the P72 conditional-independence premise because it contains no additional dependence on \(\Omega\). Yet

\[
I(Y;\Omega\mid T)=0.
\]

Thus

\[
\boxed{
I(E^\star;\Omega\mid T)=\log2,
\qquad
I(Y;\Omega\mid T)=0.
}
\]

A zero observed residual is therefore inconclusive unless the target-measurement channel is known to preserve the distinctions relevant to the bridge test.

---

## 6. Why the measurement premise matters

P72 does not claim that every real reporting or measurement process satisfies

\[
Y\perp\!\!\!\perp\Omega\mid(E^\star,T).
\]

If the measurement process retains extra dependence on the underlying state, a false observed residual can be created.

For example, let \(T\) be constant and let \(E^\star\) also be constant, so

\[
I(E^\star;\Omega\mid T)=0.
\]

If an invalid measurement mechanism directly sets

\[
Y=\Omega,
\]

then

\[
I(Y;\Omega\mid T)=H(\Omega)>0.
\]

The apparent residual now comes from the measurement mechanism, not from the latent target.

This is why P72 treats target measurement as part of the scientific model rather than as a transparent readout.

---

## 7. P72C: total-variation contraction for target witnesses

Conditional mutual information is useful for a global stochastic residual. Pairwise witness experiments often use a direct target-distribution separation.

Fix a physical descriptor value \(T=t\). Let two underlying cases have latent target laws

\[
p,q\in\Delta(\mathcal E),
\]

and let the shared target-measurement channel at this descriptor value be

\[
K_t(y\mid e).
\]

Their observed target laws are

\[
K_tp,
\qquad
K_tq.
\]

Every stochastic channel contracts total variation, so

\[
\boxed{
\operatorname{TV}(K_tp,K_tq)
\le
\operatorname{TV}(p,q).
}
\]

Therefore a measured target separation is itself a lower bound on the corresponding latent target separation:

\[
\boxed{
\operatorname{TV}(p,q)
\ge
\operatorname{TV}(K_tp,K_tq).
}
\]

This is the target-side analogue of the data-processing logic used elsewhere in the repository, including P17.

---

## 8. Target-channel stability coefficient

Contraction gives only an upper bound on what survives measurement. To quantify how much latent separation is guaranteed to remain visible, define the zero-mass subspace

\[
\mathcal H
=
\left\{
v\in\mathbb R^{|\mathcal E|}:
\mathbf 1^\top v=0
\right\}.
\]

For a finite channel matrix \(K_t\), define

\[
\boxed{
\gamma_t
=
\inf_{\substack{v\in\mathcal H\\v\ne0}}
\frac{\|K_tv\|_1}{\|v\|_1}.
}
\]

Because stochastic channels contract \(L^1\) differences of probability vectors,

\[
0\le\gamma_t\le1.
\]

For any two latent probability laws \(p,q\), their difference belongs to \(\mathcal H\), and therefore

\[
\|K_t(p-q)\|_1
\ge
\gamma_t\|p-q\|_1.
\]

Dividing by two gives the two-sided witness transfer bound

\[
\boxed{
\gamma_t\operatorname{TV}(p,q)
\le
\operatorname{TV}(K_tp,K_tq)
\le
\operatorname{TV}(p,q).
}
\]

### When is \(\gamma_t>0\)?

In finite dimension,

\[
\boxed{
\gamma_t>0
\iff
\ker K_t\cap\mathcal H=\{0\}.
}
\]

If the restricted channel is injective on target-distribution differences, the continuous function

\[
v\mapsto\|K_tv\|_1
\]

has a strictly positive minimum on the compact set

\[
\{v\in\mathcal H:\|v\|_1=1\}.
\]

Conversely, if a nonzero zero-sum vector lies in the channel kernel, then its ratio is zero and \(\gamma_t=0\).

Full column rank of \(K_t\) is sufficient for \(\gamma_t>0\), but the exact condition needed here is only injectivity on the zero-sum difference subspace.

This coefficient does not establish that the target channel is known. Estimating or identifying an unknown target-noise channel is a separate scientific problem.

---

## 9. Binary symmetric target measurement

For a binary latent target, consider

\[
Y=E^\star\oplus N,
\qquad
N\sim\operatorname{Bernoulli}(\eta),
\]

with \(N\) conditionally independent of the underlying state under the P72 premise.

If two latent target laws are Bernoulli with parameters \(p\) and \(q\), then

\[
P(Y=1)=\eta+(1-2\eta)p.
\]

Therefore

\[
\begin{aligned}
\operatorname{TV}(P_Y^{(p)},P_Y^{(q)})
&=
|\eta+(1-2\eta)p-\eta-(1-2\eta)q|\\
&=
|1-2\eta|\,|p-q|.
\end{aligned}
\]

Since total variation between Bernoulli laws is \(|p-q|\),

\[
\boxed{
\operatorname{TV}_Y
=|1-2\eta|\operatorname{TV}_{E^\star}.
}
\]

Hence the exact binary stability factor is

\[
\boxed{
\gamma=|1-2\eta|.
}
\]

Important regimes are:

| Error rate \(\eta\) | Stability \(\gamma\) | Interpretation |
| ---: | ---: | --- |
| 0 | 1 | perfect target measurement |
| 0.10 | 0.80 | 80 percent of every binary TV witness survives |
| 0.25 | 0.50 | half of the latent TV separation survives |
| 0.50 | 0 | complete erasure |

The symmetric channel becomes informative again for \(\eta>1/2\) if the reversal rate is known, because the labels are systematically flipped rather than erased. The singular point is \(\eta=1/2\).

---

## 10. P72D: finite-sample lower confidence bound for observed target separation

Consider two cases \(a,b\) with the same declared physical descriptor value \(T=t\). Suppose the observed target \(Y\) has a predeclared finite alphabet of size

\[
d_Y.
\]

Collect independent IID target measurements within each case:

\[
Y_{a,1},\ldots,Y_{a,n_a},
\qquad
Y_{b,1},\ldots,Y_{b,n_b}.
\]

Let the empirical target laws be

\[
\widehat P_a,
\qquad
\widehat P_b.
\]

Allocate total error probability \(\alpha\) across both samples and all \(d_Y\) categories. Coordinate-wise Hoeffding plus a union bound gives

\[
\boxed{
a_s
=
\sqrt{
\frac{1}{2n_s}
\log\frac{4d_Y}{\alpha}
},
\qquad s\in\{a,b\}.
}
\]

Then, simultaneously for both samples with probability at least \(1-\alpha\),

\[
\operatorname{TV}(P_s,\widehat P_s)
\le
\tau_s,
\qquad
\boxed{
\tau_s
=
\min\left\{1,\frac{d_Y}{2}a_s\right\}.
}
\]

By the triangle inequality,

\[
\left|
\operatorname{TV}(P_a,P_b)
-
\operatorname{TV}(\widehat P_a,\widehat P_b)
\right|
\le
\tau_a+\tau_b.
\]

Therefore

\[
\boxed{
L_Y
=
\max\left\{
0,
\operatorname{TV}(\widehat P_a,\widehat P_b)
-\tau_a-\tau_b
\right\}
}
\]

satisfies

\[
\boxed{
P\left(
\operatorname{TV}(P_a,P_b)\ge L_Y
\right)
\ge1-\alpha.
}
\]

Because the target channel contracts total variation,

\[
\operatorname{TV}(P_{E^\star,a},P_{E^\star,b})
\ge
\operatorname{TV}(P_a,P_b),
\]

so on the same confidence event,

\[
\boxed{
\operatorname{TV}(P_{E^\star,a},P_{E^\star,b})
\ge L_Y.
}
\]

Thus a strictly positive \(L_Y\), together with equal declared physical descriptor and a valid P72 channel premise, certifies that a latent target distinction survives behind the noisy observation process.

This is a finite-data target-side witness. It does not by itself establish that the declared \(T\) is physically complete.

---

## 11. P72E: sufficient sample size under a known channel-stability lower bound

Suppose a planned experiment assumes a latent target separation

\[
\operatorname{TV}(p,q)\ge\Delta_E>0
\]

and a known channel-stability lower bound

\[
\gamma_t\ge\gamma_0>0.
\]

Then

\[
D_Y
:=
\operatorname{TV}(K_tp,K_tq)
\ge
\gamma_0\Delta_E.
\]

For equal sample sizes \(n_a=n_b=n\), define

\[
\tau_n
=
\frac{d_Y}{2}
\sqrt{
\frac{1}{2n}
\log\frac{4d_Y}{\alpha}
}
\]

in the nontrivial regime before the cap at one is active.

On the simultaneous confidence event,

\[
\widehat D_Y
\ge
D_Y-2\tau_n.
\]

The P72D lower bound therefore obeys

\[
L_Y
=
\max\{0,\widehat D_Y-2\tau_n\}
\ge
\max\{0,\gamma_0\Delta_E-4\tau_n\}.
\]

Hence the strict condition

\[
4\tau_n<\gamma_0\Delta_E
\]

is sufficient for \(L_Y>0\) on the confidence event.

Solving for \(n\) gives

\[
\boxed{
n
>
\frac{
2d_Y^2\log(4d_Y/\alpha)
}{
\gamma_0^2\Delta_E^2
}.
}
\]

The integer implementation returns the smallest integer strictly above the right-hand side.

This is a conservative sufficient design bound. It is not claimed to be minimax-optimal or necessary.

The scaling is nevertheless scientifically informative:

\[
\boxed{
n
=O\!\left(
\frac{1}{\gamma_0^2\Delta_E^2}
\log\frac{d_Y}{\alpha}
\right)
}
\]

up to the explicit alphabet-size prefactor generated by the coordinate-wise union bound.

As the measurement channel approaches erasure,

\[
\gamma_0\to0,
\]

the sufficient sample burden diverges.

For the binary symmetric channel,

\[
\gamma_0=|1-2\eta|,
\]

so the measurement-noise penalty scales as

\[
\boxed{
\frac{1}{(1-2\eta)^2}
}
\]

away from the singular point \(\eta=1/2\).

---

## 12. Relation to P17, P19, P20, and P71

P72 is a target-side branch assembled from earlier mathematical obligations.

### P17

P17 uses stochastic-map contraction to quantify what physical distinctions can be lost under coarse observation. P72 applies the same data-processing discipline to the target measurement channel.

### P19

P19 supplies the latent physical-sufficiency residual

\[
I(E^\star;\Omega\mid T).
\]

P72 proves how an observed target residual

\[
I(Y;\Omega\mid T)
\]

relates to it under an explicit measurement model.

### P20

P20 shows why a population residual must not be replaced by an unqualified empirical estimate. P72D applies the same finite-data philosophy to pairwise observed target separations.

### P71

P71 asks whether the target was specified independently enough for a bridge test to have evidential content. P72 assumes that provenance hurdle has been addressed and asks whether the measurement process preserves or hides the independently declared target distinctions.

The logical sequence is therefore

\[
\boxed{
\text{independent target provenance}
\xrightarrow{\text{P71}}
\text{declared target-measurement channel}
\xrightarrow{\text{P72}}
\text{measurement-aware bridge witness}.
}
\]

---

## 13. Target-channel identifiability is a separate obligation

P72 conditions on a declared target-measurement channel or on a defensible lower bound for its stability.

It does not claim that such a channel can always be inferred from one noisy label stream.

This is a recognized identifiability problem in noisy-label and repeated-observer models. For example, Liu, Cheng, and Zhang (ICML 2023) analyze when a label-noise transition matrix is identifiable and show that instance-dependent transition identification can require multiple noisy labels or additional structural assumptions. Earlier repeated-observer work by Dawid and Skene models observer error rates when the latent response is unavailable.

Those works provide methodological context, not premises for P72's data-processing proof.

External context:

- Yang Liu, Hao Cheng, and Kun Zhang, "Identifiability of Label Noise Transition Matrix," *Proceedings of the 40th International Conference on Machine Learning*, PMLR 202, 2023, 21475-21496. https://proceedings.mlr.press/v202/liu23g.html
- A. P. Dawid and A. M. Skene, "Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm," *Journal of the Royal Statistical Society: Series C*, 28(1), 1979, 20-28. DOI: 10.2307/2346806.

A natural next theorem is therefore to ask under what repeated-rater, multi-view, calibration, or structural assumptions the target channel itself is identifiable well enough to support P72's stability parameter.

---

## 14. Numerical implementation

The reference implementation is

[`target_measurement_channel_robustness.py`](../src/consciousness_bridge/target_measurement_channel_robustness.py).

It provides:

- construction and verification of the conditional residual inequality under a declared finite target channel;
- exact total-variation pushforward and contraction checks;
- exact binary-symmetric target-channel attenuation;
- a conservative finite-sample lower confidence bound for observed target separation;
- a sufficient equal-sample-size design bound under a declared latent TV gap and channel-stability lower bound.

The implementation intentionally does not infer conceptual target independence from data and does not estimate an unknown general channel-stability coefficient without an identifiability model.

---

## 15. Regression tests

The P72 regression suite checks:

1. equality of latent and observed residuals under perfect measurement;
2. strict residual attenuation under a noisy informative channel;
3. complete erasure of an otherwise positive latent residual;
4. impossibility of creating a population residual from a zero latent residual under the declared nondifferential channel;
5. exact total-variation contraction through a finite target channel;
6. exact binary-symmetric attenuation by \(|1-2\eta|\);
7. complete binary witness erasure at \(\eta=1/2\);
8. finite-sample target-TV lower-bound arithmetic;
9. the derived sufficient sample-size inequality;
10. increasing sample burden as channel stability decreases; and
11. rejection of malformed channels, post-hoc alphabet mismatch, zero stability, and zero declared gap.

These tests validate the executable theorem contract. They are not empirical evidence about consciousness.

---

## 16. Scientific boundary

P72 establishes a measurement theorem, not an ontology.

It does **not** prove that \(E^\star\) is consciousness. It does not prove that self-report is infallible, that behavior is an experiential ground truth, or that any clinical or neural label is privileged. It does not prove that the target channel is known. It does not establish that the physical descriptor \(T\) is complete. It does not imply that a surviving residual is nonphysical.

Its contribution is narrower:

\[
\boxed{
\text{under a declared nondifferential target channel,}
\quad
\text{measurement can attenuate a bridge witness but cannot create the population residual from nothing.}
}
\]

A positive measurement-aware witness can therefore be transferred to the latent target under the theorem's assumptions. A null observed witness remains inconclusive unless the target channel is sufficiently informative and scientifically justified.
