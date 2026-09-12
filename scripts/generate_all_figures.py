"""Generate and validate the repository's reproducible figure atlases.

The repository contains two kinds of visual assets:

1. generated quantitative atlases under ``docs/figures/quantitative`` and
   ``docs/figures/quantum``;
2. source-controlled theorem and architecture SVGs under ``docs/figures``.

This command regenerates the two computational atlases using their canonical
scripts, reapplies the repository's embedded SVG title/description metadata,
and then validates every SVG in the figure tree as parseable vector content.
Source-authored theorem SVGs are validated and enriched from their maintained
documentation records rather than being recreated by a plotting script.

Run from the repository root with::

    python scripts/generate_all_figures.py

Use ``--validate-only`` to check the current figure tree without regenerating
atlas outputs.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE_ROOT = ROOT / "docs" / "figures"
QUANTITATIVE_DIR = FIGURE_ROOT / "quantitative"
QUANTUM_DIR = FIGURE_ROOT / "quantum"
GENERATORS = (
    ROOT / "scripts" / "generate_quantitative_atlas.py",
    ROOT / "scripts" / "generate_quantum_foundations_atlas.py",
)
ENRICHER = ROOT / "scripts" / "enrich_figure_documentation.py"


def _run_generator(path: Path) -> None:
    print(f"[figures] running {path.relative_to(ROOT)}")
    subprocess.run([sys.executable, str(path)], cwd=ROOT, check=True)


def _load_json(path: Path) -> object:
    if not path.is_file():
        raise FileNotFoundError(f"missing figure manifest: {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def _validate_quantitative_manifest() -> int:
    manifest_path = QUANTITATIVE_DIR / "quantitative_figure_manifest.json"
    manifest = _load_json(manifest_path)
    if not isinstance(manifest, list) or not manifest:
        raise ValueError("quantitative figure manifest must be a nonempty list")

    expected = {str(item["file"]) for item in manifest if isinstance(item, dict)}
    actual = {path.name for path in QUANTITATIVE_DIR.glob("q*.svg")}
    if expected != actual:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise RuntimeError(
            "quantitative figure manifest mismatch: "
            f"missing={missing}, extra={extra}"
        )
    return len(actual)


def _validate_quantum_manifest() -> int:
    manifest_path = QUANTUM_DIR / "quantum_figure_manifest.json"
    manifest = _load_json(manifest_path)
    if not isinstance(manifest, dict):
        raise TypeError("quantum figure manifest must be an object")
    figures = manifest.get("figures")
    if not isinstance(figures, list) or not figures:
        raise ValueError("quantum figure manifest must contain a nonempty figures list")

    expected = {str(item["file"]) for item in figures if isinstance(item, dict)}
    actual = {path.name for path in QUANTUM_DIR.glob("qm*.svg")}
    declared_count = manifest.get("figure_count")
    if declared_count != len(expected):
        raise RuntimeError(
            "quantum manifest figure_count does not match the listed figure records"
        )
    if expected != actual:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise RuntimeError(
            f"quantum figure manifest mismatch: missing={missing}, extra={extra}"
        )
    return len(actual)


def _validate_svg_tree() -> tuple[int, int]:
    svg_paths = sorted(FIGURE_ROOT.rglob("*.svg"))
    if not svg_paths:
        raise RuntimeError("no SVG figures were found under docs/figures")

    source_authored = 0
    for path in svg_paths:
        try:
            root = ET.fromstring(path.read_text(encoding="utf-8"))
        except (OSError, ET.ParseError) as exc:
            raise RuntimeError(f"invalid SVG: {path.relative_to(ROOT)}") from exc
        if not root.tag.endswith("svg"):
            raise RuntimeError(f"not an SVG root element: {path.relative_to(ROOT)}")
        if QUANTITATIVE_DIR not in path.parents and QUANTUM_DIR not in path.parents:
            source_authored += 1

    return len(svg_paths), source_authored


def validate_figures() -> None:
    quantitative_count = _validate_quantitative_manifest()
    quantum_count = _validate_quantum_manifest()
    svg_count, source_authored_count = _validate_svg_tree()
    print(
        "[figures] validation passed: "
        f"{quantitative_count} quantitative atlas SVGs, "
        f"{quantum_count} quantum atlas SVGs, "
        f"{source_authored_count} source-authored SVGs, "
        f"{svg_count} total SVGs"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate the reproducible figure atlases and validate all SVG assets."
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="validate current figures and manifests without regenerating atlas outputs",
    )
    args = parser.parse_args()

    if not args.validate_only:
        for generator in GENERATORS:
            if not generator.is_file():
                raise FileNotFoundError(
                    f"missing generator: {generator.relative_to(ROOT)}"
                )
            _run_generator(generator)
        if not ENRICHER.is_file():
            raise FileNotFoundError(
                f"missing figure documentation enricher: {ENRICHER.relative_to(ROOT)}"
            )
        _run_generator(ENRICHER)

    validate_figures()


if __name__ == "__main__":
    main()
