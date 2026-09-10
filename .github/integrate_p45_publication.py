from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one marker, found {count}")
    return text.replace(old, new, 1)


def write(path: str, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8")


# README
path = Path("README.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version-0.44.0-2563eb", "version-0.45.0-2563eb", "README badge")
text = replace_once(
    text,
    "**P44** extends the finite-sample design from one preselected preparation pair to a finite predeclared family, proves simultaneous family coverage, and shows that any measurable data-dependent witness selector remains valid on that shared confidence event.",
    "**P44** extends the finite-sample design from one preselected preparation pair to a finite predeclared family, proves simultaneous family coverage, and shows that any measurable data-dependent witness selector remains valid on that shared confidence event. **P45** then moves the resource-allocation problem from independent candidate pairs to a shared preparation graph: one preparation-level sample stream can tighten every incident candidate edge, the resulting inverse-square design problem is strictly convex, and the unique optimum obeys an incidence-weighted cube-root KKT law.",
    "README abstract P45",
)
text = replace_once(text, "**44 proposition-level results, 58 equation-driven quantitative figures", "**45 proposition-level results, 58 equation-driven quantitative figures", "README record count")
text = text.replace("P1 through P44", "P1 through P45")
text = replace_once(
    text,
    "| pair-adaptive finite-family certification | [Proposition 44](docs/proposition_44_pair_adaptive_sample_allocation.md) | simultaneous family confidence and valid post-data witness selection for a finite predeclared candidate set |",
    "| pair-adaptive finite-family certification | [Proposition 44](docs/proposition_44_pair_adaptive_sample_allocation.md) | simultaneous family confidence and valid post-data witness selection for a finite predeclared candidate set |\n| shared-preparation graph allocation | [Proposition 45](docs/proposition_45_shared_preparation_graph_allocation.md) | unique minimum-cost preparation-level allocation for overlapping candidate edges with an incidence-weighted KKT characterization |",
    "README navigation P45",
)
text = replace_once(
    text,
    "| **11.20 P44 pair-adaptive finite-family certification** | Can a witness pair be selected after seeing the data without losing family-level validity? |",
    "| **11.20 P44 pair-adaptive finite-family certification** | Can a witness pair be selected after seeing the data without losing family-level validity? |\n| **11.21 P45 shared-preparation graph allocation** | How should preparation-level samples be allocated when candidate witness pairs share vertices and data streams? |",
    "README paper map P45",
)
text = replace_once(text, "| proposition-level results | **44** |", "| proposition-level results | **45** |", "README table result count")
text = replace_once(text, "| research-software version | **0.44.0** |", "| research-software version | **0.45.0** |", "README table version")
text = replace_once(
    text,
    "| implementation of P44 | [pair_adaptive_sample_allocation.py](src/consciousness_bridge/pair_adaptive_sample_allocation.py) | finite-family confidence spending and post-selection certificate |",
    "| implementation of P44 | [pair_adaptive_sample_allocation.py](src/consciousness_bridge/pair_adaptive_sample_allocation.py) | finite-family confidence spending and post-selection certificate |\n| implementation of P45 | [shared_preparation_graph_allocation.py](src/consciousness_bridge/shared_preparation_graph_allocation.py) | shared preparation-level graph allocation, single-edge closed form, and KKT certificate utilities |",
    "README implementation P45",
)
p44_tail = "[Read Proposition 44](docs/proposition_44_pair_adaptive_sample_allocation.md). The [P44 theorem map](docs/figures/p44_pair_adaptive_sample_allocation.svg), [implementation](src/consciousness_bridge/pair_adaptive_sample_allocation.py), and [tests](tests/test_pair_adaptive_sample_allocation.py) expose the complete proof-to-code path.\n\n---\n\n# 14. Observer-to-bridge handoff"
p45_section = r'''[Read Proposition 44](docs/proposition_44_pair_adaptive_sample_allocation.md). The [P44 theorem map](docs/figures/p44_pair_adaptive_sample_allocation.svg), [implementation](src/consciousness_bridge/pair_adaptive_sample_allocation.py), and [tests](tests/test_pair_adaptive_sample_allocation.py) expose the complete proof-to-code path.

## 13.18 P45 - shared-preparation graph allocation

![P45 shared-preparation graph allocation](docs/figures/p45_shared_preparation_graph_allocation.svg)

P44 allows a final witness pair to be chosen after observing the data, provided the candidate family and simultaneous confidence control were declared in advance. P45 addresses the complementary design problem that appears when several candidate pairs share preparations and therefore share sample streams.

Let the candidate family form an undirected graph

\[
G=(V,E),
\]

with preparations as vertices and candidate regularity witnesses as edges. For edge \(e=\{i,j\}\), define the population regularity gap

\[
\boxed{
\Delta_e=d_{Y,e}-L_ed_{Q,e}.
}
\]

If preparation \(i\) has target uncertainty radius \(\varepsilon_i\) and quantum reconstruction radius \(r_i\), the nonuniform P42 argument yields

\[
\boxed{
\widehat M_e
\ge
\Delta_e
-2(\varepsilon_i+\varepsilon_j)
-2L_e(r_i+r_j).
}
\]

Thus the preparation-level design constraint for each candidate edge is

\[
\boxed{
2(\varepsilon_i+\varepsilon_j)
+2L_e(r_i+r_j)
\le
\Delta_e.
}
\]

Assume preparation-specific concentration laws

\[
\varepsilon_i=\frac{a_{Y,i}}{\sqrt{n_{Y,i}}},
\qquad
r_i=\frac{a_{Q,i}}{\sqrt{n_{Q,i}}}.
\]

With positive weighted sample-cost coefficients \(w_{Y,i}\) and \(w_{Q,i}\), the continuous design objective is

\[
\boxed{
C(\varepsilon,r)
=
\sum_i\frac{w_{Y,i}}{\varepsilon_i^2}
+
\sum_i\frac{w_{Q,i}}{r_i^2}.
}
\]

P45 proves that, under positive weights, positive edge gaps, graph coverage of the optimized vertices, and nonempty positive feasibility, this objective has a unique global minimizer. The reason is structural: every inverse-square term is strictly convex and every graph edge constraint is affine.

The optimum obeys an incidence-weighted KKT law. If \(\lambda_e\ge0\) is the multiplier for edge \(e\), then

\[
\boxed{
\frac{w_{Y,i}}{\varepsilon_i^3}
=
\sum_{e\ni i}\lambda_e,
}
\]

and

\[
\boxed{
\frac{w_{Q,i}}{r_i^3}
=
\sum_{e\ni i}\lambda_eL_e.
}
\]

Equivalently,

\[
\varepsilon_i
=
\left(
\frac{w_{Y,i}}{\sum_{e\ni i}\lambda_e}
\right)^{1/3},
\qquad
r_i
=
\left(
\frac{w_{Q,i}}{\sum_{e\ni i}\lambda_eL_e}
\right)^{1/3}
\]

whenever the corresponding denominators are positive. This is the graph version of the P43 cube-root allocation law. The required precision at one preparation is determined by all active incident edge constraints, not by one pair in isolation.

For a single edge with coefficient vector \(a=(2,2,2L_e,2L_e)\) and stream weights \(w_l\), define

\[
S_e=\sum_l a_l^{2/3}w_l^{1/3}.
\]

The unique continuous optimum is

\[
\boxed{
u_l^*
=
\frac{\Delta_e}{S_e}
\left(\frac{w_l}{a_l}\right)^{1/3},
}
\]

with exact minimum cost

\[
\boxed{
C_e^*=\frac{S_e^3}{\Delta_e^2}.
}
\]

Ceiling the resulting continuous sample counts preserves feasibility because increasing sample size decreases every radius of the form \(a/\sqrt n\).

The combined design logic is now

\[
\boxed{
\text{P45 shared preparation allocation}
+
\text{simultaneous confidence}
+
\text{P44 post-selection}
\Longrightarrow
\text{resource-aware valid selected witness}.
}
\]

The scientific boundary remains explicit. P45 is an experimental resource-allocation theorem for a declared quantum descriptor family and bridge regularity class. It does not establish physical completeness, quantum incompleteness, or consciousness.

[Read Proposition 45](docs/proposition_45_shared_preparation_graph_allocation.md). The [P45 theorem map](docs/figures/p45_shared_preparation_graph_allocation.svg), [implementation](src/consciousness_bridge/shared_preparation_graph_allocation.py), and [tests](tests/test_shared_preparation_graph_allocation.py) expose the complete proof-to-code path.

---

# 14. Observer-to-bridge handoff'''
text = replace_once(text, p44_tail, p45_section, "README P45 section")
write("README.md", text)

# Theorem roadmap
path = Path("docs/theorem_roadmap.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "![P44 finite-family post-selection certificate](figures/p44_pair_adaptive_sample_allocation.svg)\n",
    "![P44 finite-family post-selection certificate](figures/p44_pair_adaptive_sample_allocation.svg)\n\n![P45 shared-preparation graph allocation](figures/p45_shared_preparation_graph_allocation.svg)\n",
    "roadmap P45 figure",
)
text = replace_once(
    text,
    "| [P44](proposition_44_pair_adaptive_sample_allocation.md) | finite-family union bound and simultaneous lower-margin coverage | valid data-dependent witness selection among predeclared candidate pairs | proved post-selection theorem |",
    "| [P44](proposition_44_pair_adaptive_sample_allocation.md) | finite-family union bound and simultaneous lower-margin coverage | valid data-dependent witness selection among predeclared candidate pairs | proved post-selection theorem |\n| [P45](proposition_45_shared_preparation_graph_allocation.md) | strictly convex shared-vertex allocation plus incidence-weighted KKT conditions | unique preparation-level sample design for overlapping candidate witness pairs | proved resource-allocation theorem |",
    "roadmap P45 row",
)
anchor = "# 8. Fundamental physical sufficiency: P19"
p45_roadmap = r'''## P45 - shared-preparation graph allocation

For a preparation graph \(G=(V,E)\), each candidate edge \(e=\{i,j\}\) receives the nonuniform P42 budget

\[
2(\varepsilon_i+\varepsilon_j)
+2L_e(r_i+r_j)
\le\Delta_e.
\]

With inverse-square preparation-level sample cost

\[
C=\sum_i\frac{w_{Y,i}}{\varepsilon_i^2}
+\sum_i\frac{w_{Q,i}}{r_i^2},
\]

the design is strictly convex. Under positive feasibility it has a unique global minimizer. The KKT stationarity laws are

\[
\frac{w_{Y,i}}{\varepsilon_i^3}
=
\sum_{e\ni i}\lambda_e,
\qquad
\frac{w_{Q,i}}{r_i^3}
=
\sum_{e\ni i}\lambda_eL_e.
\]

These equations generalize the P43 cube-root rule from one pair to a graph in which a preparation-level sample stream can improve every incident candidate edge.

Direct proof: [Proposition 45](proposition_45_shared_preparation_graph_allocation.md). Implementation: [shared_preparation_graph_allocation.py](../src/consciousness_bridge/shared_preparation_graph_allocation.py). Tests: [test_shared_preparation_graph_allocation.py](../tests/test_shared_preparation_graph_allocation.py).

---

# 8. Fundamental physical sufficiency: P19'''
text = replace_once(text, anchor, p45_roadmap, "roadmap P45 section")
write("docs/theorem_roadmap.md", text)

# Research navigation
path = Path("docs/research_navigation.md")
text = path.read_text(encoding="utf-8")
text = text.replace("from P1 through P44", "from P1 through P45")
text = replace_once(
    text,
    "| P44 | [Pair-adaptive sample allocation](proposition_44_pair_adaptive_sample_allocation.md) | simultaneous finite-family confidence and valid post-data witness selection |",
    "| P44 | [Pair-adaptive sample allocation](proposition_44_pair_adaptive_sample_allocation.md) | simultaneous finite-family confidence and valid post-data witness selection |\n| P45 | [Shared-preparation graph allocation](proposition_45_shared_preparation_graph_allocation.md) | shared preparation-level resource allocation with unique convex optimum and KKT incidence law |",
    "navigation P45 row",
)
write("docs/research_navigation.md", text)

# Equation and citation map
path = Path("docs/equation_and_citation_map.md")
text = path.read_text(encoding="utf-8")
marker = "# 34. Candidate consciousness-theory feature families"
p45_equations = r'''# 34. P45 shared-preparation graph allocation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\Delta_e=d_{Y,e}-L_ed_{Q,e}\) | candidate edge population regularity gap | repository design quantity | [P45](proposition_45_shared_preparation_graph_allocation.md) |
| \(2(\varepsilon_i+\varepsilon_j)+2L_e(r_i+r_j)\le\Delta_e\) | preparation-specific sufficient edge budget | nonuniform extension of the P42 power bound | [P42](proposition_42_quantum_regular_bridge_sample_complexity.md); [P45](proposition_45_shared_preparation_graph_allocation.md) |
| \(C=\sum_iw_{Y,i}/\varepsilon_i^2+\sum_iw_{Q,i}/r_i^2\) | shared preparation-level weighted sampling cost | repository design objective | [P45](proposition_45_shared_preparation_graph_allocation.md) |
| \(w_{Y,i}/\varepsilon_i^3=\sum_{e\ni i}\lambda_e\) | target-side KKT incidence law | proved | convex KKT conditions applied in [P45](proposition_45_shared_preparation_graph_allocation.md) |
| \(w_{Q,i}/r_i^3=\sum_{e\ni i}\lambda_eL_e\) | quantum-side KKT incidence law | proved | convex KKT conditions applied in [P45](proposition_45_shared_preparation_graph_allocation.md) |
| \(C_e^*=S_e^3/\Delta_e^2\) | exact single-edge minimum cost | proved by strict convexity and stationarity | [P45](proposition_45_shared_preparation_graph_allocation.md) |
| ceiling continuous sample counts preserves edge feasibility | conservative integer conversion | monotonicity of \(a/\sqrt n\) | [P45](proposition_45_shared_preparation_graph_allocation.md) |

P45 is a resource-allocation theorem for a declared statistical design. It does not establish physical completeness, quantum incompleteness, or consciousness.

---

# 35. Candidate consciousness-theory feature families'''
text = replace_once(text, marker, p45_equations, "equation map P45")
text = replace_once(text, "# 35. Citation discipline", "# 36. Citation discipline", "equation map citation numbering")
write("docs/equation_and_citation_map.md", text)

# Metadata
path = Path("pyproject.toml")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version = "0.44.0"', 'version = "0.45.0"', "pyproject version")
write("pyproject.toml", text)

path = Path("CITATION.cff")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version: 0.44.0", "version: 0.45.0", "CITATION version")
if "shared-preparation graph allocation" not in text:
    text = replace_once(
        text,
        "finite-family post-selection certification, robust experiment design",
        "finite-family post-selection certification, shared-preparation graph allocation, robust experiment design",
        "CITATION abstract P45",
    )
write("CITATION.cff", text)

# Changelog
path = Path("CHANGELOG.md")
text = path.read_text(encoding="utf-8")
entry = """# Changelog\n\n## 0.45.0 - 2026-09-09\n\n### Added\n- Proposition 45: shared preparation-level graph allocation for overlapping candidate witness pairs.\n- A nonuniform P42 edge budget with preparation-specific target and quantum uncertainty radii.\n- A strictly convex inverse-square sample-cost program with a unique global optimum under positive feasibility.\n- Incidence-weighted KKT cube-root laws showing how active edges jointly determine preparation-level precision.\n- An exact single-edge closed form and conservative integer sample-count conversion.\n- Publication theorem map, main-paper section, roadmap entry, provenance mapping, and release visibility guards.\n\n### Scientific boundary\n- P45 is an experimental resource-allocation theorem for a declared quantum descriptor family and bridge regularity class.\n- It does not establish physical completeness, quantum incompleteness, or consciousness.\n\n"""
text = replace_once(text, "# Changelog\n\n", entry, "changelog P45")
write("CHANGELOG.md", text)

# Main paper guards
path = Path("tests/test_main_page_visual_paper.py")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    '    "p44_pair_adaptive_sample_allocation.svg",',
    '    "p44_pair_adaptive_sample_allocation.svg",\n    "p45_shared_preparation_graph_allocation.svg",',
    "main page P45 figure",
)
text = replace_once(text, "range(1, 45)", "range(1, 46)", "main page P45 proposition range")
write("tests/test_main_page_visual_paper.py", text)

# Release guards
path = Path("tests/test_release_metadata_consistency.py")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version-0.44.0-2563eb", "version-0.45.0-2563eb", "release README version")
text = replace_once(text, 'version = "0\\.44\\.0"', 'version = "0\\.45\\.0"', "release pyproject regex")
text = replace_once(text, "version: 0\\.44\\.0", "version: 0\\.45\\.0", "release citation regex")
text = replace_once(
    text,
    '        "test_pair_adaptive_sample_allocation.py",',
    '        "test_pair_adaptive_sample_allocation.py",\n        "Proposition 45",\n        "p45_shared_preparation_graph_allocation.svg",\n        "shared_preparation_graph_allocation.py",\n        "test_shared_preparation_graph_allocation.py",',
    "release P45 visibility",
)
write("tests/test_release_metadata_consistency.py", text)

# Repository-wide style and LaTeX safety scan
suffixes = {".md", ".py", ".svg", ".bib", ".txt", ".yml", ".yaml", ".toml", ".cff"}
for candidate in Path(".").rglob("*"):
    if candidate.is_file() and candidate.suffix in suffixes and ".git" not in candidate.parts:
        data = candidate.read_text(encoding="utf-8")
        if "\u2013" in data or "\u2014" in data:
            raise RuntimeError(f"forbidden Unicode dash in {candidate}")
        if "\x0c" in data:
            raise RuntimeError(f"form-feed control character in {candidate}")

print("P45 publication integration complete")
