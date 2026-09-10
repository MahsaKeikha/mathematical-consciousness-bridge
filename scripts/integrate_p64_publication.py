from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text, old, new, label):
    if old not in text:
        raise RuntimeError(f"missing P64 marker: {label}")
    return text.replace(old, new, 1)


def insert_after_line(text, token, line, label):
    if line in text:
        return text
    lines = text.splitlines()
    for i, current in enumerate(lines):
        if token in current:
            lines.insert(i + 1, line)
            return "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    raise RuntimeError(f"missing P64 line marker: {label}")


def main():
    path = "README.md"
    text = read(path)
    if "## Latest proved extension: P64 fast certified integer approximation" not in text:
        text = replace_once(text, "version-0.63.0-2563eb", "version-0.64.0-2563eb", "README version")
        text = replace_once(text, "The public research record now contains **63 proposition-level results", "The public research record now contains **64 proposition-level results", "count")
        p63 = "**P63** makes that unequal-cost design executable with whole measurements when costs and budget are integers: it gives an exact Bellman dynamic program, exact gcd budget compression, an explicit pseudo-polynomial complexity bound, and uses P62 as a rigorous continuous lower bound on the integer optimum."
        text = replace_once(text, p63, p63 + " **P64** adds a scalable certified alternative: when every P62 continuous allocation is at least one measurement, simply flooring those allocations is feasible and comes with an explicit instance-specific multiplicative guarantee relative to the exact P63 optimum.", "abstract")
        text = replace_once(text, "## Latest proved extension: P63 exact unequal-cost integer calibration", "## Previous proved extension: P63 exact unequal-cost integer calibration", "previous header")
        block = r'''## Latest proved extension: P64 fast certified integer approximation

![P64 fast certified heterogeneous integer approximation](docs/figures/p64_fast_heterogeneous_integer_approximation.svg)

P63 gives the exact whole-measurement answer when transition costs differ, but its dynamic program grows with the numeric budget. P64 asks a practical scalability question: **when can we get a fast integer design with a mathematical guarantee, without solving the full dynamic program?**

Start from the exact P62 continuous allocation \(n_e^*\). If every edge already receives at least one continuous measurement, define

\[
\boxed{k_e=\lfloor n_e^*\rfloor.}
\]

This is automatically budget-feasible. Define

\[
\boxed{r_{\min}=\min_e\frac{\lfloor n_e^*\rfloor}{n_e^*}.}
\]

P64 proves

\[
\boxed{U(k)\le\frac{1}{\sqrt{r_{\min}}}U_{\rm int}^*(B).}
\]

So the fast design comes with a directly computable certificate relative to the unknown exact P63 optimum. If every continuous allocation is at least \(\nu>1\), then the simpler uniform guarantee is

\[
\boxed{U(k)\le\sqrt{\frac{\nu}{\nu-1}}\,U_{\rm int}^*(B).}
\]

As the budget grows, the continuous counts grow and the factor approaches 1. The construction is linear in the number of calibrated edges after the P62 closed form. If any continuous count is below one, P64 refuses to claim the certificate and P63 remains the exact fallback.

[Read Proposition 64](docs/proposition_64_fast_heterogeneous_integer_approximation.md). The [visual](docs/figures/p64_fast_heterogeneous_integer_approximation.svg), [implementation](src/consciousness_bridge/fast_heterogeneous_integer_approximation.py), and [tests](tests/test_fast_heterogeneous_integer_approximation.py) expose the proof-to-code path.

---

'''
        text = replace_once(text, "# Scientific status discipline", block + "# Scientific status discipline", "latest block")
        write(path, text)

    path = "docs/theorem_roadmap.md"
    text = read(path)
    if "[P64](proposition_64_fast_heterogeneous_integer_approximation.md)" not in text:
        text = insert_after_line(text, "p63_exact_heterogeneous_integer_calibration.svg", "![P64 fast certified heterogeneous integer approximation](figures/p64_fast_heterogeneous_integer_approximation.svg)", "roadmap figure")
        text = insert_after_line(text, "| [P63](proposition_63_exact_heterogeneous_integer_calibration.md)", "| [P64](proposition_64_fast_heterogeneous_integer_approximation.md) | flooring of the P62 continuous optimum away from the one-sample boundary | O(m) feasible integer design with instance-specific and uniform approximation factors relative to P63 | proved scalable approximation theorem |", "roadmap row")
        write(path, text)

    path = "docs/research_navigation.md"
    text = read(path)
    if "| P64 | [Fast certified heterogeneous integer approximation]" not in text:
        text = text.replace("P1 through P63", "P1 through P64")
        text = insert_after_line(text, "| P63 | [Exact heterogeneous-cost integer calibration]", "| P64 | [Fast certified heterogeneous integer approximation](proposition_64_fast_heterogeneous_integer_approximation.md) | linear-time floor construction with explicit approximation certificate relative to the exact P63 optimum |", "navigation")
        write(path, text)

    path = "docs/equation_and_citation_map.md"
    text = read(path)
    if "# 53. P64 fast certified heterogeneous integer approximation" not in text:
        text = text.rstrip() + r'''

---

# 53. P64 fast certified heterogeneous integer approximation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(k_e=\lfloor n_e^*\rfloor\) | fast whole-measurement construction from P62 | repository construction | [P64](proposition_64_fast_heterogeneous_integer_approximation.md) |
| \(r_{\min}=\min_e \lfloor n_e^*\rfloor/n_e^*\) | instance-specific rounding-retention factor | repository definition | [P64](proposition_64_fast_heterogeneous_integer_approximation.md) |
| \(U(k)\le r_{\min}^{-1/2}U_{\rm int}^*\) | certified approximation ratio relative to P63 | proved from termwise floor distortion and P62 lower bound | [P64](proposition_64_fast_heterogeneous_integer_approximation.md) |
| \(n_e^*\ge\nu>1\Rightarrow U(k)/U_{\rm int}^*\le\sqrt{\nu/(\nu-1)}\) | uniform regime guarantee | proved floor inequality | [P64](proposition_64_fast_heterogeneous_integer_approximation.md) |
| \(O(m)\) | construction cost after P62 closed form | direct complexity bound | [P64](proposition_64_fast_heterogeneous_integer_approximation.md) |

P64 is a certified regime-specific approximation, not an FPTAS claim.
''' + "\n"
        write(path, text)

    for path in ("pyproject.toml", "CITATION.cff"):
        text = read(path)
        text = text.replace("0.63.0", "0.64.0")
        text = text.replace("exact heterogeneous-cost integer calibration, robust experiment design", "exact heterogeneous-cost integer calibration, fast certified heterogeneous integer approximation, robust experiment design")
        write(path, text)

    path = "CHANGELOG.md"
    text = read(path)
    if not text.startswith("# 0.64.0 - 2026-09-10"):
        write(path, "# 0.64.0 - 2026-09-10\n\n- Add P64 fast certified heterogeneous integer approximation.\n- Prove feasibility of flooring the P62 optimum when all continuous counts are at least one.\n- Add instance-specific and uniform approximation factors relative to the exact P63 optimum.\n- Add explicit regime failure, linear-time implementation, tests, visual, provenance, and publication integration.\n\n" + text)

    path = "tests/test_release_metadata_consistency.py"
    text = read(path).replace("version-0.63.0-2563eb", "version-0.64.0-2563eb").replace('version = "0\\.63\\.0"', 'version = "0\\.64\\.0"').replace("version: 0\\.63\\.0", "version: 0\\.64\\.0")
    marker = '        "Proposition 63",\n        "p63_exact_heterogeneous_integer_calibration.svg",\n        "exact_heterogeneous_integer_calibration.py",\n        "test_exact_heterogeneous_integer_calibration.py",\n'
    if '"Proposition 64"' not in text:
        text = replace_once(text, marker, marker + '        "Proposition 64",\n        "p64_fast_heterogeneous_integer_approximation.svg",\n        "fast_heterogeneous_integer_approximation.py",\n        "test_fast_heterogeneous_integer_approximation.py",\n', "release guards")
    write(path, text)

    path = "tests/test_main_page_visual_paper.py"
    text = read(path)
    if '"p64_fast_heterogeneous_integer_approximation.svg"' not in text:
        text = replace_once(text, '    "p63_exact_heterogeneous_integer_calibration.svg",', '    "p63_exact_heterogeneous_integer_calibration.svg",\n    "p64_fast_heterogeneous_integer_approximation.svg",', "visual guard")
    text = text.replace("for index in range(1, 64):", "for index in range(1, 65):")
    write(path, text)

    write("tests/test_fast_heterogeneous_integer_approximation_publication.py", '''from pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\n\ndef test_p64_publication_surface():\n    readme = (ROOT / "README.md").read_text(encoding="utf-8")\n    assert "P64 fast certified integer approximation" in readme\n    assert "p64_fast_heterogeneous_integer_approximation.svg" in readme\n    assert "fast_heterogeneous_integer_approximation.py" in readme\n    assert "[P64](proposition_64_fast_heterogeneous_integer_approximation.md)" in (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")\n    assert "| P64 | [Fast certified heterogeneous integer approximation]" in (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")\n    assert "# 53. P64 fast certified heterogeneous integer approximation" in (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")\n''')


if __name__ == "__main__":
    main()
