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
SYNCER = ROOT / "scripts" / "sync_figure_publication.py"
PREPARE_WEBSITE = ROOT / "scripts" / "prepare_website.py"
P88_FIGURE = "p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg"
RAW_PREFIX = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/"
)


def test_figure_manifest_is_complete_and_byte_exact() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 1
    assert manifest["canonical_root"] == "docs/figures"
    assert manifest["current_frontier"] == "P88"
    assert manifest["current_frontier_figure"].endswith(P88_FIGURE)
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


def test_github_figure_gateway_tracks_p88() -> None:
    gateway = GATEWAY.read_text(encoding="utf-8")
    current = CURRENT.read_text(encoding="utf-8")

    assert CURRENT_SVG.read_bytes() == (DOC_FIGURES / P88_FIGURE).read_bytes()
    assert "## Current theorem frontier: P88" in gateway
    assert P88_FIGURE in gateway
    assert "manifest.json" in gateway

    assert current.startswith("# Current visual frontier: P71-P88")
    assert "## Current theorem frontier: P88" in current
    assert "L85 = 0 < L86 = 1/192 < L87 = 1/96 < L88 = 1/64" in current
    assert "| P86 |" in current
    assert "| P87 |" in current
    assert "| P88 |" in current


def test_visual_atlas_leads_with_p88_before_historical_frontiers() -> None:
    text = VISUAL_ATLAS.read_text(encoding="utf-8")
    p88 = text.index('id="p88-frontier"')
    p87 = text.index('id="p87-frontier"')
    p86 = text.index('id="p86-frontier"')
    p85 = text.index('id="p85-frontier"')

    assert p88 < p87
    assert p88 < p86
    assert p88 < p85
    current = text[p88:p87]
    assert "Current theorem frontier · P88" in current
    assert P88_FIGURE in current
    assert "L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64" in current
    assert "radius_three_bounded_primitive_quad_projection_parity_functional_separation.py" in current
    assert "test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py" in current
    assert "Previous theorem frontier · P87" in text[p87:]


def test_homepage_balances_three_research_stages_and_keeps_history_specialist() -> None:
    text = HOME.read_text(encoding="utf-8")
    research_i = text.index('id="research-i-overview"')
    p88 = text.index('id="p88-frontier"')
    research_iii = text.index('id="research-iii-overview"')
    reader_paths = text.index('id="reader-paths"')

    assert research_i < p88 < research_iii < reader_paths
    current = text[p88:research_iii]
    assert "Current theorem frontier · P88" in current
    assert P88_FIGURE in current
    assert "L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64" in current
    assert "radius_three_bounded_primitive_quad_projection_parity_functional_separation.py" in current
    assert "test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py" in current
    assert "physics_pipeline.svg" in text[research_i:p88]
    assert "measurement_architecture.svg" in text[research_iii:reader_paths]
    for historical_id in ('id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"'):
        assert historical_id not in text
    assert "The 88 results form several dependency branches." in text
    assert "all 88 propositions" in text

def test_figure_publication_synchronizer_reports_zero_drift() -> None:
    subprocess.run(
        [sys.executable, str(SYNCER), "--check"],
        cwd=ROOT,
        check=True,
    )


def test_pages_build_bundles_exact_commit_p88_figure(tmp_path: Path) -> None:
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

    deployed_p88 = site / "figures" / P88_FIGURE
    assert deployed_p88.read_bytes() == (DOC_FIGURES / P88_FIGURE).read_bytes()

    atlas = (site / "visual-atlas.html").read_text(encoding="utf-8")
    assert f'src="figures/{P88_FIGURE}"' in atlas
    assert f'src="{RAW_PREFIX}' not in atlas

    home = (site / "index.html").read_text(encoding="utf-8")
    assert f'src="figures/{P88_FIGURE}"' in home
    assert f'src="{RAW_PREFIX}' not in home
    research_i = home.index('id="research-i-overview"')
    p88 = home.index('id="p88-frontier"')
    research_iii = home.index('id="research-iii-overview"')
    reader_paths = home.index('id="reader-paths"')
    assert research_i < p88 < research_iii < reader_paths < home.index('id="plain-language"')
    for historical_id in ('id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"'):
        assert historical_id not in home
