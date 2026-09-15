# Claim-to-Source Scientific Audit Matrix

This matrix is the reader-facing audit layer for consequential scientific claims in the Mathematical Consciousness Bridge project. Its purpose is to make the support structure explicit: what is externally established, what is repository-original, what is a declared modeling assumption, and what remains open.

A claim is not strengthened by adding an unrelated citation. The citation or local proof record must support the exact role assigned to it.

## Core project claims

| Claim family | Claim used in the project | Evidence class | Canonical support | Required boundary |
| --- | --- | --- | --- | --- |
| Research origin | The earliest conceptual line that grew into this project began while studying Max Tegmark's *Consciousness as a State of Matter* | intellectual provenance | Tegmark 2015, DOI [10.1016/j.chaos.2015.03.014](https://doi.org/10.1016/j.chaos.2015.03.014), [arXiv:1401.1219](https://arxiv.org/abs/1401.1219); [Literature Map](literature_map.md) | the later proposition sequence has its own assumptions, derivations, and reproducibility record |
| Formal consciousness modeling | A rigorous consciousness theory should make its physical and experiential mathematical objects explicit | external methodological background plus repository formulation | Kleiner 2020; Kleiner and Tull 2020/2021 in [Literature Map](literature_map.md); [Equation and Citation Map](equation_and_citation_map.md) | these sources provide methodological context; repository bridge hypotheses are evaluated through their own stated assumptions and tests |
| Theory comparison | Consciousness theories can be compared through explicit predictions and adversarial empirical tests | external review and empirical background | Seth and Bayne 2022; Cogitate Consortium et al. 2025 in [Literature Map](literature_map.md) and [Reference Audit](reference_audit.md) | theory comparison does not select a theory by literature count |
| Physical formalism | Quantum, information-theoretic, thermodynamic, probabilistic, and causal tools used here are physical or mathematical formalisms, not direct identities with consciousness | established external mathematics and physics | [Foundational physics and mathematics bibliography](../foundational_physics_mathematics.bib); [Physics equation provenance](physics_equation_provenance.md) | physical description alone does not supply the physical-to-experiential bridge |
| Empirical neuroscience | Neural, perturbational, behavioral, or physiological measurements may constrain consciousness theories | external empirical evidence | [Empirical consciousness measurement bibliography](../empirical_consciousness_measurement.bib); P11 motivation map in [Equation and Citation Map](equation_and_citation_map.md) | correlations or perturbational effects are not by themselves bridge sufficiency |

## Repository theorem chain

| Claim family | Claim used in the project | Evidence class | Canonical support | Required boundary |
| --- | --- | --- | --- | --- |
| P75 model family | The four-view binary latent target-measurement family is the declared model family audited by P75-P91 | repository modeling assumption and definition | P75 proof and implementation; dependencies recorded in [Theorem Roadmap](theorem_roadmap.md) | declaring a model does not establish that its latent state is consciousness |
| P78 continuous separation | Exact parameter-box lower bounds can be constructed for the declared P75 family by exploiting the model's multi-affine structure | repository theorem built from elementary exact mathematics | [P78 proof](proposition_78_certified_continuous_model_separation.md), P78 provenance, implementation, tests | this certifies separation from a declared family only |
| P79 finite-data handoff | A model-distance lower bound can be compared against a separately certified sampling-radius upper bound | repository theorem using standard concentration ingredients | [P79 proof](proposition_79_certified_sampling_radius.md), P79 provenance; Hoeffding source recorded in the equation/citation map | finite-sample rejection is one-sided and does not validate a non-rejected model |
| P83 parity audit | Exact projection-parity observables can reveal incompatibilities not captured by the complete P82 audit | repository theorem with standard binary parity algebra | P83 proof, provenance, implementation, tests, figure | parity is a model diagnostic, not a measure of consciousness |
| P84 pairwise compatibility | Two parity observations may each be compatible separately but incompatible under one shared P75 parameter assignment | repository theorem | [P84 proof](proposition_84_exact_projection_parity_contrast.md), P84 provenance, implementation, tests, figure | pairwise incompatibility rejects the declared family locally; it does not imply a new ontology |
| P85 triple compatibility | Three-event shared-parameter parity functionals can strictly strengthen the complete P84 certificate | repository theorem | [P85 proof](proposition_85_exact_triple_projection_parity_functional.md), [P85 provenance](p85_equation_provenance.md), implementation, tests, figure | the exact witness is synthetic and model-conditional |
| P86 weighted four-event compatibility | A minimally non-uniform four-event parity functional can strictly strengthen the complete P85 certificate | repository theorem | [P86 proof](proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md), [P86 provenance](p86_equation_provenance.md), [`weighted_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/weighted_quad_projection_parity_functional_separation.py), [tests](../tests/test_weighted_quad_projection_parity_functional_separation.py), [figure](figures/p86_exact_minimally_weighted_quad_projection_parity.svg) | `L85 = 0 < L86 = 1/192` is an exact synthetic strict witness inside the declared P75 family |
| P87 bounded primitive four-event compatibility | Completing every nonzero primitive four-event coefficient vector with `|c_i| <= 2` can strictly strengthen the complete P86 certificate | repository theorem | [P87 proof](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md), [P87 provenance](p87_equation_provenance.md), [`bounded_primitive_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py), [tests](../tests/test_bounded_primitive_quad_projection_parity_functional_separation.py), [figure](figures/p87_exact_bounded_primitive_quad_projection_parity.svg) | `L86 = 1/192 < L87 = 1/96` is an exact synthetic strict witness inside the declared P75 family |
| P88 radius-three bounded primitive four-event compatibility | Completing every nonzero primitive four-event coefficient vector with `|c_i| <= 3` can strictly strengthen the complete P87 certificate at the same four-event order | repository theorem | [P88 proof](proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md), [P88 provenance](p88_equation_provenance.md), [`radius_three_bounded_primitive_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/radius_three_bounded_primitive_quad_projection_parity_functional_separation.py), [tests](../tests/test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py), [figure](figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg) | `L87 = 1/96 < L88 = 1/64` is an exact synthetic strict witness inside the declared P75 family; it does not identify consciousness or establish nonphysicality |

## Exact parity-certificate backbone

The P86-P88 exact-certificate sequence uses several different kinds of support and keeps them separate.

| Ingredient | Classification | Support |
| --- | --- | --- |
| Binary parity identity | inherited exact algebra inside the P75 conditional-independence model | P83-P88 derivations and proposition-level provenance records |
| Multi-affine endpoint extremization | elementary exact derivation | each coordinate enters affinely with all others fixed; repeated one-coordinate endpoint reduction proves that a box extremum occurs at a vertex |
| Affine prevalence extremization | elementary exact derivation | an affine scalar function on an interval attains its extrema at interval endpoints |
| Median minimizes finite absolute-deviation sum | standard finite-dimensional fact, proved locally if needed | [P86 provenance](p86_equation_provenance.md); the slope/subgradient changes sign when the center crosses a median |
| Centered transfer inequality | elementary probability-law identity plus triangle inequality | mass conservation gives `sum_x(p-q)=0`; P86-P88 proposition proofs |
| 10,560-functional P86 family | repository-original finite construction | exact combinatorial definition, implementation, and exhaustive regression tests |
| 39,600-functional P87 family | repository-original finite construction | complete sign-normalized primitive coefficient family with magnitude at most two, exact implementation, and exhaustive tests |
| 208,560-functional P88 family | repository-original finite construction | complete sign-normalized primitive coefficient family with magnitude at most three, exact implementation, and exhaustive tests |
| Strict hierarchy `L85 = 0 < L86 = 1/192 < L87 = 1/96 < L88 = 1/64` | repository-original exact rational construction | exact `Fraction` implementations and exhaustive P85-P88 regression tests |

## Reader-facing status claims

Historical P91 publication snapshot: the statements "The current repository contains 91 proposition-level results" and "P91 is the current Research II theorem frontier" are preserved here only as provenance for the P91 public snapshot. The live repository status is 95 proposition-level results with P95 as the current frontier.


| Claim family | Claim used on the website | Evidence class | Canonical support | Required boundary |
| --- | --- | --- | --- | --- |
| Current theorem count | The current repository contains 96 proposition-level results | repository publication status | theorem roadmap, verifier, reader tests, and current website source | this is a repository count, not an external scientific consensus statement |
| Current frontier | P95 is the current Research II theorem frontier | repository publication status | [P95 proof](proposition_95_drift_aware_stratified_sign_coherence.md), [P95 provenance](p95_equation_provenance.md), implementation, exact tests, canonical figure, and frontier publication tests | P94 and earlier propositions remain historical certified frontiers, not current ones |
| Reproducibility | Mature computational claims are expected to be reproducible from source, tests, figures, and pinned reference environment | repository process claim | CI, reproducibility workflow, figure synchronization, verifier | passing CI supports internal consistency and reproducibility; it is not external peer review |
| Scientific boundary | The repository does not currently claim to have solved the physical-to-experiential bridge | repository scope statement | explicit boundaries in theorem documents, website, and [Claim, Evidence, and Citation Standard](claim_evidence_standard.md) | this is a statement about what this project establishes, not a universal impossibility theorem |

## Publication rule

Before a consequential claim is promoted to the public website, at least one of the following must be true:

1. it is an externally established result with an appropriate primary or authoritative scholarly citation;
2. it is a repository theorem with assumptions, proof, implementation where applicable, tests, and provenance;
3. it is a declared assumption or definition and is labeled as such;
4. it is a generated or synthetic result with a reproducible construction;
5. it is an open question and is explicitly labeled unresolved.

If a statement does not fit one of these classes, it should not be presented as an established scientific claim.

| P89 complete linear parity duality | Every real linear functional of the eleven canonical parity coordinates is bounded by the finite P89 primal/dual certificate; the strict witness optimum is exactly 5/168 | repository theorem | [P89 proof](proposition_89_complete_linear_parity_duality.md), [P89 provenance](p89_equation_provenance.md), implementation/tests, [P89 figure](figures/p89_complete_linear_parity_duality.svg) | Complete only for the declared linear parity-functional class; no consciousness identification or nonphysicality claim |

| P90 nonlinear rank-one separation | The strict P75 box has exact full-law L-infinity distance 5/72 from the established empirical witness | repository theorem | [P90 proof](proposition_90_exact_nonlinear_rank_one_separation.md), [P90 provenance](p90_equation_provenance.md), implementation/tests, [P90 figure](figures/p90_exact_nonlinear_rank_one_separation.svg) | Exact only for the declared strict single-component box; no consciousness identification or nonphysicality claim |

| P91 mixed-prevalence rank-two flattening separation | Every P75 law has rank at most two under the declared bipartite flattening; the established empirical witness is farther than `1/42` from the full family and one mixed rational P75 point lies at `1/24`. | Repository-original conditional theorem built from standard rank algebra plus exact rational certification. | [proposition_91_mixed_prevalence_rank_two_flattening_separation.md](proposition_91_mixed_prevalence_rank_two_flattening_separation.md); [p91_equation_provenance.md](p91_equation_provenance.md); `../src/consciousness_bridge/mixed_prevalence_rank_two_flattening_separation.py`; `../tests/test_mixed_prevalence_rank_two_flattening_separation.py` | Do not report `1/24` as the exact global optimum. Do not identify the latent state with consciousness or infer nonphysicality. |

| P92 exact global mixed-prevalence distance | The established empirical witness has exact full-cube P75 L-infinity distance `1/24`. | Repository-original conditional theorem using an elementary two-rank-one determinant identity plus exact rational sign-stability certification. | [proposition_92_exact_global_mixed_prevalence_distance.md](proposition_92_exact_global_mixed_prevalence_distance.md); [p92_equation_provenance.md](p92_equation_provenance.md); `../src/consciousness_bridge/exact_global_mixed_prevalence_distance.py`; `../tests/test_exact_global_mixed_prevalence_distance.py` | Do not identify the latent state with consciousness or infer nonphysicality from model separation. |

| P93 localized finite-sample sign-coherence rejection | A negative empirical P92 determinant-sign product plus a certified seven-cell sampling radius below every empirical sign-stability radius rejects the P75 family at confidence at least `1-alpha`. | Repository-original conditional theorem built from standard concentration, P92 sign stability, and P79 exact numerical certification. | [proposition_93_localized_sign_coherence_rejection.md](proposition_93_localized_sign_coherence_rejection.md); [p93_equation_provenance.md](p93_equation_provenance.md); `../src/consciousness_bridge/localized_sign_coherence_rejection.py`; `../tests/test_localized_sign_coherence_rejection.py` | Do not report 1623 as a universal sample-size requirement or treat non-rejection as model acceptance. |

| P94 finite-range dependent rejection | Under one common marginal law and declared m-dependence, the P92/P93 seven-cell rejection gate has squared radius `(m+1) log(14/alpha)/(2n)`; arbitrary temporal pooling is not covered | repository theorem with established concentration ingredients | [P94 proof](proposition_94_finite_range_dependent_sign_coherence.md), [P94 provenance](p94_equation_provenance.md), exact tests |

P95 drift-aware stratified sign-coherence rejection: predeclared regime-specific P94 confidence events with exact error allocation are combined by a familywise union bound. The theorem permits marginal drift across regimes but not data-dependent segmentation without additional selection accounting. Formal record: [proposition_95_drift_aware_stratified_sign_coherence.md](proposition_95_drift_aware_stratified_sign_coherence.md) and [p95_equation_provenance.md](p95_equation_provenance.md).

| P95 drift-aware stratified rejection | Predeclared regime-specific P94 confidence events can be combined with exact error allocation to reject the joint null that every regime-specific marginal belongs to P75 while allowing arbitrary marginal changes between regimes | repository theorem using P92-P94 geometry, P79 certified logarithms, standard concentration, and a familywise union bound | [P95 proof](proposition_95_drift_aware_stratified_sign_coherence.md), [P95 provenance](p95_equation_provenance.md), implementation, tests, figure | Boundaries and budgets must be predeclared; non-rejection is inconclusive; data-dependent segmentation, consciousness identification, nonphysicality, and a completed physical-to-experiential bridge are not established |

| P96 selection-valid holdout stratification | A pilot-selected regime plan may be certified with the P95 familywise guarantee without an extra pilot-search alpha penalty when the plan is frozen before evaluation on genuinely independent holdout information satisfying the selected local assumptions. | Repository-original synthesis of standard conditional/sample-splitting logic with the P92-P95 chain | `docs/proposition_96_selection_valid_holdout_stratification.md`, `docs/p96_equation_provenance.md`, exact implementation and tests | Independence and frozen-plan assumptions are essential; naive splitting of a dependent stream and same-data redesign are not covered; non-rejection is not acceptance and no consciousness ontology follows. |


### P97 current frontier

| Claim | Evidence class | Canonical source |
| --- | --- | --- |
| A finite candidate family fixed before inspection can support same-data post-inspection selection when all candidate P95 certificates are made simultaneous | Theorem under declared assumptions | [`proposition_97_simultaneous_candidate_family_selection.md`](proposition_97_simultaneous_candidate_family_selection.md) |
| Two candidates, two regimes, `m=1`, equal 5 percent global spending cross at 4045 per regime and first exact replicate at 4056 | Exact rational computation | [`test_simultaneous_candidate_family_selection.py`](../tests/test_simultaneous_candidate_family_selection.py) |
| P97 does not validate newly generated post-inspection candidates or establish consciousness ontology | Scientific boundary | [`p97_equation_provenance.md`](p97_equation_provenance.md) |


### P98 current frontier

| Claim | Evidence class | Canonical source |
| --- | --- | --- |
| Mutually independent blocks can rotate between selection and certification when each fold excludes its own certification block from its own plan selection | Theorem under declared assumptions | [`proposition_98_cross_fitted_selection_valid_certification.md`](proposition_98_cross_fitted_selection_valid_certification.md) |
| Two folds, two regimes, `m=1`, equal 5 percent global spending give 4045/4056 per regime and 16180/16224 unique observations | Exact rational computation | [`test_cross_fitted_selection_valid_certification.py`](../tests/test_cross_fitted_selection_valid_certification.py) |
| P98 does not validate dependent-stream pseudo-folds, own-fold leakage, or a consciousness ontology | Scientific boundary | [`p98_equation_provenance.md`](p98_equation_provenance.md) |


## P99 cross-fitted e-value aggregation

| Claim | Evidence role | Support | Boundary |
| --- | --- | --- | --- |
| A valid level-`tau` fold rejection gives `R(tau)/tau` with null expectation at most one | Standard probability / e-value construction | Vovk and Wang (2021); P96 fold validity | Requires fold test validity at the declared level |
| Fixed convex averages of fold e-values remain e-values without fold independence | Standard e-value merging by averaging | Vovk and Wang (2021); linearity of expectation | Weights must be fixed independently of certification outcomes |
| P99 integrates this construction with cross-fitted P96/P98 certification and exact rational thresholds | Repository-original integration | P99 proof, implementation, tests, provenance | Does not claim invention of e-values or averaging |
| Balanced distributed-evidence crossing is 3774 per regime with exact replication 3792 | Repository-original exact computation | P99 implementation and regression tests | Configuration-specific, not a universal sample-complexity theorem |
| P99 does not uniformly dominate P98 | Repository-original comparison statement | P99 exact examples | Sparse and distributed evidence can favor different procedures |
