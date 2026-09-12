# Proposition 81: Projection-Event Certificate for Continuous P75 Separation

## Status

**Proved conditional computational theorem.** P81 strengthens the continuous-family lower-bound chain developed in [P78](proposition_78_certified_continuous_model_separation.md) and [P80](proposition_80_simplex_coupled_model_separation.md) for the same declared [P75](proposition_75_target_model_adequacy_overidentification.md) four-view binary latent family and the same $L_\infty$ observed-law metric.

P80 retains probability normalization inside each exact P78 cell box. P81 retains an additional class of constraints: **exact parameter-box ranges for every nonempty projected binary event**. These event constraints are implied by the same P75 parameter box, require no new latent assumptions, and yield an exact-rational lower bound that can be strictly stronger than P80.

P81 is a **model-distance certification improvement**. It does not identify a latent variable with consciousness, does not validate conditional independence, and does not close the physical-to-experiential bridge.

---

## 1. Motivation

For a P78 parameter box $B\subset[0,1]^9$, P80 uses the exact cell intervals

\[
\ell_x(B)\le q_x(\theta)\le u_x(B),
\qquad x\in\{0,1\}^4,
\]

and the normalization identity

\[
\sum_x q_x(\theta)=1.
\]

That is already tighter than treating the sixteen intervals independently. But a P75 law also obeys many exact constraints after some observed coordinates are marginalized out.

For example, a box may force the first observed view to satisfy

\[
\Pr(X_1=1)=\frac35
\]

for every parameter vector in the box even while every individual sixteen-cell interval is wide enough to contain the corresponding empirical cell. In that situation, the P80 interval-simplex relaxation may still contain the empirical law, whereas the forced one-view marginal already proves positive distance from every P75 law in the box.

P81 formalizes that observation for **all nonempty cylinder events** of the four observed views.

---

## 2. Cylinder events

Let

\[
\mathcal X=\{0,1\}^4
\]

be the sixteen-cell observed state space. Choose a nonempty coordinate subset

\[
J\subseteq\{1,2,3,4\}
\]

and an assignment

\[
a\in\{0,1\}^{|J|}.
\]

Define the cylinder event

\[
\boxed{
C(J,a)
=
\{x\in\mathcal X:x_j=a_j\text{ for every }j\in J\}.
}
\]

Its number of full observed cells is

\[
\boxed{
|C(J,a)|=2^{4-|J|}.
}
\]

For an empirical law $\widehat p$, define the empirical event probability

\[
\widehat m_{J,a}
=
\sum_{x\in C(J,a)}\widehat p_x.
\]

---

## 3. Exact P75 projection interval on a parameter box

Write the P75 parameters as

\[
\theta=
(\pi,q_{1,-},q_{1,+},\ldots,q_{4,-},q_{4,+}),
\]

where $\pi=\Pr(S=+)$ and $q_{j,s}=\Pr(X_j=1\mid S=s)$.

For a fixed cylinder event $C(J,a)$, marginalizing the unselected views gives

\[
\boxed{
m_{J,a}(\theta)
=
(1-\pi)
\prod_{j\in J} f(q_{j,-},a_j)
+
\pi
\prod_{j\in J} f(q_{j,+},a_j),
}
\]

with

\[
f(q,1)=q,
\qquad
f(q,0)=1-q.
\]

Each selected factor is monotone on its parameter interval. Therefore each latent-state product reaches its exact minimum and maximum at parameter-box endpoints. Once those product extrema are fixed, the remaining dependence on $\pi$ is affine and is extremized at a prevalence endpoint.

Hence every cylinder event has an **exact rational box range**

\[
\boxed{
\ell_{J,a}(B)
\le
m_{J,a}(\theta)
\le
u_{J,a}(B)
\qquad
\forall\theta\in B.
}
\]

No numerical optimizer is required.

---

## 4. Event-mass Lipschitz inequality

Let $q$ be any sixteen-cell probability law. If

\[
\|\widehat p-q\|_\infty\le r,
\]

then for every cylinder event,

\[
\begin{aligned}
\left|
\widehat m_{J,a}-q(C(J,a))
\right|
&=
\left|
\sum_{x\in C(J,a)}(\widehat p_x-q_x)
\right|\\
&\le
\sum_{x\in C(J,a)}
|\widehat p_x-q_x|\\
&\le
|C(J,a)|\,r.
\end{aligned}
\]

Therefore, if the P75 event probability is restricted to
$[\ell_{J,a}(B),\nu_{J,a}(B)]$, every model law generated in $B$ must satisfy

\[
\boxed{
\|\widehat p-q(\theta)\|_\infty
\ge
\frac{
d\!\left(
\widehat m_{J,a},
[\ell_{J,a}(B),\nu_{J,a}(B)]
\right)
}{2^{4-|J|}}.
}
\]

This is the key P81 lower-bound transfer from a projected event back to the complete sixteen-cell law.

---

## 5. P81 projection lower bound

Define

\[
\boxed{
L_{\mathrm{proj}}(B)
=
\max_{\emptyset\ne J\subseteq\{1,2,3,4\}}
\max_{a\in\{0,1\}^{|J|}}
\frac{
d\!\left(
\widehat m_{J,a},
[\ell_{J,a}(B),\nu_{J,a}(B)]
\right)
}{2^{4-|J|}}.
}
\]

There are only

\[
\sum_{k=1}^4 {4\choose k}2^k
=3^4-1
=80
\]

such nonempty cylinder events, so the complete projection audit is finite and small.

For $|J|=4$, every cylinder contains one observed cell. Therefore the P78 cellwise family is included exactly, which gives

\[
\boxed{
L_{\mathrm{proj}}(B)
\ge
L_{78}(B).
}
\]

---

## 6. Theorem

For every admissible P78 parameter box $B$, define

\[
\boxed{
L_{81}(B)
=
\max\{L_{80}(B),L_{\mathrm{proj}}(B)\}.
}
\]

Then:

1. $L_{81}(B)$ is a rigorous lower bound on the distance from $\widehat p$ to the true P75 model image generated inside $B$;
2. $L_{81}(B)\ge L_{80}(B)\ge L_{78}(B)$;
3. $L_{\mathrm{proj}}(B)$ and $L_{81}(B)$ are exactly computable in rational arithmetic from the empirical count law and rational parameter-box endpoints;
4. for every finite partition $\mathcal B$ of the complete P75 parameter cube,

\[
\boxed{
L_{81}(\mathcal B)
:=
\min_{B\in\mathcal B}L_{81}(B)
\le
d_\infty(\widehat p,\mathcal M_{4,2});
}
\]

5. on the same active partition,

\[
\boxed{
L_{81}(\mathcal B)
\ge
L_{80}(\mathcal B);
}
\]

6. explicit admissible P75 parameter points remain valid upper-bound witnesses, and the established P78 mesh-width upper certificate remains valid without assuming a new convergence rate for P81.

---

## 7. Proof

### 7.1 Exact projection ranges

The P75 conditional-independence parameterization gives

\[
q_x(\theta)
=
(1-\pi)
\prod_{j=1}^4
f(q_{j,-},x_j)
+
\pi
\prod_{j=1}^4
f(q_{j,+},x_j).
\]

Summing over all coordinates outside $J$ replaces each omitted Bernoulli factor by

\[
q+(1-q)=1.
\]

Thus the cylinder probability reduces exactly to the formula in Section 3. Endpoint monotonicity of every selected Bernoulli factor, followed by affine extremization in $\pi$, gives the stated exact box interval.

### 7.2 Projection-to-full-law lower bound

For any $\theta\in B$, the model event probability belongs to the exact interval. The event-mass Lipschitz inequality therefore implies

\[
\|\widehat p-q(\theta)\|_\infty
\ge
\frac{
d(\widehat m_{J,a},[\ell_{J,a},\nu_{J,a}])
}{|C(J,a)|}
\]

for every cylinder event. Maximizing over the finite event family preserves validity, so

\[
L_{\mathrm{proj}}(B)
\le
\inf_{\theta\in B}
\|\widehat p-q(\theta)\|_\infty.
\]

### 7.3 Combination with P80

P80 already satisfies

\[
L_{80}(B)
\le
\inf_{\theta\in B}
\|\widehat p-q(\theta)\|_\infty.
\]

The maximum of two valid lower bounds remains a valid lower bound. Hence

\[
L_{81}(B)
=
\max\{L_{80}(B),L_{\mathrm{proj}}(B)\}
\]

is sound and automatically dominates P80.

### 7.4 P78 is embedded in the projection family

If $J$ contains all four views, $C(J,a)$ contains exactly one cell. Its event interval is precisely the corresponding P78 cell interval and its denominator is one. Maximizing over those full assignments recovers the P78 lower bound. Therefore

\[
L_{\mathrm{proj}}(B)\ge L_{78}(B).
\]

### 7.5 Global branch-and-bound certificate

For a finite active partition $\mathcal B$,

\[
\mathcal M_{4,2}
=
\bigcup_{B\in\mathcal B}\mathcal M(B).
\]

Taking the minimum sound box lower bound gives

\[
\min_{B\in\mathcal B}L_{81}(B)
\le
d_\infty(\widehat p,\mathcal M_{4,2}).
\]

The implementation refines the active box with the smallest P81 lower bound. Any evaluated box center is a valid P75 parameter vector and hence an upper-bound witness. For a conservative finite refinement certificate, the implementation retains each box's original P78 lower bound and applies the already-established P78 mesh-width upper certificate. Thus P81 strengthens lower-bound search without silently assuming a new P81 convergence theorem.

This proves the proposition. $\square$

---

## 8. Strict-improvement witness: P80 zero, P81 positive

The following exact example shows that the new information is not redundant with simplex normalization.

Fix a parameter box with

\[
\pi=\frac12,
\qquad
q_{1,-}=q_{1,+}=\frac35,
\]

while all six conditional probabilities for views $2,3,4$ range freely over $[0,1]$.

Let the empirical sixteen-cell law be uniform:

\[
\widehat p_x=\frac1{16}
\qquad\forall x\in\{0,1\}^4.
\]

Every empirical cell lies inside its P78 box interval and the empirical vector is normalized. Consequently

\[
\boxed{L_{80}(B)=0.}
\]

But every P75 law in the box satisfies

\[
\Pr(X_1=0)=\frac25,
\]

whereas the empirical marginal is

\[
\widehat\Pr(X_1=0)=\frac12.
\]

The event $X_1=0$ contains eight full cells. Hence

\[
L_{\mathrm{proj}}(B)
\ge
\frac{|1/2-2/5|}{8}
=
\frac{1/10}{8}
=
\boxed{\frac1{80}}.
\]

The exact implementation confirms that this is the strongest projection witness for the example, so

\[
\boxed{
L_{81}(B)=\frac1{80}>0=L_{80}(B).
}
\]

This is an algebraic strict-improvement witness. It is not an empirical consciousness result.

---

## 9. P77/P79 rejection handoff

Let $\overline\varepsilon_{79}$ be the [P79](proposition_79_certified_sampling_radius.md) certified upper envelope for the P77 finite-alphabet sampling radius. Then

\[
\boxed{
L_{81}(\mathcal B)>\overline\varepsilon_{79}
\Longrightarrow
 d_\infty(\widehat p,\mathcal M_{4,2})
>
\varepsilon_{n,K}(\alpha).
}
\]

This preserves the one-sided certification direction: P81 contributes a rigorous **lower** bound on model distance, while P79 contributes a rigorous **upper** bound on sampling uncertainty.

Failure of the strict inequality is inconclusive. It is not evidence that the P75 model is correct.

---

## 10. What P81 adds and what it does not add

P81 adds exact projected-event information that P80's interval-simplex relaxation does not necessarily preserve. It can therefore eliminate probability vectors that satisfy all individual cell intervals and normalization but violate a marginal or higher-order projected event forced by the underlying parameter box.

P81 does **not**:

- change the P75 latent model;
- validate conditional independence;
- identify the latent state with consciousness;
- establish that consciousness is a scalar, a quantum variable, or an additional dimension;
- turn non-rejection into model acceptance;
- prove that a failed P75 model implies physics is incomplete.

The physical-to-experiential bridge remains open.

---

## 11. Reproducibility map

| Research object | Direct route |
| --- | --- |
| P81 implementation | [`src/consciousness_bridge/projection_event_model_separation.py`](../src/consciousness_bridge/projection_event_model_separation.py) |
| P81 unit and certificate tests | [`tests/test_projection_event_model_separation.py`](../tests/test_projection_event_model_separation.py) |
| P81 equation and provenance record | [`docs/p81_equation_provenance.md`](p81_equation_provenance.md) |
| P81 theorem figure | [`docs/figures/p81_projection_event_model_separation.svg`](figures/p81_projection_event_model_separation.svg) |
| P80 simplex-coupled predecessor | [Proposition 80](proposition_80_simplex_coupled_model_separation.md) |
| P78 continuous-family box certificate | [Proposition 78](proposition_78_certified_continuous_model_separation.md) |
| P79 sampling-radius certificate | [Proposition 79](proposition_79_certified_sampling_radius.md) |
| P77 full-law separation criterion | [Proposition 77](proposition_77_full_law_model_set_separation.md) |
| P75 declared target-model family | [Proposition 75](proposition_75_target_model_adequacy_overidentification.md) |

For equation-level origin and dependency classification, use the [P81 equation and provenance record](p81_equation_provenance.md).
