from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    assert count == 1, f"{label}: expected one match, found {count}"
    return text.replace(old, new, 1)


# README
path = Path("README.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version-0.65.0-2563eb", "version-0.66.0-2563eb", "README version badge")
text = replace_once(
    text,
    "**P65** removes that one-sample regime restriction by solving the lower-bounded continuous problem exactly: mandatory one-observation constraints enter through a thresholded water-filling active set, and flooring the resulting baseline-safe optimum gives a feasible integer design with an instance-specific certificate and a universal square-root-of-two objective guarantee relative to the exact P63 optimum.",
    "**P65** removes that one-sample regime restriction by solving the lower-bounded continuous problem exactly: mandatory one-observation constraints enter through a thresholded water-filling active set, and flooring the resulting baseline-safe optimum gives a feasible integer design with an instance-specific certificate and a universal square-root-of-two objective guarantee relative to the exact P63 optimum. **P66** then uses the budget left after P65 flooring exactly within the floor-dominating integer class: the residual budget is always smaller than the mandatory one-observation baseline cost, so a residual dynamic program can improve the P65 allocation without scaling with the full original budget magnitude.",
    "README abstract P66",
)
text = replace_once(
    text,
    "The public research record now contains **65 proposition-level results, 60 equation-driven quantitative figures, quantum and classical physical maps, reproducible numerical examples, counterexamples, and a multi-version Python test matrix**.",
    "The public research record now contains **66 proposition-level results, 61 equation-driven quantitative figures, quantum and classical physical maps, reproducible numerical examples, counterexamples, and a multi-version Python test matrix**.",
    "README public count",
)
text = replace_once(text, "## Latest proved extension: P65 lower-bounded heterogeneous calibration", "## Previous proved extension: P65 lower-bounded heterogeneous calibration", "README P65 heading")
p65_end = "[Read Proposition 65](docs/proposition_65_lower_bounded_heterogeneous_calibration.md). The [P65 visual](docs/figures/p65_lower_bounded_heterogeneous_calibration.svg), [implementation](src/consciousness_bridge/lower_bounded_heterogeneous_calibration.py), and [tests](tests/test_lower_bounded_heterogeneous_calibration.py) expose the complete proof-to-code path.\n\n---\n\n# Scientific status discipline"
p66_section = r'''[Read Proposition 65](docs/proposition_65_lower_bounded_heterogeneous_calibration.md). The [P65 visual](docs/figures/p65_lower_bounded_heterogeneous_calibration.svg), [implementation](src/consciousness_bridge/lower_bounded_heterogeneous_calibration.py), and [tests](tests/test_lower_bounded_heterogeneous_calibration.py) expose the complete proof-to-code path.

---

## Latest proved extension: P66 residual-exact calibration augmentation

![P66 residual-exact calibration augmentation](docs/figures/p66_residual_exact_calibration_augmentation.svg)

P65 gives a baseline-safe integer allocation by flooring the exact lower-bounded continuous optimum. P66 asks whether the budget left by that floor can be used without returning to a dynamic program whose axis scales with the full budget.

Let

\[
f_e=\lfloor n_e^*\rfloor,
\qquad
R=B-\sum_e c_e f_e.
\]

Because the P65 continuous optimum spends the full budget,

\[
\boxed{
R=\sum_e c_e\{n_e^*\}
<\sum_e c_e=B_0.
}
\]

Thus the residual budget is bounded by the mandatory one-observation baseline cost, independently of how large the original budget \(B\) is.

P66 optimizes only the nonnegative integer increments above the P65 floor:

\[
\boxed{
k_e=f_e+z_e,
\qquad
z_e\in\mathbb Z_{\ge0},
\qquad
\sum_e c_ez_e\le R.
}
\]

For positive integer costs, an exact Bellman dynamic program over residual spend returns the globally optimal allocation inside the restricted class \(k_e\ge f_e\). Therefore

\[
\boxed{U(k^{66})\le U(f).}
\]

If

\[
r_{66}=\min_e\frac{k_e^{66}}{n_e^*},
\]

then \(r_{66}\ge r_{65}\), so the same continuous lower-bound argument yields the computable certificate

\[
\boxed{
U(k^{66})
\le
\frac{1}{\sqrt{r_{66}}}U_{\rm int}^*(B)
\le
\frac{1}{\sqrt{r_{65}}}U_{\rm int}^*(B)
\le
\sqrt2\,U_{\rm int}^*(B).
}
\]

P66 is exact only within the floor-dominating class. P63 remains the unrestricted exact heterogeneous-cost integer theorem. This distinction is explicit in the proof, implementation, tests, and theorem visual.

The scientific boundary is unchanged. P66 is a resource-allocation theorem for the declared calibration surrogate. It does not identify any calibration quantity with consciousness, does not solve the physical-to-experiential bridge, and does not imply any incompleteness of quantum mechanics.

[Read Proposition 66](docs/proposition_66_residual_exact_calibration_augmentation.md). The [P66 visual](docs/figures/p66_residual_exact_calibration_augmentation.svg), [implementation](src/consciousness_bridge/residual_exact_calibration_augmentation.py), and [tests](tests/test_residual_exact_calibration_augmentation.py) expose the proof-to-code path.

---

# Scientific status discipline'''
text = replace_once(text, p65_end, p66_section, "README P66 section")
text = replace_once(text, "P1 through P65 with explicit dependency branches", "P1 through P66 with explicit dependency branches", "README frontier")
p65_row = "| lower-bounded heterogeneous calibration | [Proposition 65](docs/proposition_65_lower_bounded_heterogeneous_calibration.md) | exact thresholded water-filling continuous allocation with mandatory one-observation lower bounds and a baseline-safe square-root-of-two certified integer floor approximation |"
p66_row = "| residual-exact calibration augmentation | [Proposition 66](docs/proposition_66_residual_exact_calibration_augmentation.md) | exact residual-budget augmentation above the P65 floor, with bounded residual scale and an improved computable certificate relative to P63 |"
text = replace_once(text, p65_row, p65_row + "\n" + p66_row, "README P66 row")
path.write_text(text, encoding="utf-8")

# theorem roadmap
path = Path("docs/theorem_roadmap.md")
text = path.read_text(encoding="utf-8")
p65_fig = "![P65 lower-bounded heterogeneous calibration](figures/p65_lower_bounded_heterogeneous_calibration.svg)"
p66_fig = "![P66 residual-exact calibration augmentation](figures/p66_residual_exact_calibration_augmentation.svg)"
text = replace_once(text, p65_fig, p65_fig + "\n" + p66_fig, "roadmap P66 figure")
p65_row = "| [P65](proposition_65_lower_bounded_heterogeneous_calibration.md) | lower-bounded strict convexity, active-set water filling, and floor approximation | baseline-safe heterogeneous calibration beyond the P64 one-sample regime restriction | proved continuous theorem plus approximation certificate |"
p66_row = "| [P66](proposition_66_residual_exact_calibration_augmentation.md) | P65 floor, bounded residual budget, and exact residual-spend dynamic programming | best floor-dominating integer augmentation with improved computable certificate | proved restricted-exact augmentation theorem |"
text = replace_once(text, p65_row, p65_row + "\n" + p66_row, "roadmap P66 row")
path.write_text(text, encoding="utf-8")

# research navigation
path = Path("docs/research_navigation.md")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "from P1 through P65", "from P1 through P66", "navigation frontier")
p65_nav = "| P65 | [Lower-bounded heterogeneous calibration](proposition_65_lower_bounded_heterogeneous_calibration.md) | exact thresholded water-filling continuous allocation with baseline-safe floor approximation and universal square-root-of-two certificate |"
p66_nav = "| P66 | [Residual-exact calibration augmentation](proposition_66_residual_exact_calibration_augmentation.md) | exact bounded-residual optimization above the P65 floor with monotone objective improvement and a sharpened computable approximation certificate |"
text = replace_once(text, p65_nav, p65_nav + "\n" + p66_nav, "navigation P66 row")
path.write_text(text, encoding="utf-8")

# equation and citation map
path = Path("docs/equation_and_citation_map.md")
text = path.read_text(encoding="utf-8")
assert "# 55. P66 residual-exact calibration augmentation" not in text
text = text.rstrip() + r'''

---

# 55. P66 residual-exact calibration augmentation

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(f_e=\lfloor n_e^*\rfloor\) | P65 floor used as the executable baseline | proved P65 input | [P65](proposition_65_lower_bounded_heterogeneous_calibration.md) |
| \(R=B-\sum_ec_ef_e=\sum_ec_e\{n_e^*\}<\sum_ec_e=B_0\) | bounded residual budget identity | proved | [P66](proposition_66_residual_exact_calibration_augmentation.md) |
| \(k_e=f_e+z_e\), \(z_e\in\mathbb Z_{\ge0}\), \(\sum_ec_ez_e\le R\) | floor-dominating integer augmentation class | definition | [P66](proposition_66_residual_exact_calibration_augmentation.md) |
| residual Bellman recurrence over exact spend | exact optimizer within the floor-dominating class | proved restricted exactness | [P66](proposition_66_residual_exact_calibration_augmentation.md) |
| \(U(k^{66})\le U(f)\) | monotone improvement over P65 flooring | proved | [P66](proposition_66_residual_exact_calibration_augmentation.md) |
| \(r_{66}=\min_e k_e^{66}/n_e^*\ge r_{65}\) | sharpened floor-ratio certificate | proved | [P66](proposition_66_residual_exact_calibration_augmentation.md) |
| \(U(k^{66})\le r_{66}^{-1/2}U_{\rm int}^*(B)\le\sqrt2 U_{\rm int}^*(B)\) | computable approximation certificate relative to P63 | proved | [P66](proposition_66_residual_exact_calibration_augmentation.md) |

P66 is exact only inside the declared class of integer allocations that dominate the P65 floor. P63 remains the unrestricted exact integer solver. P66 makes no experiential or quantum-ontological claim.
''' + "\n"
path.write_text(text, encoding="utf-8")

# metadata
path = Path("pyproject.toml")
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version = "0.65.0"', 'version = "0.66.0"', "pyproject version")
text = replace_once(text, "lower-bounded heterogeneous calibration, robust experiment design", "lower-bounded heterogeneous calibration, residual-exact calibration augmentation, robust experiment design", "pyproject description")
path.write_text(text, encoding="utf-8")

path = Path("CITATION.cff")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "version: 0.65.0", "version: 0.66.0", "citation version")
text = replace_once(text, "lower-bounded heterogeneous calibration, robust experiment design", "lower-bounded heterogeneous calibration, residual-exact calibration augmentation, robust experiment design", "citation abstract")
path.write_text(text, encoding="utf-8")

path = Path("CHANGELOG.md")
text = path.read_text(encoding="utf-8")
assert not text.startswith("# 0.66.0")
entry = """# 0.66.0 - 2026-09-10

- Add P66 residual-exact calibration augmentation.
- Prove that the budget left after P65 flooring is strictly smaller than the one-observation baseline cost.
- Solve the residual integer augmentation exactly within the class that dominates the P65 floor.
- Prove monotone objective improvement and a sharpened computable approximation certificate relative to the exact P63 optimum.
- Keep P63 explicitly identified as the unrestricted exact integer theorem.
- Add implementation, regression tests, geometry-guarded theorem visual, public navigation, website integration, provenance, and release metadata.

"""
path.write_text(entry + text, encoding="utf-8")

# website
path = Path("website/index.html")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "<strong>65</strong><span>proposition-level results</span>", "<strong>66</strong><span>proposition-level results</span>", "website count")
text = replace_once(text, "<strong>v0.65.0</strong><span>current documented release</span>", "<strong>v0.66.0</strong><span>current documented release</span>", "website version")
text = replace_once(text, "See all 65 results grouped by scientific role", "See all 66 results grouped by scientific role", "website link count")
text = replace_once(text, "P58-P65 form the newest quantitative chain.", "P58-P66 form the newest quantitative chain.", "website chain")
p65_card = '<article class="result"><span>P65</span><h3>Baseline-safe water filling</h3><p>Mandatory one-sample constraints enter the continuous optimization directly, yielding an exact active-set optimum and a universally square-root-of-two certified floor approximation.</p></article>'
p66_card = '<article class="result"><span>P66</span><h3>Residual-exact augmentation</h3><p>The budget left after P65 flooring is bounded by the baseline cost, enabling exact residual optimization inside the floor-dominating integer class without a full-budget dynamic-program axis.</p></article>'
text = replace_once(text, p65_card, p65_card + "\n        " + p66_card, "website P66 card")
text = replace_once(text, "docs/figures/p65_lower_bounded_heterogeneous_calibration.svg\" alt=\"P65 lower-bounded heterogeneous calibration", "docs/figures/p66_residual_exact_calibration_augmentation.svg\" alt=\"P66 residual-exact calibration augmentation", "website latest figure")
path.write_text(text, encoding="utf-8")

path = Path("website/research-map.html")
text = path.read_text(encoding="utf-8")
text = replace_once(text, "Sixty-five results, one dependency-aware scientific program", "Sixty-six results, one dependency-aware scientific program", "research map count")
text = replace_once(text, "P54-P65: From switching costs to robust measurement allocation", "P54-P66: From switching costs to robust measurement allocation", "research map frontier")
text = replace_once(text, "<span>P62-P65</span><h3>Heterogeneous-cost calibration</h3><p>Separate sensitivity from measurement cost, solve the integer problem exactly with dynamic programming, then provide scalable certified approximations both inside and outside the original P64 one-sample regime.</p>", "<span>P62-P66</span><h3>Heterogeneous-cost calibration</h3><p>Separate sensitivity from measurement cost, solve the unrestricted integer problem exactly with P63, then provide scalable certified approximations and bounded-residual exact augmentation through P66.</p>", "research map P66 group")
path.write_text(text, encoding="utf-8")

# release tests
for filename in ["tests/test_release_metadata_consistency.py", "tests/test_research_website_integrity.py"]:
    path = Path(filename)
    text = path.read_text(encoding="utf-8")
    text = text.replace("0.65.0", "0.66.0")
    text = text.replace("P54-P65", "P54-P66")
    text = text.replace(">65<", ">66<")
    path.write_text(text, encoding="utf-8")

# prohibit long dash characters in touched publication surfaces
for filename in [
    "README.md",
    "docs/proposition_66_residual_exact_calibration_augmentation.md",
    "docs/theorem_roadmap.md",
    "docs/research_navigation.md",
    "docs/equation_and_citation_map.md",
    "website/index.html",
    "website/research-map.html",
    "CHANGELOG.md",
]:
    text = Path(filename).read_text(encoding="utf-8")
    assert "\u2013" not in text, f"en dash found in {filename}"
    assert "\u2014" not in text, f"em dash found in {filename}"
