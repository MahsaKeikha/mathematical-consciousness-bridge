import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE_ROOT = ROOT / "docs" / "figures"
README = ROOT / "README.md"
CATALOG = ROOT / "docs" / "figure_catalog.md"
QUANTITATIVE_ATLAS = ROOT / "docs" / "quantitative_physics_mathematics_atlas.md"
QUANTUM_GUIDE = ROOT / "docs" / "quantum_visual_guide.md"
QUANTUM_MANIFEST = FIGURE_ROOT / "quantum" / "quantum_figure_manifest.json"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"

SPECIAL_CONCEPTUAL_FIGURES = {
    "physics_mathematics_atlas.svg": "[Main research narrative](../README.md)",
    "proposition_32_delay_quotient.svg": "[Proposition 32](proposition_32_delay_quotient_compatibility.md)",
    "spaceflight_extreme_environment_map.svg": "[Main research narrative](../README.md)",
    "state_space_dynamics_map.svg": "[Main research narrative](../README.md)",
    "thermodynamics_information_processing.svg": "[Main research narrative](../README.md)",
}


def _svg_title_and_description(path: Path) -> tuple[str, str]:
    root = ET.parse(path).getroot()
    namespace = {"svg": "http://www.w3.org/2000/svg"}
    title = root.find("svg:title", namespace)
    description = root.find("svg:desc", namespace)
    title_text = "" if title is None or title.text is None else " ".join(title.text.split())
    description_text = (
        ""
        if description is None or description.text is None
        else " ".join(description.text.split())
    )
    return title_text, description_text


def test_every_svg_has_substantive_accessible_metadata() -> None:
    figures = sorted(FIGURE_ROOT.rglob("*.svg"))
    assert figures

    failures = []
    for figure in figures:
        title, description = _svg_title_and_description(figure)
        if len(title) < 4:
            failures.append(f"{figure}: missing or trivial <title>")
        if len(description) < 140:
            failures.append(
                f"{figure}: <desc> is too short to explain the visual ({len(description)} chars)"
            )
        if description.count("Scientific status:") != 1:
            failures.append(
                f"{figure}: expected exactly one scientific-status boundary, found "
                f"{description.count('Scientific status:')}"
            )

    assert not failures, "\n".join(failures)


def test_complete_figure_catalog_covers_every_svg() -> None:
    catalog = CATALOG.read_text(encoding="utf-8")
    assert "# Complete Figure Catalog" in catalog
    assert "What it shows and how to interpret it" in catalog

    missing = []
    for figure in sorted(FIGURE_ROOT.rglob("*.svg")):
        docs_relative = figure.relative_to(ROOT / "docs").as_posix()
        if f"({docs_relative})" not in catalog:
            missing.append(docs_relative)

    assert not missing, "Figures missing from catalog:\n" + "\n".join(missing)


def test_every_readme_figure_has_an_adjacent_explanatory_caption() -> None:
    text = README.read_text(encoding="utf-8")
    lines = text.splitlines()
    figure_pattern = re.compile(r"!\[[^\]]+\]\((docs/figures/[^)]+\.svg)\)")

    failures = []
    for index, line in enumerate(lines):
        match = figure_pattern.search(line)
        if match is None:
            continue
        nearby = [candidate.strip() for candidate in lines[index + 1 : index + 6] if candidate.strip()]
        if not nearby:
            failures.append(f"{match.group(1)}: no caption after figure")
            continue
        caption = nearby[0]
        if not caption.startswith("**") or len(caption) < 100:
            failures.append(
                f"{match.group(1)}: first adjacent paragraph is not a substantive bold caption"
            )

    assert not failures, "\n".join(failures)


def test_quantitative_atlas_explains_visible_pattern_and_status_for_each_figure() -> None:
    text = QUANTITATIVE_ATLAS.read_text(encoding="utf-8")
    blocks = re.split(r"(?=## Q\d+\.)", text)
    figure_blocks = [block for block in blocks if block.startswith("## Q")]
    assert len(figure_blocks) >= 40

    failures = []
    for block in figure_blocks:
        heading = block.splitlines()[0]
        if "**What the figure shows:**" not in block:
            failures.append(f"{heading}: missing 'What the figure shows' explanation")
        if "**Status:**" not in block:
            failures.append(f"{heading}: missing scientific status")
        if not re.search(r"!\[Q\d+\]\(figures/quantitative/[^)]+\.svg\)", block):
            failures.append(f"{heading}: missing direct quantitative SVG")

    assert not failures, "\n".join(failures)


def test_quantum_figures_have_literal_physics_reading_guides() -> None:
    manifest = json.loads(QUANTUM_MANIFEST.read_text(encoding="utf-8"))
    assert manifest["figure_count"] == 18
    assert len(manifest["figures"]) == 18
    assert QUANTUM_GUIDE.exists()

    guide = QUANTUM_GUIDE.read_text(encoding="utf-8")
    catalog = CATALOG.read_text(encoding="utf-8")
    assert "## Foundational quantum-physics figures" in catalog
    assert "# Quantum Figure Visual Guide" in guide

    failures = []
    for index, item in enumerate(manifest["figures"], start=1):
        filename = item["file"]
        figure = FIGURE_ROOT / "quantum" / filename
        title, description = _svg_title_and_description(figure)

        required_description_tokens = (
            "What this figure shows:",
            "Governing relation:",
            "How to read it:",
            "Main takeaway:",
            "Scientific status:",
        )
        for token in required_description_tokens:
            if token not in description:
                failures.append(f"{filename}: SVG description missing {token!r}")

        if "Visible guideposts include" in description:
            failures.append(f"{filename}: still uses generic tick-label fallback wording")
        if len(description) < 500:
            failures.append(f"{filename}: quantum SVG explanation is too short ({len(description)} chars)")
        if not title or item["title"].lower() not in title.lower():
            failures.append(f"{filename}: SVG title does not match manifest title")

        heading = f"## QM{index:02d}. {item['title']}"
        if heading not in guide:
            failures.append(f"{filename}: missing visual-guide heading")
        if f"(figures/quantum/{filename})" not in guide:
            failures.append(f"{filename}: visual guide does not embed SVG")
        if f"**Figure QM{index:02d}. What this figure shows.**" not in guide:
            failures.append(f"{filename}: visual guide lacks literal figure caption")
        if "**How to read it.**" not in guide[guide.find(heading) : guide.find(heading) + 2500]:
            failures.append(f"{filename}: visual guide lacks reading instructions")
        if "**Scientific status.**" not in guide[guide.find(heading) : guide.find(heading) + 2500]:
            failures.append(f"{filename}: visual guide lacks scientific-status boundary")

        catalog_link = f"(figures/quantum/{filename})"
        matching_rows = [line for line in catalog.splitlines() if catalog_link in line]
        if len(matching_rows) != 1:
            failures.append(f"{filename}: expected exactly one catalog row")
        else:
            row = matching_rows[0]
            if "How to read it:" not in row or "Governing relation:" not in row:
                failures.append(f"{filename}: catalog row is not semantically self-explanatory")
            if "[Quantum visual guide](quantum_visual_guide.md)" not in row:
                failures.append(f"{filename}: catalog row lacks direct quantum-guide context")

    assert not failures, "\n".join(failures)


def test_special_conceptual_figures_are_self_explanatory_and_clickable() -> None:
    catalog = CATALOG.read_text(encoding="utf-8")
    failures = []

    for filename, context_link in SPECIAL_CONCEPTUAL_FIGURES.items():
        figure = FIGURE_ROOT / filename
        title, description = _svg_title_and_description(figure)
        if not title:
            failures.append(f"{filename}: missing title")
        for token in (
            "What this figure shows:",
            "How to read it:",
            "Main takeaway:",
            "Scientific status:",
        ):
            if token not in description:
                failures.append(f"{filename}: missing {token!r}")
        if description.count("Scientific status:") != 1:
            failures.append(f"{filename}: duplicate scientific-status wording")
        if len(description) < 500:
            failures.append(f"{filename}: description is too short ({len(description)} chars)")

        catalog_link = f"(figures/{filename})"
        matching_rows = [line for line in catalog.splitlines() if catalog_link in line]
        if len(matching_rows) != 1:
            failures.append(f"{filename}: expected exactly one catalog row")
        else:
            row = matching_rows[0]
            for token in ("What this figure shows:", "How to read it:", "Main takeaway:"):
                if token not in row:
                    failures.append(f"{filename}: catalog row missing {token!r}")
            if context_link not in row:
                failures.append(f"{filename}: catalog row missing direct formal-context link")

    assert not failures, "\n".join(failures)


def test_visual_atlas_never_presents_an_unexplained_image() -> None:
    text = VISUAL_ATLAS.read_text(encoding="utf-8")
    pattern = re.compile(
        r'<img[^>]+src="[^"]*/docs/figures/([^"]+\.svg)"[^>]+alt="([^"]*)"[^>]*/?>',
        flags=re.IGNORECASE,
    )
    matches = list(pattern.finditer(text))
    assert matches

    failures = []
    for index, match in enumerate(matches):
        filename = match.group(1)
        alt = match.group(2).strip()
        if len(alt) < 4:
            failures.append(f"{filename}: missing useful alt text")
        end = matches[index + 1].start() if index + 1 < len(matches) else min(len(text), match.end() + 3000)
        segment = text[match.end() : end]
        paragraphs = [
            re.sub(r"<[^>]+>", " ", paragraph)
            for paragraph in re.findall(r"<p[^>]*>(.*?)</p>", segment, flags=re.IGNORECASE | re.DOTALL)
        ]
        paragraphs = [" ".join(paragraph.split()) for paragraph in paragraphs]
        if not any(len(paragraph) >= 90 for paragraph in paragraphs):
            failures.append(f"{filename}: no substantive nearby visual explanation")

    assert not failures, "\n".join(failures)


def test_visual_documentation_is_prominent_from_the_main_entry_points() -> None:
    readme = README.read_text(encoding="utf-8")
    visual_atlas = VISUAL_ATLAS.read_text(encoding="utf-8")

    assert "[Complete Figure Catalog](docs/figure_catalog.md)" in readme
    assert "[Figure Caption and Description Standard](docs/figure_caption_and_description_standard.md)" in readme
    assert "How to read every figure" in visual_atlas
    assert "Complete Figure Catalog" in visual_atlas
