import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC_FIGURES = ROOT / "docs" / "figures"
MANIFEST = ROOT / "figures" / "manifest.json"
GATEWAY = ROOT / "figures" / "README.md"
CURRENT = ROOT / "figures" / "CURRENT_FRONTIER.md"
CURRENT_SVG = ROOT / "figures" / "current_frontier.svg"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"
HOME = ROOT / "website" / "index.html"
PLAIN = ROOT / "website" / "plain-language.html"
START = ROOT / "website" / "start-here.html"
SYNCER = ROOT / "scripts" / "sync_figure_publication.py"
PREPARE_WEBSITE = ROOT / "scripts" / "prepare_website.py"
P89_FIGURE = "p89_complete_linear_parity_duality.svg"
RAW_PREFIX = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/"
)


def test_figure_manifest_is_complete_and_byte_exact() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 1
    assert manifest["canonical_root"] == "docs/figures"
    assert manifest["current_frontier"] == "P89"
    assert manifest["current_frontier_figure"].endswith(P89_FIGURE)
    assert manifest["hash_algorithm"] == "sha256"

    figures = sorted(DOC_FIGURES.rglob("*.svg"))
    records = {record["path"]: record for record in manifest["figures"]}
    expected_paths = {path.relative_to(ROOT).as_posix() for path in figures}
    assert manifest["figure_count"] == len(figures)
    assert set(records) == expected_paths

    for path in figures:
        relative = path.relative_to(ROOT).as_posix()
        raw = path.read_bytes()
        record = records[relative]
        assert record["bytes"] == len(raw)
        assert record["sha256"] == hashlib.sha256(raw).hexdigest()
        assert record["title"]
        assert record["description_chars"] >= 140


def test_github_figure_gateway_tracks_p89() -> None:
    gateway = GATEWAY.read_text(encoding="utf-8")
    current = CURRENT.read_text(encoding="utf-8")

    assert CURRENT_SVG.read_bytes() == (DOC_FIGURES / P89_FIGURE).read_bytes()
    assert "## Current theorem frontier: P89" in gateway
    assert P89_FIGURE in gateway
    assert "manifest.json" in gateway

    assert current.startswith("# Current visual frontier: P71-P89")
    assert "## Current theorem frontier: P89" in current
    assert "L88 = 1/64 < L89 = 5/168" in current
    assert "| P87 |" in current
    assert "| P88 |" in current
    assert "| P89 |" in current


def test_visual_atlas_leads_with_p89_before_historical_frontiers() -> None:
    text = VISUAL_ATLAS.read_text(encoding="utf-8")
    p89 = text.index('id="p89-frontier"')
    p88 = text.index('id="p88-frontier"')
    p87 = text.index('id="p87-frontier"')

    assert p89 < p88 < p87
    current = text[p89:p88]
    assert "Current theorem frontier · P89" in current
    assert P89_FIGURE in current
    assert "5/168" in current
    assert "complete_linear_parity_duality.py" in current
    assert "test_complete_linear_parity_duality.py" in current
    assert "Previous theorem frontier · P88" in text[p88:p87]


def test_homepage_balances_three_research_stages_and_keeps_history_specialist() -> None:
    text = HOME.read_text(encoding="utf-8")
    research_i = text.index('id="research-i-overview"')
    p89 = text.index('id="p89-frontier"')
    research_iii = text.index('id="research-iii-overview"')
    reader_paths = text.index('id="reader-paths"')

    assert research_i < p89 < research_iii < reader_paths
    current = text[p89:research_iii]
    assert "Current theorem frontier · P89" in current
    assert P89_FIGURE in current
    assert "5/168" in current
    assert "complete_linear_parity_duality.py" in current
    assert "test_complete_linear_parity_duality.py" in current
    assert "physics_pipeline.svg" in text[research_i:p89]
    assert "measurement_architecture.svg" in text[research_iii:reader_paths]
    for historical_id in (
        'id="p88-frontier"',
        'id="p87-frontier"',
        'id="p86-frontier"',
        'id="p85-frontier"',
    ):
        assert historical_id not in text
    assert "The 89 results form several dependency branches." in text
    assert "all 89 propositions" in text


def test_plain_language_and_start_here_preserve_three_stage_architecture() -> None:
    plain = PLAIN.read_text(encoding="utf-8")
    start = START.read_text(encoding="utf-8")

    for source in (plain, start):
        assert "Research I" in source
        assert "Research II" in source
        assert "Research III" in source
        assert "89 results · current frontier P89" in source
        assert "physical-to-experiential bridge" in source

    assert 'id="three-stage-progress"' in plain
    assert "What the whole research program is doing" in plain
    assert 'id="program-stages"' in start
    assert "The 89 Research II propositions by scientific role" in start


def test_figure_publication_synchronizer_reports_zero_drift() -> None:
    subprocess.run(
        [sys.executable, str(SYNCER), "--check"],
        cwd=ROOT,
        check=True,
    )


def test_pages_build_bundles_exact_commit_p89_figure(tmp_path: Path) -> None:
    site = tmp_path / "site"
    subprocess.run(
        [
            sys.executable,
            str(PREPARE_WEBSITE),
            "--source",
            "website",
            "--output",
            str(site),
        ],
        cwd=ROOT,
        check=True,
    )

    deployed_p89 = site / "figures" / P89_FIGURE
    assert deployed_p89.read_bytes() == (DOC_FIGURES / P89_FIGURE).read_bytes()

    atlas = (site / "visual-atlas.html").read_text(encoding="utf-8")
    assert f'src="figures/{P89_FIGURE}"' in atlas
    assert f'src="{RAW_PREFIX}' not in atlas

    home = (site / "index.html").read_text(encoding="utf-8")
    assert f'src="figures/{P89_FIGURE}"' in home
    assert f'src="{RAW_PREFIX}' not in home
    research_i = home.index('id="research-i-overview"')
    p89 = home.index('id="p89-frontier"')
    research_iii = home.index('id="research-iii-overview"')
    reader_paths = home.index('id="reader-paths"')
    assert research_i < p89 < research_iii < reader_paths < home.index('id="plain-language"')
    for historical_id in (
        'id="p88-frontier"',
        'id="p87-frontier"',
        'id="p86-frontier"',
        'id="p85-frontier"',
    ):
        assert historical_id not in home
