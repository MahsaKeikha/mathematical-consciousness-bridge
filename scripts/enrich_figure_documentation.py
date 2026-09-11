from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass
from pathlib import Path

from quantum_figure_records import build_quantum_records, write_quantum_visual_guide

ROOT = Path(__file__).resolve().parents[1]
FIGURE_ROOT = ROOT / "docs" / "figures"
README = ROOT / "README.md"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"
QUANTITATIVE_ATLAS = ROOT / "docs" / "quantitative_physics_mathematics_atlas.md"
QUANTITATIVE_MANIFEST = FIGURE_ROOT / "quantitative" / "quantitative_figure_manifest.json"
CATALOG = ROOT / "docs" / "figure_catalog.md"


@dataclass(frozen=True)
class FigureRecord:
    title: str
    description: str
    status: str


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


def _trim(text: str, limit: int = 420) -> str:
    text = _plain(text)
    if len(text) <= limit:
        return text
    shortened = text[: limit - 1].rsplit(" ", 1)[0].rstrip(" ,;:")
    return shortened + "."


def _humanize_filename(path: Path) -> str:
    stem = path.stem
    stem = re.sub(r"^q(\d+)_", lambda m: f"Q{int(m.group(1)):02d} ", stem)
    stem = re.sub(r"^p(\d+)_", lambda m: f"P{int(m.group(1))} ", stem)
    words = stem.replace("_", " ").replace("-", " ")
    return " ".join(
        word.upper() if re.fullmatch(r"[pq]\d+", word, re.I) else word
        for word in words.split()
    ).strip().title()


def _escape_invalid_svg_text(svg: str) -> str:
    """Repair common raw comparison/text tokens without changing SVG markup.

    Several historical SVGs were browser-tolerant but not strict XML because a
    text node contained a raw '<' comparison.  The documentation guard parses
    SVGs as XML, so normalize only text-node payloads while preserving nested
    tags such as <tspan>.
    """

    def repair(match: re.Match[str]) -> str:
        start, payload, end = match.groups()
        payload = re.sub(
            r"&(?!#\d+;|#x[0-9A-Fa-f]+;|[A-Za-z][A-Za-z0-9]+;)",
            "&amp;",
            payload,
        )
        payload = payload.replace("<=", "&lt;=")
        payload = re.sub(r"<(?=[=\s0-9+\-.])", "&lt;", payload)
        return start + payload + end

    return re.sub(
        r"(<(?:text|tspan)\b[^>]*>)(.*?)(</(?:text|tspan)>)",
        repair,
        svg,
        flags=re.I | re.S,
    )


def _svg_labels(svg: str, limit: int = 8) -> list[str]:
    labels: list[str] = []
    for raw in re.findall(r"<text\b[^>]*>(.*?)</text>", svg, flags=re.I | re.S):
        label = _plain(raw)
        if not label or len(label) > 150:
            continue
        if label not in labels:
            labels.append(label)
        if len(labels) >= limit:
            break
    return labels


def _first_prose_summary(markdown: str) -> str:
    text = re.sub(r"```.*?```", "\n", markdown, flags=re.S)
    text = re.sub(r"\$\$.*?\$\$", "\n", text, flags=re.S)
    text = re.sub(r"\\\[.*?\\\]", "\n", text, flags=re.S)
    blocks = re.split(r"\n\s*\n", text)
    for block in blocks:
        block = block.strip()
        if not block or block.startswith(("#", "|", "!", "- ", "* ", ">", "[")):
            continue
        plain = _plain(block)
        if len(plain) >= 90:
            return _trim(plain, 360)
    return ""


def _existing_metadata(svg: str) -> tuple[str | None, str | None]:
    title_match = re.search(r"<title\b[^>]*>(.*?)</title>", svg, flags=re.I | re.S)
    desc_match = re.search(r"<desc\b[^>]*>(.*?)</desc>", svg, flags=re.I | re.S)
    title = _plain(title_match.group(1)) if title_match else None
    desc = _plain(desc_match.group(1)) if desc_match else None
    return title, desc


def _readme_records() -> dict[str, FigureRecord]:
    text = _read(README)
    records: dict[str, FigureRecord] = {}
    pattern = re.compile(
        r"!\[([^\]]+)\]\((docs/figures/[^)]+\.svg)\)\s*\n\s*\n([^\n]+)",
        flags=re.MULTILINE,
    )
    for alt, path, caption in pattern.findall(text):
        caption_plain = _plain(caption)
        if not caption_plain:
            continue
        records[path] = FigureRecord(
            title=_plain(alt),
            description=(
                f"What this figure shows: {caption_plain} "
                "How to read it: follow only the labeled arrows, axes, panels, set relations, or inequalities shown in the visual and interpret them using the adjacent research text. "
                "Main takeaway: the figure summarizes the stated mathematical or scientific dependency; visual proximity alone does not add a claim."
            ),
            status="Reader-facing research figure; formal status is controlled by the linked proof or source record.",
        )
    return records


def _visual_atlas_records() -> dict[str, FigureRecord]:
    text = _read(VISUAL_ATLAS)
    records: dict[str, FigureRecord] = {}
    pattern = re.compile(
        r'<img[^>]+src="[^"]*/docs/figures/([^"]+\.svg)"[^>]+alt="([^"]*)"[^>]*/?>',
        flags=re.I,
    )
    matches = list(pattern.finditer(text))
    for index, match in enumerate(matches):
        rel = f"docs/figures/{match.group(1)}"
        alt = _plain(match.group(2))
        end = matches[index + 1].start() if index + 1 < len(matches) else min(len(text), match.end() + 3500)
        tail = text[match.end() : end]
        heading_match = re.search(r"<h[23][^>]*>(.*?)</h[23]>", tail, flags=re.I | re.S)
        paragraphs = re.findall(r"<p(?![^>]*class=\"eyebrow\")[^>]*>(.*?)</p>", tail, flags=re.I | re.S)
        heading = _plain(heading_match.group(1)) if heading_match else alt
        paragraph = next((_plain(p) for p in paragraphs if len(_plain(p)) >= 60), "")
        if paragraph:
            records[rel] = FigureRecord(
                title=heading or alt,
                description=(
                    f"What this figure shows: {paragraph} "
                    "How to read it: use the labels, axes, panels, arrows, and legends as explicit guides; do not infer an unstated physical or experiential identity from the drawing."
                ),
                status="Visual-atlas explanation; theorem and provenance pages control formal claims.",
            )
    return records


def _quantitative_records() -> dict[str, FigureRecord]:
    records: dict[str, FigureRecord] = {}
    data = json.loads(_read(QUANTITATIVE_MANIFEST))
    for item in data:
        rel = f"docs/figures/quantitative/{item['file']}"
        title = _plain(item["title"])
        equation = _plain(item.get("equation", "declared numerical construction"))
        fact = _plain(item.get("fact", "The visible pattern follows from the declared construction."))
        status = _plain(item.get("status", "quantitative mathematical illustration"))
        records[rel] = FigureRecord(
            title=title,
            description=(
                f"What this figure shows: {fact} "
                f"The plotted object is generated from {equation}. "
                "How to read it: compare the labeled axes, curves, contours, matrix entries, bars, or markers exactly as defined in the atlas entry; the visible trend is the numerical realization of the stated equation or construction."
            ),
            status=f"{status}. Unless explicitly identified otherwise, this is not empirical consciousness data.",
        )
    return records


def _proposition_record(path: Path, svg: str) -> FigureRecord | None:
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
    summary = _first_prose_summary(text)
    labels = _svg_labels(svg)
    label_text = "; ".join(labels[1:7] if len(labels) > 1 else labels)

    if summary:
        what = summary
    else:
        what = f"the mathematical construction and certificate logic stated in {heading}"

    guideposts = f" Visible guideposts include: {label_text}." if label_text else ""
    description = (
        f"What this figure shows: {what}.{guideposts} "
        "How to read it: follow the diagram in the direction of its arrows and use each box, panel, inequality, or highlighted region only with the meaning printed beside it. "
        f"Main takeaway: this is the visual companion to Proposition {number}; the proposition document supplies the assumptions, proof, and exact scope of every implication."
    )
    return FigureRecord(
        title=heading,
        description=description,
        status=(
            f"Proposition {number} theorem/certificate visual. It is not independent empirical evidence and does not, by itself, identify a physical or latent variable with consciousness."
        ),
    )


def _fallback_record(path: Path, svg: str) -> FigureRecord:
    existing_title, existing_desc = _existing_metadata(svg)
    title = existing_title or _humanize_filename(path)
    labels = _svg_labels(svg)
    label_text = "; ".join(labels[:7])
    if existing_desc and len(existing_desc) >= 160:
        description = existing_desc
    else:
        guideposts = f" Visible guideposts include: {label_text}." if label_text else ""
        description = (
            f"What this figure shows: {title}.{guideposts} "
            "How to read it: use the explicitly printed labels, arrows, axes, panels, regions, and legends; do not assign meaning from color, proximity, or shape unless the figure says so. "
            "Main takeaway: this visual organizes a declared mathematical, physical, statistical, or research-architecture relationship and should be read with its linked context."
        )
    return FigureRecord(
        title=title,
        description=description,
        status="Conceptual or architecture figure; formal conclusions require the linked research context.",
    )


def _replace_or_insert_metadata(svg: str, record: FigureRecord) -> str:
    title_xml = html.escape(record.title, quote=False)
    full_description = f"{record.description} Scientific status: {record.status}"
    desc_xml = html.escape(full_description, quote=False)

    if re.search(r"<title\b[^>]*>.*?</title>", svg, flags=re.I | re.S):
        svg = re.sub(
            r"(<title\b[^>]*>).*?(</title>)",
            lambda m: f"{m.group(1)}{title_xml}{m.group(2)}",
            svg,
            count=1,
            flags=re.I | re.S,
        )
    else:
        root = re.search(r"<svg\b[^>]*>", svg, flags=re.I | re.S)
        if root is None:
            raise RuntimeError("SVG root tag not found")
        title_attr = ' id="title"' if 'aria-labelledby="title desc"' in root.group(0) else ""
        svg = svg[: root.end()] + f"\n  <title{title_attr}>{title_xml}</title>" + svg[root.end() :]

    if re.search(r"<desc\b[^>]*>.*?</desc>", svg, flags=re.I | re.S):
        svg = re.sub(
            r"(<desc\b[^>]*>).*?(</desc>)",
            lambda m: f"{m.group(1)}{desc_xml}{m.group(2)}",
            svg,
            count=1,
            flags=re.I | re.S,
        )
    else:
        title_end = re.search(r"</title>", svg, flags=re.I)
        root = re.search(r"<svg\b[^>]*>", svg, flags=re.I | re.S)
        if title_end is None or root is None:
            raise RuntimeError("SVG description insertion failed")
        desc_attr = ' id="desc"' if 'aria-labelledby="title desc"' in root.group(0) else ""
        svg = svg[: title_end.end()] + f"\n  <desc{desc_attr}>{desc_xml}</desc>" + svg[title_end.end() :]
    return svg


def _context_link(relative: str) -> str:
    path = Path(relative)
    if "quantitative" in path.parts:
        return "[Quantitative atlas](quantitative_physics_mathematics_atlas.md)"
    if "quantum" in path.parts:
        return "[Quantum visual guide](quantum_visual_guide.md)"
    match = re.match(r"p(\d+)_", path.name, flags=re.I)
    if match:
        number = int(match.group(1))
        candidates = sorted((ROOT / "docs").glob(f"proposition_{number}_*.md"))
        if candidates:
            return f"[Proposition {number}]({candidates[0].name})"
    return "[Main research narrative](../README.md)"


def _enrich_svgs() -> list[tuple[str, FigureRecord]]:
    combined = {
        **_visual_atlas_records(),
        **_readme_records(),
        **_quantitative_records(),
        **build_quantum_records(ROOT, FigureRecord, _plain),
    }
    rows: list[tuple[str, FigureRecord]] = []

    for path in sorted(FIGURE_ROOT.rglob("*.svg")):
        rel = path.relative_to(ROOT).as_posix()
        original = _read(path)
        svg = _escape_invalid_svg_text(original)

        record = combined.get(rel)
        if record is None:
            record = _proposition_record(path, svg)
        if record is None:
            record = _fallback_record(path, svg)

        enriched = _replace_or_insert_metadata(svg, record)
        if enriched != original:
            _write(path, enriched)
        rows.append((rel, record))
    return rows


def _update_quantitative_atlas() -> None:
    text = _read(QUANTITATIVE_ATLAS)
    for old in ("**Fact / interpretation:**", "**Fact:**", "**Interpretation:**"):
        text = text.replace(old, "**What the figure shows:**")

    marker = "## Scientific-status rule\n\n"
    addition = (
        "Each figure entry is intentionally self-explanatory: the generating equation or definition is stated first, "
        "**What the figure shows** explains the visible pattern in ordinary scientific language, and **Status** states whether the visual is an exact result, deterministic calculation, fixed-seed simulation, synthetic benchmark, or numerical verification. "
        "A reader should not have to infer the meaning of a curve, contour, matrix, or marker from appearance alone. "
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
        "\n> **Visual reading standard.** Every reader-facing figure now has a clear title, an embedded SVG description, a nearby caption or atlas explanation, a scientific-status boundary, and a direct route to the proof or source context. "
        "Use the [Complete Figure Catalog](docs/figure_catalog.md) to understand every visual without searching the repository, and the [Figure Caption and Description Standard](docs/figure_caption_and_description_standard.md) for the enforced documentation rules.\n"
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
        '<strong>Scientific boundary:</strong> diagrams, synthetic examples, and simulations do not become empirical consciousness evidence merely because they are visually compelling.</p>'
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
        '<h3>Gaussian geometry</h3></article>': '<h3>Gaussian geometry</h3><p>Read the contour orientation and elongation as the visible effect of covariance: zero off-diagonal covariance keeps principal axes aligned, while correlation rotates the equal-density ellipses. This is an equation-driven probability example, not empirical consciousness data.</p></article>',
        '<h3>Response geometry</h3></article>': '<h3>Response geometry</h3><p>Read each matrix entry as the total-variation separation between a pair of intervention-conditioned response laws. The zero diagonal and symmetry are metric properties; larger off-diagonal entries mean the two responses are more distinguishable.</p></article>',
        '<h3>Finite-data scaling</h3></article>': '<h3>Finite-data scaling</h3><p>Read the curve as the sample burden required to resolve progressively smaller robust gaps under the declared concentration bound. The steep increase toward small gaps is the important visual message: weak separation demands substantially more data.</p></article>',
        '<h3>P58 uncertainty envelopes</h3></article>': '<h3>P58 uncertainty envelopes</h3><p>Read each interval as the finite-data uncertainty attached to a transition or switching quantity. Robust routing must respect the complete certified envelope rather than treating a point estimate as exact.</p></article>',
        '<h3>P62 cost-aware calibration</h3></article>': '<h3>P62 cost-aware calibration</h3><p>Read allocation changes against heterogeneous measurement costs: an expensive transition receives resources only when its contribution to the certified objective justifies that cost. The figure illustrates the proved optimization rule, not an empirical consciousness measurement.</p></article>',
        '<h3>P70 certificate diagnostics</h3></article>': '<h3>P70 certificate diagnostics</h3><p>Read the decomposition as an audit trail for the final optimization gap. Each component shows where remaining suboptimality or uncertainty enters, so a small total gap has an explicit mathematical explanation rather than being inferred from solver output alone.</p></article>',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    _write(VISUAL_ATLAS, text)


def _write_catalog(rows: list[tuple[str, FigureRecord]]) -> None:
    conceptual = [
        row for row in rows
        if "/quantitative/" not in row[0]
        and "/quantum/" not in row[0]
        and not re.match(r"docs/figures/p\d+_", row[0], flags=re.I)
    ]
    quantum = [row for row in rows if "/quantum/" in row[0]]
    propositions = [row for row in rows if re.match(r"docs/figures/p\d+_", row[0], flags=re.I)]
    quantitative = [row for row in rows if "/quantitative/" in row[0]]

    lines = [
        "# Complete Figure Catalog",
        "",
        "This is the single visual index for the **Mathematical Consciousness Bridge** repository. Every SVG is listed with a direct link, an explicit description, a reading instruction, a scientific-status statement, and a route to formal context. A reader should not need to guess from a filename, search another folder, or infer an unstated meaning from visual appearance.",
        "",
        f"**Current catalog:** {len(rows)} SVG figures: {len(conceptual)} architecture/conceptual visuals, {len(quantum)} foundational quantum-physics visuals, {len(propositions)} proposition/theorem visuals, and {len(quantitative)} quantitative figures.",
        "",
        "Every SVG also carries an embedded `<title>` and substantive `<desc>` for direct viewing and accessibility. Caption requirements are defined in the [Figure Caption and Description Standard](figure_caption_and_description_standard.md).",
        "",
        "## Reading rule",
        "",
        "For every visual, identify **what objects are shown, how arrows/axes/panels/regions should be read, what precise takeaway is permitted, and what the scientific status is**. A theorem diagram illustrates a proved conditional result; a numerical or synthetic plot illustrates the declared mathematics or test behavior. Neither becomes empirical evidence about consciousness without an independently justified target and measurement record.",
        "",
    ]

    def add_section(title: str, section_rows: list[tuple[str, FigureRecord]]) -> None:
        lines.extend([
            f"## {title}",
            "",
            "| Figure | What it shows and how to interpret it | Scientific status | Formal context |",
            "| --- | --- | --- | --- |",
        ])
        for rel, record in section_rows:
            docs_rel = Path(rel).relative_to("docs").as_posix()
            safe_title = record.title.replace("|", "\\|")
            safe_desc = record.description.replace("|", "\\|")
            safe_status = record.status.replace("|", "\\|")
            lines.append(
                f"| [{safe_title}]({docs_rel}) | {safe_desc} | {safe_status} | {_context_link(rel)} |"
            )
        lines.append("")

    add_section("Architecture and conceptual figures", conceptual)
    add_section("Foundational quantum-physics figures", quantum)
    add_section("Proposition and theorem figures", propositions)
    add_section("Quantitative physics and mathematics figures", quantitative)

    lines.extend([
        "## Reproducibility routes",
        "",
        "- [Main research narrative](../README.md): scientific argument and curated captions.",
        "- [Visual Atlas](../website/visual-atlas.html): web-oriented visual browsing with nearby explanations.",
        "- [Quantitative Physics & Mathematics Atlas](quantitative_physics_mathematics_atlas.md): equation-driven Q-series figures with equations, interpretations, and status labels.",
        "- [Quantitative figure manifest](figures/quantitative/quantitative_figure_manifest.json): machine-readable quantitative metadata.",
        "- [Equation and Citation Map](equation_and_citation_map.md): equation-level provenance and source classification.",
        "- [Theorem Roadmap](theorem_roadmap.md): proposition dependency structure.",
        "",
        "The catalog is generated by [`scripts/enrich_figure_documentation.py`](../scripts/enrich_figure_documentation.py). The automated documentation tests require new figures to receive metadata and a catalog entry, so a visual cannot silently become orphaned from its explanation.",
    ])
    _write(CATALOG, "\n".join(lines) + "\n")


def main() -> None:
    _update_quantitative_atlas()
    _update_readme()
    _update_visual_atlas()
    rows = _enrich_svgs()
    write_quantum_visual_guide(ROOT)
    _write_catalog(rows)


if __name__ == "__main__":
    main()
