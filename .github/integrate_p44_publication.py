from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one marker, found {count}")
    return text.replace(old, new, 1)


def write(path: str, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8")


# README publication integration.
path = Path("README.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "version-0.43.0-2563eb",
    "version-0.44.0-2563eb",
    "README badge",
)
text = replace_once(
    text,
    "**P43** removes the arbitrary P42 quantum-versus-target uncertainty split and proves the unique cube-root allocation that minimizes a declared weighted sampling cost, including an explicit integer-rounding overhead bound.",
    "**P43** removes the arbitrary P42 quantum-versus-target uncertainty split and proves the unique cube-root allocation that minimizes a declared weighted sampling cost, including an explicit integer-rounding overhead bound. **P44** extends the finite-sample design from one preselected preparation pair to a finite predeclared family, proves simultaneous family coverage, and shows that any measurable data-dependent witness selector remains valid on that shared confidence event.",
    "README abstract P44",
)
text = replace_once(
    text,
    "**43 proposition-level results, 58 equation-driven quantitative figures",
    "**44 proposition-level results, 58 equation-driven quantitative figures",
    "README record count",
)
text = text.replace("P1 through P43", "P1 through P44")
text = replace_once(
    text,
    "| optimal quantum-target allocation | [Proposition 43](docs/proposition_43_optimal_quantum_target_allocation.md) | closed-form cube-root allocation minimizing weighted P42 sampling cost with integer-rounding control |",
    "| optimal quantum-target allocation | [Proposition 43](docs/proposition_43_optimal_quantum_target_allocation.md) | closed-form cube-root allocation minimizing weighted P42 sampling cost with integer-rounding control |\n| pair-adaptive finite-family certification | [Proposition 44](docs/proposition_44_pair_adaptive_sample_allocation.md) | simultaneous family confidence and valid post-data witness selection for a finite predeclared candidate set |",
    "README navigation P44",
)
text = replace_once(
    text,
    "| implementation of P41 | [trace_ball_quantum_envelope.py](src/consciousness_bridge/trace_ball_quantum_envelope.py) | trace-ball quantum envelope and global Lipschitz obstruction certificate |",
    "| implementation of P41 | [trace_ball_quantum_envelope.py](src/consciousness_bridge/trace_ball_quantum_envelope.py) | trace-ball quantum envelope and global Lipschitz obstruction certificate |\n| implementation of P42 | [quantum_regular_bridge_sample_complexity.py](src/consciousness_bridge/quantum_regular_bridge_sample_complexity.py) | explicit fixed-IC finite-sample regularity certificate |\n| implementation of P43 | [optimal_quantum_target_allocation.py](src/consciousness_bridge/optimal_quantum_target_allocation.py) | exact minimum-cost quantum-target uncertainty allocation |\n| implementation of P44 | [pair_adaptive_sample_allocation.py](src/consciousness_bridge/pair_adaptive_sample_allocation.py) | finite-family confidence spending and post-selection certificate |",
    "README implementation P44",
)
text = replace_once(
    text,
    "| **11.19 P43 optimal quantum-target allocation** | How should the P42 uncertainty budget be divided to minimize declared weighted sampling cost? |",
    "| **11.19 P43 optimal quantum-target allocation** | How should the P42 uncertainty budget be divided to minimize declared weighted sampling cost? |\n| **11.20 P44 pair-adaptive finite-family certification** | Can a witness pair be selected after seeing the data without losing family-level validity? |",
    "README paper map P44",
)
text = replace_once(
    text,
    "| proposition-level results | **43** |",
    "| proposition-level results | **44** |",
    "README table result count",
)
text = replace_once(
    text,
    "| research-software version | **0.43.0** |",
    "| research-software version | **0.44.0** |",
    "README table version",
)
p43_tail = "[Read Proposition 43](docs/proposition_43_optimal_quantum_target_allocation.md). The [P43 theorem map](docs/figures/p43_optimal_quantum_target_allocation.svg), [implementation](src/consciousness_bridge/optimal_quantum_target_allocation.py), and [tests](tests/test_optimal_quantum_target_allocation.py) expose the complete proof-to-code path.\n\n---\n\n# 14. Observer-to-bridge handoff"
p44_section = r'''[Read Proposition 43](docs/proposition_43_optimal_quantum_target_allocation.md). The [P43 theorem map](docs/figures/p43_optimal_quantum_target_allocation.svg), [implementation](src/consciousness_bridge/optimal_quantum_target_allocation.py), and [tests](tests/test_optimal_quantum_target_allocation.py) expose the complete proof-to-code path.

## 13.17 P44 - pair-adaptive finite-family certification

![P44 finite-family post-selection certificate](docs/figures/p44_pair_adaptive_sample_allocation.svg)

P42 and P43 design a regularity test for one preparation pair selected before data collection. P44 asks a different statistical question: can the final witness pair be selected after the data are observed without invalidating the stated confidence level?

Let a finite predeclared candidate family be indexed by

\[
\mathcal J=\{1,\ldots,J\},
\]

with true population regularity margins

\[
\boxed{M_j=d_{Y,j}-L_jd_{Q,j}.}
\]

Suppose candidate \(j\) has a random lower confidence margin \(\underline M_j\), with quantum and target failure allocations \(\alpha_{Q,j}\) and \(\alpha_{Y,j}\). If

\[
\sum_j\alpha_{Q,j}\le\alpha_Q,
\qquad
\sum_j\alpha_{Y,j}\le\alpha_Y,
\]

then the union bound gives the simultaneous family event

\[
\boxed{
\Pr\left(\underline M_j\le M_j\ \forall j\in\mathcal J\right)
\ge
1-\alpha_Q-\alpha_Y.
}
\]

No independence assumption between candidate analyses is required. This matters because candidate pairs can share preparations and can therefore share data.

Let \(\widehat j=\mathcal S(\mathcal D)\) be any measurable selector taking values in the predeclared family. On the same simultaneous event,

\[
\boxed{\underline M_{\widehat j}\le M_{\widehat j}.}
\]

Therefore

\[
\boxed{
\underline M_{\widehat j}>0
\Longrightarrow
M_{\widehat j}>0
}
\]

with confidence at least

\[
\boxed{\max\{0,1-\alpha_Q-\alpha_Y\}.}
\]

A useful selector is

\[
\widehat j\in\arg\max_j\underline M_j,
\]

but the theorem does not require that particular rule. Its validity comes from simultaneous coverage of the complete candidate family, not from a special property of the maximizer.

P44 also permits predeclared weighted confidence spending. Positive weights can allocate more error budget to scientifically prioritized or more efficient candidates while preserving the family theorem. Equal weights recover Bonferroni spending. If the weights themselves are chosen from the evidence used for certification, a new adaptive-design theorem is required.

The scientific boundary is strict:

\[
\boxed{
\text{valid selected regularity witness}
\neq
\text{physical completeness}
\neq
\text{quantum incompleteness}
\neq
\text{consciousness theorem}.
}
\]

P44 certifies a finite family of declared descriptor and bridge-regularity tests. It does not show that a richer quantum descriptor cannot work, and it does not identify the target with consciousness.

[Read Proposition 44](docs/proposition_44_pair_adaptive_sample_allocation.md). The [P44 theorem map](docs/figures/p44_pair_adaptive_sample_allocation.svg), [implementation](src/consciousness_bridge/pair_adaptive_sample_allocation.py), and [tests](tests/test_pair_adaptive_sample_allocation.py) expose the complete proof-to-code path.

---

# 14. Observer-to-bridge handoff'''
text = replace_once(text, p43_tail, p44_section, "README P44 section")
write("README.md", text)

# Theorem roadmap.
path = Path("docs/theorem_roadmap.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "![P43 optimal quantum-target allocation](figures/p43_optimal_quantum_target_allocation.svg)\n",
    "![P43 optimal quantum-target allocation](figures/p43_optimal_quantum_target_allocation.svg)\n\n![P44 finite-family post-selection certificate](figures/p44_pair_adaptive_sample_allocation.svg)\n",
    "roadmap figure",
)
text = replace_once(
    text,
    "| [P43](proposition_43_optimal_quantum_target_allocation.md) | strict convexity and closed-form weighted allocation | unique minimum-cost split of the P42 quantum and target uncertainty budget | proved resource-allocation theorem |",
    "| [P43](proposition_43_optimal_quantum_target_allocation.md) | strict convexity and closed-form weighted allocation | unique minimum-cost split of the P42 quantum and target uncertainty budget | proved resource-allocation theorem |\n| [P44](proposition_44_pair_adaptive_sample_allocation.md) | finite-family union bound and simultaneous lower-margin coverage | valid data-dependent witness selection among predeclared candidate pairs | proved post-selection theorem |",
    "roadmap P44 row",
)
p43_roadmap_tail = "Direct proof: [Proposition 43](proposition_43_optimal_quantum_target_allocation.md). Implementation: [optimal_quantum_target_allocation.py](../src/consciousness_bridge/optimal_quantum_target_allocation.py). Tests: [test_optimal_quantum_target_allocation.py](../tests/test_optimal_quantum_target_allocation.py).\n\n---\n\n# 8. Fundamental physical sufficiency: P19"
p44_roadmap = r'''Direct proof: [Proposition 43](proposition_43_optimal_quantum_target_allocation.md). Implementation: [optimal_quantum_target_allocation.py](../src/consciousness_bridge/optimal_quantum_target_allocation.py). Tests: [test_optimal_quantum_target_allocation.py](../tests/test_optimal_quantum_target_allocation.py).

---

## P44 - finite-family post-selection certification

Let \(\underline M_j\) be a lower confidence margin for each candidate \(j\) in a finite predeclared family. If the candidate-specific failure allocations satisfy

\[
\sum_j\alpha_{Q,j}\le\alpha_Q,
\qquad
\sum_j\alpha_{Y,j}\le\alpha_Y,
\]

then

\[
\boxed{
\Pr(\underline M_j\le M_j\ \forall j)
\ge1-\alpha_Q-\alpha_Y.
}
\]

Consequently, for any measurable data-dependent selector \(\widehat j\),

\[
\boxed{
\underline M_{\widehat j}>0
\Longrightarrow
M_{\widehat j}>0
}
\]

on that same simultaneous event. Shared preparations and dependent candidate analyses are allowed; independence is not required for the union-bound guarantee.

Direct proof: [Proposition 44](proposition_44_pair_adaptive_sample_allocation.md). Implementation: [pair_adaptive_sample_allocation.py](../src/consciousness_bridge/pair_adaptive_sample_allocation.py). Tests: [test_pair_adaptive_sample_allocation.py](../tests/test_pair_adaptive_sample_allocation.py).

---

# 8. Fundamental physical sufficiency: P19'''
text = replace_once(text, p43_roadmap_tail, p44_roadmap, "roadmap P44 section")
write("docs/theorem_roadmap.md", text)

# Research navigation.
path = Path("docs/research_navigation.md")
text = path.read_text(encoding="utf-8")
text = text.replace("from P1 through P43", "from P1 through P44")
text = replace_once(
    text,
    "| P43 | [Optimal quantum-target allocation](proposition_43_optimal_quantum_target_allocation.md) | cube-root minimum-cost allocation of the P42 uncertainty budget |",
    "| P43 | [Optimal quantum-target allocation](proposition_43_optimal_quantum_target_allocation.md) | cube-root minimum-cost allocation of the P42 uncertainty budget |\n| P44 | [Pair-adaptive sample allocation](proposition_44_pair_adaptive_sample_allocation.md) | simultaneous finite-family confidence and valid post-data witness selection |",
    "navigation P44 row",
)
write("docs/research_navigation.md", text)

# Equation and citation map.
path = Path("docs/equation_and_citation_map.md")
text = path.read_text(encoding="utf-8")
marker = "# 33. Candidate consciousness-theory feature families"
p44_equations = r'''# 33. P44 pair-adaptive finite-family certification

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(M_j=d_{Y,j}-L_jd_{Q,j}\) | candidate population regularity margin | repository design quantity | [P44](proposition_44_pair_adaptive_sample_allocation.md) |
| \(\sum_j\alpha_{Q,j}\le\alpha_Q,\ \sum_j\alpha_{Y,j}\le\alpha_Y\) | predeclared family failure-budget constraint | declared statistical design condition | [P44](proposition_44_pair_adaptive_sample_allocation.md) |
| \(\Pr(\underline M_j\le M_j\ \forall j)\ge1-\alpha_Q-\alpha_Y\) | simultaneous finite-family lower-margin coverage | union bound | standard probability; [P44](proposition_44_pair_adaptive_sample_allocation.md) |
| \(\underline M_{\widehat j}>0\Rightarrow M_{\widehat j}>0\) | post-selection validity for any measurable selector in the predeclared family | proved | [P44](proposition_44_pair_adaptive_sample_allocation.md) |
| weighted alpha spending | allocates family confidence before viewing certification data | proved to preserve family budget | [P44](proposition_44_pair_adaptive_sample_allocation.md) |

P44 is a finite-family statistical theorem. It does not establish physical completeness, quantum incompleteness, or consciousness.

---

# 34. Candidate consciousness-theory feature families'''
text = replace_once(text, marker, p44_equations, "equation map P44")
text = replace_once(text, "# 34. Citation discipline", "# 35. Citation discipline", "equation map numbering")
write("docs/equation_and_citation_map.md", text)

# Release metadata.
path = Path("pyproject.toml")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version = "0.43.0"', 'version = "0.44.0"', "pyproject version")
text = replace_once(
    text,
    "optimal quantum-target resource allocation, robust experiment design",
    "optimal quantum-target resource allocation, finite-family post-selection certification, robust experiment design",
    "pyproject description",
) if "optimal quantum-target resource allocation, robust experiment design" in text else text
write("pyproject.toml", text)

path = Path("CITATION.cff")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version: 0.43.0", "version: 0.44.0", "CITATION version")
text = replace_once(
    text,
    "optimal quantum-target resource allocation, robust experiment design",
    "optimal quantum-target resource allocation, finite-family post-selection certification, robust experiment design",
    "CITATION abstract",
)
write("CITATION.cff", text)

# Changelog.
path = Path("CHANGELOG.md")
text = path.read_text(encoding="utf-8")
entry = """# Changelog\n\n## 0.44.0 - 2026-09-09\n\n### Added\n- Proposition 44: finite-family simultaneous-confidence and post-selection certification for candidate preparation pairs.\n- Validity for arbitrary measurable data-dependent witness selection inside a predeclared candidate family.\n- Weighted and equal confidence spending with explicit family failure-budget accounting.\n- Pair-specific connection to the P42 sample-complexity and P43 cost-allocation results.\n- Publication theorem map, main-paper section, roadmap integration, provenance entries, and visibility guards.\n\n### Scientific boundary\n- P44 certifies selection among declared finite-family regularity tests.\n- It does not establish physical completeness, quantum incompleteness, or consciousness.\n\n"""
text = replace_once(text, "# Changelog\n\n", entry, "changelog P44")
write("CHANGELOG.md", text)

# Main-page visibility guard.
path = Path("tests/test_main_page_visual_paper.py")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    '    "p43_optimal_quantum_target_allocation.svg",',
    '    "p43_optimal_quantum_target_allocation.svg",\n    "p44_pair_adaptive_sample_allocation.svg",',
    "main page P44 figure guard",
)
text = replace_once(text, "range(1, 44)", "range(1, 45)", "main page P44 proposition guard")
write("tests/test_main_page_visual_paper.py", text)

# Permanent publication metadata guard.
path = Path("tests/test_release_metadata_consistency.py")
text = path.read_text(encoding="utf-8")
# Existing test is intentionally generic in most releases. No structural rewrite is needed.
write("tests/test_release_metadata_consistency.py", text)

# Final style safety check before CI.
for candidate in [Path("README.md"), *Path("docs").rglob("*.md"), *Path("src").rglob("*.py"), *Path("tests").rglob("*.py")]:
    data = candidate.read_text(encoding="utf-8")
    if "\u2013" in data or "\u2014" in data:
        raise RuntimeError(f"forbidden Unicode dash in {candidate}")

print("P44 publication integration complete")
