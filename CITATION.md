# How to Cite This Research

The **Mathematical Consciousness Bridge** is an ongoing mathematical-physics research program by **Mahsa Keikha, PhD**. It develops a falsifiable test architecture for the physical-to-experiential bridge problem, with theorem-level derivations, numerical figures, executable implementations, and explicit scientific-status boundaries.

If this research program, one of its propositions, figures, algorithms, or implementations contributes to your work, please cite it. When a specific proposition or artifact is central to your use, cite both the overall research program and the specific proposition or artifact.

## Preferred scholarly citation

> Keikha, M. (2026). *Mathematical Consciousness Bridge: A Mathematical-Physics Test Architecture for the Physical-to-Experiential Bridge Problem* (Version 0.82.0). GitHub research repository. https://github.com/MahsaKeikha/mathematical-consciousness-bridge

This is the preferred citation for the research program at the current documented theorem frontier, **P84**.

## BibTeX

```bibtex
@misc{keikha2026mathematicalconsciousnessbridge,
  author       = {Keikha, Mahsa},
  title        = {Mathematical Consciousness Bridge: A Mathematical-Physics Test Architecture for the Physical-to-Experiential Bridge Problem},
  year         = {2026},
  version      = {0.82.0},
  howpublished = {GitHub research repository},
  url          = {https://github.com/MahsaKeikha/mathematical-consciousness-bridge},
  note         = {Ongoing research program. Current documented theorem frontier: P84.}
}
```

A machine-readable BibTeX record is maintained in [`CITATION.bib`](CITATION.bib), and GitHub-compatible metadata are maintained in [`CITATION.cff`](CITATION.cff).

## Citing a specific proposition

For theorem-level attribution, cite the research program and identify the proposition explicitly. A recommended form is:

> Keikha, M. (2026). Proposition PXX, "Proposition title." In *Mathematical Consciousness Bridge: A Mathematical-Physics Test Architecture for the Physical-to-Experiential Bridge Problem* (Version 0.82.0). GitHub research repository. Direct proposition URL.

Replace `PXX`, the title, and the URL with the proposition actually used. The [Detailed Proposition Record](docs/detailed_proposition_record.md), [Theorem Roadmap](docs/theorem_roadmap.md), and [Research Navigation](docs/research_navigation.md) provide titles, dependency structure, implementations, and direct proof links.

### Target-side and continuous-family methods

- Cite [P71](docs/proposition_71_target_provenance_noncircularity.md) for descriptor-derived target circularity and non-circular target provenance.
- Cite [P72](docs/proposition_72_target_measurement_channel_robustness.md) for noisy-target residual transfer, witness attenuation/erasure, and target-channel stability.
- Cite [P73](docs/proposition_73_target_channel_identifiability.md) for the three-view binary latent-target population inversion and two-view non-identifiability boundary.
- Cite [P74](docs/proposition_74_finite_sample_target_channel_recovery.md) for finite-sample target-channel recovery and the covariance nondegeneracy gate.
- Cite [P75](docs/proposition_75_target_model_adequacy_overidentification.md) for four-view overidentification, adequacy constraints, and full-law reconstruction.
- Cite [P76](docs/proposition_76_finite_sample_target_model_adequacy.md) for finite-data inadequacy rejection based on simultaneous sixteen-cell uncertainty.
- Cite [P77](docs/proposition_77_full_law_model_set_separation.md) for full-law confidence-region separation from the complete declared model set and the requirement for a certified distance lower bound.
- Cite [P78](docs/proposition_78_certified_continuous_model_separation.md) for exact-rational multi-affine box enclosures, global branch-and-bound, and the P77 continuous-family rejection handoff.
- Cite [P79](docs/proposition_79_certified_sampling_radius.md) for the exact-rational one-sided sampling-radius upper certificate.
- Cite [P80](docs/proposition_80_simplex_coupled_model_separation.md) for probability-simplex coupling of P78 cell intervals and the never-weaker P80 box lower bound.
- Cite [P81](docs/proposition_81_projection_event_model_separation.md) for exact projected-event box intervals and event-mass transfer to full-law L-infinity distance.
- Cite [P82](docs/proposition_82_exact_nested_projection_contrast.md) for 256 exact nested residual-event intervals and the strict `1/12` versus `1/16` witness.
- Cite [P83](docs/proposition_83_exact_projection_parity.md) for 22 exact projection-parity observables and the strict `L82 = 0 < L83 = 1/16` witness.
- Cite [P84](docs/proposition_84_exact_joint_projection_parity_contrast.md) for 220 genuinely coupled projection-parity contrasts, exact common-endpoint extremization under shared P75 response parameters, and the strict `L83 = 0 < L84 = 1/32` witness.

For P84 equation-level attribution, also cite the [P84 equation and provenance record](docs/p84_equation_provenance.md). The executable implementation is [`src/consciousness_bridge/joint_projection_parity_contrast_separation.py`](src/consciousness_bridge/joint_projection_parity_contrast_separation.py), with regression tests in [`tests/test_joint_projection_parity_contrast_separation.py`](tests/test_joint_projection_parity_contrast_separation.py).

## Citing a figure, algorithm, or implementation

When a figure, numerical result, or implementation is used directly, include the repository citation and identify the artifact by repository path or proposition number. The [Equation and Citation Map](docs/equation_and_citation_map.md), [Complete Figure Catalog](docs/figure_catalog.md), and [Visual Atlas](website/visual-atlas.html) connect equations and figures to assumptions, proofs, source files, and tests.

For example:

> Keikha, M. (2026). Figure or implementation associated with Proposition PXX. *Mathematical Consciousness Bridge* (Version 0.82.0). GitHub research repository. Direct artifact URL.

For the current frontier visual, cite [P84 joint projection-parity contrast certificate](docs/figures/p84_joint_projection_parity_contrast.svg) together with the P84 proposition.

## Version-specific reproducibility

This repository is an evolving research program. For reproducible scholarly use:

1. Cite the documented version used in your analysis.
2. Record the exact Git commit SHA when results depend on a particular repository state.
3. Cite the individual proposition or artifact when your argument depends on a specific theorem, figure, algorithm, or test.
4. Do not attribute later propositions or later numerical results to an earlier repository state.

The current citation metadata identify Version **0.82.0** and theorem frontier **P84**. The release version and theorem frontier are intentionally tracked as separate concepts: theorem development can advance before the next formal release is cut, but public metadata must agree on both.

## DOI and archival status

No DOI is currently asserted for this repository. A DOI should be added to the preferred citation only after an archival service has actually issued one for a versioned release. Until then, the GitHub repository URL, documented version, and exact commit SHA provide the appropriate citation and reproducibility path.

Once an archival DOI exists, it should be added consistently to:

- [`CITATION.cff`](CITATION.cff)
- [`CITATION.bib`](CITATION.bib)
- this citation guide
- the citation section of the main [`README.md`](README.md)

## Scientific attribution and scope

Citation of this work should preserve its scientific status. The repository establishes a mathematical and computational **test architecture** for physical-to-experiential bridge claims under explicit assumptions. It does not presently claim that the final physical-to-experiential bridge has been derived, that consciousness has been identified with a scalar or state of matter, or that quantum mechanics has been shown to be incomplete.

P71-P74 protect target provenance and target measurement. P75-P77 separate target-channel identifiability from model adequacy and then define a full-law finite-data rejection standard. P78-P84 progressively tighten the certified continuous-family separation side while preserving the one-sided interpretation of rejection.

P84's new statement is specifically about **shared-parameter compatibility**. Separate P83 parity probabilities can each lie inside their exact box ranges even when their signed contrast is outside the exact range attainable by one common P75 response-parameter assignment. The exact strict witness has `L83 = 0` and `L84 = 1/32`. This strengthens rejection of one declared statistical model family. It is not evidence that the latent state is consciousness and is not evidence that experience lies outside physics.

Non-rejection remains inconclusive throughout the chain. Passing a model test means compatibility with the declared assumptions and current data, not truth of the model or closure of the physical-to-experiential bridge.

## Citation metadata resources

- [`CITATION.cff`](CITATION.cff): machine-readable Citation File Format metadata used by GitHub citation tools.
- [`CITATION.bib`](CITATION.bib): ready-to-import BibTeX record.
- [Detailed Proposition Record](docs/detailed_proposition_record.md): P1 through P84 chronological theorem record.
- [Theorem Roadmap](docs/theorem_roadmap.md): dependency-oriented theorem map.
- [Research Navigation](docs/research_navigation.md): reader-oriented proof/code/figure paths.
- [P72 equation and provenance record](docs/p72_equation_provenance.md): noisy-target theorem provenance.
- [P73 equation and provenance record](docs/p73_equation_provenance.md): target-channel identifiability provenance.
- [P74 equation and provenance record](docs/p74_equation_provenance.md): finite-sample target-channel recovery provenance.
- [P75 equation and provenance record](docs/p75_equation_provenance.md): model-adequacy provenance.
- [P76 equation and provenance record](docs/p76_equation_provenance.md): finite-data inadequacy provenance.
- [P77 equation and provenance record](docs/p77_equation_provenance.md): full-law model-set separation provenance.
- [P78 equation and provenance record](docs/p78_equation_provenance.md): continuous-model separation provenance.
- [P79 equation and provenance record](docs/p79_equation_provenance.md): exact-rational sampling-radius provenance.
- [P80 equation and provenance record](docs/p80_equation_provenance.md): simplex-coupled separation provenance.
- [P81 equation and provenance record](docs/p81_equation_provenance.md): projection-event provenance.
- [P82 equation and provenance record](docs/p82_equation_provenance.md): nested projection-contrast provenance.
- [P83 equation and provenance record](docs/p83_equation_provenance.md): projection-parity provenance.
- [P84 equation and provenance record](docs/p84_equation_provenance.md): joint projection-parity contrast provenance.
- [Equation and Citation Map](docs/equation_and_citation_map.md): equation/source classification across the program.
- [Citation and Reference Policy](docs/citation_and_reference_policy.md): repository attribution rules.

## Proposition 84 method citation

For work that specifically uses the current continuous-family frontier, cite the program together with **Proposition 84: Exact Joint Projection-Parity Contrast Certificate for Continuous P75 Separation**. P84 adds 220 genuinely coupled parity contrasts, exact common-endpoint rational box extremization, and the strict witness `L83 = 0 < L84 = 1/32`.

The result is a conditional model-distance certificate for the declared P75 latent family. It should not be cited as an identification, definition, or measurement of consciousness, and non-rejection remains inconclusive.