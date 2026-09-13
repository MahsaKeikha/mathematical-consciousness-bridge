"""Apply the one-time P86 publication-integration repair deterministically."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise RuntimeError(f"expected exactly one {label} in {path.relative_to(ROOT)}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def repair_syncer() -> None:
    path = ROOT / "scripts" / "sync_figure_publication.py"
    text = path.read_text(encoding="utf-8")
    dash = chr(0x2014)
    if text.count(dash) != 1:
        raise RuntimeError("expected exactly one em dash in figure synchronizer")
    path.write_text(text.replace(dash, "N/A"), encoding="utf-8")


def repair_website_builder() -> None:
    path = ROOT / "scripts" / "prepare_website.py"
    old = '''    frontier_figure = output / "figures" / CURRENT_FRONTIER_FIGURE
    if not frontier_figure.is_file():
        raise RuntimeError(
            "website build is missing the current P86 theorem figure: "
            f"{frontier_figure}"
        )

    visual_atlas = (output / "visual-atlas.html").read_text(encoding="utf-8")
    local_frontier_src = f'src="figures/{CURRENT_FRONTIER_FIGURE}"'
    if local_frontier_src not in visual_atlas:
        raise RuntimeError("Visual Atlas does not use the bundled P86 theorem figure")
    if f'src="{RAW_FIGURE_PREFIX}' in visual_atlas:
        raise RuntimeError("Visual Atlas still depends on raw GitHub main for figures")
'''
    new = '''    visual_atlas_path = output / "visual-atlas.html"
    if visual_atlas_path.is_file():
        frontier_figure = output / "figures" / CURRENT_FRONTIER_FIGURE
        if not frontier_figure.is_file():
            raise RuntimeError(
                "website build is missing the current P86 theorem figure: "
                f"{frontier_figure}"
            )

        visual_atlas = visual_atlas_path.read_text(encoding="utf-8")
        local_frontier_src = f'src="figures/{CURRENT_FRONTIER_FIGURE}"'
        if local_frontier_src not in visual_atlas:
            raise RuntimeError("Visual Atlas does not use the bundled P86 theorem figure")
        if f'src="{RAW_FIGURE_PREFIX}' in visual_atlas:
            raise RuntimeError("Visual Atlas still depends on raw GitHub main for figures")
'''
    _replace_once(path, old, new, "exact-commit website verification block")


def repair_reproducibility_contract() -> None:
    path = ROOT / "tests" / "test_reproducibility_contract.py"
    old = '''def test_unified_figure_build_reapplies_documentation_metadata() -> None:
    source = _read("scripts/generate_all_figures.py")
    assert "enrich_figure_documentation.py" in source
    assert "_run_generator(ENRICHER)" in source
'''
    new = '''def test_unified_figure_build_reapplies_documentation_metadata() -> None:
    source = _read("scripts/generate_all_figures.py")
    assert "enrich_figure_documentation.py" in source
    assert "_run_script(ENRICHER)" in source
    assert "_run_script(PUBLICATION_SYNCER)" in source
    assert '_run_script(PUBLICATION_SYNCER, "--check")' in source
'''
    _replace_once(path, old, new, "unified figure build contract")


def main() -> None:
    repair_syncer()
    repair_website_builder()
    repair_reproducibility_contract()
    print("P86 publication contract repair applied")


if __name__ == "__main__":
    main()
