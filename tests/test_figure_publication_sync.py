import hashlib
import json
import re
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
VERIFIER = ROOT / "scripts" / "verify_repository.py"
RAW_PREFIX = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/"
)


def _current_frontier() -> tuple[int, str]:
    verifier = VERIFIER.read_text(encoding="utf-8")
    match = re.search(r'^CURRENT_FRONTIER = "P(\d+)"$', verifier, flags=re.MULTILINE)
    assert match is not None
    number = int(match.group(1))
    return number, f"P{number}"


def _manifest() -> dict[str, object]:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def _current_figure() -> str:
    manifest = _manifest()
    path = str(manifest["current_frontier_figure"])
    return Path(path).name


def test_figure_manifest_is_complete_and_byte_exact() -> None:
    manifest = _manifest()
    frontier, label = _current_frontier()
    assert manifest["schema_version"] == 1
    assert manifest["canonical_root"] == "docs/figures"
    assert manifest["current_frontier"] == label
    assert str(manifest["current_frontier_figure"]).startswith(
        f"docs/figures/p{frontier}_"
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


def test_github_figure_gateway_tracks_current_frontier() -> None:
    frontier, label = _current_frontier()
    figure = _current_figure()
    gateway = GATEWAY.read_text(encoding="utf-8")
    current = CURRENT.read_text(encoding="utf-8")

    assert CURRENT_SVG.read_bytes() == (DOC_FIGURES / figure).read_bytes()
    assert f"## Current theorem frontier: {label}" in gateway
    assert figure in gateway
    assert "manifest.json" in gateway

    assert current.startswith(f"# Current visual frontier: P71-P{frontier}")
    assert f"## Current theorem frontier: {label}" in current
    assert figure in current
    assert f"| {label} |" in current
    for proposition in range(max(89, frontier - 4), frontier):
        assert f"| P{proposition} |" in current


def test_visual_atlas_leads_with_current_before_previous_frontiers() -> None:
    frontier, label = _current_frontier()
    figure = _current_figure()
    previous = frontier - 1
    text = VISUAL_ATLAS.read_text(encoding="utf-8")
    current_pos = text.index(f'id="p{frontier}-frontier"')
    previous_pos = text.index(f'id="p{previous}-frontier"')

    assert current_pos < previous_pos
    current = text[current_pos:previous_pos]
    assert f"Current theorem frontier · {label}" in current
    assert figure in current
    assert f"proposition_{frontier}_" in current
    assert f"Immediate predecessor · P{previous}" in text[previous_pos:]


def test_homepage_balances_three_research_stages_and_keeps_history_specialist() -> None:
    frontier, label = _current_frontier()
    figure = _current_figure()
    text = HOME.read_text(encoding="utf-8")
    research_i = text.index('id="research-i-overview"')
    current = text.index(f'id="p{frontier}-frontier"')
    research_iii = text.index('id="research-iii-overview"')
    reader_paths = text.index('id="reader-paths"')

    assert research_i < current < research_iii < reader_paths
    block = text[current:research_iii]
    assert f"Current theorem frontier · {label}" in block
    assert figure in block
    assert f"proposition_{frontier}_" in block
    assert "physics_pipeline.svg" in text[research_i:current]
    assert "measurement_architecture.svg" in text[research_iii:reader_paths]
    assert f"The {frontier} results form several dependency branches." in text
    assert f"all {frontier} propositions" in text
    for historical in range(88, frontier):
        assert f'id="p{historical}-frontier"' not in text


def test_plain_language_and_start_here_preserve_three_stage_architecture() -> None:
    frontier, label = _current_frontier()
    plain = PLAIN.read_text(encoding="utf-8")
    start = START.read_text(encoding="utf-8")

    for source in (plain, start):
        assert "Research I" in source
        assert "Research II" in source
        assert "Research III" in source
        assert str(frontier) in source
        assert label in source
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


def test_pages_build_bundles_exact_commit_current_figure(tmp_path: Path) -> None:
    frontier, _ = _current_frontier()
    figure = _current_figure()
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
    research_i = home.index('id="research-i-overview"')
    current = home.index(f'id="p{frontier}-frontier"')
    research_iii = home.index('id="research-iii-overview"')
    reader_paths = home.index('id="reader-paths"')
    assert research_i < current < research_iii < reader_paths < home.index(
        'id="plain-language"'
    )
    for historical in range(88, frontier):
        assert f'id="p{historical}-frontier"' not in home
