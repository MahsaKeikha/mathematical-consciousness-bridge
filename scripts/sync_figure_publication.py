"""Synchronize public figure surfaces with the canonical ``docs/figures`` tree.

There is one canonical SVG archive in this repository: ``docs/figures``. This
command derives the GitHub-facing ``figures/`` gateway, its SHA-256 manifest,
the current-frontier documentation, and placement of the current theorem figure
on the homepage and Visual Atlas.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC_FIGURES = ROOT / "docs" / "figures"
GATEWAY = ROOT / "figures"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"
HOME = ROOT / "website" / "index.html"
GATEWAY_CURRENT_FIGURE = GATEWAY / "current_frontier.svg"
VERIFIER = ROOT / "scripts" / "verify_repository.py"

FRONTIER_RE = re.compile(r'^CURRENT_FRONTIER = "P(?P<number>\d+)"$', re.MULTILINE)
RAW_FIGURE_PREFIX = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/"
)
BLOB_PREFIX = (
    "https://github.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/blob/main/"
)


def _current_frontier() -> int:
    match = FRONTIER_RE.search(VERIFIER.read_text(encoding="utf-8"))
    if match is None:
        raise RuntimeError("could not determine CURRENT_FRONTIER from verifier")
    return int(match.group("number"))


def _one_match(pattern: str, *, root: Path) -> Path:
    matches = sorted(root.glob(pattern))
    if len(matches) != 1:
        relative = root.relative_to(ROOT)
        raise RuntimeError(
            f"expected exactly one {relative}/{pattern} match, found "
            f"{[path.name for path in matches]}"
        )
    return matches[0]


def _frontier_records(start: int, stop: int) -> list[dict[str, str | int]]:
    records: list[dict[str, str | int]] = []
    for number in range(start, stop + 1):
        figure = _one_match(f"p{number}_*.svg", root=DOC_FIGURES)
        proposition = _one_match(f"proposition_{number}_*.md", root=ROOT / "docs")
        provenance = ROOT / "docs" / f"p{number}_equation_provenance.md"
        records.append(
            {
                "number": number,
                "figure": figure.relative_to(ROOT).as_posix(),
                "proposition": proposition.relative_to(ROOT).as_posix(),
                "provenance": (
                    provenance.relative_to(ROOT).as_posix()
                    if provenance.is_file()
                    else ""
                ),
            }
        )
    return records


def _svg_metadata(path: Path) -> tuple[str, str]:
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


def _figure_manifest(frontier: int) -> str:
    records: list[dict[str, object]] = []
    for path in sorted(DOC_FIGURES.rglob("*.svg")):
        raw = path.read_bytes()
        title, description = _svg_metadata(path)
        relative = path.relative_to(ROOT).as_posix()
        if "/quantitative/" in relative:
            category = "quantitative"
        elif "/quantum/" in relative:
            category = "quantum"
        else:
            category = "theorem-or-architecture"
        records.append(
            {
                "path": relative,
                "sha256": hashlib.sha256(raw).hexdigest(),
                "bytes": len(raw),
                "category": category,
                "title": title,
                "description_chars": len(description),
            }
        )

    current_figure = _one_match(f"p{frontier}_*.svg", root=DOC_FIGURES)
    payload = {
        "schema_version": 1,
        "canonical_root": "docs/figures",
        "current_frontier": f"P{frontier}",
        "current_frontier_figure": current_figure.relative_to(ROOT).as_posix(),
        "figure_count": len(records),
        "hash_algorithm": "sha256",
        "figures": records,
    }
    return json.dumps(payload, indent=2) + "\n"


def _gateway_readme(frontier: int) -> str:
    current_figure = _one_match(f"p{frontier}_*.svg", root=DOC_FIGURES)
    current_prop = _one_match(f"proposition_{frontier}_*.md", root=ROOT / "docs")
    return f"""# Visual research gateway

This top-level `figures/` directory is the GitHub-facing entry point for the
visual record of the Mathematical Consciousness Bridge project. The canonical
SVG archive lives in [`docs/figures/`](../docs/figures/); this gateway is derived
from that archive by code so it cannot silently remain on an older proposition.

## Current theorem frontier: P{frontier}

![P{frontier} current theorem frontier](../{current_figure.relative_to(ROOT).as_posix()})

Canonical figure: [`{current_figure.name}`](../{current_figure.relative_to(ROOT).as_posix()})
Theorem: [`{current_prop.name}`](../{current_prop.relative_to(ROOT).as_posix()})
Equation provenance: [`p{frontier}_equation_provenance.md`](../docs/p{frontier}_equation_provenance.md)

For the full P71-P{frontier} visual progression, open
[`CURRENT_FRONTIER.md`](CURRENT_FRONTIER.md).

## Complete reproducible figure record

[`manifest.json`](manifest.json) is generated from **every SVG under
`docs/figures/`**. Each record contains its canonical path, SHA-256 digest, byte
size, category, SVG title, and description length.

The curated human-readable index remains
[`docs/figure_catalog.md`](../docs/figure_catalog.md), and the browser-facing
atlas is [`website/visual-atlas.html`](../website/visual-atlas.html).

## Reproduce and validate

```bash
python scripts/generate_all_figures.py
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

## Scientific boundary

Generated atlases, theorem diagrams, and architecture illustrations have
different evidential meanings. A figure is not empirical consciousness evidence
merely because it is visual. Its scientific status comes from the associated
theorem, assumptions, data provenance, tests, and declared evidence class.
"""


def _frontier_page(frontier: int) -> str:
    records = _frontier_records(71, frontier)
    current = records[-1]
    lines = [
        f"# Current visual frontier: P71-P{frontier}",
        "",
        "This page is generated from the canonical proposition and figure tree.",
        "It is the compact GitHub-facing visual route through the current target-side branch.",
        "",
        f"## Current theorem frontier: P{frontier}",
        "",
        f"![P{frontier} current theorem frontier](../{current['figure']})",
        "",
        f"[Read Proposition {frontier}](../{current['proposition']})",
        "",
        f"[Open P{frontier} equation provenance](../docs/p{frontier}_equation_provenance.md)",
        "",
    ]
    if frontier == 87:
        lines.extend(
            [
                "### Exact P87 hierarchy witness",
                "",
                "P87 completes the primitive four-event coefficient box with nonzero integer coefficients satisfying `|c_i| <= 2` and strictly strengthens the complete P86 certificate on the exact rational witness:",
                "",
                "```text",
                "L85 = 0 < L86 = 1/192 < L87 = 1/96",
                "120 primitive sign-normalized coefficient patterns per four-event subset",
                "39,600 standard P87 functionals",
                "```",
                "",
                "This is a conditional model-separation result inside the declared P75 family. It is not an identification of a latent state with conscious experience.",
                "",
            ]
        )

    lines.extend(
        [
            f"## P71-P{frontier} canonical theorem-figure index",
            "",
            "| Proposition | Canonical figure | Proof | Provenance |",
            "| --- | --- | --- | --- |",
        ]
    )
    for record in records:
        provenance = (
            f"[equations](../{record['provenance']})" if record["provenance"] else "N/A"
        )
        lines.append(
            f"| P{record['number']} | [figure](../{record['figure']}) | "
            f"[proof](../{record['proposition']}) | {provenance} |"
        )

    lines.extend(
        [
            "",
            "## Reproduce the visual record",
            "",
            "```bash",
            "python scripts/generate_all_figures.py",
            "python scripts/sync_figure_publication.py --check",
            "python scripts/verify_repository.py",
            "```",
            "",
            "The complete machine-readable SHA-256 inventory is in [`manifest.json`](manifest.json).",
            "",
            "## Interpretation boundary",
            "",
            f"P71-P{frontier} strengthens the methodology for testing a declared physical-to-target model. It does not derive consciousness from physics, prove nonphysicality, or close the physical-to-experiential bridge.",
            "",
        ]
    )
    return "\n".join(lines)


def _docs_figure_readme(frontier: int) -> str:
    current = _one_match(f"p{frontier}_*.svg", root=DOC_FIGURES)
    recent = _frontier_records(max(71, frontier - 3), frontier)
    recent_lines = "\n".join(f"- `{Path(record['figure']).name}`" for record in recent)
    return f"""# Figure provenance and regeneration

`docs/figures/` is the canonical visual archive for the Mathematical
Consciousness Bridge research program. The repository distinguishes generated
computational atlases from source-controlled theorem and architecture diagrams
because they have different scientific meanings.

## Generated computational atlases

```text
docs/figures/quantitative/
docs/figures/quantum/
```

Regenerate and validate them with:

```bash
python scripts/generate_all_figures.py
```

## Source-controlled theorem and architecture figures

SVGs stored directly in this directory communicate theorem structure,
assumptions, inequalities, dependencies, or scientific boundaries. They are
validated as SVG documents and enriched with accessible `<title>` and `<desc>`
metadata. They are not reclassified as empirical evidence simply because they
are visual.

## Current frontier: P{frontier}

![P{frontier} current theorem frontier]({current.name})

Canonical current-frontier figure: `{current.name}`

Recent exact frontier figures:

{recent_lines}

The GitHub-facing [`figures/`](../../figures/) gateway and its SHA-256
[`manifest.json`](../../figures/manifest.json) are deterministically synchronized
from this canonical tree by `scripts/sync_figure_publication.py`.

## Validation without regeneration

```bash
python scripts/generate_all_figures.py --validate-only
python scripts/sync_figure_publication.py --check
```

For the curated reader-facing index, see [`docs/figure_catalog.md`](../figure_catalog.md).
For complete setup instructions, see [`docs/reproducibility.md`](../reproducibility.md).

## Scientific boundary

A successful figure workflow proves that the declared generation and validation
path reproduced successfully. It does not turn a theorem illustration, synthetic
benchmark, or model calculation into empirical evidence about consciousness.
"""


def _p87_visual_section() -> str:
    return f'''<section id="p87-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Current theorem frontier · P87</p>
    <h2>Complete bounded primitive four-event parity certificate</h2>
    <p>P87 completes the nonzero primitive coefficient box with |c_i| at most 2 at the same four-event order. Its 39,600-function exact audit strictly strengthens the complete P86 certificate on the same rational witness.</p>
  </div>
  <div class="theorem-figure-shell">
    <a href="{BLOB_PREFIX}docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg" aria-label="Open the full P87 theorem figure">
      <img loading="eager" decoding="async" src="{RAW_FIGURE_PREFIX}p87_exact_bounded_primitive_quad_projection_parity.svg" alt="P87 bounded primitive four-event parity certificate showing L86 equals one over 192 and L87 equals one over 96" />
    </a>
  </div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Complete bounded family</h3><p>120 primitive sign-normalized coefficient patterns per four-event subset yield 39,600 exact P87 functionals.</p></article>
    <article class="frontier-summary-card"><h3>Strict hierarchy</h3><p>The exact witness has <strong>L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96</strong>.</p></article>
    <article class="frontier-summary-card"><h3>Reproducible record</h3><p>The proof, equation provenance, exact implementation, exhaustive tests, theorem SVG, and figure manifest are source controlled.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> P87 is a conditional exact model-separation theorem for the declared P75 family. It does not identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.</p></div>
  <p><a href="{BLOB_PREFIX}docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md">Open the P87 theorem</a> · <a href="{BLOB_PREFIX}docs/p87_equation_provenance.md">Equation provenance</a> · <a href="{BLOB_PREFIX}src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py">Implementation</a> · <a href="{BLOB_PREFIX}tests/test_bounded_primitive_quad_projection_parity_functional_separation.py">Exact tests</a></p>
</section>'''


def _remove_section(text: str, section_id: str) -> str:
    pattern = re.compile(
        rf'\s*<section id="{re.escape(section_id)}".*?</section>\s*',
        re.DOTALL,
    )
    text, count = pattern.subn("\n", text, count=1)
    if count > 1:
        raise RuntimeError(f"expected at most one {section_id} section")
    return text


def _demote_p86(text: str) -> str:
    return text.replace(
        "Current theorem frontier · P86",
        "Previous theorem frontier · P86",
    )


def _normalize_visual_atlas(text: str) -> str:
    text = _remove_section(text, "p87-frontier")
    text = _demote_p86(text)
    text = re.sub(r"\s*<!-- current-frontier-visual: P\d+ -->\s*", "\n", text)
    boundary = re.search(r'<section class="boundary">.*?</section>', text, re.DOTALL)
    if boundary is None:
        raise RuntimeError("could not locate Visual Atlas reading-boundary section")
    prefix = text[: boundary.end()].rstrip()
    suffix = text[boundary.end() :].lstrip()
    insertion = "\n\n<!-- current-frontier-visual: P87 -->\n" + _p87_visual_section() + "\n\n"
    result = prefix + insertion + suffix
    return "\n".join(line.rstrip() for line in result.splitlines()) + "\n"


def _normalize_homepage(text: str) -> str:
    text = _remove_section(text, "p87-frontier")
    text = _demote_p86(text)
    replacements = (
        ("The 86 results form several dependency branches.", "The 87 results form several dependency branches."),
        ("all 86 propositions", "all 87 propositions"),
        ("P71-P86, then read the falsification program", "P71-P87, then read the falsification program"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    text = re.sub(r"\s*<!-- current-frontier-home: P\d+ -->\s*", "\n", text)
    hero = re.search(r'<section class="hero">.*?</section>', text, re.DOTALL)
    if hero is None:
        raise RuntimeError("could not locate homepage hero section")
    prefix = text[: hero.end()].rstrip()
    suffix = text[hero.end() :].lstrip()
    insertion = "\n\n<!-- current-frontier-home: P87 -->\n" + _p87_visual_section() + "\n\n"
    result = prefix + insertion + suffix
    return "\n".join(line.rstrip() for line in result.splitlines()) + "\n"


def _expected_outputs() -> dict[Path, str]:
    frontier = _current_frontier()
    if frontier != 87:
        raise RuntimeError(f"P87 synchronizer expected frontier 87, found {frontier}")
    current_figure = _one_match(f"p{frontier}_*.svg", root=DOC_FIGURES)
    return {
        GATEWAY_CURRENT_FIGURE: current_figure.read_text(encoding="utf-8"),
        GATEWAY / "README.md": _gateway_readme(frontier),
        GATEWAY / "CURRENT_FRONTIER.md": _frontier_page(frontier),
        GATEWAY / "manifest.json": _figure_manifest(frontier),
        DOC_FIGURES / "README.md": _docs_figure_readme(frontier),
        VISUAL_ATLAS: _normalize_visual_atlas(VISUAL_ATLAS.read_text(encoding="utf-8")),
        HOME: _normalize_homepage(HOME.read_text(encoding="utf-8")),
    }


def synchronize(*, check: bool) -> None:
    drift: list[str] = []
    for path, expected in _expected_outputs().items():
        current = path.read_text(encoding="utf-8") if path.is_file() else None
        if current == expected:
            continue
        relative = path.relative_to(ROOT).as_posix()
        if check:
            drift.append(relative)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8")
            print(f"[figure-sync] updated {relative}")

    if drift:
        raise RuntimeError(
            "figure publication surfaces are out of sync: " + ", ".join(drift)
        )
    if check:
        print("[figure-sync] publication surfaces are synchronized")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Synchronize GitHub and website figure publication surfaces."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail on drift instead of rewriting synchronized publication files",
    )
    args = parser.parse_args()
    synchronize(check=args.check)


if __name__ == "__main__":
    main()
