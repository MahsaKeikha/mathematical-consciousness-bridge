from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, *, label: str) -> str:
    if old not in text:
        raise AssertionError(f"missing marker for {label}: {old[:120]!r}")
    return text.replace(old, new, 1)


def update_readme() -> None:
    path = "README.md"
    text = read(path)
    if "**First time here?**" not in text:
        marker = "**Mahsa Keikha, PhD**\n\n"
        block = (
            "**Mahsa Keikha, PhD**\n\n"
            "> [!TIP]\n"
            "> **First time here?** Begin with **[START_HERE.md](START_HERE.md)** "
            "for a short orientation, audience-specific reading paths, the P1-P81 "
            "program map, and the current P81 frontier. Keep the "
            "**[Glossary](docs/glossary.md)** open for terminology, and use the "
            "**[Reproducibility Guide](docs/reproducibility.md)** when you want to "
            "run the tests or regenerate the computational figure atlases.\n\n"
        )
        text = replace_once(text, marker, block, label="README reader entry")
    write(path, text)


def update_research_navigation() -> None:
    path = "docs/research_navigation.md"
    text = read(path)
    old = (
        "This page is the reading and reference index for the **Mathematical "
        "Consciousness Bridge** repository. It is organized by scientific dependency "
        "rather than by development chronology so that a reader can move from the "
        "research question to proofs, figures, code, falsification conditions, and "
        "citation resources without searching through the repository manually.\n\n"
        "The current documented theorem frontier is **P80**. The complete proposition "
        "record runs from **P1 through P81**. P71-P80 form a target-side methodology "
        "branch descending from the P19 physical-sufficiency question. They are not "
        "extensions of the P61-P70 calibration branch."
    )
    new = (
        "This page is the reading and reference index for the **Mathematical "
        "Consciousness Bridge** repository. It is organized by scientific dependency "
        "rather than by development chronology so that a reader can move from the "
        "research question to proofs, figures, code, falsification conditions, and "
        "citation resources without searching through the repository manually.\n\n"
        "**First-time reader:** begin with [Start Here](../START_HERE.md) for the "
        "shortest orientation, keep the [Glossary and Reader Vocabulary](glossary.md) "
        "nearby for terminology, and use the [Reproducibility Guide](reproducibility.md) "
        "when you want to run the code, tests, or generated figure atlases.\n\n"
        "The current documented theorem frontier is **P81**. The complete proposition "
        "record runs from **P1 through P81**. P71-P81 form a target-side methodology "
        "branch descending from the P19 physical-sufficiency question. They are not "
        "extensions of the P61-P70 calibration branch."
    )
    if "frontier is **P80**" in text:
        text = replace_once(text, old, new, label="navigation frontier")

    section_start = text.index("## Recommended reading order")
    section_end = text.index("## Scientific branch map")
    before = text[:section_start]
    section = text[section_start:section_end]
    after = text[section_end:]
    lines = section.splitlines()
    items: list[str] = []
    header: list[str] = []
    started = False
    for line in lines:
        match = re.match(r"^(\d+)\.\s+(.*)$", line)
        if match:
            started = True
            items.append(match.group(2))
        elif not started:
            header.append(line)
    if not any("P81 projection-event" in item for item in items):
        insertion = next(
            i + 1 for i, item in enumerate(items) if "P80 simplex-coupled" in item
        )
        items.insert(
            insertion,
            "[P81 projection-event continuous P75 separation]"
            "(proposition_81_projection_event_model_separation.md) for exact "
            "projected-event box intervals, event-size distance transfer, P81 >= P80 "
            "dominance, and the strict-improvement witness.",
        )
    rebuilt = "\n".join(header).rstrip() + "\n\n"
    rebuilt += "\n".join(f"{index}. {item}" for index, item in enumerate(items, 1))
    rebuilt += "\n\n"
    text = before + rebuilt + after

    p80_row = (
        "| Simplex-coupled continuous target-model separation | P80 | Tightens each "
        "P78 box lower bound by intersecting exact cell intervals with probability "
        "normalization while preserving the global lower-bound direction | "
        "[P80](proposition_80_simplex_coupled_model_separation.md) |"
    )
    p81_row = (
        "| Projection-event continuous target-model separation | P81 | Adds exact "
        "parameter-box ranges for every nonempty projected binary event and transfers "
        "event mismatch into a never-weaker full-law distance certificate | "
        "[P81](proposition_81_projection_event_model_separation.md) |"
    )
    if p81_row not in text:
        text = replace_once(
            text,
            p80_row,
            p80_row + "\n" + p81_row,
            label="navigation P81 branch row",
        )
    write(path, text)


def update_theorem_roadmap() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = text.replace(
        "The current documented theorem frontier is **P80**. The proposition record "
        "runs from **P1 through P81 with explicit dependency branches**. P71-P80 return "
        "to the core P19 bridge-sufficiency lineage; they do not extend the P61-P70 "
        "calibration branch.",
        "The current documented theorem frontier is **P81**. The proposition record "
        "runs from **P1 through P81 with explicit dependency branches**. P71-P81 return "
        "to the core P19 bridge-sufficiency lineage; they do not extend the P61-P70 "
        "calibration branch.",
        1,
    )
    p80_map = (
        "&\\text{P80: probability-simplex coupling tightens the continuous-family "
        "box certificate}"
    )
    if "P81: projected-event constraints" not in text and p80_map in text:
        text = text.replace(
            p80_map,
            p80_map
            + "\\\\\n&\\Downarrow\\\\\n"
            + "&\\text{P81: projected-event constraints tighten the same certified "
            "model-distance lower bound}",
            1,
        )
    text = text.replace(
        "The proposition number records development order. It does not imply that P80 "
        "depends on P70. P80 depends scientifically on P78's continuous-family "
        "certificate and uses the P79 one-sided sampling-radius handoff; both descend "
        "from P77, the P75 continuous target-model family, P19, and the P71-P76 "
        "target-side lineage.",
        "The proposition number records development order. It does not imply that P81 "
        "depends on P70. P81 strengthens P80's box certificate, uses P78's "
        "continuous-family construction and the P79 one-sided sampling-radius handoff, "
        "and ultimately descends from P77, the P75 continuous target-model family, "
        "P19, and the P71-P76 target-side lineage.",
        1,
    )

    match = re.search(
        r"\n### P81: projection-event continuous-family certificate\n(?P<body>.*)\Z",
        text,
        flags=re.S,
    )
    if match:
        p81_body = match.group("body").strip()
        text = text[: match.start()].rstrip() + "\n"
        p81_section = (
            "### P81: projection-event continuous-family certificate\n\n"
            + p81_body
            + "\n\n"
        )
        text = text.replace(
            "\n## 3. Complete proposition index\n",
            "\n" + p81_section + "## 3. Complete proposition index\n",
            1,
        )

    p80_index = (
        "| [P80](proposition_80_simplex_coupled_model_separation.md) | "
        "probability-simplex interval relaxation and exact rational feasibility "
        "crossings | tighter certified continuous P75 full-law model separation | "
        "proved conditional computational theorem |"
    )
    p81_index = (
        "| [P81](proposition_81_projection_event_model_separation.md) | exact "
        "projected-event box intervals and event-size distance transfer | never-weaker "
        "projection-aware continuous P75 model separation | proved conditional "
        "computational theorem |"
    )
    if p81_index not in text:
        text = replace_once(
            text,
            p80_index,
            p80_index + "\n" + p81_index,
            label="roadmap P81 index",
        )

    open_frontier = """## 5. Current open frontier

After P81, the target-side chain has a substantially clearer scientific burden:

1. target provenance must be non-circular relative to the physical descriptor being tested;
2. the target-observation channel must be scientifically defensible and sufficiently informative for the claimed witness;
3. channel reliability must be identified or externally calibrated under a declared measurement model;
4. finite data must resolve the channel far enough from singularity for recovery to be certified;
5. the target-measurement model must survive adequacy tests rather than being accepted because it can be fit;
6. finite data must separate genuine adequacy failure from sampling noise before rejection is claimed;
7. full-law rejection must be defined against the complete declared model family;
8. continuous-family separation must use a certified global lower bound rather than a local optimizer value;
9. the sampling-radius side of the rejection gate must have a certified upper direction; and
10. computational relaxations should retain as much exact probability structure as possible without invalidating the lower-bound direction.

P78 closes the global-lower-bound gap for the specific continuous P75 four-view binary latent family. P79 certifies the one-sided sampling-radius envelope. P80 strengthens the box relaxation by retaining probability normalization. P81 strengthens it again by retaining exact marginal and projected-event constraints implied by each parameter box.

The next computational question is therefore not another cosmetic bound. A substantive continuation would retain **simultaneous dependence among overlapping projected events** or introduce a demonstrably tighter convex or semialgebraic relaxation while preserving exact certification. Statistical extensions remain open as well, including sharper power analysis and target-view models with residual dependence, shared bias, temporal drift, or learned measurement pipelines.

None of P71-P81 identifies a latent variable with consciousness. None proves that a failed descriptor implies nonphysical consciousness. The physical-to-experiential bridge remains open.
"""
    text = re.sub(r"## 5\. Current open frontier\n.*\Z", open_frontier, text, flags=re.S)
    write(path, text)


def update_detailed_record() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    text = text.replace("## Complete P1 to P78 chronology", "## Complete P1 to P81 chronology", 1)
    text = text.replace("- P71-P78 return to the target side", "- P71-P81 return to the target side", 1)
    text = text.replace(
        "### P81: projection-event continuous-family certificate",
        "## Proposition 81: Projection-Event Certificate for Continuous P75 Separation",
        1,
    )

    sci_marker = "## Scientific interpretation of the chronology"
    p79_marker = "## Proposition 79: Certified Rational Sampling-Radius Envelope"
    if sci_marker in text and p79_marker in text and text.index(sci_marker) < text.index(p79_marker):
        prefix, rest = text.split(sci_marker, 1)
        interpretation, late = rest.split(p79_marker, 1)
        late_block = p79_marker + late
        interpretation_block = sci_marker + interpretation
        text = (
            prefix.rstrip()
            + "\n\n"
            + late_block.rstrip()
            + "\n\n---\n\n"
            + interpretation_block.lstrip()
        )

    text = text.replace(
        "P76 adds a finite-sample rejection layer for a tracked family of necessary P75 "
        "polynomial constraints. Its non-rejection output is explicitly inconclusive. "
        "P77 then defines the stronger finite-sample full-law criterion by asking "
        "whether the complete confidence region is separated from the complete "
        "declared model family. P78 supplies the missing global lower-bound certificate "
        "for the continuous P75 latent family using exact-rational multi-affine box "
        "refinement. The next problems are computational efficiency, sharper power, "
        "and robust alternatives for residually dependent or learned target-view systems.",
        "P76 adds a finite-sample rejection layer for a tracked family of necessary P75 "
        "polynomial constraints. Its non-rejection output is explicitly inconclusive. "
        "P77 defines the stronger full-law criterion. P78 supplies the global "
        "exact-rational lower-bound certificate for the continuous P75 family. P79 "
        "gives the sampling-radius side a certified upper direction. P80 retains "
        "probability-simplex coupling, and P81 adds exact projected-event constraints "
        "that can strictly strengthen P80. The next problems are tighter simultaneous "
        "event coupling, computational efficiency, sharper power, and robust "
        "alternatives for residually dependent or learned target-view systems.",
        1,
    )
    write(path, text)


def update_website_navigation() -> None:
    for path in (ROOT / "website").glob("*.html"):
        text = path.read_text(encoding="utf-8")
        nav_start = text.find("<nav>")
        nav_end = text.find("</nav>", nav_start)
        if nav_start < 0 or nav_end < 0:
            continue
        nav = text[nav_start:nav_end]
        if 'href="start-here.html"' not in nav:
            insertion = '\n      <a href="start-here.html">Start Here</a>'
            text = text[: nav_start + len("<nav>")] + insertion + text[nav_start + len("<nav>") :]
            path.write_text(text, encoding="utf-8")


def update_start_here() -> None:
    path = "START_HERE.md"
    text = read(path)
    if "**Reproduce everything:**" not in text:
        text = text.replace(
            "- **Public visual site:** [website](website/index.html)",
            "- **Reproduce everything:** [Reproducibility Guide](docs/reproducibility.md)\n"
            "- **Contribute or review changes:** [CONTRIBUTING.md](CONTRIBUTING.md)\n"
            "- **Public visual site:** [website](website/index.html)",
            1,
        )
    write(path, text)


def update_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    marker = "# 0.81.0 - 2026-09-11\n\n"
    note = (
        "- Added a first-reader `START_HERE.md`, glossary, reproducibility guide, "
        "contribution guide, unified figure-generation command, repository verifier, "
        "and reproducible figure GitHub Actions workflow.\n"
        "- Reorganized reader-facing navigation so the P81 frontier, proof/code/test "
        "paths, and scientific boundaries are consistent across GitHub and the public "
        "website.\n"
    )
    if "first-reader `START_HERE.md`" not in text:
        text = replace_once(text, marker, marker + note, label="changelog documentation note")
    write(path, text)


def assert_integration() -> None:
    checks = {
        "README.md": ("START_HERE.md", "docs/reproducibility.md"),
        "docs/research_navigation.md": ("frontier is **P81**", "P71-P81"),
        "docs/theorem_roadmap.md": ("frontier is **P81**", "P71-P81"),
        "docs/detailed_proposition_record.md": ("Projection-Event Certificate",),
        "website/research-map.html": ('href="start-here.html"',),
    }
    for path, markers in checks.items():
        source = read(path)
        for marker in markers:
            if marker not in source:
                raise AssertionError(f"{path} missing expected marker {marker!r}")


def main() -> None:
    update_readme()
    update_research_navigation()
    update_theorem_roadmap()
    update_detailed_record()
    update_website_navigation()
    update_start_here()
    update_changelog()
    assert_integration()
    print("reader documentation integration completed")


if __name__ == "__main__":
    main()
