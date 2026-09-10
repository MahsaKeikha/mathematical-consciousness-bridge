from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing P62 publication marker: {label}")
    return text.replace(old, new, 1)


def insert_after_line(text: str, token: str, new_line: str, label: str) -> str:
    if new_line in text:
        return text
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if token in line:
            lines.insert(index + 1, new_line)
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    raise RuntimeError(f"missing P62 line marker: {label}")


def integrate_readme() -> None:
    path = "README.md"
    text = read(path)
    if "## Latest proved extension: P62 heterogeneous-cost calibration" in text:
        return

    text = replace_once(text, "version-0.61.0-2563eb", "version-0.62.0-2563eb", "README version")
    text = replace_once(
        text,
        "The public research record now contains **61 proposition-level results",
        "The public research record now contains **62 proposition-level results",
        "README proposition count",
    )
    p61 = (
        "**P61** closes the remaining discrete optimization gap for the same separable surrogate: starting from one measurement per edge, repeatedly assigning the next whole measurement to the edge with the largest current marginal uncertainty reduction is globally optimal because those marginal gains decrease strictly with repeated sampling."
    )
    p62 = (
        p61
        + " **P62** removes the equal-cost assumption in the continuous calibration problem: when transition e costs c_e per observation, the unique optimum allocates sample counts in proportion to b_e^(2/3)c_e^(-2/3), while the actual budget share scales as b_e^(2/3)c_e^(1/3)."
    )
    text = replace_once(text, p61, p62, "README P61 abstract sentence")

    old_header = "## Latest proved extension: P61 exact integer calibration"
    new_header = "## Previous proved extension: P61 exact integer calibration"
    text = replace_once(text, old_header, new_header, "README P61 latest header")

    block = r'''
## Latest proved extension: P62 heterogeneous-cost calibration

![P62 heterogeneous-cost transition-calibration allocation](docs/figures/p62_heterogeneous_cost_transition_calibration.svg)

P59-P61 answer how to allocate transition measurements when every observation consumes the same unit of experimental effort. Real experiments are often less uniform. Some transitions take longer to stabilize, require different equipment, consume more subject time, or simply cost more to measure.

P62 asks the practical version of the allocation problem: **how should we spend a fixed calibration budget when different transition measurements have different costs?**

For each edge \(e\), let \(b_e\) combine its uncertainty coefficient and scientific sensitivity, and let \(c_e>0\) be the cost of one observation. P62 solves

\[
\boxed{
\min_{n_e>0}\sum_e\frac{b_e}{\sqrt{n_e}}
\quad\text{subject to}\quad
\sum_ec_en_e=B.
}
\]

Define

\[
\boxed{
T=\sum_e b_e^{2/3}c_e^{1/3}.
}
\]

Then the unique optimum is

\[
\boxed{
n_e^*=\frac{B}{T}b_e^{2/3}c_e^{-2/3},
\qquad
U^*(B)=\frac{T^{3/2}}{\sqrt B}.
}
\]

In plain language, **important or noisy transitions deserve more measurements, while expensive transitions deserve fewer measurements**. But sample count and money spent are not the same thing. The optimal budget share is

\[
\boxed{
c_en_e^*\propto b_e^{2/3}c_e^{1/3}.
}
\]

So a very expensive transition can receive fewer observations and still consume a larger fraction of the total budget.

This extends the calibration chain to a more realistic experimental setting:

\[
\boxed{
\text{P58 uncertainty}
\to
\text{P59 equal-cost continuous allocation}
\to
\text{P60-P61 whole-measurement allocation}
\to
\text{P62 heterogeneous-cost continuous allocation}.
}
\]

The scientific boundary remains explicit. P62 is an experimental resource-allocation theorem. It does not solve the heterogeneous-cost integer problem, does not prove the sensitivity weights are uniquely correct, and does not make an experiential or quantum-ontological claim.

[Read Proposition 62](docs/proposition_62_heterogeneous_cost_transition_calibration.md). The [P62 visual](docs/figures/p62_heterogeneous_cost_transition_calibration.svg), [implementation](src/consciousness_bridge/heterogeneous_cost_transition_calibration.py), and [tests](tests/test_heterogeneous_cost_transition_calibration.py) expose the proof-to-code path.

---

'''
    marker = "# Scientific status discipline"
    text = replace_once(text, marker, block + marker, "README P62 latest block")
    write(path, text)


def integrate_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    if "[P62](proposition_62_heterogeneous_cost_transition_calibration.md)" in text:
        return
    text = insert_after_line(
        text,
        "p61_exact_integer_transition_calibration.svg",
        "![P62 heterogeneous-cost transition-calibration allocation](figures/p62_heterogeneous_cost_transition_calibration.svg)",
        "roadmap P62 figure",
    )
    text = insert_after_line(
        text,
        "| [P61](proposition_61_exact_integer_transition_calibration.md)",
        "| [P62](proposition_62_heterogeneous_cost_transition_calibration.md) | strict convexity and KKT allocation under edge-specific observation costs | exact heterogeneous-cost continuous sample allocation, budget shares, and target-budget formula | proved continuous resource-allocation theorem |",
        "roadmap P62 row",
    )
    write(path, text)


def integrate_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    if "| P62 | [Heterogeneous-cost transition-calibration allocation]" in text:
        return
    text = text.replace("P1 through P61", "P1 through P62")
    text = insert_after_line(
        text,
        "| P61 | [Exact integer transition-calibration allocation]",
        "| P62 | [Heterogeneous-cost transition-calibration allocation](proposition_62_heterogeneous_cost_transition_calibration.md) | unique continuous calibration optimum when transition observations have different per-measurement costs |",
        "navigation P62 row",
    )
    write(path, text)


def integrate_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 51. P62 heterogeneous-cost transition-calibration allocation" in text:
        return
    addition = r'''

---

# 51. P62 heterogeneous-cost transition-calibration allocation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\sum_ec_en_e=B\) | heterogeneous calibration-cost constraint | repository design assumption | [P62](proposition_62_heterogeneous_cost_transition_calibration.md) |
| \(T=\sum_e b_e^{2/3}c_e^{1/3}\) | normalization coupling scientific importance and per-observation cost | repository definition | [P62](proposition_62_heterogeneous_cost_transition_calibration.md) |
| \(n_e^*=(B/T)b_e^{2/3}c_e^{-2/3}\) | unique continuous sample-count optimum | proved by strict convexity and KKT conditions | [P62](proposition_62_heterogeneous_cost_transition_calibration.md) |
| \(c_en_e^*=B b_e^{2/3}c_e^{1/3}/T\) | exact optimal budget share | algebraic consequence of P62 optimum | [P62](proposition_62_heterogeneous_cost_transition_calibration.md) |
| \(U^*(B)=T^{3/2}/\sqrt B\) | exact minimum declared surrogate uncertainty | proved closed-form optimum | [P62](proposition_62_heterogeneous_cost_transition_calibration.md) |
| \(B\ge T^3/\varepsilon^2\) | exact continuous budget threshold for target uncertainty | proved inversion of optimum | [P62](proposition_62_heterogeneous_cost_transition_calibration.md) |

P62 solves the continuous heterogeneous-cost version of the declared P59 surrogate. The heterogeneous-cost integer problem remains separate.
'''
    write(path, text.rstrip() + addition + "\n")


def integrate_metadata() -> None:
    path = "pyproject.toml"
    text = read(path)
    text = replace_once(text, 'version = "0.61.0"', 'version = "0.62.0"', "pyproject version")
    text = replace_once(
        text,
        "exact integer transition-calibration allocation, robust experiment design",
        "exact integer transition-calibration allocation, heterogeneous-cost transition-calibration allocation, robust experiment design",
        "pyproject description",
    )
    write(path, text)

    path = "CITATION.cff"
    text = read(path)
    text = replace_once(text, "version: 0.61.0", "version: 0.62.0", "citation version")
    text = replace_once(
        text,
        "exact integer transition-calibration allocation, robust experiment design",
        "exact integer transition-calibration allocation, heterogeneous-cost transition-calibration allocation, robust experiment design",
        "citation abstract",
    )
    write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.62.0 - 2026-09-10"):
        entry = """# 0.62.0 - 2026-09-10

- Add P62 heterogeneous-cost transition-calibration allocation.
- Prove the unique continuous optimum when calibration observations have edge-specific positive costs.
- Distinguish optimal sample-count scaling from optimal budget-share scaling.
- Recover P59 exactly as the equal-cost special case and derive the exact target-budget threshold.
- Add implementation, tests, theorem visual, public navigation, provenance, and release integration.

"""
        write(path, entry + text)


def integrate_tests() -> None:
    path = "tests/test_release_metadata_consistency.py"
    text = read(path)
    text = text.replace("version-0.61.0-2563eb", "version-0.62.0-2563eb")
    text = text.replace('version = "0\\.61\\.0"', 'version = "0\\.62\\.0"')
    text = text.replace("version: 0\\.61\\.0", "version: 0\\.62\\.0")
    marker = (
        '        "Proposition 61",\n'
        '        "p61_exact_integer_transition_calibration.svg",\n'
        '        "exact_integer_transition_calibration.py",\n'
        '        "test_exact_integer_transition_calibration.py",\n'
    )
    replacement = marker + (
        '        "Proposition 62",\n'
        '        "p62_heterogeneous_cost_transition_calibration.svg",\n'
        '        "heterogeneous_cost_transition_calibration.py",\n'
        '        "test_heterogeneous_cost_transition_calibration.py",\n'
    )
    text = replace_once(text, marker, replacement, "release P62 guards")
    write(path, text)

    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    if '"p62_heterogeneous_cost_transition_calibration.svg"' not in text:
        text = replace_once(
            text,
            '    "p61_exact_integer_transition_calibration.svg",',
            '    "p61_exact_integer_transition_calibration.svg",\n    "p62_heterogeneous_cost_transition_calibration.svg",',
            "main page P62 figure guard",
        )
    text = text.replace("for index in range(1, 62):", "for index in range(1, 63):")
    write(path, text)

    write(
        "tests/test_heterogeneous_cost_transition_calibration_publication.py",
        '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\n\ndef test_p62_is_visible_on_main_page():\n    text = (ROOT / "README.md").read_text(encoding="utf-8")\n    for token in (\n        "P62 heterogeneous-cost calibration",\n        "p62_heterogeneous_cost_transition_calibration.svg",\n        "heterogeneous_cost_transition_calibration.py",\n        "test_heterogeneous_cost_transition_calibration.py",\n    ):\n        assert token in text\n\n\ndef test_p62_is_in_public_research_maps():\n    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")\n    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")\n    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")\n    assert "[P62](proposition_62_heterogeneous_cost_transition_calibration.md)" in roadmap\n    assert "| P62 | [Heterogeneous-cost transition-calibration allocation]" in navigation\n    assert "# 51. P62 heterogeneous-cost transition-calibration allocation" in equations\n''',
    )


def main() -> None:
    integrate_readme()
    integrate_roadmap()
    integrate_navigation()
    integrate_equation_map()
    integrate_metadata()
    integrate_tests()


if __name__ == "__main__":
    main()
