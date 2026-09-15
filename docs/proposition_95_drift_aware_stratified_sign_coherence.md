# Proposition 95: Drift-Aware Stratified Sign-Coherence Rejection

## Purpose

P94 extends the P92 and P93 sign-coherence rejection witness from IID samples to a declared finite-range dependent stream with one common marginal law. It also proves an exact no-go result for naive temporal pooling: two time-specific P75 laws can each satisfy the P92 sign constraint while their average violates it.

P95 closes the next gap by changing the scientific target.

Instead of asking whether one pooled drifting law belongs to P75, P95 asks:

> Across predeclared regimes, can we reject the joint null that every regime-specific marginal law belongs to P75?

The answer is yes. Each regime receives its own P94 certificate and its own error budget. A familywise union bound then remains valid even if the regimes are dependent on one another.

P95 therefore permits arbitrary marginal drift across regimes while preserving a rigorous rejection statement about the collection of regime-specific laws.

---

## P95A. Predeclared regime model

Let the observation sequence be partitioned into `B` predeclared regimes

\[
\mathcal R_1,\ldots,\mathcal R_B.
\]

For regime `b`, let the sample size be

\[
n_b=|\mathcal R_b|.
\]

Assume only within that regime that:

1. every observation has the same regime-specific marginal four-view law `P_b`;
2. the regime is `m_b`-dependent in the P94 sense;
3. the seven P92 witness cells are measured under the same declared coding convention.

The marginal laws may drift freely across regimes:

\[
P_b\neq P_{b'}
\]

is allowed.

No independence assumption between different regimes is required.

The regime boundaries must be fixed independently of the selected P92 witness. If boundaries are chosen after inspecting the same sign-coherence statistic, additional selection accounting is required and P95 does not apply directly.

---

## P95B. Regime-specific confidence events

Give regime `b` an exact rational error budget

\[
\alpha_b>0.
\]

Let the total declared familywise budget satisfy

\[
\boxed{
\sum_{b=1}^{B}\alpha_b\le\alpha.
}
\]

P94 gives the regime-specific seven-cell radius

\[
\boxed{
\varepsilon_b
=
\sqrt{
\frac{(m_b+1)\log(14/\alpha_b)}{2n_b}
}.
}
\]

Define the event

\[
\mathcal A_b
=
\left\{
\max_{x\in\mathcal J}
|\widehat P_b(x)-P_b(x)|
\le\varepsilon_b
\right\},
\]

where `J` is the same seven-cell set used by P92 through P94.

P94 implies

\[
\Pr(\mathcal A_b^c)\le\alpha_b.
\]

A union bound across regimes gives

\[
\Pr\left(\bigcap_{b=1}^{B}\mathcal A_b\right)
\ge
1-\sum_{b=1}^{B}\alpha_b
\ge
1-\alpha.
\]

This step does not require the regime events to be independent.

---

## P95C. Drift-aware joint rejection theorem

For regime `b`, let

\[
\widehat D_{b,1},\widehat D_{b,2},\widehat D_{b,3}
\]

be the empirical P92 determinants and let

\[
\widehat r_{b,1},\widehat r_{b,2},\widehat r_{b,3}
\]

be their exact P93 sign-stability radii.

Suppose some predeclared regime `b_star` satisfies

\[
\widehat D_{b_\star,1}
\widehat D_{b_\star,2}
\widehat D_{b_\star,3}<0
\]

and

\[
\boxed{
\varepsilon_{b_\star}
<
\min_i\widehat r_{b_\star,i}.
}
\]

On the simultaneous event from P95B, P93 sign stability preserves all three determinant signs in that regime. Therefore

\[
D_{b_\star,1}D_{b_\star,2}D_{b_\star,3}<0.
\]

P92 proves that every P75 law must satisfy

\[
D_1D_2D_3\ge0.
\]

Hence

\[
P_{b_\star}\notin\mathcal M_{75}.
\]

The joint null

\[
\boxed{
H_0^{\mathrm{all}}
:
P_b\in\mathcal M_{75}
\quad\text{for every }b=1,\ldots,B
}
\]

is therefore rejected with confidence at least

\[
\boxed{
1-\sum_b\alpha_b
\ge
1-\alpha.
}
\]

This is the P95 drift-aware conclusion.

It is a statement about the collection of regime-specific laws. It is not a statement about the pooled marginal law.

---

## P95D. Exact-rational gate

As in P94, no ordinary floating-point logarithm or square root is required for the executable rejection gate.

For each regime, P79 provides a rational bracket

\[
\underline L_b
\le
\log(14/\alpha_b)
\le
\overline L_b.
\]

Therefore

\[
\frac{(m_b+1)\underline L_b}{2n_b}
\le
\varepsilon_b^2
\le
\frac{(m_b+1)\overline L_b}{2n_b}.
\]

The safe regime-specific rejection comparison is

\[
\boxed{
\frac{(m_b+1)\overline L_b}{2n_b}
<
\left(
\min_i\widehat r_{b,i}
\right)^2.
}
\]

All quantities in this final gate are rational.

---

## P95E. Equal-budget 95 percent threshold

For a simple balanced design, split the total 5 percent familywise error budget equally:

\[
\alpha_b=rac{0.05}{B}.
\]

For the established P92 witness,

\[
\min_i\widehat r_i=\frac1{24}.
\]

The P95 threshold becomes

\[
\sqrt{
\frac{(m+1)\log(280B)}{2n}
}
<
\frac1{24},
\]

or equivalently

\[
\boxed{
n>288(m+1)\log(280B).}
\]

For two equally budgeted regimes and one-step dependence, `B=2` and `m=1`, the first mathematical crossing is

\[
\boxed{n=3645}
\]

per regime. The first exact replication of the denominator-24 witness that clears the gate is

\[
\boxed{n=3648}
\]

per regime.

For `B=1`, P95 reduces exactly to the P94 threshold.

---

## P95F. What drift is now allowed

P95 allows the regime-specific laws to differ arbitrarily:

\[
P_1,P_2,\ldots,P_B
\]

need not lie on a smooth path, share prevalence, share channel parameters, or average to a P75 law.

The theorem also allows different:

- sample sizes `n_b`;
- dependence ranges `m_b`;
- error budgets `alpha_b`.

The only stationarity requirement is local: one common marginal law inside each declared regime.

This is why P95 resolves the exact pooling failure exposed by P94 without making an unsupported stationary approximation.

---

## P95G. What P95 does not solve

P95 does not cover:

1. data-dependent regime boundaries selected using the same rejection statistic without additional correction;
2. unknown change points inferred from the same data unless the segmentation procedure receives its own validity argument;
3. gradual drift inside a regime when no common marginal law is defensible;
4. unknown or misspecified within-regime dependence range;
5. long-range dependence or general mixing without additional concentration results;
6. acceptance of P75 when no regime rejects;
7. semantic validation of the latent state;
8. identification of any latent class with consciousness;
9. nonphysicality of consciousness;
10. completion of the physical-to-experiential bridge.

The next natural frontier is therefore no longer naive pooling. It is either valid data-dependent segmentation, gradual-drift concentration around a declared time-varying target, or broader dependence classes with explicit assumptions.

---

## Reproducibility

Implementation:

[`src/consciousness_bridge/drift_aware_stratified_sign_coherence.py`](../src/consciousness_bridge/drift_aware_stratified_sign_coherence.py)

Regression tests:

[`tests/test_drift_aware_stratified_sign_coherence.py`](../tests/test_drift_aware_stratified_sign_coherence.py)

Direct predecessors:

- [P92 exact global mixed-prevalence distance](proposition_92_exact_global_mixed_prevalence_distance.md)
- [P93 localized finite-sample sign-coherence rejection](proposition_93_localized_sign_coherence_rejection.md)
- [P94 finite-range dependent sign-coherence rejection](proposition_94_finite_range_dependent_sign_coherence.md)

Equation and novelty record:

[`p95_equation_provenance.md`](p95_equation_provenance.md)
