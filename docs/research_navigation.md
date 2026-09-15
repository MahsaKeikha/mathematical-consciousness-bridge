# Research Navigation

**Use this page when you know what kind of detail you want and need the shortest route to it.**

This page is an index, not another chapter. If you are still learning the overall story, go one layer up to the **[Research Map](research_map.md)**.

The current documented theorem frontier is **P98**. The formal release is **v0.82.0**. The final bridge from physical description to experience remains open.

---

## Choose by question

| I want to find... | Go here |
| --- | --- |
| A short first introduction | [Start Here](../START_HERE.md) |
| The overall scientific story | [Research Map](research_map.md) |
| The formal physical and bridge architecture | [Technical Research Architecture](research_architecture.md) |
| The central sufficiency problem | [Bridge Problem](bridge_problem.md) |
| The dependency structure of the mathematics | [Theorem Roadmap](theorem_roadmap.md) |
| Every proposition in chronological order | [Detailed Proposition Record](detailed_proposition_record.md) |
| What could falsify a claim | [Falsification Program](falsification_program.md) |
| Equation and source provenance | [Equation and Citation Map](equation_and_citation_map.md) |
| All figures and their interpretation | [Figure Catalog](figure_catalog.md) |
| Code, tests, and reproducibility | [Reproducibility Guide](reproducibility.md) |
| Definitions of recurring terms | [Glossary](glossary.md) |
| Citation guidance | [Citation Guide](../CITATION.md) |

---

## Choose by scientific branch

### Physical foundations

**Question:** What physical structure is actually being described, and which parts are invariant, identifiable, causal, temporal, compositional, or dependent on scale?

**Results:** P1 through P18, and P25 through P37

**Start with:** [Technical Research Architecture](research_architecture.md) · [Theorem Roadmap](theorem_roadmap.md)

---

### Physical sufficiency

**Question:** Does the declared physical descriptor preserve every distinction required by an independently specified target?

**Results:** P19 through P24

**Start with:** [P19: Fundamental Physical Sufficiency](proposition_19_fundamental_physical_sufficiency.md)

Then use the [Theorem Roadmap](theorem_roadmap.md) for the extensions involving finite data, refinement, selection, and repeated analysis.

---

### Quantum operational branch

**Question:** What can a complete operational quantum description establish, and what still requires an independent bridge principle?

**Results:** P38 through P44

**Start with:** [Quantum Foundations and Bridge Test](quantum_foundations_and_bridge_test.md)

---

### Experiment design and calibration

**Question:** How should evidence be collected, scheduled, and allocated without losing statistical validity or wasting resources?

**Results:** P45 through P70

**Start with:** [Theorem Roadmap](theorem_roadmap.md) · [Calibration and Optimization Frontier](calibration_optimization_frontier_p61_p70.md)

---

### Target integrity and measurement

**Question:** Is the target independent of the physical descriptor, and can its measurement be trusted?

**Results:** P71 through P74

This branch addresses circular targets, noisy observation, identifiability of the measurement channel, and recovery from finite data.

**Start with:** [P71: Target Provenance Noncircularity](proposition_71_target_provenance_noncircularity.md)

Then follow P72 through P74 in the [Detailed Proposition Record](detailed_proposition_record.md).

---

### Model adequacy and exact separation

**Question:** Can the declared model of the target and its measurement actually reproduce the observations, or can it be rejected under its own assumptions?

**Results:** P75 through P98

This branch moves from model adequacy to rejection with finite data, separation from the complete declared model set, certified bounds for continuous families, and increasingly strong exact tests that preserve shared parameters.

**Start with:** [P75: Target Model Adequacy](proposition_75_target_model_adequacy_overidentification.md)

**Previous frontier:** [P97: Simultaneous Finite Candidate-Family Selection](proposition_97_simultaneous_candidate_family_selection.md)

---

## Audit the current frontier without searching folders

For P98:

| Audit surface | Canonical route |
| --- | --- |
| Direct theorem | [P98 proposition](proposition_98_cross_fitted_selection_valid_certification.md) |
| Equation and method provenance | [P98 provenance](p98_equation_provenance.md) |
| Implementation | [`cross_fitted_selection_valid_certification.py`](../src/consciousness_bridge/cross_fitted_selection_valid_certification.py) |
| Regression tests | [`test_cross_fitted_selection_valid_certification.py`](../tests/test_cross_fitted_selection_valid_certification.py) |
| Theorem figure | [P98 cross-fitted certificate](figures/p98_cross_fitted_selection_valid_certification.svg) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P98 is a conditional rotated-holdout theorem. It requires mutually independent certification blocks, own-fold exclusion from selection, frozen fold plans, and exact fold-level error accounting. The final fold certificates may be dependent.

---

For P97 (previous frontier):

| Audit surface | Canonical route |
| --- | --- |
| Direct theorem | [P97 proposition](proposition_97_simultaneous_candidate_family_selection.md) |
| Equation and method provenance | [P97 provenance](p97_equation_provenance.md) |
| Implementation | [`simultaneous_candidate_family_selection.py`](../src/consciousness_bridge/simultaneous_candidate_family_selection.py) |
| Regression tests | [`test_simultaneous_candidate_family_selection.py`](../tests/test_simultaneous_candidate_family_selection.py) |
| Theorem figure | [P97 simultaneous candidate-family certificate](figures/p97_simultaneous_candidate_family_selection.svg) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P97 is a conditional same-data selection-valid model-audit result for a finite candidate family fixed before certification statistics are inspected. It pays for candidate search through explicit multiplicity rather than P96 sample separation. New post-inspection candidates, unrestricted within-regime drift, model acceptance, consciousness identification, nonphysicality, and bridge completion remain outside the theorem.

---

For P96 (previous frontier):

| Audit surface | Canonical route |
| --- | --- |
| Direct theorem | [P96 proposition](proposition_96_selection_valid_holdout_stratification.md) |
| Equation and method provenance | [P96 provenance](p96_equation_provenance.md) |
| Implementation | [`selection_valid_holdout_stratification.py`](../src/consciousness_bridge/selection_valid_holdout_stratification.py) |
| Regression tests | [`test_selection_valid_holdout_stratification.py`](../tests/test_selection_valid_holdout_stratification.py) |
| Theorem figure | [P96 selection-valid holdout certificate](figures/p96_selection_valid_holdout_stratification.svg) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P96 is a conditional selection-valid model-audit result. Pilot selection may be arbitrarily complicated, but the selected plan must be frozen before evaluation on genuinely independent holdout information that satisfies the selected local P94 assumptions. A naive split of one dependent stream is not automatically independent. The theorem does not establish model acceptance after non-rejection, identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.

---

For P89:

| Audit surface | Canonical route |
| --- | --- |
| Direct theorem | [P89 proposition](proposition_89_complete_linear_parity_duality.md) |
| Equation and method provenance | [P89 provenance](p89_equation_provenance.md) |
| Implementation | [`complete_linear_parity_duality.py`](../src/consciousness_bridge/complete_linear_parity_duality.py) |
| Regression tests | [`test_complete_linear_parity_duality.py`](../tests/test_complete_linear_parity_duality.py) |
| Theorem figure | [P89 complete-linear certificate](figures/p89_complete_linear_parity_duality.svg) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P89 is a conditional model-separation result for the declared P75 target-measurement family. It closes the declared real linear parity-functional class only; it does not identify the latent state with consciousness, establish nonphysicality, exhaust nonlinear model constraints, or close the final bridge from physical description to experience.

---

## How to audit any proposition

Every mature result is intended to follow the same chain:

**question → assumptions → theorem → proof → implementation → tests → provenance → scientific boundary**

You do not need every link for every purpose.

- If you want the **idea**, read the proposition introduction and conclusion.
- If you want the **mathematics**, read the theorem and proof.
- If you want to **verify the computation**, inspect the source and tests.
- If you want to know **where an equation came from**, open its provenance record.
- If you want to know **what the result does not establish**, read the scientific boundary section.

The [Detailed Proposition Record](detailed_proposition_record.md) is the complete proposition audit trail.

---

## Choose by background

| Your background | Suggested path |
| --- | --- |
| Physics | [Research Map](research_map.md) → [Technical Research Architecture](research_architecture.md) → [Quantum branch](quantum_foundations_and_bridge_test.md) |
| Mathematics | [Research Map](research_map.md) → [Theorem Roadmap](theorem_roadmap.md) → proposition proofs |
| Statistics and inference | [P19](proposition_19_fundamental_physical_sufficiency.md) → P20 through P24 → P74 through P98 via [Detailed Proposition Record](detailed_proposition_record.md) |
| Consciousness science | [Bridge Problem](bridge_problem.md) → [Falsification Program](falsification_program.md) → P71 through P98 |
| Software and reproducibility | [Reproducibility Guide](reproducibility.md) → [`src/`](../src/) → [`tests/`](../tests/) |
| Visual learner | [Figure Catalog](figure_catalog.md) → [Visual Atlas](../website/visual-atlas.html) |

---

## Where the complete detail lives

This page intentionally does **not** duplicate the full 98 proposition index.

Use:

- **[Detailed Proposition Record](detailed_proposition_record.md)** for the complete chronological record;
- **[Theorem Roadmap](theorem_roadmap.md)** for mathematical dependencies;
- **[Equation and Citation Map](equation_and_citation_map.md)** for provenance;
- **[Figure Catalog](figure_catalog.md)** for the complete visual record;
- **[Reproducibility Guide](reproducibility.md)** for code and verification.

That separation is deliberate: each page should have one job.

---

**One layer up:** [Research Map](research_map.md)
**Formal dependency layer:** [Theorem Roadmap](theorem_roadmap.md)
**Complete theorem archive:** [Detailed Proposition Record](detailed_proposition_record.md)

## P90 historical nonlinear frontier

For P90:

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P90 proposition](proposition_90_exact_nonlinear_rank_one_separation.md) |
| Equation and method provenance | [P90 provenance](p90_equation_provenance.md) |
| Implementation | [`exact_nonlinear_rank_one_separation.py`](../src/consciousness_bridge/exact_nonlinear_rank_one_separation.py) |
| Regression tests | [`test_exact_nonlinear_rank_one_separation.py`](../tests/test_exact_nonlinear_rank_one_separation.py) |
| Figure | [P90 nonlinear rank-one certificate](figures/p90_exact_nonlinear_rank_one_separation.svg) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P90 is a conditional model-separation result for the declared strict P75 box. It uses nonlinear model-image structure but does not identify the latent state with consciousness, establish nonphysicality, or close the physical-to-experiential bridge.

## P91 historical mixed-prevalence frontier

For P91:

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P91 proposition](proposition_91_mixed_prevalence_rank_two_flattening_separation.md) |
| Equation and method provenance | [P91 provenance](p91_equation_provenance.md) |
| Implementation | [`mixed_prevalence_rank_two_flattening_separation.py`](../src/consciousness_bridge/mixed_prevalence_rank_two_flattening_separation.py) |
| Regression tests | [`test_mixed_prevalence_rank_two_flattening_separation.py`](../tests/test_mixed_prevalence_rank_two_flattening_separation.py) |
| Figure | [P91 mixed-prevalence rank-two certificate](figures/p91_mixed_prevalence_rank_two_flattening_separation.svg) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P91 certifies `1/42 < d_inf(P_emp, M75) <= 1/24` over the full P75 parameter cube. It does not claim that `1/24` is the exact global optimum and does not identify the latent state with consciousness, establish nonphysicality, or close the physical-to-experiential bridge.

## P92 historical exact population frontier

For P92:

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P92 proposition](proposition_92_exact_global_mixed_prevalence_distance.md) |
| Equation and method provenance | [P92 provenance](p92_equation_provenance.md) |
| Implementation | [`exact_global_mixed_prevalence_distance.py`](../src/consciousness_bridge/exact_global_mixed_prevalence_distance.py) |
| Regression tests | [`test_exact_global_mixed_prevalence_distance.py`](../tests/test_exact_global_mixed_prevalence_distance.py) |
| Figure | [P92 exact global distance](figures/p92_exact_global_mixed_prevalence_distance.svg) |
| Repository reproduction | [Reproducibility Guide](reproducibility.md) |

P92 proves the exact full-cube result `d_inf(P_emp, M75) = 1/24`. Its lower certificate is a nonlinear three-minor sign-coherence invariant. The result does not identify the latent state with consciousness, establish nonphysicality, or close the physical-to-experiential bridge.

## P93 historical IID finite-sample frontier

For P93:

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P93 proposition](proposition_93_localized_sign_coherence_rejection.md) |
| Equation and method provenance | [P93 provenance](p93_equation_provenance.md) |
| Implementation | [`localized_sign_coherence_rejection.py`](../src/consciousness_bridge/localized_sign_coherence_rejection.py) |
| Exact tests | [`test_localized_sign_coherence_rejection.py`](../tests/test_localized_sign_coherence_rejection.py) |
| Figure | [P93 localized finite-sample certificate](figures/p93_localized_sign_coherence_rejection.svg) |

P93 uses seven observable cells from the P92 sign witness. The 1623 crossing is the exact mathematical confidence-radius threshold for the established sign geometry at 95 percent confidence; the first exact replication of the original profile that clears is 1632.

## P94 historical finite-range frontier

For P94:

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P94 proposition](proposition_94_finite_range_dependent_sign_coherence.md) |
| Equation and method provenance | [P94 provenance](p94_equation_provenance.md) |
| Implementation | [`finite_range_dependent_sign_coherence.py`](../src/consciousness_bridge/finite_range_dependent_sign_coherence.py) |
| Exact threshold implementation | [`finite_range_dependent_sign_coherence_threshold.py`](../src/consciousness_bridge/finite_range_dependent_sign_coherence_threshold.py) |
| Exact tests | [`test_finite_range_dependent_sign_coherence.py`](../tests/test_finite_range_dependent_sign_coherence.py) |
| Figure | [P94 finite-range dependence certificate](figures/p94_finite_range_dependent_sign_coherence.svg) |

P94 relaxes temporal independence, not stationarity. Its confidence radius carries an exact `m+1` squared-radius penalty under a declared finite dependence range and one common marginal law. The exact pooling counterexample proves that arbitrary marginal drift can imitate the P92 negative determinant-product pattern, so drift remains outside the theorem.

## P95 historical drift-aware frontier

**Immediate predecessor:** [P95: Drift-Aware Stratified Sign-Coherence Rejection](proposition_95_drift_aware_stratified_sign_coherence.md)

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P95 proposition](proposition_95_drift_aware_stratified_sign_coherence.md) |
| Equation and method provenance | [P95 provenance](p95_equation_provenance.md) |
| Implementation | [`drift_aware_stratified_sign_coherence.py`](../src/consciousness_bridge/drift_aware_stratified_sign_coherence.py) |
| Regression tests | [`test_drift_aware_stratified_sign_coherence.py`](../tests/test_drift_aware_stratified_sign_coherence.py) |
| Figure | [P95 drift-aware stratified certificate](figures/p95_drift_aware_stratified_sign_coherence.svg) |

P95 permits marginal drift across predeclared regimes while keeping a common marginal law only within each regime. P96 keeps that local P95 logic but allows the regime plan itself to be chosen from separate pilot information.


## P96 previous frontier

**Previous frontier:** [P97: Simultaneous Finite Candidate-Family Selection](proposition_97_simultaneous_candidate_family_selection.md)

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P96 proposition](proposition_96_selection_valid_holdout_stratification.md) |
| Equation and method provenance | [P96 provenance](p96_equation_provenance.md) |
| Implementation | [`selection_valid_holdout_stratification.py`](../src/consciousness_bridge/selection_valid_holdout_stratification.py) |
| Regression tests | [`test_selection_valid_holdout_stratification.py`](../tests/test_selection_valid_holdout_stratification.py) |
| Figure | [P96 selection-valid holdout certificate](figures/p96_selection_valid_holdout_stratification.svg) |

P96 permits pilot-selected regime plans only when selection and certification are separated by a justified independent holdout design and the selected plan is frozen before holdout evaluation. It inherits the P95 local rejection logic and preserves the same familywise error budget by conditioning on the pilot information.


## P97 previous frontier

**Previous frontier:** [P97: Simultaneous Finite Candidate-Family Selection](proposition_97_simultaneous_candidate_family_selection.md)

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P97 proposition](proposition_97_simultaneous_candidate_family_selection.md) |
| Equation and method provenance | [P97 provenance](p97_equation_provenance.md) |
| Implementation | [`simultaneous_candidate_family_selection.py`](../src/consciousness_bridge/simultaneous_candidate_family_selection.py) |
| Regression tests | [`test_simultaneous_candidate_family_selection.py`](../tests/test_simultaneous_candidate_family_selection.py) |
| Figure | [P97 simultaneous candidate-family certificate](figures/p97_simultaneous_candidate_family_selection.svg) |

P97 permits same-data comparison and post-inspection selection only within a finite candidate family fixed before certification statistics are inspected. It assigns exact candidate-level budgets, nests P95 within each candidate, and uses a second union bound across candidates to preserve simultaneous validity.


## P98 current frontier

**Current frontier:** [P98: Cross-Fitted Selection-Valid Certification](proposition_98_cross_fitted_selection_valid_certification.md)

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P98 proposition](proposition_98_cross_fitted_selection_valid_certification.md) |
| Equation and method provenance | [P98 provenance](p98_equation_provenance.md) |
| Implementation | [`cross_fitted_selection_valid_certification.py`](../src/consciousness_bridge/cross_fitted_selection_valid_certification.py) |
| Regression tests | [`test_cross_fitted_selection_valid_certification.py`](../tests/test_cross_fitted_selection_valid_certification.py) |
| Figure | [P98 cross-fitted certificate](figures/p98_cross_fitted_selection_valid_certification.svg) |

P98 rotates independent holdout certification across mutually independent blocks. Every block may contribute to selection for other folds and to certification in its own fold, but no fold may use its own certification statistics to choose the plan later tested on that fold.
