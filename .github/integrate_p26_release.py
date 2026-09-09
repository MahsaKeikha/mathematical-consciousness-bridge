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
    "version-0.25.0-2563eb",
    "version-0.26.0-2563eb",
    "README version badge",
)
replace_once(
    "README.md",
    "**P25** returns to the P11 physical candidate and proves a directed-influence scale theorem: deterministic target coarse observation cannot increase matched-intervention influence, and P18 reconstruction defect bounds the loss by twice the uniform reconstruction error.",
    "**P25** returns to the P11 physical candidate and proves a directed-influence scale theorem: deterministic target coarse observation cannot increase matched-intervention influence, and P18 reconstruction defect bounds the loss by twice the uniform reconstruction error. **P26** extends the same physical scale program to P11 partition irreducibility: block-compatible coarse observation cannot increase the distance from the declared partition-product null, and P18 reconstruction separately controls the actual response law and its factorized reference.",
    "README abstract P26 summary",
)
replace_once(
    "README.md",
    "**25 proposition-level results, 58 equation-driven quantitative figures",
    "**26 proposition-level results, 58 equation-driven quantitative figures",
    "README proposition record count",
)
replace_once(
    "README.md",
    "P1 through P25 with explicit dependency branches",
    "P1 through P26 with explicit dependency branches",
    "README theorem navigation range",
)
replace_once(
    "README.md",
    "| directed-influence scale theorem | [Proposition 25](docs/proposition_25_directed_influence_scale_certification.md) | P11 directed influence under P18 reconstruction-controlled target coarse observation |",
    "| directed-influence scale theorem | [Proposition 25](docs/proposition_25_directed_influence_scale_certification.md) | P11 directed influence under P18 reconstruction-controlled target coarse observation |\n| partition-irreducibility scale theorem | [Proposition 26](docs/proposition_26_partition_irreducibility_scale_certification.md) | P11 partition irreducibility under block-compatible observation with P18 reconstruction control |",
    "README P26 theorem navigation",
)
replace_once(
    "README.md",
    "| implementation of P25 | [directed_influence_scale_certification.py](src/consciousness_bridge/directed_influence_scale_certification.py) | directed-influence distortion and threshold-edge scale certificate |",
    "| implementation of P25 | [directed_influence_scale_certification.py](src/consciousness_bridge/directed_influence_scale_certification.py) | directed-influence distortion and threshold-edge scale certificate |\n| implementation of P26 | [partition_irreducibility_scale_certification.py](src/consciousness_bridge/partition_irreducibility_scale_certification.py) | partition-product commutation, irreducibility contraction, and reconstruction-controlled scale certificate |",
    "README P26 implementation navigation",
)
replace_once(
    "README.md",
    "| **11.1 P25 directed-influence scale** | When does P11 directed influence survive target coarse observation? |",
    "| **11.1 P25 directed-influence scale** | When does P11 directed influence survive target coarse observation? |\n| **11.2 P26 partition-irreducibility scale** | When does P11 partition irreducibility survive block-compatible coarse observation? |",
    "README P26 paper-map row",
)
replace_once(
    "README.md",
    "| proposition-level results | **25** |",
    "| proposition-level results | **26** |",
    "README proposition count",
)
replace_once(
    "README.md",
    "| research-software version | **0.25.0** |",
    "| research-software version | **0.26.0** |",
    "README software version",
)
replace_once(
    "README.md",
    "# 7. Theorem roadmap - P1 through P25",
    "# 7. Theorem roadmap - P1 through P26",
    "README theorem heading",
)
replace_once(
    "README.md",
    "| **P25** | P11 directed influence contracts under target coarse observation, with P18 reconstruction controlling the loss | proved physical scale theorem | [P25](docs/proposition_25_directed_influence_scale_certification.md) |",
    "| **P25** | P11 directed influence contracts under target coarse observation, with P18 reconstruction controlling the loss | proved physical scale theorem | [P25](docs/proposition_25_directed_influence_scale_certification.md) |\n| **P26** | P11 partition irreducibility contracts under block-compatible observation, with P18 reconstruction controlling the loss from the partition-product null | proved physical scale theorem | [P26](docs/proposition_26_partition_irreducibility_scale_certification.md) |",
    "README P26 theorem table row",
)

p25_end = r"""[Read Proposition 25](docs/proposition_25_directed_influence_scale_certification.md). The [P25 theorem map](docs/figures/p25_directed_influence_scale_certification.svg), [implementation](src/consciousness_bridge/directed_influence_scale_certification.py), and [tests](tests/test_directed_influence_scale_certification.py) expose the complete proof-to-code path.

---

# 14. Observer-to-bridge handoff"""
p26_readme = r"""[Read Proposition 25](docs/proposition_25_directed_influence_scale_certification.md). The [P25 theorem map](docs/figures/p25_directed_influence_scale_certification.svg), [implementation](src/consciousness_bridge/directed_influence_scale_certification.py), and [tests](tests/test_directed_influence_scale_certification.py) expose the complete proof-to-code path.

## 13.4 P26 - partition-irreducibility scale certification

![P26 partition-irreducibility scale certification](docs/figures/p26_partition_irreducibility_scale_certification.svg)

P26 extends the physical scale audit from response geometry and directed influence to the P11 partition component \(\mathcal K\). Fix an intervention \(u\), delay \(\tau\), and a declared partition \(\pi\). The fine partition-product reference is

\[
\boxed{
P_{\pi}^{u,\tau}
=
\bigotimes_{B\in\pi}P_B^{u,\tau},
}
\]

and the fine irreducibility is

\[
\boxed{
\kappa_f^{u,\tau}(\pi)
=
\|P^{u,\tau}-P_{\pi}^{u,\tau}\|_{\mathrm{TV}}.
}
\]

The scale comparison is scientifically meaningful only when the deterministic observation map is block compatible with the declared partition. For a coordinatewise or blockwise map \(C\), partition productization commutes with observation:

\[
\boxed{
C_\#P_{\pi}^{u,\tau}
=
\bigotimes_{B\in\pi}(C_B)_\#P_B^{u,\tau}.
}
\]

Therefore the coarse irreducibility

\[
\kappa_c^{u,\tau}(\pi)
=
\|C_\#P^{u,\tau}-C_\#P_{\pi}^{u,\tau}\|_{\mathrm{TV}}
\]

obeys total-variation contraction:

\[
\boxed{
0\le
\kappa_f^{u,\tau}(\pi)-\kappa_c^{u,\tau}(\pi).
}
\]

Let \(D=R_\#C_\#\) be the P18 reconstruction operator and define \(\rho(Q)=\|Q-DQ\|_{\mathrm{TV}}\). Applying P18 to the pair \((P^{u,\tau},P_{\pi}^{u,\tau})\) gives the sharper P26 bound

\[
\boxed{
0\le
\kappa_f^{u,\tau}(\pi)-\kappa_c^{u,\tau}(\pi)
\le
\rho(P^{u,\tau})+
\rho(P_{\pi}^{u,\tau}).
}
\]

The two reconstruction terms are intentionally kept separate because they correspond to different physical objects: the actual joint response and the factorized partition null.

If both reconstruct exactly, then

\[
\boxed{
\kappa_c^{u,\tau}(\pi)=\kappa_f^{u,\tau}(\pi).
}
\]

For a threshold \(\theta\), define

\[
\varepsilon_{\pi}^{u,\tau}
=
\rho(P^{u,\tau})+ho(P_{\pi}^{u,\tau}).
\]

Then

\[
\boxed{
\kappa_f^{u,\tau}(\pi)>
\theta+arepsilon_{\pi}^{u,\tau}
\Longrightarrow
\kappa_c^{u,\tau}(\pi)>	heta.
}
\]

Conversely,

\[
\kappa_c^{u,\tau}(\pi)>	heta
\Longrightarrow
\kappa_f^{u,\tau}(\pi)>	heta.
\]

A binary counterexample shows why no stronger unconditional invariance statement is possible: a correlated fine law can have \(\kappa_f=0.4\), while collapsing one coordinate makes \(\kappa_c=0\). Fine dependence can therefore disappear completely under information-destroying observation.

P26 remains an observation-scale theorem. It does not yet solve aggregation of multiple fine blocks into a new coarse node, transformation of the full partition lattice, changing intervention semantics, genuine physical fusion, complete P11 scale equivalence, physical completeness, or experience.

[Read Proposition 26](docs/proposition_26_partition_irreducibility_scale_certification.md). The [P26 theorem map](docs/figures/p26_partition_irreducibility_scale_certification.svg), [implementation](src/consciousness_bridge/partition_irreducibility_scale_certification.py), and [tests](tests/test_partition_irreducibility_scale_certification.py) expose the complete proof-to-code path.

---

# 14. Observer-to-bridge handoff"""
replace_once("README.md", p25_end, p26_readme, "README P26 scale section")

replace_once(
    "README.md",
    "P17 shows that coarse-graining can erase distinctions. P18 quantifies when reconstruction is good enough to retain the declared response geometry. P25 extends that control to the P11 directed-influence component under fixed intervention semantics and target observation coarse-graining.",
    "P17 shows that coarse-graining can erase distinctions. P18 quantifies when reconstruction is good enough to retain the declared response geometry. P25 extends that control to the P11 directed-influence component under fixed intervention semantics and target observation coarse-graining. P26 extends it to P11 partition irreducibility when the observation map is compatible with the declared partition.",
    "README P26 falsification scale update",
)
replace_once(
    "README.md",
    "the P1-P20 proposition chain",
    "the P1-P26 proposition chain",
    "README reproducibility theorem-range text",
)

# Theorem roadmap -----------------------------------------------------------
replace_once(
    "docs/theorem_roadmap.md",
    "![P1-P25 theorem roadmap](figures/theorem_roadmap.svg)",
    "![P1-P26 theorem roadmap](figures/theorem_roadmap.svg)",
    "roadmap image alt",
)
replace_once(
    "docs/theorem_roadmap.md",
    "| [P25](proposition_25_directed_influence_scale_certification.md) | P11 influence plus P18 reconstruction distortion | directed-influence preservation and edge-margin certification across target observation scale | proved physical scale theorem |",
    "| [P25](proposition_25_directed_influence_scale_certification.md) | P11 influence plus P18 reconstruction distortion | directed-influence preservation and edge-margin certification across target observation scale | proved physical scale theorem |\n| [P26](proposition_26_partition_irreducibility_scale_certification.md) | P11 partition productization plus P17 contraction and P18 reconstruction | partition-irreducibility preservation and margin certification under block-compatible observation | proved physical scale theorem |",
    "roadmap P26 proposition row",
)
p25_roadmap_end = r"""Direct proof: [Proposition 25](proposition_25_directed_influence_scale_certification.md). Implementation: [directed_influence_scale_certification.py](../src/consciousness_bridge/directed_influence_scale_certification.py). Tests: [test_directed_influence_scale_certification.py](../tests/test_directed_influence_scale_certification.py).

---

# 8. Fundamental physical sufficiency: P19"""
p26_roadmap = r"""Direct proof: [Proposition 25](proposition_25_directed_influence_scale_certification.md). Implementation: [directed_influence_scale_certification.py](../src/consciousness_bridge/directed_influence_scale_certification.py). Tests: [test_directed_influence_scale_certification.py](../tests/test_directed_influence_scale_certification.py).

## P26 - partition-irreducibility scale certification from P11 + P17 + P18

P26 applies the scale theorem to the P11 partition component. For a declared partition \(\pi\),

\[
\kappa_f^{u,\tau}(\pi)
=
\|P^{u,\tau}-P_{\pi}^{u,\tau}\|_{\mathrm{TV}},
\qquad
P_{\pi}^{u,\tau}
=
\bigotimes_{B\in\pi}P_B^{u,\tau}.
\]

Under a block-compatible deterministic observation map \(C\), productization commutes with pushforward and therefore

\[
\boxed{
\kappa_c^{u,\tau}(\pi)
\le
\kappa_f^{u,\tau}(\pi).
}
\]

If \(D=R_\#C_\#\) is the P18 reconstruction operator, then

\[
\boxed{
0\le
\kappa_f^{u,\tau}(\pi)-\kappa_c^{u,\tau}(\pi)
\le
\rho(P^{u,\tau})+ho(P_{\pi}^{u,\tau}).
}
\]

Exact reconstruction of both laws gives exact preservation. A fine margin larger than the reconstruction budget guarantees survival of a declared coarse threshold.

The theorem does not yet transport the entire partition lattice through physical node aggregation. It certifies one declared partition under observation-compatible scale change.

Direct proof: [Proposition 26](proposition_26_partition_irreducibility_scale_certification.md). Implementation: [partition_irreducibility_scale_certification.py](../src/consciousness_bridge/partition_irreducibility_scale_certification.py). Tests: [test_partition_irreducibility_scale_certification.py](../tests/test_partition_irreducibility_scale_certification.py).

---

# 8. Fundamental physical sufficiency: P19"""
replace_once(
    "docs/theorem_roadmap.md",
    p25_roadmap_end,
    p26_roadmap,
    "roadmap P26 branch section",
)
replace_once(
    "docs/theorem_roadmap.md",
    "1. extend P25 from target observation coarse-graining to genuine block aggregation with source/intervention compatibility;\n2. characterize partition-lattice compatibility required to control \\(\\mathcal K\\) across scale;",
    "1. extend P25-P26 from observation-compatible scale change to genuine block aggregation with source/intervention compatibility;\n2. characterize the induced map between fine and coarse partition lattices and determine when the full \\(\\mathcal A,\\mathcal K\\) structure survives node aggregation;",
    "roadmap post-P26 frontier",
)

# Research navigation -------------------------------------------------------
replace_once(
    "docs/research_navigation.md",
    "3. [Theorem roadmap](theorem_roadmap.md) for the dependency structure from P1 through P25, including the P11+P18 branch to P25.",
    "3. [Theorem roadmap](theorem_roadmap.md) for the dependency structure from P1 through P26, including the physical scale branches from P11-P18 to P25-P26.",
    "navigation theorem range",
)
replace_once(
    "docs/research_navigation.md",
    "11. [Proposition 25](proposition_25_directed_influence_scale_certification.md) for P11 directed-influence preservation under P18 reconstruction-controlled target coarse observation.\n12. [Fundamental Theory to Consciousness program]",
    "11. [Proposition 25](proposition_25_directed_influence_scale_certification.md) for P11 directed-influence preservation under P18 reconstruction-controlled target coarse observation.\n12. [Proposition 26](proposition_26_partition_irreducibility_scale_certification.md) for P11 partition-irreducibility preservation under block-compatible observation with P18 reconstruction control.\n13. [Fundamental Theory to Consciousness program]",
    "navigation recommended P26",
)
replace_once(
    "docs/research_navigation.md",
    "| P25 | [Directed-influence scale certification](proposition_25_directed_influence_scale_certification.md) | P11 directed-influence distortion and edge preservation under P18 reconstruction control |",
    "| P25 | [Directed-influence scale certification](proposition_25_directed_influence_scale_certification.md) | P11 directed-influence distortion and edge preservation under P18 reconstruction control |\n| P26 | [Partition-irreducibility scale certification](proposition_26_partition_irreducibility_scale_certification.md) | P11 partition-product distortion and threshold preservation under block-compatible scale observation |",
    "navigation P26 proposition row",
)
replace_once(
    "docs/research_navigation.md",
    "| [P25 directed-influence scale certification](proposition_25_directed_influence_scale_certification.md) | P11 directed influence under target observation coarse-graining with P18 reconstruction control |",
    "| [P25 directed-influence scale certification](proposition_25_directed_influence_scale_certification.md) | P11 directed influence under target observation coarse-graining with P18 reconstruction control |\n| [P26 partition-irreducibility scale certification](proposition_26_partition_irreducibility_scale_certification.md) | P11 partition structure under block-compatible coarse observation with P18 reconstruction control |",
    "navigation interface P26 row",
)
replace_once(
    "docs/research_navigation.md",
    "The P25 physical scale layer is implemented in [directed_influence_scale_certification.py](../src/consciousness_bridge/directed_influence_scale_certification.py), tested in [test_directed_influence_scale_certification.py](../tests/test_directed_influence_scale_certification.py), and summarized by [p25_directed_influence_scale_certification.svg](figures/p25_directed_influence_scale_certification.svg).",
    "The P25 physical scale layer is implemented in [directed_influence_scale_certification.py](../src/consciousness_bridge/directed_influence_scale_certification.py), tested in [test_directed_influence_scale_certification.py](../tests/test_directed_influence_scale_certification.py), and summarized by [p25_directed_influence_scale_certification.svg](figures/p25_directed_influence_scale_certification.svg). The P26 partition-scale layer is implemented in [partition_irreducibility_scale_certification.py](../src/consciousness_bridge/partition_irreducibility_scale_certification.py), tested in [test_partition_irreducibility_scale_certification.py](../tests/test_partition_irreducibility_scale_certification.py), and summarized by [p26_partition_irreducibility_scale_certification.svg](figures/p26_partition_irreducibility_scale_certification.svg).",
    "navigation P26 implementation paragraph",
)

# Equation and citation map -------------------------------------------------
p25_eq_end = r"""P25 is a physical scale theorem with dependency branch P11 + P18. It does not establish scale stability of partition irreducibility, arbitrary source aggregation, changed intervention semantics, physical completeness, or experience.

---

# 20. Candidate consciousness-theory feature families"""
p26_eq = r"""P25 is a physical scale theorem with dependency branch P11 + P18. It does not by itself establish scale stability of partition irreducibility, arbitrary source aggregation, changed intervention semantics, physical completeness, or experience.

---

# 20. P26 - partition-irreducibility scale certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(P_{\pi}^{u,\tau}=\bigotimes_{B\in\pi}P_B^{u,\tau}\) | partition-factorized reference law | P11 physical-signature definition | [P11](proposition_11_intervention_resolved_causal_structure.md) |
| \(\kappa_f^{u,\tau}(\pi)=\|P^{u,\tau}-P_{\pi}^{u,\tau}\|_{\mathrm{TV}}\) | fine partition irreducibility | P11 physical-signature definition | [P11](proposition_11_intervention_resolved_causal_structure.md) |
| \(C_\#P_{\pi}^{u,\tau}=\bigotimes_{B\in\pi}(C_B)_\#P_B^{u,\tau}\) | commutation of productization with block-compatible coarse observation | proved from product pushforward factorization | [P26](proposition_26_partition_irreducibility_scale_certification.md) |
| \(\kappa_c^{u,\tau}(\pi)\le\kappa_f^{u,\tau}(\pi)\) | coarse observation cannot increase declared partition irreducibility | proved by TV contraction | P17; [P26](proposition_26_partition_irreducibility_scale_certification.md) |
| \(0\le\kappa_f-\kappa_c\le\rho(P)+\rho(P_{\pi})\) | reconstruction-controlled partition-scale loss | proved by applying P18 to the response/product-law pair | [P18](proposition_18_scale_sufficiency_certification.md); [P26](proposition_26_partition_irreducibility_scale_certification.md) |
| \(\rho(P)=\rho(P_{\pi})=0\Rightarrow\kappa_c=\kappa_f\) | exact preservation on the declared two-law family | proved corollary | [P26](proposition_26_partition_irreducibility_scale_certification.md) |
| \(\kappa_f>\theta+\rho(P)+\rho(P_{\pi})\Rightarrow\kappa_c>\theta\) | threshold-preservation margin | proved corollary | [P26](proposition_26_partition_irreducibility_scale_certification.md) |

P26 is an observation-scale theorem for one declared partition. It does not yet define the induced map between fine and coarse partition lattices under physical node aggregation, and it does not establish physical completeness or experience.

---

# 21. Candidate consciousness-theory feature families"""
replace_once(
    "docs/equation_and_citation_map.md",
    p25_eq_end,
    p26_eq,
    "equation map P26 section",
)
replace_once(
    "docs/equation_and_citation_map.md",
    "# 21. Citation discipline",
    "# 22. Citation discipline",
    "equation map citation heading renumber",
)

# Release metadata ----------------------------------------------------------
replace_once(
    "pyproject.toml",
    'version = "0.25.0"',
    'version = "0.26.0"',
    "pyproject version",
)
replace_once(
    "pyproject.toml",
    "directed-influence scale certification, recoverability",
    "directed-influence scale certification, partition-irreducibility scale certification, recoverability",
    "pyproject P26 description",
)
replace_once(
    "CITATION.cff",
    "version: 0.25.0",
    "version: 0.26.0",
    "citation version",
)
replace_once(
    "CITATION.cff",
    "directed-influence scale certification, robust experiment design",
    "directed-influence scale certification, partition-irreducibility scale certification, robust experiment design",
    "citation abstract P26",
)

changelog = Path("CHANGELOG.md")
text = changelog.read_text(encoding="utf-8")
marker = "This changelog records theorem-level scientific releases. Definitions, proofs, implementations, tests, figures, and documentation remain linked from the main research page.\n\n"
if text.count(marker) != 1:
    raise RuntimeError("unexpected changelog introduction marker")
entry = r"""## 0.26.0 - 2026-09-09

### Proposition 26 - partition-irreducibility scale certification

- Extended the P11 physical scale program from response geometry and directed influence to the partition-irreducibility component.
- Formalized block-compatible deterministic observation so the declared partition has the same physical meaning at fine and coarse scales.
- Proved that partition productization commutes with block-compatible pushforward.
- Proved contraction \(\kappa_c\le\kappa_f\), so compatible coarse observation cannot manufacture additional partition irreducibility.
- Applied P18 to the response law and its partition-product null to prove \(0\le\kappa_f-\kappa_c\le\rho(P)+\rho(P_\pi)\).
- Kept the two reconstruction terms separate to expose the actual-response and factorized-null reconstruction burdens.
- Proved exact preservation under exact reconstruction and a threshold-survival margin under bounded reconstruction error.
- Added a binary counterexample in which fine irreducibility \(0.4\) collapses to zero after one coordinate is observationally erased.
- Added executable utilities, regression tests, a publication theorem map, README paper integration, theorem-roadmap integration, navigation, provenance, and release guards.
- Preserved the boundary that P26 does not yet solve partition-lattice transport, physical node aggregation, genuine fusion, physical completeness, or experience.

"""
changelog.write_text(text.replace(marker, marker + entry, 1), encoding="utf-8")

# Public guards -------------------------------------------------------------
replace_once(
    "tests/test_main_page_visual_paper.py",
    '    "p25_directed_influence_scale_certification.svg",\n    "observer_to_bridge_handoff.svg",',
    '    "p25_directed_influence_scale_certification.svg",\n    "p26_partition_irreducibility_scale_certification.svg",\n    "observer_to_bridge_handoff.svg",',
    "main-page canonical P26 figure",
)
replace_once(
    "tests/test_main_page_visual_paper.py",
    "for index in range(1, 26):",
    "for index in range(1, 27):",
    "main-page P26 proposition range",
)
replace_once(
    "tests/test_document_link_integrity.py",
    "for number in range(1, 26):",
    "for number in range(1, 27):",
    "navigation P26 proposition range",
)
replace_once(
    "tests/test_visual_and_terminology_quality.py",
    '    "p25_directed_influence_scale_certification.svg",\n    "universal_proof_ladder.svg",',
    '    "p25_directed_influence_scale_certification.svg",\n    "p26_partition_irreducibility_scale_certification.svg",\n    "universal_proof_ladder.svg",',
    "visual guard P26 figure",
)

# Global theorem roadmap SVG ------------------------------------------------
replace_once(
    "docs/figures/theorem_roadmap.svg",
    'height="2410" viewBox="0 0 1600 2410"',
    'height="2640" viewBox="0 0 1600 2640"',
    "roadmap SVG dimensions",
)
replace_once(
    "docs/figures/theorem_roadmap.svg",
    "Theorem roadmap through Proposition 25",
    "Theorem roadmap through Proposition 26",
    "roadmap SVG title",
)
replace_once(
    "docs/figures/theorem_roadmap.svg",
    "Theorem Roadmap - P1 through P25",
    "Theorem Roadmap - P1 through P26",
    "roadmap SVG heading",
)
replace_once(
    "docs/figures/theorem_roadmap.svg",
    '<rect width="1600" height="2180" fill="#ffffff"/>',
    '<rect width="1600" height="2640" fill="#ffffff"/>',
    "roadmap SVG background",
)
old_tail = '''  <rect x="95" y="2320" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="2345" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="2368" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Partition scale, block aggregation, physical completeness, and experiential formalization remain open.</text>
</svg>'''
new_tail = '''  <rect x="225" y="2320" width="1150" height="190" rx="20" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="265" y="2357" class="label">PHYSICAL SCALE BRANCH · P26</text>
  <text x="265" y="2395" class="head">P11 partition structure + P17 contraction + P18 reconstruction</text>
  <text x="265" y="2429" class="body">Block-compatible observation cannot increase declared irreducibility.</text>
  <text x="265" y="2464" class="eq">0 ≤ κf − κc ≤ ρ(P) + ρ(Pπ)</text>
  <text x="790" y="2464" class="eq">κf &gt; θ + ε ⇒ κc &gt; θ</text>
  <text x="265" y="2494" class="body">Partition-lattice transport under node aggregation remains open.</text>

  <rect x="95" y="2550" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="2575" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="2598" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Block aggregation, partition-lattice transport, physical completeness, and experiential formalization remain open.</text>
</svg>'''
replace_once(
    "docs/figures/theorem_roadmap.svg",
    old_tail,
    new_tail,
    "roadmap SVG P26 tail",
)

# Tighten the standalone P26 figure footer before it becomes canonical.
replace_once(
    "docs/figures/p26_partition_irreducibility_scale_certification.svg",
    "P26 certifies one declared partition under block-compatible observation. Partition-lattice aggregation, genuine physical fusion, complete P11 scale equivalence, and experiential interpretation remain open.",
    "P26 certifies one partition under compatible observation. Partition-lattice aggregation, physical fusion, full P11 scale equivalence, and experience remain open.",
    "P26 figure footer copy",
)

# Final release requirements ------------------------------------------------
for path, token, label in (
    ("README.md", "**P26**", "README P26 theorem marker"),
    ("README.md", "p26_partition_irreducibility_scale_certification.svg", "README P26 figure"),
    ("docs/theorem_roadmap.md", "proposition_26_partition_irreducibility_scale_certification.md", "roadmap P26 link"),
    ("docs/research_navigation.md", "proposition_26_partition_irreducibility_scale_certification.md", "navigation P26 link"),
    ("docs/equation_and_citation_map.md", "# 20. P26 - partition-irreducibility scale certification", "equation map P26 section"),
    ("pyproject.toml", 'version = "0.26.0"', "pyproject release version"),
    ("CITATION.cff", "version: 0.26.0", "citation release version"),
):
    require(path, token, label)
