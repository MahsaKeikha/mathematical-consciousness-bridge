# How to Cite This Research

The **Mathematical Consciousness Bridge** is an ongoing mathematical-physics research program by **Mahsa Keikha, PhD**. It develops a falsifiable test architecture for the physical-to-experiential bridge problem, with theorem-level derivations, numerical figures, executable implementations, and explicit scientific-status boundaries.

If this research program, one of its propositions, figures, algorithms, or implementations contributes to your work, please cite it. When a specific proposition or artifact is central to your use, cite both the overall research program and the specific proposition or artifact.

## Preferred scholarly citation

> Keikha, M. (2026). *Mathematical Consciousness Bridge: A Mathematical-Physics Test Architecture for the Physical-to-Experiential Bridge Problem* (Version 0.82.0). GitHub research repository. https://github.com/MahsaKeikha/mathematical-consciousness-bridge

This is the preferred citation for the research program at the current documented frontier, P86.

## BibTeX

```bibtex
@misc{keikha2026mathematicalconsciousnessbridge,
  author       = {Keikha, Mahsa},
  title        = {Mathematical Consciousness Bridge: A Mathematical-Physics Test Architecture for the Physical-to-Experiential Bridge Problem},
  year         = {2026},
  version      = {0.82.0},
  howpublished = {GitHub research repository},
  url          = {https://github.com/MahsaKeikha/mathematical-consciousness-bridge},
  note         = {Ongoing research program. Current documented theorem frontier: P86.}
}
```

A machine-readable BibTeX record is also available in [`CITATION.bib`](CITATION.bib), and GitHub-compatible citation metadata are maintained in [`CITATION.cff`](CITATION.cff).

## Citing a specific proposition

For theorem-level attribution, cite the research program and identify the proposition explicitly. A recommended form is:

> Keikha, M. (2026). Proposition PXX, "Proposition title." In *Mathematical Consciousness Bridge: A Mathematical-Physics Test Architecture for the Physical-to-Experiential Bridge Problem* (Version 0.82.0). GitHub research repository. Direct proposition URL.

Replace `PXX`, the title, and the URL with the proposition actually used. The [Detailed proposition record](docs/detailed_proposition_record.md) and [Theorem roadmap](docs/theorem_roadmap.md) provide the proposition titles, dependency structure, and direct proof links.

For target-side bridge methodology, cite [Proposition 71](docs/proposition_71_target_provenance_noncircularity.md) when relying on the non-circularity result for descriptor-derived targets. Cite [Proposition 72](docs/proposition_72_target_measurement_channel_robustness.md) when relying on noisy-target residual attenuation, target-channel witness stability, or its finite-sample target-separation certificate. Cite [Proposition 73](docs/proposition_73_target_channel_identifiability.md) when relying on the three-view binary latent-target population identifiability theorem, recovery of P72 channel-stability coefficients, the joint-view stability consequence, or the constructive two-view non-identifiability result. Cite [Proposition 74](docs/proposition_74_finite_sample_target_channel_recovery.md) when relying on the simultaneous finite-data recovery certificate, covariance nondegeneracy gate, confidence intervals for target-channel quantities, or the conservative covariance-margin sample-size condition. Cite [Proposition 75](docs/proposition_75_target_model_adequacy_overidentification.md) when relying on the distinction between three-view just-identification and four-view overidentification, the covariance-tetrad or cross-triple adequacy constraints, the fourth-centered-moment relation, or the full-law target-model reconstruction audit. Cite [Proposition 76](docs/proposition_76_finite_sample_target_model_adequacy.md) when relying on the sixteen-cell finite-sample adequacy rejection theorem, the explicit tetrad confidence radius, denominator-free polynomial adequacy intervals, or the one-sided rule separating certified model rejection from inconclusive non-rejection. Cite [Proposition 77](docs/proposition_77_full_law_model_set_separation.md) when relying on finite-sample confidence-region separation from the complete declared model set, 1-Lipschitz transport of model distance, fixed-margin design bounds, or the requirement that rejection of a continuous family use a certified distance lower bound or equivalent feasibility proof rather than an ordinary best-fit upper bound. Cite [Proposition 78](docs/proposition_78_certified_continuous_model_separation.md) when relying on the exact multi-affine box enclosure for the P75 model, the certified continuous-family L-infinity lower bound, the mesh-gap convergence guarantee, the exact-rational branch-and-bound implementation, or its strict P77 rejection handoff. Cite [Proposition 79](docs/proposition_79_certified_sampling_radius.md) when relying on exact-rational one-sided certification of the finite-alphabet sampling radius or the rounding-direction-safe rejection comparison. Cite [Proposition 80](docs/proposition_80_simplex_coupled_model_separation.md) when relying on probability-simplex coupling of the P78 cell intervals, the exact interval-simplex L-infinity distance, or the never-weaker P80 box lower bound. Cite [Proposition 81](docs/proposition_81_projection_event_model_separation.md) when relying on exact projected-event parameter-box intervals, the event-size transfer to full-law L-infinity distance, the P81 never-weaker-than-P80 certificate, or its strict-improvement witness. Cite [Proposition 82](docs/proposition_82_exact_nested_projection_contrast.md) when relying on exact nested residual-event parameter-box intervals, the 256-contrast audit, the P82 never-weaker-than-P81 certificate, the direct residual extremization theorem, or the exact 1/12 versus 1/16 strict-improvement witness.

## Citing a figure, algorithm, or implementation

When a figure, numerical result, or implementation is used directly, include the repository citation and identify the artifact by its repository path or proposition number. The [Equation and citation map](docs/equation_and_citation_map.md), [Visual atlas](website/visual-atlas.html), and proposition records connect equations and figures to their assumptions, proofs, source files, and tests.

For example:

> Keikha, M. (2026). Figure or implementation associated with Proposition PXX. *Mathematical Consciousness Bridge* (Version 0.82.0). GitHub research repository. Direct artifact URL.

## Version-specific reproducibility

This repository is an evolving research program. For reproducible scholarly use:

1. Cite the documented version used in your analysis.
2. Record the exact Git commit SHA when results depend on a particular repository state.
3. Cite the individual proposition or artifact when your argument depends on a specific theorem, figure, algorithm, or test.
4. Do not attribute later propositions or later numerical results to an earlier version of the repository.

The current citation metadata identify Version **0.82.0** and theorem frontier **P86**. Future research versions should update the version number, theorem frontier, citation metadata, and archival record together.

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

P78 supplies the continuous-family lower-bound mechanism for the specific P75 four-view binary latent model. It exploits the model's multi-affine nine-parameter map to compute exact rational cell enclosures on parameter boxes, aggregates those into a global L-infinity lower bound, and proves a mesh-width convergence guarantee.

P79 certifies the finite-alphabet sampling-radius side of the P77 rejection gate with one-sided exact-rational numerical enclosures, so the comparison against the model-distance lower bound does not depend on unsafe floating-point rounding direction.

P80 tightens the P78 parameter-box relaxation by intersecting the exact observed-cell intervals with probability normalization. The resulting interval-simplex distance is never weaker than the corresponding P78 coordinatewise bound, while it remains a lower bound on distance to the true continuous P75 box image. 

P81 further tightens the declared continuous-family test by retaining exact parameter-box ranges for every nonempty projected binary event. Event-level mismatch is divided by the number of full observed cells in that event to obtain a sound full-law L-infinity lower bound. The combined P81 certificate is never weaker than P80 and can be strictly stronger. None of P78-P84 turns non-rejection into model validation or identifies the latent state with consciousness.

P82 strengthens that chain again by retaining exact common-parameter structure for residual events formed from nested projected cylinders. It computes each residual interval directly from the P75 branchwise factorization rather than by subtracting separate P81 event intervals, audits 256 genuinely new residual events, and preserves the one-sided model-rejection interpretation. Its exact witness gives P80 = 0, P81 = 1/16, and P82 = 1/12. This is a stronger certificate against the declared P75 family, not evidence that its latent variable is consciousness.

These remain conditional statistical target-measurement results, not validation of an experiential ontology or a privileged consciousness label.

When citing a theorem, readers should consult the proposition document for its assumptions and scope rather than citing the theorem statement without its declared conditions.

## Citation metadata resources

- [`CITATION.cff`](CITATION.cff): machine-readable Citation File Format metadata used by GitHub citation tools.
- [`CITATION.bib`](CITATION.bib): ready-to-import BibTeX record.
- [Detailed proposition record](docs/detailed_proposition_record.md): P1 through P86 chronological theorem record.
- [Theorem roadmap](docs/theorem_roadmap.md): dependency-oriented theorem map.
- [P72 equation and provenance record](docs/p72_equation_provenance.md): equation-level classification for the noisy-target theorem.
- [P73 equation and provenance record](docs/p73_equation_provenance.md): equation-level classification and external latent-class context for the target-channel identifiability theorem.
- [P74 equation and provenance record](docs/p74_equation_provenance.md): finite-sample concentration, perturbation, and target-channel confidence construction.
- [P75 equation and provenance record](docs/p75_equation_provenance.md): just-identification, four-view overidentification, moment-adequacy constraints, and full-law reconstruction provenance.
- [P76 equation and provenance record](docs/p76_equation_provenance.md): sixteen-cell concentration, denominator-free polynomial intervals, and finite-sample adequacy rejection provenance.
- [P77 equation and provenance record](docs/p77_equation_provenance.md): full-law confidence-region inversion, model-distance transport, and certified lower-bound rejection provenance.
- [P78 equation and provenance record](docs/p78_equation_provenance.md): multi-affine box enclosures, exact-rational global lower bounds, mesh-gap convergence, and P77 rejection handoff provenance.
- [P79 equation and provenance record](docs/p79_equation_provenance.md): one-sided exact-rational sampling-radius certification and safe numerical handoff.
- [P80 equation and provenance record](docs/p80_equation_provenance.md): probability-simplex coupling, exact interval-simplex distance, and P80/P78 dominance.
- [P81 equation and provenance record](docs/p81_equation_provenance.md): projected-event box intervals, event-size distance transfer, dominance, and the P79 rejection handoff.
- [P82 equation and provenance record](docs/p82_equation_provenance.md): exact nested residual-event intervals, direct residual extremization, dominance, and the P79 rejection handoff.
- [P83 equation and provenance record](docs/p83_equation_provenance.md): exact projection-parity identities, parity box intervals, dominance, and strict improvement over P82.
- [P84 equation and provenance record](docs/p84_equation_provenance.md): exact joint parity-event contrasts, common-vertex extremization, 220-contrast audit, and strict improvement over P83.
- [Equation and citation map](docs/equation_and_citation_map.md): provenance of equations, assumptions, and external sources.
- [Citation and reference policy](docs/citation_and_reference_policy.md): repository rules for attribution and scientific sourcing.


## Proposition 79

For the exact-rational sampling-radius certificate, cite the repository together with [Proposition 79](docs/proposition_79_certified_sampling_radius.md) and its [equation provenance record](docs/p79_equation_provenance.md).


## Proposition 80

For the simplex-coupled continuous-model certificate, cite the repository together with [Proposition 80](docs/proposition_80_simplex_coupled_model_separation.md) and its [equation provenance record](docs/p80_equation_provenance.md). P80 is a computational tightening of the P78 continuous P75 separation certificate and should not be cited as an identification of consciousness.


## Proposition 81

For the projection-event continuous-model certificate, cite the repository together with [Proposition 81](docs/proposition_81_projection_event_model_separation.md) and its [equation provenance record](docs/p81_equation_provenance.md). P81 is a computational tightening of the P80/P78 continuous P75 separation chain and should not be cited as an identification of consciousness.

## Proposition 82

For the exact nested projection-contrast certificate, cite the repository together with [Proposition 82](docs/proposition_82_exact_nested_projection_contrast.md) and its [equation provenance record](docs/p82_equation_provenance.md). P82 is a conditional computational model-distance theorem for the declared P75 family. It should not be cited as an identification of consciousness.

## P82 frontier citation note

P82 strengthens the P81 continuous P75 separation chain through exact nested residual-event intervals. It is a conditional model-distance certificate and should not be cited as an identification of consciousness.


## Proposition 83 method citation

For work that specifically uses the newest continuous-family certificate, cite the program together with **Proposition 83: Exact Projection-Parity Certificate for Continuous P75 Separation**. P83 adds 22 parity observables, exact rational box extremization through the Bernoulli parity identity, and a strict witness with `L82 = 0 < L83 = 1/16`.

The result is a conditional model-distance certificate for the declared P75 latent family. It should not be cited as an identification, definition, or measurement of consciousness, and non-rejection remains inconclusive.


## Proposition 84 method citation

For work that specifically uses the current joint parity certificate, cite the program together with **Proposition 84: Exact Joint Projection-Parity Contrast Certificate** and its [equation provenance record](docs/p84_equation_provenance.md). P84 retains all of P83 and adds 220 exact coupled parity-event contrasts that preserve one shared P75 parameter assignment. Its exact-rational strict witness has `L83 = 0 < L84 = 1/32`.

The result is a conditional model-distance certificate for the declared P75 latent family. It should not be cited as an identification, definition, or measurement of consciousness, and non-rejection remains inconclusive.


## Current theorem frontier: P85

The current documented theorem frontier is **P85**, the exact three-event projection-parity functional certificate. When citing this frontier result specifically, cite [Proposition 85](docs/proposition_85_exact_triple_projection_parity_functional.md) together with its [equation and provenance record](docs/p85_equation_provenance.md), implementation, tests, and exact theorem figure. P85 is conditional on the declared P75 model and does not claim that the physical-to-experiential bridge has been solved.


## Proposition 86 method citation

For work using the minimally weighted four-event shared-parameter parity certificate, cite the program together with **Proposition 86: Exact Minimally Weighted Four-Event Projection-Parity Functional Certificate**. P86 exhausts 10,560 exact functionals with primitive coefficient magnitudes `{1,1,1,2}` and includes the strict exact-rational hierarchy witness `L85 = 0 < L86 = 1/192`.

- [P86 proof](docs/proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md)
- [P86 equation provenance](docs/p86_equation_provenance.md)

P86 is conditional on the declared P75 model and should not be cited as an identification or definition of consciousness.
