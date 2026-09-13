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
RESEARCH_MAP = ROOT / "website" / "research-map.html"
RESEARCH_NAV = ROOT / "website" / "research-navigation.html"
SYNCER = ROOT / "scripts" / "sync_figure_publication.py"
PREPARE_WEBSITE = ROOT / "scripts" / "prepare_website.py"
P87_FIGURE = "p87_exact_bounded_primitive_quad_projection_parity.svg"
RAW_PREFIX = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/"
)

CANONICAL_BRANCHES = (
    ("Foundations", "P1-P10"),
    ("Physical description", "P11-P18"),
    ("Candidate bridge class", "P19-P24"),
    ("Operational scale", "P25-P37"),
    ("Quantum interface", "P38-P44"),
    ("Adaptive evidence acquisition", "P45-P60"),
    ("Calibration and optimization", "P61-P70"),
    ("Target provenance", "P71"),
    ("Target measurement", "P72"),
    ("Channel recovery and model testing", "P73-P87"),
)

PUBLIC_BOUNDARY = (
    "P87 is a conditional model-separation result for the declared P75 "
    "target-measurement family. It does not identify a latent state with "
    "consciousness, prove that consciousness is nonphysical, or complete the "
    "physical-to-experiential bridge. The final bridge remains open."
)


def _assert_order(text: str, values: tuple[str, ...]) -> None:
    positions = [text.index(value) for value in values]
    assert positions == sorted(positions)


def test_figure_manifest_is_complete_and_byte_exact() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 1
    assert manifest["canonical_root"] == "docs/figures"
    assert manifest["current_frontier"] == "P87"
    assert manifest["current_frontier_figure"].endswith(P87_FIGURE)
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


def test_github_figure_gateway_tracks_p87() -> None:
    gateway = GATEWAY.read_text(encoding="utf-8")
    current = CURRENT.read_text(encoding="utf-8")

    assert CURRENT_SVG.read_bytes() == (DOC_FIGURES / P87_FIGURE).read_bytes()
    assert "## Current theorem frontier: P87" in gateway
    assert P87_FIGURE in gateway
    assert "manifest.json" in gateway
    assert current.startswith("# Current visual frontier: P71 to P87")
    assert "## Current theorem frontier: P87" in current
    assert "| P87 |" in current


def test_public_website_uses_one_p87_87_result_state() -> None:
    home = HOME.read_text(encoding="utf-8")
    atlas = VISUAL_ATLAS.read_text(encoding="utf-8")

    assert "Explore all 87 results" in home
    assert "P87" in home
    assert P87_FIGURE in home
    assert "86 results" not in home
    assert "P86 current theorem frontier" not in home

    assert "P87 is the 87th public result" in atlas
    assert P87_FIGURE in atlas
    assert "86 results" not in atlas
    assert PUBLIC_BOUNDARY in home
    assert PUBLIC_BOUNDARY in atlas


def test_research_map_and_navigation_share_canonical_branch_order() -> None:
    for path in (RESEARCH_MAP, RESEARCH_NAV):
        text = path.read_text(encoding="utf-8")
        _assert_order(text, tuple(label for label, _ in CANONICAL_BRANCHES))
        _assert_order(text, tuple(result_range for _, result_range in CANONICAL_BRANCHES))
        assert "Chapter 1" not in text
        assert "Chapter 2" not in text


def test_figure_publication_synchronizer_reports_zero_drift() -> None:
    subprocess.run(
        [sys.executable, str(SYNCER), "--check"],
        cwd=ROOT,
        check=True,
    )


def test_pages_build_bundles_exact_commit_p87_figure(tmp_path: Path) -> None:
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

    deployed_p87 = site / "figures" / P87_FIGURE
    assert deployed_p87.read_bytes() == (DOC_FIGURES / P87_FIGURE).read_bytes()

    for name in ("index.html", "visual-atlas.html"):
        text = (site / name).read_text(encoding="utf-8")
        assert f'src="figures/{P87_FIGURE}"' in text
        assert f'src="{RAW_PREFIX}' not in text

    assert "Explore all 87 results" in (site / "index.html").read_text(encoding="utf-8")
    assert (site / "research-navigation.html").is_file()
