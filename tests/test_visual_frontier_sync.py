import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "website" / "index.html"
ATLAS = ROOT / "website" / "visual-atlas.html"
GATEWAY = ROOT / "figures" / "README.md"
CURRENT = ROOT / "figures" / "CURRENT_FRONTIER.md"
MANIFEST = ROOT / "figures" / "frontier_manifest.json"
DOC_FIGURE_README = ROOT / "docs" / "figures" / "README.md"
PREPARE = ROOT / "scripts" / "prepare_website.py"
PAGES = ROOT / ".github" / "workflows" / "pages.yml"
P86_FIGURE = ROOT / "docs" / "figures" / "p86_exact_minimally_weighted_quad_projection_parity.svg"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_p86_is_the_first_frontier_figure_on_homepage() -> None:
    text = _text(INDEX)
    p86 = text.index('id="p86-frontier"')
    plain = text.index('id="plain-language"')
    p84 = text.index('id="p84-frontier"')
    p85 = text.index('id="p85-frontier"')
    assert p86 < plain < p84 < p85
    assert "Current theorem frontier · P86" in text
    assert "p86_exact_minimally_weighted_quad_projection_parity.svg" in text


def test_visual_atlas_presents_p86_before_p85() -> None:
    text = _text(ATLAS)
    p86 = text.index('id="p86-frontier"')
    p85 = text.index('id="p85-frontier"')
    assert p86 < p85
    assert "Current theorem frontier · P86" in text
    assert "Previous theorem frontier · P85" in text


def test_top_level_figure_gateway_is_p86_and_machine_readable() -> None:
    gateway = _text(GATEWAY)
    current = _text(CURRENT)
    manifest = json.loads(_text(MANIFEST))

    assert "Current theorem frontier · P86" in gateway
    assert "L85 = 0 < L86 = 1/192" in gateway
    assert "# Current visual frontier: P71-P86" in current
    assert "P84 and P85 remain scientifically important historical frontiers" in current
    assert manifest["current_frontier"] == "P86"
    assert manifest["current_figure"].endswith(
        "p86_exact_minimally_weighted_quad_projection_parity.svg"
    )
    assert manifest["standard_functional_count"] == 10560


def test_current_p86_figure_exists_in_canonical_archive() -> None:
    assert P86_FIGURE.is_file()
    text = _text(P86_FIGURE)
    assert "<svg" in text
    assert "P86" in text
    assert "1/192" in text


def test_figure_readme_and_deployment_pipeline_track_p86() -> None:
    figure_readme = _text(DOC_FIGURE_README)
    prepare = _text(PREPARE)
    pages = _text(PAGES)

    assert "current theorem frontier is **P86**" in figure_readme.lower()
    assert "p86_exact_minimally_weighted_quad_projection_parity.svg" in figure_readme
    assert "docs/figures" in prepare
    assert "copytree" in prepare
    assert '"docs/figures/**"' in pages


def test_visual_frontier_sync_script_is_idempotent_by_contract() -> None:
    source = _text(ROOT / "scripts" / "sync_visual_frontier.py")
    assert '"--check"' in source
    assert "stale visual-frontier surfaces" in source
    assert "CURRENT = \"P86\"" in source
