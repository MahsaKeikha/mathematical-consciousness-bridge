# P95 Equation Provenance and Novelty Boundary

## Scope

This record documents the mathematical origin and scientific status of Proposition 95, the drift-aware stratified sign-coherence rejection theorem.

P95 is repository-original as a specific familywise construction that combines the P92 nonlinear sign invariant, the P93 sign-stability radius, and the P94 finite-range dependent confidence radius across multiple predeclared drifting regimes.

The elementary ingredients used in the proof are standard. The novelty claim is not that the union bound, Hoeffding concentration, or familywise error allocation is new mathematics. The contribution is the exact way these ingredients are assembled to repair the temporal-pooling failure proved by P94 while preserving a falsifiable target for the P75 model family.

---

## Equation inventory

### Regime-specific P94 radius

For regime `b`,

\[
\varepsilon_b
=
\sqrt{
\frac{(m_b+1)\log(14/\alpha_b)}{2n_b}
}.
\]

Status: direct specialization of the P94 finite-range dependent seven-cell concentration radius to regime-specific sample size, dependence range, and error budget.

Primary predecessor: [P94](proposition_94_finite_range_dependent_sign_coherence.md).

### Familywise allocation

\[
\sum_{b=1}^{B}\alpha_b\le\alpha.
\]

Status: declared design condition.

The simultaneous event follows from the standard union bound:

\[
\Pr\left(\bigcap_b\mathcal A_b\right)
\ge
1-\sum_b\alpha_b.
\]

No independence between regime events is needed.

### Joint P75 null

\[
H_0^{\mathrm{all}}
:
P_b\in\mathcal M_{75}
\quad\text{for every }b.
\]

Status: repository-defined scientific target for the drift-aware analysis.

The change from one pooled marginal law to a collection of regime-specific laws is the central conceptual move in P95.

### Local sign-coherence rejection

For any regime `b_star`,

\[
\widehat D_{b_\star,1}
\widehat D_{b_\star,2}
\widehat D_{b_\star,3}<0
\]

and

\[
\varepsilon_{b_\star}<\min_i\widehat r_{b_\star,i}
\]

imply

\[
P_{b_\star}\notin\mathcal M_{75}
\]

on the simultaneous confidence event.

Status: repository-original drift-aware composition of P92, P93, and P94.

### Exact-rational regime gate

With the P79 logarithm bracket

\[
\underline L_b
\le
\log(14/\alpha_b)
\le
\overline L_b,
\]

P95 uses the safe comparison

\[
\frac{(m_b+1)\overline L_b}{2n_b}
<
\left(\min_i\widehat r_{b,i}\right)^2.
\]

Status: direct extension of the P94 exact-rational gate with regime-specific error allocation.

Primary predecessors: [P79](proposition_79_certified_sampling_radius.md), [P93](proposition_93_localized_sign_coherence_rejection.md), and [P94](proposition_94_finite_range_dependent_sign_coherence.md).

### Balanced 95 percent witness threshold

With total familywise level `alpha=0.05` and equal allocation across `B` regimes,

\[
\alpha_b=\frac{0.05}{B}.
\]

For the established P92 witness radius `1/24`,

\[
\boxed{
n>288(m+1)\log(280B).}
\]

For `B=2` and `m=1`, exact P79 bracketing gives the first integer crossing `n=3645`; the first denominator-24 replication is `n=3648`.

Status: repository-derived threshold from the P94 radius and the P92/P93 witness geometry.

---

## Standard mathematical ingredients

The proof uses only standard ingredients already cited and audited in predecessor propositions:

- Hoeffding's inequality for bounded independent variables inside the P94 residue classes;
- Holder's inequality in the P94 finite-range dependence argument;
- a union bound for simultaneous control across seven witness cells and then across regimes;
- exact determinant sign-stability geometry from P92 and P93;
- exact rational logarithm bracketing from P79.

P95 does not claim these standard ingredients as new.

---

## Repository-original content

The repository-original contribution is the following combined statement:

1. allow arbitrary marginal changes between predeclared regimes;
2. keep only local common-marginal assumptions inside each regime;
3. permit different finite dependence ranges and sample sizes by regime;
4. permit arbitrary dependence between regime events;
5. allocate exact rational familywise error budgets;
6. reject the joint null that every regime-specific law belongs to P75 if any locally certified regime violates the P92 sign invariant;
7. never interpret the pooled drifting distribution as one stationary P75 target.

This directly addresses the P94 temporal-drift no-go certificate.

---

## Scientific boundary

P95 is a conditional statistical theorem about a declared latent-class model family and predeclared temporal regimes.

It does not prove that:

- the predeclared segmentation is scientifically optimal;
- data-dependent change-point selection is automatically valid;
- gradual drift inside a regime is controlled;
- P75 is true when no regime rejects;
- any recovered latent state is consciousness;
- consciousness is nonphysical;
- the physical-to-experiential bridge is solved.

The result should therefore be read as a model-audit theorem, not an ontology theorem.

---

## Direct audit path

- Theorem: [`proposition_95_drift_aware_stratified_sign_coherence.md`](proposition_95_drift_aware_stratified_sign_coherence.md)
- Implementation: [`../src/consciousness_bridge/drift_aware_stratified_sign_coherence.py`](../src/consciousness_bridge/drift_aware_stratified_sign_coherence.py)
- Tests: [`../tests/test_drift_aware_stratified_sign_coherence.py`](../tests/test_drift_aware_stratified_sign_coherence.py)
- P94 drift no-go predecessor: [`p94_temporal_drift_no_go.md`](p94_temporal_drift_no_go.md)
