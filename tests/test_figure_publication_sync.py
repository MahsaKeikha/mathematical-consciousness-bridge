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
P93_FIGURE = "p93_localized_sign_coherence_rejection.svg"
RAW_PREFIX = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/"
)


def test_figure_manifest_is_complete_and_byte_exact() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 1
    assert manifest["canonical_root"] == "docs/figures"
    assert manifest["current_frontier"] == "P93"
    assert manifest["current_frontier_figure"].endswith(P93_FIGURE)
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


def test_github_figure_gateway_tracks_p93() -> None:
    gateway = GATEWAY.read_text(encoding="utf-8")
    current = CURRENT.read_text(encoding="utf-8")

    assert CURRENT_SVG.read_bytes() == (DOC_FIGURES / P93_FIGURE).read_bytes()
    assert "## Current theorem frontier: P93" in gateway
    assert P93_FIGURE in gateway
    assert "manifest.json" in gateway

    assert current.startswith("# Current visual frontier: P71-P93")
    assert "## Current theorem frontier: P93" in current
    assert "empirical determinants = (-1/48, 1/64, 5/192)" in current
    assert "d_inf(P_emp, M_75) = 1/24" in current
    for proposition in ("P89", "P90", "P91", "P92"):
        assert f"| {proposition} |" in current


def test_visual_atlas_leads_with_p93_before_historical_frontiers() -> None:
    text = VISUAL_ATLAS.read_text(encoding="utf-8")
    p93 = text.index('id="p93-frontier"')
    p92 = text.index('id="p92-frontier"')
    p93 = text.index('id="p93-frontier"')
    p91 = text.index('id="p91-frontier"')
    p90 = text.index('id="p90-frontier"')
    p89 = text.index('id="p89-frontier"')

    assert p93 < p92 < p91 < p90
    current = text[p93:p92]
    assert "Current theorem frontier · P93" in current
    assert P93_FIGURE in current
    assert "1/24" in current
    assert "proposition_93_localized_sign_coherence_rejection.md" in current
    previous = text[p92:p91]
    assert "Previous theorem frontier · P92" in previous


def test_homepage_balances_three_research_stages_and_keeps_history_specialist() -> None:
    text = HOME.read_text(encoding="utf-8")
    research_i = text.index('id="research-i-overview"')
    p93 = text.index('id="p93-frontier"')
    research_iii = text.index('id="research-iii-overview"')
    reader_paths = text.index('id="reader-paths"')

    assert research_i < p93 < research_iii < reader_paths
    current = text[p93:research_iii]
    assert "Current theorem frontier · P93" in current
    assert P93_FIGURE in current
    assert "1/24" in current
    assert "localized_sign_coherence_rejection.py" in current
    assert "test_localized_sign_coherence_rejection.py" in current
    assert "physics_pipeline.svg" in text[research_i:p93]
    assert "measurement_architecture.svg" in text[research_iii:reader_paths]
    for historical_id in (
        'id="p92-frontier"',
        'id="p92-frontier"',
        'id="p92-frontier"',
        'id="p91-frontier"',
        'id="p90-frontier"',
        'id="p89-frontier"',
        'id="p88-frontier"',
    ):
        assert historical_id not in text
    assert "The 93 results form several dependency branches." in text
    assert "all 93 propositions" in text


def test_plain_language_and_start_here_preserve_three_stage_architecture() -> None:
    plain = PLAIN.read_text(encoding="utf-8")
    start = START.read_text(encoding="utf-8")

    for source in (plain, start):
        assert "Research I" in source
        assert "Research II" in source
        assert "Research III" in source
        assert "93" in source
        assert "P93" in source
        assert "physical-to-experiential bridge" in source

    assert 'id="three-stage-progress"' in plain
    assert "What the whole research program is doing" in plain
    assert 'id="program-stages"' in start


def test_figure_publication_synchronizer_reports_zero_drift() -> None:
    subprocess.run(
        [sys.executable, str(SYNCER), "--check"],
        cwd=ROOT,
        check=True,
    )


def test_pages_build_bundles_exact_commit_p93_figure(tmp_path: Path) -> None:
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

    deployed_p93 = site / "figures" / P93_FIGURE
    assert deployed_p93.read_bytes() == (DOC_FIGURES / P93_FIGURE).read_bytes()

    atlas = (site / "visual-atlas.html").read_text(encoding="utf-8")
    assert f'src="figures/{P93_FIGURE}"' in atlas
    assert f'src="{RAW_PREFIX}' not in atlas

    home = (site / "index.html").read_text(encoding="utf-8")
    assert f'src="figures/{P93_FIGURE}"' in home
    assert f'src="{RAW_PREFIX}' not in home
    research_i = home.index('id="research-i-overview"')
    p93 = home.index('id="p93-frontier"')
    research_iii = home.index('id="research-iii-overview"')
    reader_paths = home.index('id="reader-paths"')
    assert research_i < p93 < research_iii < reader_paths < home.index('id="plain-language"')
    for historical_id in (
        'id="p92-frontier"',
        'id="p92-frontier"',
        'id="p92-frontier"',
        'id="p91-frontier"',
        'id="p90-frontier"',
        'id="p89-frontier"',
        'id="p88-frontier"',
    ):
        assert historical_id not in home
