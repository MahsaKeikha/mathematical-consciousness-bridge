"""Finalize the one-run P94 publication migration deterministically.

This helper runs after ``promote_p94_public_frontier.py``. It removes residual
P93 hard-codes from permanent publication machinery, repairs reader and citation
contracts, and leaves figure regeneration to ``generate_all_figures.py``.

Delete this helper together with the temporary promotion workflow and the
reader-contract helper after the exact promoted head is validated.
"""

from __future__ import annotations

from pathlib import Path

from repair_p94_reader_contracts import main as repair_reader_contracts

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_one_of(path: str, text: str, old: str, new: str) -> str:
    if old in text:
        if text.count(old) != 1:
            raise RuntimeError(f"{path}: expected one {old!r}, found {text.count(old)}")
        return text.replace(old, new, 1)
    if new in text:
        return text
    raise RuntimeError(f"{path}: found neither old nor promoted marker for {old!r}")


def repair_formal_provenance() -> None:
    path = "docs/proposition_94_finite_range_dependent_sign_coherence.md"
    text = read(path)
    wrong = "certify_p94_temporal_pooling_no_go_exact()"
    right = "certify_p94_temporal_drift_no_go_exact()"
    if wrong in text:
        text = replace_one_of(path, text, wrong, right)
    if text.count(right) != 1:
        raise RuntimeError(f"{path}: expected exactly one executable drift certificate name")
    write(path, text)


def repair_homepage() -> None:
    path = "website/index.html"
    text = read(path)
    replacements = (
        (
            "<strong>93</strong><span>proposition-level results</span>",
            "<strong>94</strong><span>proposition-level results</span>",
        ),
        (
            "P93 current theorem frontier · v0.82.0",
            "P94 current theorem frontier · v0.82.0",
        ),
        ("Explore all 93 results", "Explore all 94 results"),
        ("current P93 frontier", "current P94 frontier"),
        (
            'sources.html#p93-source">P93 sources',
            'sources.html#p94-source">P94 sources',
        ),
    )
    for old, new in replacements:
        text = replace_one_of(path, text, old, new)
    write(path, text)


def repair_website_research_map() -> None:
    path = "website/research-map.html"
    text = read(path)
    replacements = (
        ("P71-P93 return", "P71-P94 return"),
        (
            "<strong>93</strong><span>proposition-level results</span>",
            "<strong>94</strong><span>proposition-level results</span>",
        ),
        (
            "<strong>P93</strong><span>current theorem frontier</span>",
            "<strong>P94</strong><span>current theorem frontier</span>",
        ),
        ("P74-P93 continue", "P74-P94 continue"),
        ("<span>6 · P73-P93</span>", "<span>6 · P73-P94</span>"),
        (
            "culminating in P92 exact global mixed-prevalence distance and the P93 finite-sample rejection handoff.",
            "culminating in P92 exact global mixed-prevalence distance, the P93 IID finite-sample handoff, and P94 finite-range dependent rejection.",
        ),
        (
            "P19 and P71-P93: from sufficiency to falsifiable target-model separation",
            "P19 and P71-P94: from sufficiency to finite-range dependent target-model falsification",
        ),
        (
            'href="index.html#p93-frontier">Continue to the current P93 frontier',
            'href="index.html#p94-frontier">Continue to the current P94 frontier',
        ),
        (
            'href="visual-atlas.html#p93-frontier">See the P93 figure',
            'href="visual-atlas.html#p94-frontier">See the P94 figure',
        ),
        (
            'docs/p93_equation_provenance.md">Audit P93 provenance',
            'docs/p94_equation_provenance.md">Audit P94 provenance',
        ),
    )
    for old, new in replacements:
        text = replace_one_of(path, text, old, new)
    write(path, text)


def repair_repository_verifier() -> None:
    path = "scripts/verify_repository.py"
    text = read(path)

    citation_old = (
        'if f"Current documented theorem frontier: {CURRENT_FRONTIER}" not in citation:\n'
        '        raise RuntimeError(f"CITATION.md does not declare {CURRENT_FRONTIER} as the current theorem frontier")'
    )
    citation_new = (
        'if f"The current documented theorem frontier is **{CURRENT_FRONTIER}**." not in citation:\n'
        '        raise RuntimeError(f"CITATION.md does not declare {CURRENT_FRONTIER} as the current theorem frontier")'
    )
    text = replace_one_of(path, text, citation_old, citation_new)

    coverage_old = "missing = [number for number in range(1, 94) if number not in covered]"
    coverage_new = (
        'frontier_number = int(CURRENT_FRONTIER.removeprefix("P"))\n'
        '    missing = [number for number in range(1, frontier_number + 1) if number not in covered]'
    )
    text = replace_one_of(path, text, coverage_old, coverage_new)

    figure_old = '''    if not figure_path.endswith("p93_localized_sign_coherence_rejection.svg"):
        raise RuntimeError("figure manifest does not point to the canonical P93 SVG")
    figures = manifest.get("figures")
    if not isinstance(figures, list) or len(figures) != 151:
        raise RuntimeError("figure manifest does not contain the canonical 151 figures")'''
    figure_new = '''    frontier_number = int(CURRENT_FRONTIER.removeprefix("P"))
    expected = sorted((ROOT / "docs" / "figures").glob(f"p{frontier_number}_*.svg"))
    if len(expected) != 1:
        raise RuntimeError(f"expected exactly one canonical {CURRENT_FRONTIER} SVG, found {expected}")
    expected_path = expected[0].relative_to(ROOT).as_posix()
    if figure_path != expected_path:
        raise RuntimeError(
            f"figure manifest current figure is {figure_path!r}, expected {expected_path!r}"
        )
    figures = manifest.get("figures")
    canonical_count = len(list((ROOT / "docs" / "figures").rglob("*.svg")))
    if not isinstance(figures, list) or len(figures) != canonical_count:
        observed = len(figures) if isinstance(figures, list) else "invalid"
        raise RuntimeError(
            f"figure manifest contains {observed} figures; canonical tree contains {canonical_count}"
        )'''
    text = replace_one_of(path, text, figure_old, figure_new)

    atlas_old = '''    p93 = visual_atlas.index('id="p93-frontier"')
    p92 = visual_atlas.index('id="p92-frontier"')
    p91 = visual_atlas.index('id="p91-frontier"')
    if not (p93 < p92 < p91):
        raise RuntimeError("Visual Atlas does not lead with the current P93 figure")'''
    atlas_new = '''    frontier_number = int(CURRENT_FRONTIER.removeprefix("P"))
    current_marker = f'id="p{frontier_number}-frontier"'
    previous_marker = f'id="p{frontier_number - 1}-frontier"'
    current_position = visual_atlas.index(current_marker)
    previous_position = visual_atlas.index(previous_marker)
    if current_position >= previous_position:
        raise RuntimeError(
            f"Visual Atlas does not lead P{frontier_number} ahead of P{frontier_number - 1}"
        )'''
    text = replace_one_of(path, text, atlas_old, atlas_new)
    write(path, text)


def repair_research_three_syncer() -> None:
    path = "scripts/synchronize_research_three_website.py"
    text = read(path)
    old = 'CURRENT_HOME_MARKER = "<!-- current-frontier-home: P93 -->"'
    new = '''ROOT = Path(__file__).resolve().parents[1]


def _current_frontier_label() -> str:
    verifier = (ROOT / "scripts" / "verify_repository.py").read_text(encoding="utf-8")
    match = re.search(r'^CURRENT_FRONTIER = "(P\\d+)"$', verifier, flags=re.MULTILINE)
    if match is None:
        raise RuntimeError("could not determine current Research II frontier")
    return match.group(1)


CURRENT_FRONTIER_LABEL = _current_frontier_label()
CURRENT_HOME_MARKER = f"<!-- current-frontier-home: {CURRENT_FRONTIER_LABEL} -->"'''
    text = replace_one_of(path, text, old, new)
    write(path, text)


def repair_prepare_website() -> None:
    path = "scripts/prepare_website.py"
    text = read(path)

    if "import json\n" not in text:
        text = text.replace("import argparse\n", "import argparse\nimport json\n", 1)

    old_constants = '''CURRENT_FRONTIER_FIGURE = (
    "p94_finite_range_dependent_sign_coherence.svg"
)
CURRENT_RECORD_TEXT = "Current record:</strong> 94 proposition-level results through P94"'''
    if old_constants not in text:
        old_constants = '''CURRENT_FRONTIER_FIGURE = (
    "p93_localized_sign_coherence_rejection.svg"
)
CURRENT_RECORD_TEXT = "Current record:</strong> 93 proposition-level results through P93"'''
    new_constants = '''FIGURE_MANIFEST = ROOT / "figures" / "manifest.json"
_FRONTIER_MANIFEST = json.loads(FIGURE_MANIFEST.read_text(encoding="utf-8"))
CURRENT_FRONTIER_LABEL = str(_FRONTIER_MANIFEST["current_frontier"])
CURRENT_FRONTIER = int(CURRENT_FRONTIER_LABEL.removeprefix("P"))
CURRENT_FRONTIER_FIGURE = Path(str(_FRONTIER_MANIFEST["current_frontier_figure"])).name
CURRENT_RECORD_TEXT = (
    f"Current record:</strong> {CURRENT_FRONTIER} proposition-level results "
    f"through P{CURRENT_FRONTIER}"
)'''
    text = replace_one_of(path, text, old_constants, new_constants)

    replacements = (
        (
            '    """Require the deployed site to be internally consistent with P93."""',
            '    """Require the deployed site to match the declared current frontier."""',
        ),
        (
            '            "website build is missing the current P93 theorem figure: "',
            '            "website build is missing the current theorem figure: "',
        ),
        (
            '        raise RuntimeError("Visual Atlas does not use the bundled P93 theorem figure")',
            '        raise RuntimeError("Visual Atlas does not use the bundled current theorem figure")',
        ),
        (
            '    _require_once(visual_atlas, \'id="p93-frontier"\', "Visual Atlas")',
            '    _require_once(visual_atlas, f\'id="p{CURRENT_FRONTIER}-frontier"\', "Visual Atlas")',
        ),
        (
            '        raise RuntimeError("Homepage does not use the bundled P93 theorem figure")',
            '        raise RuntimeError("Homepage does not use the bundled current theorem figure")',
        ),
        (
            '        raise RuntimeError("Homepage Project at a glance is not synchronized to 93/P93")',
            '        raise RuntimeError("Homepage Project at a glance is not synchronized to the current frontier")',
        ),
        (
            '    _require_once(homepage, \'id="p93-frontier"\', "Homepage")',
            '    _require_once(homepage, f\'id="p{CURRENT_FRONTIER}-frontier"\', "Homepage")',
        ),
        (
            '        "<strong>93</strong><span>proposition-level results</span>",',
            '        f"<strong>{CURRENT_FRONTIER}</strong><span>proposition-level results</span>",',
        ),
        (
            '        "<strong>P93</strong><span>current theorem frontier</span>",',
            '        f"<strong>P{CURRENT_FRONTIER}</strong><span>current theorem frontier</span>",',
        ),
        (
            '        "prepared website with Research II P93 and Research III "',
            '        f"prepared website with Research II P{CURRENT_FRONTIER} and Research III "',
        ),
    )
    for old, new in replacements:
        text = replace_one_of(path, text, old, new)

    # The current promotion may already have P94-specific variants. Convert them too.
    text = text.replace(
        '    _require_once(visual_atlas, \'id="p94-frontier"\', "Visual Atlas")',
        '    _require_once(visual_atlas, f\'id="p{CURRENT_FRONTIER}-frontier"\', "Visual Atlas")',
    )
    text = text.replace(
        '    _require_once(homepage, \'id="p94-frontier"\', "Homepage")',
        '    _require_once(homepage, f\'id="p{CURRENT_FRONTIER}-frontier"\', "Homepage")',
    )
    text = text.replace(
        '        "<strong>94</strong><span>proposition-level results</span>",',
        '        f"<strong>{CURRENT_FRONTIER}</strong><span>proposition-level results</span>",',
    )
    text = text.replace(
        '        "<strong>P94</strong><span>current theorem frontier</span>",',
        '        f"<strong>P{CURRENT_FRONTIER}</strong><span>current theorem frontier</span>",',
    )
    text = text.replace(
        '        "prepared website with Research II P94 and Research III "',
        '        f"prepared website with Research II P{CURRENT_FRONTIER} and Research III "',
    )
    write(path, text)


def verify_finalizer_state() -> None:
    verifier = read("scripts/verify_repository.py")
    if 'CURRENT_FRONTIER = "P94"' not in verifier:
        raise RuntimeError("repository verifier is not promoted to P94")
    if "range(1, 94)" in verifier:
        raise RuntimeError("repository verifier still hard-codes P93 proposition coverage")

    syncer = read("scripts/synchronize_research_three_website.py")
    if 'CURRENT_HOME_MARKER = "<!-- current-frontier-home: P93 -->"' in syncer:
        raise RuntimeError("Research III synchronizer still hard-codes the P93 homepage marker")

    prepare = read("scripts/prepare_website.py")
    for stale in (
        'id="p93-frontier"',
        '"<strong>93</strong><span>proposition-level results</span>"',
        '"<strong>P93</strong><span>current theorem frontier</span>"',
    ):
        if stale in prepare:
            raise RuntimeError(f"website builder still contains stale frontier contract: {stale}")


def main() -> None:
    repair_formal_provenance()
    repair_homepage()
    repair_website_research_map()
    repair_repository_verifier()
    repair_research_three_syncer()
    repair_prepare_website()
    repair_reader_contracts()
    verify_finalizer_state()
    print("[P94] publication finalizer applied")


if __name__ == "__main__":
    main()
