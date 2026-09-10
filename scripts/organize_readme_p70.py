from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

text = README.read_text(encoding="utf-8")

abstract_marker = "# Abstract\n\n"
chronology_marker = "The program here makes that bridge itself an object of mathematics."
quantum_marker = "A new quantum-foundations layer now asks a sharper question."
record_marker = "The public research record now contains **70 proposition-level results"
section_end_marker = "\n\n---\n\n"

abstract_start = text.index(abstract_marker)
chronology_start = text.index(chronology_marker, abstract_start)
quantum_start = text.index(quantum_marker, chronology_start)
record_start = text.index(record_marker, quantum_start)
abstract_end = text.index(section_end_marker, record_start) + len(section_end_marker)

opening = text[abstract_start + len(abstract_marker):chronology_start].strip()
chronology = text[chronology_start:quantum_start].strip()
quantum_paragraph = text[quantum_start:record_start].strip()
record_end = text.index("\n\n", record_start)
record_paragraph = text[record_start:record_end].strip()

new_abstract = f'''# Abstract

{opening}

This repository treats the physical-to-experiential bridge as a sequence of separately testable mathematical questions rather than as a single assumed identity. The program develops representation-invariant physical descriptors, intervention-resolved causal and temporal structure, exact and finite-data sufficiency tests, quantum operational tests, adaptive experiment design, and executable calibration optimization. Each proposition is labeled by what is actually proved, implemented, simulated, empirically supported, or still open.

The current result chain is organized into seven scientific stages: foundations and identifiability (P1-P10), structured causal and temporal candidates (P11-P18), bridge factorization and finite-data inference (P19-P24), multiscale operational structure (P25-P37), quantum sufficiency and falsification tests (P38-P44), adaptive experimental design and scheduling (P45-P58), and transition-calibration optimization and certification (P59-P70).

{quantum_paragraph}

{record_paragraph}

---

# Research at a glance

A reader should be able to understand the architecture before reading individual proofs. The table below gives the shortest faithful map of what has been built and where each part belongs.

| Scientific stage | Proposition range | Central question | Current status | Best entry point |
| --- | --- | --- | --- | --- |
| 1. Foundations and identifiability | **P1-P10** | What must be invariant, distinguishable, recoverable, and statistically testable before a physical descriptor can support any bridge claim? | Proved / implemented / tested | [Theorem roadmap](docs/theorem_roadmap.md) |
| 2. Causal, temporal, compositional, and scale structure | **P11-P18** | What structured physical information can be retained across interventions, time, composition, and coarse-graining? | Proved / implemented / tested | [Quantitative physics and mathematics atlas](docs/quantitative_physics_mathematics_atlas.md) |
| 3. Bridge factorization and finite-data inference | **P19-P24** | Does an independently declared target factor through a physical descriptor, and can insufficiency be certified from finite data and repeated looks? | Proved under declared models | [Research navigation](docs/research_navigation.md) |
| 4. Multiscale operational structure | **P25-P37** | Which causal and response structures survive node, state, intervention, and delay quotients, and how much distortion is introduced? | Proved / implemented / tested | [Theorem roadmap](docs/theorem_roadmap.md) |
| 5. Quantum sufficiency and falsification | **P38-P44** | What can and cannot be inferred from a declared tomographically complete quantum description, especially with finite-data uncertainty and bridge regularity assumptions? | Proved conditional tests; ontology remains open | [Quantum foundations atlas](docs/quantum_foundations_atlas.md) |
| 6. Adaptive experiment design and scheduling | **P45-P58** | How should evidence gathering, stopping, service allocation, switching, and noisy transition measurement be organized with valid uncertainty control? | Proved / implemented / tested | [Equation and citation map](docs/equation_and_citation_map.md) |
| 7. Transition calibration and integer optimization | **P59-P70** | How should finite calibration resources be allocated, rounded, optimized, certified, and diagnostically decomposed under heterogeneous costs? | Proved / implemented / tested | [P70 proposition](docs/proposition_70_primal_dual_gap_decomposition.md) |

## Current scientific status

| Item | Current state |
| --- | --- |
| Public theorem frontier | **P70** |
| Documented release | **v0.70.0** |
| Proposition-level results | **70** |
| Equation-driven quantitative figures | **61** |
| Reproducibility | Python 3.10, 3.11, and 3.12 test matrix plus theorem-specific regression guards |
| Physical-to-experiential bridge | **Open physical-to-experiential bridge** |
| Quantum ontology claim | **Not assumed** |
| Consciousness identified with a scalar, state of matter, or spacetime coordinate | **Not claimed** |

## How to navigate the research

| If you want to... | Start here |
| --- | --- |
| Understand the complete dependency structure | [Theorem roadmap](docs/theorem_roadmap.md) |
| Follow the work by scientific question rather than proposition number | [Research navigation](docs/research_navigation.md) |
| Check where equations, standard results, external evidence, and repository-original results come from | [Equation and citation map](docs/equation_and_citation_map.md) |
| Inspect figures before reading long proofs | [Visual atlas](website/visual-atlas.html) |
| Read the public research website | [Website entry point](website/index.html) |
| Audit the source code and regression tests | [Source package](src/consciousness_bridge/) and [tests](tests/) |
| Check the explicit scientific claim discipline | [Research publication architecture](docs/research_publication_architecture.md) |

The organizing principle is always the same:

\[
\boxed{
\text{{physical description}}
\longrightarrow
\text{{operational structure}}
\longrightarrow
\text{{sufficiency / insufficiency test}}
\longrightarrow
\text{{finite-data certification}}
\longrightarrow
\text{{experimental design}}
\longrightarrow
\text{{open bridge question}}.
}}
\]

Nothing later in the repository is allowed to silently strengthen an earlier result. A theorem about calibration remains a calibration theorem. A quantum operational test remains conditional on its declared descriptor and regularity class. An empirical observation remains empirical evidence. The final physical-to-experiential bridge remains open until independently justified mathematics and evidence close it.

---

# Detailed proposition record

The full chronological record is preserved here for readers who want proposition-by-proposition lineage after seeing the architecture above.

<details>
<summary><strong>Open the complete P1 to P70 chronology</strong></summary>

{chronology}

</details>

---

'''

text = text[:abstract_start] + new_abstract + text[abstract_end:]

# Remove stale duplicate research-record counts later in the README without
# removing the useful table itself.
text = text.replace("# Research record at a glance", "# Repository scale and validation record", 1)
text = text.replace("| proposition-level results | **45** |", "| proposition-level results | **70** |", 1)
text = text.replace(
    "| equation-driven classical/causal quantitative figures | **40** |",
    "| equation-driven classical/causal and optimization figures | **43** |",
    1,
)
text = text.replace(
    "| total equation-driven quantitative figures | **58** |",
    "| total equation-driven quantitative figures | **61** |",
    1,
)

README.write_text(text, encoding="utf-8")
