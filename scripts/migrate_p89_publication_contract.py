"""One-shot migration of hard-coded publication contracts from P88 to P89.

This helper updates maintained synchronizers/builders/verifiers so the permanent
contract follows P89 and the balanced Research I -> Research II -> Research III
reader architecture. It is intentionally separate from the canonical promoter;
once the migration is committed and validated this helper can be removed.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rewrite(path: str, transform) -> None:
    target = ROOT / path
    original = target.read_text(encoding="utf-8")
    updated = transform(original)
    if updated == original:
        print(f"[migration] unchanged: {path}")
        return
    target.write_text(updated, encoding="utf-8")
    print(f"[migration] updated: {path}")


def migrate_sync(text: str) -> str:
    text = text.replace("matching P88\npublication script", "matching P89\npublication script")
    text = text.replace(
        'PROMOTER = ROOT / "scripts" / "promote_p88_public_frontier.py"',
        'PROMOTER = ROOT / "scripts" / "promote_p89_public_frontier.py"',
    )
    old_block = re.compile(
        r"    if frontier == 88:\n        lines\.extend\(\[.*?        \]\)\n",
        re.DOTALL,
    )
    p89_block = '''    if frontier == 89:\n        lines.extend([\n            "### Exact P89 complete-linear witness", "",\n            "P89 removes both the finite coefficient-radius restriction and the exactly-four-observable support restriction. It considers every real linear functional of all eleven canonical P83 parity coordinates and proves the exact optimum by matching rational lower and upper certificates:", "",\n            "```text",\n            "L88 = 1/64 < L89 = 5/168",\n            "all real coefficient vectors c in R^11 except zero",\n            "matching zero-mass perturbation radius = 5/168",\n            "```", "",\n            "The strict P89 direction is `(0, -2, -1, 1, 1, 1, -2, -1, -3, 2, -3)`, with empirical value `-13/6`, exact P75 interval `[-51/8, -3]`, gap `5/6`, and centered norm `28`.", "",\n            "This is complete only for the declared real linear parity-functional class. It does not identify a latent state with conscious experience or exhaust nonlinear P75 constraints.", "",\n        ])\n'''
    text, count = old_block.subn(p89_block, text, count=1)
    if count != 1 and "if frontier == 89:" not in text:
        raise RuntimeError("could not migrate sync_figure_publication frontier summary")

    check_pattern = re.compile(
        r"def _check_reader_surfaces\(frontier: int\) -> None:\n.*?\n\ndef main\(\) -> None:",
        re.DOTALL,
    )
    new_check = '''def _check_reader_surfaces(frontier: int) -> None:\n    if frontier != 89:\n        return\n    home = HOME.read_text(encoding="utf-8")\n    atlas = VISUAL_ATLAS.read_text(encoding="utf-8")\n    plain = (ROOT / "website" / "plain-language.html").read_text(encoding="utf-8")\n    start = (ROOT / "website" / "start-here.html").read_text(encoding="utf-8")\n    required_home = (\n        "Explore all 89 results",\n        "Research I · Physical-system identification",\n        'id="research-i-overview"',\n        "physics_pipeline.svg",\n        "Research II · Bridge sufficiency and falsification",\n        "P89 current theorem frontier · v0.82.0",\n        'id="p89-frontier"',\n        "Current theorem frontier · P89",\n        "Research III · Consciousness measurement science",\n        'id="research-iii-overview"',\n        "measurement_architecture.svg",\n        "Open</strong><span>physical-to-experiential bridge",\n    )\n    required_atlas = (\n        'id="p89-frontier"',\n        "Current theorem frontier · P89",\n        "Previous theorem frontier · P88",\n    )\n    required_plain = (\n        '<strong>Research I</strong><span>physical-system identification</span>',\n        '<strong>Research II</strong><span>89 results · current frontier P89</span>',\n        '<strong>Research III</strong><span>measurement science under uncertainty</span>',\n        'id="three-stage-progress"',\n        'id="p89-reader-frontier"',\n    )\n    required_start = (\n        '<strong>Research I</strong><span>physical-system identification</span>',\n        '<strong>Research II</strong><span>89 results · current frontier P89</span>',\n        '<strong>Research III</strong><span>measurement science under uncertainty</span>',\n        'id="program-stages"',\n        "The 89 Research II propositions by scientific role",\n    )\n    for label, source, markers in (\n        ("homepage", home, required_home),\n        ("Visual Atlas", atlas, required_atlas),\n        ("Plain Language", plain, required_plain),\n        ("Start Here", start, required_start),\n    ):\n        missing = [marker for marker in markers if marker not in source]\n        if missing:\n            raise RuntimeError(f"{label} is not synchronized to P89 balanced publication state: {missing}")\n    research_i = home.index('id="research-i-overview"')\n    p89_home = home.index('id="p89-frontier"')\n    research_iii = home.index('id="research-iii-overview"')\n    if home.index('class="research-dashboard"') > research_i:\n        raise RuntimeError("homepage must orient readers to the full research program before stage details")\n    if not (research_i < p89_home < research_iii):\n        raise RuntimeError("homepage must balance Research I, Research II/P89, and Research III in stage order")\n    for historical_id in ('id="p88-frontier"', 'id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"'):\n        if historical_id in home:\n            raise RuntimeError("historical Research II frontiers must remain off the Overview")\n    if atlas.index('id="p89-frontier"') > atlas.index('id="p88-frontier"'):\n        raise RuntimeError("Visual Atlas does not lead with P89")\n\n\ndef main() -> None:'''
    text, count = check_pattern.subn(new_check, text, count=1)
    if count != 1:
        raise RuntimeError("could not replace sync_figure_publication reader contract")
    text = text.replace("if frontier == 88:\n        subprocess.run", "if frontier == 89:\n        subprocess.run")
    return text


def migrate_verifier(text: str) -> str:
    text = text.replace('CURRENT_FRONTIER = "P88"', 'CURRENT_FRONTIER = "P89"')
    anchor = '    "docs/figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg",\n'
    addition = anchor + '    "docs/figures/p89_complete_linear_parity_duality.svg",\n'
    if '"docs/figures/p89_complete_linear_parity_duality.svg"' not in text:
        text = text.replace(anchor, addition)
    anchor = '    "docs/p88_equation_provenance.md",\n'
    addition = anchor + '    "docs/proposition_89_complete_linear_parity_duality.md",\n    "docs/p89_equation_provenance.md",\n'
    if '"docs/proposition_89_complete_linear_parity_duality.md"' not in text:
        text = text.replace(anchor, addition)
    if '"scripts/promote_p89_public_frontier.py"' not in text:
        text = text.replace(
            '    "scripts/sync_figure_publication.py",\n',
            '    "scripts/sync_figure_publication.py",\n    "scripts/promote_p89_public_frontier.py",\n    "scripts/synchronize_p89_reader_frontier_phrases.py",\n',
        )
    text = text.replace("for number in range(1, 89):", "for number in range(1, 90):")
    text = text.replace(
        '"p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg"',
        '"p89_complete_linear_parity_duality.svg"',
        1,
    )
    atlas_pattern = re.compile(
        r"    visual_atlas = _read\(\"website/visual-atlas\.html\"\)\n    p88 = .*?raise RuntimeError\(\"Visual Atlas does not lead with the current P88 figure\"\)\n",
        re.DOTALL,
    )
    atlas_block = '''    visual_atlas = _read("website/visual-atlas.html")\n    p89 = visual_atlas.index('id="p89-frontier"')\n    p88 = visual_atlas.index('id="p88-frontier"')\n    p87 = visual_atlas.index('id="p87-frontier"')\n    if not (p89 < p88 < p87):\n        raise RuntimeError("Visual Atlas does not lead with the current P89 figure")\n'''
    text, count = atlas_pattern.subn(atlas_block, text, count=1)
    if count != 1:
        raise RuntimeError("could not migrate verifier Visual Atlas contract")
    stale_insert = '    "Current theorem frontier · P88",\n    "current P88 frontier",\n    "<strong>P88</strong><span>current theorem frontier</span>",\n'
    marker = "STALE_READER_FRONTIER_MARKERS = (\n"
    if stale_insert.strip() not in text:
        text = text.replace(marker, marker + stale_insert, 1)
    return text


def migrate_prepare(text: str) -> str:
    text = text.replace("P88_HOME_MARKER", "P89_HOME_MARKER")
    text = text.replace(
        '"p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg"',
        '"p89_complete_linear_parity_duality.svg"',
    )
    text = text.replace(
        'CURRENT_RECORD_TEXT = "Current record:</strong> 88 proposition-level results through P88"',
        'CURRENT_RECORD_TEXT = "Current record:</strong> 89 proposition-level results through P89"',
    )
    text = text.replace("consistent with P88", "consistent with P89")
    text = text.replace("current P88 theorem figure", "current P89 theorem figure")
    text = text.replace("bundled P88 theorem figure", "bundled P89 theorem figure")
    text = text.replace("synchronized to 88/P88", "synchronized to 89/P89")
    text = text.replace('id="p88-frontier"', 'id="p89-frontier"')
    text = text.replace("stale pre-P88 reader text", "stale pre-P89 reader text")
    text = text.replace(
        '"<strong>88</strong><span>proposition-level results</span>",\n        "<strong>P88</strong><span>current theorem frontier</span>",',
        '"<strong>89</strong><span>proposition-level results</span>",\n        "<strong>P89</strong><span>current theorem frontier</span>",',
    )
    return text


def migrate_research_three_sync(text: str) -> str:
    text = text.replace("P88_HOME_MARKER", "P89_HOME_MARKER")
    text = text.replace('"<!-- current-frontier-home: P88 -->"', '"<!-- current-frontier-home: P89 -->"')
    return text


def main() -> None:
    rewrite("scripts/sync_figure_publication.py", migrate_sync)
    rewrite("scripts/verify_repository.py", migrate_verifier)
    rewrite("scripts/prepare_website.py", migrate_prepare)
    rewrite("scripts/synchronize_research_three_website.py", migrate_research_three_sync)


if __name__ == "__main__":
    main()
