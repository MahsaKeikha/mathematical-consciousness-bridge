# Detailed proposition record

## Complete P1 to P84 chronology

This page preserves the proposition-by-proposition development history of the Mathematical Consciousness Bridge research program. It is intentionally separate from the main README so a first-time reader can follow the scientific argument without first learning the internal chronology of the project.

The proposition record is an audit trail, not a substitute for the scientific narrative. For dependency structure, see the [Theorem roadmap](theorem_roadmap.md). For topic-oriented navigation, see [Research navigation](research_navigation.md). For equation provenance and external references, see the [Equation and citation map](equation_and_citation_map.md).

The scientific status rule is strict throughout: a theorem is only a theorem under its declared assumptions, an implementation is not empirical evidence, a simulation is not an ontological result, and the physical-to-experiential bridge remains open unless separately established.

---

## Complete P1 to P84 chronology

Propositions **P1-P10** establish representation invariance, empirical theory identifiability, observational equivalence, discriminating experiment design, feature sufficiency, canonical bridge completeness, experimental recoverability, finite-error recovery, sample complexity, and robust protocol design.

- **P1** establishes representation invariance as a quotient-factorization requirement.
- **P2** gives the bridge-identifiability criterion for declared experiment classes.
- **P3** defines observational bridge-equivalence classes.
- **P4** formulates discriminating experiment design as a maximin/set-cover problem.
- **P5** states exact feature-sufficiency conditions.
- **P6** defines a canonical bridge signature under the declared equivalence structure.
- **P7** gives exact experimental signature-recovery conditions.
- **P8** extends recovery to finite-error robustness.
- **P9** gives categorical finite-sample complexity bounds.
- **P10** makes protocol design robust to declared nuisance variation.

Propositions **P11-P18** turn the physical side into an operational object rather than a static feature list.

- **P11** introduces intervention-resolved causal structure.
- **P12** proves component-insufficiency through projection collisions.
- **P13** strengthens that logic to pairwise component irredundancy.
- **P14** adds temporal continuation in representation-invariant form.
- **P15** certifies temporal structure under finite sampling.
- **P16** distinguishes independent composition from coupling defects.
- **P17** formalizes coarse-graining information loss and refinement ambiguity.
- **P18** supplies a scale-sufficiency reconstruction certificate.

Propositions **P19-P24** define and statistically certify the core physical-sufficiency question.

- **P19** states deterministic, stochastic, and differential physical-sufficiency conditions.
- **P20** adds finite-sample certification of the conditional-information residual.
- **P21** quantifies residual persistence under descriptor refinement.
- **P22** certifies an entire refinement chain under one simultaneous finite-sample event.
- **P23** preserves validity after adaptive descriptor selection.
- **P24** extends that validity to repeated looks and finite stopping times.

Propositions **P25-P37** develop operational scale compatibility.

- **P25-P30** transport directed influence, partition irreducibility, node aggregation, intervention structure, response geometry, and complete P11 structure across reconstruction-controlled scale changes.
- **P31-P34** add intervention, delay, joint operational quotient, and full operational-scale declarations.
- **P35-P37** quantify approximate quotient stability and complete distortion control.

Propositions **P38-P44** form the quantum operational-sufficiency branch.

- **P38** states the quantum operational factorization test and exact non-factorization criterion.
- **P39** adds finite-data quantum non-factorization certification.
- **P40** identifies a regularity obstruction for continuous quantum regions under unrestricted bridge classes.
- **P41** derives an analytic trace-ball uncertainty envelope.
- **P42** converts regular-bridge separation into explicit quantum/target sample complexity.
- **P43-P44** complete the finite-data quantum allocation and operational-certification layer used by the repository's quantum branch.

Propositions **P45-P60** develop adaptive evidence acquisition, graph allocation, stopping, switching, and transition-calibration machinery. This branch concerns how to collect or route evidence efficiently after the scientific witness has been declared.

Propositions **P61-P70** form the downstream calibration and optimization branch.

- **P61** solves exact integer transition calibration.
- **P62** introduces heterogeneous transition costs.
- **P63** gives exact heterogeneous integer calibration.
- **P64** gives a fast heterogeneous approximation with an explicit comparison target.
- **P65** adds lower bounds to heterogeneous calibration.
- **P66** uses residual exact augmentation after the lower-bounded solution.
- **P67** certifies global integer optimality.
- **P68** derives a Lagrangian optimality gap.
- **P69** identifies a dual-optimal multiplier.
- **P70** makes the resulting certificate diagnostic rather than opaque by decomposing the primal-dual gap into interpretable components.

The complete P61-P70 resource-allocation lineage is separately organized in the [Calibration and Optimization Frontier](calibration_optimization_frontier_p61_p70.md).

---

## Target-side methodology and model adequacy: P71-P84

**P71** returns from the downstream calibration branch to the central bridge problem and asks whether the target used in a sufficiency test is scientifically independent of the physical descriptor being tested. [Proposition 71](proposition_71_target_provenance_noncircularity.md) proves that descriptor-derived targets can satisfy the bridge condition by construction, so successful prediction is not automatically independent evidence. Source: [`target_provenance_noncircularity.py`](../src/consciousness_bridge/target_provenance_noncircularity.py). Figure: [P71 target provenance](figures/p71_target_provenance_noncircularity.svg).

**P72** adds the next target-side obligation: the target can be independently justified yet still observed through a noisy measurement channel. [Proposition 72](proposition_72_target_measurement_channel_robustness.md) proves one-way residual transfer, witness attenuation/erasure, target-TV contraction, stability inequalities, and a conservative finite-sample target-separation certificate. Source: [`target_measurement_channel_robustness.py`](../src/consciousness_bridge/target_measurement_channel_robustness.py). Figure: [P72 target measurement channel robustness](figures/p72_target_measurement_channel_robustness.svg).

**P73** closes the population identifiability step for one deliberately restricted binary target-measurement model. [Proposition 73](proposition_73_target_channel_identifiability.md) gives an explicit three-view inversion up to the unavoidable latent-label swap and proves constructively that two views do not generally identify individual channel reliabilities. Source: [`target_channel_identifiability.py`](../src/consciousness_bridge/target_channel_identifiability.py). Figure: [P73 target-channel identifiability](figures/p73_target_channel_identifiability.svg).

**P74** converts the P73 population inversion into a finite-sample confidence certificate. [Proposition 74](proposition_74_finite_sample_target_channel_recovery.md) propagates one simultaneous eight-cell empirical-law event through the nonlinear inversion and introduces a covariance nondegeneracy gate so unstable recovery near the singular set is not reported as reliable. Source: [`finite_sample_target_channel_recovery.py`](../src/consciousness_bridge/finite_sample_target_channel_recovery.py). Figure: [P74 finite-sample target-channel recovery](figures/p74_finite_sample_target_channel_recovery.svg).

**P75** separates target-channel identifiability from target-model adequacy. [Proposition 75](proposition_75_target_model_adequacy_overidentification.md) shows that the three-view binary latent model is generically just-identified, while a fourth binary view creates six generic overidentifying degrees of freedom, observable tetrad/cross-triple constraints, a fourth-centered-moment relation, and a full-law reconstruction audit. Source: [`target_model_adequacy.py`](../src/consciousness_bridge/target_model_adequacy.py). Figure: [P75 target-model adequacy](figures/p75_target_model_adequacy_overidentification.svg).

**P76** converts the tracked P75 population adequacy restrictions into simultaneous finite-sample rejection certificates. [Proposition 76](proposition_76_finite_sample_target_model_adequacy.md) uses one sixteen-cell empirical-law confidence event and denominator-free polynomial constraints. Non-rejection remains inconclusive. Source: [`finite_sample_target_model_adequacy.py`](../src/consciousness_bridge/finite_sample_target_model_adequacy.py). Figure: [P76 finite-sample target-model adequacy](figures/p76_finite_sample_target_model_adequacy.svg).

**P77** closes the finite-data full-law gap left explicit by P76. [Proposition 77](proposition_77_full_law_model_set_separation.md) asks whether the entire empirical-law confidence region is disjoint from the entire declared model family. It makes the lower-bound direction explicit: a candidate best fit is an upper bound on minimum distance and cannot by itself certify rejection. Source: [`full_law_model_set_separation.py`](../src/consciousness_bridge/full_law_model_set_separation.py). Figure: [P77 full-law separation](figures/p77_full_law_model_set_separation.svg).

**P78** supplies the continuous-family optimization certificate required by P77 for the P75 four-view binary latent family. [Proposition 78](proposition_78_certified_continuous_model_separation.md) exploits the model's nine-parameter multi-affine map, computes exact-rational parameter-box enclosures, aggregates them into a certified global L-infinity distance lower bound, and retains explicit model points as upper-bound witnesses. Source: [`certified_continuous_model_separation.py`](../src/consciousness_bridge/certified_continuous_model_separation.py). Figure: [P78 certified continuous-model separation](figures/p78_certified_continuous_model_separation.svg).

**P79** certifies the sampling-radius side of the same rejection inequality. [Proposition 79](proposition_79_certified_sampling_radius.md) uses rational logarithm bracketing and integer-certified dyadic square-root enclosure to guarantee the upper-bound direction required by P77. Source: [`certified_sampling_radius.py`](../src/consciousness_bridge/certified_sampling_radius.py).

**P80** tightens the P78 box relaxation by intersecting exact observed-cell intervals with probability normalization. [Proposition 80](proposition_80_simplex_coupled_model_separation.md) computes the resulting interval-simplex L-infinity relaxation distance exactly and proves the P80 box bound is never weaker than P78. Source: [`simplex_coupled_model_separation.py`](../src/consciousness_bridge/simplex_coupled_model_separation.py).

**P81** adds exact parameter-box ranges for every nonempty projected binary event. [Proposition 81](proposition_81_projection_event_model_separation.md) transfers any event mismatch back to a sound full-law L-infinity lower bound and proves the combined P81 certificate is never weaker than P80. Source: [`projection_event_model_separation.py`](../src/consciousness_bridge/projection_event_model_separation.py).

**P82** restores additional common-parameter information through exact nested projection contrasts. [Proposition 82](proposition_82_exact_nested_projection_contrast.md) audits 256 residual events and provides an exact-rational strict witness improving the declared certificate from `L81 = 1/16` to `L82 = 1/12`. Source: [`nested_projection_contrast_separation.py`](../src/consciousness_bridge/nested_projection_contrast_separation.py).

**P83** adds 22 exact projection-parity observables. [Proposition 83](proposition_83_exact_projection_parity.md) uses the branchwise Bernoulli parity identity, exact multi-affine endpoint extremization, and eight-cell event-mass transfer. Its strict exact-rational witness has `L82 = 0` and `L83 = 1/16`. Source: [`projection_parity_model_separation.py`](../src/consciousness_bridge/projection_parity_model_separation.py). Figure: [P83 exact projection-parity certificate](figures/p83_exact_projection_parity.svg).

**P84** keeps the parameter coupling that P83 still relaxes. [Proposition 84](proposition_84_exact_joint_projection_parity_contrast.md) evaluates signed contrasts between pairs of parity observables using one common endpoint assignment for the shared P75 response coordinates. The standard family contains 220 genuinely coupled contrasts. Every contrast interval is exact over the declared rational parameter box, and the final box certificate is `max(P83, joint-parity)`. An exact-rational strict witness has `L83 = 0` and `L84 = 1/32`, with an empirical contrast `-1/4` outside the exact model interval `[0, 1/2]` and signed support size eight. Source: [`joint_projection_parity_contrast_separation.py`](../src/consciousness_bridge/joint_projection_parity_contrast_separation.py). Tests: [`test_joint_projection_parity_contrast_separation.py`](../tests/test_joint_projection_parity_contrast_separation.py). Provenance: [P84 equation and provenance record](p84_equation_provenance.md). Figure: [P84 exact joint projection-parity contrast certificate](figures/p84_joint_projection_parity_contrast.svg).

---

## Current frontier interpretation

P84 is a strict computational strengthening of the declared P75 model-distance certificate. It demonstrates that separate observable compatibility can be weaker than common-parameter compatibility. It does not identify a parity observable with consciousness, does not establish that the P75 latent state is an experiential state, and does not turn rejection of P75 into evidence that consciousness lies outside physics.

The complete P71-P84 chain is conditional on its declared measurement/model assumptions, and the physical-to-experiential bridge remains open.