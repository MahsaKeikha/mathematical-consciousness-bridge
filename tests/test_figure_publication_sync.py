import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC_FIGURES = ROOT / "docs" / "figures"
DOCS = ROOT / "docs"
MANIFEST = ROOT / "figures" / "manifest.json"
GATEWAY = ROOT / "figures" / "README.md"
CURRENT = ROOT / "figures" / "CURRENT_FRONTIER.md"
CURRENT_SVG = ROOT / "figures" / "current_frontier.svg"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"
HOME = ROOT / "website" / "index.html"
SYNCER = ROOT / "scripts" / "sync_figure_publication.py"
PREPARE_WEBSITE = ROOT / "scripts" / "prepare_website.py"
RAW_PREFIX = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/"
)


def _frontier() -> int:
    numbers: list[int] = []
    for path in DOCS.glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers
    return max(numbers)


def _manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def _frontier_figure() -> str:
    manifest = _manifest()
    return Path(manifest["current_frontier_figure"]).name


def test_figure_manifest_is_complete_and_byte_exact() -> None:
    frontier = _frontier()
    manifest = _manifest()
    assert manifest["schema_version"] == 1
    assert manifest["canonical_root"] == "docs/figures"
    assert manifest["current_frontier"] == f"P{frontier}"
    current_figure = Path(manifest["current_frontier_figure"])
    assert current_figure.name.startswith(f"p{frontier}_")
    assert (ROOT / current_figure).is_file()
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


def test_github_figure_gateway_tracks_current_frontier() -> None:
    frontier = _frontier()
    figure = _frontier_figure()
    gateway = GATEWAY.read_text(encoding="utf-8")
    current = CURRENT.read_text(encoding="utf-8")

    assert CURRENT_SVG.read_bytes() == (DOC_FIGURES / figure).read_bytes()
    assert f"## Current theorem frontier: P{frontier}" in gateway
    assert figure in gateway
    assert "manifest.json" in gateway

    assert current.startswith(f"# Current visual frontier: P71-P{frontier}")
    assert f"## Current theorem frontier: P{frontier}" in current
    assert figure in current
    assert f"| P{frontier} |" in current
    if frontier > 71:
        assert f"| P{frontier - 1} |" in current


def test_visual_atlas_leads_with_current_before_historical_frontiers() -> None:
    frontier = _frontier()
    previous = frontier - 1
    figure = _frontier_figure()
    text = VISUAL_ATLAS.read_text(encoding="utf-8")
    current_id = f'id="p{frontier}-frontier"'
    previous_id = f'id="p{previous}-frontier"'
    current_pos = text.index(current_id)
    previous_pos = text.index(previous_id)

    assert current_pos < previous_pos
    current = text[current_pos:previous_pos]
    assert f"Current theorem frontier · P{frontier}" in current
    assert figure in current
    assert "Implementation" in current
    assert "Exact tests" in current
    assert f"Previous theorem frontier · P{previous}" in text[previous_pos:]


def test_homepage_leads_with_current_before_historical_frontiers() -> None:
    frontier = _frontier()
    previous = frontier - 1
    figure = _frontier_figure()
    text = HOME.read_text(encoding="utf-8")
    current_id = f'id="p{frontier}-frontier"'
    previous_id = f'id="p{previous}-frontier"'
    current_pos = text.index(current_id)
    plain = text.index('id="plain-language"')
    previous_pos = text.index(previous_id)

    assert current_pos < plain
    assert current_pos < previous_pos
    current = text[current_pos:plain]
    assert f"Current theorem frontier · P{frontier}" in current
    assert figure in current
    assert "Implementation" in current
    assert "Exact tests" in current
    assert f"Previous theorem frontier · P{previous}" in text[previous_pos:]
    assert f"Current theorem frontier · P{previous}" not in text
    assert f"The {previous} results form several dependency branches." not in text
    assert f"all {previous} propositions" not in text
    assert f"The {frontier} results form several dependency branches." in text
    assert f"all {frontier} propositions" in text


def test_figure_publication_synchronizer_reports_zero_drift() -> None:
    subprocess.run(
        [sys.executable, str(SYNCER), "--check"],
        cwd=ROOT,
        check=True,
    )


def test_pages_build_bundles_exact_current_frontier_figure(tmp_path: Path) -> None:
    frontier = _frontier()
    figure = _frontier_figure()
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

    deployed = site / "figures" / figure
    assert deployed.read_bytes() == (DOC_FIGURES / figure).read_bytes()

    atlas = (site / "visual-atlas.html").read_text(encoding="utf-8")
    assert f'src="figures/{figure}"' in atlas
    assert f'src="{RAW_PREFIX}' not in atlas

    home = (site / "index.html").read_text(encoding="utf-8")
    assert f'src="figures/{figure}"' in home
    assert f'src="{RAW_PREFIX}' not in home
    assert home.index(f'id="p{frontier}-frontier"') < home.index('id="plain-language"')
    if frontier > 71:
        assert home.index(f'id="p{frontier}-frontier"') < home.index(
            f'id="p{frontier - 1}-frontier"'
        )
