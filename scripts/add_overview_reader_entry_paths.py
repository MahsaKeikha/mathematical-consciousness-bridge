"""Add reader-specific entry paths to the Overview page.

This is a temporary, idempotent migration helper for the Overview reader-path
change. It inserts the reader-path section between the three-stage project
journey and the current P88 frontier, then adds a focused publication contract.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "website" / "index.html"
CONTRACT = ROOT / "tests" / "test_publication_contract_v2.py"

SECTION = '''    <section id="reader-paths">
      <div class="section-head">
        <p class="eyebrow">Choose where to start</p>
        <h2>Enter the program through the question you care about.</h2>
        <p>The research spans physical-system identification, bridge mathematics, measurement science, and reproducibility. You do not need to read it in proposition order. Choose the route that matches what you want to understand or audit first.</p>
      </div>
      <div class="research-dashboard reader-entry-dashboard" aria-label="Reader-specific entry paths through the research program">
        <article class="card">
          <p class="eyebrow">New to the program</p>
          <h3>Understand the scientific question first</h3>
          <p>Start with the problem, the three-research lineage, and the boundary between what has been established and what remains open.</p>
          <p><a class="button primary" href="start-here.html">Start Here</a> <a class="button" href="plain-language.html">Plain language</a> <a class="button" href="research-lineage.html">Research lineage</a></p>
        </article>
        <article class="card">
          <p class="eyebrow">Mathematics and theorem audit</p>
          <h3>Follow definitions, proofs, equations, and provenance</h3>
          <p>Use the dependency-aware Research II map, inspect the current P88 theorem, and trace each major claim back to its source and equation record.</p>
          <p><a class="button primary" href="research-map.html">Research map</a> <a class="button" href="sources.html#p88-source">P88 sources</a> <a class="button" href="physics-mathematics.html">Physics &amp; Math</a></p>
        </article>
        <article class="card">
          <p class="eyebrow">Measurement science</p>
          <h3>Examine evidence, uncertainty, and non-identification</h3>
          <p>Follow Research III to see how reports, behavior, physiology, neural measurements, interventions, dependence, and uncertainty are handled without forcing a single answer.</p>
          <p><a class="button primary" href="measurement-science.html">Research III</a> <a class="button" href="https://github.com/MahsaKeikha/consciousness-measurement-science">Repository</a> <a class="button" href="research-lineage.html">How it connects</a></p>
        </article>
        <article class="card">
          <p class="eyebrow">Visual and reproducibility audit</p>
          <h3>Inspect figures, implementation, and exact reproduction</h3>
          <p>Use the visual atlas for the scientific structure, then follow implementation and reproducibility records to audit what can be regenerated from source.</p>
          <p><a class="button primary" href="visual-atlas.html">Visual atlas</a> <a class="button" href="implementation.html">Implementation</a> <a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/reproducibility.md">Reproduce results</a></p>
        </article>
      </div>
    </section>

'''

TEST = '''\n\ndef test_overview_offers_reader_specific_entry_paths_before_p88() -> None:\n    overview = _read(WEBSITE / "index.html")\n    journey = overview.index('id="project-journey"')\n    paths = overview.index('id="reader-paths"')\n    p88 = overview.index('id="p88-frontier"')\n    assert journey < paths < p88\n    for token in (\n        "Choose where to start",\n        "New to the program",\n        "Mathematics and theorem audit",\n        "Measurement science",\n        "Visual and reproducibility audit",\n        "start-here.html",\n        "plain-language.html",\n        "research-lineage.html",\n        "research-map.html",\n        "sources.html#p88-source",\n        "measurement-science.html",\n        "consciousness-measurement-science",\n        "visual-atlas.html",\n        "implementation.html",\n        "docs/reproducibility.md",\n    ):\n        assert token in overview\n'''


def main() -> None:
    index = INDEX.read_text(encoding="utf-8")
    if 'id="reader-paths"' not in index:
        marker = '<!-- current-frontier-home: P88 -->'
        if marker not in index:
            raise RuntimeError("Overview P88 marker is missing")
        index = index.replace(marker, SECTION + marker, 1)
        INDEX.write_text(index, encoding="utf-8")

    contract = CONTRACT.read_text(encoding="utf-8")
    if "test_overview_offers_reader_specific_entry_paths_before_p88" not in contract:
        CONTRACT.write_text(contract.rstrip() + TEST + "\n", encoding="utf-8")

    index = INDEX.read_text(encoding="utf-8")
    if index.count('id="reader-paths"') != 1:
        raise RuntimeError("Overview must contain exactly one reader-path section")
    if not (
        index.index('id="project-journey"')
        < index.index('id="reader-paths"')
        < index.index('id="p88-frontier"')
    ):
        raise RuntimeError("Reader paths must appear after the three-stage journey and before P88")


if __name__ == "__main__":
    main()
