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
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"
SYNCER = ROOT / "scripts" / "sync_figure_publication.py"


def test_figure_manifest_is_complete_and_byte_exact() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 1
    assert manifest["canonical_root"] == "docs/figures"
    assert manifest["current_frontier"] == "P86"
    assert manifest["current_frontier_figure"].endswith(
        "p86_exact_minimally_weighted_quad_projection_parity.svg"
    )
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


def test_github_figure_gateway_tracks_p86() -> None:
    gateway = GATEWAY.read_text(encoding="utf-8")
    current = CURRENT.read_text(encoding="utf-8")

    assert "## Current theorem frontier: P86" in gateway
    assert "p86_exact_minimally_weighted_quad_projection_parity.svg" in gateway
    assert "manifest.json" in gateway
    assert "P81 - Projection-Event Certificate" not in gateway

    assert current.startswith("# Current visual frontier: P71-P86")
    assert "## Current theorem frontier: P86" in current
    assert "L85 = 0 < L86 = 1/192" in current
    assert "| P84 |" in current
    assert "| P85 |" in current
    assert "| P86 |" in current


def test_visual_atlas_leads_with_p86_before_historical_frontiers() -> None:
    text = VISUAL_ATLAS.read_text(encoding="utf-8")
    p86 = text.index('id="p86-frontier"')
    p84 = text.index('id="p84-frontier"')
    p85 = text.index('id="p85-frontier"')

    assert p86 < p84 < p85
    assert "Current theorem frontier · P86" in text[p86:p84]
    assert "p86_exact_minimally_weighted_quad_projection_parity.svg" in text[p86:p84]
    assert "L85 = 0 &lt; L86 = 1/192" in text[p86:p84]
    assert "weighted_quad_projection_parity_functional_separation.py" in text[p86:p84]
    assert "test_weighted_quad_projection_parity_functional_separation.py" in text[
        p86:p84
    ]


def test_figure_publication_synchronizer_reports_zero_drift() -> None:
    subprocess.run(
        [sys.executable, str(SYNCER), "--check"],
        cwd=ROOT,
        check=True,
    )
