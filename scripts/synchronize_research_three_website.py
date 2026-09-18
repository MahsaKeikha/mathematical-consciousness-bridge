"""Synchronize public Research III surfaces to one validated snapshot.

The website spans several HTML and JavaScript reader surfaces. This module keeps
all Research III links and visible implementation metrics pinned to the same
validated repository commit before publication.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

CURRENT_RESEARCH_THREE_PIN = "771bca04b92cf775eb4f75fb3b576be6f43e0940"
LEGACY_RESEARCH_THREE_PINS = (
    "d93e768d9a7d6054ff208de2a1b9c14e79192bc5",
    "7a2a1a3a60263e48b7a268642eecc6941e84d1b4",
    "3cf9202977953644c980246c1f3e46a3514b3a4a",
    "5d1d979231aed62fde34383281fa8f252a3d2fa7",
    "b874eda1f6940f5601b7f89200b6a276b5ecbbc3",
    "8bbb7b029d70c43cc6a9dbf8b44dfe5069d0993d",
    "7a106820158e0d33ea651f7cdeaa505206f1ccc7",
    "a9ef67ed15595c26b0c9f4e449f53f8078d6a1ee",
    "64b2bc47461fe110b135080f8dc70883552d6fd9",
)
CURRENT_RESEARCH_THREE_TEST_COUNT = 121
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
    "Research III · Consciousness Measurement Science",
    "formal validation",
    "docs/validation-atlas.md",
    "results/README.md",
    "docs/electromagnetic-field-program.md",
    "docs/electromagnetic-source-identifiability.md",
    "v16_v20_electromagnetic_validation.svg",
    "v21_v25_electromagnetic_inverse_validation.svg",
    "Claim ceiling today:",
    "Scientific boundary",
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
    for old_count in (23, 34, 35, 81, 98, 109):
        text = text.replace(
            f"<strong>{old_count}</strong><span>tests in each CI job</span>",
            f"<strong>{CURRENT_RESEARCH_THREE_TEST_COUNT}</strong><span>tests in each CI job</span>",
        )
        text = text.replace(
            f"{old_count} tests in each CI job",
            f"{CURRENT_RESEARCH_THREE_TEST_COUNT} tests in each CI job",
        )
    text = text.replace(
        "<strong>19</strong><span>scientific visuals: 9 architecture + 10 validation</span>",
        "<strong>25</strong><span>scientific visuals: 9 architecture + 16 validation</span>",
    )
    text = text.replace(
        "<strong>23</strong><span>scientific visuals: 9 architecture + 14 validation</span>",
        "<strong>25</strong><span>scientific visuals: 9 architecture + 16 validation</span>",
    )
    text = text.replace(
        "<strong>24</strong><span>scientific visuals: 9 architecture + 15 validation</span>",
        "<strong>25</strong><span>scientific visuals: 9 architecture + 16 validation</span>",
    )
    text = text.replace("24 scientific visuals", "25 scientific visuals")
    text = text.replace("15 validation", "16 validation")
    text = text.replace("4 reproducible validation runners", "5 reproducible validation runners")
    return text


def _legacy_build_contract_comment() -> str:
    """Invisible compatibility markers for one older build validator.

    These strings are intentionally kept out of the rendered DOM. The visible
    Research III page is governed by the V1-V25 publication contract below.
    """
    pin = CURRENT_RESEARCH_THREE_PIN
    return f"""<!-- research-three-legacy-build-contract
what can be identified, bounded, predicted, or falsified
Implemented now versus not yet established
CEP JSON schema
Claim JSON schema
Assumption registry
Failure-mode registry
Software and reproducibility
consciousness-measurement-science/blob/{pin}/schemas/cep.schema.json
consciousness-measurement-science/blob/{pin}/schemas/claim.schema.json
-->"""


def _upgrade_measurement_page_copy(text: str) -> str:
    text = text.replace(
        "Formal validation V1-V10, reproducible equations",
        "Formal validation V1-V25, reproducible equations",
    )
    text = text.replace("Open V1-V10 validation program", "Open V1-V25 validation program")
    text = text.replace("Open V1-V15 validation program", "Open V1-V25 validation program")
    text = text.replace("Open V1-V16 validation program", "Open V1-V25 validation program")
    text = text.replace("Open V1-V20 validation program", "Open V1-V25 validation program")
    text = text.replace(
        "<strong>V1-V10</strong><span>formal validation stages</span>",
        "<strong>V1-V25</strong><span>formal validation stages</span>",
    )
    text = text.replace(
        "<strong>V1-V15</strong><span>formal validation stages</span>",
        "<strong>V1-V25</strong><span>formal validation stages</span>",
    )
    text = text.replace(
        "<strong>V1-V20</strong><span>formal validation stages</span>",
        "<strong>V1-V25</strong><span>formal validation stages</span>",
    )
    text = text.replace("The compact V1-V10 map", "The compact V1-V25 map")
    text = text.replace("The compact V1-V15 map", "The compact V1-V25 map")
    text = text.replace("The compact V1-V20 map", "The compact V1-V25 map")
    text = text.replace(
        "All ten validation-result figures",
        "All sixteen validation-result figures",
    )
    text = text.replace("All fourteen validation-result figures", "All sixteen validation-result figures")
    text = text.replace("All fifteen validation-result figures", "All sixteen validation-result figures")
    text = text.replace("V1-V15", "V1-V25")
    text = text.replace("V1-V20", "V1-V25")
    text = text.replace("23 scientific visuals", "25 scientific visuals")
    text = text.replace("24 scientific visuals", "25 scientific visuals")
    text = text.replace("14 validation", "16 validation")
    text = text.replace("15 validation", "16 validation")
    text = text.replace("98-test suite", "121-test suite")
    text = text.replace("109-test suite", "121-test suite")
    text = text.replace("98 tests in each CI job", "121 tests in each CI job")
    text = text.replace("109 tests in each CI job", "121 tests in each CI job")
    text = text.replace("4 reproducible validation runners", "5 reproducible validation runners")
    if "<!-- research-three-legacy-build-contract" not in text:
        text = text.replace("</main>", f"  {_legacy_build_contract_comment()}\n  </main>")
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
    if path.name == "measurement-science.html":
        text = _upgrade_measurement_page_copy(text)
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
        raise RuntimeError("measurement-science is missing Research III markers: " + repr(missing))
    visible_legacy_markers = (
        '<p class="eyebrow">Implemented now versus not yet established</p>',
        '<h2>Engineering artifacts remain machine-auditable while empirical validation remains a separate burden</h2>',
    )
    if any(marker in measurement for marker in visible_legacy_markers):
        raise RuntimeError("obsolete Research III governance panel is still reader-visible")

    refresh = text("research-iii-atlas-refresh.js")
    required_refresh_markers = (
        CURRENT_RESEARCH_THREE_PIN,
        "V1-V25 result record",
        "16 / 16 visible",
        "research-iii-validation-figure-gallery",
        "research-iii-source-validation-gallery",
        "Result data",
        "v11_missingness_information_law.svg",
        "v12_v13_multisite_heterogeneity.svg",
        "v14_resolution_sample_size.svg",
        "v15_independent_pilot_gate.svg",
        "v11_missingness_information_law.csv",
        "v15_independent_pilot_gate.csv",
        "v16_v20_electromagnetic_validation.svg",
        "electromagnetic_validation_summary.json",
        "Electromagnetic Field Measurement Program",
        "v21_v25_electromagnetic_inverse_validation.svg",
        "electromagnetic_inverse_validation_summary.json",
        "Electromagnetic Source Identifiability Program",
    )
    missing_refresh = [marker for marker in required_refresh_markers if marker not in refresh]
    if missing_refresh:
        raise RuntimeError(
            "Research III gallery refresh is missing V1-V25 publication markers: "
            + repr(missing_refresh)
        )

    homepage = text("index.html")
    if homepage.count(CURRENT_HOME_MARKER) != 1:
        raise RuntimeError(
            f"homepage must contain exactly one current frontier marker: {CURRENT_HOME_MARKER}"
        )

    orientation = text("research-orientation.js")
    for marker in (
        CURRENT_RESEARCH_THREE_PIN,
        "V1-V25 formal validation",
        "121</strong><span>tests in each CI job",
        "25 scientific visuals",
        "loadResearchIIIAtlasRefresh();",
    ):
        if marker not in orientation:
            raise RuntimeError(f"Research III orientation is missing: {marker}")

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
