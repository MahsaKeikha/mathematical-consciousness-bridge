from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace(text: str, old: str, new: str) -> str:
    return text.replace(old, new) if old in text else text


def insert_before(text: str, marker: str, addition: str) -> str:
    if addition.strip() in text:
        return text
    if marker not in text:
        raise RuntimeError(f"missing insertion marker: {marker[:100]!r}")
    return text.replace(marker, addition + marker, 1)


def insert_after(text: str, marker: str, addition: str) -> str:
    if addition.strip() in text:
        return text
    if marker not in text:
        raise RuntimeError(f"missing insertion marker: {marker[:100]!r}")
    return text.replace(marker, marker + addition, 1)


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    text = replace(text, "version-0.78.0-2563eb", "version-0.79.0-2563eb")
    text = replace(text, "Version 0.78.0", "Version 0.79.0")
    text = replace(text, "The research currently contains **78 proposition-level results** and **66 equation-driven quantitative figures**. The theorem frontier is P78.", "The research currently contains **79 proposition-level results** and **67 equation-driven quantitative figures**. The theorem frontier is P79.")
    text = replace(text, "P1 through P78 with explicit dependency branches", "P1 through P79 with explicit dependency branches")
    text = replace(text, "P19-P24, P71-P78", "P19-P24, P71-P79")
    text = replace(text, "P71-P78 return to the P19 target-sufficiency lineage", "P71-P79 return to the P19 target-sufficiency lineage")
    text = replace(text, "Read the complete P1 to P78 detailed proposition record", "Read the complete P1 to P79 detailed proposition record")
    text = replace(text, "| Public theorem frontier | **P78** |", "| Public theorem frontier | **P79** |")
    text = replace(text, "| Documented version | **v0.78.0** |", "| Documented version | **v0.79.0** |")
    text = replace(text, "| Proposition-level results | **78** |", "| Proposition-level results | **79** |")
    text = replace(text, "| Equation-driven quantitative figures | **66** |", "| Equation-driven quantitative figures | **67** |")
    text = replace(text, "extend P78's certified continuous-family computation", "extend the P78-P79 certified full-law pipeline")

    plain = """

P79 closes a smaller but important numerical-certification gap. P77's sampling radius contains a logarithm and a square root. An ordinary floating-point evaluation may be numerically excellent, but a formal rejection certificate needs the inequality direction to be guaranteed. P79 therefore constructs an exact rational upper bound on that radius: it brackets the logarithm with a positive convergent series and an explicit tail, then encloses the square root using integer arithmetic. The P77/P78/P79 rejection handoff is valid only when the P78 lower bound is strictly larger than the P79 upper bound. This closes a numerical-direction gap, does not make non-rejection into model acceptance, and the physical-to-experiential bridge remains open.
"""
    if "P79 closes a smaller but important numerical-certification gap" not in text:
        marker = "\nOnly after the physical description, the target, and the way the target is measured are all scientifically defensible"
        text = insert_before(text, marker, plain)

    p79_section = r'''

## 1.13 P79: certified rational sampling-radius envelope

P77 defines the simultaneous finite-alphabet sampling radius and P78 supplies a certified lower bound on distance to the complete continuous P75 model family. The remaining rejection comparison has to preserve its inequality direction numerically: **P78 lower-bounds model distance**, while **P79 upper-bounds the P77 sampling radius**.

For alphabet size $K$, sample size $n$, and confidence level $1-\alpha$,

$$
\varepsilon_{n,K}(\alpha)
=
\sqrt{\frac{\log(2K/\alpha)}{2n}}.
$$

P79 constructs exact rational values $\underline\varepsilon$ and $\overline\varepsilon$ satisfying

$$
\boxed{\underline\varepsilon\le\varepsilon_{n,K}(\alpha)\le\overline\varepsilon.}
$$

The logarithm is enclosed after exact power-of-two reduction by a positive atanh series with an explicit rational remainder bound. The square root is then enclosed by integer-certified dyadic floor and ceiling operations. Consequently,

$$
\boxed{L_{\mathrm{model}}>\overline\varepsilon\Longrightarrow L_{\mathrm{model}}>\varepsilon_{n,K}(\alpha),}
$$

where $L_{\mathrm{model}}$ is a certified P78 lower bound. This closes a numerical-certification gap in the P77/P78 chain. It does not validate a model when rejection fails, does not identify the P75 latent state with consciousness, and does not solve the physical-to-experiential bridge.

![P79 certified rational sampling-radius envelope](docs/figures/p79_certified_sampling_radius.svg)

**Figure 14. P79 one-sided numerical certification.** Exact statistical inputs are reduced to rational logarithm bounds and an integer-certified dyadic square-root enclosure. The final decision compares a lower bound on model distance with an upper bound on sampling uncertainty, so decimal rounding cannot silently reverse the rejection inequality.

Direct proof: [Proposition 79](docs/proposition_79_certified_sampling_radius.md). Equation and literature classification: [P79 provenance record](docs/p79_equation_provenance.md). Implementation: [`certified_sampling_radius.py`](src/consciousness_bridge/certified_sampling_radius.py). Tests: [`test_certified_sampling_radius.py`](tests/test_certified_sampling_radius.py) and [`test_p79_figure_geometry.py`](tests/test_p79_figure_geometry.py).
'''
    if "## 1.13 P79: certified rational sampling-radius envelope" not in text:
        text = insert_before(text, "\n---\n\n# 2. From physical dynamics to operational structure", p79_section + "\n")

    text = replace(text, "P78 then supplies an exact-rational branch-and-bound lower-bound certificate for the continuous P75 latent family. The remaining challenges are faster and tighter global certification, sharper power, and broader dependent-view alternatives.", "P78 then supplies an exact-rational branch-and-bound lower-bound certificate for the continuous P75 latent family. P79 completes the one-sided numerical handoff by certifying an exact-rational upper envelope for the P77 sampling radius. The remaining challenges are faster and tighter global optimization, sharper statistical power, and broader dependent-view alternatives.")

    p78_status = "| Continuous-family full-law optimization certificate | **P78 proved for the P75 four-view binary latent family using exact-rational multi-affine box lower bounds and an explicit mesh-gap guarantee** |"
    p79_status = "| One-sided sampling-radius numerical certificate | **P79 proved with exact-rational logarithm bracketing and integer-certified dyadic square-root enclosure for the P77 radius** |"
    if p79_status not in text and p78_status in text:
        text = text.replace(p78_status, p78_status + "\n" + p79_status, 1)

    p78_evidence = "| [P78 equation and provenance record](docs/p78_equation_provenance.md) | Multi-affine box enclosures, global branch-and-bound lower bounds, mesh-gap certification, and P77 handoff provenance |"
    p79_evidence = "| [P79 equation and provenance record](docs/p79_equation_provenance.md) | Exact-rational logarithm bounds, dyadic square-root enclosure, and the directionally safe P78/P79 rejection handoff |"
    if p79_evidence not in text and p78_evidence in text:
        text = text.replace(p78_evidence, p78_evidence + "\n" + p79_evidence, 1)

    p78_fals = "| Continuous P75 full-law separation is certified | A P78 global lower bound exceeds a valid P77 sampling-radius upper bound | Treating an incomplete parameter search or ordinary floating approximation as a formal certificate |"
    p79_fals = "| P77/P78 rejection comparison is numerically certified | A P78 model-distance lower bound is strictly larger than the P79 exact-rational sampling-radius upper bound | Comparing rounded decimal approximations without a one-sided enclosure |"
    if p79_fals not in text and p78_fals in text:
        text = text.replace(p78_fals, p78_fals + "\n" + p79_fals, 1)

    write(path, text)


def update_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = replace(text, "frontier is **P78**", "frontier is **P79**")
    text = replace(text, "P1 through P78", "P1 through P79")
    text = replace(text, "P71-P78 return", "P71-P79 return")
    text = replace(text, "P71-P78 form", "P71-P79 form")

    p79 = r'''

### P79: certified rational sampling-radius envelope

P77 supplies the analytic finite-alphabet sampling radius and P78 supplies a certified lower bound on distance to the continuous P75 model family. P79 makes the remaining comparison numerically one-sided rather than relying on floating-point rounding direction.

For

\[
\varepsilon_{n,K}(\alpha)=\sqrt{\frac{\log(2K/\alpha)}{2n}},
\]

P79 constructs exact rational values satisfying

\[
\boxed{\underline\varepsilon\le\varepsilon_{n,K}(\alpha)\le\overline\varepsilon.}
\]

The strict P77 handoff is certified whenever the P78 lower bound satisfies $L_{\mathrm{model}}>\overline\varepsilon$. Failure of this strict inequality is inconclusive and is not model acceptance.

![P79 certified rational sampling-radius envelope](figures/p79_certified_sampling_radius.svg)

Direct proof: [P79](proposition_79_certified_sampling_radius.md). Provenance: [P79 equation record](p79_equation_provenance.md). Implementation: [`certified_sampling_radius.py`](../src/consciousness_bridge/certified_sampling_radius.py). Tests: [`test_certified_sampling_radius.py`](../tests/test_certified_sampling_radius.py).
'''
    if "### P79: certified rational sampling-radius envelope" not in text:
        text = insert_before(text, "\n## 3. Complete proposition index", p79 + "\n")
    p78_row = "| [P78](proposition_78_certified_continuous_model_separation.md) | multi-affine box lower bounds and mesh-gap convergence | certified continuous P75 full-law model separation | proved conditional computational theorem |"
    p79_row = "| [P79](proposition_79_certified_sampling_radius.md) | exact-rational logarithm and dyadic square-root enclosure | one-sided numerical certification of the P77 sampling radius | proved numerical-certification theorem |"
    if p79_row not in text and p78_row in text:
        text = text.replace(p78_row, p78_row + "\n" + p79_row, 1)
    text = replace(text, "After P78, the target side has eight explicit requirements:", "After P79, the target side has nine explicit requirements:")
    if "9. the P77 sampling radius" not in text:
        marker = "8. when the declared family is continuous, the required separation distance must be lower-bounded globally rather than inferred from a local best fit."
        text = insert_after(text, marker, "\n9. the sampling-radius side of the rejection inequality must be upper-bounded with certified numerical direction rather than an unqualified rounded decimal.")
    text = replace(text, "P78 closes the eighth item", "P78 closes the eighth item")
    if "P79 closes the ninth item" not in text:
        text = text.replace("P78 closes the eighth item for the specific P75 four-view binary latent family in L-infinity distance.", "P78 closes the eighth item for the specific P75 four-view binary latent family in L-infinity distance. P79 closes the ninth item for the P77 finite-alphabet sampling radius by exact-rational one-sided numerical enclosure.")
    write(path, text)


def update_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    text = replace(text, "frontier is **P78**", "frontier is **P79**")
    text = replace(text, "P1 through P78", "P1 through P79")
    text = replace(text, "P71-P78 form", "P71-P79 form")
    if "P79 certified rational sampling-radius envelope" not in text:
        anchor = "14. [P78 certified continuous P75 model separation](proposition_78_certified_continuous_model_separation.md) for exact multi-affine box enclosures, global L-infinity distance lower bounds, mesh-gap convergence, and the strict P77 rejection handoff."
        text = insert_after(text, anchor, "\n15. [P79 certified rational sampling-radius envelope](proposition_79_certified_sampling_radius.md) for exact-rational logarithm brackets, integer-certified dyadic square-root enclosure, and the one-sided P78/P79 rejection comparison.")
    branch78 = "| Certified continuous target-model separation | P78 | Supplies exact-rational global lower bounds for distance to the continuous P75 model family and a convergent mesh certificate | [P78](proposition_78_certified_continuous_model_separation.md) |"
    branch79 = "| Certified sampling-radius envelope | P79 | Supplies an exact-rational upper bound for the P77 sampling radius so the P78 rejection comparison has certified numerical direction | [P79](proposition_79_certified_sampling_radius.md) |"
    if branch79 not in text and branch78 in text:
        text = text.replace(branch78, branch78 + "\n" + branch79, 1)
    row78 = "| P78 | [Certified continuous model separation](proposition_78_certified_continuous_model_separation.md) | certified global distance lower bound for the continuous P75 family |"
    row79 = "| P79 | [Certified rational sampling-radius envelope](proposition_79_certified_sampling_radius.md) | exact-rational one-sided certification of the P77 sampling radius |"
    if row79 not in text and row78 in text:
        text = text.replace(row78, row78 + "\n" + row79, 1)
    write(path, text)


def update_detail() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    if "Complete P1 to P79 chronology" not in text:
        text = text.replace("# Detailed proposition record", "# Detailed proposition record\n\n## Complete P1 to P79 chronology", 1)
    p79 = """

## Proposition 79: Certified Rational Sampling-Radius Envelope

**P79** closes the numerical-direction gap in the P77/P78 rejection handoff. P78 supplies a certified lower bound on empirical distance to the complete continuous P75 model family. P79 supplies a mathematically valid exact-rational upper envelope for the P77 sampling radius by combining rational logarithm brackets with an integer-certified dyadic square-root enclosure. A strict lower-bound versus upper-bound comparison can therefore certify rejection without assuming the direction of floating-point rounding.

Proof: [Proposition 79](proposition_79_certified_sampling_radius.md). Provenance: [P79 equation record](p79_equation_provenance.md). Figure: [P79 theorem figure](figures/p79_certified_sampling_radius.svg). Implementation: [`certified_sampling_radius.py`](../src/consciousness_bridge/certified_sampling_radius.py). Tests: [`test_certified_sampling_radius.py`](../tests/test_certified_sampling_radius.py).

P79 does not validate non-rejected models and does not close the physical-to-experiential bridge.
"""
    if "## Proposition 79: Certified Rational Sampling-Radius Envelope" not in text:
        text += p79
    write(path, text)


def update_equation_map() -> None:
    path = "docs/equation_and_citation_map.md"
    text = read(path)
    p79 = r'''

# P79 certified rational sampling-radius envelope

| Object | Equation or certificate | Provenance | Direct route |
| --- | --- | --- | --- |
| P77 sampling radius | $\varepsilon_{n,K}(\alpha)=\sqrt{\log(2K/\alpha)/(2n)}$ | Standard finite-alphabet concentration quantity inherited from P77 | [P77](proposition_77_full_law_model_set_separation.md) |
| Rational logarithm bracket | $\underline L_m(x)\le\log x\le\overline L_m(x)$ | Positive atanh series with explicit rational tail after exact power-of-two reduction | [P79 provenance](p79_equation_provenance.md) |
| Dyadic square-root bracket | $\underline\varepsilon\le\varepsilon\le\overline\varepsilon$ | Integer comparison on a power-of-two denominator | [P79 proof](proposition_79_certified_sampling_radius.md) |
| Certified rejection handoff | $L_{\mathrm{model}}>\overline\varepsilon$ | P78 lower-bounds model distance; P79 upper-bounds sampling uncertainty | [P79 figure](figures/p79_certified_sampling_radius.svg) |
| Executable certificate | exact `Fraction` arithmetic | Repository implementation and regression tests | [`certified_sampling_radius.py`](../src/consciousness_bridge/certified_sampling_radius.py), [`tests`](../tests/test_certified_sampling_radius.py) |

Scientific boundary: P79 closes a numerical certification gap only. It does not identify a latent state with consciousness and does not solve the physical-to-experiential bridge.
'''
    if "# P79 certified rational sampling-radius envelope" not in text:
        text += p79
    write(path, text)


def update_citations() -> None:
    path = "CITATION.cff"
    text = read(path)
    text = replace(text, "version: 0.78.0", "version: 0.79.0")
    text = replace(text, "date-released: 2026-09-10", "date-released: 2026-09-11")
    text = replace(text, "Current documented theorem frontier: P78", "Current documented theorem frontier: P79")
    text = replace(text, "Version 0.78.0.", "Version 0.79.0.")
    if "Proposition 79 adds an exact-rational" not in text:
        text = text.replace("P78 preserves the P77 requirement that only a valid lower bound, not an ordinary best-fit upper bound, can certify full-law separation.", "P78 preserves the P77 requirement that only a valid lower bound, not an ordinary best-fit upper bound, can certify full-law separation. Proposition 79 adds an exact-rational upper certificate for the P77 sampling radius using rational logarithm bracketing and integer-certified dyadic square-root enclosure, making the final P78/P79 comparison one-sided and rounding-direction safe.")
    write(path, text)

    path = "CITATION.bib"
    text = read(path)
    text = replace(text, "version      = {0.78.0}", "version      = {0.79.0}")
    text = replace(text, "Current documented theorem frontier: P78.", "Current documented theorem frontier: P79.")
    write(path, text)

    path = "CITATION.md"
    text = read(path)
    text = replace(text, "0.78.0", "0.79.0")
    text = replace(text, "P78", "P79") if "Current documented theorem frontier: P78" in text else text
    if "Proposition 79" not in text:
        text += "\n\n## Proposition 79\n\nFor the exact-rational sampling-radius certificate, cite the repository together with [Proposition 79](docs/proposition_79_certified_sampling_radius.md) and its [equation provenance record](docs/p79_equation_provenance.md).\n"
    write(path, text)


def update_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    entry = """# 0.79.0 - 2026-09-11

- Added Proposition 79, Certified Rational Sampling-Radius Envelope.
- Added exact-rational logarithm bracketing and integer-certified dyadic square-root enclosure for the P77 finite-alphabet sampling radius.
- Completed the directionally safe P77/P78/P79 rejection handoff: P78 lower-bounds model distance and P79 upper-bounds sampling uncertainty.
- Added the P79 theorem figure, proof, provenance record, implementation, tests, public navigation, website integration, and release metadata.
- Preserved the scientific boundary that non-rejection is not model acceptance and the physical-to-experiential bridge remains open.

"""
    if "# 0.79.0 - 2026-09-11" not in text:
        text = entry + text
    write(path, text)


def update_website() -> None:
    path = "website/index.html"
    text = read(path)
    text = replace(text, "<strong>78</strong><span>proposition-level results</span>", "<strong>79</strong><span>proposition-level results</span>")
    text = replace(text, "<strong>v0.78.0</strong>", "<strong>v0.79.0</strong>")
    text = replace(text, "P71-P78", "P71-P79")
    text = replace(text, "See all 78 results grouped by scientific role", "See all 79 results grouped by scientific role")
    if "p79_certified_sampling_radius.svg" not in text:
        card = '''
      <div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p79_certified_sampling_radius.svg" alt="P79 certified rational sampling-radius envelope"/><div><h3>P79: Certified rational sampling-radius envelope</h3><p>P79 gives an exact-rational upper certificate for the P77 sampling radius, complementing P78's certified lower bound on continuous model distance. Rejection requires the strict lower-bound versus upper-bound comparison; failure to reject remains inconclusive.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_79_certified_sampling_radius.md">Read Proposition 79 -></a></div></div>
'''
        text = insert_before(text, "\n    <section id=\"falsification\"", card)
    write(path, text)

    path = "website/research-map.html"
    text = read(path)
    text = replace(text, "Seventy-six results", "Seventy-nine results")
    text = replace(text, "<strong>76</strong><span>proposition-level results</span>", "<strong>79</strong><span>proposition-level results</span>")
    text = replace(text, "P71-P78", "P71-P79")
    p79 = '''
<section><div class="section-head"><p class="eyebrow">IV-I · Certified sampling radius</p><h2>P79: Certified rational sampling-radius envelope</h2></div><div class="result-grid"><article class="result"><span>P79</span><h3>One-sided numerical certification</h3><p>Exact-rational logarithm brackets and integer-certified dyadic square-root bounds produce a valid upper envelope for the P77 sampling radius. The P78/P79 rejection handoff compares a model-distance lower bound with a sampling-radius upper bound.</p></article></div><div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p79_certified_sampling_radius.svg" alt="P79 certified rational sampling-radius envelope"/><div><h3>P79 numerical certificate</h3><p>Rounding direction is explicit, and non-rejection remains inconclusive.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_79_certified_sampling_radius.md">Read Proposition 79 -></a></div></div></section>

'''
    if "P79: Certified rational sampling-radius envelope" not in text:
        text = insert_before(text, "<section><div class=\"section-head\"><p class=\"eyebrow\">V · Operational scale consistency", p79)
    write(path, text)

    path = "website/visual-atlas.html"
    text = read(path)
    if "p79_certified_sampling_radius.svg" not in text:
        card = '''
    <section class="figure-card">
      <img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p79_certified_sampling_radius.svg" alt="P79 certified rational sampling-radius envelope" />
      <div>
        <p class="eyebrow">P79</p>
        <h2>Certified Rational Sampling-Radius Envelope</h2>
        <p>The figure shows the exact-rational upper side of the P77/P78/P79 rejection chain: logarithm enclosure, integer-certified dyadic square-root enclosure, and the strict comparison with the P78 model-distance lower bound.</p>
        <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_79_certified_sampling_radius.md">Open the P79 proof</a>
      </div>
    </section>

'''
        text = insert_before(text, "</main>", card)
    write(path, text)


def update_p78_history_test() -> None:
    path = "tests/test_p78_research_integration.py"
    text = read(path)
    pattern = re.compile(r"def test_p78_release_metadata_and_counts_are_consistent\(\) -> None:\n.*?\n\ndef test_p78_certification_boundary_is_preserved", re.S)
    replacement = '''def test_p78_release_history_is_preserved_after_later_frontiers() -> None:
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")

    assert "# 0.78.0 - 2026-09-10" in changelog
    assert "Proposition 78" in changelog
    assert "## 1.12 P78: certified continuous separation for the P75 model family" in readme
    assert "| [P78]" in roadmap


def test_p78_certification_boundary_is_preserved'''
    text, count = pattern.subn(replacement, text, count=1)
    if count != 1 and "test_p78_release_history_is_preserved_after_later_frontiers" not in text:
        raise RuntimeError("could not update P78 historical release test")
    write(path, text)


def cleanup_temporary_workflow() -> None:
    workflow = ROOT / ".github" / "workflows" / "p79-reader-publication-integration.yml"
    if workflow.exists():
        workflow.unlink()


def main() -> None:
    update_readme()
    update_roadmap()
    update_navigation()
    update_detail()
    update_equation_map()
    update_citations()
    update_changelog()
    update_website()
    update_p78_history_test()
    cleanup_temporary_workflow()


if __name__ == "__main__":
    main()
