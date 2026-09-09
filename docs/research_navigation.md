# Research Navigation

This page is the reading and reference index for the Mathematical Consciousness Bridge repository. It is designed so that a reader can move from the research question to the theorem chain, proofs, figures, code, empirical boundaries, and references without searching through the repository manually.

## Recommended reading order

1. [Main research paper](../README.md) for the complete scientific narrative and embedded figures.
2. [Bridge problem](bridge_problem.md) for the formal statement of the physical-to-experiential problem.
3. [Theorem roadmap](theorem_roadmap.md) for the dependency structure from P1 through P21.
4. [Equation and citation map](equation_and_citation_map.md) for equation-level provenance and theorem lineage.
5. [Proposition 19](proposition_19_fundamental_physical_sufficiency.md) for the population physical-sufficiency theorem.
6. [Proposition 20](proposition_20_finite_sample_residual_certification.md) for finite-sample certification of the P19 stochastic residual.
7. [Proposition 21](proposition_21_descriptor_refinement_residual_persistence.md) for the omitted-physics refinement audit and residual-persistence theorem.
8. [Fundamental Theory to Consciousness program](fundamental_theory_consciousness_program.md) for the candidate fundamental-state framework.
9. [Stochastic fundamental bridge](stochastic_fundamental_bridge.md) for the conditional-information formulation.
10. [Falsification program](falsification_program.md) for the empirical burden required before any bridge claim can be accepted.
11. [Citation and Reference Policy](citation_and_reference_policy.md) and [Reference Audit](reference_audit.md) for evidence classification and source standards.

## Complete proposition index

| Proposition | Direct proof | Main role |
| --- | --- | --- |
| P1 | [Representation invariance](proposition_1_representation_invariance.md) | bridge objects must descend to the physical quotient |
| P2 | [Bridge identifiability](proposition_2_bridge_identifiability.md) | exact experiment-class discriminability |
| P3 | [Bridge equivalence classes](proposition_3_bridge_equivalence_classes.md) | observable theory quotient |
| P4 | [Discriminating experiment design](proposition_4_discriminating_experiment_design.md) | maximin and set-cover protocol design |
| P5 | [Feature sufficiency](proposition_5_feature_sufficiency.md) | exact factorization through physical features |
| P6 | [Canonical bridge signature](proposition_6_canonical_bridge_signature.md) | canonical completeness target |
| P7 | [Experimental signature recovery](proposition_7_experimental_signature_recovery.md) | exact recoverability criterion |
| P8 | [Robust signature recovery](proposition_8_robust_signature_recovery.md) | finite-error partition recovery |
| P9 | [Categorical sample complexity](proposition_9_categorical_sample_complexity.md) | explicit finite trial requirement |
| P10 | [Robust experiment design](proposition_10_robust_experiment_design.md) | discrimination under nuisance variation |
| P11 | [Intervention-resolved causal structure](proposition_11_intervention_resolved_causal_structure.md) | structured candidate physical signature |
| P12 | [Component insufficiency](proposition_12_component_insufficiency.md) | single-component and scalar no-go results |
| P13 | [Pairwise component irredundancy](proposition_13_pairwise_component_irredundancy.md) | pairwise projection no-go results |
| P14 | [Temporal continuation](proposition_14_temporal_continuation.md) | representation-invariant temporal geometry |
| P15 | [Finite-sample temporal certification](proposition_15_finite_sample_temporal_certification.md) | uncertainty propagation through temporal structure |
| P16 | [Independent composition and coupling](proposition_16_independent_composition_and_coupling.md) | independence null and coupling defect |
| P17 | [Coarse-graining and refinement](proposition_17_coarse_graining_and_refinement.md) | information loss and refinement ambiguity |
| P18 | [Scale sufficiency certification](proposition_18_scale_sufficiency_certification.md) | approximate reconstruction and scale certificate |
| P19 | [Fundamental physical sufficiency](proposition_19_fundamental_physical_sufficiency.md) | deterministic, stochastic, and differential sufficiency tests |
| P20 | [Finite-sample residual certification](proposition_20_finite_sample_residual_certification.md) | confidence interval for the P19 conditional-information residual |
| P21 | [Descriptor refinement and residual persistence](proposition_21_descriptor_refinement_residual_persistence.md) | omitted-physics audit, residual monotonicity, and exact refinement gain |

## Physics, mathematics, and quantitative figures

| Resource | What it contains |
| --- | --- |
| [Quantitative Physics and Mathematics Atlas](quantitative_physics_mathematics_atlas.md) | Q01 through Q40 with equations, numerical checks, and generated figures |
| [Advanced Physics Visual Atlas](advanced_physics_visual_atlas.md) | additional physics maps and equation-focused visual context |
| [Conscious State Measurement Atlas](conscious_state_measurement_atlas.md) | measured signals, derived features, and empirical-state boundaries |
| [Quantitative Atlas Validation Report](quantitative_atlas_validation_report.md) | numerical checkpoints and reproducibility checks |
| [Figure Style Guide](figure_style_guide.md) | publication layout, typography, scale, and interpretation rules |

The quantitative figures are generated by [generate_quantitative_atlas.py](../scripts/generate_quantitative_atlas.py). Quantum-foundations figures are generated by [generate_quantum_foundations_atlas.py](../scripts/generate_quantum_foundations_atlas.py).

## Fundamental theory and consciousness interface

| Resource | Scientific role |
| --- | --- |
| [Fundamental Theory to Consciousness program](fundamental_theory_consciousness_program.md) | common candidate-state framework for geometry, quantum structure, causal structure, and experiential structure |
| [Stochastic fundamental bridge](stochastic_fundamental_bridge.md) | Markov-kernel and conditional-information version of physical sufficiency |
| [P19 fundamental physical sufficiency](proposition_19_fundamental_physical_sufficiency.md) | exact factorization theorem, stochastic criterion, and local rank obstruction |
| [P20 finite-sample residual certification](proposition_20_finite_sample_residual_certification.md) | finite-data confidence certificate for the P19 stochastic residual |
| [P21 descriptor refinement and residual persistence](proposition_21_descriptor_refinement_residual_persistence.md) | nested physical-description audit that quantifies how added physical detail removes or fails to remove the residual |
| [Candidate theory families](candidate_theory_families.md) | source-grounded translations of major consciousness-theory families into a common comparison language |
| [Axiom ledger](axiom_ledger.md) | explicit assumptions and open commitments |

## Evidence, falsification, and references

| Resource | Scientific role |
| --- | --- |
| [Equation and Citation Map](equation_and_citation_map.md) | tells the reader which equations are standard, repository-defined, proved here, or externally motivated |
| [Foundational Physics and Mathematics Bibliography](foundational_physics_mathematics_bibliography.md) | primary physics, mathematics, statistics, and empirical sources |
| [Literature Map](literature_map.md) | consciousness-theory and empirical literature with stated source roles |
| [Fundamental Theory References](fundamental_theory_references.bib) | machine-readable bibliography for the fundamental-theory layer |
| [Reference Audit](reference_audit.md) | evidence-classification audit for high-impact sources |
| [Citation and Reference Policy](citation_and_reference_policy.md) | citation, attribution, DOI, evidence-class, and writing rules |
| [Falsification Program](falsification_program.md) | conditions that would defeat or weaken a proposed bridge claim |

## Implementation and reproducibility

The executable P19 implementation is [fundamental_physical_sufficiency.py](../src/consciousness_bridge/fundamental_physical_sufficiency.py), with regression tests in [test_fundamental_physical_sufficiency.py](../tests/test_fundamental_physical_sufficiency.py) and the publication figure in [p19_fundamental_physical_sufficiency.svg](figures/p19_fundamental_physical_sufficiency.svg). The P20 finite-sample layer is implemented in [finite_sample_residual_certification.py](../src/consciousness_bridge/finite_sample_residual_certification.py), tested in [test_finite_sample_residual_certification.py](../tests/test_finite_sample_residual_certification.py), and summarized by [p20_finite_sample_residual_certificate.svg](figures/p20_finite_sample_residual_certificate.svg). The P21 omitted-physics audit is implemented in [descriptor_refinement_residual.py](../src/consciousness_bridge/descriptor_refinement_residual.py), tested in [test_descriptor_refinement_residual.py](../tests/test_descriptor_refinement_residual.py), and summarized by [p21_descriptor_refinement_residual_persistence.svg](figures/p21_descriptor_refinement_residual_persistence.svg).

The repository-wide test workflow is [test.yml](../.github/workflows/test.yml). Local documentation, figure, and anchor integrity is enforced by [test_document_link_integrity.py](../tests/test_document_link_integrity.py). The quantitative figure generators and tests are linked directly from their atlas pages.

## Interpretation rule

A reader should never infer a stronger claim than the linked source establishes. Standard physics is labeled as standard physics. Repository propositions are labeled as repository results. Empirical findings are labeled as empirical findings. Open bridge claims remain open until their assumptions, measurement models, finite-data bounds, and falsification tests are satisfied.
