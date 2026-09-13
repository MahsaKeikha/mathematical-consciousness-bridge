# Mathematical Consciousness Bridge

[![tests](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml)
[![reproducibility](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/reproducibility.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/reproducibility.yml)
[![figures](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/figures.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/figures.yml)
[![version](https://img.shields.io/badge/version-0.82.0-2563eb)](CITATION.cff)
[![license](https://img.shields.io/badge/license-MIT-059669)](LICENSE)

**Mahsa Keikha, PhD**

> ## The question
>
> **What would have to be true before a physical description of a system could support a scientifically testable claim about experience?**

This repository develops a rigorous mathematical framework for that question. It does **not** begin by declaring a brain pattern, information measure, quantum effect, latent variable, or mathematical object to be consciousness. Instead, it asks what any proposed physical-to-experiential bridge would have to survive before the claim deserves scientific weight.

The program separates several questions that are often mixed together: Is the physical description well defined? Is the experience-related target independent rather than circular? Is the target measurable? Is the measurement model identifiable? Does the declared model actually fit the observations? Can a finite-data rejection be certified without hiding numerical or selection error?

**If this is your first visit, do not read the repository folder by folder.** Start with the guided routes below.

## Start in one click

| I want to... | Open this |
| --- | --- |
| Understand the idea without technical background | **[Start Here](START_HERE.md)** |
| See the research as a visual scientific program | **[Research Architecture](docs/research_architecture.md)** |
| Find a theorem, figure, source file, test, or provenance record | **[Research Traceability Index](docs/research_traceability_index.md)** |
| Follow the proposition dependencies | **[Theorem Roadmap](docs/theorem_roadmap.md)** |
| Browse the figures first | **[Figure Catalog](docs/figure_catalog.md)** |
| Reproduce the computational record | **[Reproducibility Guide](docs/reproducibility.md)** |
| Read the complete proposition record | **[Detailed Proposition Record](docs/detailed_proposition_record.md)** |

---

## The project in one picture

![Research architecture](docs/figures/research_architecture.svg)

The architecture is deliberately layered. A theorem about physical structure is not automatically a theorem about experience. A successful fit is not automatically a bridge. A non-rejection is not model validation. Each layer must earn the right to support the next one.

The complete theorem roadmap covers **P1 through P88 with explicit dependency branches**, but the landing page does not require you to read 88 results in sequence.

---

## What the research is building

The program can be read as five scientific questions.

### 1. What counts as the same physical system?

The early results formalize representation invariance, identifiability, intervention-resolved structure, temporal continuation, composition, and scale. The goal is to prevent arbitrary coordinates or coarse descriptions from being mistaken for physical facts.

**Go deeper:** [Research Architecture](docs/research_architecture.md) · [P1-P18 in the theorem roadmap](docs/theorem_roadmap.md)

### 2. When is a physical description sufficient for a target?

P19-P24 formulate and test physical sufficiency: whether an independently defined target contains distinctions that the proposed physical descriptor loses. The framework is designed so that an inadequate descriptor can fail.

**Go deeper:** [P19 fundamental physical sufficiency](docs/proposition_19_fundamental_physical_sufficiency.md) · [Falsification Program](docs/falsification_program.md)

### 3. Can the target and its measurement be trusted?

P71-P74 address target circularity, noisy observation, identifiability, and finite-sample recovery. This prevents an experience-related target from being quietly constructed out of the same physical variables that are then claimed to explain it.

**Go deeper:** [P71-P74 research path](docs/research_traceability_index.md#target-integrity-and-measurement-p71-p74)

### 4. Does the declared target model actually fit the data?

P75-P87 move from overidentifying restrictions to increasingly strong exact-rational model-separation certificates. The point is not to produce a more complicated formula. It is to make model inadequacy mathematically visible when simpler checks remain silent.

**Go deeper:** [P75-P87 model-adequacy path](docs/research_traceability_index.md#model-adequacy-and-exact-separation-p75-p87)

### 5. Can a discovered incompatibility survive independent validation?

P88 adds a held-out validation layer. A model box and one P87 functional may be selected using discovery data, but the pair must be frozen before an independent validation sample is examined. Under that design, the selected scalar test can be certified without a 39,600-way functional union bound.

**Go deeper:** [P88 theorem](docs/proposition_88_heldout_selected_parity_functional_certification.md) · [P88 provenance](docs/p88_equation_provenance.md) · [implementation](src/consciousness_bridge/heldout_selected_parity_functional_certification.py) · [tests](tests/test_heldout_selected_parity_functional_certification.py)

---

## Current frontier: P88

![P88 held-out selected parity functional certification](docs/figures/p88_heldout_selected_parity_functional_certification.svg)

P88 asks a narrow but important statistical question: after a large discovery search finds a promising exact P87 incompatibility, can that selected result be tested on fresh data without pretending the selection never happened?

For the stored exact witness, the discovery-selected P75 box and P87 functional are frozen before validation. With `n = 2400` held-out observations and `alpha = 0.05`, the exact certificate gives a positive population lower-confidence bound on distance from the P75 laws inside the frozen box:

\[
\inf_{q\in\mathcal M_B}\|p-q\|_\infty
\ge
\frac{701849}{201326592}
\approx 0.00348612.
\]

The exact P79-certified design threshold for the stored functional gap is **1063 held-out observations**; 1062 is insufficient under the same certificate settings.

> **Interpretation boundary:** this is a box-specific finite-sample rejection result under genuine discovery/validation independence. It is not, by itself, a rejection of every P75 parameter value. It does not identify the latent state with consciousness, prove nonphysicality, or close the physical-to-experiential bridge.

### Audit P88 without searching the repository

| Question | Direct record |
| --- | --- |
| What is proved? | [P88 theorem](docs/proposition_88_heldout_selected_parity_functional_certification.md) |
| Where do the equations come from? | [P88 equation provenance](docs/p88_equation_provenance.md) |
| What code computes the certificate? | [P88 implementation](src/consciousness_bridge/heldout_selected_parity_functional_certification.py) |
| What regression tests protect it? | [P88 tests](tests/test_heldout_selected_parity_functional_certification.py) |
| What does the result look like visually? | [P88 figure](docs/figures/p88_heldout_selected_parity_functional_certification.svg) |
| How do I reproduce the repository? | [Reproducibility Guide](docs/reproducibility.md) |

---

## Scientific status

The research currently contains **88 proposition-level results** and **72 equation-driven quantitative figures**. The theorem frontier is P88. These results build a test architecture and close specific mathematical gaps; the physical-to-experiential bridge itself remains open.

The repository now contains 88 proposition-level results. The theorem frontier is P88.

| Research status | Current value |
| --- | --- |
| Formal release | **v0.82.0** |
| Public theorem frontier | **P88** |
| Proposition-level results | **88** |
| Equation-driven quantitative figures | **72** |
| Physical-to-experiential bridge | **Open** |

The formal release number and theorem frontier are intentionally separate concepts. New theorem work may advance before a new formal release is cut.

Read the complete P1 to P88 detailed proposition record in [docs/detailed_proposition_record.md](docs/detailed_proposition_record.md). For a more navigable entry point, use the [Research Traceability Index](docs/research_traceability_index.md).

---

## What this repository does not claim

| The repository can establish | It does not automatically establish |
| --- | --- |
| A theorem under declared assumptions | That the assumptions are true in nature |
| Identifiability of a declared latent model | That the latent state is consciousness |
| Rejection of a declared model or parameter box | That consciousness is nonphysical |
| Compatibility with observed data | That the model is uniquely correct |
| A physical descriptor with useful predictive structure | A completed physical-to-experiential bridge |

This distinction is central to the project. The aim is to make stronger claims **harder to make casually and easier to audit scientifically**.

---

## Reproduce the work

Recommended development environment: Python **3.12.14**.

```bash
python -m pip install -r requirements-reproducibility.txt
make reproduce
```

For the full verification suite:

```bash
make check
```

The repository also supports Python 3.10, 3.11, and 3.12 in continuous integration. See [docs/reproducibility.md](docs/reproducibility.md) for exact commands and the scope of each audit.

---

## Explore by depth, not by folder

**Five minutes:** [Start Here](START_HERE.md)

**Thirty minutes:** [Research Architecture](docs/research_architecture.md) → [P19](docs/proposition_19_fundamental_physical_sufficiency.md) → [P71-P88 traceability path](docs/research_traceability_index.md#target-side-research-frontier-p71-p88)

**Technical review:** [Theorem Roadmap](docs/theorem_roadmap.md) → proposition proof → equation provenance → source → tests

**Visual review:** [Figure Catalog](docs/figure_catalog.md) → [Visual Atlas](website/visual-atlas.html)

**Full audit:** [Detailed Proposition Record](docs/detailed_proposition_record.md) → [Equation and Citation Map](docs/equation_and_citation_map.md) → [Reproducibility Guide](docs/reproducibility.md)

The full theorem program is preserved. The landing page is intentionally selective so that a reader can understand the research before encountering its complete technical depth.

---

## Related physical foundation

This project continues [Spatiotemporal Observer Mathematics](https://github.com/MahsaKeikha/spatiotemporal-observer-math), which studies the prior physical problem of identifying a persistent moving subsystem from measured dynamics. That repository is a separate completed research record; this repository addresses the subsequent bridge methodology.

---

## Citation

See [CITATION.md](CITATION.md) and [CITATION.cff](CITATION.cff) for repository and proposition-level citation guidance.

Current theorem frontier: **P88**  
Formal release: **v0.82.0**

---

## License

MIT. See [LICENSE](LICENSE).
