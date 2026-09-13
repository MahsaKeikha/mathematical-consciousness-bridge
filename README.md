# Mathematical Consciousness Bridge

[![tests](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/test.yml)
[![reproducibility](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/reproducibility.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/reproducibility.yml)
[![figures](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/figures.yml/badge.svg)](https://github.com/MahsaKeikha/mathematical-consciousness-bridge/actions/workflows/figures.yml)
[![version](https://img.shields.io/badge/version-0.82.0-2563eb)](CITATION.cff)
[![license](https://img.shields.io/badge/license-MIT-059669)](LICENSE)

**Mahsa Keikha, PhD**

> ## The question
>
> **How could we scientifically test whether a physical description is enough to explain an experience-related difference?**

This project is about making that question testable.

It does not assume that consciousness is a particular brain signal, information measure, quantum effect, hidden variable, or mathematical object. Instead, it asks what evidence would be needed before any such claim should be trusted.

The basic idea is simple: **define what you are measuring, define what you are trying to explain, and build tests that can genuinely fail if the proposed explanation is not good enough.**

If this is your first visit, start with the simple routes below. The technical mathematics is always available one click deeper.

## Start in one click

| I want to... | Open this |
| --- | --- |
| Understand the idea in plain language | **[Start Here](START_HERE.md)** |
| See how the whole research fits together | **[Research Architecture](docs/research_architecture.md)** |
| Browse the figures | **[Figure Catalog](docs/figure_catalog.md)** |
| Find the theorem, code, test, or source behind a result | **[Research Traceability Index](docs/research_traceability_index.md)** |
| Follow the complete mathematical path | **[Theorem Roadmap](docs/theorem_roadmap.md)** |
| Reproduce the work | **[Reproducibility Guide](docs/reproducibility.md)** |

---

## The project in one picture

![Research architecture](docs/figures/research_architecture.svg)

The research is built in layers. Each layer asks one question before allowing the next claim to become stronger.

The complete theorem roadmap covers **P1 through P88 with explicit dependency branches**, but you do not need to read 88 results to understand the project.

---

## What the research is building

Think of the project as five simple questions.

| Step | Plain-language question | Go deeper |
| --- | --- | --- |
| **1** | **What exactly are we measuring in the physical system?** We first make the physical description clear enough that different representations cannot create different conclusions. | [Research Architecture](docs/research_architecture.md) |
| **2** | **Does that physical description contain everything needed to explain the target?** If two cases look physically the same but the target still distinguishes them, the description is missing something relevant. | [P19 physical sufficiency](docs/proposition_19_fundamental_physical_sufficiency.md) |
| **3** | **Can we trust the target and how it was measured?** The target cannot simply be created from the same information we are trying to test. | [Target integrity path](docs/research_traceability_index.md#target-integrity-and-measurement-p71-p74) |
| **4** | **Does the proposed model actually match what we observe?** A model should be able to fail when the data do not support it. | [Model testing path](docs/research_traceability_index.md#model-adequacy-and-exact-separation-p75-p87) |
| **5** | **Does the result still hold on fresh data?** A result found during exploration should survive an independent test before we trust it. | [P88 held-out validation](docs/proposition_88_heldout_selected_parity_functional_certification.md) |

That is the central logic of the entire project.

---

## Current frontier: P88

![P88 held-out selected parity functional certification](docs/figures/p88_heldout_selected_parity_functional_certification.svg)

P88 asks a very practical question:

**If we find an interesting result in one set of data, does it still hold when we test it on new data that was not used to find it?**

For the stored example in this repository, the answer is yes under the stated assumptions. The result remains statistically detectable in the independent validation data.

That does **not** mean consciousness has been explained. It means one specific mathematical model can be rejected inside one specified region of its parameter space using a properly separated discovery and validation design.

### Want the technical details?

| What you want | Direct link |
| --- | --- |
| The theorem | [P88 theorem](docs/proposition_88_heldout_selected_parity_functional_certification.md) |
| Where the equations come from | [P88 equation provenance](docs/p88_equation_provenance.md) |
| The source code | [P88 implementation](src/consciousness_bridge/heldout_selected_parity_functional_certification.py) |
| The regression tests | [P88 tests](tests/test_heldout_selected_parity_functional_certification.py) |
| The figure | [P88 figure](docs/figures/p88_heldout_selected_parity_functional_certification.svg) |
| How to reproduce the repository | [Reproducibility Guide](docs/reproducibility.md) |

---

## What this project can and cannot say

| The research can show | It does not automatically show |
| --- | --- |
| A mathematical result follows from stated assumptions | That those assumptions are true in nature |
| A particular model does not fit the evidence | That consciousness is nonphysical |
| A hidden variable can be mathematically identified | That the hidden variable is consciousness |
| A model is compatible with current data | That the model is uniquely correct |
| A physical description is useful | That the physical-to-experiential bridge is complete |

The **physical-to-experiential bridge remains open**. That scientific boundary is intentional.

---

## Scientific status

The research currently contains **88 proposition-level results** and **72 equation-driven quantitative figures**. The theorem frontier is P88.

| Research status | Current value |
| --- | --- |
| Formal release | **v0.82.0** |
| Public theorem frontier | **P88** |
| Proposition-level results | **88** |
| Equation-driven quantitative figures | **72** |
| Physical-to-experiential bridge | **Open** |

The formal release number and theorem frontier are separate. New theorem work can advance before a new formal release is published.

Read the complete P1 to P88 detailed proposition record in [docs/detailed_proposition_record.md](docs/detailed_proposition_record.md). For a simpler path, use the [Research Traceability Index](docs/research_traceability_index.md).

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

The repository also supports Python 3.10, 3.11, and 3.12 in continuous integration. See [docs/reproducibility.md](docs/reproducibility.md) for the full reproducibility record.

---

## Explore by depth, not by folder

**Five minutes:** [Start Here](START_HERE.md)

**See the big picture:** [Research Architecture](docs/research_architecture.md)

**See the evidence:** [Figure Catalog](docs/figure_catalog.md)

**Follow one result all the way to code and tests:** [Research Traceability Index](docs/research_traceability_index.md)

**Review the full mathematics:** [Theorem Roadmap](docs/theorem_roadmap.md)

**Full technical audit:** [Detailed Proposition Record](docs/detailed_proposition_record.md) -> [Equation and Citation Map](docs/equation_and_citation_map.md) -> [Reproducibility Guide](docs/reproducibility.md)

---

## Related physical foundation

This project continues [Spatiotemporal Observer Mathematics](https://github.com/MahsaKeikha/spatiotemporal-observer-math), a separate completed research project on identifying a persistent moving subsystem from measured dynamics.

---

## Citation

See [CITATION.md](CITATION.md) and [CITATION.cff](CITATION.cff) for citation guidance.

Current theorem frontier: **P88**  
Formal release: **v0.82.0**

---

## License

MIT. See [LICENSE](LICENSE).
