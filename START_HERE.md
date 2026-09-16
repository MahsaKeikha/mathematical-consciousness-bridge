# Start Here

**A short introduction to the Mathematical Consciousness Bridge research program.**

> ## The central question
>
> **When can a physical description be said to explain a difference related to experience, rather than simply correlate with it?**

This project does not begin by choosing a formula for consciousness. It begins by asking what a scientific bridge from physics to experience would have to demonstrate before we should trust it.

The basic idea is simple: **define the physical description clearly, define the target independently, test whether the measurements are trustworthy, and give the proposed model a real chance to fail.**

The mathematics behind those steps is extensive. You do not need it to understand the research question. It is available through the deeper links below when you want to inspect the details.

---

## The research in four steps

### 1. Describe the physical system clearly

What information about the system are we actually using?

A claim cannot be stronger than the description it begins with. The project therefore asks what is measured, what changes over time, what can be intervened on, and what information may have been left out.

**[See where this fits in the Research Map](docs/research_map.md#chapter-1-what-physical-system-are-we-talking-about)**

### 2. Keep the target independent

If we want to know whether physics explains a distinction related to experience, we should not secretly build that distinction from the same physical variables and then call the match an explanation.

The target needs its own scientific justification.

**[See where this fits in the Research Map](docs/research_map.md#chapter-3-is-the-target-independent-or-did-we-build-the-answer-into-it)**

### 3. Test the measurement and the model

Reports, behavior, labels, and other observations can be incomplete or noisy. A mathematical model can also fit some features of the data while still be wrong.

The research therefore asks whether the observations are trustworthy and whether the proposed model makes constraints that can genuinely fail.

**[See where this fits in the Research Map](docs/research_map.md#chapter-4-can-the-proposed-model-be-wrong)**

### 4. Ask whether the result survives uncertainty

A promising pattern is not enough by itself. Finite data, numerical approximation, model selection, and repeated testing can all create false confidence.

The later work develops ways to make those conclusions auditable and reproducible.

**[See where this fits in the Research Map](docs/research_map.md#chapter-5-does-the-conclusion-survive-uncertainty)**

---

## What has this project built so far?

The repository contains a large mathematical and computational framework for turning the broad question from physics to experience into smaller scientific questions that can be tested separately.

Those results include methods for:

- defining physical structure without depending on arbitrary representation choices;
- asking whether a physical description leaves out a distinction relevant to an independent target;
- checking whether the target and its measurements are scientifically usable;
- testing whether a proposed model can reproduce the observed data;
- controlling uncertainty from finite data and numerical computation;
- making the complete reasoning chain reproducible and auditable.

The public theorem frontier is **P99**. The formal release is **v0.82.0**. The final bridge from physical description to experience remains **open**.

You do not need to read 99 propositions to understand the project.

---

## Choose how deep you want to go

| I want to... | Open this |
| --- | --- |
| See the whole research story without equations | **[Research Map](docs/research_map.md)** |
| Understand the central bridge question more formally | **[Bridge Problem](docs/bridge_problem.md)** |
| Browse the research through figures | **[Figure Catalog](docs/figure_catalog.md)** |
| Move into the formal scientific architecture | **[Technical Research Architecture](docs/research_architecture.md)** |
| See how the mathematical results depend on one another | **[Theorem Roadmap](docs/theorem_roadmap.md)** |
| Read the current frontier result | **[P99](docs/proposition_99_cross_fitted_evalue_aggregation.md)** |
| Inspect every proposition in the complete technical record | **[Detailed Proposition Record](docs/detailed_proposition_record.md)** |
| Trace equations, sources, implementations, and tests | **[Research Navigation](docs/research_navigation.md)** |
| Reproduce the computational work | **[Reproducibility Guide](docs/reproducibility.md)** |

---

## The most important scientific boundary

This repository is building a **test framework**, not announcing that consciousness has been mathematically solved.

A physical model may fail because it is incomplete. A statistical model may fail without telling us which alternative is correct. A latent variable may be useful without being consciousness. A theorem may be correct under assumptions that still need empirical justification.

The final bridge from physical description to experience therefore remains an open question.

That openness is intentional. The purpose of the project is to make the path toward stronger claims more precise, more falsifiable, and easier for other researchers to inspect.

---

## Where to go next

For the best next step, continue to the **[Research Map](docs/research_map.md)**. It explains how the major scientific questions connect without requiring equations or theorem numbers.

When you are ready for the formal structure, continue to **[Technical Research Architecture](docs/research_architecture.md)** or the **[Theorem Roadmap](docs/theorem_roadmap.md)**.

For the full proposition audit trail, open the **[Detailed Proposition Record](docs/detailed_proposition_record.md)**.

For figures first, open the **[Figure Catalog](docs/figure_catalog.md)**.

For code and verification, open the **[Reproducibility Guide](docs/reproducibility.md)**.

### P91 historical mixed-prevalence step

The P91 Research II step is [P91](docs/proposition_91_mixed_prevalence_rank_two_flattening_separation.md). P91 shows that the nonlinear P75 separation is not confined to P90's prevalence-zero face: over the full two-component mixture cube, the established witness obeys the certified bracket `1/42 < d_inf <= 1/24`. The upper endpoint remains a constructive bound rather than a claimed exact optimum.

### P92 historical exact full-cube step

The P92 Research II step is [P92](docs/proposition_92_exact_global_mixed_prevalence_distance.md). P92 closes the P91 mixed-prevalence bracket and proves the exact full-cube result `d_inf(P_emp, M75) = 1/24` through a nonlinear three-minor sign-coherence invariant.

### P93 historical IID finite-sample step

The historical IID finite-sample step is [P93](docs/proposition_93_localized_sign_coherence_rejection.md). P93 takes P92's exact nonlinear sign-coherence obstruction into finite IID data. It needs simultaneous control of only seven observable cells. At 95 percent confidence, the exact mathematical radius crosses between 1622 and 1623 samples; the first exact replication of the original 24-count profile that clears the certificate is 1632 samples. Non-rejection remains inconclusive.

### P94 historical finite-range dependent step

[P94](docs/proposition_94_finite_range_dependent_sign_coherence.md) keeps the seven-cell P92/P93 nonlinear rejection witness but relaxes IID sampling to a declared finite-range dependent sequence with one common marginal four-view law. For dependence range `m`, the squared confidence radius is multiplied by `m+1`. At 95 percent confidence, the established witness crosses at 1623, 3246, and 4869 samples for `m=0,1,2` respectively. An exact temporal-pooling counterexample shows why arbitrary marginal drift is outside the theorem. Non-rejection remains inconclusive, and the physical-to-experiential bridge remains open.

### P95 historical drift-aware stratified rejection

P94 showed why drifting marginals cannot be pooled safely. P95 makes the next valid move: declare regimes before testing, permit a different marginal law in every regime, certify each regime with its own P94 radius and error budget, and reject the all-regimes P75 null if any regime is locally incompatible. [Read P95](docs/proposition_95_drift_aware_stratified_sign_coherence.md).

### P96 previous frontier: selection-valid holdout stratification

P95 requires the regime plan to be fixed independently of the certification witness. P96 closes one precise post-selection gap by allowing arbitrary pilot-data selection of the regime plan, freezing that plan, and then applying P95 to genuinely independent holdout information. Conditional P95 validity integrates to the same unconditional familywise guarantee, so pilot-search complexity itself requires no additional alpha spending under the declared independence assumptions. The pilot data are not reused for certification. [Read P96](docs/proposition_96_selection_valid_holdout_stratification.md).

An ordinary random split of a temporally dependent stream is not automatically an independent holdout design. Same-data redesign remains outside P96.

### P97: simultaneous finite candidate-family selection

P97 addresses that complementary same-data case. A finite family of candidate regime plans is fixed before the certification statistics are inspected. Each candidate receives its own exact P95 familywise budget, and a second union bound across candidates makes all candidate certificates valid simultaneously. The final candidate may then be chosen after seeing the results without invalidating the selected certificate. [Read P97](docs/proposition_97_simultaneous_candidate_family_selection.md).

For two predeclared candidates with two one-step-dependent regimes each, equal spending of a 5 percent global error budget gives a mathematical threshold of 4045 observations per regime and a first exact denominator-24 replication at 4056. P97 pays for same-data search through multiplicity. It does not permit generating a new candidate after inspection, unrestricted within-regime drift, model acceptance after non-rejection, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.


### P98: cross-fitted selection-valid certification

P98 rotates the P96 independent-holdout idea across mutually independent blocks. Each fold may choose its regime plan using the other blocks, but its own certification block is excluded from that selection and is evaluated only after the plan is frozen. The fold certificates are allowed to be dependent; an outer union bound controls their total error budget.

For two folds with two one-step-dependent regimes each, the 95 percent per-regime threshold is 4045 and the first exact denominator-24 replication is 4056. Because the folds are genuinely different certification blocks, the unique totals are 16180 and 16224.

P98 does not make an ordinary split of a dependent time series independent. It does not permit own-fold leakage, unbudgeted cross-fitting search, model acceptance after non-rejection, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge. [Read P98](docs/proposition_98_cross_fitted_selection_valid_certification.md).


### P99: cross-fitted e-value aggregation

P99 extends the P98 cross-fitted design from simultaneous foldwise error spending to exact evidence aggregation. A valid level-`tau` fold rejection becomes the e-value `R(tau)/tau`. Finite calibration mixtures fixed before own-fold evaluation remain e-values, and a fixed convex average across folds remains valid without assuming the fold certificates are independent.

For two folds with two one-step-dependent regimes each, the declared 95 percent distributed-evidence checkpoint crosses at 3774 observations per regime and first reaches an exact denominator-24 replication at 3792. Unique two-fold totals are 15096 and 15168. The gain over P98 is configuration-specific, and neither procedure uniformly dominates the other.

P99 does not justify own-fold leakage, post-hoc calibration search, naive dependent-stream splitting, model acceptance, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge. [Read P99](docs/proposition_99_cross_fitted_evalue_aggregation.md).

### P100: anytime-valid sequential e-process

P100 adds a sequential outer layer to P99. Each new certification round produces a P99 e-value `E_t` that must remain conditionally valid given the completed history. A stake `eta_t` is chosen from past information only, and the factor `F_t = (1 - eta_t) + eta_t E_t` updates the cumulative process `M_t`.

The exact 95 percent checkpoint is intentionally easy to audit: `E_t = 25/2` is not individually decisive; half stake gives `F_t = 27/4`; two fresh rounds give `M_2 = 729/16 = 45.5625 > 20`. The declared two-round unique-data totals are `30192 / 30336`.

The protection is anytime-valid because `M_t` is a nonnegative supermartingale under the declared sequential null and Ville's inequality controls the probability of ever crossing `1 / alpha`. P100 does not permit current-round leakage or reused-data relabeling.

Direct proof: [P100](docs/proposition_100_anytime_sequential_eprocess.md).
