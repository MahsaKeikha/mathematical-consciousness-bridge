"""Synchronize public Research III surfaces to one validated snapshot.

The website spans several HTML and JavaScript reader surfaces. This module keeps
all Research III links and visible implementation metrics pinned to the same
validated repository commit before publication.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

CURRENT_RESEARCH_THREE_PIN = "64b2bc47461fe110b135080f8dc70883552d6fd9"
LEGACY_RESEARCH_THREE_PINS = (
    "3cf9202977953644c980246c1f3e46a3514b3a4a",
    "5d1d979231aed62fde34383281fa8f252a3d2fa7",
    "b874eda1f6940f5601b7f89200b6a276b5ecbbc3",
    "8bbb7b029d70c43cc6a9dbf8b44dfe5069d0993d",
    "7a106820158e0d33ea651f7cdeaa505206f1ccc7",
    "a9ef67ed15595c26b0c9f4e449f53f8078d6a1ee",
)
CURRENT_RESEARCH_THREE_TEST_COUNT = 81
ROOT = Path(__file__).resolve().parents[1]
MEASUREMENT_REPO_PATH = "MahsaKeikha/consciousness-measurement-science"
PUBLIC_SUFFIXES = {".html", ".js"}


def _current_frontier_label() -> str:
    verifier = (ROOT / "scripts" / "verify_repository.py").read_text(encoding="utf-8")
    match = re.search(r'^CURRENT_FRONTIER = "(P\d+)"$', verifier, flags=re.MULTILINE)
    if match is None:
        raise RuntimeError("could not determine current Research II frontier")
    return match.group(1)


CURRENT_FRONTIER_LABEL = _current_frontier_label()
CURRENT_HOME_MARKER = f"<!-- current-frontier-home: {CURRENT_FRONTIER_LABEL} -->"

MEASUREMENT_SCIENCE_REQUIRED_MARKERS = (
    "Formal validation V1-V10",
    "19</strong><span>scientific visuals: 9 architecture + 10 validation",
    "81</strong><span>tests in each CI job",
    "docs/validation-atlas.md",
    "results/README.md",
    "resolution_abstention_frontier.svg",
    "analytic and synthetic validation results",
    "corrected V10 abstention theorem",
)


def _replace_research_three_pins(text: str) -> str:
    for legacy in LEGACY_RESEARCH_THREE_PINS:
        text = text.replace(legacy, CURRENT_RESEARCH_THREE_PIN)

    text = text.replace(
        f"github.com/{MEASUREMENT_REPO_PATH}/blob/main/",
        f"github.com/{MEASUREMENT_REPO_PATH}/blob/{CURRENT_RESEARCH_THREE_PIN}/",
    )
    text = text.replace(
        f"github.com/{MEASUREMENT_REPO_PATH}/tree/main/",
        f"github.com/{MEASUREMENT_REPO_PATH}/tree/{CURRENT_RESEARCH_THREE_PIN}/",
    )
    text = text.replace(
        f"raw.githubusercontent.com/{MEASUREMENT_REPO_PATH}/main/",
        f"raw.githubusercontent.com/{MEASUREMENT_REPO_PATH}/{CURRENT_RESEARCH_THREE_PIN}/",
    )
    return text


def _replace_research_three_metrics(text: str) -> str:
    if "Research III" not in text and "consciousness-measurement-science" not in text:
        return text
    for old_count in (23, 34, 35):
        text = text.replace(
            f"<strong>{old_count}</strong><span>tests in each CI job</span>",
            f"<strong>{CURRENT_RESEARCH_THREE_TEST_COUNT}</strong><span>tests in each CI job</span>",
        )
        text = text.replace(
            f"{old_count} tests in each CI job",
            f"{CURRENT_RESEARCH_THREE_TEST_COUNT} tests in each CI job",
        )
    return text


def _collapse_frontier_markers(text: str) -> str:
    marker_pattern = re.compile(
        rf"(?:{re.escape(CURRENT_HOME_MARKER)}\s*){{2,}}",
        flags=re.MULTILINE,
    )
    return marker_pattern.sub(f"{CURRENT_HOME_MARKER}\n", text)


def _transform(path: Path, text: str) -> str:
    text = _replace_research_three_pins(text)
    text = _replace_research_three_metrics(text)
    if path.name == "index.html":
        text = _collapse_frontier_markers(text)
    return text


def _public_files(site: Path) -> list[Path]:
    return sorted(
        path
        for path in site.rglob("*")
        if path.is_file() and path.suffix.lower() in PUBLIC_SUFFIXES
    )


def _validate_site(site: Path, transformed: dict[Path, str]) -> None:
    def text(relative: str) -> str:
        path = site / relative
        if path not in transformed:
            raise FileNotFoundError(f"missing public Research III surface: {path}")
        return transformed[path]

    measurement = text("measurement-science.html")
    missing = [marker for marker in MEASUREMENT_SCIENCE_REQUIRED_MARKERS if marker not in measurement]
    if missing:
        raise RuntimeError("measurement-science is missing V1-V10 markers: " + repr(missing))

    if "Implemented now versus not yet established" in measurement:
        raise RuntimeError("measurement-science still contains the removed governance panel")

    refresh = text("research-iii-atlas-refresh.js")
    required_refresh_markers = (
        CURRENT_RESEARCH_THREE_PIN,
        "research-iii-validation-figure-gallery",
        "research-iii-source-validation-gallery",
        "10 / 10 visible",
        "calibration_sample_uncertainty.svg",
        "missingness_identification_loss.svg",
        "inverse_conditioning_youden.svg",
        "two_site_partial_identification.svg",
        "resolution_abstention_frontier.svg",
    )
    missing_refresh = [marker for marker in required_refresh_markers if marker not in refresh]
    if missing_refresh:
        raise RuntimeError(
            "Research III gallery refresh is missing current validation markers: "
            + repr(missing_refresh)
        )

    homepage = text("index.html")
    if homepage.count(CURRENT_HOME_MARKER) != 1:
        raise RuntimeError(
            f"homepage must contain exactly one current frontier marker: {CURRENT_HOME_MARKER}"
        )

    orientation = text("research-orientation.js")
    for marker in (
        "function enhanceHomepageResearchIII()",
        "Measurement engineering and formal validation",
        "V1-V10 formal validation",
        "81</strong><span>tests in each CI job",
        "10 result figures",
        "machine-readable outputs",
    ):
        if marker not in orientation:
            raise RuntimeError(f"homepage Research III engineering record is missing: {marker}")

    key_surfaces = (
        "measurement-science.html",
        "index.html",
        "research-lineage.html",
        "research-iii-atlas-refresh.js",
        "source-section-visuals.js",
        "atlas-architecture-refresh.js",
        "research-orientation.js",
    )
    for relative in key_surfaces:
        surface = text(relative)
        if CURRENT_RESEARCH_THREE_PIN not in surface:
            raise RuntimeError(f"{relative} is not pinned to Research III {CURRENT_RESEARCH_THREE_PIN}")
        stale = [pin for pin in LEGACY_RESEARCH_THREE_PINS if pin in surface]
        if stale:
            raise RuntimeError(f"{relative} still contains stale Research III pins: {stale}")


def synchronize_site(site: Path, *, write: bool) -> list[str]:
    """Return changed paths and optionally write synchronized public source files."""

    files = _public_files(site)
    transformed: dict[Path, str] = {}
    changed: list[str] = []

    for path in files:
        original = path.read_text(encoding="utf-8")
        updated = _transform(path, original)
        transformed[path] = updated
        if updated != original:
            changed.append(str(path.relative_to(site)))
            if write:
                path.write_text(updated, encoding="utf-8")

    _validate_site(site, transformed)
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, default=Path("website"))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()

    changed = synchronize_site(args.site, write=args.write)
    if args.check and changed:
        raise SystemExit(
            "Research III website synchronization required for: " + ", ".join(changed)
        )
    if changed:
        action = "updated" if args.write else "would update"
        print(f"{action}: {', '.join(changed)}")
    else:
        print("Research III website surfaces are synchronized.")


if __name__ == "__main__":
    main()
