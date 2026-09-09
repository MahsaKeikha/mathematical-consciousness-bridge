from pathlib import Path


def replace_once(path: str, old: str, new: str, label: str) -> None:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected one marker for {label} in {path}, found {count}")
    file_path.write_text(text.replace(old, new, 1), encoding="utf-8")


def require(path: str, token: str, label: str) -> None:
    if token not in Path(path).read_text(encoding="utf-8"):
        raise RuntimeError(f"missing requirement {label} in {path}")


# README metadata and summary.
replace_once("README.md", "version-0.28.0-2563eb", "version-0.29.0-2563eb", "README badge")
replace_once("README.md", "**28 proposition-level results", "**29 proposition-level results", "README result count")
replace_once("README.md", "P1 through P28 with explicit dependency branches", "P1 through P29 with explicit dependency branches", "README theorem range")
replace_once("README.md", "| proposition-level results | **28** |", "| proposition-level results | **29** |", "README proposition count")
replace_once("README.md", "| research-software version | **0.28.0** |", "| research-software version | **0.29.0** |", "README version table")
replace_once("README.md", "# 7. Theorem roadmap - P1 through P28", "# 7. Theorem roadmap - P1 through P29", "README theorem heading")
replace_once("README.md", "the P1-P28 proposition chain", "the P1-P29 proposition chain", "README reproducibility range")
replace_once(
    "README.md",
    "**P28** transports the P11 directed-influence branch through the same changing node set by giving an exact compatibility criterion for matched intervention-pair source labels, pooling only inherited comparisons within each aggregate source, and applying P25/P18 control to the full fine target fiber before target-state aggregation.",
    "**P28** transports the P11 directed-influence branch through the same changing node set by giving an exact compatibility criterion for matched intervention-pair source labels, pooling only inherited comparisons within each aggregate source, and applying P25/P18 control to the full fine target fiber before target-state aggregation. **P29** transports the complete P11 response geometry on a fixed intervention-delay grid: every pairwise total-variation response distance contracts under node aggregation, while P18 reconstruction bounds the sup-norm distortion of the entire indexed geometry by twice the uniform reconstruction defect.",
    "README abstract P29",
)
replace_once(
    "README.md",
    "| intervention node-aggregation theorem | [Proposition 28](docs/proposition_28_intervention_node_aggregation_compatibility.md) | source-label descent and directed-influence certification across aggregate source and target nodes |",
    "| intervention node-aggregation theorem | [Proposition 28](docs/proposition_28_intervention_node_aggregation_compatibility.md) | source-label descent and directed-influence certification across aggregate source and target nodes |\n| response-geometry node-aggregation theorem | [Proposition 29](docs/proposition_29_response_geometry_node_aggregation.md) | complete intervention-delay response pseudometric under node aggregation with P18 distortion control |",
    "README P29 nav row",
)
replace_once(
    "README.md",
    "| implementation of P28 | [intervention_node_aggregation_compatibility.py](src/consciousness_bridge/intervention_node_aggregation_compatibility.py) | matched-pair source descent and aggregate-source/target directed-influence certificate |",
    "| implementation of P28 | [intervention_node_aggregation_compatibility.py](src/consciousness_bridge/intervention_node_aggregation_compatibility.py) | matched-pair source descent and aggregate-source/target directed-influence certificate |\n| implementation of P29 | [response_geometry_node_aggregation.py](src/consciousness_bridge/response_geometry_node_aggregation.py) | complete indexed response-geometry contraction and P18 reconstruction certificate |",
    "README P29 implementation row",
)
replace_once(
    "README.md",
    "| **11.4 P28 intervention compatibility under node aggregation** | When do matched intervention comparisons retain an unambiguous source meaning after node aggregation? |",
    "| **11.4 P28 intervention compatibility under node aggregation** | When do matched intervention comparisons retain an unambiguous source meaning after node aggregation? |\n| **11.5 P29 response geometry under node aggregation** | How much can the complete intervention-delay response pseudometric change under the same node quotient? |",
    "README P29 paper map row",
)
replace_once(
    "README.md",
    "| **P28** | matched intervention-pair source labels descend iff each pair has at most one coarse source image; aggregate-source influence then contracts under target-fiber state aggregation with P18 reconstruction control | proved physical scale theorem | [P28](docs/proposition_28_intervention_node_aggregation_compatibility.md) |",
    "| **P28** | matched intervention-pair source labels descend iff each pair has at most one coarse source image; aggregate-source influence then contracts under target-fiber state aggregation with P18 reconstruction control | proved physical scale theorem | [P28](docs/proposition_28_intervention_node_aggregation_compatibility.md) |\n| **P29** | every response-geometry entry on the fixed intervention-delay grid contracts under node aggregation, with complete sup-norm geometry distortion bounded by P18 reconstruction | proved physical scale theorem | [P29](docs/proposition_29_response_geometry_node_aggregation.md) |",
    "README P29 theorem row",
)

p28_end = r"""[Read Proposition 28](docs/proposition_28_intervention_node_aggregation_compatibility.md). The [P28 theorem map](docs/figures/p28_intervention_node_aggregation_compatibility.svg), [implementation](src/consciousness_bridge/intervention_node_aggregation_compatibility.py), and [tests](tests/test_intervention_node_aggregation_compatibility.py) expose the complete proof-to-code path.

---

# 14. Observer-to-bridge handoff"""
p29_section = r"""[Read Proposition 28](docs/proposition_28_intervention_node_aggregation_compatibility.md). The [P28 theorem map](docs/figures/p28_intervention_node_aggregation_compatibility.svg), [implementation](src/consciousness_bridge/intervention_node_aggregation_compatibility.py), and [tests](tests/test_intervention_node_aggregation_compatibility.py) expose the complete proof-to-code path.

## 13.7 P29 - response-geometry transport under node aggregation

![P29 response-geometry transport under node aggregation](docs/figures/p29_response_geometry_node_aggregation.svg)

P29 completes the changing-node transport analysis for the third central P11 component, the response geometry \(\mathcal G\). It keeps the intervention labels \(\mathcal U\) and delay labels \(\mathcal T\) fixed and changes only the physical response representation through the P27 node quotient and its aggregate-state map.

For every intervention pair and retained delay,

\[
\boxed{
G_f(u,v,\tau)
=
\|P^{u,\tau}-P^{v,\tau}\|_{\mathrm{TV}}.
}
\]

After the aggregation-compatible state map \(C_a\),

\[
\overline P^{u,\tau}=(C_a)_\#P^{u,\tau},
\]

and

\[
\boxed{
G_c(u,v,\tau)
=
\|\overline P^{u,\tau}-\overline P^{v,\tau}\|_{\mathrm{TV}}.
}
\]

Total-variation data processing gives an entrywise theorem over the complete declared experiment grid:

\[
\boxed{
0\le G_f(u,v,\tau)-G_c(u,v,\tau)
\quad\forall u,v,\tau.
}
\]

Let \(D=R_\#(C_a)_\#\) be the P18 reconstruction operator and define

\[
\rho_{u,\tau}
=
\|P^{u,\tau}-DP^{u,\tau}\|_{\mathrm{TV}}.
\]

P18 gives the sharper law-specific bound

\[
\boxed{
0\le
G_f(u,v,\tau)-G_c(u,v,\tau)
\le
\rho_{u,\tau}+\rho_{v,\tau}.
}
\]

For the uniform declared-family defect

\[
\rho_*
=
\sup_{u,\tau}\rho_{u,\tau},
\]

all geometry entries are controlled simultaneously:

\[
\boxed{
\|\mathcal G_f-\mathcal G_c\|_\infty
\le2\rho_*.
}
\]

Thus \(\rho_*=0\) gives exact preservation of the complete indexed response geometry, not merely preservation of its diameter. As corollaries,

\[
\boxed{
0\le\Delta_f-\Delta_c\le2\rho_*
}
\]

for response diameters, and a fine separation satisfying

\[
G_f(u,v,\tau)>\theta+2\rho_*
\]

must remain above \(\theta\) after aggregation.

The common index grid is an explicit scientific assumption:

\[
\boxed{
\text{state-space aggregation}
\neq
\text{intervention aggregation}
\neq
\text{time aggregation}.
}
\]

P29 does not merge intervention labels or identify different delays. Those operations require separate compatibility theorems.

At this point P27, P28, and P29 provide changing-node transport rules for the three central P11 components

\[
\boxed{
\mathcal K,
\qquad
\mathcal A,
\qquad
\mathcal G.
}
\]

That still does not by itself establish full P11 scale equivalence. A simultaneous assembly theorem must require one common node quotient, aggregate-state map, intervention semantics, delay semantics, and reconstruction family and prove all component correspondences on the same compatibility diagram.

[Read Proposition 29](docs/proposition_29_response_geometry_node_aggregation.md). The [P29 theorem map](docs/figures/p29_response_geometry_node_aggregation.svg), [implementation](src/consciousness_bridge/response_geometry_node_aggregation.py), and [tests](tests/test_response_geometry_node_aggregation.py) expose the complete proof-to-code path.

---

# 14. Observer-to-bridge handoff"""
replace_once("README.md", p28_end, p29_section, "README P29 section")
replace_once(
    "README.md",
    "P28 adds the source-side compatibility condition required to transport matched intervention comparisons and directed influence through that same node quotient.",
    "P28 adds the source-side compatibility condition required to transport matched intervention comparisons and directed influence through that same node quotient. P29 then controls the complete P11 response geometry on the unchanged intervention-delay experiment grid.",
    "README scale falsification P29",
)

# Theorem roadmap.
replace_once("docs/theorem_roadmap.md", "![P1-P28 theorem roadmap]", "![P1-P29 theorem roadmap]", "roadmap alt")
replace_once(
    "docs/theorem_roadmap.md",
    "| [P28](proposition_28_intervention_node_aggregation_compatibility.md) | P11 matched-pair source incidence plus P25 target contraction and P27 node aggregation | exact source-label descent and directed-influence certification across aggregate nodes | proved physical scale theorem |",
    "| [P28](proposition_28_intervention_node_aggregation_compatibility.md) | P11 matched-pair source incidence plus P25 target contraction and P27 node aggregation | exact source-label descent and directed-influence certification across aggregate nodes | proved physical scale theorem |\n| [P29](proposition_29_response_geometry_node_aggregation.md) | P11 response geometry plus P17 contraction, P18 reconstruction, and P27 node aggregation | complete indexed response-pseudometric transport on a fixed intervention-delay grid | proved physical scale theorem |",
    "roadmap P29 index row",
)
p28_roadmap_end = r"""Direct proof: [Proposition 28](proposition_28_intervention_node_aggregation_compatibility.md). Implementation: [intervention_node_aggregation_compatibility.py](../src/consciousness_bridge/intervention_node_aggregation_compatibility.py). Tests: [test_intervention_node_aggregation_compatibility.py](../tests/test_intervention_node_aggregation_compatibility.py).

---

# 8. Fundamental physical sufficiency: P19"""
p29_roadmap = r"""Direct proof: [Proposition 28](proposition_28_intervention_node_aggregation_compatibility.md). Implementation: [intervention_node_aggregation_compatibility.py](../src/consciousness_bridge/intervention_node_aggregation_compatibility.py). Tests: [test_intervention_node_aggregation_compatibility.py](../tests/test_intervention_node_aggregation_compatibility.py).

## P29 - response-geometry transport under node aggregation

For the same declared intervention and delay labels at both scales,

\[
G_f(u,v,\tau)=\|P^{u,\tau}-P^{v,\tau}\|_{\mathrm{TV}},
\]

while \(\overline P^{u,\tau}=(C_a)_\#P^{u,\tau}\) gives

\[
G_c(u,v,\tau)=\|\overline P^{u,\tau}-\overline P^{v,\tau}\|_{\mathrm{TV}}.
\]

P17 and P18 imply

\[
\boxed{
0\le G_f(u,v,\tau)-G_c(u,v,\tau)
\le\rho_{u,\tau}+\rho_{v,\tau}.
}
\]

With \(\rho_*=\sup_{u,\tau}\rho_{u,\tau}\),

\[
\boxed{
\|\mathcal G_f-\mathcal G_c\|_\infty\le2\rho_*.
}
\]

Exact reconstruction preserves the entire response geometry. P29 deliberately does not merge interventions or resample delays.

Direct proof: [Proposition 29](proposition_29_response_geometry_node_aggregation.md). Implementation: [response_geometry_node_aggregation.py](../src/consciousness_bridge/response_geometry_node_aggregation.py). Tests: [test_response_geometry_node_aggregation.py](../tests/test_response_geometry_node_aggregation.py).

---

# 8. Fundamental physical sufficiency: P19"""
replace_once("docs/theorem_roadmap.md", p28_roadmap_end, p29_roadmap, "roadmap P29 section")

# Research navigation.
replace_once("docs/research_navigation.md", "from P1 through P28", "from P1 through P29", "navigation range")
replace_once(
    "docs/research_navigation.md",
    "14. [Proposition 28](proposition_28_intervention_node_aggregation_compatibility.md) for source-label descent and directed-influence certification under node aggregation.\n15. [Fundamental Theory to Consciousness program]",
    "14. [Proposition 28](proposition_28_intervention_node_aggregation_compatibility.md) for source-label descent and directed-influence certification under node aggregation.\n15. [Proposition 29](proposition_29_response_geometry_node_aggregation.md) for complete response-geometry transport under node aggregation on a fixed intervention-delay grid.\n16. [Fundamental Theory to Consciousness program]",
    "navigation reading P29",
)
replace_once("docs/research_navigation.md", "16. [Stochastic fundamental bridge]", "17. [Stochastic fundamental bridge]", "navigation number 17")
replace_once("docs/research_navigation.md", "17. [Falsification program]", "18. [Falsification program]", "navigation number 18")
replace_once("docs/research_navigation.md", "18. [Citation and Reference Policy]", "19. [Citation and Reference Policy]", "navigation number 19")
replace_once(
    "docs/research_navigation.md",
    "| P28 | [Intervention node-aggregation compatibility](proposition_28_intervention_node_aggregation_compatibility.md) | exact matched-pair source descent and aggregate-node directed-influence control |",
    "| P28 | [Intervention node-aggregation compatibility](proposition_28_intervention_node_aggregation_compatibility.md) | exact matched-pair source descent and aggregate-node directed-influence control |\n| P29 | [Response-geometry node aggregation](proposition_29_response_geometry_node_aggregation.md) | complete intervention-delay response pseudometric under node aggregation with P18 distortion control |",
    "navigation P29 index row",
)
replace_once(
    "docs/research_navigation.md",
    "| [P28 intervention node-aggregation compatibility](proposition_28_intervention_node_aggregation_compatibility.md) | matched intervention semantics and directed influence across aggregate source and target nodes |",
    "| [P28 intervention node-aggregation compatibility](proposition_28_intervention_node_aggregation_compatibility.md) | matched intervention semantics and directed influence across aggregate source and target nodes |\n| [P29 response-geometry node aggregation](proposition_29_response_geometry_node_aggregation.md) | full response geometry on the fixed intervention-delay grid under aggregate response states |",
    "navigation P29 interface row",
)
replace_once(
    "docs/research_navigation.md",
    "and summarized by [p28_intervention_node_aggregation_compatibility.svg](figures/p28_intervention_node_aggregation_compatibility.svg).",
    "and summarized by [p28_intervention_node_aggregation_compatibility.svg](figures/p28_intervention_node_aggregation_compatibility.svg). The P29 response-geometry layer is implemented in [response_geometry_node_aggregation.py](../src/consciousness_bridge/response_geometry_node_aggregation.py), tested in [test_response_geometry_node_aggregation.py](../tests/test_response_geometry_node_aggregation.py), and summarized by [p29_response_geometry_node_aggregation.svg](figures/p29_response_geometry_node_aggregation.svg).",
    "navigation P29 implementation",
)

# Equation provenance.
p28_boundary = r"""P28 is a theorem about declared intervention comparisons and target response blocks. It does not create simultaneous interventions, establish complete P11 scale equivalence, physical completeness, or experience.

---

# 23. Candidate consciousness-theory feature families"""
p29_eq = r"""P28 is a theorem about declared intervention comparisons and target response blocks. P29 supplies the complete response-geometry transport statement on a fixed intervention-delay grid.

---

# 23. P29 - response-geometry transport under node aggregation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(G_f(u,v,\tau)=\|P^{u,\tau}-P^{v,\tau}\|_{\mathrm{TV}}\) | fine P11 response-geometry entry | P11 definition applied to declared grid | P11; [P29](proposition_29_response_geometry_node_aggregation.md) |
| \(\overline P^{u,\tau}=(C_a)_\#P^{u,\tau}\) | node-aggregated response law | repository construction using P27 aggregate-state map | P27; [P29](proposition_29_response_geometry_node_aggregation.md) |
| \(G_c(u,v,\tau)\le G_f(u,v,\tau)\) | entrywise geometry contraction | proved by TV data processing | P17; [P29](proposition_29_response_geometry_node_aggregation.md) |
| \(0\le G_f-G_c\le\rho_{u,\tau}+\rho_{v,\tau}\) | law-specific reconstruction-controlled geometry loss | proved by P18 | P18; [P29](proposition_29_response_geometry_node_aggregation.md) |
| \(\rho_*=\sup_{u,\tau}\rho_{u,\tau}\) | uniform reconstruction defect on the declared experiment grid | repository definition | [P29](proposition_29_response_geometry_node_aggregation.md) |
| \(\|\mathcal G_f-\mathcal G_c\|_\infty\le2\rho_*\) | simultaneous distortion bound for the complete indexed geometry | proved | [P29](proposition_29_response_geometry_node_aggregation.md) |
| \(0\le\Delta_f-\Delta_c\le2\rho_*\) | response-diameter corollary | proved | [P29](proposition_29_response_geometry_node_aggregation.md) |

P29 fixes intervention and delay semantics. It does not merge intervention labels, resample time, establish full P11 scale equivalence, physical completeness, or experience.

---

# 24. Candidate consciousness-theory feature families"""
replace_once("docs/equation_and_citation_map.md", p28_boundary, p29_eq, "equation map P29")
replace_once("docs/equation_and_citation_map.md", "# 24. Citation discipline", "# 25. Citation discipline", "equation citation renumber")

# Release metadata.
replace_once("pyproject.toml", 'version = "0.28.0"', 'version = "0.29.0"', "pyproject version")
replace_once(
    "pyproject.toml",
    "intervention node-aggregation compatibility, recoverability",
    "intervention node-aggregation compatibility, response-geometry node aggregation, recoverability",
    "pyproject description",
)

citation = Path("CITATION.cff")
text = citation.read_text(encoding="utf-8")
if "version: 0.28.0" not in text:
    raise RuntimeError("unexpected citation version")
text = text.replace("version: 0.28.0", "version: 0.29.0", 1)
if "response-geometry node aggregation" not in text:
    text = text.replace(
        "intervention node-aggregation compatibility",
        "intervention node-aggregation compatibility, response-geometry node aggregation",
        1,
    )
citation.write_text(text, encoding="utf-8")

changelog = Path("CHANGELOG.md")
text = changelog.read_text(encoding="utf-8")
marker = "This changelog records theorem-level scientific releases. Definitions, proofs, implementations, tests, figures, and documentation remain linked from the main research page.\n\n"
if text.count(marker) != 1:
    raise RuntimeError("unexpected changelog marker")
entry = r"""## 0.29.0 - 2026-09-09

### Proposition 29 - response-geometry transport under node aggregation

- Extended the P11 physical scale program to the complete response-geometry component under the P27 changing node set.
- Kept intervention labels and delay labels fixed so every fine geometry entry has one exact coarse counterpart.
- Defined the complete intervention-delay total-variation response geometry before and after aggregation-compatible state mapping.
- Proved entrywise total-variation contraction for every intervention pair at every retained delay.
- Applied P18 to obtain the law-specific bound \(0\le G_f-G_c\le\rho_{u,\tau}+\rho_{v,\tau}\).
- Proved the uniform whole-geometry certificate \(\|\mathcal G_f-\mathcal G_c\|_\infty\le2\rho_*\).
- Derived exact geometry preservation, response-diameter control, and per-edge threshold preservation as corollaries.
- Added executable implementation, nine regression tests, a publication theorem map, main-paper integration, theorem-roadmap integration, navigation, provenance, release guards, and synchronized 0.29.0 metadata.
- Preserved the boundary that intervention merging, temporal resampling, full P11 assembly, physical completeness, and experiential interpretation remain open.

"""
changelog.write_text(text.replace(marker, marker + entry, 1), encoding="utf-8")

# Public guards.
replace_once(
    "tests/test_main_page_visual_paper.py",
    '    "p28_intervention_node_aggregation_compatibility.svg",\n    "observer_to_bridge_handoff.svg",',
    '    "p28_intervention_node_aggregation_compatibility.svg",\n    "p29_response_geometry_node_aggregation.svg",\n    "observer_to_bridge_handoff.svg",',
    "main page P29 figure",
)
replace_once("tests/test_main_page_visual_paper.py", "for index in range(1, 29):", "for index in range(1, 30):", "main page P29 range")
replace_once("tests/test_document_link_integrity.py", "for number in range(1, 29):", "for number in range(1, 30):", "navigation P29 range")
replace_once(
    "tests/test_visual_and_terminology_quality.py",
    '    "p28_intervention_node_aggregation_compatibility.svg",\n    "universal_proof_ladder.svg",',
    '    "p28_intervention_node_aggregation_compatibility.svg",\n    "p29_response_geometry_node_aggregation.svg",\n    "universal_proof_ladder.svg",',
    "visual P29 figure",
)

# Global theorem-roadmap SVG.
roadmap = Path("docs/figures/theorem_roadmap.svg")
text = roadmap.read_text(encoding="utf-8")
for old, new, label in (
    ('height="3100" viewBox="0 0 1600 3100"', 'height="3330" viewBox="0 0 1600 3330"', "dimensions"),
    ("Theorem roadmap through Proposition 28", "Theorem roadmap through Proposition 29", "title"),
    ("Theorem Roadmap - P1 through P28", "Theorem Roadmap - P1 through P29", "heading"),
    ('<rect width="1600" height="3100" fill="#ffffff"/>', '<rect width="1600" height="3330" fill="#ffffff"/>', "background"),
):
    if old not in text:
        raise RuntimeError(f"roadmap SVG missing {label}")
    text = text.replace(old, new, 1)
old_tail = '''  <rect x="95" y="3030" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="3055" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="3078" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Full response geometry, complete P11 scale equivalence, physical completeness, and experiential formalization remain open.</text>
</svg>'''
new_tail = '''  <rect x="225" y="3030" width="1150" height="190" rx="20" fill="#fff7ed" stroke="#ea580c" stroke-width="1.8"/>
  <text x="265" y="3067" class="label">RESPONSE GEOMETRY · P29</text>
  <text x="265" y="3105" class="head">Every intervention-pair distance is controlled at every delay</text>
  <text x="265" y="3139" class="body">The experiment grid is fixed while the response state is aggregated.</text>
  <text x="265" y="3174" class="eq">||Gf-Gc||∞ ≤ 2ρ*</text>
  <text x="765" y="3174" class="eq">ρ*=0 ⇒ Gf=Gc</text>
  <text x="265" y="3204" class="body">P27, P28, and P29 now cover K, A, and G separately.</text>

  <rect x="95" y="3260" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="3285" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="3308" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Simultaneous P11 assembly, intervention/time quotienting, physical completeness, and experiential formalization remain open.</text>
</svg>'''
if old_tail not in text:
    raise RuntimeError("P28 roadmap tail not found")
roadmap.write_text(text.replace(old_tail, new_tail, 1), encoding="utf-8")

for path, token, label in (
    ("README.md", "**P29**", "README P29 marker"),
    ("README.md", "p29_response_geometry_node_aggregation.svg", "README P29 figure"),
    ("docs/theorem_roadmap.md", "proposition_29_response_geometry_node_aggregation.md", "roadmap P29 link"),
    ("docs/research_navigation.md", "proposition_29_response_geometry_node_aggregation.md", "navigation P29 link"),
    ("docs/equation_and_citation_map.md", "# 23. P29 - response-geometry transport under node aggregation", "equation P29"),
    ("pyproject.toml", 'version = "0.29.0"', "pyproject P29"),
    ("CITATION.cff", "version: 0.29.0", "citation P29"),
):
    require(path, token, label)
