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
| P75 model family | The four-view binary latent target-measurement family is the declared model family audited by P75-P86 | repository modeling assumption and definition | P75 proof and implementation; dependencies recorded in [Theorem Roadmap](theorem_roadmap.md) | declaring a model does not establish that its latent state is consciousness |
| P78 continuous separation | Exact parameter-box lower bounds can be constructed for the declared P75 family by exploiting the model's multi-affine structure | repository theorem built from elementary exact mathematics | [P78 proof](proposition_78_certified_continuous_model_separation.md), P78 provenance, implementation, tests | this certifies separation from a declared family only |
| P79 finite-data handoff | A model-distance lower bound can be compared against a separately certified sampling-radius upper bound | repository theorem using standard concentration ingredients | [P79 proof](proposition_79_certified_sampling_radius.md), P79 provenance; Hoeffding source recorded in the equation/citation map | finite-sample rejection is one-sided and does not validate a non-rejected model |
| P83 parity audit | Exact projection-parity observables can reveal incompatibilities not captured by the complete P82 audit | repository theorem with standard binary parity algebra | P83 proof, provenance, implementation, tests, figure | parity is a model diagnostic, not a measure of consciousness |
| P84 pairwise compatibility | Two parity observations may each be compatible separately but incompatible under one shared P75 parameter assignment | repository theorem | [P84 proof](proposition_84_exact_projection_parity_contrast.md), P84 provenance, implementation, tests, figure | pairwise incompatibility rejects the declared family locally; it does not imply a new ontology |
| P85 triple compatibility | Three-event shared-parameter parity functionals can strictly strengthen the complete P84 certificate | repository theorem | [P85 proof](proposition_85_exact_triple_projection_parity_functional.md), [P85 provenance](p85_equation_provenance.md), implementation, tests, figure | the exact witness is synthetic and model-conditional |
| P86 weighted four-event compatibility | A minimally non-uniform four-event parity functional can strictly strengthen the complete P85 certificate | repository theorem | [P86 proof](proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md), [P86 provenance](p86_equation_provenance.md), [`weighted_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/weighted_quad_projection_parity_functional_separation.py), [tests](../tests/test_weighted_quad_projection_parity_functional_separation.py), [figure](figures/p86_exact_minimally_weighted_quad_projection_parity.svg) | `L85 = 0 < L86 = 1/192` is an exact synthetic strict witness inside the declared P75 family |

## P86 mathematical backbone

The P86 proof uses three different kinds of support and keeps them separate.

| Ingredient | Classification | Support |
| --- | --- | --- |
| Binary parity identity | inherited exact algebra inside the P75 conditional-independence model | P83-P85 derivations and [P86 provenance](p86_equation_provenance.md) |
| Multi-affine endpoint extremization | elementary exact derivation | each coordinate enters affinely with all others fixed; repeated one-coordinate endpoint reduction proves that a box extremum occurs at a vertex |
| Affine prevalence extremization | elementary exact derivation | an affine scalar function on an interval attains its extrema at interval endpoints |
| Median minimizes finite absolute-deviation sum | standard finite-dimensional fact, proved locally if needed | [P86 provenance](p86_equation_provenance.md); the slope/subgradient changes sign when the center crosses a median |
| Centered transfer inequality | elementary probability-law identity plus triangle inequality | mass conservation gives `sum_x(p-q)=0`; [P86 proof](proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md) |
| 10,560-functional family | repository-original finite construction | exact combinatorial definition, implementation, and exhaustive regression tests |
| Strict witness `L85 = 0 < L86 = 1/192` | repository-original exact rational construction | exact `Fraction` implementation and exhaustive P85/P86 regression tests |

## Reader-facing status claims

| Claim family | Claim used on the website | Evidence class | Canonical support | Required boundary |
| --- | --- | --- | --- | --- |
| Current theorem count | The current repository contains 86 proposition-level results | repository publication status | theorem roadmap, verifier, reader tests, and current website source | this is a repository count, not an external scientific consensus statement |
| Current frontier | P86 is the current theorem frontier | repository publication status | P86 proof, implementation, tests, provenance, figure, and frontier publication tests | P84 and P85 remain historical certified frontiers, not current ones |
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
