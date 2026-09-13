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
HOME = ROOT / "website" / "index.html"
SYNCER = ROOT / "scripts" / "sync_figure_publication.py"
PREPARE_WEBSITE = ROOT / "scripts" / "prepare_website.py"
P86_FIGURE = "p86_exact_minimally_weighted_quad_projection_parity.svg"
RAW_PREFIX = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/"
)


def test_figure_manifest_is_complete_and_byte_exact() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 1
    assert manifest["canonical_root"] == "docs/figures"
    assert manifest["current_frontier"] == "P86"
    assert manifest["current_frontier_figure"].endswith(P86_FIGURE)
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
    assert P86_FIGURE in gateway
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
    assert P86_FIGURE in text[p86:p84]
    assert "L85 = 0 &lt; L86 = 1/192" in text[p86:p84]
    assert "weighted_quad_projection_parity_functional_separation.py" in text[p86:p84]
    assert "test_weighted_quad_projection_parity_functional_separation.py" in text[
        p86:p84
    ]


def test_homepage_leads_with_p86_before_historical_frontiers() -> None:
    text = HOME.read_text(encoding="utf-8")
    p86 = text.index('id="p86-frontier"')
    plain = text.index('id="plain-language"')
    p84 = text.index('id="p84-frontier"')
    p85 = text.index('id="p85-frontier"')

    assert p86 < plain
    assert p86 < p84
    assert p86 < p85
    current = text[p86:plain]
    assert "Current theorem frontier · P86" in current
    assert P86_FIGURE in current
    assert "L85 = 0 &lt; L86 = 1/192" in current
    assert "weighted_quad_projection_parity_functional_separation.py" in current
    assert "test_weighted_quad_projection_parity_functional_separation.py" in current
    assert "Previous theorem frontier · P84" in text[p84:]
    assert "Previous theorem frontier · P85" in text[p85:]
    assert "Current theorem frontier · P85" not in text
    assert "The 84 results form several dependency branches." not in text
    assert "all 84 propositions" not in text
    assert "P71-P84, then read the falsification program" not in text
    assert "The 86 results form several dependency branches." in text
    assert "all 86 propositions" in text


def test_figure_publication_synchronizer_reports_zero_drift() -> None:
    subprocess.run(
        [sys.executable, str(SYNCER), "--check"],
        cwd=ROOT,
        check=True,
    )


def test_pages_build_bundles_exact_commit_p86_figure(tmp_path: Path) -> None:
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

    deployed_p86 = site / "figures" / P86_FIGURE
    assert deployed_p86.read_bytes() == (DOC_FIGURES / P86_FIGURE).read_bytes()

    atlas = (site / "visual-atlas.html").read_text(encoding="utf-8")
    assert f'src="figures/{P86_FIGURE}"' in atlas
    assert f'src="{RAW_PREFIX}' not in atlas

    home = (site / "index.html").read_text(encoding="utf-8")
    assert f'src="figures/{P86_FIGURE}"' in home
    assert f'src="{RAW_PREFIX}' not in home
    assert home.index('id="p86-frontier"') < home.index('id="plain-language"')
    assert home.index('id="p86-frontier"') < home.index('id="p85-frontier"')
