from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    assert count == 1, f"{label}: expected one match, found {count}"
    return text.replace(old, new, 1)


# README
path = Path("README.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "version-0.64.0-2563eb",
    "version-0.65.0-2563eb",
    "README version badge",
)
text = replace_once(
    text,
    "**P64** adds a scalable certified alternative: when every P62 continuous allocation is at least one measurement, simply flooring those allocations is feasible and comes with an explicit instance-specific multiplicative guarantee relative to the exact P63 optimum.",
    "**P64** adds a scalable certified alternative: when every P62 continuous allocation is at least one measurement, simply flooring those allocations is feasible and comes with an explicit instance-specific multiplicative guarantee relative to the exact P63 optimum. **P65** removes that one-sample regime restriction by solving the lower-bounded continuous problem exactly: mandatory one-observation constraints enter through a thresholded water-filling active set, and flooring the resulting baseline-safe optimum gives a feasible integer design with an instance-specific certificate and a universal square-root-of-two objective guarantee relative to the exact P63 optimum.",
    "README abstract P65",
)
text = replace_once(
    text,
    "The public research record now contains **64 proposition-level results, 59 equation-driven quantitative figures, quantum and classical physical maps, reproducible numerical examples, counterexamples, and a multi-version Python test matrix**.",
    "The public research record now contains **65 proposition-level results, 60 equation-driven quantitative figures, quantum and classical physical maps, reproducible numerical examples, counterexamples, and a multi-version Python test matrix**.",
    "README public count",
)
text = replace_once(
    text,
    "## Latest proved extension: P64 fast certified integer approximation",
    "## Previous proved extension: P64 fast certified integer approximation",
    "README P64 heading",
)
p64_end = "[Read Proposition 64](docs/proposition_64_fast_heterogeneous_integer_approximation.md). The [visual](docs/figures/p64_fast_heterogeneous_integer_approximation.svg), [implementation](src/consciousness_bridge/fast_heterogeneous_integer_approximation.py), and [tests](tests/test_fast_heterogeneous_integer_approximation.py) expose the proof-to-code path.\n\n---\n\n# Scientific status discipline"
p65_section = r'''[Read Proposition 64](docs/proposition_64_fast_heterogeneous_integer_approximation.md). The [visual](docs/figures/p64_fast_heterogeneous_integer_approximation.svg), [implementation](src/consciousness_bridge/fast_heterogeneous_integer_approximation.py), and [tests](tests/test_fast_heterogeneous_integer_approximation.py) expose the proof-to-code path.

---

## Latest proved extension: P65 lower-bounded heterogeneous calibration

![P65 lower-bounded heterogeneous calibration](docs/figures/p65_lower_bounded_heterogeneous_calibration.svg)

P64 gives a fast certified floor construction only when the unconstrained P62 optimum already assigns at least one observation to every calibrated edge. P65 removes that regime restriction by putting the mandatory baseline directly into the continuous optimization.

For effective uncertainty coefficients \(b_e>0\), per-observation costs \(c_e>0\), and total calibration budget \(B\), P65 solves

\[
\boxed{
\min_{n_e\ge1}\sum_e\frac{b_e}{\sqrt{n_e}}
\quad\text{subject to}\quad
\sum_ec_en_e\le B.
}
\]

The problem is feasible exactly when

\[
\boxed{B\ge B_0=\sum_ec_e.}
\]

Strict convexity and the KKT conditions give the unique thresholded water-filling solution

\[
\boxed{
n_e^*=\max\left\{1,\tau\left(\frac{b_e}{c_e}\right)^{2/3}\right\},
}
\]

where \(\tau\) is chosen so that

\[
\boxed{
\sum_ec_e\max\left\{1,\tau\left(\frac{b_e}{c_e}\right)^{2/3}\right\}=B.
}
\]

Edges whose free solution would fall below one remain pinned at the mandatory baseline. The remaining budget is distributed over the free active set. Sorting the edge thresholds gives an \(O(m\log m)\) continuous solver for \(m\) calibrated edges.

Because the continuous optimum already satisfies \(n_e^*\ge1\), flooring is now always safe:

\[
\boxed{k_e=\lfloor n_e^*\rfloor\ge1,\qquad \sum_ec_ek_e\le B.}
\]

With

\[
r_{\min}=\min_e\frac{\lfloor n_e^*\rfloor}{n_e^*},
\]

P65 proves

\[
\boxed{
U(k)\le\frac{1}{\sqrt{r_{\min}}}U_{\rm int}^*(B)
\le\sqrt2\,U_{\rm int}^*(B).
}
\]

The first factor is instance-specific. The second follows from \(\lfloor x\rfloor\ge x/2\) for every \(x\ge1\). P63 remains the exact unequal-cost integer solver; P65 is a scalable lower-bounded continuous theorem plus a certified integer approximation, not an exact integer theorem.

The scientific boundary is unchanged. P65 optimizes a declared experimental calibration surrogate. It does not identify any calibration variable with consciousness, does not solve the physical-to-experiential bridge, and does not imply that quantum mechanics is incomplete.

[Read Proposition 65](docs/proposition_65_lower_bounded_heterogeneous_calibration.md). The [P65 visual](docs/figures/p65_lower_bounded_heterogeneous_calibration.svg), [implementation](src/consciousness_bridge/lower_bounded_heterogeneous_calibration.py), and [tests](tests/test_lower_bounded_heterogeneous_calibration.py) expose the complete proof-to-code path.

---

# Scientific status discipline'''
text = replace_once(text, p64_end, p65_section, "README P65 section")
text = replace_once(
    text,
    "P1 through P64 with explicit dependency branches",
    "P1 through P65 with explicit dependency branches",
    "README navigation frontier",
)
p64_row = "| fast certified heterogeneous integer approximation | [Proposition 64](docs/proposition_64_fast_heterogeneous_integer_approximation.md) | linear-time floor construction with an explicit approximation certificate relative to P63 |"
p65_row = "| lower-bounded heterogeneous calibration | [Proposition 65](docs/proposition_65_lower_bounded_heterogeneous_calibration.md) | exact thresholded water-filling continuous allocation with mandatory one-observation lower bounds and a baseline-safe square-root-of-two certified integer floor approximation |"
text = replace_once(text, p64_row, p64_row + "\n" + p65_row, "README P65 row")
path.write_text(text, encoding="utf-8")

# Theorem roadmap
path = Path("docs/theorem_roadmap.md")
text = path.read_text(encoding="utf-8")
p64_fig = "![P64 fast certified heterogeneous integer approximation](figures/p64_fast_heterogeneous_integer_approximation.svg)"
p65_fig = "![P65 lower-bounded heterogeneous calibration](figures/p65_lower_bounded_heterogeneous_calibration.svg)"
text = replace_once(text, p64_fig, p64_fig + "\n" + p65_fig, "roadmap P65 figure")
p64_index = "| [P64](proposition_64_fast_heterogeneous_integer_approximation.md) | flooring of the P62 continuous optimum away from the one-sample boundary | O(m) feasible integer design with instance-specific and uniform approximation factors relative to P63 | proved scalable approximation theorem |"
p65_index = "| [P65](proposition_65_lower_bounded_heterogeneous_calibration.md) | lower-bounded strict convexity, active-set water filling, and floor approximation | baseline-safe heterogeneous calibration beyond the P64 one-sample regime restriction | proved continuous theorem plus approximation certificate |"
text = replace_once(text, p64_index, p64_index + "\n" + p65_index, "roadmap P65 index")
path.write_text(text, encoding="utf-8")

# Research navigation
path = Path("docs/research_navigation.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "for the dependency structure from P1 through P64, including the physical scale branches",
    "for the dependency structure from P1 through P65, including the physical scale branches",
    "research navigation frontier",
)
p64_nav = "| P64 | [Fast certified heterogeneous integer approximation](proposition_64_fast_heterogeneous_integer_approximation.md) | linear-time floor construction with explicit approximation certificate relative to the exact P63 optimum |"
p65_nav = "| P65 | [Lower-bounded heterogeneous calibration](proposition_65_lower_bounded_heterogeneous_calibration.md) | exact thresholded water-filling continuous allocation with baseline-safe floor approximation and universal square-root-of-two certificate |"
text = replace_once(text, p64_nav, p64_nav + "\n" + p65_nav, "research navigation P65")
path.write_text(text, encoding="utf-8")

# Equation and citation map
path = Path("docs/equation_and_citation_map.md")
text = path.read_text(encoding="utf-8")
assert "# 54. P65 lower-bounded heterogeneous calibration" not in text
p65_map = r'''

---

# 54. P65 lower-bounded heterogeneous calibration

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(B_0=\sum_ec_e\), with feasibility exactly when \(B\ge B_0\) | mandatory one-observation baseline cost | proved feasibility threshold | [P65](proposition_65_lower_bounded_heterogeneous_calibration.md) |
| \(n_e^*=\max\{1,\tau(b_e/c_e)^{2/3}\}\) | unique lower-bounded continuous calibration allocation | proved by strict convexity and KKT conditions | [P65](proposition_65_lower_bounded_heterogeneous_calibration.md) |
| \(t_e=(c_e/b_e)^{2/3}\) and threshold-sorted active-set scan | identifies pinned and free calibration edges | proved water-filling construction | [P65](proposition_65_lower_bounded_heterogeneous_calibration.md) |
| \(k_e=\lfloor n_e^*\rfloor\ge1\), \(\sum_ec_ek_e\le B\) | baseline-safe executable integer construction | proved feasibility corollary | [P65](proposition_65_lower_bounded_heterogeneous_calibration.md) |
| \(r_{\min}=\min_e\lfloor n_e^*\rfloor/n_e^*\) and \(U(k)\le r_{\min}^{-1/2}U_{\rm int}^*(B)\) | instance-specific approximation certificate relative to P63 | proved from termwise floor distortion plus continuous relaxation | [P65](proposition_65_lower_bounded_heterogeneous_calibration.md) |
| \(\lfloor x\rfloor\ge x/2\) for \(x\ge1\), hence \(U(k)\le\sqrt2\,U_{\rm int}^*(B)\) | universal guarantee for the P65 floor construction | proved approximation corollary | [P65](proposition_65_lower_bounded_heterogeneous_calibration.md) |

P65 solves the lower-bounded continuous version of the declared separable calibration surrogate and provides a certified floor approximation. P63 remains the exact heterogeneous-cost integer solver. P65 does not establish a physical-to-experiential bridge or any quantum-ontological conclusion.
'''
text = text.rstrip() + p65_map + "\n"
path.write_text(text, encoding="utf-8")

# pyproject
path = Path("pyproject.toml")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version = "0.64.0"', 'version = "0.65.0"', "pyproject version")
text = replace_once(
    text,
    "exact heterogeneous-cost integer calibration, fast certified heterogeneous integer approximation, robust experiment design",
    "exact heterogeneous-cost integer calibration, fast certified heterogeneous integer approximation, lower-bounded heterogeneous calibration, robust experiment design",
    "pyproject description",
)
path.write_text(text, encoding="utf-8")

# CITATION
path = Path("CITATION.cff")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version: 0.64.0", "version: 0.65.0", "citation version")
text = replace_once(
    text,
    "exact heterogeneous-cost integer calibration, fast certified heterogeneous integer approximation, robust experiment design",
    "exact heterogeneous-cost integer calibration, fast certified heterogeneous integer approximation, lower-bounded heterogeneous calibration, robust experiment design",
    "citation abstract",
)
path.write_text(text, encoding="utf-8")

# Changelog
path = Path("CHANGELOG.md")
text = path.read_text(encoding="utf-8")
assert not text.startswith("# 0.65.0")
entry = """# 0.65.0 - 2026-09-10

- Add P65 lower-bounded heterogeneous calibration.
- Solve the continuous unequal-cost calibration problem exactly with mandatory one-observation lower bounds using a thresholded water-filling active set.
- Prove exact feasibility at B greater than or equal to the mandatory baseline and recovery of P62 when no lower bound is active.
- Add a baseline-safe floor construction with an instance-specific factor and a universal square-root-of-two objective certificate relative to the exact P63 optimum.
- Add implementation, regression tests, theorem visual, public navigation, website integration, provenance, and release metadata.

"""
path.write_text(entry + text, encoding="utf-8")

# Website index
path = Path("website/index.html")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "<strong>64</strong><span>proposition-level results</span>", "<strong>65</strong><span>proposition-level results</span>", "website proposition count")
text = replace_once(text, "<strong>v0.64.0</strong><span>current documented release</span>", "<strong>v0.65.0</strong><span>current documented release</span>", "website version")
text = replace_once(text, "See all 64 results grouped by scientific role", "See all 65 results grouped by scientific role", "website result link")
text = replace_once(text, "P58-P64 form the newest quantitative chain.", "P58-P65 form the newest quantitative chain.", "website newest chain")
p64_article = '<article class="result"><span>P64</span><h3>Fast certified approximation</h3><p>Flooring the continuous optimum gives a scalable feasible design with an explicit approximation factor in its declared validity regime.</p></article>'
p65_article = '<article class="result"><span>P65</span><h3>Baseline-safe water filling</h3><p>Mandatory one-sample constraints enter the continuous optimization directly, yielding an exact active-set optimum and a universally square-root-of-two certified floor approximation.</p></article>'
text = replace_once(text, p64_article, p64_article + "\n        " + p65_article, "website P65 card")
text = replace_once(
    text,
    "docs/figures/p64_fast_heterogeneous_integer_approximation.svg\" alt=\"P64 fast heterogeneous integer approximation",
    "docs/figures/p65_lower_bounded_heterogeneous_calibration.svg\" alt=\"P65 lower-bounded heterogeneous calibration",
    "website latest figure",
)
path.write_text(text, encoding="utf-8")

# Website research map
path = Path("website/research-map.html")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "Sixty-four results, one dependency-aware scientific program", "Sixty-five results, one dependency-aware scientific program", "research map count")
text = replace_once(text, "P54-P64: From switching costs to robust measurement allocation", "P54-P65: From switching costs to robust measurement allocation", "research map frontier")
text = replace_once(text, "<span>P62-P64</span><h3>Heterogeneous-cost calibration</h3><p>Separate sensitivity from measurement cost, solve the integer problem exactly with dynamic programming, then provide a fast certified approximation in its stated regime.</p>", "<span>P62-P65</span><h3>Heterogeneous-cost calibration</h3><p>Separate sensitivity from measurement cost, solve the integer problem exactly with dynamic programming, then provide scalable certified approximations both inside and outside the original P64 one-sample regime.</p>", "research map P65 group")
path.write_text(text, encoding="utf-8")

# Release consistency test
path = Path("tests/test_release_metadata_consistency.py")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'assert "version-0.64.0-2563eb" in readme', 'assert "version-0.65.0-2563eb" in readme', "release test badge")
text = replace_once(text, 'r\'^version = "0\\.64\\.0"$\'', 'r\'^version = "0\\.65\\.0"$\'', "release test pyproject")
text = replace_once(text, 'r\'^version: 0\\.64\\.0$\'', 'r\'^version: 0\\.65\\.0$\'', "release test citation")
p64_tokens = '        "Proposition 64",\n        "p64_fast_heterogeneous_integer_approximation.svg",\n        "fast_heterogeneous_integer_approximation.py",\n        "test_fast_heterogeneous_integer_approximation.py",'
p65_tokens = '        "Proposition 65",\n        "p65_lower_bounded_heterogeneous_calibration.svg",\n        "lower_bounded_heterogeneous_calibration.py",\n        "test_lower_bounded_heterogeneous_calibration.py",'
text = replace_once(text, p64_tokens, p64_tokens + "\n" + p65_tokens, "release test P65 tokens")
path.write_text(text, encoding="utf-8")

# Website integrity test
path = Path("tests/test_research_website_integrity.py")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'figure = "docs/figures/p64_fast_heterogeneous_integer_approximation.svg"', 'figure = "docs/figures/p65_lower_bounded_heterogeneous_calibration.svg"', "website test latest figure")
text = replace_once(text, '    assert "P54-P64" in html\n    assert _max_proposition_number() == 64', '    frontier = _max_proposition_number()\n    assert f"P54-P{frontier}" in html', "website test frontier")
path.write_text(text, encoding="utf-8")
