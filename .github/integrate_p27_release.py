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


# Fix the P26 README and roadmap transcription defect before extending the paper.
replace_once(
    "README.md",
    "\\rho(P^{u,\\tau})+\nho(P_{\\pi}^{u,\\tau}).",
    "\\rho(P^{u,\\tau})+\\rho(P_{\\pi}^{u,\\tau}).",
    "P26 README rho transcription",
)
replace_once(
    "docs/theorem_roadmap.md",
    "\\rho(P^{u,\\tau})+\nho(P_{\\pi}^{u,\\tau}).",
    "\\rho(P^{u,\\tau})+\\rho(P_{\\pi}^{u,\\tau}).",
    "P26 roadmap rho transcription",
)

# README release metadata and navigation.
replace_once("README.md", "version-0.26.0-2563eb", "version-0.27.0-2563eb", "README badge")
replace_once("README.md", "**26 proposition-level results", "**27 proposition-level results", "README result count")
replace_once("README.md", "P1 through P26 with explicit dependency branches", "P1 through P27 with explicit dependency branches", "README theorem range")
replace_once("README.md", "| proposition-level results | **26** |", "| proposition-level results | **27** |", "README proposition table count")
replace_once("README.md", "| research-software version | **0.26.0** |", "| research-software version | **0.27.0** |", "README software version")
replace_once("README.md", "# 7. Theorem roadmap - P1 through P26", "# 7. Theorem roadmap - P1 through P27", "README theorem heading")
replace_once(
    "README.md",
    "**P26** extends the same physical scale program to P11 partition irreducibility: block-compatible coarse observation cannot increase the distance from the declared partition-product null, and P18 reconstruction separately controls the actual response law and its factorized reference.",
    "**P26** extends the same physical scale program to P11 partition irreducibility: block-compatible coarse observation cannot increase the distance from the declared partition-product null, and P18 reconstruction separately controls the actual response law and its factorized reference. **P27** then allows the node set itself to change: a fine partition descends through a surjective node aggregation exactly when it is saturated by the aggregation fibers, the surviving partitions form a lattice isomorphic to the coarse partition lattice, and P18 controls any remaining irreducibility loss under an aggregation-compatible state map.",
    "README abstract P27",
)
replace_once(
    "README.md",
    "| partition-irreducibility scale theorem | [Proposition 26](docs/proposition_26_partition_irreducibility_scale_certification.md) | P11 partition irreducibility under block-compatible observation with P18 reconstruction control |",
    "| partition-irreducibility scale theorem | [Proposition 26](docs/proposition_26_partition_irreducibility_scale_certification.md) | P11 partition irreducibility under block-compatible observation with P18 reconstruction control |\n| partition-lattice node-aggregation theorem | [Proposition 27](docs/proposition_27_partition_lattice_node_aggregation.md) | exact partition descent, lattice transport, and P18-controlled irreducibility under changing node sets |",
    "README P27 nav theorem row",
)
replace_once(
    "README.md",
    "| implementation of P26 | [partition_irreducibility_scale_certification.py](src/consciousness_bridge/partition_irreducibility_scale_certification.py) | partition-product commutation, irreducibility contraction, and reconstruction-controlled scale certificate |",
    "| implementation of P26 | [partition_irreducibility_scale_certification.py](src/consciousness_bridge/partition_irreducibility_scale_certification.py) | partition-product commutation, irreducibility contraction, and reconstruction-controlled scale certificate |\n| implementation of P27 | [partition_lattice_node_aggregation.py](src/consciousness_bridge/partition_lattice_node_aggregation.py) | saturated partition descent, lattice isomorphism, aggregate-state maps, and node-aggregation irreducibility certificate |",
    "README P27 implementation row",
)
replace_once(
    "README.md",
    "| **11.2 P26 partition-irreducibility scale** | When does P11 partition irreducibility survive block-compatible coarse observation? |",
    "| **11.2 P26 partition-irreducibility scale** | When does P11 partition irreducibility survive block-compatible coarse observation? |\n| **11.3 P27 partition lattice under node aggregation** | Which fine partitions remain well-defined after several nodes become one coarse node? |",
    "README P27 paper map row",
)
replace_once(
    "README.md",
    "| **P26** | P11 partition irreducibility contracts under block-compatible observation, with P18 reconstruction controlling the loss from the partition-product null | proved physical scale theorem | [P26](docs/proposition_26_partition_irreducibility_scale_certification.md) |",
    "| **P26** | P11 partition irreducibility contracts under block-compatible observation, with P18 reconstruction controlling the loss from the partition-product null | proved physical scale theorem | [P26](docs/proposition_26_partition_irreducibility_scale_certification.md) |\n| **P27** | aggregation-saturated fine partitions are exactly those that descend through a surjective node map; the surviving partition lattice is isomorphic to the coarse partition lattice, with P18 controlling probabilistic irreducibility loss | proved physical scale theorem | [P27](docs/proposition_27_partition_lattice_node_aggregation.md) |",
    "README P27 theorem row",
)

p26_end = r"""[Read Proposition 26](docs/proposition_26_partition_irreducibility_scale_certification.md). The [P26 theorem map](docs/figures/p26_partition_irreducibility_scale_certification.svg), [implementation](src/consciousness_bridge/partition_irreducibility_scale_certification.py), and [tests](tests/test_partition_irreducibility_scale_certification.py) expose the complete proof-to-code path.

---

# 14. Observer-to-bridge handoff"""
p27_section = r"""[Read Proposition 26](docs/proposition_26_partition_irreducibility_scale_certification.md). The [P26 theorem map](docs/figures/p26_partition_irreducibility_scale_certification.svg), [implementation](src/consciousness_bridge/partition_irreducibility_scale_certification.py), and [tests](tests/test_partition_irreducibility_scale_certification.py) expose the complete proof-to-code path.

## 13.5 P27 - partition-lattice transport under node aggregation

![P27 partition-lattice transport under node aggregation](docs/figures/p27_partition_lattice_node_aggregation.svg)

P27 removes an assumption that P26 deliberately retained. The node set itself may now change. Let

\[
\boxed{
a:V_f\twoheadrightarrow V_c
}
\]

be a surjective node-aggregation map and let

\[
F_c=a^{-1}(c)
\]

be the fine-node fiber represented by coarse node \(c\).

A fine partition \(\pi_f\) has an exact coarse meaning if and only if no aggregation fiber is split across two fine partition blocks:

\[
\boxed{
\pi_f\text{ descends through }a
\iff
\forall c\in V_c\;\exists B\in\pi_f:\;F_c\subseteq B.
}
\]

Equivalently,

\[
\boxed{
a(i)=a(j)\Longrightarrow i\sim_{\pi_f}j.}
\]

This aggregation-saturation criterion separates a structural incompatibility from ordinary measurement error. If a fiber crosses a proposed partition boundary, the corresponding coarse partition simply does not exist.

For every coarse partition \(\pi_c\), define the lift

\[
\boxed{
L_a(\pi_c)=\{a^{-1}(C):C\in\pi_c\}.
}
\]

For every saturated fine partition, define its descent by the images of its blocks. The two operations are inverse and preserve the refinement order, meet, and join. Therefore

\[
\boxed{
\operatorname{Part}(V_c)
\simeq_{\mathrm{lattice}}
\operatorname{Part}_{\mathrm{sat}}(V_f;a).
}
\]

This identifies exactly which portion of the fine partition lattice survives node aggregation.

The probabilistic P11 quantity can also be transported when each coarse state depends only on the fine states inside its aggregation fiber. If \(C_a\) is such an aggregation-compatible state map and \(\pi_f=L_a(\pi_c)\), then

\[
\boxed{
(C_a)_\#P_{\pi_f}
=
\bigl((C_a)_\#P\bigr)_{\pi_c}.
}
\]

Hence total-variation contraction gives

\[
\boxed{
\kappa_c(\pi_c)
\le
\kappa_f(L_a\pi_c).
}
\]

With a P18 reconstruction operator \(D=R_\#(C_a)_\#\),

\[
\boxed{
0\le
\kappa_f(\pi_f)-\kappa_c(\pi_c)
\le
\rho(P)+\rho(P_{\pi_f}).
}
\]

Exact reconstruction of the response law and its partition-product null gives exact irreducibility preservation even though the declared node count has changed.

P27 therefore distinguishes two failure modes that should never be conflated:

\[
\boxed{
\text{no partition descent}
\neq
\text{valid partition with attenuated irreducibility}.
}
\]

The first is a semantic obstruction created by the node quotient. The second is information loss created by the aggregate-state map.

P27 still does not solve intervention-channel aggregation, source-node perturbation semantics, directed influence under source aggregation, complete P11 scale equivalence, genuine physical fusion, physical completeness, or experience. Those remain separate theorem burdens.

[Read Proposition 27](docs/proposition_27_partition_lattice_node_aggregation.md). The [P27 theorem map](docs/figures/p27_partition_lattice_node_aggregation.svg), [implementation](src/consciousness_bridge/partition_lattice_node_aggregation.py), and [tests](tests/test_partition_lattice_node_aggregation.py) expose the complete proof-to-code path.

---

# 14. Observer-to-bridge handoff"""
replace_once("README.md", p26_end, p27_section, "README P27 section")
replace_once(
    "README.md",
    "P25 extends that control to the P11 directed-influence component under fixed intervention semantics and target observation coarse-graining. P26 extends it to P11 partition irreducibility when the observation map is compatible with the declared partition.",
    "P25 extends that control to the P11 directed-influence component under fixed intervention semantics and target observation coarse-graining. P26 extends it to P11 partition irreducibility when the observation map is compatible with the declared partition. P27 identifies exactly which fine partitions remain meaningful when the node set itself is aggregated and quantifies their remaining irreducibility under aggregation-compatible state maps.",
    "README falsification scale P27",
)
replace_once("README.md", "the P1-P26 proposition chain", "the P1-P27 proposition chain", "README reproducibility range")

# Theorem roadmap.
replace_once("docs/theorem_roadmap.md", "![P1-P26 theorem roadmap]", "![P1-P27 theorem roadmap]", "roadmap alt")
replace_once(
    "docs/theorem_roadmap.md",
    "| [P26](proposition_26_partition_irreducibility_scale_certification.md) | P11 partition productization plus P17 contraction and P18 reconstruction | partition-irreducibility preservation and margin certification under block-compatible observation | proved physical scale theorem |",
    "| [P26](proposition_26_partition_irreducibility_scale_certification.md) | P11 partition productization plus P17 contraction and P18 reconstruction | partition-irreducibility preservation and margin certification under block-compatible observation | proved physical scale theorem |\n| [P27](proposition_27_partition_lattice_node_aggregation.md) | surjective node quotient plus partition saturation, lattice transport, P17 contraction, and P18 reconstruction | exact criterion for surviving partition semantics under node aggregation and quantitative irreducibility control | proved physical scale theorem |",
    "roadmap P27 index row",
)
p26_roadmap_end = r"""Direct proof: [Proposition 26](proposition_26_partition_irreducibility_scale_certification.md). Implementation: [partition_irreducibility_scale_certification.py](../src/consciousness_bridge/partition_irreducibility_scale_certification.py). Tests: [test_partition_irreducibility_scale_certification.py](../tests/test_partition_irreducibility_scale_certification.py).

---

# 8. Fundamental physical sufficiency: P19"""
p27_roadmap = r"""Direct proof: [Proposition 26](proposition_26_partition_irreducibility_scale_certification.md). Implementation: [partition_irreducibility_scale_certification.py](../src/consciousness_bridge/partition_irreducibility_scale_certification.py). Tests: [test_partition_irreducibility_scale_certification.py](../tests/test_partition_irreducibility_scale_certification.py).

## P27 - partition-lattice transport under node aggregation

Let \(a:V_f\twoheadrightarrow V_c\) be a surjective node map. A fine partition \(\pi_f\) descends exactly when every aggregation fiber lies wholly within one fine block:

\[
\boxed{
\pi_f\text{ descends}
\iff
\forall c\in V_c\;\exists B\in\pi_f:\;a^{-1}(c)\subseteq B.
}
\]

Coarse partitions and aggregation-saturated fine partitions are in bijection through lift and descent, and the correspondence preserves refinement, meet, and join:

\[
\boxed{
\operatorname{Part}(V_c)
\simeq_{\mathrm{lattice}}
\operatorname{Part}_{\mathrm{sat}}(V_f;a).
}
\]

For an aggregation-compatible state map \(C_a\), partition productization commutes with pushforward for every descendable partition. Therefore

\[
\boxed{
\kappa_c(\pi_c)\le\kappa_f(L_a\pi_c)
}
\]

and P18 gives

\[
\boxed{
0\le\kappa_f-\kappa_c\le\rho(P)+\rho(P_{\pi_f}).
}
\]

P27 separates structural non-descendability from ordinary information loss. It does not yet transport intervention channels or directed influence through source-node aggregation.

Direct proof: [Proposition 27](proposition_27_partition_lattice_node_aggregation.md). Implementation: [partition_lattice_node_aggregation.py](../src/consciousness_bridge/partition_lattice_node_aggregation.py). Tests: [test_partition_lattice_node_aggregation.py](../tests/test_partition_lattice_node_aggregation.py).

---

# 8. Fundamental physical sufficiency: P19"""
replace_once("docs/theorem_roadmap.md", p26_roadmap_end, p27_roadmap, "roadmap P27 section")

# Research navigation.
replace_once(
    "docs/research_navigation.md",
    "from P1 through P26, including the physical scale branches from P11-P18 to P25-P26",
    "from P1 through P27, including the physical scale branches from P11-P18 to P25-P27",
    "navigation range",
)
replace_once(
    "docs/research_navigation.md",
    "12. [Proposition 26](proposition_26_partition_irreducibility_scale_certification.md) for P11 partition-irreducibility preservation under block-compatible observation with P18 reconstruction control.\n13. [Fundamental Theory to Consciousness program]",
    "12. [Proposition 26](proposition_26_partition_irreducibility_scale_certification.md) for P11 partition-irreducibility preservation under block-compatible observation with P18 reconstruction control.\n13. [Proposition 27](proposition_27_partition_lattice_node_aggregation.md) for exact partition descent and lattice transport under node aggregation.\n14. [Fundamental Theory to Consciousness program]",
    "navigation reading P27",
)
# Repair subsequent duplicate numbering while here.
replace_once("docs/research_navigation.md", "13. [Stochastic fundamental bridge]", "15. [Stochastic fundamental bridge]", "navigation stochastic number")
replace_once("docs/research_navigation.md", "14. [Falsification program]", "16. [Falsification program]", "navigation falsification number")
replace_once("docs/research_navigation.md", "15. [Citation and Reference Policy]", "17. [Citation and Reference Policy]", "navigation citation number")
replace_once(
    "docs/research_navigation.md",
    "| P26 | [Partition-irreducibility scale certification](proposition_26_partition_irreducibility_scale_certification.md) | P11 partition-product distortion and threshold preservation under block-compatible scale observation |",
    "| P26 | [Partition-irreducibility scale certification](proposition_26_partition_irreducibility_scale_certification.md) | P11 partition-product distortion and threshold preservation under block-compatible scale observation |\n| P27 | [Partition-lattice node aggregation](proposition_27_partition_lattice_node_aggregation.md) | exact saturated-partition descent, lattice transport, and irreducibility control across changing node sets |",
    "navigation P27 index row",
)
replace_once(
    "docs/research_navigation.md",
    "| [P26 partition-irreducibility scale certification](proposition_26_partition_irreducibility_scale_certification.md) | P11 partition structure under block-compatible coarse observation with P18 reconstruction control |",
    "| [P26 partition-irreducibility scale certification](proposition_26_partition_irreducibility_scale_certification.md) | P11 partition structure under block-compatible coarse observation with P18 reconstruction control |\n| [P27 partition-lattice node aggregation](proposition_27_partition_lattice_node_aggregation.md) | partition semantics and irreducibility under explicit many-to-one node aggregation |",
    "navigation P27 interface row",
)
replace_once(
    "docs/research_navigation.md",
    "and summarized by [p26_partition_irreducibility_scale_certification.svg](figures/p26_partition_irreducibility_scale_certification.svg).",
    "and summarized by [p26_partition_irreducibility_scale_certification.svg](figures/p26_partition_irreducibility_scale_certification.svg). The P27 node-aggregation layer is implemented in [partition_lattice_node_aggregation.py](../src/consciousness_bridge/partition_lattice_node_aggregation.py), tested in [test_partition_lattice_node_aggregation.py](../tests/test_partition_lattice_node_aggregation.py), and summarized by [p27_partition_lattice_node_aggregation.svg](figures/p27_partition_lattice_node_aggregation.svg).",
    "navigation P27 implementation paragraph",
)

# Equation and citation map.
p26_boundary = r"""P26 is an observation-scale theorem for one declared partition. It does not yet define the induced map between fine and coarse partition lattices under physical node aggregation, and it does not establish physical completeness or experience.

---

# 21. Candidate consciousness-theory feature families"""
p27_eq = r"""P26 is an observation-scale theorem for one declared partition. P27 supplies the missing node-aggregation transport criterion.

---

# 21. P27 - partition-lattice transport under node aggregation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(a:V_f\twoheadrightarrow V_c\), \(F_c=a^{-1}(c)\) | declared surjective node aggregation and its fibers | repository definition | [P27](proposition_27_partition_lattice_node_aggregation.md) |
| \(F_c\subseteq B\) for some \(B\in\pi_f\) for every \(c\) | aggregation-saturation criterion | necessary and sufficient for exact partition descent | [P27](proposition_27_partition_lattice_node_aggregation.md) |
| \(L_a(\pi_c)=\{a^{-1}(C):C\in\pi_c\}\) | lifts coarse partitions to saturated fine partitions | repository construction | [P27](proposition_27_partition_lattice_node_aggregation.md) |
| \(\operatorname{Part}(V_c)\simeq_{\mathrm{lattice}}\operatorname{Part}_{\mathrm{sat}}(V_f;a)\) | exact surviving partition-lattice correspondence | proved | [P27](proposition_27_partition_lattice_node_aggregation.md) |
| \((C_a)_\#P_{\pi_f}=((C_a)_\#P)_{\pi_c}\) | productization commutes with aggregation-compatible state mapping for descendable partitions | proved | [P27](proposition_27_partition_lattice_node_aggregation.md) |
| \(\kappa_c(\pi_c)\le\kappa_f(L_a\pi_c)\) | node aggregation cannot increase corresponding partition irreducibility | proved by TV contraction | P17; [P27](proposition_27_partition_lattice_node_aggregation.md) |
| \(0\le\kappa_f-\kappa_c\le\rho(P)+\rho(P_{\pi_f})\) | reconstruction-controlled irreducibility loss after node aggregation | proved by P18 applied to the response/product pair | P18; [P27](proposition_27_partition_lattice_node_aggregation.md) |

P27 distinguishes failure of partition semantics from loss of partition signal. It does not yet transport intervention channels or directed influence through source-node aggregation and does not establish physical completeness or experience.

---

# 22. Candidate consciousness-theory feature families"""
replace_once("docs/equation_and_citation_map.md", p26_boundary, p27_eq, "equation map P27 section")
replace_once("docs/equation_and_citation_map.md", "# 22. Citation discipline", "# 23. Citation discipline", "equation map citation renumber")

# Release metadata.
replace_once("pyproject.toml", 'version = "0.26.0"', 'version = "0.27.0"', "pyproject version")
replace_once(
    "pyproject.toml",
    "partition-irreducibility scale certification, recoverability",
    "partition-irreducibility scale certification, partition-lattice node aggregation, recoverability",
    "pyproject description",
)

citation = Path("CITATION.cff")
text = citation.read_text(encoding="utf-8")
if "version: 0.26.0" not in text:
    raise RuntimeError("CITATION.cff is not at expected 0.26.0 version")
text = text.replace("version: 0.26.0", "version: 0.27.0", 1)
if "partition-irreducibility scale certification" in text and "partition-lattice node aggregation" not in text:
    text = text.replace(
        "partition-irreducibility scale certification",
        "partition-irreducibility scale certification, partition-lattice node aggregation",
        1,
    )
citation.write_text(text, encoding="utf-8")

changelog = Path("CHANGELOG.md")
text = changelog.read_text(encoding="utf-8")
marker = "This changelog records theorem-level scientific releases. Definitions, proofs, implementations, tests, figures, and documentation remain linked from the main research page.\n\n"
if text.count(marker) != 1:
    raise RuntimeError("unexpected changelog introduction marker")
entry = r"""## 0.27.0 - 2026-09-09

### Proposition 27 - partition-lattice transport under node aggregation

- Introduced an explicit surjective node-aggregation map \(a:V_f\twoheadrightarrow V_c\) and its fine aggregation fibers.
- Proved that a fine partition has an exact coarse descent if and only if every aggregation fiber lies wholly inside one fine partition block.
- Proved that coarse partitions are in one-to-one correspondence with aggregation-saturated fine partitions through inverse lift/descent maps.
- Proved preservation of refinement order, meet, and join, yielding a lattice isomorphism between \(\operatorname{Part}(V_c)\) and the saturated sublattice of \(\operatorname{Part}(V_f)\).
- Defined aggregation-compatible state maps that distinguish node-count reduction from within-fiber state compression.
- Proved partition-product commutation for descendable partitions under aggregation-compatible state maps.
- Proved irreducibility contraction across node aggregation and inherited the P18 reconstruction bound \(0\le\kappa_f-\kappa_c\le\rho(P)+\rho(P_{\pi_f})\).
- Added exact-preservation and complete-loss examples, separating structural non-descendability from observational attenuation.
- Added executable mathematics, nine dedicated tests, a publication theorem map, main-paper integration, navigation, provenance, release guards, and synchronized 0.27.0 metadata.
- Corrected the P26 README and theorem-roadmap transcription of the second reconstruction term from a malformed `ho(...)` token to \(\rho(...)\).
- Preserved the boundary that intervention aggregation, directed influence under source aggregation, full P11 scale equivalence, physical completeness, genuine physical fusion, and experience remain open.

"""
changelog.write_text(text.replace(marker, marker + entry, 1), encoding="utf-8")

# Tests and publication guards.
replace_once(
    "tests/test_main_page_visual_paper.py",
    '    "p26_partition_irreducibility_scale_certification.svg",\n    "observer_to_bridge_handoff.svg",',
    '    "p26_partition_irreducibility_scale_certification.svg",\n    "p27_partition_lattice_node_aggregation.svg",\n    "observer_to_bridge_handoff.svg",',
    "main-page P27 figure guard",
)
replace_once("tests/test_main_page_visual_paper.py", "for index in range(1, 27):", "for index in range(1, 28):", "main-page P27 proposition guard")
replace_once("tests/test_document_link_integrity.py", "for number in range(1, 27):", "for number in range(1, 28):", "navigation P27 guard")
replace_once(
    "tests/test_visual_and_terminology_quality.py",
    '    "p26_partition_irreducibility_scale_certification.svg",\n    "universal_proof_ladder.svg",',
    '    "p26_partition_irreducibility_scale_certification.svg",\n    "p27_partition_lattice_node_aggregation.svg",\n    "universal_proof_ladder.svg",',
    "visual P27 guard",
)

# Global theorem roadmap SVG: extend to P27.
roadmap = Path("docs/figures/theorem_roadmap.svg")
text = roadmap.read_text(encoding="utf-8")
text = text.replace('height="2640" viewBox="0 0 1600 2640"', 'height="2870" viewBox="0 0 1600 2870"', 1)
text = text.replace("Theorem roadmap through Proposition 26", "Theorem roadmap through Proposition 27", 1)
text = text.replace("Theorem Roadmap - P1 through P26", "Theorem Roadmap - P1 through P27", 1)
text = text.replace('<rect width="1600" height="2640" fill="#ffffff"/>', '<rect width="1600" height="2870" fill="#ffffff"/>', 1)
old_tail = '''  <rect x="95" y="2550" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="2575" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="2598" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Block aggregation, partition-lattice transport, physical completeness, and experiential formalization remain open.</text>
</svg>'''
new_tail = '''  <rect x="225" y="2550" width="1150" height="190" rx="20" fill="#eef2ff" stroke="#4f46e5" stroke-width="1.8"/>
  <text x="265" y="2587" class="label">NODE-AGGREGATION BRANCH · P27</text>
  <text x="265" y="2625" class="head">Exact partition descent through a surjective node quotient</text>
  <text x="265" y="2659" class="body">Only aggregation-saturated fine partitions survive as coarse partitions.</text>
  <text x="265" y="2694" class="eq">Part(Vc) ≅ Partsat(Vf;a)</text>
  <text x="765" y="2694" class="eq">0 ≤ κf − κc ≤ ρ(P)+ρ(Pπf)</text>
  <text x="265" y="2724" class="body">Intervention and source aggregation remain separate theorem burdens.</text>

  <rect x="95" y="2790" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="2815" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="2838" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Intervention aggregation, full P11 scale equivalence, physical completeness, and experiential formalization remain open.</text>
</svg>'''
if old_tail not in text:
    raise RuntimeError("theorem roadmap SVG tail marker not found")
roadmap.write_text(text.replace(old_tail, new_tail, 1), encoding="utf-8")

# Final release assertions.
for path, token, label in (
    ("README.md", "**P27**", "README P27 marker"),
    ("README.md", "p27_partition_lattice_node_aggregation.svg", "README P27 figure"),
    ("README.md", "\\rho(P^{u,\\tau})+\\rho(P_{\\pi}^{u,\\tau})", "corrected P26 README rho"),
    ("docs/theorem_roadmap.md", "proposition_27_partition_lattice_node_aggregation.md", "roadmap P27 link"),
    ("docs/research_navigation.md", "proposition_27_partition_lattice_node_aggregation.md", "navigation P27 link"),
    ("docs/equation_and_citation_map.md", "# 21. P27 - partition-lattice transport under node aggregation", "equation map P27 section"),
    ("pyproject.toml", 'version = "0.27.0"', "pyproject version"),
    ("CITATION.cff", "version: 0.27.0", "citation version"),
):
    require(path, token, label)
