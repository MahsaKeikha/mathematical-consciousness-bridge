"""Synchronize the public website with the validated Research III snapshot.

This script keeps the cross-repository handoff auditable. It updates pinned
Research III asset references, refreshes reader-facing implementation claims,
collapses duplicated current-frontier source markers, and checks that the
Research III surfaces describe one exact validated commit coherently.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

CURRENT_RESEARCH_THREE_PIN = "5d1d979231aed62fde34383281fa8f252a3d2fa7"
LEGACY_RESEARCH_THREE_PINS = (
    "b874eda1f6940f5601b7f89200b6a276b5ecbbc3",
    "8bbb7b029d70c43cc6a9dbf8b44dfe5069d0993d",
    "7a106820158e0d33ea651f7cdeaa505206f1ccc7",
)
CURRENT_HOME_MARKER = "<!-- current-frontier-home: P93 -->"

MEASUREMENT_SCIENCE_REPLACEMENTS = {
    '<div><strong>23</strong><span>tests in each CI job</span></div>':
        '<div><strong>35</strong><span>tests in each CI job</span></div>',
    '<div><strong>34</strong><span>tests in each CI job</span></div>':
        '<div><strong>35</strong><span>tests in each CI job</span></div>',
    'The repository policy audit, source compilation, 23 tests, and Ruff passed on Python 3.10, 3.11, and 3.12 before the framework was promoted to <code>main</code>.':
        'The repository policy audit, source compilation, 35 tests, and Ruff passed on Python 3.10, 3.11, and 3.12 before the framework was promoted to <code>main</code>.',
    'The repository policy audit, source compilation, 34 tests, and Ruff passed on Python 3.10, 3.11, and 3.12 before the framework was promoted to <code>main</code>.':
        'The repository policy audit, source compilation, 35 tests, and Ruff passed on Python 3.10, 3.11, and 3.12 before the framework was promoted to <code>main</code>.',
    '<p><strong>Software scaffolds:</strong> transparent likelihood-ratio fusion under an explicit independence assumption, evidence-profile objects, and structural-alignment tools are implemented and tested.</p>':
        '<p><strong>Software scaffolds:</strong> conditional-independence likelihood-ratio fusion, dependence-robust partial identification with sharp Fr&eacute;chet-Hoeffding bounds, evidence-profile objects, and structural-alignment tools are implemented and tested.</p>',
    '<a href="https://github.com/MahsaKeikha/consciousness-measurement-science/blob/5d1d979231aed62fde34383281fa8f252a3d2fa7/docs/software-guide.md"><h3>Software guide</h3><p>What the current evidence, profile, and structural-alignment modules do and do not implement.</p></a>':
        '<a href="https://github.com/MahsaKeikha/consciousness-measurement-science/blob/5d1d979231aed62fde34383281fa8f252a3d2fa7/docs/software-guide.md"><h3>Software guide</h3><p>What the current evidence, profile, partial-identification, and structural-alignment modules do and do not implement.</p></a>',
    '<a href="https://github.com/MahsaKeikha/consciousness-measurement-science/tree/5d1d979231aed62fde34383281fa8f252a3d2fa7/tests"><h3>Test suite</h3><p>Unit tests for evidence fusion, profile semantics, structural alignment, schemas, and repository policy.</p></a>':
        '<a href="https://github.com/MahsaKeikha/consciousness-measurement-science/tree/5d1d979231aed62fde34383281fa8f252a3d2fa7/tests"><h3>Test suite</h3><p>Unit tests for point fusion, dependence-robust partial identification, profile semantics, structural alignment, schemas, repository policy, and measurement-figure geometry.</p></a>',
    '<div class="boundary">\n        <p><strong>Current implementation boundary:</strong> the likelihood-ratio fusion helper assumes conditional independence only when the caller explicitly declares it. It is a transparent research scaffold, not the final dependence-robust multimodal inference model planned by the roadmap.</p>\n      </div>':
        '<div class="boundary">\n        <p><strong>Two implemented fusion regimes:</strong> when conditional independence is scientifically justified and explicitly declared, the point-fusion helper returns a likelihood ratio and posterior point estimate. When dependence is unknown, the partial-identification module instead uses sharp marginal-only Fr&eacute;chet-Hoeffding bounds to return compatible intervals for the observed pattern probability, likelihood ratio, and posterior.</p>\n        <p>An interval as wide as <code>[0,1]</code> is a valid scientific result: it means the available marginal calibration does not identify the posterior without stronger dependence information. Infinite likelihood-ratio bounds are handled explicitly rather than clipped into a convenient finite score.</p>\n        <p><a href="https://github.com/MahsaKeikha/consciousness-measurement-science/blob/5d1d979231aed62fde34383281fa8f252a3d2fa7/docs/partial-identification.md">Open the dependence-robust partial-identification derivation &rarr;</a></p>\n      </div>',
}

MEASUREMENT_SCIENCE_REQUIRED_MARKERS = (
    '<strong>35</strong><span>tests in each CI job</span>',
    'dependence-robust partial identification with sharp Fr&eacute;chet-Hoeffding bounds',
    '<strong>Two implemented fusion regimes:</strong>',
    'An interval as wide as <code>[0,1]</code> is a valid scientific result',
    'docs/partial-identification.md',
)


def _replace_research_three_pins(text: str) -> str:
    for legacy in LEGACY_RESEARCH_THREE_PINS:
        text = text.replace(legacy, CURRENT_RESEARCH_THREE_PIN)
    return text


def _synchronize_measurement_science(text: str) -> str:
    text = _replace_research_three_pins(text)
    for old, new in MEASUREMENT_SCIENCE_REPLACEMENTS.items():
        text = text.replace(old, new)
    return text


def _collapse_frontier_markers(text: str) -> str:
    marker_pattern = re.compile(
        rf"(?:{re.escape(CURRENT_HOME_MARKER)}\s*){{2,}}",
        flags=re.MULTILINE,
    )
    return marker_pattern.sub(f"{CURRENT_HOME_MARKER}\n", text)


def _synchronize_index(text: str) -> str:
    text = _replace_research_three_pins(text)
    return _collapse_frontier_markers(text)


def synchronize_site(site: Path, *, write: bool) -> list[str]:
    """Return changed paths and optionally write synchronized source files."""

    targets = {
        "measurement-science.html": _synchronize_measurement_science,
        "research-lineage.html": _replace_research_three_pins,
        "index.html": _synchronize_index,
    }
    changed: list[str] = []

    for relative, transform in targets.items():
        path = site / relative
        if not path.is_file():
            raise FileNotFoundError(f"missing website surface: {path}")
        original = path.read_text(encoding="utf-8")
        updated = transform(original)
        if updated != original:
            changed.append(relative)
            if write:
                path.write_text(updated, encoding="utf-8")

    validation_text = {
        name: (site / name).read_text(encoding="utf-8")
        for name in targets
    }
    if validation_text["index.html"].count(CURRENT_HOME_MARKER) != 1:
        raise RuntimeError(
            f"homepage must contain exactly one current frontier source marker: {CURRENT_HOME_MARKER}"
        )

    for surface in ("measurement-science.html", "research-lineage.html", "index.html"):
        text = validation_text[surface]
        if CURRENT_RESEARCH_THREE_PIN not in text:
            raise RuntimeError(
                f"{surface} is not pinned to Research III {CURRENT_RESEARCH_THREE_PIN}"
            )
        stale = [pin for pin in LEGACY_RESEARCH_THREE_PINS if pin in text]
        if stale:
            raise RuntimeError(f"{surface} still contains stale Research III pins: {stale}")

    measurement_text = validation_text["measurement-science.html"]
    missing = [
        marker for marker in MEASUREMENT_SCIENCE_REQUIRED_MARKERS
        if marker not in measurement_text
    ]
    if missing:
        raise RuntimeError(
            "measurement-science reader surface is missing current Research III markers: "
            + repr(missing)
        )
    if "23</strong><span>tests in each CI job" in measurement_text:
        raise RuntimeError("measurement-science still reports the obsolete 23-test count")
    if "34</strong><span>tests in each CI job" in measurement_text:
        raise RuntimeError("measurement-science still reports the obsolete 34-test count")
    if "planned by the roadmap" in measurement_text:
        raise RuntimeError("measurement-science still describes implemented partial identification as planned")

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
