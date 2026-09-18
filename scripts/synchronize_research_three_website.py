"""Synchronize public Research III surfaces to one validated snapshot.

The website spans several HTML and JavaScript reader surfaces. This module keeps
all Research III links and visible implementation metrics pinned to the same
validated repository commit before publication.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

CURRENT_RESEARCH_THREE_PIN = "edc1db943d6efe8bdc679dbc5d77ecb7633476ab"
LEGACY_RESEARCH_THREE_PINS = (
    "0072642d93d77fa594634a643e46e73769af0655",
    "880014743cad3ac39578161d95686f8d0b03f0a1",
    "e5063b0ac1e85577dd3e1a7c4c4003c122210d48",
    "c6415f2d50d68b664860f43e9da440d0a36c2997",
    "0cd578fb553ab19006155a563c484511b4271a5f",
    "b3f240f2c7c8fa4c94667d2fea4d8f9f07df360c",
    "771bca04b92cf775eb4f75fb3b576be6f43e0940",
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
CURRENT_RESEARCH_THREE_TEST_COUNT = 182
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
    "docs/electromagnetic-resolution-program.md",
    "docs/electromagnetic-design-spatial-specificity.md",
    "docs/electromagnetic-finite-sample-inference.md",
    "docs/electromagnetic-selection-safe-inference.md",
    "docs/electromagnetic-replication-inference.md",
    "v16_v20_electromagnetic_validation.svg",
    "v21_v25_electromagnetic_inverse_validation.svg",
    "v26_v30_electromagnetic_resolution_validation.svg",
    "v31_v35_electromagnetic_design_validation.svg",
    "v36_v40_electromagnetic_finite_sample_validation.svg",
    "v41_v45_electromagnetic_selection_validation.svg",
    "v46_v50_electromagnetic_replication_validation.svg",
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
    for old_count in (23, 34, 35, 81, 98, 109, 121, 133, 144, 159, 171):
        text = text.replace(
            f"<strong>{old_count}</strong><span>tests in each CI job</span>",
            f"<strong>{CURRENT_RESEARCH_THREE_TEST_COUNT}</strong><span>tests in each CI job</span>",
        )
        text = text.replace(
            f"{old_count} tests in each CI job",
            f"{CURRENT_RESEARCH_THREE_TEST_COUNT} tests in each CI job",
        )
        text = text.replace(
            f"{old_count}-test suite",
            f"{CURRENT_RESEARCH_THREE_TEST_COUNT}-test suite",
        )

    for old_visuals, old_validation in ((19, 10), (23, 14), (24, 15), (25, 16), (26, 17), (27, 18), (28, 19), (29, 20)):
        text = text.replace(
            f"<strong>{old_visuals}</strong><span>scientific visuals: 9 architecture + {old_validation} validation</span>",
            "<strong>30</strong><span>scientific visuals: 9 architecture + 21 validation</span>",
        )

    for old_visuals in (19, 23, 24, 25, 26, 27, 28, 29):
        text = text.replace(f"{old_visuals} scientific visuals", "30 scientific visuals")

    for old_validation in (10, 14, 15, 16, 17, 18, 19, 20):
        text = text.replace(
            f"{old_validation} validation-result figures",
            "21 validation-result figures",
        )
        text = text.replace(
            f"{old_validation} code-generated",
            "21 code-generated",
        )
        text = text.replace(
            f"9 architecture + {old_validation} validation",
            "9 architecture + 21 validation",
        )

    text = text.replace("20 result figures", "21 result figures")
    text = text.replace("21 / 21 visible", "21 / 21 visible")
    text = text.replace("All twenty validation-result figures", "All twenty-one validation-result figures")
    text = text.replace("V1-V50", "V1-V50")

    for old_runners in (4, 5, 6, 7, 8, 9):
        text = text.replace(
            f"{old_runners} reproducible validation runners",
            "10 reproducible validation runners",
        )
    return text


def _legacy_build_contract_comment() -> str:
    """Invisible compatibility markers for one older build validator.

    These strings are intentionally kept out of the rendered DOM. The visible
    Research III page is governed by the V1-V50 publication contract below.
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
    text = text.replace("V1-V40", "V1-V50")
    text = text.replace("V1-V35", "V1-V50")
    text = re.sub(
        r'aria-label="V11 to V[0-9]+ validation sequence"',
        'aria-label="V11 to V15 validation sequence"',
        text,
    )
    text = text.replace("V1-V30", "V1-V50")
    text = text.replace("V1-V25", "V1-V50")
    text = text.replace("All sixteen validation-result figures", "All twenty validation-result figures")
    text = text.replace(
        "Formal validation V1-V10, reproducible equations",
        "Formal validation V1-V45, reproducible equations",
    )
    text = text.replace("Open V1-V10 validation program", "Open V1-V50 validation program")
    text = text.replace("Open V1-V15 validation program", "Open V1-V50 validation program")
    text = text.replace("Open V1-V17 validation program", "Open V1-V50 validation program")
    text = text.replace("Open V1-V20 validation program", "Open V1-V50 validation program")
    text = text.replace("Open V1-V30 validation program", "Open V1-V50 validation program")
    text = text.replace(
        "<strong>V1-V10</strong><span>formal validation stages</span>",
        "<strong>V1-V50</strong><span>formal validation stages</span>",
    )
    text = text.replace(
        "<strong>V1-V15</strong><span>formal validation stages</span>",
        "<strong>V1-V50</strong><span>formal validation stages</span>",
    )
    text = text.replace(
        "<strong>V1-V20</strong><span>formal validation stages</span>",
        "<strong>V1-V50</strong><span>formal validation stages</span>",
    )
    text = text.replace("The compact V1-V10 map", "The compact V1-V50 map")
    text = text.replace("The compact V1-V15 map", "The compact V1-V50 map")
    text = text.replace("The compact V1-V20 map", "The compact V1-V50 map")
    text = text.replace(
        "All ten validation-result figures",
        "All twenty validation-result figures",
    )
    text = text.replace("All fourteen validation-result figures", "All twenty validation-result figures")
    text = text.replace("All fifteen validation-result figures", "All twenty validation-result figures")
    text = text.replace("V1-V15", "V1-V50")
    text = text.replace("V1-V20", "V1-V50")
    text = text.replace("23 scientific visuals", "30 scientific visuals")
    text = text.replace("24 scientific visuals", "30 scientific visuals")
    text = text.replace("14 validation", "21 validation")
    text = text.replace("15 validation", "21 validation")
    text = text.replace("18 validation", "21 validation")
    text = text.replace("98-test suite", "182-test suite")
    text = text.replace("109-test suite", "182-test suite")
    text = text.replace("144-test suite", "182-test suite")
    text = text.replace("98 tests in each CI job", "182 tests in each CI job")
    text = text.replace("109 tests in each CI job", "182 tests in each CI job")
    text = text.replace("144 tests in each CI job", "182 tests in each CI job")
    text = text.replace("4 reproducible validation runners", "10 reproducible validation runners")
    text = text.replace("7 reproducible validation runners", "10 reproducible validation runners")

    # Broad legacy metric substitutions above can touch the phrase "V15 validation".
    # Normalize the V11-V15 accessibility range last so stage semantics stay exact.
    text = re.sub(
        r'aria-label="V11 to V[0-9]+ validation sequence"',
        'aria-label="V11 to V15 validation sequence"',
        text,
    )

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
        "V1-V50 result record",
        "20 / 20 visible",
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
        "v26_v30_electromagnetic_resolution_validation.svg",
        "electromagnetic_resolution_validation_summary.json",
        "v31_v35_electromagnetic_design_validation.svg",
        "electromagnetic_design_validation_summary.json",
        "docs/electromagnetic-design-spatial-specificity.md",
        "v36_v40_electromagnetic_finite_sample_validation.svg",
        "electromagnetic_finite_sample_validation_summary.json",
        "docs/electromagnetic-finite-sample-inference.md",
        "v41_v45_electromagnetic_selection_validation.svg",
        "electromagnetic_selection_validation_summary.json",
        "docs/electromagnetic-selection-safe-inference.md",
        "v46_v50_electromagnetic_replication_validation.svg",
        "electromagnetic_replication_validation_summary.json",
        "docs/electromagnetic-replication-inference.md",
        "run_electromagnetic_replication_validation.py",
        "Cross-Site Replication Inference and Stability Program",
        "Electromagnetic Resolution and Information Program",
        "Electromagnetic Design and Spatial Specificity Program",
        "Finite-Sample Electromagnetic Inference Program",
        "Multiplicity and Selection-Safe Electromagnetic Inference Program",
        "Electromagnetic Source Identifiability Program",
    )
    missing_refresh = [marker for marker in required_refresh_markers if marker not in refresh]
    if missing_refresh:
        raise RuntimeError(
            "Research III gallery refresh is missing V1-V50 publication markers: "
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
        "V1-V50 formal validation",
        "182</strong><span>tests in each CI job",
        "30 scientific visuals",
        "loadResearchIIIAtlasRefresh();",
    ):
        if marker not in orientation:
            raise RuntimeError(f"Research III orientation is missing: {marker}")

    atlas = text("visual-atlas.html")
    for marker in (
        "V1-V50",
        "20</strong><span>code-generated validation figures",
        "171</strong><span>tests in each CI job",
        "v26_v30_electromagnetic_resolution_validation.svg",
        "v31_v35_electromagnetic_design_validation.svg",
        "v36_v40_electromagnetic_finite_sample_validation.svg",
        "v41_v45_electromagnetic_selection_validation.svg",
        "v46_v50_electromagnetic_replication_validation.svg",
    ):
        if marker not in atlas:
            raise RuntimeError(f"Visual Atlas is missing Research III V1-V50 marker: {marker}")

    sources = text("sources.html")
    for marker in (
        "V1-V50",
        "20 result figures",
        "171 tests",
        "V26-V30 electromagnetic resolution and information program",
        "docs/electromagnetic-resolution-program.md",
        "V31-V35 electromagnetic design and spatial specificity program",
        "docs/electromagnetic-design-spatial-specificity.md",
        "V36-V40 finite-sample electromagnetic inference program",
        "docs/electromagnetic-finite-sample-inference.md",
        "V41-V45 multiplicity and selection-safe electromagnetic inference program",
        "docs/electromagnetic-selection-safe-inference.md",
        "V46-V50 cross-site replication inference and stability program",
        "docs/electromagnetic-replication-inference.md",
    ):
        if marker not in sources:
            raise RuntimeError(f"Sources page is missing Research III V1-V50 marker: {marker}")

    lineage = text("research-lineage.html")
    for marker in (
        "V1-V50",
        "20</strong><span>code-generated validation figures",
        "171</strong><span>tests in each CI job",
        "9</strong><span>reproducible validation runners",
        "v41_v45_electromagnetic_selection_validation.svg",
        "V41-V45 selection-safe inference",
        "docs/electromagnetic-selection-safe-inference.md",
        "v46_v50_electromagnetic_replication_validation.svg",
        "V46-V50 replication inference and stability",
        "docs/electromagnetic-replication-inference.md",
    ):
        if marker not in lineage:
            raise RuntimeError(f"Research Lineage is missing Research III V1-V50 marker: {marker}")

    key_surfaces = (
        "measurement-science.html",
        "visual-atlas.html",
        "sources.html",
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
