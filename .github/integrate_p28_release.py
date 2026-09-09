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
replace_once("README.md", "version-0.27.0-2563eb", "version-0.28.0-2563eb", "README badge")
replace_once("README.md", "**27 proposition-level results", "**28 proposition-level results", "README result count")
replace_once("README.md", "P1 through P27 with explicit dependency branches", "P1 through P28 with explicit dependency branches", "README theorem range")
replace_once("README.md", "| proposition-level results | **27** |", "| proposition-level results | **28** |", "README proposition count")
replace_once("README.md", "| research-software version | **0.27.0** |", "| research-software version | **0.28.0** |", "README version table")
replace_once("README.md", "# 7. Theorem roadmap - P1 through P27", "# 7. Theorem roadmap - P1 through P28", "README theorem heading")
replace_once("README.md", "the P1-P27 proposition chain", "the P1-P28 proposition chain", "README reproducibility range")
replace_once(
    "README.md",
    "**P27** then allows the node set itself to change: a fine partition descends through a surjective node aggregation exactly when it is saturated by the aggregation fibers, the surviving partitions form a lattice isomorphic to the coarse partition lattice, and P18 controls any remaining irreducibility loss under an aggregation-compatible state map.",
    "**P27** then allows the node set itself to change: a fine partition descends through a surjective node aggregation exactly when it is saturated by the aggregation fibers, the surviving partitions form a lattice isomorphic to the coarse partition lattice, and P18 controls any remaining irreducibility loss under an aggregation-compatible state map. **P28** transports the P11 directed-influence branch through the same changing node set by giving an exact compatibility criterion for matched intervention-pair source labels, pooling only inherited comparisons within each aggregate source, and applying P25/P18 control to the full fine target fiber before target-state aggregation.",
    "README abstract P28",
)
replace_once(
    "README.md",
    "| partition-lattice node-aggregation theorem | [Proposition 27](docs/proposition_27_partition_lattice_node_aggregation.md) | exact partition descent, lattice transport, and P18-controlled irreducibility under changing node sets |",
    "| partition-lattice node-aggregation theorem | [Proposition 27](docs/proposition_27_partition_lattice_node_aggregation.md) | exact partition descent, lattice transport, and P18-controlled irreducibility under changing node sets |\n| intervention node-aggregation theorem | [Proposition 28](docs/proposition_28_intervention_node_aggregation_compatibility.md) | source-label descent and directed-influence certification across aggregate source and target nodes |",
    "README P28 nav row",
)
replace_once(
    "README.md",
    "| implementation of P27 | [partition_lattice_node_aggregation.py](src/consciousness_bridge/partition_lattice_node_aggregation.py) | saturated partition descent, lattice isomorphism, aggregate-state maps, and node-aggregation irreducibility certificate |",
    "| implementation of P27 | [partition_lattice_node_aggregation.py](src/consciousness_bridge/partition_lattice_node_aggregation.py) | saturated partition descent, lattice isomorphism, aggregate-state maps, and node-aggregation irreducibility certificate |\n| implementation of P28 | [intervention_node_aggregation_compatibility.py](src/consciousness_bridge/intervention_node_aggregation_compatibility.py) | matched-pair source descent and aggregate-source/target directed-influence certificate |",
    "README P28 implementation row",
)
replace_once(
    "README.md",
    "| **11.3 P27 partition lattice under node aggregation** | Which fine partitions remain well-defined after several nodes become one coarse node? |",
    "| **11.3 P27 partition lattice under node aggregation** | Which fine partitions remain well-defined after several nodes become one coarse node? |\n| **11.4 P28 intervention compatibility under node aggregation** | When do matched intervention comparisons retain an unambiguous source meaning after node aggregation? |",
    "README P28 paper map row",
)
replace_once(
    "README.md",
    "| **P27** | aggregation-saturated fine partitions are exactly those that descend through a surjective node map; the surviving partition lattice is isomorphic to the coarse partition lattice, with P18 controlling probabilistic irreducibility loss | proved physical scale theorem | [P27](docs/proposition_27_partition_lattice_node_aggregation.md) |",
    "| **P27** | aggregation-saturated fine partitions are exactly those that descend through a surjective node map; the surviving partition lattice is isomorphic to the coarse partition lattice, with P18 controlling probabilistic irreducibility loss | proved physical scale theorem | [P27](docs/proposition_27_partition_lattice_node_aggregation.md) |\n| **P28** | matched intervention-pair source labels descend iff each pair has at most one coarse source image; aggregate-source influence then contracts under target-fiber state aggregation with P18 reconstruction control | proved physical scale theorem | [P28](docs/proposition_28_intervention_node_aggregation_compatibility.md) |",
    "README P28 theorem row",
)

p27_end = r"""[Read Proposition 27](docs/proposition_27_partition_lattice_node_aggregation.md). The [P27 theorem map](docs/figures/p27_partition_lattice_node_aggregation.svg), [implementation](src/consciousness_bridge/partition_lattice_node_aggregation.py), and [tests](tests/test_partition_lattice_node_aggregation.py) expose the complete proof-to-code path.

---

# 14. Observer-to-bridge handoff"""
p28_section = r"""[Read Proposition 27](docs/proposition_27_partition_lattice_node_aggregation.md). The [P27 theorem map](docs/figures/p27_partition_lattice_node_aggregation.svg), [implementation](src/consciousness_bridge/partition_lattice_node_aggregation.py), and [tests](tests/test_partition_lattice_node_aggregation.py) expose the complete proof-to-code path.

## 13.6 P28 - intervention compatibility under node aggregation

![P28 intervention compatibility under node aggregation](docs/figures/p28_intervention_node_aggregation_compatibility.svg)

P28 transports the P11 directed-influence branch through the changing node set introduced by P27. For each fine source \(i\), let \(\mathcal E_i\) be its declared matched intervention-pair family. For a pair \(e\), define its fine source incidence

\[
S_f(e)=\{i:e\in\mathcal E_i\}.
\]

Under the surjective node map \(a:V_f\twoheadrightarrow V_c\), the pair has an unambiguous coarse source label exactly when

\[
\boxed{
|\{a(i):i\in S_f(e)\}|\le1.
}
\]

Equivalently,

\[
\boxed{
e\in\mathcal E_i\cap\mathcal E_j
\Longrightarrow a(i)=a(j).
}
\]

When this condition holds, the inherited coarse pair family is

\[
\boxed{
\mathcal E_c^a
=
\bigcup_{i\in a^{-1}(c)}\mathcal E_i.
}
\]

This union is a pooling of already declared comparisons. It is not a newly inferred simultaneous perturbation of every fine source in the aggregate node.

For coarse target \(d\), P28 first takes the full fine target-fiber marginal

\[
\boxed{
P_{F_d}^{u,\tau}
=
\operatorname{Marg}_{F_d}P^{u,\tau},
\qquad F_d=a^{-1}(d),
}
\]

and defines inherited fine block influence

\[
\boxed{
A_{c\to d}^{f,a}(\tau)
=
\sup_{(u,v)\in\mathcal E_c^a}
\|P_{F_d}^{u,\tau}-P_{F_d}^{v,\tau}\|_{\mathrm{TV}}.
}
\]

If \(g_d\) is the declared target-fiber state map, the coarse response is \(\overline P_d^{u,\tau}=(g_d)_\#P_{F_d}^{u,\tau}\) and

\[
\boxed{
A_{c\to d}^{c,a}(\tau)
\le
A_{c\to d}^{f,a}(\tau).
}
\]

Thus target-state aggregation cannot create a stronger directed-influence value once the source intervention semantics have validly descended.

With P18 target-fiber reconstruction defect

\[
\rho_{c\to d}^{a}(\tau)
=
\sup_u
\|P_{F_d}^{u,\tau}-(R_d)_\#(g_d)_\#P_{F_d}^{u,\tau}\|_{\mathrm{TV}},
\]

P28 obtains

\[
\boxed{
0\le
A_{c\to d}^{f,a}(\tau)-A_{c\to d}^{c,a}(\tau)
\le
2\rho_{c\to d}^{a}(\tau).
}
\]

Therefore exact target reconstruction gives exact influence preservation, and for threshold \(\theta\),

\[
\boxed{
A_{c\to d}^{f,a}(\tau)>
\theta+2\rho_{c\to d}^{a}(\tau)
\Longrightarrow
A_{c\to d}^{c,a}(\tau)>	heta.
}
\]

The central interpretation guard is

\[
\boxed{
\text{aggregate source label}
\neq
\text{new aggregate physical actuator}.
}
\]

A simultaneous or synergistic intervention on several fine constituents requires its own independently declared protocol and response laws. P28 does not manufacture that experiment by notation.

After P27 and P28, the changing-node-set transport problem has explicit rules for the P11 partition component \(\mathcal K\) and directed-influence component \(\mathcal A\). The next physical theorem burden is to align the complete response geometry \(\mathcal G\), admissible intervention family \(\mathcal U\), and delays \(\mathcal T\) under the same node quotient before claiming full P11 scale equivalence.

[Read Proposition 28](docs/proposition_28_intervention_node_aggregation_compatibility.md). The [P28 theorem map](docs/figures/p28_intervention_node_aggregation_compatibility.svg), [implementation](src/consciousness_bridge/intervention_node_aggregation_compatibility.py), and [tests](tests/test_intervention_node_aggregation_compatibility.py) expose the complete proof-to-code path.

---

# 14. Observer-to-bridge handoff"""
replace_once("README.md", p27_end, p28_section, "README P28 section")
replace_once(
    "README.md",
    "P27 identifies exactly which fine partitions remain meaningful when the node set itself is aggregated and quantifies their remaining irreducibility under aggregation-compatible state maps.",
    "P27 identifies exactly which fine partitions remain meaningful when the node set itself is aggregated and quantifies their remaining irreducibility under aggregation-compatible state maps. P28 adds the source-side compatibility condition required to transport matched intervention comparisons and directed influence through that same node quotient.",
    "README scale falsification P28",
)

# Theorem roadmap.
replace_once("docs/theorem_roadmap.md", "![P1-P27 theorem roadmap]", "![P1-P28 theorem roadmap]", "roadmap alt")
replace_once(
    "docs/theorem_roadmap.md",
    "| [P27](proposition_27_partition_lattice_node_aggregation.md) | surjective node quotient plus partition saturation, lattice transport, P17 contraction, and P18 reconstruction | exact criterion for surviving partition semantics under node aggregation and quantitative irreducibility control | proved physical scale theorem |",
    "| [P27](proposition_27_partition_lattice_node_aggregation.md) | surjective node quotient plus partition saturation, lattice transport, P17 contraction, and P18 reconstruction | exact criterion for surviving partition semantics under node aggregation and quantitative irreducibility control | proved physical scale theorem |\n| [P28](proposition_28_intervention_node_aggregation_compatibility.md) | P11 matched-pair source incidence plus P25 target contraction and P27 node aggregation | exact source-label descent and directed-influence certification across aggregate nodes | proved physical scale theorem |",
    "roadmap P28 row",
)
p27_roadmap_end = r"""Direct proof: [Proposition 27](proposition_27_partition_lattice_node_aggregation.md). Implementation: [partition_lattice_node_aggregation.py](../src/consciousness_bridge/partition_lattice_node_aggregation.py). Tests: [test_partition_lattice_node_aggregation.py](../tests/test_partition_lattice_node_aggregation.py).

---

# 8. Fundamental physical sufficiency: P19"""
p28_roadmap = r"""Direct proof: [Proposition 27](proposition_27_partition_lattice_node_aggregation.md). Implementation: [partition_lattice_node_aggregation.py](../src/consciousness_bridge/partition_lattice_node_aggregation.py). Tests: [test_partition_lattice_node_aggregation.py](../tests/test_partition_lattice_node_aggregation.py).

## P28 - intervention compatibility under node aggregation

For each matched intervention pair \(e\), let \(S_f(e)=\{i:e\in\mathcal E_i\}\). Exact coarse source labeling exists iff

\[
\boxed{
|\{a(i):i\in S_f(e)\}|\le1
\quad\forall e.
}
\]

Then the coarse source family is the inherited union

\[
\mathcal E_c^a=\bigcup_{i\in a^{-1}(c)}\mathcal E_i.
\]

For target fiber \(F_d=a^{-1}(d)\), P28 defines the inherited fine block influence and proves

\[
\boxed{
A_{c\to d}^{c,a}(\tau)
\le
A_{c\to d}^{f,a}(\tau),
}
\]

with P18 reconstruction control

\[
\boxed{
0\le A_{c\to d}^{f,a}-A_{c\to d}^{c,a}
\le2\rho_{c\to d}^{a}.
}
\]

Pooling inherited intervention pairs does not create a simultaneous aggregate actuator. Full P11 scale equivalence still requires response-geometry and intervention-family alignment.

Direct proof: [Proposition 28](proposition_28_intervention_node_aggregation_compatibility.md). Implementation: [intervention_node_aggregation_compatibility.py](../src/consciousness_bridge/intervention_node_aggregation_compatibility.py). Tests: [test_intervention_node_aggregation_compatibility.py](../tests/test_intervention_node_aggregation_compatibility.py).

---

# 8. Fundamental physical sufficiency: P19"""
replace_once("docs/theorem_roadmap.md", p27_roadmap_end, p28_roadmap, "roadmap P28 section")

# Research navigation.
replace_once("docs/research_navigation.md", "from P1 through P27", "from P1 through P28", "navigation range")
replace_once(
    "docs/research_navigation.md",
    "13. [Proposition 27](proposition_27_partition_lattice_node_aggregation.md) for exact partition descent and lattice transport under node aggregation.\n14. [Fundamental Theory to Consciousness program]",
    "13. [Proposition 27](proposition_27_partition_lattice_node_aggregation.md) for exact partition descent and lattice transport under node aggregation.\n14. [Proposition 28](proposition_28_intervention_node_aggregation_compatibility.md) for source-label descent and directed-influence certification under node aggregation.\n15. [Fundamental Theory to Consciousness program]",
    "navigation reading P28",
)
replace_once("docs/research_navigation.md", "15. [Stochastic fundamental bridge]", "16. [Stochastic fundamental bridge]", "navigation number 16")
replace_once("docs/research_navigation.md", "16. [Falsification program]", "17. [Falsification program]", "navigation number 17")
replace_once("docs/research_navigation.md", "17. [Citation and Reference Policy]", "18. [Citation and Reference Policy]", "navigation number 18")
replace_once(
    "docs/research_navigation.md",
    "| P27 | [Partition-lattice node aggregation](proposition_27_partition_lattice_node_aggregation.md) | exact saturated-partition descent, lattice transport, and irreducibility control across changing node sets |",
    "| P27 | [Partition-lattice node aggregation](proposition_27_partition_lattice_node_aggregation.md) | exact saturated-partition descent, lattice transport, and irreducibility control across changing node sets |\n| P28 | [Intervention node-aggregation compatibility](proposition_28_intervention_node_aggregation_compatibility.md) | exact matched-pair source descent and aggregate-node directed-influence control |",
    "navigation P28 proposition row",
)
replace_once(
    "docs/research_navigation.md",
    "| [P27 partition-lattice node aggregation](proposition_27_partition_lattice_node_aggregation.md) | partition semantics and irreducibility under explicit many-to-one node aggregation |",
    "| [P27 partition-lattice node aggregation](proposition_27_partition_lattice_node_aggregation.md) | partition semantics and irreducibility under explicit many-to-one node aggregation |\n| [P28 intervention node-aggregation compatibility](proposition_28_intervention_node_aggregation_compatibility.md) | matched intervention semantics and directed influence across aggregate source and target nodes |",
    "navigation P28 interface row",
)
replace_once(
    "docs/research_navigation.md",
    "and summarized by [p27_partition_lattice_node_aggregation.svg](figures/p27_partition_lattice_node_aggregation.svg).",
    "and summarized by [p27_partition_lattice_node_aggregation.svg](figures/p27_partition_lattice_node_aggregation.svg). The P28 intervention-aggregation layer is implemented in [intervention_node_aggregation_compatibility.py](../src/consciousness_bridge/intervention_node_aggregation_compatibility.py), tested in [test_intervention_node_aggregation_compatibility.py](../tests/test_intervention_node_aggregation_compatibility.py), and summarized by [p28_intervention_node_aggregation_compatibility.svg](figures/p28_intervention_node_aggregation_compatibility.svg).",
    "navigation P28 implementation",
)

# Equation provenance.
p27_boundary = r"""P27 distinguishes failure of partition semantics from loss of partition signal. It does not yet transport intervention channels or directed influence through source-node aggregation and does not establish physical completeness or experience.

---

# 22. Candidate consciousness-theory feature families"""
p28_eq = r"""P27 distinguishes failure of partition semantics from loss of partition signal. P28 supplies the matched-intervention source-label transport needed for the directed-influence branch.

---

# 22. P28 - intervention compatibility under node aggregation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(S_f(e)=\{i:e\in\mathcal E_i\}\) | fine source-incidence set of one matched intervention pair | repository definition | [P28](proposition_28_intervention_node_aggregation_compatibility.md) |
| \(|\{a(i):i\in S_f(e)\}|\le1\) | exact compatibility criterion for unambiguous coarse source labeling | proved necessary and sufficient | [P28](proposition_28_intervention_node_aggregation_compatibility.md) |
| \(\mathcal E_c^a=\bigcup_{i\in a^{-1}(c)}\mathcal E_i\) | canonical pooling of inherited matched comparisons | repository construction | [P28](proposition_28_intervention_node_aggregation_compatibility.md) |
| \(P_{F_d}^{u,\tau}=\operatorname{Marg}_{F_d}P^{u,\tau}\) | complete fine response block represented by aggregate target \(d\) | repository construction from P11 marginalization | P11; [P28](proposition_28_intervention_node_aggregation_compatibility.md) |
| \(A_{c\to d}^{c,a}\le A_{c\to d}^{f,a}\) | target aggregation cannot increase directed influence for the descended pair family | proved by TV contraction | P17, P25; [P28](proposition_28_intervention_node_aggregation_compatibility.md) |
| \(0\le A_f-A_c\le2\rho_{c\to d}^{a}\) | reconstruction-controlled aggregate-node influence loss | proved by P18 applied pairwise before the supremum | P18, P25; [P28](proposition_28_intervention_node_aggregation_compatibility.md) |
| aggregate source label \(\ne\) new aggregate actuator | prevents pair-family pooling from being misread as physical intervention synergy | interpretation boundary | [P28](proposition_28_intervention_node_aggregation_compatibility.md) |

P28 is a theorem about declared intervention comparisons and target response blocks. It does not create simultaneous interventions, establish complete P11 scale equivalence, physical completeness, or experience.

---

# 23. Candidate consciousness-theory feature families"""
replace_once("docs/equation_and_citation_map.md", p27_boundary, p28_eq, "equation map P28")
replace_once("docs/equation_and_citation_map.md", "# 23. Citation discipline", "# 24. Citation discipline", "equation citation renumber")

# Release metadata.
replace_once("pyproject.toml", 'version = "0.27.0"', 'version = "0.28.0"', "pyproject version")
replace_once(
    "pyproject.toml",
    "partition-lattice node aggregation, recoverability",
    "partition-lattice node aggregation, intervention node-aggregation compatibility, recoverability",
    "pyproject description",
)

citation = Path("CITATION.cff")
text = citation.read_text(encoding="utf-8")
if "version: 0.27.0" not in text:
    raise RuntimeError("unexpected citation version")
text = text.replace("version: 0.27.0", "version: 0.28.0", 1)
if "intervention node-aggregation compatibility" not in text:
    text = text.replace(
        "partition-lattice node aggregation",
        "partition-lattice node aggregation, intervention node-aggregation compatibility",
        1,
    )
citation.write_text(text, encoding="utf-8")

changelog = Path("CHANGELOG.md")
text = changelog.read_text(encoding="utf-8")
marker = "This changelog records theorem-level scientific releases. Definitions, proofs, implementations, tests, figures, and documentation remain linked from the main research page.\n\n"
if text.count(marker) != 1:
    raise RuntimeError("unexpected changelog marker")
entry = r"""## 0.28.0 - 2026-09-09

### Proposition 28 - intervention compatibility under node aggregation

- Extended the P25 directed-influence scale branch through the changing node set introduced by P27.
- Defined the fine source-incidence set of each matched intervention pair and proved the exact condition for unambiguous coarse source descent.
- Defined canonical coarse source pair families as unions of inherited fine pair families within each aggregation fiber, with duplicate comparisons removed.
- Explicitly separated aggregate source labeling from any claim of a new simultaneous aggregate actuator.
- Defined the fine target block as the full response marginal on the target aggregation fiber rather than an arbitrary constituent node.
- Proved directed-influence contraction under deterministic target-fiber state aggregation.
- Applied P18 reconstruction to prove \(0\le A_f-A_c\le2\rho\), with exact-preservation and threshold-edge corollaries.
- Added executable implementation, nine regression tests, a publication theorem map, main-paper integration, roadmap, navigation, provenance, release guards, and synchronized 0.28.0 metadata.
- Preserved the boundary that response-geometry alignment, genuinely new aggregate interventions, complete P11 scale equivalence, physical completeness, and experience remain open.

"""
changelog.write_text(text.replace(marker, marker + entry, 1), encoding="utf-8")

# Public guards.
replace_once(
    "tests/test_main_page_visual_paper.py",
    '    "p27_partition_lattice_node_aggregation.svg",\n    "observer_to_bridge_handoff.svg",',
    '    "p27_partition_lattice_node_aggregation.svg",\n    "p28_intervention_node_aggregation_compatibility.svg",\n    "observer_to_bridge_handoff.svg",',
    "main page P28 figure",
)
replace_once("tests/test_main_page_visual_paper.py", "for index in range(1, 28):", "for index in range(1, 29):", "main page P28 range")
replace_once("tests/test_document_link_integrity.py", "for number in range(1, 28):", "for number in range(1, 29):", "navigation P28 range")
replace_once(
    "tests/test_visual_and_terminology_quality.py",
    '    "p27_partition_lattice_node_aggregation.svg",\n    "universal_proof_ladder.svg",',
    '    "p27_partition_lattice_node_aggregation.svg",\n    "p28_intervention_node_aggregation_compatibility.svg",\n    "universal_proof_ladder.svg",',
    "visual P28 figure",
)

# Global theorem roadmap SVG.
roadmap = Path("docs/figures/theorem_roadmap.svg")
text = roadmap.read_text(encoding="utf-8")
text = text.replace('height="2870" viewBox="0 0 1600 2870"', 'height="3100" viewBox="0 0 1600 3100"', 1)
text = text.replace("Theorem roadmap through Proposition 27", "Theorem roadmap through Proposition 28", 1)
text = text.replace("Theorem Roadmap - P1 through P27", "Theorem Roadmap - P1 through P28", 1)
text = text.replace('<rect width="1600" height="2870" fill="#ffffff"/>', '<rect width="1600" height="3100" fill="#ffffff"/>', 1)
old_tail = '''  <rect x="95" y="2790" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="2815" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="2838" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Intervention aggregation, full P11 scale equivalence, physical completeness, and experiential formalization remain open.</text>
</svg>'''
new_tail = '''  <rect x="225" y="2790" width="1150" height="190" rx="20" fill="#ecfeff" stroke="#0891b2" stroke-width="1.8"/>
  <text x="265" y="2827" class="label">INTERVENTION AGGREGATION · P28</text>
  <text x="265" y="2865" class="head">Matched-pair source labels must descend consistently</text>
  <text x="265" y="2899" class="body">Each inherited pair has at most one aggregate source image.</text>
  <text x="265" y="2934" class="eq">|{a(i):i∈Sf(e)}| ≤ 1</text>
  <text x="765" y="2934" class="eq">0 ≤ Af − Ac ≤ 2ρ</text>
  <text x="265" y="2964" class="body">Pair pooling is not a new simultaneous aggregate intervention.</text>

  <rect x="95" y="3030" width="1410" height="62" rx="14" fill="#0f172a"/>
  <text x="125" y="3055" style="font:700 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#cbd5e1">OPEN BRIDGE FRONTIER</text>
  <text x="125" y="3078" style="font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#f8fafc">Full response geometry, complete P11 scale equivalence, physical completeness, and experiential formalization remain open.</text>
</svg>'''
if old_tail not in text:
    raise RuntimeError("P27 roadmap tail not found")
roadmap.write_text(text.replace(old_tail, new_tail, 1), encoding="utf-8")

for path, token, label in (
    ("README.md", "**P28**", "README P28 marker"),
    ("README.md", "p28_intervention_node_aggregation_compatibility.svg", "README P28 figure"),
    ("docs/theorem_roadmap.md", "proposition_28_intervention_node_aggregation_compatibility.md", "roadmap P28 link"),
    ("docs/research_navigation.md", "proposition_28_intervention_node_aggregation_compatibility.md", "navigation P28 link"),
    ("docs/equation_and_citation_map.md", "# 22. P28 - intervention compatibility under node aggregation", "equation P28"),
    ("pyproject.toml", 'version = "0.28.0"', "pyproject P28"),
    ("CITATION.cff", "version: 0.28.0", "citation P28"),
):
    require(path, token, label)
