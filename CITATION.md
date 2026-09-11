# How to Cite This Research

The **Mathematical Consciousness Bridge** is an ongoing mathematical-physics research program by **Mahsa Keikha, PhD**. It develops a falsifiable test architecture for the physical-to-experiential bridge problem, with theorem-level derivations, numerical figures, executable implementations, and explicit scientific-status boundaries.

If this research program, one of its propositions, figures, algorithms, or implementations contributes to your work, please cite it. When a specific proposition or artifact is central to your use, cite both the overall research program and the specific proposition or artifact.

## Preferred scholarly citation

> Keikha, M. (2026). *Mathematical Consciousness Bridge: A Mathematical-Physics Test Architecture for the Physical-to-Experiential Bridge Problem* (Version 0.78.0). GitHub research repository. https://github.com/MahsaKeikha/mathematical-consciousness-bridge

This is the preferred citation for the research program at the current documented frontier, P78.

## BibTeX

```bibtex
@misc{keikha2026mathematicalconsciousnessbridge,
  author       = {Keikha, Mahsa},
  title        = {Mathematical Consciousness Bridge: A Mathematical-Physics Test Architecture for the Physical-to-Experiential Bridge Problem},
  year         = {2026},
  version      = {0.78.0},
  howpublished = {GitHub research repository},
  url          = {https://github.com/MahsaKeikha/mathematical-consciousness-bridge},
  note         = {Ongoing research program. Current documented theorem frontier: P78.}
}
```

A machine-readable BibTeX record is also available in [`CITATION.bib`](CITATION.bib), and GitHub-compatible citation metadata are maintained in [`CITATION.cff`](CITATION.cff).

## Citing a specific proposition

For theorem-level attribution, cite the research program and identify the proposition explicitly. A recommended form is:

> Keikha, M. (2026). Proposition PXX, "Proposition title." In *Mathematical Consciousness Bridge: A Mathematical-Physics Test Architecture for the Physical-to-Experiential Bridge Problem* (Version 0.78.0). GitHub research repository. Direct proposition URL.

Replace `PXX`, the title, and the URL with the proposition actually used. The [Detailed proposition record](docs/detailed_proposition_record.md) and [Theorem roadmap](docs/theorem_roadmap.md) provide the proposition titles, dependency structure, and direct proof links.

For target-side bridge methodology, cite [Proposition 71](docs/proposition_71_target_provenance_noncircularity.md) when relying on the non-circularity result for descriptor-derived targets. Cite [Proposition 72](docs/proposition_72_target_measurement_channel_robustness.md) when relying on noisy-target residual attenuation, target-channel witness stability, or its finite-sample target-separation certificate. Cite [Proposition 73](docs/proposition_73_target_channel_identifiability.md) when relying on the three-view binary latent-target population identifiability theorem, recovery of P72 channel-stability coefficients, the joint-view stability consequence, or the constructive two-view non-identifiability result. Cite [Proposition 74](docs/proposition_74_finite_sample_target_channel_recovery.md) when relying on the simultaneous finite-data recovery certificate, covariance nondegeneracy gate, confidence intervals for target-channel quantities, or the conservative covariance-margin sample-size condition. Cite [Proposition 75](docs/proposition_75_target_model_adequacy_overidentification.md) when relying on the distinction between three-view just-identification and four-view overidentification, the covariance-tetrad or cross-triple adequacy constraints, the fourth-centered-moment relation, or the full-law target-model reconstruction audit. Cite [Proposition 76](docs/proposition_76_finite_sample_target_model_adequacy.md) when relying on the sixteen-cell finite-sample adequacy rejection theorem, the explicit tetrad confidence radius, denominator-free polynomial adequacy intervals, or the one-sided rule separating certified model rejection from inconclusive non-rejection. Cite [Proposition 77](docs/proposition_77_full_law_model_set_separation.md) when relying on finite-sample confidence-region separation from the complete declared model set, 1-Lipschitz transport of model distance, fixed-margin design bounds, or the requirement that rejection of a continuous family use a certified distance lower bound or equivalent feasibility proof rather than an ordinary best-fit upper bound. Cite [Proposition 78](docs/proposition_78_certified_continuous_model_separation.md) when relying on the exact multi-affine box enclosure for the P75 model, the certified continuous-family L-infinity lower bound, the mesh-gap convergence guarantee, the exact-rational branch-and-bound implementation, or its strict P77 rejection handoff.

## Citing a figure, algorithm, or implementation

When a figure, numerical result, or implementation is used directly, include the repository citation and identify the artifact by its repository path or proposition number. The [Equation and citation map](docs/equation_and_citation_map.md), [Visual atlas](website/visual-atlas.html), and proposition records connect equations and figures to their assumptions, proofs, source files, and tests.

For example:

> Keikha, M. (2026). Figure or implementation associated with Proposition PXX. *Mathematical Consciousness Bridge* (Version 0.78.0). GitHub research repository. Direct artifact URL.

## Version-specific reproducibility

This repository is an evolving research program. For reproducible scholarly use:

1. Cite the documented version used in your analysis.
2. Record the exact Git commit SHA when results depend on a particular repository state.
3. Cite the individual proposition or artifact when your argument depends on a specific theorem, figure, algorithm, or test.
4. Do not attribute later propositions or later numerical results to an earlier version of the repository.

The current citation metadata identify Version **0.78.0** and theorem frontier **P78**. Future research versions should update the version number, theorem frontier, citation metadata, and archival record together.

## DOI and archival status

No DOI is currently asserted for this repository. A DOI should be added to the preferred citation only after an archival service has actually issued one for a versioned release. Until then, the GitHub repository URL, documented version, and exact commit SHA provide the appropriate citation and reproducibility path.

Once an archival DOI exists, it should be added consistently to:

- [`CITATION.cff`](CITATION.cff)
- [`CITATION.bib`](CITATION.bib)
- this citation guide
- the citation section of the main [`README.md`](README.md)

## Scientific attribution and scope

Citation of this work should preserve its scientific status. The repository establishes a mathematical and computational **test architecture** for physical-to-experiential bridge claims under explicit assumptions. It does not presently claim that the final physical-to-experiential bridge has been derived, that consciousness has been identified with a scalar or state of matter, or that quantum mechanics has been shown to be incomplete.

P71 separates successful factorization from independent target provenance. A target constructed from the tested descriptor can satisfy a bridge condition by construction.

P72 separates latent target structure from target observation. Under the declared nondifferential measurement condition, target measurement can attenuate or erase a genuine bridge witness but cannot create a positive population residual from a latent target already screened off by the physical descriptor.

P73 asks when target-channel reliability can be identified rather than assumed. Under one fixed physical stratum, a binary latent target, three conditionally independent binary target views, interior prevalence, and nonzero view loadings, P73 gives explicit population recovery up to a common latent-label swap. The P72 stability coefficients are invariant under that swap. P73 also proves constructively that two views alone do not generally identify the individual view reliabilities.

P74 separates population identifiability from finite-data certifiability. Under the P73 model and IID sampling, it propagates a simultaneous confidence event for the eight-cell observed law into conservative bounds for the P73 latent quantities and the P72 stability coefficients. The covariance nondegeneracy gate prevents finite-data noise near the P73 singular set from being reported as a stable latent recovery.

P75 then separates identifiability from **model adequacy**. Three binary views and one binary latent state have equal generic continuous dimension, so successful three-view recovery does not by itself supply an independent equality-based goodness-of-fit test. Adding a fourth binary view produces six generic overidentifying degrees of freedom. P75 derives observable covariance-tetrad, cross-triple, and fourth-centered-moment consistency obligations and supplements them with full four-view law reconstruction. Passing these tests establishes compatibility with the declared target-measurement model, not uniqueness or truth of that model.

P76 adds finite-data model falsification to that adequacy layer. It places the sixteen-cell empirical law inside one simultaneous Hoeffding event, propagates that event to denominator-free P75 polynomial constraints, and permits model rejection when any necessary-constraint confidence interval excludes zero. P76 deliberately does not infer an ordinary chi-square null law from the P75 dimension count, and a failure to reject remains inconclusive rather than model acceptance.

P77 then extends finite-data adequacy from selected necessary constraints to the complete declared observed-law model set. It inverts the simultaneous empirical-law confidence region against that model set and permits rejection only when the confidence region is certified disjoint from the model family. For continuous latent models, an ordinary candidate fit is only an upper bound on the minimum model distance, so P77 requires a sound lower bound or equivalent certified feasibility result before claiming full-law incompatibility.

P78 supplies that missing continuous-family lower-bound mechanism for the specific P75 four-view binary latent model. It exploits the model's multi-affine nine-parameter map to compute exact rational cell enclosures on parameter boxes, aggregates those into a global L-infinity lower bound, and proves a mesh-width convergence guarantee. P78 remains a computational certificate under the declared P75 model; it does not turn non-rejection into model validation or identify the latent state with consciousness.

These remain conditional statistical target-measurement results, not validation of an experiential ontology or a privileged consciousness label.

When citing a theorem, readers should consult the proposition document for its assumptions and scope rather than citing the theorem statement without its declared conditions.

## Citation metadata resources

- [`CITATION.cff`](CITATION.cff): machine-readable Citation File Format metadata used by GitHub citation tools.
- [`CITATION.bib`](CITATION.bib): ready-to-import BibTeX record.
- [Detailed proposition record](docs/detailed_proposition_record.md): P1 through P78 chronological theorem record.
- [Theorem roadmap](docs/theorem_roadmap.md): dependency-oriented theorem map.
- [P72 equation and provenance record](docs/p72_equation_provenance.md): equation-level classification for the noisy-target theorem.
- [P73 equation and provenance record](docs/p73_equation_provenance.md): equation-level classification and external latent-class context for the target-channel identifiability theorem.
- [P74 equation and provenance record](docs/p74_equation_provenance.md): finite-sample concentration, perturbation, and target-channel confidence construction.
- [P75 equation and provenance record](docs/p75_equation_provenance.md): just-identification, four-view overidentification, moment-adequacy constraints, and full-law reconstruction provenance.
- [P76 equation and provenance record](docs/p76_equation_provenance.md): sixteen-cell concentration, denominator-free polynomial intervals, and finite-sample adequacy rejection provenance.
- [P77 equation and provenance record](docs/p77_equation_provenance.md): full-law confidence-region inversion, model-distance transport, and certified lower-bound rejection provenance.
- [P78 equation and provenance record](docs/p78_equation_provenance.md): multi-affine box enclosures, exact-rational global lower bounds, mesh-gap convergence, and P77 rejection handoff provenance.
- [Equation and citation map](docs/equation_and_citation_map.md): provenance of equations, assumptions, and external sources.
- [Citation and reference policy](docs/citation_and_reference_policy.md): repository rules for attribution and scientific sourcing.
