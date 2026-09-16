import re
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
    return re.findall(r"^\| \[P(\d+)\]\(([^)]+)\)", block, flags=re.MULTILINE)


def test_complete_navigator_has_exactly_p1_through_p100() -> None:
    page = PAGE.read_text(encoding="utf-8")
    cards = re.findall(
        r'<a class="proposition-nav-card" data-proposition="P(\d+)" href="([^"]+)">',
        page,
    )
    assert [int(number) for number, _ in cards] == list(range(1, 101))
    assert page.count('class="proposition-nav-card"') == 100


def test_complete_navigator_links_match_canonical_roadmap() -> None:
    page = PAGE.read_text(encoding="utf-8")
    cards = dict(
        re.findall(
            r'<a class="proposition-nav-card" data-proposition="P(\d+)" href="([^"]+)">',
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


def test_research_map_p100_frontier_copy_is_current() -> None:
    page = PAGE.read_text(encoding="utf-8")
    assert "P19 and P71-P100: from sufficiency to selection-valid and anytime-valid target-model falsification" in page
    assert "P77-P100: from full-law rejection to anytime-valid sequential certification" in page
    assert "P100 remains a conditional sequential model-rejection theorem" in page
    assert "P97 protects same-data selection over a finite predeclared candidate family" in page
    assert "P99 aggregates distributed cross-fitted evidence with e-values" in page
    assert "P100 makes fresh P99 rounds anytime-valid under predictable reserve stakes" in page
    assert "P77-P100: from full-law rejection to finite-range dependent localized nonlinear certification" not in page
    assert "P99 remains a conditional model-rejection theorem under its declared independent-block" not in page


def test_navigator_cards_render_plain_reader_text() -> None:
    page = PAGE.read_text(encoding="utf-8")
    block = page.split("<!-- BEGIN COMPLETE PROPOSITION NAVIGATOR -->", 1)[1].split(
        "<!-- END COMPLETE PROPOSITION NAVIGATOR -->", 1
    )[0]
    assert "`" not in block
    assert "<strong>Representation-independent bridge objects</strong>" in block
    assert "<strong>Full mixed-prevalence P75 separation bracket" in block
