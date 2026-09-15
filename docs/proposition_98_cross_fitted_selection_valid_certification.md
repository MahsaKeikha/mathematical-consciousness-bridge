# Proposition 98: Cross-Fitted Selection-Valid Certification

## Purpose

P96 proves that an arbitrarily complicated data-dependent regime plan may be certified without an extra selection-complexity penalty when the plan is learned from information independent of the final certification sample. The cost is a dedicated holdout: information used for final certification cannot also be used to choose that same plan.

P97 proves a complementary same-data result for a finite family fixed before certification statistics are inspected. It permits post-inspection choice among the predeclared candidates, but pays an explicit multiplicity budget across them.

P98 rotates the P96 separation across several independent data blocks. Every block serves once as certification information and may serve as selection information for the other folds. The resulting fold certificates are generally dependent because their selection information overlaps, so P98 does not multiply fold probabilities. Instead, it uses one exact union bound across fold-level error budgets.

The key distinction is:

> P98 permits arbitrary leave-one-block-out plan selection in every fold, provided each fold is certified only on a block excluded from its own selection information and the fold-level budgets are controlled simultaneously.

This recovers certification use from every independent block without pretending that cross-fitting removes multiplicity.

---

## P98A. Independent certification blocks

Let

\[
\mathcal D_1,\ldots,\mathcal D_K
\]

be mutually independent data blocks, with \(K\ge 2\).

For fold \(k\), define the selection information

\[
\mathcal S_k
\subseteq
\sigma(\mathcal D_1,\ldots,\mathcal D_{k-1},\mathcal D_{k+1},\ldots,\mathcal D_K).
\]

The fold-specific plan

\[
\widehat\Pi_k
\]

may be an arbitrarily complicated \(\mathcal S_k\)-measurable function. It may choose the number of regimes, regime definitions, declared finite dependence ranges, and exact rational local error budgets.

The only structural requirement is that \(\widehat\Pi_k\) is frozen before any certification statistic from \(\mathcal D_k\) is inspected.

Because the blocks are mutually independent,

\[
\boxed{
\mathcal D_k\perp\mathcal S_k.
}
\]

Thus each fold satisfies the selection-certification separation required by P96.

---

## P98B. Fold-level conditional validity

Give fold \(k\) an exact error budget \(\beta_k\), and require the P95 regime budgets inside \(\widehat\Pi_k\) to sum to at most \(\beta_k\).

Let \(\mathcal A_k\) be the event that every local confidence statement in the P96 certificate for fold \(k\) is correct.

Conditional on \(\mathcal S_k\), the selected plan is fixed. P96 therefore gives

\[
\Pr(\mathcal A_k^c\mid\mathcal S_k)\le\beta_k.
\]

Taking expectations over the selection information yields

\[
\boxed{
\Pr(\mathcal A_k^c)\le\beta_k.
}
\]

No complexity term depending on how difficult the plan-selection algorithm is appears in this fold-level inequality.

---

## P98C. Simultaneous cross-fitted theorem

Require

\[
\boxed{
\sum_{k=1}^{K}\beta_k\le\alpha.
}
\]

The fold events \(\mathcal A_k\) need not be independent. In fact, under ordinary cross-fitting they are generally dependent because the plan for one fold may use data that serve as certification information in another fold.

Nevertheless, the union bound gives

\[
\Pr\left(\bigcup_{k=1}^{K}\mathcal A_k^c\right)
\le
\sum_{k=1}^{K}\Pr(\mathcal A_k^c)
\le
\sum_{k=1}^{K}\beta_k
\le\alpha.
\]

Therefore

\[
\boxed{
\Pr\left(\bigcap_{k=1}^{K}\mathcal A_k\right)\ge1-\alpha.
}
\]

This is the P98 simultaneous cross-fitted event.

---

## P98D. Post-inspection fold selection

After every fold has been certified, let

\[
\widehat K
\in\{1,\ldots,K\}
\]

be any rule that selects a fold after inspecting the complete set of fold results.

On the simultaneous event, every fold certificate is already correct. Hence

\[
\boxed{
\bigcap_{k=1}^{K}\mathcal A_k
\subseteq
\mathcal A_{\widehat K}.
}
\]

Consequently,

\[
\boxed{
\Pr(\mathcal A_{\widehat K})\ge1-\alpha.
}
\]

The selected fold may therefore be chosen because it has the strongest certified rejection, the largest certified margin, or another post-inspection criterion. No additional correction is needed beyond the fold budgets already included in \(\sum_k\beta_k\).

---

## P98E. Cross-fitted rejection

For fold \(k\), let the selected P95 plan contain regimes

\[
\widehat\Pi_k
=
\{(\mathcal R_{kb},m_{kb},\alpha_{kb})\}_{b=1}^{B_k},
\]

with

\[
\sum_{b=1}^{B_k}\alpha_{kb}\le\beta_k.
\]

If the nested P96/P95 certificate for fold \(k\) certifies the P92 sign violation in at least one selected regime, then that fold's selected joint null

\[
H_{0,k}:
P_{kb}\in\mathcal M_{75}
\quad\text{for every selected regime }b
\]

is rejected under the fold's declared assumptions.

Define the cross-fitted joint null

\[
H_0^{\mathrm{CF}}:
H_{0,k}\text{ holds for every }k=1,\ldots,K.
\]

On the simultaneous P98 event, any certified fold rejection implies

\[
\boxed{
H_0^{\mathrm{CF}}\text{ is false}.
}
\]

Thus the rule "reject if any cross-fitted fold certifies rejection" has familywise error at most \(\alpha\) under the declared design.

---

## P98F. Why overlapping selection information is allowed

For \(K>2\), the selection information for different folds overlaps. For example, fold 1 may select using blocks 2 through \(K\), while fold 2 may select using blocks 1 and 3 through \(K\).

Therefore the random selected plans and final fold certificates are not independent.

P98 does not need them to be independent.

The proof uses only two ingredients:

1. for each fold separately, its own certification block is independent of the information used to choose its own plan;
2. the unconditional fold error probabilities are combined with a union bound.

This is why the theorem remains valid despite heavy cross-fold reuse.

---

## P98G. Exact-rational execution

Every fold budget \(\beta_k\) and regime budget \(\alpha_{kb}\) may be represented exactly as a rational number.

Inside fold \(k\), P96 delegates to the exact P95/P94 gate. For regime \(b\), sample size \(n_{kb}\), dependence range \(m_{kb}\), and a certified rational upper bracket \(\overline L_{kb}\) for \(\log(14/\alpha_{kb})\), rejection is certified whenever

\[
\boxed{
\frac{(m_{kb}+1)\overline L_{kb}}{2n_{kb}}
<
\left(\min_i\widehat r_{kb,i}\right)^2.
}
\]

The outer cross-fitting proof adds only exact rational budget accounting and a union bound. It introduces no floating-point decision at the final certificate boundary.

---

## P98H. Balanced 95 percent checkpoint

Take

\[
K=2,\qquad B=2,\qquad m=1,\qquad \alpha=\frac1{20}.
\]

Equal fold spending gives

\[
\beta_k=\frac1{40}.
\]

Equal regime spending within each fold gives

\[
\boxed{
\alpha_{kb}=\frac1{80}.
}
\]

This is the same local alpha budget that appears in the established P97 two-candidate, two-regime checkpoint. Therefore the first per-regime mathematical crossing is again

\[
\boxed{n=4045},
\]

and the first exact denominator-24 replication is

\[
\boxed{n_{\mathrm{exact}}=4056}.
\]

Each certification fold contains two regimes, so the first certification-block sizes are

\[
\boxed{N_{\mathrm{fold}}=2\times4045=8090}
\]

and

\[
\boxed{N_{\mathrm{fold,exact}}=2\times4056=8112}.
\]

Because the two folds are genuinely different certification blocks, the unique data totals are

\[
\boxed{N_{\mathrm{CF}}=2\times8090=16180}
\]

and

\[
\boxed{N_{\mathrm{CF,exact}}=2\times8112=16224}.
\]

For either fold, the other 8090 observations at the mathematical threshold, or 8112 observations at the exact-replication threshold, may be used as selection information. Those observations are not additional data. They are the other certification block reused in the opposite role.

---

## P98I. Relation to P96 and P97

P96, P97, and P98 now define three distinct design options.

### P96: one adaptive plan, one independent holdout

- selection may be arbitrarily complicated;
- no multiplicity penalty for selection complexity;
- pilot information is not reused for final certification of the same plan;
- one holdout certificate is produced.

### P97: finite predeclared same-data candidate family

- all candidates may use the same certification data;
- candidates must be fixed before inspection;
- post-inspection selection is allowed;
- multiplicity is paid across the finite candidate family.

### P98: rotated independent-block cross-fitting

- every fold may choose an arbitrary plan from the other blocks;
- every block serves once as independent certification data;
- the fold certificates may be dependent;
- multiplicity is paid across the rotated certification statements;
- no fold may use its own certification statistics to choose its own plan.

P98 therefore closes the specific data-efficiency gap left open by P96 without relaxing the independence condition that makes selection validity possible.

---

## P98J. What P98 solves

P98 permits:

- arbitrary leave-one-block-out regime-plan selection;
- different selected regime counts in different folds;
- different regime definitions and dependence ranges by fold;
- unequal exact rational fold budgets;
- unequal exact rational regime budgets inside each fold;
- reuse of every independent block as selection information outside its own certification fold;
- simultaneous validity of all fold certificates without assuming they are independent;
- arbitrary post-inspection selection among the already certified folds;
- familywise rejection when any fold certifies a selected-plan violation.

---

## P98K. What P98 does not solve

P98 does not justify:

1. using block \(k\)'s certification statistics to choose the plan later certified on block \(k\);
2. treating adjacent pieces of one dependent stream as independent blocks merely because they were split;
3. misspecified within-regime dependence ranges;
4. unrestricted drift inside a selected regime;
5. repeated exploration of unbudgeted cross-fitting schemes followed by selective reporting;
6. assuming the cross-fitted fold certificates are independent;
7. model acceptance when no fold rejects;
8. identification of a latent state with consciousness;
9. nonphysicality of consciousness;
10. completion of the physical-to-experiential bridge.

A natural next question is whether several selection-valid cross-fitted certificates can be combined more efficiently than a simple foldwise union bound while retaining a rigorous finite-sample guarantee. That is a separate theorem problem.

---

## Reproducibility

Implementation:

[`src/consciousness_bridge/cross_fitted_selection_valid_certification.py`](../src/consciousness_bridge/cross_fitted_selection_valid_certification.py)

Regression tests:

[`tests/test_cross_fitted_selection_valid_certification.py`](../tests/test_cross_fitted_selection_valid_certification.py)

Direct predecessors:

- [P94 finite-range dependent sign-coherence rejection](proposition_94_finite_range_dependent_sign_coherence.md)
- [P95 drift-aware stratified sign-coherence rejection](proposition_95_drift_aware_stratified_sign_coherence.md)
- [P96 selection-valid holdout stratification](proposition_96_selection_valid_holdout_stratification.md)
- [P97 simultaneous candidate-family selection](proposition_97_simultaneous_candidate_family_selection.md)

Equation and novelty record:

[`p98_equation_provenance.md`](p98_equation_provenance.md)
