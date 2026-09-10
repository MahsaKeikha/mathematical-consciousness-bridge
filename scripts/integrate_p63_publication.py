from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P63 publication marker: {label}")
    return text.replace(old, new, 1)


def insert_after_line(text: str, token: str, new_line: str, label: str) -> str:
    if new_line in text:
        return text
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if token in line:
            lines.insert(index + 1, new_line)
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    raise RuntimeError(f"missing P63 line marker: {label}")


def integrate_readme() -> None:
    path = "README.md"
    text = read(path)
    if "## Latest proved extension: P63 exact unequal-cost integer calibration" in text:
        return
    text = replace_once(text, "version-0.62.0-2563eb", "version-0.63.0-2563eb", "README version")
    text = replace_once(
        text,
        "The public research record now contains **62 proposition-level results",
        "The public research record now contains **63 proposition-level results",
        "README proposition count",
    )
    p62 = (
        "**P62** removes the equal-cost assumption in the continuous calibration problem: when transition e costs c_e per observation, the unique optimum allocates sample counts in proportion to b_e^(2/3)c_e^(-2/3), while the actual budget share scales as b_e^(2/3)c_e^(1/3)."
    )
    p63 = (
        p62
        + " **P63** makes that unequal-cost design executable with whole measurements when costs and budget are integers: it gives an exact Bellman dynamic program, exact gcd budget compression, an explicit pseudo-polynomial complexity bound, and uses P62 as a rigorous continuous lower bound on the integer optimum."
    )
    text = replace_once(text, p62, p63, "README P62 abstract sentence")
    text = replace_once(
        text,
        "## Latest proved extension: P62 heterogeneous-cost calibration",
        "## Previous proved extension: P62 heterogeneous-cost calibration",
        "README P62 latest header",
    )
    block = r'''
## Latest proved extension: P63 exact unequal-cost integer calibration

![P63 exact heterogeneous-cost integer calibration](docs/figures/p63_exact_heterogeneous_integer_calibration.svg)

P62 tells us the ideal fractional allocation when different transition measurements have different costs. P63 answers the next practical question: **what if measurements must be taken in whole numbers?**

The executable problem is

\[
\boxed{
\min_{k_e\in\{1,2,3,\ldots\}}
\sum_e\frac{b_e}{\sqrt{k_e}}
\quad\text{subject to}\quad
\sum_ec_ek_e\le B.
}
\]

When every measurement costs the same, P61's largest-marginal-gain rule is exactly optimal. When costs differ, that proof no longer applies because one measurement may consume several times as much budget as another. P63 therefore uses an exact dynamic program rather than pretending the equal-cost greedy rule still works.

Define \(F_i(s)\) as the best uncertainty obtainable from the first \(i\) transition edges when exactly \(s\) units of budget have been spent. P63 proves the Bellman recurrence

\[
\boxed{
F_i(s)=
\min_{\substack{k\ge1\\c_i k\le s}}
\left[
F_{i-1}(s-c_i k)+\frac{b_i}{\sqrt{k}}
\right].
}
\]

The exact whole-measurement optimum is then

\[
\boxed{
U_{\rm int}^*(B)=\min_{0\le s\le B}F_m(s).
}
\]

The solver also divides all integer costs by their greatest common divisor before optimization, which compresses the budget axis **without approximation**. The straightforward implementation has a valid pseudo-polynomial worst-case bound \(O(mB'^2)\) after this exact scaling.

P62 remains useful because its continuous optimum is a rigorous lower bound:

\[
\boxed{
U_{\rm cont}^*(B)\le U_{\rm int}^*(B).
}
\]

So every exact P63 run can report how much is lost purely because real experiments require discrete measurements.

The calibration sequence is now

\[
\boxed{
\text{P58 uncertainty}
\to
\text{P59-P61 equal-cost allocation}
\to
\text{P62 unequal-cost continuous allocation}
\to
\text{P63 exact unequal-cost integer allocation}.
}
\]

The scientific boundary remains strict: P63 optimizes a declared experimental uncertainty surrogate. It does not prove that the full robust-routing design problem has the same structure and makes no claim that any scheduling quantity is consciousness or that quantum mechanics is incomplete.

[Read Proposition 63](docs/proposition_63_exact_heterogeneous_integer_calibration.md). The [P63 visual](docs/figures/p63_exact_heterogeneous_integer_calibration.svg), [implementation](src/consciousness_bridge/exact_heterogeneous_integer_calibration.py), and [tests](tests/test_exact_heterogeneous_integer_calibration.py) expose the proof-to-code path.

---

'''
    text = replace_once(text, "# Scientific status discipline", block + "# Scientific status discipline", "README P63 block")
    write(path, text)


def integrate_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    if "[P63](proposition_63_exact_heterogeneous_integer_calibration.md)" in text:
        return
    text = insert_after_line(
        text,
        "p62_heterogeneous_cost_transition_calibration.svg",
        "![P63 exact heterogeneous-cost integer calibration](figures/p63_exact_heterogeneous_integer_calibration.svg)",
        "roadmap P63 figure",
    )
    text = insert_after_line(
        text,
        "| [P62](proposition_62_heterogeneous_cost_transition_calibration.md)",
        "| [P63](proposition_63_exact_heterogeneous_integer_calibration.md) | exact-spend Bellman recursion with gcd cost compression | globally exact whole-measurement allocation under positive integer unequal costs, with P62 lower bound | proved pseudo-polynomial exact discrete theorem |",
        "roadmap P63 row",
    )
    write(path, text)


def integrate_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    if "| P63 | [Exact heterogeneous-cost integer calibration]" in text:
        return
    text = text.replace("P1 through P62", "P1 through P63")
    text = insert_after_line(
        text,
        "| P62 | [Heterogeneous-cost transition-calibration allocation]",
        "| P63 | [Exact heterogeneous-cost integer calibration](proposition_63_exact_heterogeneous_integer_calibration.md) | exact Bellman solver for whole transition measurements with unequal positive integer costs, gcd compression, and continuous lower-bound certificate |",
        "navigation P63 row",
    )
    write(path, text)


def integrate_equations() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 52. P63 exact heterogeneous-cost integer calibration" in text:
        return
    addition = r'''

---

# 52. P63 exact heterogeneous-cost integer calibration

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\min\sum_e b_e/\sqrt{k_e}\) subject to \(\sum_ec_ek_e\le B\), integer \(k_e\ge1\) | executable unequal-cost calibration problem | repository definition | [P63](proposition_63_exact_heterogeneous_integer_calibration.md) |
| \(F_i(s)=\min_k[F_{i-1}(s-c_i k)+b_i/\sqrt{k}]\) | exact-spend Bellman recurrence | proved exact by induction over processed edges | [P63](proposition_63_exact_heterogeneous_integer_calibration.md) |
| \(U_{\rm int}^*(B)=\min_{s\le B}F_m(s)\) | exact hard-budget integer optimum | proved Bellman consequence | [P63](proposition_63_exact_heterogeneous_integer_calibration.md) |
| \(g=\gcd(c_1,\ldots,c_m)\) and \(B'=\lfloor B/g\rfloor\) | exact budget-axis compression | proved lattice equivalence | [P63](proposition_63_exact_heterogeneous_integer_calibration.md) |
| \(O(mB'^2)\) | straightforward pseudo-polynomial worst-case time bound | proved counting bound | [P63](proposition_63_exact_heterogeneous_integer_calibration.md) |
| \(U_{\rm cont}^*(B)\le U_{\rm int}^*(B)\) | P62 continuous relaxation lower bound | proved by feasible-set inclusion | [P63](proposition_63_exact_heterogeneous_integer_calibration.md) |

P63 does not claim a greedy solution or a complexity-hardness classification for the binary-encoded heterogeneous-cost integer problem.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    path = "pyproject.toml"
    text = read(path)
    text = replace_once(text, 'version = "0.62.0"', 'version = "0.63.0"', "pyproject version")
    text = replace_once(
        text,
        "heterogeneous-cost transition-calibration allocation, robust experiment design",
        "heterogeneous-cost transition-calibration allocation, exact heterogeneous-cost integer calibration, robust experiment design",
        "pyproject description",
    )
    write(path, text)

    path = "CITATION.cff"
    text = read(path)
    text = replace_once(text, "version: 0.62.0", "version: 0.63.0", "citation version")
    text = replace_once(
        text,
        "heterogeneous-cost transition-calibration allocation, robust experiment design",
        "heterogeneous-cost transition-calibration allocation, exact heterogeneous-cost integer calibration, robust experiment design",
        "citation abstract",
    )
    write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.63.0 - 2026-09-10"):
        entry = """# 0.63.0 - 2026-09-10

- Add P63 exact heterogeneous-cost integer transition calibration.
- Prove the exact Bellman recurrence for whole measurement counts under unequal positive integer costs.
- Add exact gcd budget compression and an explicit pseudo-polynomial complexity bound.
- Use P62 as a rigorous continuous lower bound and report instance-specific integrality gaps.
- Add implementation, brute-force regression tests, theorem visual, public navigation, provenance, and release integration.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.62.0-2563eb", "version-0.63.0-2563eb")
    text = text.replace('version = "0\\.62\\.0"', 'version = "0\\.63\\.0"')
    text = text.replace("version: 0\\.62\\.0", "version: 0\\.63\\.0")
    marker = (
        '        "Proposition 62",\n'
        '        "p62_heterogeneous_cost_transition_calibration.svg",\n'
        '        "heterogeneous_cost_transition_calibration.py",\n'
        '        "test_heterogeneous_cost_transition_calibration.py",\n'
    )
    replacement = marker + (
        '        "Proposition 63",\n'
        '        "p63_exact_heterogeneous_integer_calibration.svg",\n'
        '        "exact_heterogeneous_integer_calibration.py",\n'
        '        "test_exact_heterogeneous_integer_calibration.py",\n'
    )
    text = replace_once(text, marker, replacement, "release P63 guards")
    write(path, text)

    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    if '"p63_exact_heterogeneous_integer_calibration.svg"' not in text:
        text = replace_once(
            text,
            '    "p62_heterogeneous_cost_transition_calibration.svg",',
            '    "p62_heterogeneous_cost_transition_calibration.svg",\n    "p63_exact_heterogeneous_integer_calibration.svg",',
            "main-page P63 figure",
        )
    text = text.replace("for index in range(1, 63):", "for index in range(1, 64):")
    write(path, text)

    write(
        "tests/test_exact_heterogeneous_integer_calibration_publication.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef test_p63_is_visible_on_main_page():\n    text = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "P63 exact unequal-cost integer calibration",\n        "p63_exact_heterogeneous_integer_calibration.svg",\n        "exact_heterogeneous_integer_calibration.py",\n        "test_exact_heterogeneous_integer_calibration.py",\n    ):\n        assert token in text\n\n\ndef test_p63_is_in_public_research_maps():\n    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")\n    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")\n    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")\n    assert "[P63](proposition_63_exact_heterogeneous_integer_calibration.md)" in roadmap\n    assert "| P63 | [Exact heterogeneous-cost integer calibration]" in navigation\n    assert "# 52. P63 exact heterogeneous-cost integer calibration" in equations\n''',
    )


def main() -> None:
    integrate_readme()
    integrate_roadmap()
    integrate_navigation()
    integrate_equations()
    integrate_metadata()
    integrate_tests()


if __name__ == "__main__":
    main()
