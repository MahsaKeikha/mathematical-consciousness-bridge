import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE_ROOT = ROOT / "docs" / "figures"
README = ROOT / "README.md"
CATALOG = ROOT / "docs" / "figure_catalog.md"
QUANTITATIVE_ATLAS = ROOT / "docs" / "quantitative_physics_mathematics_atlas.md"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"


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
            for paragraph in re.findall(r"<p[^>]*>(.*?)</p>", segment, flags=re.I | re.S)
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
