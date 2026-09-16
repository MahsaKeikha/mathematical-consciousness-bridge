from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "website" / "sources.html"
RESEARCH_MAP = ROOT / "website" / "research-map.html"
STYLES = ROOT / "website" / "styles.css"
FOOTER = ROOT / "website" / "footer.js"
TEST = ROOT / "tests" / "test_sources_p1_p100_sequence.py"

BEGIN_NAV = "<!-- BEGIN COMPLETE PROPOSITION NAVIGATOR -->"
END_NAV = "<!-- END COMPLETE PROPOSITION NAVIGATOR -->"
BEGIN_SOURCE = "<!-- BEGIN COMPLETE SOURCE SEQUENCE -->"
END_SOURCE = "<!-- END COMPLETE SOURCE SEQUENCE -->"

RAW_ROADMAP = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/theorem_roadmap.svg"
)
GITHUB_ROADMAP = (
    "https://github.com/MahsaKeikha/mathematical-consciousness-bridge/"
    "blob/main/docs/theorem_roadmap.md"
)


def extract_source_sequence() -> str:
    research = RESEARCH_MAP.read_text(encoding="utf-8")
    match = re.search(
        re.escape(BEGIN_NAV) + r".*?" + re.escape(END_NAV),
        research,
        flags=re.DOTALL,
    )
    if not match:
        raise RuntimeError("complete proposition navigator is missing from research-map.html")

    block = match.group(0)
    block = block.replace(BEGIN_NAV, BEGIN_SOURCE)
    block = block.replace(END_NAV, END_SOURCE)
    block = block.replace(
        '<section id="complete-proposition-navigator" class="proposition-navigator">',
        '<section id="complete-source-sequence" class="proposition-navigator source-proposition-sequence">',
        1,
    )
    block = block.replace("Complete proposition navigator", "Complete theorem source sequence", 1)
    block = block.replace(
        "Open any result from P1 through P100 directly",
        "Follow every theorem source from P1 through P100 in order",
        1,
    )
    old_intro = (
        "The stage cards above show the scientific architecture. This navigator gives every "
        "proposition its own visible, native link so readers can move from the map straight to "
        "the canonical theorem record without guessing which range contains it."
    )
    new_intro = (
        "This is the continuous source path for the full proposition record. Every proposition "
        "appears exactly once in numeric order, with its title, scientific object, status, and a "
        "direct link to the canonical proof document. Group headings keep the sequence readable "
        "without hiding any proposition inside a range summary."
    )
    if old_intro not in block:
        raise RuntimeError("research-map navigator intro changed unexpectedly")
    block = block.replace(old_intro, new_intro, 1)
    block = block.replace(
        'aria-label="Proposition navigator groups"',
        'aria-label="Theorem source sequence groups"',
        1,
    )
    block = block.replace("#navigator-p", "#source-sequence-p")
    block = block.replace('id="navigator-p', 'id="source-sequence-p')
    block = re.sub(
        r'<a class="proposition-nav-card" data-proposition="P(\d+)"',
        r'<a id="source-p\1" class="proposition-nav-card" data-proposition="P\1"',
        block,
    )

    figure = f'''  <div class="source-sequence-roadmap">
    <div class="source-sequence-rule">
      <strong>Two orders, one record.</strong>
      <span>The cards below are deliberately numeric, P1 through P100. The roadmap shows scientific dependency, because proposition number records development order and does not mean that every earlier branch is a prerequisite for every later result.</span>
    </div>
    <div class="theorem-figure-shell">
      <a href="{GITHUB_ROADMAP}"><img loading="lazy" decoding="async" src="{RAW_ROADMAP}" alt="Complete theorem roadmap P1-P100" /></a>
    </div>
    <p class="source-sequence-caption">Core bridge lineage: P1-P24 then P71-P100. Connected branches: P25-P70. The physical-to-experiential bridge remains open.</p>
  </div>
'''
    marker = '  <nav class="proposition-nav-index"'
    if block.count(marker) != 1:
        raise RuntimeError("could not locate source-sequence index insertion point")
    block = block.replace(marker, figure + marker, 1)

    numbers = [
        int(value)
        for value in re.findall(r'data-proposition="P(\d+)"', block)
    ]
    if numbers != list(range(1, 101)):
        raise RuntimeError(f"source sequence is not exact P1-P100: {numbers}")
    if "\u2013" in block or "\u2014" in block:
        raise RuntimeError("source sequence violates reader-facing dash policy")
    return block


def normalize_hero(sources: str) -> str:
    hero = '''<section class="hero compact-hero">
  <p class="eyebrow">Sources and reproducibility</p>
  <h1>A complete source path from P1 through P100</h1>
  <p class="lede">Start with the ordered theorem source sequence below. Every proposition is visible once, in numeric order, grouped by scientific stage, and linked directly to its canonical proof record. The rest of this page explains provenance, reproducibility, and the richer audit bundles behind the latest theorem family.</p>
  <div class="status-grid" aria-label="Theorem source sequence status">
    <div><strong>100</strong><span>ordered proposition records</span></div>
    <div><strong>P1-P100</strong><span>continuous numeric source path</span></div>
    <div><strong>P100</strong><span>current theorem frontier</span></div>
    <div><strong>Open</strong><span>physical-to-experiential bridge</span></div>
  </div>
</section>'''
    updated, count = re.subn(
        r'<section class="hero compact-hero">.*?</section>',
        hero,
        sources,
        count=1,
        flags=re.DOTALL,
    )
    if count != 1:
        raise RuntimeError(f"expected one Sources hero, found {count}")
    return updated


def insert_source_sequence(sources: str, sequence: str) -> str:
    sources = re.sub(
        re.escape(BEGIN_SOURCE) + r".*?" + re.escape(END_SOURCE) + r"\s*",
        "",
        sources,
        flags=re.DOTALL,
    )
    hero = re.search(r'<section class="hero compact-hero">.*?</section>', sources, flags=re.DOTALL)
    if not hero:
        raise RuntimeError("could not locate Sources hero for source-sequence insertion")
    insertion = hero.end()
    return sources[:insertion] + "\n\n" + sequence + sources[insertion:]


def sort_detailed_source_records(sources: str) -> str:
    pattern = re.compile(r'<section id="p(\d+)-source"[^>]*>.*?</section>', flags=re.DOTALL)
    matches = list(pattern.finditer(sources))
    if not matches:
        raise RuntimeError("no detailed theorem source records found")

    numbers = [int(match.group(1)) for match in matches]
    if sorted(numbers) != list(range(86, 101)):
        raise RuntimeError(f"expected detailed P86-P100 records, found {sorted(numbers)}")
    if len(numbers) != len(set(numbers)):
        raise RuntimeError("duplicate detailed theorem source record detected")
    for left, right in zip(matches, matches[1:]):
        if sources[left.end() : right.start()].strip():
            raise RuntimeError("unexpected non-record content between detailed source records")

    normalized: list[tuple[int, str]] = []
    for match in matches:
        number = int(match.group(1))
        section = match.group(0)
        label = (
            "Current theorem source · P100"
            if number == 100
            else f"Detailed theorem source record · P{number}"
        )
        section, count = re.subn(
            r'(<p class="eyebrow">).*?(</p>)',
            rf"\1{label}\2",
            section,
            count=1,
            flags=re.DOTALL,
        )
        if count != 1:
            raise RuntimeError(f"P{number} detailed record has no unique eyebrow")
        normalized.append((number, section))

    deep_index = "".join(
        f'<a href="#p{number}-source">P{number}</a>' for number in range(86, 101)
    )
    intro = f'''<section id="expanded-theorem-source-records" class="boundary expanded-source-records">
  <div class="section-head">
    <p class="eyebrow">Expanded audit records</p>
    <h2>Detailed theorem source records, P86 through P100, in order</h2>
    <p>The complete P1-P100 sequence above is the authoritative navigation path for every proposition. The expanded records below add richer proof, provenance, implementation, test, figure, and scientific-boundary links for the most recent theorem family. They are sorted strictly by proposition number so the argument can be followed without backtracking.</p>
  </div>
  <nav class="proposition-nav-index" aria-label="Expanded theorem source records">{deep_index}</nav>
</section>'''

    ordered = "\n\n".join(section for _, section in sorted(normalized))
    prefix = sources[: matches[0].start()]
    suffix = sources[matches[-1].end() :]
    return prefix + intro + "\n\n" + ordered + suffix


def update_footer_compatibility() -> None:
    text = FOOTER.read_text(encoding="utf-8")
    old = '''    const p99 = document.querySelector('#p99-source');
    if (!p99) return;

    const p99Eyebrow = p99.querySelector('.section-head .eyebrow');
    if (p99Eyebrow) {
      p99Eyebrow.textContent = 'Immediate predecessor theorem source · P99';
    }

    if (document.querySelector('#p100-source')) return;
'''
    new = '''    if (document.querySelector('#p100-source')) return;

    const p99 = document.querySelector('#p99-source');
    if (!p99) return;

    const p99Eyebrow = p99.querySelector('.section-head .eyebrow');
    if (p99Eyebrow) {
      p99Eyebrow.textContent = 'Immediate predecessor theorem source · P99';
    }
'''
    if old in text:
        text = text.replace(old, new, 1)
    elif new not in text:
        raise RuntimeError("footer Sources frontier compatibility block changed unexpectedly")
    FOOTER.write_text(text, encoding="utf-8")


def update_styles() -> None:
    text = STYLES.read_text(encoding="utf-8")
    begin = "/* BEGIN COMPLETE SOURCE SEQUENCE */"
    end = "/* END COMPLETE SOURCE SEQUENCE */"
    text = re.sub(
        re.escape(begin) + r".*?" + re.escape(end) + r"\s*",
        "",
        text,
        flags=re.DOTALL,
    )
    css = '''/* BEGIN COMPLETE SOURCE SEQUENCE */
.source-proposition-sequence {
  margin-top: 8px;
}

.source-sequence-roadmap {
  margin: 26px 0 34px;
  padding: 20px;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--soft);
}

.source-sequence-rule {
  display: grid;
  grid-template-columns: minmax(130px, 0.3fr) minmax(0, 1fr);
  gap: 16px;
  align-items: start;
  margin-bottom: 18px;
}

.source-sequence-rule strong {
  color: var(--accent2);
  font-size: 0.82rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.source-sequence-rule span,
.source-sequence-caption {
  color: var(--muted);
  font-size: 0.9rem;
  line-height: 1.62;
}

.source-sequence-caption {
  margin: 14px 2px 0;
}

.source-proposition-sequence .proposition-nav-card {
  scroll-margin-top: 100px;
}

.expanded-source-records {
  margin-top: 48px;
}

@media (max-width: 680px) {
  .source-sequence-roadmap {
    padding: 14px;
  }

  .source-sequence-rule {
    grid-template-columns: 1fr;
    gap: 7px;
  }
}
/* END COMPLETE SOURCE SEQUENCE */
'''
    STYLES.write_text(text.rstrip() + "\n\n" + css, encoding="utf-8")


def write_test() -> None:
    TEST.write_text(
        '''import re\nfrom html import unescape\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nSOURCES = ROOT / "website" / "sources.html"\nRESEARCH_MAP = ROOT / "website" / "research-map.html"\nFOOTER = ROOT / "website" / "footer.js"\n\n\ndef _block(text: str, begin: str, end: str) -> str:\n    return text.split(begin, 1)[1].split(end, 1)[0]\n\n\ndef _cards(block: str) -> list[tuple[int, str, str]]:\n    pattern = re.compile(\n        r'<a(?: id="[^"]+")? class="proposition-nav-card" '\n        r'data-proposition="P(\\d+)" href="([^"]+)">.*?'\n        r'<strong>(.*?)</strong>',\n        flags=re.DOTALL,\n    )\n    return [\n        (int(number), href, unescape(re.sub(r"<.*?>", "", title)).strip())\n        for number, href, title in pattern.findall(block)\n    ]\n\n\ndef test_sources_has_exact_ordered_p1_p100_source_sequence():\n    text = SOURCES.read_text(encoding="utf-8")\n    block = _block(\n        text,\n        "<!-- BEGIN COMPLETE SOURCE SEQUENCE -->",\n        "<!-- END COMPLETE SOURCE SEQUENCE -->",\n    )\n    cards = _cards(block)\n    assert [number for number, _, _ in cards] == list(range(1, 101))\n    assert len({number for number, _, _ in cards}) == 100\n    assert [int(value) for value in re.findall(r'id="source-p(\\d+)"', block)] == list(range(1, 101))\n    assert "Follow every theorem source from P1 through P100 in order" in block\n    assert "Complete theorem roadmap P1-P100" in block\n    assert "Core bridge lineage: P1-P24 then P71-P100" in block\n    assert "physical-to-experiential bridge remains open" in block\n    assert "\\u2013" not in block\n    assert "\\u2014" not in block\n\n\ndef test_sources_sequence_matches_research_map_canonical_cards():\n    sources = SOURCES.read_text(encoding="utf-8")\n    research = RESEARCH_MAP.read_text(encoding="utf-8")\n    source_block = _block(\n        sources,\n        "<!-- BEGIN COMPLETE SOURCE SEQUENCE -->",\n        "<!-- END COMPLETE SOURCE SEQUENCE -->",\n    )\n    research_block = _block(\n        research,\n        "<!-- BEGIN COMPLETE PROPOSITION NAVIGATOR -->",\n        "<!-- END COMPLETE PROPOSITION NAVIGATOR -->",\n    )\n    assert _cards(source_block) == _cards(research_block)\n\n\ndef test_sources_group_index_is_complete_and_scannable():\n    text = SOURCES.read_text(encoding="utf-8")\n    block = _block(\n        text,\n        "<!-- BEGIN COMPLETE SOURCE SEQUENCE -->",\n        "<!-- END COMPLETE SOURCE SEQUENCE -->",\n    )\n    expected = [\n        "p1-p10",\n        "p11-p18",\n        "p19-p24",\n        "p25-p37",\n        "p38-p44",\n        "p45-p53",\n        "p54-p60",\n        "p61-p70",\n        "p71-p76",\n        "p77-p89",\n        "p90-p95",\n        "p96-p100",\n    ]\n    ids = re.findall(r'id="source-sequence-(p\\d+-p\\d+)"', block)\n    assert ids == expected\n    hrefs = re.findall(r'href="#source-sequence-(p\\d+-p\\d+)"', block)\n    assert hrefs == expected\n\n\ndef test_detailed_source_records_are_strictly_ascending_without_gaps():\n    text = SOURCES.read_text(encoding="utf-8")\n    detailed = [int(value) for value in re.findall(r'<section id="p(\\d+)-source"', text)]\n    assert detailed == list(range(86, 101))\n    assert "Detailed theorem source records, P86 through P100, in order" in text\n    assert text.count("Current theorem source · P100") == 1\n    assert not re.search(r"Current theorem source[^<]*· P(?:8[6-9]|9[0-9])", text)\n\n\ndef test_static_sources_frontier_is_not_rewritten_when_p100_exists():\n    footer = FOOTER.read_text(encoding="utf-8")\n    function = footer.split("function syncSourcesFrontier()", 1)[1].split(\n        "function wireSourceCards()", 1\n    )[0]\n    assert function.index("document.querySelector('#p100-source')") < function.index(\n        "document.querySelector('#p99-source')"\n    )\n''',
        encoding="utf-8",
    )


def main() -> None:
    sources = SOURCES.read_text(encoding="utf-8")
    sources = normalize_hero(sources)
    sources = insert_source_sequence(sources, extract_source_sequence())
    sources = sort_detailed_source_records(sources)
    SOURCES.write_text(sources, encoding="utf-8")
    update_footer_compatibility()
    update_styles()
    write_test()


if __name__ == "__main__":
    main()
