from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "docs" / "theorem_roadmap.md"
RESEARCH_MAP = ROOT / "website" / "research-map.html"
STYLES = ROOT / "website" / "styles.css"
TEST = ROOT / "tests" / "test_complete_research_map_proposition_navigator.py"

NAV_START = "<!-- BEGIN COMPLETE PROPOSITION NAVIGATOR -->"
NAV_END = "<!-- END COMPLETE PROPOSITION NAVIGATOR -->"
CSS_START = "/* BEGIN COMPLETE PROPOSITION NAVIGATOR */"
CSS_END = "/* END COMPLETE PROPOSITION NAVIGATOR */"

GROUPS = [
    (1, 10, "Foundations"),
    (11, 18, "Structured physical descriptions"),
    (19, 24, "Bridge sufficiency and finite-data validity"),
    (25, 37, "Operational scale and quotient compatibility"),
    (38, 44, "Quantum operational interface"),
    (45, 53, "Adaptive evidence acquisition"),
    (54, 60, "Scheduling and transition calibration setup"),
    (61, 70, "Exact calibration and optimization"),
    (71, 76, "Target provenance, measurement, and adequacy"),
    (77, 89, "Certified continuous-family model separation"),
    (90, 95, "Nonlinear and finite-sample model rejection"),
    (96, 100, "Selection-valid and anytime-valid inference"),
]

ROW_RE = re.compile(
    r"^\| \[P(?P<number>\d+)\]\((?P<href>[^)]+)\) \| "
    r"(?P<mathematical>[^|]+?) \| (?P<scientific>[^|]+?) \| "
    r"(?P<status>[^|]+?) \|$",
    flags=re.MULTILINE,
)


def parse_rows() -> list[dict[str, str | int]]:
    roadmap = ROADMAP.read_text(encoding="utf-8")
    block = roadmap.split("## 3. Complete proposition index", 1)[1].split(
        "## 4. Calibration branch remains separate", 1
    )[0]
    rows: list[dict[str, str | int]] = []
    for match in ROW_RE.finditer(block):
        rows.append(
            {
                "number": int(match.group("number")),
                "href": match.group("href").strip(),
                "mathematical": match.group("mathematical").strip(),
                "scientific": match.group("scientific").strip(),
                "status": match.group("status").strip(),
            }
        )
    numbers = [int(row["number"]) for row in rows]
    expected = list(range(1, 101))
    if numbers != expected:
        raise RuntimeError(f"Expected exact P1-P100 proposition index, got {numbers}")
    return rows


def github_href(relative_href: str) -> str:
    return (
        "https://github.com/MahsaKeikha/mathematical-consciousness-bridge/"
        f"blob/main/docs/{relative_href}"
    )


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def card(row: dict[str, str | int]) -> str:
    number = int(row["number"])
    return "\n".join(
        [
            (
                f'        <a class="proposition-nav-card" data-proposition="P{number}" '
                f'href="{esc(github_href(str(row["href"])))}">'
            ),
            f'          <span class="proposition-nav-number">P{number}</span>',
            f'          <strong>{esc(str(row["scientific"]))}</strong>',
            f'          <span class="proposition-nav-object">{esc(str(row["mathematical"]))}</span>',
            f'          <span class="proposition-nav-status">{esc(str(row["status"]))}</span>',
            "        </a>",
        ]
    )


def build_navigation(rows: list[dict[str, str | int]]) -> str:
    by_number = {int(row["number"]): row for row in rows}
    index_links = "\n".join(
        f'      <a href="#navigator-p{start}-p{end}">P{start}-P{end}</a>'
        for start, end, _ in GROUPS
    )
    groups = []
    for start, end, title in GROUPS:
        cards = "\n".join(card(by_number[number]) for number in range(start, end + 1))
        groups.append(
            "\n".join(
                [
                    f'    <section class="proposition-nav-group" id="navigator-p{start}-p{end}">',
                    '      <div class="proposition-nav-group-head">',
                    f"        <span>P{start}-P{end}</span>",
                    f"        <h3>{esc(title)}</h3>",
                    "      </div>",
                    '      <div class="proposition-nav-grid">',
                    cards,
                    "      </div>",
                    "    </section>",
                ]
            )
        )
    return "\n".join(
        [
            NAV_START,
            '<section id="complete-proposition-navigator" class="proposition-navigator">',
            '  <div class="section-head">',
            '    <p class="eyebrow">Complete proposition navigator</p>',
            '    <h2>Open any result from P1 through P100 directly</h2>',
            (
                '    <p>The stage cards above show the scientific architecture. This navigator gives '
                'every proposition its own visible, native link so readers can move from the map '
                'straight to the canonical theorem record without guessing which range contains it.</p>'
            ),
            "  </div>",
            '  <nav class="proposition-nav-index" aria-label="Proposition navigator groups">',
            index_links,
            "  </nav>",
            '  <div class="proposition-nav-groups">',
            "\n".join(groups),
            "  </div>",
            "</section>",
            NAV_END,
        ]
    )


def replace_or_insert_navigation(page: str, navigation: str) -> str:
    if NAV_START in page:
        pattern = re.compile(
            re.escape(NAV_START) + r".*?" + re.escape(NAV_END),
            flags=re.DOTALL,
        )
        return pattern.sub(navigation, page, count=1)
    marker = '<section id="bridge-lineage">'
    if page.count(marker) != 1:
        raise RuntimeError("Could not locate unique bridge-lineage insertion point")
    return page.replace(marker, navigation + "\n\n" + marker, 1)


def css_block() -> str:
    return """/* BEGIN COMPLETE PROPOSITION NAVIGATOR */
.proposition-navigator {
  border-top: 1px solid var(--line);
}

.proposition-nav-index {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 24px 0 38px;
}

.proposition-nav-index a {
  padding: 7px 10px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--paper);
  color: var(--ink);
  font-size: 0.78rem;
  font-weight: 700;
  text-decoration: none;
}

.proposition-nav-index a:hover,
.proposition-nav-index a:focus-visible {
  border-color: var(--accent);
  color: var(--accent);
  text-decoration: none;
}

.proposition-nav-group + .proposition-nav-group {
  margin-top: 38px;
}

.proposition-nav-group-head {
  display: flex;
  gap: 14px;
  align-items: baseline;
  margin-bottom: 14px;
}

.proposition-nav-group-head > span {
  color: var(--accent2);
  font-size: 0.76rem;
  font-weight: 760;
  letter-spacing: 0.07em;
  text-transform: uppercase;
}

.proposition-nav-group-head h3 {
  margin: 0;
  font-family: var(--font-display);
  font-size: 1.3rem;
  font-weight: 600;
  letter-spacing: -0.015em;
}

.proposition-nav-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 11px;
}

.proposition-nav-card {
  display: flex;
  min-width: 0;
  min-height: 164px;
  padding: 16px;
  flex-direction: column;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--paper);
  color: var(--ink);
  text-decoration: none;
  transition: transform 150ms ease, border-color 150ms ease, box-shadow 150ms ease;
}

.proposition-nav-card:hover,
.proposition-nav-card:focus-visible {
  transform: translateY(-2px);
  border-color: var(--accent);
  box-shadow: 0 9px 22px rgba(20, 26, 36, 0.07);
  text-decoration: none;
}

.proposition-nav-number {
  color: var(--accent2);
  font-size: 0.76rem;
  font-weight: 780;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.proposition-nav-card strong {
  display: block;
  margin-top: 8px;
  font-size: 0.95rem;
  line-height: 1.38;
}

.proposition-nav-object {
  display: block;
  margin-top: 8px;
  color: var(--muted);
  font-size: 0.77rem;
  line-height: 1.45;
}

.proposition-nav-status {
  display: block;
  margin-top: auto;
  padding-top: 10px;
  color: var(--muted);
  font-size: 0.7rem;
  font-weight: 650;
  line-height: 1.4;
}

@media (max-width: 1100px) {
  .proposition-nav-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

@media (max-width: 780px) {
  .proposition-nav-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 520px) {
  .proposition-nav-grid {
    grid-template-columns: 1fr;
  }

  .proposition-nav-group-head {
    display: block;
  }

  .proposition-nav-group-head h3 {
    margin-top: 4px;
  }
}
/* END COMPLETE PROPOSITION NAVIGATOR */"""


def replace_or_append_css(styles: str, block: str) -> str:
    if CSS_START in styles:
        pattern = re.compile(
            re.escape(CSS_START) + r".*?" + re.escape(CSS_END),
            flags=re.DOTALL,
        )
        return pattern.sub(block, styles, count=1)
    return styles.rstrip() + "\n\n" + block + "\n"


def test_source() -> str:
    return '''import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "docs" / "theorem_roadmap.md"
PAGE = ROOT / "website" / "research-map.html"
STYLES = ROOT / "website" / "styles.css"


def roadmap_links() -> list[tuple[str, str]]:
    roadmap = ROADMAP.read_text(encoding="utf-8")
    block = roadmap.split("## 3. Complete proposition index", 1)[1].split(
        "## 4. Calibration branch remains separate", 1
    )[0]
    return re.findall(r"^\\| \\[P(\\d+)\\]\\(([^)]+)\\)", block, flags=re.MULTILINE)


def test_complete_navigator_has_exactly_p1_through_p100() -> None:
    page = PAGE.read_text(encoding="utf-8")
    cards = re.findall(
        r'<a class="proposition-nav-card" data-proposition="P(\\d+)" href="([^"]+)">',
        page,
    )
    assert [int(number) for number, _ in cards] == list(range(1, 101))
    assert page.count('class="proposition-nav-card"') == 100


def test_complete_navigator_links_match_canonical_roadmap() -> None:
    page = PAGE.read_text(encoding="utf-8")
    cards = dict(
        re.findall(
            r'<a class="proposition-nav-card" data-proposition="P(\\d+)" href="([^"]+)">',
            page,
        )
    )
    expected = {
        number: (
            "https://github.com/MahsaKeikha/mathematical-consciousness-bridge/"
            f"blob/main/docs/{href}"
        )
        for number, href in roadmap_links()
    }
    assert cards == expected


def test_complete_navigator_preserves_architecture_and_native_clickability() -> None:
    page = PAGE.read_text(encoding="utf-8")
    styles = STYLES.read_text(encoding="utf-8")
    assert 'id="program-stages"' in page
    assert 'id="complete-proposition-navigator"' in page
    assert 'id="bridge-lineage"' in page
    assert page.index('id="program-stages"') < page.index('id="complete-proposition-navigator"')
    assert page.index('id="complete-proposition-navigator"') < page.index('id="bridge-lineage"')
    for start, end in [
        (1, 10), (11, 18), (19, 24), (25, 37), (38, 44), (45, 53),
        (54, 60), (61, 70), (71, 76), (77, 89), (90, 95), (96, 100),
    ]:
        assert f'id="navigator-p{start}-p{end}"' in page
    assert '<a class="proposition-nav-card"' in page
    assert '<article class="proposition-nav-card"' not in page
    assert ".proposition-nav-grid" in styles
    assert ".proposition-nav-card" in styles


def test_complete_navigator_reader_text_obeys_punctuation_policy() -> None:
    page = PAGE.read_text(encoding="utf-8")
    block = page.split("<!-- BEGIN COMPLETE PROPOSITION NAVIGATOR -->", 1)[1].split(
        "<!-- END COMPLETE PROPOSITION NAVIGATOR -->", 1
    )[0]
    assert "–" not in block
    assert "—" not in block
'''


def main() -> None:
    rows = parse_rows()
    navigation = build_navigation(rows)

    page = RESEARCH_MAP.read_text(encoding="utf-8")
    updated_page = replace_or_insert_navigation(page, navigation)
    RESEARCH_MAP.write_text(updated_page, encoding="utf-8")

    styles = STYLES.read_text(encoding="utf-8")
    STYLES.write_text(replace_or_append_css(styles, css_block()), encoding="utf-8")

    TEST.write_text(test_source(), encoding="utf-8")

    if updated_page.count('class="proposition-nav-card"') != 100:
        raise RuntimeError("Generated navigator does not contain exactly 100 proposition cards")
    if "–" in navigation or "—" in navigation:
        raise RuntimeError("Generated reader text violates punctuation policy")


if __name__ == "__main__":
    main()
