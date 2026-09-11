from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE_ROOT = ROOT / "docs" / "figures"
README = ROOT / "README.md"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"
QUANTITATIVE_ATLAS = ROOT / "docs" / "quantitative_physics_mathematics_atlas.md"
QUANTITATIVE_MANIFEST = (
    ROOT / "docs" / "figures" / "quantitative" / "quantitative_figure_manifest.json"
)
CATALOG = ROOT / "docs" / "figure_catalog.md"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def _plain(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("**", "").replace("__", "").replace("`", "")
    text = text.replace("$", "")
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def _humanize_filename(path: Path) -> str:
    stem = path.stem
    stem = re.sub(r"^q(\d+)_", lambda match: f"Q{int(match.group(1)):02d} ", stem)
    stem = re.sub(r"^p(\d+)_", lambda match: f"P{int(match.group(1))} ", stem)
    words = stem.replace("_", " ").replace("-", " ")
    return " ".join(word.upper() if re.fullmatch(r"[pq]\d+", word, re.I) else word for word in words.split()).strip().title()


def _readme_records() -> dict[str, tuple[str, str]]:
    text = _read(README)
    records: dict[str, tuple[str, str]] = {}
    pattern = re.compile(
        r"!\[([^\]]+)\]\((docs/figures/[^)]+\.svg)\)\s*\n\s*\n([^\n]+)",
        flags=re.MULTILINE,
    )
    for alt, path, caption in pattern.findall(text):
        caption_plain = _plain(caption)
        if not caption_plain:
            continue
        description = (
            f"What this figure shows: {caption_plain} "
            "This is the interpretation permitted by the main research narrative. "
            "The figure is a visual explanation of declared mathematical, physical, or statistical structure; "
            "proof status and assumptions come from the linked proposition or provenance record rather than from visual appearance alone."
        )
        records[path] = (_plain(alt), description)
    return records


def _visual_atlas_records() -> dict[str, tuple[str, str]]:
    text = _read(VISUAL_ATLAS)
    records: dict[str, tuple[str, str]] = {}
    image_pattern = re.compile(
        r'<img[^>]+src="[^"]*/docs/figures/([^"]+\.svg)"[^>]+alt="([^"]*)"[^>]*/?>',
        flags=re.IGNORECASE,
    )
    matches = list(image_pattern.finditer(text))
    for index, match in enumerate(matches):
        rel = f"docs/figures/{match.group(1)}"
        alt = _plain(match.group(2))
        end = matches[index + 1].start() if index + 1 < len(matches) else min(len(text), match.end() + 2500)
        tail = text[match.end() : end]
        heading_match = re.search(r"<h[23][^>]*>(.*?)</h[23]>", tail, flags=re.I | re.S)
        paragraphs = re.findall(r"<p(?![^>]*class=\"eyebrow\")[^>]*>(.*?)</p>", tail, flags=re.I | re.S)
        heading = _plain(heading_match.group(1)) if heading_match else alt
        paragraph = _plain(paragraphs[0]) if paragraphs else ""
        if paragraph:
            description = (
                f"What this figure shows: {paragraph} "
                "How to read it: follow the labels, panels, axes, arrows, or regions according to the relations stated in the figure. "
                "The visual is a navigation and explanation aid; the associated theorem or documentation controls the formal scientific conclusion."
            )
            records.setdefault(rel, (heading or alt, description))
    return records


def _quantitative_records() -> dict[str, tuple[str, str]]:
    records: dict[str, tuple[str, str]] = {}
    data = json.loads(_read(QUANTITATIVE_MANIFEST))
    for item in data:
        rel = f"docs/figures/quantitative/{item['file']}"
        title = _plain(item["title"])
        equation = _plain(item.get("equation", "declared numerical construction"))
        fact = _plain(item.get("fact", "The displayed pattern follows from the declared construction."))
        status = _plain(item.get("status", "quantitative mathematical illustration"))
        description = (
            f"What this figure shows: {fact} "
            f"The plotted object is generated from {equation}. "
            f"Scientific status: {status}. "
            "How to read it: interpret the displayed axes, curves, contours, bars, matrices, or markers as the numerical realization of that declared construction. "
            "Unless explicitly identified otherwise, this is not empirical consciousness data."
        )
        records[rel] = (title, description)
    return records


def _proposition_record(path: Path) -> tuple[str, str] | None:
    match = re.match(r"p(\d+)_", path.name, flags=re.I)
    if not match:
        return None
    number = int(match.group(1))
    candidates = sorted((ROOT / "docs").glob(f"proposition_{number}_*.md"))
    if not candidates:
        return None
    proposition = candidates[0]
    text = _read(proposition)
    heading_match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    heading = _plain(heading_match.group(1)) if heading_match else f"Proposition {number}"
    description = (
        f"Theorem figure for {heading}. "
        "What this figure shows: a visual summary of the proposition's declared mathematical objects, assumptions, construction, or certificate logic. "
        "How to read it: arrows, panels, inequalities, and highlighted regions represent only the relationships stated by the proposition. "
        "Scientific status, proof conditions, and interpretation boundaries are defined in the proposition document; the diagram by itself is not empirical evidence and does not identify a physical or latent variable with consciousness."
    )
    return heading, description


def _existing_metadata(svg: str) -> tuple[str | None, str | None]:
    title_match = re.search(r"<title\b[^>]*>(.*?)</title>", svg, flags=re.I | re.S)
    desc_match = re.search(r"<desc\b[^>]*>(.*?)</desc>", svg, flags=re.I | re.S)
    title = _plain(title_match.group(1)) if title_match else None
    desc = _plain(desc_match.group(1)) if desc_match else None
    return title, desc


def _replace_or_insert_metadata(svg: str, title: str, description: str) -> str:
    title_xml = html.escape(title, quote=False)
    desc_xml = html.escape(description, quote=False)

    if re.search(r"<title\b[^>]*>.*?</title>", svg, flags=re.I | re.S):
        svg = re.sub(
            r"(<title\b[^>]*>).*?(</title>)",
            lambda match: f"{match.group(1)}{title_xml}{match.group(2)}",
            svg,
            count=1,
            flags=re.I | re.S,
        )
    else:
        root_match = re.search(r"<svg\b[^>]*>", svg, flags=re.I | re.S)
        if root_match is None:
            raise RuntimeError("SVG root tag not found")
        root_tag = root_match.group(0)
        title_attr = ' id="title"' if 'aria-labelledby="title desc"' in root_tag else ""
        svg = svg[: root_match.end()] + f"\n  <title{title_attr}>{title_xml}</title>" + svg[root_match.end() :]

    if re.search(r"<desc\b[^>]*>.*?</desc>", svg, flags=re.I | re.S):
        svg = re.sub(
            r"(<desc\b[^>]*>).*?(</desc>)",
            lambda match: f"{match.group(1)}{desc_xml}{match.group(2)}",
            svg,
            count=1,
            flags=re.I | re.S,
        )
    else:
        title_match = re.search(r"</title>", svg, flags=re.I)
        if title_match is None:
            raise RuntimeError("SVG title insertion failed")
        root_match = re.search(r"<svg\b[^>]*>", svg, flags=re.I | re.S)
        root_tag = root_match.group(0) if root_match else ""
        desc_attr = ' id="desc"' if 'aria-labelledby="title desc"' in root_tag else ""
        svg = svg[: title_match.end()] + f"\n  <desc{desc_attr}>{desc_xml}</desc>" + svg[title_match.end() :]
    return svg


def _context_link(relative: str) -> str:
    path = Path(relative)
    if "quantitative" in path.parts:
        return "[Quantitative atlas](quantitative_physics_mathematics_atlas.md)"
    proposition = _proposition_record(ROOT / relative)
    if proposition:
        match = re.match(r"p(\d+)_", path.name, flags=re.I)
        if match:
            number = int(match.group(1))
            candidates = sorted((ROOT / "docs").glob(f"proposition_{number}_*.md"))
            if candidates:
                return f"[Proposition {number}]({candidates[0].name})"
    return "[Main research narrative](../README.md)"


def _enrich_svgs() -> list[tuple[str, str, str]]:
    readme = _readme_records()
    visual = _visual_atlas_records()
    quantitative = _quantitative_records()
    combined = {**visual, **readme, **quantitative}

    catalog_rows: list[tuple[str, str, str]] = []
    for path in sorted(FIGURE_ROOT.rglob("*.svg")):
        rel = path.relative_to(ROOT).as_posix()
        svg = _read(path)
        existing_title, existing_desc = _existing_metadata(svg)

        title: str
        description: str
        if rel in combined:
            title, description = combined[rel]
        else:
            proposition = _proposition_record(path)
            if proposition is not None:
                title, description = proposition
            else:
                title = existing_title or _humanize_filename(path)
                if existing_desc and len(existing_desc) >= 140:
                    description = existing_desc
                else:
                    description = (
                        f"Conceptual figure: {title}. "
                        "What this figure shows: a visual summary of mathematical, physical, statistical, or research-architecture relationships declared in the repository documentation. "
                        "How to read it: use the labels, arrows, axes, panels, regions, and legends according to their explicit annotations rather than inferring meaning from visual proximity alone. "
                        "The figure is explanatory and navigational; formal conclusions require the linked theorem, assumptions, source record, or validation artifact."
                    )

        enriched = _replace_or_insert_metadata(svg, title, description)
        if enriched != svg:
            _write(path, enriched)
        catalog_rows.append((rel, title, description))
    return catalog_rows


def _update_quantitative_atlas() -> None:
    text = _read(QUANTITATIVE_ATLAS)
    replacements = {
        "**Fact / interpretation:**": "**What the figure shows:**",
        "**Fact:**": "**What the figure shows:**",
        "**Interpretation:**": "**What the figure shows:**",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    marker = "## Scientific-status rule\n\n"
    addition = (
        "Each figure entry is written so it can be interpreted without guessing: the generating equation or definition is stated first, "
        "**What the figure shows** explains the visible pattern, and **Status** identifies whether the visual is an exact fact, deterministic calculation, fixed-seed simulation, synthetic benchmark, or numerical verification. "
        "For a single index of every visual in the repository, use the [Complete Figure Catalog](figure_catalog.md).\n\n"
    )
    if addition not in text:
        if marker not in text:
            raise RuntimeError("quantitative atlas scientific-status marker not found")
        text = text.replace(marker, marker + addition, 1)
    _write(QUANTITATIVE_ATLAS, text)


def _update_readme() -> None:
    text = _read(README)
    marker = (
        "**Figure 1. Scientific architecture of the project.** The research moves from physical dynamics to operationally measurable structure, "
        "then to mathematical sufficiency tests, target-side validity, finite-data certification, experimental design, and finally the still-open physical-to-experiential bridge. "
        "The arrows are logical dependencies, not claims that one layer has already been identified with consciousness.\n"
    )
    addition = (
        "\n> **Visual reading standard.** Every reader-facing figure is documented with a title, a substantive embedded SVG description, an adjacent caption or atlas explanation, a scientific-status boundary, and a direct route to its formal context. "
        "Use the [Complete Figure Catalog](docs/figure_catalog.md) to browse every visual without searching the repository, and the [Figure Caption and Description Standard](docs/figure_caption_and_description_standard.md) to see the rules enforced across the project.\n"
    )
    if addition.strip() not in text:
        if marker not in text:
            raise RuntimeError("README Figure 1 caption marker not found")
        text = text.replace(marker, marker + addition, 1)
    _write(README, text)


def _update_visual_atlas() -> None:
    text = _read(VISUAL_ATLAS)
    hero = (
        '<section class="hero compact-hero"><p class="eyebrow">Visual research atlas</p><h1>Figures as navigational aids to the mathematics</h1>'
        '<p class="lede">The figures below are selected entry points into the formal record. They are diagrams, quantitative illustrations, or computational visualizations. '
        'They do not replace proofs, and each should be read together with its theorem, assumptions, and provenance.</p></section>'
    )
    reading_key = (
        '\n<section class="boundary"><h2>How to read every figure</h2>'
        '<p><strong>What you are seeing:</strong> identify the mathematical objects, panels, axes, or regions. '
        '<strong>How to read it:</strong> follow arrows only as the declared logical, temporal, set-inclusion, or computational relation; compare plotted quantities using the labeled axes and legends. '
        '<strong>Main takeaway:</strong> use the accompanying text to identify the precise conclusion the visual supports. '
        '<strong>Scientific boundary:</strong> diagrams and simulations do not become empirical consciousness evidence merely because they are visually compelling.</p>'
        '<p>For a direct index of every SVG, including figures not selected for this web page, open the '
        '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figure_catalog.md">Complete Figure Catalog</a>. '
        'The repository-wide rules are in the '
        '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figure_caption_and_description_standard.md">Figure Caption and Description Standard</a>.</p></section>\n'
    )
    if reading_key.strip() not in text:
        if hero not in text:
            raise RuntimeError("visual atlas hero marker not found")
        text = text.replace(hero, hero + reading_key, 1)

    replacements = {
        '<h3>Gaussian geometry</h3></article>': '<h3>Gaussian geometry</h3><p>Read the contour orientation and elongation as the visible effect of covariance: zero off-diagonal covariance keeps principal axes aligned, while correlation rotates the equal-density ellipses. The figure is an equation-driven probability example, not empirical consciousness data.</p></article>',
        '<h3>Response geometry</h3></article>': '<h3>Response geometry</h3><p>Read the matrix entry at each intervention pair as their total-variation separation. Symmetry and the zero diagonal are metric properties; larger off-diagonal entries mean more distinguishable intervention-conditioned response laws.</p></article>',
        '<h3>Finite-data scaling</h3></article>': '<h3>Finite-data scaling</h3><p>Read the curve as the sample burden required to resolve progressively smaller effect gaps under the declared bound. The steep increase toward small gaps is the key message: weak separation requires substantially more data.</p></article>',
        '<h3>P58 uncertainty envelopes</h3></article>': '<h3>P58 uncertainty envelopes</h3><p>Read each interval as the finite-data uncertainty attached to a transition or switching quantity. Robust routing must respect the entire certified envelope rather than treating a point estimate as exact.</p></article>',
        '<h3>P62 cost-aware calibration</h3></article>': '<h3>P62 cost-aware calibration</h3><p>Read allocation changes against heterogeneous measurement costs: expensive transitions receive resources only when their contribution to the certified objective justifies the cost. The figure illustrates the proved optimization rule, not an empirical consciousness measurement.</p></article>',
        '<h3>P70 certificate diagnostics</h3></article>': '<h3>P70 certificate diagnostics</h3><p>Read the decomposition as an audit trail for the final optimization gap. Each component identifies where remaining suboptimality or uncertainty enters, so a small total gap has an explicit mathematical explanation rather than being inferred from solver output alone.</p></article>',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    _write(VISUAL_ATLAS, text)


def _write_catalog(rows: list[tuple[str, str, str]]) -> None:
    conceptual = [row for row in rows if "/quantitative/" not in row[0] and not re.match(r"docs/figures/p\d+_", row[0], flags=re.I)]
    propositions = [row for row in rows if re.match(r"docs/figures/p\d+_", row[0], flags=re.I)]
    quantitative = [row for row in rows if "/quantitative/" in row[0]]

    lines = [
        "# Complete Figure Catalog",
        "",
        "This page is the single visual index for the **Mathematical Consciousness Bridge** repository. Every SVG is listed with a direct link and an explanation so readers do not need to guess from a filename or search through folders to understand what a visual is for.",
        "",
        f"**Current catalog:** {len(rows)} SVG figures: {len(conceptual)} architecture/conceptual visuals, {len(propositions)} proposition/theorem visuals, and {len(quantitative)} quantitative figures.",
        "",
        "Every SVG also carries an embedded `<title>` and `<desc>` for direct viewing and accessibility. Caption requirements are defined in the [Figure Caption and Description Standard](figure_caption_and_description_standard.md).",
        "",
        "## Reading rule",
        "",
        "For each visual, ask: **what objects are shown, how should the visual relation be read, what precise takeaway is permitted, and what is the scientific status?** A theorem diagram illustrates a proved conditional result; a synthetic or simulated plot illustrates mathematics or test behavior; neither should be promoted into an empirical consciousness claim without an independently justified target and measurement record.",
        "",
    ]

    def add_section(title: str, section_rows: list[tuple[str, str, str]]) -> None:
        lines.extend([f"## {title}", "", "| Figure | What it shows and how to interpret it | Formal context |", "| --- | --- | --- |"])
        for rel, figure_title, description in section_rows:
            docs_rel = Path(rel).relative_to("docs").as_posix()
            safe_title = figure_title.replace("|", "\\|")
            safe_desc = description.replace("|", "\\|")
            lines.append(f"| [{safe_title}]({docs_rel}) | {safe_desc} | {_context_link(rel)} |")
        lines.append("")

    add_section("Architecture and conceptual figures", conceptual)
    add_section("Proposition and theorem figures", propositions)
    add_section("Quantitative physics and mathematics figures", quantitative)

    lines.extend(
        [
            "## Reproducibility routes",
            "",
            "- [Main research narrative](../README.md): scientific argument and curated figure captions.",
            "- [Visual Atlas](../website/visual-atlas.html): web-oriented visual browsing.",
            "- [Quantitative Physics & Mathematics Atlas](quantitative_physics_mathematics_atlas.md): equation-driven Q-series figures with status labels.",
            "- [Quantitative figure manifest](figures/quantitative/quantitative_figure_manifest.json): machine-readable quantitative metadata.",
            "- [Equation and Citation Map](equation_and_citation_map.md): equation-level provenance and source classification.",
            "- [Theorem Roadmap](theorem_roadmap.md): proposition dependency structure.",
            "",
            "The catalog is generated from repository metadata by [`scripts/enrich_figure_documentation.py`](../scripts/enrich_figure_documentation.py), so newly added figures cannot remain visually orphaned without being exposed by the documentation tests.",
        ]
    )
    _write(CATALOG, "\n".join(lines) + "\n")


def main() -> None:
    _update_quantitative_atlas()
    _update_readme()
    _update_visual_atlas()
    rows = _enrich_svgs()
    _write_catalog(rows)


if __name__ == "__main__":
    main()
