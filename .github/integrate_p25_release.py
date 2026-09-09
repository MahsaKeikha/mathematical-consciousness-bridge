from pathlib import Path


def replace_once(path: str, old: str, new: str, label: str) -> None:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(
            f"expected one marker for {label} in {path}, found {count}"
        )
    file_path.write_text(text.replace(old, new, 1), encoding="utf-8")


def require(path: str, token: str, label: str) -> None:
    if token not in Path(path).read_text(encoding="utf-8"):
        raise RuntimeError(f"missing requirement {label} in {path}")


# README ---------------------------------------------------------------------
replace_once(
    "README.md",
    "version-0.24.0-2563eb",
    "version-0.25.0-2563eb",
    "README version badge",
)
replace_once(
    "README.md",
    "**P24** converts that fixed-sample result into an anytime-valid certificate by allocating the total error budget across all positive sample sizes, giving simultaneous repeated-look and finite stopping-time validity under the declared finite-alphabet IID model.",
    "**P24** converts that fixed-sample result into an anytime-valid certificate by allocating the total error budget across all positive sample sizes, giving simultaneous repeated-look and finite stopping-time validity under the declared finite-alphabet IID model. **P25** returns to the P11 physical candidate and proves a directed-influence scale theorem: deterministic target coarse observation cannot increase matched-intervention influence, and P18 reconstruction defect bounds the loss by twice the uniform reconstruction error.",
    "README abstract P25 summary",
)
replace_once(
    "README.md",
    "**24 proposition-level results, 58 equation-driven quantitative figures",
    "**25 proposition-level results, 58 equation-driven quantitative figures",
    "README proposition record count",
)
replace_once(
    "README.md",
    "P1 through P24 in dependency order",
    "P1 through P25 with explicit dependency branches",
    "README theorem navigation range",
)
replace_once(
    "README.md",
    "| anytime refinement theorem | [Proposition 24](docs/proposition_24_anytime_adaptive_refinement_certification.md) | repeated-look, adaptive-selection, and finite stopping-time validity |",
    "| anytime refinement theorem | [Proposition 24](docs/proposition_24_anytime_adaptive_refinement_certification.md) | repeated-look, adaptive-selection, and finite stopping-time validity |\n| directed-influence scale theorem | [Proposition 25](docs/proposition_25_directed_influence_scale_certification.md) | P11 directed influence under P18 reconstruction-controlled target coarse observation |",
    "README P25 theorem navigation",
)
replace_once(
    "README.md",
    "| implementation of P24 | [anytime_refinement_certification.py](src/consciousness_bridge/anytime_refinement_certification.py) | anytime-valid adaptive refinement and stopping-time certificate |",
    "| implementation of P24 | [anytime_refinement_certification.py](src/consciousness_bridge/anytime_refinement_certification.py) | anytime-valid adaptive refinement and stopping-time certificate |\n| implementation of P25 | [directed_influence_scale_certification.py](src/consciousness_bridge/directed_influence_scale_certification.py) | directed-influence distortion and threshold-edge scale certificate |",
    "README P25 implementation navigation",
)
replace_once(
    "README.md",
    "| **11. P17-P18** | What is lost under coarse-graining, and when is a scale still sufficient? |",
    "| **11. P17-P18** | What is lost under coarse-graining, and when is a scale still sufficient? |\n| **11.1 P25 directed-influence scale** | When does P11 directed influence survive target coarse observation? |",
    "README P25 paper-map row",
)
replace_once(
    "README.md",
    "| proposition-level results | **24** |",
    "| proposition-level results | **25** |",
    "README proposition count",
)
replace_once(
    "README.md",
    "| research-software version | **0.24.0** |",
    "| research-software version | **0.25.0** |",
    "README software version",
)
replace_once(
    "README.md",
    "# 7. Theorem roadmap - P1 through P24",
    "# 7. Theorem roadmap - P1 through P25",
    "README theorem heading",
)
replace_once(
    "README.md",
    "| **P24** | summable alpha spending gives time-uniform adaptive-selection and finite stopping-time validity | proved anytime-valid theorem | [P24](docs/proposition_24_anytime_adaptive_refinement_certification.md) |",
    "| **P24** | summable alpha spending gives time-uniform adaptive-selection and finite stopping-time validity | proved anytime-valid theorem | [P24](docs/proposition_24_anytime_adaptive_refinement_certification.md) |\n| **P25** | P11 directed influence contracts under target coarse observation, with P18 reconstruction controlling the loss | proved physical scale theorem | [P25](docs/proposition_25_directed_influence_scale_certification.md) |",
    "README P25 theorem table row",
)

p18_end = """P18 does not automatically certify directed influence, partition structure, intervention semantics, quantum coherence, physical split/merge dynamics, or experiential properties.

---

# 14. Observer-to-bridge handoff"""
p25_readme = r"""P18 does not automatically certify directed influence, partition structure, intervention semantics, quantum coherence, physical split/merge dynamics, or experiential properties.

## 13.3 P25 - directed-influence scale certification

![P25 directed-influence scale certification](docs/figures/p25_directed_influence_scale_certification.svg)

P25 returns to the P11 directed-influence component and asks whether it survives deterministic coarse observation of the target response. Fix a source block \(i\), target block \(j\), delay \(\tau\), and the same matched intervention-pair family \(\mathcal E_i\) at both observational scales.

The fine directed influence is

\[
\boxed{
A_{i\to j}^{f}(\tau)
=
\sup_{(u,v)\in\mathcal E_i}
\|P_j^{u,\tau}-P_j^{v,\tau}\|_{\mathrm{TV}}.
}
\]

For deterministic target map \(C_j\), define

\[
\overline P_j^{u,\tau}=(C_j)_\#P_j^{u,\tau}
\]

and

\[
\boxed{
A_{i\to j}^{c}(\tau)
=
\sup_{(u,v)\in\mathcal E_i}
\|\overline P_j^{u,\tau}-\overline P_j^{v,\tau}\|_{\mathrm{TV}}.
}
\]

Total-variation contraction gives the first P25 statement:

\[
\boxed{
A_{i\to j}^{c}(\tau)
\le
A_{i\to j}^{f}(\tau).
}
\]

Thus deterministic target coarse observation cannot manufacture a larger P11 directed-influence value when intervention semantics are held fixed.

Now let \(R_j\) be a P18 fiber-consistent stochastic decoder and define

\[
\rho_{i\to j}(\tau)
=
\sup_u
\|P_j^{u,\tau}-(R_j)_\#(C_j)_\#P_j^{u,\tau}\|_{\mathrm{TV}},
\]

where the supremum is over interventions appearing in the matched-pair family. Applying the P18 pairwise distortion theorem before taking the P11 supremum gives

\[
\boxed{
0
\le
A_{i\to j}^{f}(\tau)-A_{i\to j}^{c}(\tau)
\le
2\rho_{i\to j}(\tau).
}
\]

Equivalently,

\[
\boxed{
A_{i\to j}^{c}(\tau)
\ge
A_{i\to j}^{f}(\tau)-2\rho_{i\to j}(\tau).
}
\]

Therefore exact reconstruction on the declared response family, \(\rho_{i\to j}(\tau)=0\), gives exact directed-influence preservation even when the target map is globally many-to-one.

For a declared edge threshold \(\theta\), P25 also yields the margin certificate

\[
\boxed{
A_{i\to j}^{f}(\tau)>\theta+2\rho_{i\to j}(\tau)
\Longrightarrow
A_{i\to j}^{c}(\tau)>\theta.
}
\]

Conversely, contraction gives

\[
A_{i\to j}^{c}(\tau)>\theta
\Longrightarrow
A_{i\to j}^{f}(\tau)>\theta.
\]

So coarse observation cannot create a threshold edge relative to the same fine intervention semantics, while a sufficiently strong fine edge is guaranteed to survive coarse observation.

The theorem has a deliberately narrow physical scope. P25 certifies target-response observation coarse-graining. It does not yet certify source-node aggregation, changed intervention channels, partition irreducibility \(\mathcal K\), genuine physical fusion, the entire P11 structure, physical completeness, or experience.

[Read Proposition 25](docs/proposition_25_directed_influence_scale_certification.md). The [P25 theorem map](docs/figures/p25_directed_influence_scale_certification.svg), [implementation](src/consciousness_bridge/directed_influence_scale_certification.py), and [tests](tests/test_directed_influence_scale_certification.py) expose the complete proof-to-code path.

---

# 14. Observer-to-bridge handoff"""
replace_once("README.md", p18_end, p25_readme, "README P25 scale section")

replace_once(
    "README.md",
    "P17 shows that coarse-graining can erase distinctions. P18 quantifies when reconstruction is good enough to retain the declared response geometry.",
    "P17 shows that coarse-graining can erase distinctions. P18 quantifies when reconstruction is good enough to retain the declared response geometry. P25 extends that control to the P11 directed-influence component under fixed intervention semantics and target observation coarse-graining.",
    "README P25 falsification scale update",
)

# Theorem roadmap prose ------------------------------------------------------
replace_once(
    "docs/theorem_roadmap.md",
    "![P1-P24 theorem roadmap](figures/theorem_roadmap.svg)",
    "![P1-P25 theorem roadmap](figures/theorem_roadmap.svg)",
    "roadmap image alt",
)
replace_once(
    "docs/theorem_roadmap.md",
    "| [P24](proposition_24_anytime_adaptive_refinement_certification.md) | summable alpha spending plus countable union control | repeated-look adaptive refinement and finite stopping-time validity | proved anytime-valid theorem |",
    "| [P24](proposition_24_anytime_adaptive_refinement_certification.md) | summable alpha spending plus countable union control | repeated-look adaptive refinement and finite stopping-time validity | proved anytime-valid theorem |\n| [P25](proposition_25_directed_influence_scale_certification.md) | P11 influence plus P18 reconstruction distortion | directed-influence preservation and edge-margin certification across target observation scale | proved physical scale theorem |",
    "roadmap P25 proposition row",
)

p18_marker = """If \(\rho_{\mathcal F}=0\), pairwise response geometry is preserved exactly even when \(C\) is globally many-to-one. The relevant requirement is family sufficiency, not microscopic invertibility everywhere.

---

# 8. Fundamental physical sufficiency: P19"""
p25_roadmap = r"""If \(\rho_{\mathcal F}=0\), pairwise response geometry is preserved exactly even when \(C\) is globally many-to-one. The relevant requirement is family sufficiency, not microscopic invertibility everywhere.

## P25 - directed-influence scale certification from P11 + P18

P25 is a branch extension of the physical scale program, not a consequence of P24. It combines the P11 directed-influence definition with the P18 reconstruction theorem.

For fixed source \(i\), target \(j\), delay \(\tau\), and matched intervention family \(\mathcal E_i\),

\[
A_{i\to j}^{f}(\tau)
=
\sup_{(u,v)\in\mathcal E_i}
\|P_j^{u,\tau}-P_j^{v,\tau}\|_{\mathrm{TV}}.
\]

A deterministic target map \(C_j\) gives

\[
\boxed{A_{i\to j}^{c}(\tau)\le A_{i\to j}^{f}(\tau).}
\]

If a P18 decoder reconstructs all relevant target response laws with uniform defect \(\rho_{i\to j}(\tau)\), then

\[
\boxed{
0\le
A_{i\to j}^{f}(\tau)-A_{i\to j}^{c}(\tau)
\le2\rho_{i\to j}(\tau).
}
\]

Hence for threshold \(\theta\),

\[
\boxed{
A_{i\to j}^{f}(\tau)>\theta+2\rho_{i\to j}(\tau)
\Longrightarrow
A_{i\to j}^{c}(\tau)>\theta.
}
\]

The theorem controls observation loss for \(\mathcal A\). It does not yet solve block aggregation, changing intervention semantics, or scale behavior of \(\mathcal K\).

Direct proof: [Proposition 25](proposition_25_directed_influence_scale_certification.md). Implementation: [directed_influence_scale_certification.py](../src/consciousness_bridge/directed_influence_scale_certification.py). Tests: [test_directed_influence_scale_certification.py](../tests/test_directed_influence_scale_certification.py).

---

# 8. Fundamental physical sufficiency: P19"""
replace_once(
    "docs/theorem_roadmap.md",
    p18_marker,
    p25_roadmap,
    "roadmap P25 branch section",
)
replace_once(
    "docs/theorem_roadmap.md",
    "# 15. Current frontier",
    "# 15. Current frontier",
    "roadmap stable frontier heading",
)
replace_once(
    "docs/theorem_roadmap.md",
    "1. extend scale certification from response geometry \\(\\mathcal G\\) to directed influence \\(\\mathcal A\\) under block-compatible coarse maps;",
    "1. extend P25 from target observation coarse-graining to genuine block aggregation with source/intervention compatibility;",
    "roadmap post-P25 frontier",
)

# Global theorem roadmap SVG: add an explicit dependency branch from P11 + P18.
replace_once(
    "docs/figures/theorem_roadmap.svg",
    'height="2180" viewBox="0 0 1600 2180"',
    'height="2410" viewBox="0 0 1600 2410"',
    "roadmap SVG dimensions",
)
replace_once(
    "docs/figures/theorem_roadmap.svg",
    "Theorem roadmap through Proposition 24",
    "Theorem roadmap through Proposition 25",
    "roadmap SVG title",
)
replace_once(
    "docs/figures/theorem_roadmap.svg",
    "Theorem Roadmap - P1 through P24",
    "Theorem Roadmap - P1 through P25",
    "roadmap SVG heading",
)
old_svg_tail = '''  <path class="arrow" d="M800 2055 V2090"/>

  <rect x="95" y="2102" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="2127" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="2150" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Sharper time-uniform inference, physical completeness, replication, and experiential formalization remain open.</text>
</svg>
'''
new_svg_tail = '''  <rect x="225" y="2100" width="1150" height="190" rx="20" fill="#f0fdfa" stroke="#0d9488" stroke-width="1.8"/>
  <text x="265" y="2137" class="label">PHYSICAL SCALE BRANCH · P25</text>
  <text x="265" y="2175" class="head">P11 directed influence + P18 reconstruction control</text>
  <text x="265" y="2209" class="body">Target coarse observation cannot increase matched-pair influence.</text>
  <text x="265" y="2244" class="eq">0 ≤ Af − Ac ≤ 2ρ</text>
  <text x="725" y="2244" class="eq">Af &gt; θ + 2ρ ⇒ Ac &gt; θ</text>
  <text x="265" y="2274" class="body">Dependency branch: P11 + P18; P24 is not a mathematical prerequisite.</text>

  <rect x="95" y="2320" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="2345" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="2368" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Partition scale, block aggregation, physical completeness, and experiential formalization remain open.</text>
</svg>
'''
replace_once(
    "docs/figures/theorem_roadmap.svg",
    old_svg_tail,
    new_svg_tail,
    "roadmap SVG P25 branch",
)

# Reader navigation ---------------------------------------------------------
replace_once(
    "docs/research_navigation.md",
    "for the dependency structure from P1 through P24.",
    "for the dependency structure from P1 through P25, including the P11+P18 branch to P25.",
    "navigation theorem range",
)
replace_once(
    "docs/research_navigation.md",
    "10. [Proposition 24](proposition_24_anytime_adaptive_refinement_certification.md) for time-uniform repeated-look and finite stopping-time validity.\n11. [Fundamental Theory to Consciousness program]",
    "10. [Proposition 24](proposition_24_anytime_adaptive_refinement_certification.md) for time-uniform repeated-look and finite stopping-time validity.\n11. [Proposition 25](proposition_25_directed_influence_scale_certification.md) for P11 directed-influence preservation under P18 reconstruction-controlled target coarse observation.\n12. [Fundamental Theory to Consciousness program]",
    "navigation P25 reading order start",
)
replace_once(
    "docs/research_navigation.md",
    "12. [Stochastic fundamental bridge]",
    "13. [Stochastic fundamental bridge]",
    "navigation renumber stochastic",
)
replace_once(
    "docs/research_navigation.md",
    "13. [Falsification program]",
    "14. [Falsification program]",
    "navigation renumber falsification",
)
replace_once(
    "docs/research_navigation.md",
    "14. [Citation and Reference Policy]",
    "15. [Citation and Reference Policy]",
    "navigation renumber citation",
)
replace_once(
    "docs/research_navigation.md",
    "| P24 | [Anytime adaptive refinement certification](proposition_24_anytime_adaptive_refinement_certification.md) | repeated-look validity, adaptive selection, and finite stopping-time control |",
    "| P24 | [Anytime adaptive refinement certification](proposition_24_anytime_adaptive_refinement_certification.md) | repeated-look validity, adaptive selection, and finite stopping-time control |\n| P25 | [Directed-influence scale certification](proposition_25_directed_influence_scale_certification.md) | P11 directed-influence distortion and edge preservation under P18 reconstruction control |",
    "navigation P25 index row",
)
replace_once(
    "docs/research_navigation.md",
    "| [P24 anytime adaptive refinement certification](proposition_24_anytime_adaptive_refinement_certification.md) | time-uniform coverage for repeated inspection and finite stopping times |",
    "| [P24 anytime adaptive refinement certification](proposition_24_anytime_adaptive_refinement_certification.md) | time-uniform coverage for repeated inspection and finite stopping times |\n| [P25 directed-influence scale certification](proposition_25_directed_influence_scale_certification.md) | P11 directed influence under target observation coarse-graining with P18 reconstruction control |",
    "navigation P25 interface row",
)
replace_once(
    "docs/research_navigation.md",
    "The P24 anytime-valid layer is implemented in [anytime_refinement_certification.py](../src/consciousness_bridge/anytime_refinement_certification.py), tested in [test_anytime_refinement_certification.py](../tests/test_anytime_refinement_certification.py), and summarized by [p24_anytime_adaptive_refinement_certification.svg](figures/p24_anytime_adaptive_refinement_certification.svg).",
    "The P24 anytime-valid layer is implemented in [anytime_refinement_certification.py](../src/consciousness_bridge/anytime_refinement_certification.py), tested in [test_anytime_refinement_certification.py](../tests/test_anytime_refinement_certification.py), and summarized by [p24_anytime_adaptive_refinement_certification.svg](figures/p24_anytime_adaptive_refinement_certification.svg). The P25 physical scale layer is implemented in [directed_influence_scale_certification.py](../src/consciousness_bridge/directed_influence_scale_certification.py), tested in [test_directed_influence_scale_certification.py](../tests/test_directed_influence_scale_certification.py), and summarized by [p25_directed_influence_scale_certification.svg](figures/p25_directed_influence_scale_certification.svg).",
    "navigation P25 implementation",
)

# Equation and citation provenance -----------------------------------------
p24_boundary = """P24 uses a transparent alpha-spending union-bound construction. It is intentionally conservative and is not claimed to be an optimal confidence sequence. Anytime statistical validity does not establish physical completeness or experiential interpretation.

---

# 19. Candidate consciousness-theory feature families"""
p25_provenance = r"""P24 uses a transparent alpha-spending union-bound construction. It is intentionally conservative and is not claimed to be an optimal confidence sequence. Anytime statistical validity does not establish physical completeness or experiential interpretation.

---

# 19. P25 - directed-influence scale certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(A_{i\to j}^{f}(\tau)=\sup_{(u,v)\in\mathcal E_i}\|P_j^{u,\tau}-P_j^{v,\tau}\|_{\mathrm{TV}}\) | fine P11 directed perturbational influence | repository physical-signature definition | [P11](proposition_11_intervention_resolved_causal_structure.md) |
| \(\overline P_j^{u,\tau}=(C_j)_\#P_j^{u,\tau}\) | deterministic target observation coarse-graining | standard pushforward applied to P11 marginal law | P17; [P25](proposition_25_directed_influence_scale_certification.md) |
| \(A_{i\to j}^{c}(\tau)\le A_{i\to j}^{f}(\tau)\) | coarse target observation cannot increase matched-pair influence | proved by TV contraction and supremum monotonicity | P17; [P25](proposition_25_directed_influence_scale_certification.md) |
| \(\rho_{i\to j}(\tau)=\sup_u\|P_j^{u,\tau}-R_{j\#}C_{j\#}P_j^{u,\tau}\|_{\mathrm{TV}}\) | uniform response-family reconstruction defect | P18 reconstruction object specialized to the P11 target family | [P18](proposition_18_scale_sufficiency_certification.md); [P25](proposition_25_directed_influence_scale_certification.md) |
| \(0\le A^f-A^c\le2\rho\) | directed-influence scale distortion theorem | proved | [P25](proposition_25_directed_influence_scale_certification.md) |
| \(A^f>\theta+2\rho\Rightarrow A^c>\theta\) | threshold-edge preservation margin | proved corollary | [P25](proposition_25_directed_influence_scale_certification.md) |
| \(A^c>\theta\Rightarrow A^f>\theta\) | no threshold false positive under deterministic target coarse observation | proved by contraction | [P25](proposition_25_directed_influence_scale_certification.md) |

P25 is a physical scale theorem with dependency branch P11 + P18. It does not establish scale stability of partition irreducibility, arbitrary source aggregation, changed intervention semantics, physical completeness, or experience.

---

# 20. Candidate consciousness-theory feature families"""
replace_once(
    "docs/equation_and_citation_map.md",
    p24_boundary,
    p25_provenance,
    "equation map P25 section",
)
replace_once(
    "docs/equation_and_citation_map.md",
    "# 20. Citation discipline",
    "# 21. Citation discipline",
    "equation map citation numbering",
)

# Tests ---------------------------------------------------------------------
replace_once(
    "tests/test_main_page_visual_paper.py",
    '    "p24_anytime_adaptive_refinement_certification.svg",\n',
    '    "p24_anytime_adaptive_refinement_certification.svg",\n    "p25_directed_influence_scale_certification.svg",\n',
    "main page P25 figure guard",
)
replace_once(
    "tests/test_main_page_visual_paper.py",
    "for index in range(1, 25):",
    "for index in range(1, 26):",
    "main page P25 theorem range",
)
replace_once(
    "tests/test_document_link_integrity.py",
    "for number in range(1, 25):",
    "for number in range(1, 26):",
    "navigation P25 theorem guard",
)
replace_once(
    "tests/test_visual_and_terminology_quality.py",
    '    "p24_anytime_adaptive_refinement_certification.svg",\n',
    '    "p24_anytime_adaptive_refinement_certification.svg",\n    "p25_directed_influence_scale_certification.svg",\n',
    "visual P25 figure guard",
)

# Release metadata ----------------------------------------------------------
replace_once(
    "pyproject.toml",
    'version = "0.24.0"',
    'version = "0.25.0"',
    "pyproject version",
)
replace_once(
    "pyproject.toml",
    "anytime-valid refinement certification, recoverability, and falsifiable experiment design.",
    "anytime-valid refinement certification, directed-influence scale certification, recoverability, and falsifiable experiment design.",
    "pyproject P25 description",
)
replace_once(
    "src/consciousness_bridge/__init__.py",
    '__version__ = "0.24.0"',
    '__version__ = "0.25.0"',
    "runtime version",
)
replace_once(
    "CITATION.cff",
    "version: 0.24.0",
    "version: 0.25.0",
    "citation version",
)
replace_once(
    "CITATION.cff",
    "adaptive descriptor-selection certification, anytime-valid refinement certification, robust experiment design",
    "adaptive descriptor-selection certification, anytime-valid refinement certification, directed-influence scale certification, robust experiment design",
    "citation P25 abstract",
)

changelog_header = "# Changelog\n\nThis changelog records theorem-level scientific releases. Definitions, proofs, implementations, tests, figures, and documentation remain linked from the main research page.\n\n"
p25_changelog = r"""# Changelog

This changelog records theorem-level scientific releases. Definitions, proofs, implementations, tests, figures, and documentation remain linked from the main research page.

## 0.25.0 - 2026-09-09

### Proposition 25 - directed-influence scale certification

- Returned to the P11 structured physical candidate and isolated the directed perturbational influence component for scale analysis.
- Proved that deterministic target observation coarse-graining cannot increase matched-intervention directed influence.
- Specialized the P18 fiber-consistent reconstruction defect to the intervention-conditioned target response family.
- Proved the sharp additive bound \(0\le A^f-A^c\le2\rho\).
- Proved exact directed-influence preservation when the declared response family reconstructs exactly.
- Derived the threshold-edge margin \(A^f>\theta+2\rho\Rightarrow A^c>\theta\) and the no-false-positive implication \(A^c>\theta\Rightarrow A^f>\theta\).
- Added an explicit binary counterexample saturating the \(2\rho\) loss bound.
- Added executable certification, regression tests, a publication theorem map, and an explicit P11+P18 dependency branch in the global roadmap.
- Preserved the boundary that P25 does not certify partition irreducibility, node fusion, changed intervention semantics, physical completeness, or experience.
- Integrated P25 into the README paper, navigation, equation provenance, release metadata, theorem guards, and visual-quality guards.

"""
replace_once("CHANGELOG.md", changelog_header, p25_changelog, "P25 changelog")

# Fail-fast postconditions ---------------------------------------------------
requirements = {
    "README.md": [
        "version-0.25.0-2563eb",
        "## 13.3 P25 - directed-influence scale certification",
        "# 7. Theorem roadmap - P1 through P25",
        "**25 proposition-level results",
        "p25_directed_influence_scale_certification.svg",
    ],
    "docs/theorem_roadmap.md": [
        "![P1-P25 theorem roadmap]",
        "P25 - directed-influence scale certification from P11 + P18",
        "proposition_25_directed_influence_scale_certification.md",
    ],
    "docs/figures/theorem_roadmap.svg": [
        "Theorem Roadmap - P1 through P25",
        "PHYSICAL SCALE BRANCH · P25",
        "P11 + P18",
    ],
    "docs/research_navigation.md": [
        "proposition_25_directed_influence_scale_certification.md",
        "directed_influence_scale_certification.py",
    ],
    "docs/equation_and_citation_map.md": [
        "# 19. P25 - directed-influence scale certification",
        "# 20. Candidate consciousness-theory feature families",
        "# 21. Citation discipline",
    ],
    "pyproject.toml": ['version = "0.25.0"'],
    "CITATION.cff": ["version: 0.25.0"],
    "src/consciousness_bridge/__init__.py": ['__version__ = "0.25.0"'],
    "CHANGELOG.md": ["## 0.25.0 - 2026-09-09"],
    "tests/test_main_page_visual_paper.py": [
        "p25_directed_influence_scale_certification.svg",
        "range(1, 26)",
    ],
    "tests/test_document_link_integrity.py": ["range(1, 26)"],
    "tests/test_visual_and_terminology_quality.py": [
        "p25_directed_influence_scale_certification.svg"
    ],
}

for path, tokens in requirements.items():
    for token in tokens:
        require(path, token, token)
