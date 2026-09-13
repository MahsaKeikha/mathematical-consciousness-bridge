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
P88_FIGURE = "p88_exact_radius3_bounded_primitive_quad_projection_parity.svg"
P87_FIGURE = "p87_exact_bounded_primitive_quad_projection_parity.svg"
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


def test_github_figure_gateway_tracks_p88_and_preserves_p87_history() -> None:
    gateway = GATEWAY.read_text(encoding="utf-8")
    current = CURRENT.read_text(encoding="utf-8")

    assert CURRENT_SVG.read_bytes() == (DOC_FIGURES / P88_FIGURE).read_bytes()
    assert "## Current theorem frontier: P88" in gateway
    assert P88_FIGURE in gateway
    assert "manifest.json" in gateway

    assert current.startswith("# Current visual frontier: P71-P88")
    assert "## Current theorem frontier: P88" in current
    assert "L85 = 0 < L86 = 1/192 < L87 = 1/96 < L88 = 1/64" in current
    assert "| P85 |" in current
    assert "| P86 |" in current
    assert "| P87 |" in current
    assert "| P88 |" in current
    assert P87_FIGURE in current


def test_visual_atlas_leads_with_p88_then_preserves_p87_history() -> None:
    text = VISUAL_ATLAS.read_text(encoding="utf-8")
    p88 = text.index('id="p88-frontier"')
    p87 = text.index('id="p87-frontier"')
    p86 = text.index('id="p86-frontier"')
    p84 = text.index('id="p84-frontier"')
    p85 = text.index('id="p85-frontier"')

    assert p88 < p87 < p86
    assert p88 < p84
    assert p88 < p85
    current = text[p88:p87]
    assert "Current theorem frontier · P88" in current
    assert P88_FIGURE in current
    assert "L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64" in current
    assert "bounded_primitive_radius3_quad_projection_parity_functional_separation.py" in current
    assert "test_bounded_primitive_radius3_quad_projection_parity_functional_separation.py" in current
    assert "Previous theorem frontier · P87" in text[p87:p86]
    assert P87_FIGURE in text[p87:]
    assert "Current theorem frontier · P87" not in text


def test_homepage_leads_with_p88_and_keeps_reader_first_structure() -> None:
    text = HOME.read_text(encoding="utf-8")
    p88 = text.index('id="p88-frontier"')
    p87 = text.index('id="p87-frontier"')
    plain = text.index('id="plain-language"')
    p86 = text.index('id="p86-frontier"')

    assert p88 < p87 < plain
    assert p88 < p86
    current = text[p88:p87]
    assert "Current theorem frontier · P88" in current
    assert P88_FIGURE in current
    assert "L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64" in current
    assert "bounded_primitive_radius3_quad_projection_parity_functional_separation.py" in current
    assert "test_bounded_primitive_radius3_quad_projection_parity_functional_separation.py" in current
    assert "Previous theorem frontier · P87" in text[p87:plain]
    assert "Current theorem frontier · P87" not in text
    assert "Explore all 88 results" in text
    assert "What would a scientifically testable bridge from physical description to experience actually require?" in text


def test_figure_publication_synchronizer_reports_zero_drift() -> None:
    subprocess.run(
        [sys.executable, str(SYNCER), "--check"],
        cwd=ROOT,
        check=True,
    )


def test_pages_build_bundles_exact_commit_p88_and_p87_figures(tmp_path: Path) -> None:
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

    for figure in (P88_FIGURE, P87_FIGURE):
        deployed = site / "figures" / figure
        assert deployed.read_bytes() == (DOC_FIGURES / figure).read_bytes()

    atlas = (site / "visual-atlas.html").read_text(encoding="utf-8")
    assert f'src="figures/{P88_FIGURE}"' in atlas
    assert f'src="figures/{P87_FIGURE}"' in atlas
    assert f'src="{RAW_PREFIX}' not in atlas

    home = (site / "index.html").read_text(encoding="utf-8")
    assert f'src="figures/{P88_FIGURE}"' in home
    assert f'src="figures/{P87_FIGURE}"' in home
    assert f'src="{RAW_PREFIX}' not in home
    assert home.index('id="p88-frontier"') < home.index('id="p87-frontier"')
    assert home.index('id="p88-frontier"') < home.index('id="plain-language"')
