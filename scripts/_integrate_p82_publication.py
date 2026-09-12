"""One-time helper to synchronize reader-facing surfaces with the P82 frontier."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace(path: str, old: str, new: str) -> None:
    text = read(path)
    if old in text:
        text = text.replace(old, new)
        write(path, text)


def insert_once(path: str, marker: str, insertion: str, guard: str) -> None:
    text = read(path)
    if guard in text:
        return
    if marker not in text:
        raise RuntimeError(f"marker not found in {path}: {marker[:80]!r}")
    text = text.replace(marker, marker + insertion, 1)
    write(path, text)


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    replacements = {
        "P1-P81 program map": "P1-P82 program map",
        "current P81 frontier": "current P82 frontier",
        "P1-P81": "P1-P82",
        "P1 through P81": "P1 through P82",
        "P71-P81": "P71-P82",
        "P73-P81": "P73-P82",
        "P74-P81": "P74-P82",
        "P75-P81": "P75-P82",
        "81 proposition-level results": "82 proposition-level results",
        "69 equation-driven quantitative figures": "70 equation-driven quantitative figures",
        "The theorem frontier is P81.": "The theorem frontier is P82.",
        "| Equation-driven quantitative figures | **69** |": "| Equation-driven quantitative figures | **70** |",
        "Later P61-P70 and P71-P81": "Later P61-P70 and P71-P82",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    if "P82 asks what nested projected events can reveal" not in text:
        marker = (
            "P81 asks what P80 still leaves out. A P75 parameter box can force exact probabilities "
            "for one-view marginals and higher-order projected events even when every individual "
            "sixteen-cell interval, together with normalization, still overlaps the empirical law. "
            "P81 computes the exact rational interval for every nonempty projected binary event and "
            "converts any event mismatch into a lower bound on the full sixteen-cell L-infinity "
            "distance. The combined P81 certificate is never weaker than P80 and can be strictly "
            "stronger. This remains a test of the declared target-measurement model, not an "
            "identification of a latent state with consciousness.\n"
        )
        addition = (
            "\nP82 asks what nested projected events can reveal that separate P81 event tests still "
            "discard. For a parent cylinder and a stricter child cylinder, their difference is a "
            "generally non-cylinder residual event. Under the declared P75 conditional-independence "
            "model, P82 derives the exact parameter-box range of that residual directly from disjoint "
            "parent and added-view response coordinates, rather than conservatively subtracting two "
            "separate event intervals. The resulting certificate retains all of P81 and adds 256 "
            "genuinely new nested contrasts. An exact-rational witness gives P80 = 0, P81 = 1/16, "
            "and P82 = 1/12. This is a stronger model-distance certificate, not evidence that the "
            "latent state is consciousness.\n"
        )
        if marker not in text:
            raise RuntimeError("P81 plain-language marker not found in README")
        text = text.replace(marker, marker + addition, 1)

    if "[P82](docs/proposition_82_exact_nested_projection_contrast.md)" not in text:
        anchor = "[P81](docs/proposition_81_projection_event_model_separation.md)"
        if anchor in text:
            text = text.replace(
                anchor,
                anchor + " and [P82](docs/proposition_82_exact_nested_projection_contrast.md)",
                1,
            )

    write(path, text)


def update_start_here() -> None:
    path = "START_HERE.md"
    text = read(path)
    for old, new in (
        ("P1-P81", "P1-P82"),
        ("P1 through P81", "P1 through P82"),
        ("P71-P81", "P71-P82"),
        ("P75-P81", "P75-P82"),
        ("current P81 frontier", "current P82 frontier"),
        ("frontier is P81", "frontier is P82"),
    ):
        text = text.replace(old, new)
    if "proposition_82_exact_nested_projection_contrast.md" not in text:
        text += (
            "\n## Current theorem frontier: P82\n\n"
            "[P82: Exact Nested Projection-Contrast Certificate](docs/proposition_82_exact_nested_projection_contrast.md) "
            "strengthens P81 by computing exact P75 parameter-box ranges for non-cylinder residual events "
            "formed from nested projected cylinders. It preserves the one-sided model-rejection logic and "
            "does not identify any latent state with consciousness.\n"
        )
    write(path, text)


def update_detailed_record() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    text = text.replace("Complete P1 to P81 chronology", "Complete P1 to P82 chronology")
    text = text.replace("P1-P81", "P1-P82")
    text = text.replace("P71-P81", "P71-P82")
    if "**P82** strengthens P81" not in text:
        marker = "**P81** strengthens P80"
        index = text.find(marker)
        if index < 0:
            raise RuntimeError("P81 chronology marker missing")
        paragraph_end = text.find("\n\n", index)
        if paragraph_end < 0:
            paragraph_end = len(text)
        addition = (
            "\n\n**P82** strengthens P81 by retaining exact structure from nested projected events. "
            "For a parent cylinder A and strict child B, it computes the exact P75 parameter-box interval "
            "of the generally non-cylinder residual A\\B directly from the branchwise factorization "
            "P_s(A\\B)=P_s(A)[1-P_s(D)]. Because parent and added-view factors use disjoint response "
            "coordinates, the residual box extrema are jointly attainable and prevalence is handled by "
            "affine endpoint evaluation. P82 audits 256 genuinely new nested contrasts, satisfies "
            "L82 >= L81 >= L80 >= L78, and has an exact-rational strict witness with L80=0, "
            "L81=1/16, and L82=1/12. The P78 mesh-width upper certificate and P79 one-sided sampling "
            "handoff are retained unchanged.\n"
        )
        text = text[:paragraph_end] + addition + text[paragraph_end:]
    write(path, text)


def update_theorem_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = text.replace("current documented theorem frontier is **P81**", "current documented theorem frontier is **P82**")
    text = text.replace("P1 through P81 with explicit dependency branches", "P1 through P82 with explicit dependency branches")
    text = text.replace("P71-P81 return", "P71-P82 return")
    text = text.replace("None of P71-P81", "None of P71-P82")
    text = text.replace("After P81,", "After P82,")
    if "P82: exact nested residual-event constraints" not in text:
        old = "&\\text{P81: projected-event constraints tighten the same certified model-distance lower bound}\n\\end{aligned}"
        new = (
            "&\\text{P81: projected-event constraints tighten the same certified model-distance lower bound}\\\\\n"
            "&\\Downarrow\\\\\n"
            "&\\text{P82: exact nested residual-event constraints tighten P81 while preserving certification}\n"
            "\\end{aligned}"
        )
        if old not in text:
            raise RuntimeError("P81 roadmap equation marker missing")
        text = text.replace(old, new, 1)
    if "### P82: exact nested projection-contrast certificate" not in text:
        marker = (
            "| [P81](proposition_81_projection_event_model_separation.md) | P75, P77, P78, P79, P80 | "
            "Exact projection-event intervals, event-size distance transfer, P81 >= P80 dominance, and strict-improvement witness |\n"
        )
        addition = (
            "\n### P82: exact nested projection-contrast certificate\n\n"
            "[P82](proposition_82_exact_nested_projection_contrast.md) retains every P81 lower bound and adds "
            "exact residual-event constraints from nested cylinder pairs. The direct residual extremization can "
            "be strictly tighter than subtracting the separate P81 intervals because it preserves the shared "
            "P75 parameter structure.\n\n"
            "| Result | Depends on | Adds |\n| --- | --- | --- |\n"
            "| [P82](proposition_82_exact_nested_projection_contrast.md) | P75, P77, P78, P79, P80, P81 | "
            "Exact nested-residual intervals, 256 new contrasts, P82 >= P81 dominance, and a strict 1/12 versus 1/16 witness |\n"
        )
        if marker not in text:
            raise RuntimeError("P81 roadmap table marker missing")
        text = text.replace(marker, marker + addition, 1)
    if "| [P82](proposition_82_exact_nested_projection_contrast.md) |" not in text[text.find("## 3. Complete proposition index"):]:
        p81_row = (
            "| [P81](proposition_81_projection_event_model_separation.md) | exact projected-event box intervals and event-size distance transfer | "
            "never-weaker projection-aware continuous P75 model separation | proved conditional computational theorem |"
        )
        p82_row = (
            "| [P82](proposition_82_exact_nested_projection_contrast.md) | exact nested residual-event box intervals and event-size distance transfer | "
            "never-weaker nested-contrast continuous P75 model separation | proved conditional computational theorem |"
        )
        if p81_row not in text:
            raise RuntimeError("P81 proposition-index row missing")
        text = text.replace(p81_row, p81_row + "\n" + p82_row, 1)
    text = text.replace(
        "P81 strengthens it again by retaining exact marginal and projected-event constraints implied by each parameter box.",
        "P81 strengthens it again by retaining exact marginal and projected-event constraints implied by each parameter box. "
        "P82 then adds exact non-cylinder residual constraints from nested projected events, retaining common-parameter structure that separate event intervals discard.",
    )
    text = text.replace(
        "A substantive continuation would retain **simultaneous dependence among overlapping projected events** or introduce a demonstrably tighter convex or semialgebraic relaxation while preserving exact certification.",
        "A substantive continuation beyond P82 would retain broader **simultaneous dependence among multiple overlapping events** or introduce a demonstrably tighter exact-rational convex or semialgebraic relaxation while preserving the certified lower-bound direction.",
    )
    write(path, text)


def update_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    text = text.replace("frontier is **P81**", "frontier is **P82**")
    text = text.replace("P1 through P81", "P1 through P82")
    text = text.replace("P71-P81 form", "P71-P82 form")
    text = text.replace("from P1 through P81", "from P1 through P82")
    if "[P82 exact nested projection-contrast separation]" not in text:
        marker = (
            "17. [P81 projection-event continuous P75 separation](proposition_81_projection_event_model_separation.md) "
            "for exact projected-event box intervals, event-size distance transfer, P81 >= P80 dominance, and the strict-improvement witness.\n"
        )
        addition = (
            "18. [P82 exact nested projection-contrast separation](proposition_82_exact_nested_projection_contrast.md) "
            "for exact nested residual-event box intervals, the 256-contrast audit, P82 >= P81 dominance, and the strict 1/12 versus 1/16 witness.\n"
        )
        if marker not in text:
            raise RuntimeError("P81 navigation reading-order marker missing")
        text = text.replace(marker, marker + addition, 1)
        # Keep following numbering human-readable.
        for number in range(30, 17, -1):
            text = text.replace(f"\n{number}. ", f"\n{number + 1}. ", 1)
    if "| Nested projection-contrast continuous target-model separation | P82 |" not in text:
        marker = (
            "| Projection-event continuous target-model separation | P81 | Adds exact parameter-box ranges for every nonempty projected binary event and transfers event mismatch into a never-weaker full-law distance certificate | [P81](proposition_81_projection_event_model_separation.md) |"
        )
        addition = (
            "\n| Nested projection-contrast continuous target-model separation | P82 | Adds exact residual-event ranges for nested projected cylinders and retains common-parameter structure beyond separate P81 event tests | [P82](proposition_82_exact_nested_projection_contrast.md) |"
        )
        if marker not in text:
            raise RuntimeError("P81 navigation branch-map marker missing")
        text = text.replace(marker, marker + addition, 1)
    if "| P82 | [Exact nested projection-contrast certificate]" not in text:
        p81 = "| P81 | [Projection-event model separation](proposition_81_projection_event_model_separation.md) | exact projected-event box constraints and full-law distance transfer |"
        p82 = "| P82 | [Exact nested projection-contrast certificate](proposition_82_exact_nested_projection_contrast.md) | exact non-cylinder residual-event constraints from nested projections |"
        if p81 not in text:
            # tolerate wording variation by inserting immediately before the next heading
            marker = "\n## "
            pos = text.rfind(marker)
            if pos < 0:
                raise RuntimeError("could not place P82 complete-index row")
            text = text[:pos] + "\n" + p82 + "\n" + text[pos:]
        else:
            text = text.replace(p81, p81 + "\n" + p82, 1)
    write(path, text)


def update_citations() -> None:
    cff = read("CITATION.cff")
    cff = cff.replace("Current documented theorem frontier: P81", "Current documented theorem frontier: P82")
    if "Proposition 82 adds exact nested projection-contrast" not in cff:
        marker = "The downstream calibration branch includes lower-bounded heterogeneous calibration"
        addition = (
            "Proposition 82 adds exact nested projection-contrast residual intervals for the same P75 family, "
            "audits 256 genuinely new residual events, and yields a never-weaker certificate with an exact-rational "
            "strict witness improving P81 from one sixteenth to one twelfth. "
        )
        if marker not in cff:
            raise RuntimeError("CFF abstract marker missing")
        cff = cff.replace(marker, addition + marker, 1)
    write("CITATION.cff", cff)

    guide = read("CITATION.md")
    guide = guide.replace("P81", "P82", 1) if "Current documented theorem frontier: P81" in guide else guide
    if "P82" not in guide:
        guide += (
            "\n## P82 frontier citation note\n\nP82 is the Exact Nested Projection-Contrast Certificate for Continuous P75 Separation. "
            "It strengthens P81 through exact residual-event box intervals and should be cited as a conditional "
            "computational model-distance theorem, not as an identification of consciousness.\n"
        )
    else:
        guide += (
            "\n## P82 frontier citation note\n\nP82 strengthens the P81 continuous P75 separation chain through exact nested residual-event intervals. "
            "It is a conditional model-distance certificate and should not be cited as an identification of consciousness.\n"
        ) if "P82 frontier citation note" not in guide else ""
    write("CITATION.md", guide)

    bib = read("CITATION.bib")
    if "P82" not in bib:
        bib = bib.replace(
            "note         = {",
            "note         = {Current documented theorem frontier: P82. ",
            1,
        )
    write("CITATION.bib", bib)


def update_website() -> None:
    path = "website/index.html"
    text = read(path)
    replacements = {
        "81-result": "82-result",
        "Explore all 81 results": "Explore all 82 results",
        "<strong>81</strong><span>proposition-level results</span>": "<strong>82</strong><span>proposition-level results</span>",
        "<strong>P81</strong><span>current theorem frontier</span>": "<strong>P82</strong><span>current theorem frontier</span>",
        "81 proposition-level results through P81": "82 proposition-level results through P82",
        "P73-P81": "P73-P82",
        "The 81 results": "The 82 results",
        "read 81 proofs": "read 82 proofs",
        "P71-P81": "P71-P82",
        "P74-P81": "P74-P82",
        "The 81-result program": "The 82-result program",
        "P75-P81": "P75-P82",
        "P75-P81 test": "P75-P82 test",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    if "p82_exact_nested_projection_contrast.svg" not in text:
        marker = (
            "      <div class=\"figure-card\">\n"
            "        <img src=\"https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p81_projection_event_model_separation.svg\" alt=\"P81 projection-event model separation certificate\" />\n"
            "        <div><h3>P81 · Projected-event coupling</h3><p>Marginals and higher-order projected events impose exact box constraints not visible in independent full-cell intervals. Their mismatch is transferred back into a certified full-law L-infinity lower bound. A strict witness shows P81 can be stronger than P80.</p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_81_projection_event_model_separation.md\">Read P81 →</a></div>\n"
            "      </div>\n"
        )
        addition = (
            "\n      <div class=\"figure-card\">\n"
            "        <img src=\"https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p82_exact_nested_projection_contrast.svg\" alt=\"P82 exact nested projection-contrast certificate\" />\n"
            "        <div><h3>P82 · Exact nested projection contrasts</h3><p>Nested parent-child projected events define residual events that are generally not cylinders. P82 computes their P75 parameter-box ranges exactly, audits 256 genuinely new contrasts, and has an exact witness improving the P81 lower bound from 1/16 to 1/12.</p><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_82_exact_nested_projection_contrast.md\">Read P82 →</a></div>\n"
            "      </div>\n"
        )
        if marker not in text:
            raise RuntimeError("P81 homepage figure marker missing")
        text = text.replace(marker, marker + addition, 1)
    write(path, text)

    path = "website/research-map.html"
    text = read(path)
    text = text.replace("P71-P81", "P71-P82")
    text = text.replace("P75-P81", "P75-P82")
    if "P82" not in text:
        raise RuntimeError("unexpected research map without any P81 frontier marker")
    if "Exact nested projection-contrast" not in text:
        marker = "P81"
        pos = text.rfind(marker)
        if pos < 0:
            raise RuntimeError("P81 missing from research map")
        paragraph_end = text.find("</", pos)
        block = (
            "<p><strong>P82: Exact nested projection-contrast certificate.</strong> Nested cylinder residual events "
            "retain shared P75 parameter structure that separate P81 event intervals can discard. The exact-rational "
            "certificate audits 256 new contrasts and strictly improves P81 on a concrete witness.</p>"
        )
        text = text[: paragraph_end + 4] + block + text[paragraph_end + 4 :]
    write(path, text)


def update_frontier_helpers() -> None:
    for path in (
        "docs/equation_and_citation_map.md",
        "figures/CURRENT_FRONTIER.md",
    ):
        if not (ROOT / path).exists():
            continue
        text = read(path)
        text = text.replace("P1-P81", "P1-P82")
        text = text.replace("P1 through P81", "P1 through P82")
        text = text.replace("P71-P81", "P71-P82")
        text = text.replace("frontier is P81", "frontier is P82")
        text = text.replace("frontier: P81", "frontier: P82")
        if path.endswith("equation_and_citation_map.md") and "p82_equation_provenance.md" not in text:
            text += (
                "\n## P82 exact nested projection-contrast certificate\n\n"
                "Formal theorem: [P82](proposition_82_exact_nested_projection_contrast.md). "
                "Equation provenance: [P82 equation record](p82_equation_provenance.md). "
                "Implementation: [`nested_projection_contrast_separation.py`](../src/consciousness_bridge/nested_projection_contrast_separation.py).\n"
            )
        write(path, text)


def update_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    if "P82 exact nested projection-contrast" not in text:
        marker = "# Changelog\n"
        entry = (
            "\n## Unreleased - P82 exact nested projection-contrast certificate\n\n"
            "- Added exact P75 parameter-box intervals for nested residual events A\\B.\n"
            "- Added 256 genuinely new nested projection contrasts and P82 >= P81 dominance.\n"
            "- Added an exact-rational strict witness with P80=0, P81=1/16, and P82=1/12.\n"
            "- Added the P82 proof, equation-provenance record, theorem figure, and regression tests.\n"
            "- Retained the P78 mesh-width upper certificate and P79 one-sided sampling-radius handoff.\n"
        )
        if marker not in text:
            raise RuntimeError("CHANGELOG heading missing")
        text = text.replace(marker, marker + entry, 1)
    write(path, text)


def update_test_wording() -> None:
    path = "tests/test_nested_projection_contrast_separation.py"
    text = read(path)
    text = text.replace('"does not validate",', '"not validate",')
    write(path, text)


def main() -> None:
    update_readme()
    update_start_here()
    update_detailed_record()
    update_theorem_roadmap()
    update_navigation()
    update_citations()
    update_website()
    update_frontier_helpers()
    update_changelog()
    update_test_wording()
    print("P82 reader/publication surfaces synchronized")


if __name__ == "__main__":
    main()
