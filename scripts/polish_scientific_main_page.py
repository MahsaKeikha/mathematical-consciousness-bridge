from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
text = README.read_text(encoding="utf-8")


def replace_once(old: str, new: str) -> None:
    global text
    if old not in text:
        raise SystemExit(f"Expected README block not found:\n{old[:180]}")
    text = text.replace(old, new, 1)


# Add a visual reading guide immediately after the scientific-status discipline.
status_tail = """**Quantum mechanics does not by itself imply consciousness.** A complete quantum state specifies the outcome statistics of declared measurements, but an experiential conclusion requires an additional bridge statement unless that bridge is independently derived.

---

# Research at a glance
"""
status_replacement = """**Quantum mechanics does not by itself imply consciousness.** A complete quantum state specifies the outcome statistics of declared measurements, but an experiential conclusion requires an additional bridge statement unless that bridge is independently derived.

---

# How to read this study

The main page is organized as a scientific argument rather than a chronological project log. A first-time reader can follow it in four passes: first identify the physical and experiential objects being compared; then inspect the intervention-resolved physical structure; next examine the exact and finite-data sufficiency tests; finally read the quantum, adaptive-experiment, falsification, and open-problem sections. Detailed proposition chronology and downstream calibration mathematics are linked separately so they do not interrupt the core argument.

| Reader question | Where the answer appears |
| --- | --- |
| **What is the scientific problem?** | Abstract, Research at a glance, and Section 1. |
| **What exactly is being measured and compared?** | Sections 1-4 and the measurement / response figures. |
| **What has actually been proved?** | Scientific status discipline, theorem roadmap, and “What has actually been established.” |
| **What would falsify the framework or a candidate bridge?** | Falsification logic and the linked falsification program. |
| **What remains unknown?** | “What remains open,” current scientific status, and the dedicated technical pages. |

![Universal proof ladder](docs/figures/universal_proof_ladder.svg)

**Figure 2. Scientific proof ladder.** A credible consciousness bridge must pass distinct layers: physical well-definedness, experiential well-definedness, non-circular bridge premises, representation invariance, physical-feature sufficiency, experimental recoverability, competing-theory discrimination, finite-data support, and explicit falsification. The figure is a requirements map, not a claim that every layer has already been closed.

---

# Research at a glance
"""
replace_once(status_tail, status_replacement)

# Improve the theorem-map transition and renumber its caption.
replace_once(
    "**Figure 2. Theorem dependency map.** Read from foundational identifiability toward the bridge tests and experimental-design branches. A later optimization theorem does not strengthen an earlier ontology claim. It solves the experimental problem stated at its own layer.",
    "**Figure 3. Theorem dependency map.** Read from foundational identifiability toward bridge tests and experimental-design branches. Each arrow is a mathematical dependency. Later optimization results improve how experiments are executed or certified; they do not retroactively strengthen an earlier ontological claim."
)

# Make the target variable legible to readers outside the project and add the empirical dissociation map.
target_block = """represent the target distinctions the proposed bridge claims to determine. The independence requirement matters: if $E$ is defined from $T$, factorization becomes circular and cannot test the physical description.

## 1.2 Exact deterministic sufficiency
"""
target_replacement = """represent the target distinctions the proposed bridge claims to determine. The independence requirement matters: if $E$ is defined from $T$, factorization becomes circular and cannot test the physical description.

A useful way to keep the notation straight is:

| Symbol | Role | Scientific requirement |
| --- | --- | --- |
| $\Omega$ | admissible physical states or histories | must be declared relative to a physical model and experiment class |
| $T$ | physical descriptor | must be operationally defined, representation-aware, and recoverable |
| $E$ | experiential target | must be specified independently enough to avoid definitional circularity |
| $B$ | candidate bridge law | must state how physical equivalence classes map to target distinctions |
| $R_{\mathrm{stoch}}$ | residual target information outside $T$ | must be interpreted under an explicit probabilistic model |

The target $E$ is intentionally not equated with verbal report or overt responsiveness. Dreaming, anesthesia, perturbational complexity, and covert command-related brain activation show why behavior, report, neural evidence, and experiential inference must be kept distinct (Casali et al., 2013; Sarasso et al., 2015; Siclari et al., 2017; Claassen et al., 2019; see the references below).

![Conscious-state measurement and dissociation map](docs/figures/conscious_state_measurement_map.svg)

**Figure 4. Measurement and dissociation map.** Behavioral responsiveness, subjective report, perturbational complexity, and command-related brain activation are different evidence channels. A bridge theory must state which pattern of observables it predicts and must remain testable when report or behavior is unavailable. The figure motivates the independent-target requirement; it does not define consciousness by any single measurement.

## 1.2 Exact deterministic sufficiency
"""
replace_once(target_block, target_replacement)

# Renumber and tighten the physical-to-experiential map caption.
replace_once(
    "**Figure 3. The logical gap being tested.** Fundamental physical theory determines physical structure and operational predictions. A consciousness theory still needs a justified map from physical equivalence classes to experiential equivalence classes. The purpose of the project is to make the required bridge and its possible failure conditions explicit.",
    "**Figure 5. The logical gap being tested.** Fundamental physical theory determines physical structure and operational predictions. A consciousness theory still requires a justified map from physical equivalence classes to experiential equivalence classes. The project makes that extra bridge explicit so its assumptions, regularity, uncertainty, and failure conditions can be tested rather than hidden inside terminology."
)

# Strengthen the causal section and add the information-geometry figure.
replace_once(
    "The intervention language is grounded in the causal distinction between observation and intervention developed in Pearl's causal framework. Empirically, perturbational approaches such as Casali et al. motivate direct probing of distributed neural response rather than relying only on passive correlation.",
    "The intervention language is grounded in the causal distinction between observation and intervention developed in Pearl's causal framework (Pearl, 2009). Empirically, perturbational approaches such as TMS-EEG motivate direct probing of distributed neural response rather than relying only on passive correlation (Casali et al., 2013)."
)
replace_once(
    "**Figure 4. Anatomy of the operational physical candidate.** Controlled interventions generate response distributions. Distances among those distributions define response geometry; comparisons across sources define directed influence; comparisons with partitioned null models expose irreducibility. These are physical candidates to be tested for sufficiency, not definitions of consciousness.\n\nThe intervention language",
    "**Figure 6. Anatomy of the operational physical candidate.** Controlled interventions generate response distributions. Distances among those distributions define response geometry; comparisons across sources define directed influence; comparisons with partitioned null models expose irreducibility. These are physical candidates to be tested for sufficiency, not definitions of consciousness.\n\n![Information geometry of intervention-response laws](docs/figures/information_geometry_response_manifold.svg)\n\n**Figure 7. Response laws as a physical geometry.** Parameterized intervention-conditioned probability laws can be studied with local statistical geometry and finite operational distances. Temporal trajectories, composition, and coarse-graining then become transformations of a physical response space. An experiential geometry would still require a separately justified bridge.\n\nThe intervention language"
)

# Renumber scale and finite-data figures.
replace_once(
    "**Figure 5. Scale sufficiency logic.**",
    "**Figure 8. Scale sufficiency logic.**"
)
replace_once(
    "**Figure 6. Multiscale hierarchy.**",
    "**Figure 9. Multiscale hierarchy.**"
)
replace_once(
    "**Figure 7. From exact factorization to finite-data evidence.**",
    "**Figure 10. From exact factorization to finite-data evidence.**"
)

# Add a direct visual handoff from the prior physical-observer project before the quantum branch.
fund_tail = """The repository also distinguishes scientific sources from speculative antecedents. Thomas W. Campbell's *My Big TOE* and similar consciousness-first proposals are **not treated as established scientific facts**. They may be discussed only as a **speculative, falsifiable antecedent**, but they are not used as assumptions in the theorem chain. The same evidential rule applies to any proposed consciousness-first ontology: conceptual inspiration and established physical evidence are different categories.

---

# 5. Quantum mechanics enters as a physical description, not as an assumption about consciousness
"""
fund_replacement = """The repository also distinguishes scientific sources from speculative antecedents. Thomas W. Campbell's *My Big TOE* and similar consciousness-first proposals are **not treated as established scientific facts**. They may be discussed only as a **speculative, falsifiable antecedent**, but they are not used as assumptions in the theorem chain. The same evidential rule applies to any proposed consciousness-first ontology: conceptual inspiration and established physical evidence are different categories.

![Observer-to-bridge research handoff](docs/figures/observer_to_bridge_handoff.svg)

**Figure 11. Research handoff.** The preceding Spatiotemporal Observer Mathematics project identifies and statistically certifies a physical subsystem from measured dynamics. This repository begins only after that physical object has been established and asks what additional causal, temporal, multiscale, and bridge structure is required. No experiential property is inserted at the handoff.

---

# 5. Quantum mechanics enters as a physical description, not as an assumption about consciousness
"""
replace_once(fund_tail, fund_replacement)

# Renumber quantum/adaptive figures.
for old, new in [
    ("**Figure 8. What quantum completeness does and does not establish.**", "**Figure 12. What quantum completeness does and does not establish.**"),
    ("**Figure 9. P38 quantum sufficiency test.**", "**Figure 13. P38 quantum sufficiency test.**"),
    ("**Figure 10. Finite-data quantum envelope.**", "**Figure 14. Finite-data quantum envelope.**"),
    ("**Figure 11. Adaptive evidence collection.**", "**Figure 15. Adaptive evidence collection.**"),
]:
    replace_once(old, new)

# Keep P61-P70 fully off the reader-facing main flow and correct the collapsed audit label.
replace_once(
    "<summary><strong>Permanent proof, figure, code, and test index: P39-P70</strong></summary>",
    "<summary><strong>Permanent proof, figure, code, and test index: P39-P60</strong></summary>"
)
replace_once(
    "This compact index preserves direct public traceability without placing thirty-two additional full-size figures in the main reading flow.",
    "This compact index preserves direct public traceability for the quantum and experiment-design continuation without placing every technical figure in the main reading flow. The P61-P70 calibration frontier is documented on its dedicated page."
)
replace_once(
    "9. **Experimental resources can be optimized and certified.** The P45-P70 branches give increasingly realistic allocation, scheduling, calibration, and optimality guarantees.",
    "9. **Experimental resources can be optimized and certified.** The experiment-design branch develops allocation, scheduling, stopping, and calibration guarantees; the detailed P61-P70 calibration sequence is documented separately so it does not dominate the scientific introduction."
)

# Add a theory-comparison visual after the falsification table.
fals_tail = """This is the intended scientific discipline: every positive claim should bring its own way of being wrong.

---

# Evidence, references, and provenance
"""
fals_replacement = """This is the intended scientific discipline: every positive claim should bring its own way of being wrong.

![Theory-comparative interface](docs/figures/theory_comparison_map.svg)

**Figure 16. Common interface for competing theory families.** Integrated Information Theory, Global Neuronal Workspace Theory, Recurrent Processing Theory, higher-order approaches, predictive / neurorepresentational families, and the repository's intervention-resolved physical candidate can be compared using the same categories: physical feature family, bridge architecture, measurement interface, and discriminating experiment. This framing follows the broader theory-comparison literature rather than treating any existing theory as the default answer (Seth & Bayne, 2022; Cogitate Consortium et al., 2025).

---

# Evidence, references, and provenance
"""
replace_once(fals_tail, fals_replacement)

# Add three empirical references used by the new measurement figure and prose.
refs_tail = """11. A. I. Luppi et al., \"Convergent transcriptomic and connectomic controllers of information integration and its anaesthetic breakdown across mammalian brains,\" *Nature Human Behaviour* 10 (2026), 777-802. [DOI 10.1038/s41562-025-02381-5](https://doi.org/10.1038/s41562-025-02381-5).

The complete bibliography is maintained in the dedicated reference documents above so this page can remain readable while every major scientific dependency stays auditable.
"""
refs_replacement = """11. A. I. Luppi et al., \"Convergent transcriptomic and connectomic controllers of information integration and its anaesthetic breakdown across mammalian brains,\" *Nature Human Behaviour* 10 (2026), 777-802. [DOI 10.1038/s41562-025-02381-5](https://doi.org/10.1038/s41562-025-02381-5).
12. F. Siclari et al., \"The neural correlates of dreaming,\" *Nature Neuroscience* 20 (2017), 872-878. [DOI 10.1038/nn.4545](https://doi.org/10.1038/nn.4545).
13. S. Sarasso et al., \"Consciousness and Complexity during Unresponsiveness Induced by Propofol, Xenon, and Ketamine,\" *Current Biology* 25(23) (2015), 3099-3105. [DOI 10.1016/j.cub.2015.10.014](https://doi.org/10.1016/j.cub.2015.10.014).
14. J. Claassen et al., \"Detection of Brain Activation in Unresponsive Patients with Acute Brain Injury,\" *New England Journal of Medicine* 380(26) (2019), 2497-2505. [DOI 10.1056/NEJMoa1812757](https://doi.org/10.1056/NEJMoa1812757).

The complete bibliography is maintained in the dedicated reference documents above so this page can remain readable while every major scientific dependency stays auditable.
"""
replace_once(refs_tail, refs_replacement)

# Renumber the evidence-provenance figure and strengthen the visual-atlas transition.
replace_once(
    "**Figure 13. Evidence provenance.**",
    "**Figure 17. Evidence provenance.**"
)
replace_once(
    "The main page intentionally shows the figures needed to understand the argument. The complete visual record remains available without forcing a first-time reader through every calibration plot.",
    "The main page intentionally shows the figures needed to understand the argument in scientific order. The complete visual record remains available for audit without forcing a first-time reader through every theorem-specific or calibration plot."
)

README.write_text(text, encoding="utf-8")

# Expand the curated-figure regression guard to match the new visual reading path.
p = ROOT / "tests" / "test_main_page_visual_paper.py"
s = p.read_text(encoding="utf-8")
for anchor, addition in [
    ('    "research_architecture.svg",\n', '    "universal_proof_ladder.svg",\n'),
    ('    "theorem_roadmap.svg",\n', '    "conscious_state_measurement_map.svg",\n'),
    ('    "causal_structure_anatomy.svg",\n', '    "information_geometry_response_manifold.svg",\n'),
    ('    "p20_finite_sample_residual_certificate.svg",\n', '    "observer_to_bridge_handoff.svg",\n'),
    ('    "p47_sequential_graph_refinement.svg",\n', '    "theory_comparison_map.svg",\n'),
]:
    if addition not in s:
        s = s.replace(anchor, anchor + addition, 1)
p.write_text(s, encoding="utf-8")

# Strengthen reader-order regression so every major post-status section stays on the main page.
p = ROOT / "tests" / "test_readme_research_orientation.py"
s = p.read_text(encoding="utf-8")
old = '''    status = text.index("# Scientific status discipline")
    glance = text.index("# Research at a glance")
    formulation = text.index("# 1. Mathematical formulation of the bridge problem")
    open_section = text.index("# What remains open")
    detail = text.index("# Detailed proposition record")

    assert plain < abstract < status < glance < formulation < open_section < detail
'''
new = '''    status = text.index("# Scientific status discipline")
    reading = text.index("# How to read this study")
    glance = text.index("# Research at a glance")
    formulation = text.index("# 1. Mathematical formulation of the bridge problem")
    operational = text.index("# 2. From physical dynamics to operational structure")
    scale = text.index("# 3. Time, composition, and scale cannot be ignored")
    finite = text.index("# 4. Turning a population theorem into a finite experiment")
    fundamental = text.index("# 4.4 Fundamental theory / Theory-of-Everything interface")
    quantum = text.index("# 5. Quantum mechanics enters as a physical description")
    adaptive = text.index("# 6. Adaptive experiment design")
    calibration = text.index("# 7. Calibration and optimization as a downstream experimental layer")
    established = text.index("# What has actually been established")
    open_section = text.index("# What remains open")
    falsification = text.index("# Falsification logic")
    evidence = text.index("# Evidence, references, and provenance")
    visuals = text.index("# Complete visual evidence without front-page overload")
    validation = text.index("# Numerical validation facts")
    reproducibility = text.index("# Reproducibility and audit path")
    detail = text.index("# Detailed proposition record")
    current = text.index("# Current scientific status")
    navigation = text.index("# Navigation")

    assert plain < abstract < status < reading < glance < formulation
    assert formulation < operational < scale < finite < fundamental < quantum < adaptive < calibration
    assert calibration < established < open_section < falsification < evidence < visuals < validation < reproducibility < detail < current < navigation
'''
if old not in s:
    raise SystemExit("Reader-order test block not found")
s = s.replace(old, new, 1)
p.write_text(s, encoding="utf-8")

# Tighten the calibration-frontier regression: theorem-specific P61-P70 labels remain off README.
p = ROOT / "tests" / "test_calibration_frontier_page.py"
s = p.read_text(encoding="utf-8")
needle = '''    for figure in (
'''
insert = '''    for label in (
        "# P61. Exact integer transition-calibration allocation",
        "# P62. Heterogeneous-cost transition calibration",
        "# P63. Exact heterogeneous-cost integer calibration",
        "# P64. Fast certified heterogeneous integer approximation",
        "# Proposition 65: lower-bounded heterogeneous calibration",
        "# Proposition 66: residual-exact calibration augmentation",
        "# Proposition 67: global integer optimality certificate",
        "# Proposition 68: Lagrangian optimality gap certificate",
        "# Proposition 69: certified dual-optimal multiplier search",
        "# Proposition 70: exact primal-dual gap decomposition",
    ):
        assert label not in README
        assert label in FRONTIER

    for figure in (
'''
if insert not in s:
    s = s.replace(needle, insert, 1)
p.write_text(s, encoding="utf-8")
