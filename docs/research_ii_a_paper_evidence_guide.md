# Research II-A: journal-paper evidence and verification guide

**Status: submission preparation, not an accepted or independently certified paper.** This guide connects the public Research II theorem record to the proposed manuscript *Falsifiable Physical Sufficiency for Experiential Targets: Non-Circular Provenance, Measurement Robustness, and Finite-Data Certification*. It does not claim empirical access to subjective experience.

## Scope of the paper

The paper's central question is whether a **declared physical descriptor** is sufficient for a **separately defined target**, with target provenance, measurement reliability, and finite-data error controlled explicitly. It does not imply that rejecting one descriptor rejects all physical explanations.

| Obligation | Primary source | What the claim requires |
|---|---|---|
| Deterministic factorization and finite stochastic screening-off | [P19](proposition_19_fundamental_physical_sufficiency.md) | Declared descriptor, independent target, and finite joint law for the conditional-information result |
| Finite-sample residual certificate | [P20](proposition_20_finite_sample_residual_certification.md) | IID observations, declared finite alphabets, prespecified error rate |
| Target-provenance non-circularity | [P71](proposition_71_target_provenance_noncircularity.md) | Target construction not derived from the descriptor whose sufficiency is being tested |
| Nondifferential target-observation channel | [P72](proposition_72_target_measurement_channel_robustness.md) | Observed target conditionally independent of underlying state given latent target and descriptor |
| Three-view binary latent identification | [P73](proposition_73_target_channel_identifiability.md) | Three conditionally independent binary views, interior prevalence, nonzero loadings |
| Finite-sample channel recovery | [P74](proposition_74_finite_sample_target_channel_recovery.md) | IID eight-cell sampling and a strict nondegeneracy certification gate |
| Target-model adequacy | [P75](proposition_75_target_model_adequacy_overidentification.md), [P76](proposition_76_finite_sample_target_model_adequacy.md) | Recovery/identifiability must not be confused with empirical model fit; cite as downstream context only unless included explicitly |

## Exact toy example (not participant data)

Let the underlying state be two independent fair bits, `Ω=(A,B)`, the declared physical descriptor `T=A`, and an independently specified target `E=B`. The conditional information residual is `I(E;Ω|T)=1 bit`, so **this particular T** is insufficient for E. If the observed target `Y=B XOR N`, where independent binary reporting noise has probability `P(N=1)=0.2`, then `I(Y;Ω|T)=1-h₂(0.2)≈0.278072 bits`. If the target were instead manufactured as `E=T`, then the residual is zero by construction and is not independent evidence for sufficiency.

These are population identities under the specified distribution, not sample results, human measurements, or findings about the ontology of consciousness.

## Explicit limits for journal claims

- **Theory:** Factorization, conditional independence, channel contraction, and finite-data bounds have different assumptions and must not be conflated.
- **Measurement:** A recovered latent class is a statistical construct, not an independently established experiential ground truth.
- **Evidence:** A numerical example or successful regression test checks an implementation or theorem example; it does not validate psychological construct interpretation.
- **Selection:** The manuscript must not claim unrestricted adaptive or anytime validity based on the IID certificate; see the distinct later P95-P100 program in the [research map](research_map.md).
- **Reproducibility:** See [reproducibility instructions](reproducibility.md). The instructions are not a report that all checks passed on a particular date.

## Submission audit checklist

1. Check all displayed equations and proof dependencies against the six theorem records above.
2. Recompute P20 and P74 numeric checkpoints with exact sample sizes, alphabets, logs, and rounding.
3. Verify the manuscript's references against primary bibliographic records and contextualize novelty rather than claiming standard concentration or data-processing tools as newly invented.
4. Match main manuscript figures, supplements, and tests to a pinned source revision.
5. Check all author-identifying metadata and repository URLs against the journal's double-blind review instructions.
6. Keep Research II-B and II-C principal novelty in their companion papers.

This page is a **paper-facing audit index**, not a replacement for the formal proposition records.

## Journal positioning check (2026-10-20)

The revised manuscript now explicitly separates standard mathematics from the proposed methodological integration. Conditional mutual information, factorization, entropy continuity, and classical latent identification are not claimed as individually new. The psychological contribution is a prespecified testing workflow joining independent target provenance, observation-model reliability, adequacy, and sampling uncertainty. Five threats must be evaluated before extrapolating synthetic results: correlated view errors, differential measurement, dependent or drifting samples, conservative high-dimensional bounds, and unchecked model selection.

The working blinded manuscript contains **25 references and six figures**. Pagination depends on its rendered submission version. Rendering was performed, but independent external mathematical peer review and complete source-test reproducibility remain outstanding. No acceptance claim is made.


## Manuscript figure gallery

The website's [Research II-A evidence page](../website/research-ii-paper.html) displays six purpose-built SVG figures in `website/figures/research-ii-a/`, following the same six conceptual topics and numbering as the working manuscript. The vector diagrams are independently redrawn for accessibility and high-resolution browser rendering; the manuscript itself contains separately rendered publication figures. No proof or empirical claim is made by a diagram alone. Review the source proposition records before citing the figures as evidence.

## Submission-stage methodological clarification (October 2026)

The current reviewer-strengthened draft clarifies three interpretive boundaries:

1. **Non-rejection is not sufficiency.** A lower confidence bound that does not exceed zero is inconclusive about the descriptor. An affirmative bounded equivalence statement requires a prespecified tolerance, an appropriate upper bound and independent construct validity.
2. **Two synthetic experiments test different objects.** Residual-certificate frequencies are not the same as the three-view covariance nondegeneracy-gate passage frequencies. Neither establishes empirical psychological validity or general coverage under model misspecification.
3. **Uniform guarantees have defined scope.** Shared base-law events protect admissible deterministic descriptor pushforwards for a declared target and finite IID model; they do not automatically protect newly selected targets, dependent recordings, arbitrary learned observation channels or distribution shift.

These notes are a documentation alignment with the manuscript's claims, not a report of independent proof verification or new participant evidence. For the journal manuscript, source proposition identifiers should stay out of the reader-facing figures and prose; these identifiers remain here for traceability.

## Next validation gate

Before treating the reviewer-strengthened draft as submission-final, reproduce the binary information-certificate and three-view covariance-gate experiments from archived source code, verify the full proof appendix against manuscript assumptions, and confirm the psychological sampling units. The manuscript's illustrative visual-detection design is proposed rather than conducted, and repeated within-subject neural trials do not become IID merely by randomizing trial order. Report this limitation in both manuscript and study preregistration.

## Fixed-time and repeated-look reporting check

The manuscript's theorem statements must distinguish a fixed-n base-law confidence event from an error-spent simultaneous sequence. For a declared alpha, the allocation alpha_n = 6 alpha / (pi^2 n^2) sums to alpha over positive integer n. A countable union bound then provides a simultaneous event, supporting inspections at an almost surely finite data-dependent stopping time only within the fixed finite-alphabet IID sampling model. The conclusion is not a generic confidence-sequence result for dependent trials, drifting distributions, newly constructed targets or arbitrary adaptive observation channels. This is a clarification of a standard proof mechanism, not a novel sequential-inference theorem.

## Three-view inversion boundary (manuscript verification, October 2026)

In one fixed physical stratum, assume a binary latent target with interior prevalence and three conditionally independent binary observation views with nonzero loadings. The population identities are `C_ij = b_i b_j (1-m^2)` and `M_123 = -2m(1-m^2)b_1b_2b_3`. Consequently `C_12 C_13 C_23 > 0` and `q = M_123^2/(C_12 C_13 C_23) = 4m^2/(1-m^2)`. An observed zero third centered moment is compatible with a balanced latent state (`m=0`); it does not by itself invalidate identification. A zero pair covariance invalidates the nondegenerate moment inversion, and a covariance sign pattern with negative product challenges the declared model. The finite-sample covariance gate remains a sufficient refusal criterion, not an empirical validation of conditional independence, construct interpretation, or parameter-orbit coverage under model violations.

This audit reconciles the manuscript interpretation with [the three-view proposition](proposition_73_target_channel_identifiability.md) and [the finite-sample recovery proposition](proposition_74_finite_sample_target_channel_recovery.md). The reviewer-strengthened manuscript remains a draft, not an independently peer-certified mathematical result.

## Eight-cell concentration and certification audit (22 October 2026)

For IID triples within one prespecified stratum, the eight empirical cell proportions admit the simultaneous cellwise Hoeffding radius `epsilon_n = sqrt(log(16/alpha)/(2n))` with probability at least `1-alpha`. The implied L1 bound is `delta_n = min(2, 8*epsilon_n)`. Under that common event, a conservative bound for every first moment is `delta_n`; for every pair covariance it is `3*delta_n`; and for the third centered moment it is `13*delta_n`. These constants follow from expansion in raw bounded moments and triangle inequalities and are not claimed optimal. Recovery must refuse to invert unless all three pair-covariance intervals exclude zero and their sign product is compatible with the positive product implied by the assumed nondegenerate binary three-view latent model. This is a conditional finite-sample statement, not an independent empirical model-fit test. It does not cover data-dependent stratum or target selection without additional simultaneous calibration.

The revised paper states the finite-sample certificate in reader-facing terms without internal proposition numbers. The repository retains provenance and formal proof records. Mathematical review of every appendix lemma and full simulation replication remain separate outstanding checks.

## Manuscript Version 9: moment-error bound audit

The manuscript now spells out the raw-moment expansion underlying the conservative `delta_n`, `3 delta_n`, and `13 delta_n` simultaneous mean, pair-covariance, and third-centered-moment bounds. The common eight-cell probability event is the only claimed source of joint coverage. Failed nondegeneracy certification is a refusal to invert, not evidence that the target is absent. These are source-alignment checks, not a substitute for independent external proof review or full empirical validation.
