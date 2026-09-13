"""Synchronize the public website to the validated Research III snapshot.

This script keeps the Research III reader pages pinned to one immutable commit,
adds the current implementation and open-boundary summary, and removes duplicate
Research II frontier markers from the homepage source.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"
MEASUREMENT_REPO = "https://github.com/MahsaKeikha/consciousness-measurement-science"
RESEARCH_THREE_PIN = "7a106820158e0d33ea651f7cdeaa505206f1ccc7"
OLD_RESEARCH_THREE_PINS = ("8bbb7b029d70c43cc6a9dbf8b44dfe5069d0993d",)

SNAPSHOT_START = "<!-- research-iii-snapshot:start -->"
SNAPSHOT_END = "<!-- research-iii-snapshot:end -->"
LINEAGE_START = "<!-- research-iii-lineage-snapshot:start -->"
LINEAGE_END = "<!-- research-iii-lineage-snapshot:end -->"

MEASUREMENT_SNAPSHOT = f"""{SNAPSHOT_START}
    <section id="research-iii-snapshot">
      <div class="section-head">
        <p class="eyebrow">Validated Research III snapshot</p>
        <h2>What is implemented now, and what is not yet established</h2>
        <p>This website is pinned to Research III commit <code>{RESEARCH_THREE_PIN}</code>. The repository is a reproducible measurement-science framework, not a validated universal consciousness instrument.</p>
      </div>
      <div class="status-grid" aria-label="Research III validation status">
        <div><strong>23</strong><span>automated tests</span></div>
        <div><strong>3</strong><span>Python versions validated</span></div>
        <div><strong>2</strong><span>machine-readable evidence schemas</span></div>
        <div><strong>Green</strong><span>policy, compile, tests, and Ruff</span></div>
      </div>
      <div class="two-col">
        <article class="card">
          <p class="eyebrow">Implemented now</p>
          <h3>A complete research contract for measurement claims</h3>
          <p>The repository now includes the target taxonomy, Consciousness Evidence Profile, assumption registry, failure-mode registry, claim ladder, preregistration template, experimental program, statistical validation plan, clinical and ethical boundaries, structural-measurement arm, software scaffolds, machine-readable claim and CEP schemas, worked examples, and repository-wide publication checks.</p>
          <div class="source-grid">
            <a href="{MEASUREMENT_REPO}/blob/{RESEARCH_THREE_PIN}/docs/start-here.md"><h3>Start Here</h3><p>Read the research program in the intended order.</p></a>
            <a href="{MEASUREMENT_REPO}/blob/{RESEARCH_THREE_PIN}/docs/README.md"><h3>Documentation index</h3><p>Navigate every major scientific and reproducibility document.</p></a>
            <a href="{MEASUREMENT_REPO}/blob/{RESEARCH_THREE_PIN}/docs/assumption-registry.md"><h3>Assumption registry</h3><p>See which conclusions depend on which assumptions.</p></a>
            <a href="{MEASUREMENT_REPO}/blob/{RESEARCH_THREE_PIN}/docs/failure-modes.md"><h3>Failure modes</h3><p>See how the program handles misleading or uninterpretable evidence.</p></a>
            <a href="{MEASUREMENT_REPO}/blob/{RESEARCH_THREE_PIN}/docs/reproducibility.md"><h3>Reproducibility</h3><p>Inspect the computational and publication contract.</p></a>
            <a href="{MEASUREMENT_REPO}/blob/{RESEARCH_THREE_PIN}/docs/software-guide.md"><h3>Software guide</h3><p>Inspect the current executable research scaffolds.</p></a>
          </div>
        </article>
        <article class="card">
          <p class="eyebrow">Not yet established</p>
          <h3>The scientific claims that still require empirical evidence</h3>
          <p>No universal scalar, biomarker, bridge law, necessary-and-sufficient physical condition, substrate-independent threshold, or direct third-person measurement of qualia has been established. Those remain research targets. Clinical use is explicitly prohibited by the current schema and documentation.</p>
          <p>The next evidence-bearing steps are prospective benchmark data, cross-state and held-out-site transport, perturbational validation, multimodal dependence analysis, structural prediction on held-out experiences, and preregistered theory-discriminating experiments.</p>
          <div class="source-grid">
            <a href="{MEASUREMENT_REPO}/blob/{RESEARCH_THREE_PIN}/schemas/cep.schema.json"><h3>CEP schema</h3><p>Machine-readable target-specific evidence records.</p></a>
            <a href="{MEASUREMENT_REPO}/blob/{RESEARCH_THREE_PIN}/schemas/claim.schema.json"><h3>Claim schema</h3><p>Machine-readable scientific claim boundaries.</p></a>
            <a href="{MEASUREMENT_REPO}/blob/{RESEARCH_THREE_PIN}/examples/cep_example.json"><h3>CEP example</h3><p>A worked evidence-profile record.</p></a>
            <a href="{MEASUREMENT_REPO}/blob/{RESEARCH_THREE_PIN}/examples/claim_example.json"><h3>Claim example</h3><p>A worked claim-registry record.</p></a>
          </div>
        </article>
      </div>
      <div class="boundary">
        <p><strong>Validation record:</strong> on Python 3.10, 3.11, and 3.12, the repository policy audit, byte-code compilation, 23-test suite, and Ruff check all passed for this pinned snapshot.</p>
      </div>
    </section>
{SNAPSHOT_END}"""

LINEAGE_SNAPSHOT = f"""{LINEAGE_START}
      <div class="boundary lineage-boundary research-iii-validation">
        <h2>Research III now has a validated reproducible repository snapshot</h2>
        <p>The public measurement program is pinned here to commit <code>{RESEARCH_THREE_PIN}</code>. That snapshot contains the Start Here guide, documentation index, assumption and failure-mode registries, CEP and claim schemas, worked examples, reproducibility and software guides, and a 23-test suite. Its policy audit, compilation, tests, and Ruff checks pass on Python 3.10, 3.11, and 3.12.</p>
        <p><strong>Boundary:</strong> this is a completed measurement-research framework, not evidence that a universal consciousness meter or direct qualia measurement has already been achieved.</p>
      </div>
{LINEAGE_END}"""


def _pin_research_three_links(text: str) -> str:
    for old_pin in OLD_RESEARCH_THREE_PINS:
        text = text.replace(old_pin, RESEARCH_THREE_PIN)
    return text.replace(
        f"{MEASUREMENT_REPO}/blob/main/",
        f"{MEASUREMENT_REPO}/blob/{RESEARCH_THREE_PIN}/",
    )


def _replace_or_insert_block(
    text: str,
    start_marker: str,
    end_marker: str,
    block: str,
    insertion_token: str,
) -> str:
    pattern = re.compile(
        rf"{re.escape(start_marker)}.*?{re.escape(end_marker)}",
        flags=re.DOTALL,
    )
    if pattern.search(text):
        return pattern.sub(block, text, count=1)
    if insertion_token not in text:
        raise RuntimeError(f"website insertion token not found: {insertion_token!r}")
    return text.replace(insertion_token, f"{block}\n\n{insertion_token}", 1)


def _synchronize_measurement_page(text: str) -> str:
    text = _pin_research_three_links(text)
    return _replace_or_insert_block(
        text,
        SNAPSHOT_START,
        SNAPSHOT_END,
        MEASUREMENT_SNAPSHOT,
        '    <section class="dark-section">',
    )


def _synchronize_lineage_page(text: str) -> str:
    text = _pin_research_three_links(text)
    section_token = '    <section id="research-iii">'
    if section_token not in text:
        raise RuntimeError("Research III lineage section not found")
    head, tail = text.split(section_token, 1)
    tail = _replace_or_insert_block(
        tail,
        LINEAGE_START,
        LINEAGE_END,
        LINEAGE_SNAPSHOT,
        '      <div class="boundary lineage-boundary">',
    )
    return head + section_token + tail


def _synchronize_homepage(text: str) -> str:
    marker = "<!-- current-frontier-home: P88 -->"
    pattern = re.compile(rf"(?:{re.escape(marker)}\s*)+")
    text = pattern.sub(f"{marker}\n", text, count=1)
    if text.count(marker) != 1:
        raise RuntimeError("Homepage must contain exactly one P88 frontier marker")
    return text


def _planned_text(path: Path, transform) -> tuple[bool, str]:
    original = path.read_text(encoding="utf-8")
    updated = transform(original)
    return original != updated, updated


def synchronize(check: bool = False) -> list[str]:
    targets = (
        (WEBSITE / "measurement-science.html", _synchronize_measurement_page),
        (WEBSITE / "research-lineage.html", _synchronize_lineage_page),
        (WEBSITE / "index.html", _synchronize_homepage),
    )
    changed: list[str] = []
    planned: dict[Path, str] = {}
    for path, transform in targets:
        differs, updated = _planned_text(path, transform)
        planned[path] = updated
        if differs:
            changed.append(str(path.relative_to(ROOT)))
            if not check:
                path.write_text(updated, encoding="utf-8")

    measurement = planned[WEBSITE / "measurement-science.html"]
    lineage = planned[WEBSITE / "research-lineage.html"]
    homepage = planned[WEBSITE / "index.html"]

    required_measurement = (
        RESEARCH_THREE_PIN,
        "Implemented now",
        "Not yet established",
        "23</strong><span>automated tests",
        "schemas/cep.schema.json",
        "schemas/claim.schema.json",
        "docs/start-here.md",
        "docs/assumption-registry.md",
        "docs/failure-modes.md",
        "docs/reproducibility.md",
        "docs/software-guide.md",
    )
    missing = [token for token in required_measurement if token not in measurement]
    if missing:
        raise RuntimeError(f"Research III website synchronization missing: {missing}")
    if any(old_pin in measurement or old_pin in lineage for old_pin in OLD_RESEARCH_THREE_PINS):
        raise RuntimeError("Research III website still contains a stale pinned commit")
    if f"{MEASUREMENT_REPO}/blob/main/" in measurement or f"{MEASUREMENT_REPO}/blob/main/" in lineage:
        raise RuntimeError("Research III documentation links are not pinned")
    if LINEAGE_START not in lineage or "23-test suite" not in lineage:
        raise RuntimeError("Research III lineage validation snapshot is missing")
    if homepage.count("<!-- current-frontier-home: P88 -->") != 1:
        raise RuntimeError("Homepage contains duplicate P88 frontier markers")

    if check and changed:
        raise RuntimeError(
            "Research III website source is not synchronized: " + ", ".join(changed)
        )
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    changed = synchronize(check=args.check)
    if args.check:
        print("Research III website synchronization check passed.")
    elif changed:
        print("Synchronized Research III website: " + ", ".join(changed))
    else:
        print("Research III website already synchronized.")


if __name__ == "__main__":
    main()
