# Mathematical Consciousness Bridge

[![tests](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml)
[![version](https://img.shields.io/badge/version-0.82.0-2563eb)](CITATION.cff)
[![license](https://img.shields.io/badge/license-MIT-059669)](LICENSE)

**Mahsa Keikha, PhD**

> ## The question
>
> **Can a physical description ever be enough to explain a difference related to experience?**

Science is extraordinarily good at describing what physical systems do. We can measure activity, structure, behavior, dynamics, responses to stimulation, information flow, and many other physical properties.

This project asks a different question: **how would we know whether a physical description is actually enough to account for a distinction related to experience, rather than merely being correlated with it?**

The repository does not begin by declaring a brain pattern, information measure, quantum effect, hidden variable, or mathematical object to be consciousness. Instead, it builds a framework for testing proposed connections carefully enough that they can fail.

**[Start here](START_HERE.md)** · **[Research map](docs/research_map.md)** · **[Visual atlas](docs/figure_catalog.md)** · **[Technical record](docs/detailed_proposition_record.md)** · **[Reproduce the work](docs/reproducibility.md)**

---

## The idea in one minute

A scientific claim linking physics to experience should survive a few basic questions:

| Question | In plain language | Go deeper |
| --- | --- | --- |
| **What are we describing?** | Be clear about which physical information is actually included. | [Research map](docs/research_map.md) |
| **Could something important be missing?** | A useful physical description may still leave out a distinction that matters to the target we care about. | [Bridge problem](docs/bridge_problem.md) |
| **Can we trust what we observe?** | Reports, labels, behavior, and other measurements can be incomplete or noisy. | [Start Here](START_HERE.md) |
| **Can the proposed model be wrong?** | A serious model must make predictions or constraints that can fail. | [Falsification program](docs/falsification_program.md) |
| **Does the result survive real uncertainty?** | Apparent patterns should remain meaningful when finite data and numerical uncertainty are taken seriously. | [Reproducibility guide](docs/reproducibility.md) |

That is the core of the project. The mathematics behind each question is available one layer deeper for readers who want to inspect it.

---

## Why this matters

The difficult part of consciousness research is not only collecting more measurements. It is knowing **what those measurements would have to establish** before a physical description could legitimately be said to explain a distinction related to experience.

This repository tries to make that logic explicit. It separates the scientific question into smaller pieces that can be tested, challenged, reproduced, and improved independently.

The goal is not to make the strongest possible claim. It is to make strong claims **hard to make casually and easy to audit carefully**.

---

## What has been built

The repository contains a growing mathematical and computational research program covering physical description, sufficiency, measurement, model testing, reasoning with finite data, and reproducibility.

You do **not** need to read the propositions in order to understand the project.

If you want the complete theorem record, including assumptions, proofs, implementations, tests, figures, and scientific boundaries, use the **[Detailed Proposition Record](docs/detailed_proposition_record.md)** or the **[Theorem Roadmap](docs/theorem_roadmap.md)**.

The current public theorem frontier is **P93**. The formal release remains **v0.82.0**.

**[Read the current frontier](docs/proposition_93_localized_sign_coherence_rejection.md)**

---

## Visual architecture

![Scientific architecture of the project](docs/figures/research_architecture.svg)

**Figure 1. Scientific architecture of the project.** The research moves from physical dynamics to operationally measurable structure, then to mathematical sufficiency tests, target-side validity, finite-data certification, experimental design, and finally the still-open physical-to-experiential bridge. The arrows are logical dependencies, not claims that one layer has already been identified with consciousness.

> **Visual reading standard.** Every reader-facing figure now has a clear title, an embedded SVG description, a nearby caption or atlas explanation, a scientific-status boundary, and a direct route to the proof or source context. Use the [Complete Figure Catalog](docs/figure_catalog.md) to understand every visual without searching the repository, and the [Figure Caption and Description Standard](docs/figure_caption_and_description_standard.md) for the enforced documentation rules.

### Current theorem frontier

![P93 Localized Finite-Sample Sign-Coherence Rejection](docs/figures/p93_localized_sign_coherence_rejection.svg)

**Figure 2. P93 localized finite-sample sign-coherence rejection.** P92 proves the exact nonlinear population obstruction. P93 turns that obstruction into a finite-data rejection rule using only the seven observable cells that enter the three P92 minors. For the established sign geometry, the exact determinant stability radii are `1/24`, `3/56`, and `5/72`. At 95 percent confidence, P79 exact-rational envelopes prove that the seven-cell sampling radius is still above `1/24` at `n = 1622` and below it at `n = 1623`. The first exact replication of the original 24-count profile that clears the certificate is `n = 1632 = 68 x 24`.

The generic P77 fixed-population-margin sufficient bound crosses at `n = 7444`, but that is a different guarantee. P93 is a localized observed-data certificate for the P92 sign witness. It is not claimed to be minimax optimal or universally sufficient.

P93 is a conditional finite-sample model-rejection theorem. Non-rejection remains inconclusive. It does not identify consciousness, establish nonphysicality, validate an alternative theory, or close the physical-to-experiential bridge.
## Choose your path

| If you want to... | Start here |
| --- | --- |
| Understand the project without technical background | **[Start Here](START_HERE.md)** |
| See how the scientific questions fit together | **[Research Map](docs/research_map.md)** |
| Explore the project visually | **[Figure Catalog](docs/figure_catalog.md)** |
| Move into the formal architecture | **[Technical Research Architecture](docs/research_architecture.md)** |
| Follow the complete mathematical development | **[Theorem Roadmap](docs/theorem_roadmap.md)** |
| Find every proposition and its technical record | **[Detailed Proposition Record](docs/detailed_proposition_record.md)** |
| Check equations and sources | **[Equation and Citation Map](docs/equation_and_citation_map.md)** |
| Run the code and verification yourself | **[Reproducibility Guide](docs/reproducibility.md)** |
| Look up terminology | **[Glossary](docs/glossary.md)** |

---

## What this project does not claim

This repository does **not** claim that:

- a particular equation or hidden variable has been identified as consciousness;
- a model that survives one test is therefore uniquely correct;
- rejection of one physical model proves that consciousness is nonphysical;
- mathematical proof under stated assumptions makes those assumptions true in nature;
- the final bridge from physical description to experience has been solved.

The bridge remains an open scientific problem.

---

## Related physical foundation

This work follows the separate project **[Spatiotemporal Observer Mathematics](https://github.com/MahsaKeikha/spatiotemporal-observer-math)**, which studies how a persistent physical subsystem can be identified from measured dynamics.

That project asks **which physical system is being tracked**. This repository asks the next question: **what would be required before a physical description of that system could support a scientifically testable claim about experience?**

---

## Citation and license

For scholarly citation, see **[CITATION.md](CITATION.md)** and **[CITATION.cff](CITATION.cff)**.

MIT License. See **[LICENSE](LICENSE)**.

**Public theorem frontier:** P93
**Formal release:** v0.82.0
**Final bridge from physical description to experience:** open
