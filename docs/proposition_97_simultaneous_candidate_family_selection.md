# Proposition 97: Simultaneous Candidate-Family Selection

## Purpose

P96 makes arbitrarily complicated pilot selection valid by separating selection from independent holdout certification. Its cost is data separation: the pilot observations cannot also certify the selected plan.

P97 proves a complementary theorem for a different design. If the possible regime plans form a **finite family fixed before the certification statistics are inspected**, all candidates may be evaluated on the **same data**. A simultaneous error budget across the complete family then makes arbitrary post-inspection selection among those candidates valid.

The central distinction is exact:

> P96 removes the selection-complexity alpha penalty by using independent holdout information. P97 permits same-data selection from a finite predeclared candidate family by paying an explicit multiplicity budget across candidates.

P97 does not allow a new candidate to be invented after inspection and added retroactively to the certified family.

---

## P97A. Finite predeclared candidate family

Fix a finite family

\[
\mathfrak P=\{\Pi_1,\ldots,\Pi_J\}
\]

before any P92/P94/P95 certification statistic is inspected.

Candidate \(j\) contains a finite P95 regime plan

\[
\Pi_j=\{(\mathcal R_{jb},m_{jb},\alpha_{jb})\}_{b=1}^{B_j},
\]

where every regime definition, declared finite dependence range, and local rational error budget is fixed in advance.

Give candidate \(j\) a candidate-level budget \(\beta_j\) satisfying

\[
\sum_{b=1}^{B_j}\alpha_{jb}\le\beta_j.
\]

The complete candidate-family budget obeys

\[
\boxed{
\sum_{j=1}^{J}\beta_j\le\alpha.
}
\]

Different candidates may reuse exactly the same observations and may overlap arbitrarily with one another. No independence assumption between candidate certificates is required.

---

## P97B. Candidate-wise P95 events

For candidate \(j\), let \(\mathcal A_j\) denote the event that all of its local P94/P95 confidence statements are simultaneously correct.

P95 gives

\[
\Pr(\mathcal A_j^c)\le\beta_j.
\]

This statement remains valid even though another candidate may be computed from the same observations, because each candidate plan was already fixed before the certification statistics were inspected.

---

## P97C. Simultaneous candidate-family theorem

Apply the union bound over candidates:

\[
\Pr\left(\bigcup_{j=1}^{J}\mathcal A_j^c\right)
\le
\sum_{j=1}^{J}\Pr(\mathcal A_j^c)
\le
\sum_{j=1}^{J}\beta_j
\le\alpha.
\]

Therefore

\[
\boxed{
\Pr\left(\bigcap_{j=1}^{J}\mathcal A_j\right)\ge1-\alpha.
}
\]

On this event, every candidate certificate is simultaneously valid.

Now let

\[
\widehat J=\widehat J(\mathcal D)
\in\{1,\ldots,J\}
\]

be any data-dependent selection rule applied after the candidate certificates have been computed. Because all candidate statements are already correct on the simultaneous event,

\[
\boxed{
\mathcal A_1\cap\cdots\cap\mathcal A_J
\subseteq
\mathcal A_{\widehat J}.
}
\]

Hence

\[
\boxed{
\Pr(\mathcal A_{\widehat J})\ge1-\alpha.
}
\]

The selected candidate may therefore be chosen using the same data, including the observed rejection pattern, without a further post-selection correction beyond the candidate-family budget already spent.

---

## P97D. Selection-valid rejection

Suppose the selected candidate \(\widehat J\) contains at least one regime whose P95 gate certifies the P92 sign violation. On the simultaneous event, the corresponding population regime lies outside \(\mathcal M_{75}\). Therefore the selected candidate joint null

\[
H_{0,\widehat J}:
P_{\widehat J,b}\in\mathcal M_{75}
\quad\text{for every regime }b
\]

is rejected with confidence at least

\[
\boxed{1-\alpha.}
\]

This remains valid even when the analyst chooses \(\widehat J\) because it produced the most scientifically interesting or strongest certified rejection, provided \(\widehat J\) belongs to the original finite family.

---

## P97E. The multiplicity price of same-data selection

Under equal candidate spending,

\[
\beta_j=\frac{\alpha}{J}.
\]

If candidate \(j\) has \(B\) equally budgeted regimes, then

\[
\boxed{
\alpha_{jb}=\frac{\alpha}{JB}.
}
\]

Thus P97 explicitly pays for the number of candidates that are simultaneously available for post-inspection selection. This is the mathematical price that P96 avoids through independent sample separation.

The two theorems therefore establish a clean design tradeoff:

\[
\boxed{
\text{independent holdout} \Longleftrightarrow \text{no candidate-search alpha penalty},
}
\]

while

\[
\boxed{
\text{same-data finite search} \Longleftrightarrow \text{simultaneous candidate-family alpha spending}.
}
\]

---

## P97F. Exact-rational execution

All candidate and regime budgets may be exact rational numbers. Each local certificate remains the exact P94 gate nested inside P95.

For candidate \(j\), regime \(b\), sample size \(n_{jb}\), and declared dependence range \(m_{jb}\), P79/P94 provide a rational upper bracket \(\overline L_{jb}\) for

\[
\log(14/\alpha_{jb}).
\]

The local rejection gate is certified whenever

\[
\boxed{
\frac{(m_{jb}+1)\overline L_{jb}}{2n_{jb}}
<
\left(\min_i\widehat r_{jb,i}\right)^2.
}
\]

No floating-point decision is required at the final certificate boundary.

---

## P97G. Balanced 95 percent checkpoint

Take

\[
J=2,\qquad B=2,\qquad m=1,\qquad \alpha=\frac1{20}.
\]

Equal candidate and regime spending gives

\[
\beta_j=\frac1{40},
\qquad
\alpha_{jb}=\frac1{80}.
\]

For the established P92 witness radius \(1/24\), the first mathematical per-regime crossing is

\[
\boxed{n=4045},
\]

and the first exact denominator-24 replication is

\[
\boxed{n_{\mathrm{exact}}=4056}.
\]

In the balanced design, both candidate plans reuse the same underlying dataset. With two equally sized regimes per candidate, the first balanced dataset sizes are therefore

\[
\boxed{N=2\times4045=8090}
\]

and

\[
\boxed{N_{\mathrm{exact}}=2\times4056=8112}.
\]

The candidate count increases the required confidence radius through \(\alpha_{jb}\); it does **not** multiply the unique observation count by \(J\) because candidate plans are evaluated on the same observations.

---

## P97H. What P97 solves

P97 permits, from one certification dataset:

- comparison of multiple predeclared regime segmentations;
- comparison of multiple predeclared dependence-range assignments;
- unequal exact candidate and regime error budgets;
- arbitrary post-inspection choice among the already certified candidates;
- selection based on which candidate rejects, which has the strongest margin, or another data-dependent criterion.

The guarantee does not require the candidate certificates to be independent.

---

## P97I. What P97 does not solve

P97 does not justify:

1. generating a new candidate after seeing the certification statistics and treating it as if it had been predeclared;
2. searching an infinite or unbudgeted candidate family;
3. misspecified within-regime finite dependence ranges;
4. gradual drift inside a candidate regime when one common marginal law is not defensible;
5. long-range dependence without an appropriate concentration theorem;
6. model acceptance when no candidate rejects;
7. identification of a latent state with consciousness;
8. nonphysicality of consciousness;
9. completion of the physical-to-experiential bridge.

A natural next question is whether sample-splitting can be rotated so that every independent data block serves once as certification data and elsewhere as selection information. That is the cross-fitting direction suggested by P96.

---

## Reproducibility

Implementation:

[`src/consciousness_bridge/simultaneous_candidate_family_selection.py`](../src/consciousness_bridge/simultaneous_candidate_family_selection.py)

Regression tests:

[`tests/test_simultaneous_candidate_family_selection.py`](../tests/test_simultaneous_candidate_family_selection.py)

Direct predecessors:

- [P92 exact global mixed-prevalence distance](proposition_92_exact_global_mixed_prevalence_distance.md)
- [P94 finite-range dependent sign-coherence rejection](proposition_94_finite_range_dependent_sign_coherence.md)
- [P95 drift-aware stratified sign-coherence rejection](proposition_95_drift_aware_stratified_sign_coherence.md)
- [P96 selection-valid holdout stratification](proposition_96_selection_valid_holdout_stratification.md)

Equation and novelty record:

[`p97_equation_provenance.md`](p97_equation_provenance.md)
