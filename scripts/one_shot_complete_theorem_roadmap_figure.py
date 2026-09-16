from __future__ import annotations

import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs" / "figures" / "theorem_roadmap.svg"
RECORDS = ROOT / "scripts" / "conceptual_figure_records.py"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"
RESEARCH_MAP = ROOT / "website" / "research-map.html"
TEST = ROOT / "tests" / "test_theorem_roadmap_caption.py"

RAW_FIGURE = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/theorem_roadmap.svg"
)
GITHUB_FIGURE = (
    "https://github.com/MahsaKeikha/mathematical-consciousness-bridge/"
    "blob/main/docs/figures/theorem_roadmap.svg"
)
GITHUB_ROADMAP = (
    "https://github.com/MahsaKeikha/mathematical-consciousness-bridge/"
    "blob/main/docs/theorem_roadmap.md"
)

TITLE = "Complete theorem dependency map for P1-P100"
DESCRIPTION = (
    "What this figure shows: the complete theorem roadmap for Propositions 1 through 100. "
    "Every proposition P1 through P100 appears explicitly. Solid arrows show the primary "
    "bridge-sufficiency lineage from foundations through P19-P24 and then P71-P100. "
    "Dashed connectors show connected physical, quantum, evidence-acquisition, scheduling, "
    "and calibration branches P25-P70; they do not assert that every proposition in one "
    "block is a prerequisite for every proposition in the next. How to read it: follow the "
    "lane labels and connectors rather than proposition number alone. P71-P100 returns to "
    "the P19 bridge-sufficiency lineage and does not extend the P61-P70 calibration branch. "
    "Main takeaway: proposition numbering records development order, while the roadmap "
    "separates the core bridge lineage from connected machinery branches and marks P100 as "
    "the current theorem frontier."
)
STATUS = (
    "Research-orientation figure. It summarizes documented dependency structure across "
    "P1-P100; it does not add a theorem, empirical consciousness result, or "
    "physical-to-experiential bridge claim."
)


def chips(numbers: range, x: int, y: int, width: int, cols: int) -> str:
    lines: list[str] = []
    for index, number in enumerate(numbers):
        row = index // cols
        col = index % cols
        cx = x + 24 + col * 66
        cy = y + 112 + row * 42
        class_name = "chip current" if number == 100 else "chip"
        lines.append(
            f'    <g class="{class_name}" data-proposition="P{number}">'
            f'<rect x="{cx}" y="{cy}" width="56" height="30" rx="8"/>'
            f'<text x="{cx + 28}" y="{cy + 20}" class="chipText" '
            f'text-anchor="middle">P{number}</text></g>'
        )
    return "\n".join(lines)


def box(
    x: int,
    y: int,
    width: int,
    height: int,
    label: str,
    title: str,
    description: str,
    numbers: range,
    fill: str,
    stroke: str,
    cols: int,
) -> str:
    return "\n".join(
        [
            '  <g class="group-box">',
            (
                f'    <rect x="{x}" y="{y}" width="{width}" height="{height}" '
                f'rx="18" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>'
            ),
            f'    <text x="{x + 28}" y="{y + 34}" class="label">{escape(label)}</text>',
            f'    <text x="{x + 28}" y="{y + 69}" class="head">{escape(title)}</text>',
            (
                f'    <text x="{x + 28}" y="{y + 96}" class="body">'
                f'{escape(description)}</text>'
            ),
            chips(numbers, x, y, width, cols),
            "  </g>",
        ]
    )


def build_svg() -> str:
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="2800" '
        'viewBox="0 0 1600 2800" role="img" aria-labelledby="title desc">',
        f'  <title id="title">{escape(TITLE)}</title>',
        f'  <desc id="desc">{escape(DESCRIPTION + " Scientific status: " + STATUS)}</desc>',
        "  <defs>",
        '    <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="4" orient="auto">',
        '      <path d="M0 0 L0 8 L10 4 z" fill="#64748b"/>',
        "    </marker>",
        "    <style>",
        "      .title{font:700 38px Inter,Segoe UI,Arial,sans-serif;fill:#0f172a}",
        "      .subtitle{font:400 17px Inter,Segoe UI,Arial,sans-serif;fill:#475569}",
        "      .lane{font:700 12px Inter,Segoe UI,Arial,sans-serif;letter-spacing:1.2px;fill:#334155}",
        "      .label{font:700 10px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.8px;fill:#64748b}",
        "      .head{font:700 17px Inter,Segoe UI,Arial,sans-serif;fill:#0f172a}",
        "      .body{font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#475569}",
        "      .eq{font:600 15px Georgia,'Times New Roman',serif;fill:#0f172a}",
        "      .chip rect{fill:#ffffff;stroke:#cbd5e1;stroke-width:1}",
        "      .chipText{font:700 11px Inter,Segoe UI,Arial,sans-serif;fill:#334155}",
        "      .current rect{fill:#ecfdf5;stroke:#059669;stroke-width:2}",
        "      .current .chipText{fill:#047857}",
        "      .arrow{stroke:#475569;stroke-width:2.4;fill:none;marker-end:url(#arrow)}",
        "      .branch{stroke:#94a3b8;stroke-width:2.2;stroke-dasharray:8 8;fill:none;marker-end:url(#arrow)}",
        "      .legend{font:400 13px Inter,Segoe UI,Arial,sans-serif;fill:#475569}",
        "    </style>",
        "  </defs>",
        '  <rect width="1600" height="2800" fill="#ffffff"/>',
        '  <text x="70" y="62" class="title">Complete Theorem Roadmap - P1 through P100</text>',
        (
            '  <text x="70" y="94" class="subtitle">All 100 proposition nodes are shown. '
            "Solid arrows mark the core bridge lineage; dashed connectors mark connected branches.</text>"
        ),
    ]

    opening = (
        (95, 145, 420, 180, "FOUNDATION | P1-P4", "Invariance and identifiability", "Representation, equivalence, design", range(1, 5), "#eff6ff", "#3b82f6", 5),
        (590, 145, 420, 180, "FOUNDATION | P5-P10", "Recovery and finite data", "Recovery, sample complexity, robust design", range(5, 11), "#faf5ff", "#8b5cf6", 6),
        (1085, 145, 420, 180, "PHYSICS | P11-P13", "Intervention-resolved structure", "Causal response and irredundancy tests", range(11, 14), "#ecfdf5", "#10b981", 5),
        (95, 410, 420, 180, "TIME | P14-P15", "Temporal continuation", "Temporal geometry and certification", range(14, 16), "#fff7ed", "#f97316", 5),
        (590, 410, 420, 180, "COMPOSITION | P16", "Independent systems and coupling", "Product structure and coupling", range(16, 17), "#f0fdfa", "#14b8a6", 5),
        (1085, 410, 420, 180, "SCALE | P17-P18", "Loss and recoverable sufficiency", "Coarse loss and reconstruction control", range(17, 19), "#fff1f2", "#e11d48", 5),
    )
    for spec in opening:
        parts.append(box(*spec))

    parts.extend(
        [
            '  <path class="arrow" d="M515 235 H578"/>',
            '  <path class="arrow" d="M1010 235 H1073"/>',
            '  <path class="arrow" d="M1295 325 V360 H305 V398"/>',
            '  <path class="arrow" d="M515 500 H578"/>',
            '  <path class="arrow" d="M1010 500 H1073"/>',
            '  <text x="90" y="658" class="lane">CORE BRIDGE-SUFFICIENCY LINEAGE</text>',
            '  <text x="1030" y="658" class="lane">CONNECTED PHYSICAL / EXPERIMENTAL BRANCHES</text>',
        ]
    )

    core = (
        (90, 700, 880, 250, "CORE | P19-P24", "Physical sufficiency and adaptive validity", "P19 screening-off; P20-P24 finite data, refinement, selection, repeated looks", range(19, 25), "#f8fafc", "#0f172a", 10),
        (90, 1030, 880, 250, "CORE | P71-P76", "Target provenance, measurement, and adequacy", "Independent target provenance, channel robustness, recovery, model adequacy", range(71, 77), "#eef2ff", "#4f46e5", 10),
        (90, 1360, 880, 300, "CORE | P77-P89", "Certified continuous-family model separation", "Full-law rejection, global bounds, parity constraints, complete linear duality", range(77, 90), "#f5f3ff", "#7c3aed", 10),
        (90, 1740, 880, 250, "CORE | P90-P95", "Nonlinear geometry and finite-sample rejection", "Rank constraints, exact distance, IID and dependent rejection, drift-aware gates", range(90, 96), "#fff7ed", "#ea580c", 10),
        (90, 2070, 880, 250, "CORE | P96-P100", "Selection-valid and anytime-valid inference", "Holdout, candidate selection, cross-fitting, e-values, sequential stopping", range(96, 101), "#ecfdf5", "#059669", 10),
    )
    for spec in core:
        parts.append(box(*spec))

    side = (
        (1030, 700, 480, 300, "BRANCH | P25-P37", "Operational scale and quotient compatibility", "Scale transport, aggregation, metrics, quotients", range(25, 38), "#f0fdfa", "#0d9488", 6),
        (1030, 1080, 480, 250, "BRANCH | P38-P44", "Quantum operational interface", "Operational sufficiency and quantum regularity tests", range(38, 45), "#eff6ff", "#2563eb", 6),
        (1030, 1410, 480, 260, "BRANCH | P45-P53", "Adaptive evidence acquisition", "Witness graphs, allocation, starvation, stopping", range(45, 54), "#fff7ed", "#f59e0b", 6),
        (1030, 1750, 480, 250, "BRANCH | P54-P60", "Scheduling and calibration setup", "Routing, reoptimization, uncertainty, calibration", range(54, 61), "#fdf2f8", "#db2777", 6),
        (1030, 2080, 480, 260, "BRANCH | P61-P70", "Exact calibration and optimization", "Integer allocation, costs, approximation, dual gaps", range(61, 71), "#faf5ff", "#9333ea", 6),
    )
    for spec in side:
        parts.append(box(*spec))

    parts.extend(
        [
            '  <path class="arrow" d="M1295 590 V640 H530 V688"/>',
            '  <path class="branch" d="M1295 590 V640 H1270 V688"/>',
            '  <path class="arrow" d="M530 950 V1018"/>',
            '  <path class="arrow" d="M530 1280 V1348"/>',
            '  <path class="arrow" d="M530 1660 V1728"/>',
            '  <path class="arrow" d="M530 1990 V2058"/>',
            '  <path class="branch" d="M1270 1000 V1068"/>',
            '  <path class="branch" d="M1270 1330 V1398"/>',
            '  <path class="branch" d="M1270 1670 V1738"/>',
            '  <path class="branch" d="M1270 2000 V2068"/>',
            '  <rect x="90" y="2390" width="1420" height="300" rx="20" fill="#f8fafc" stroke="#cbd5e1"/>',
            '  <text x="125" y="2432" class="head">How to read this complete roadmap</text>',
            '  <path class="arrow" d="M130 2476 H235"/>',
            '  <text x="255" y="2481" class="legend">Solid arrows: primary bridge-sufficiency lineage summarized in the theorem roadmap.</text>',
            '  <path class="branch" d="M130 2522 H235"/>',
            '  <text x="255" y="2527" class="legend">Dashed connectors: connected branch handoffs, not universal pairwise prerequisites.</text>',
            '  <text x="125" y="2580" class="legend">P71-P100 returns to the P19 bridge lineage. It does not extend the P61-P70 calibration branch.</text>',
            '  <text x="125" y="2620" class="legend">Every proposition P1 through P100 is explicitly represented above; P100 is the current documented theorem frontier.</text>',
            '  <text x="125" y="2660" class="legend">This figure summarizes dependency structure only; it does not close the physical-to-experiential bridge.</text>',
            "</svg>",
        ]
    )
    svg = "\n".join(parts) + "\n"
    nodes = sorted(int(value) for value in re.findall(r'data-proposition="P(\d+)"', svg))
    if nodes != list(range(1, 101)):
        raise RuntimeError(f"roadmap SVG does not contain exact P1-P100 node coverage: {nodes}")
    if "\u2013" in svg or "\u2014" in svg:
        raise RuntimeError("roadmap SVG violates repository dash policy")
    return svg


def update_record() -> None:
    text = RECORDS.read_text(encoding="utf-8")
    pattern = re.compile(
        r'    "docs/figures/theorem_roadmap\.svg": \{.*?\n    \},\n'
        r'(?=    "docs/figures/fundamental_theory_consciousness_map\.svg": \{)',
        flags=re.DOTALL,
    )
    replacement = f'''    "docs/figures/theorem_roadmap.svg": {{
        "title": {TITLE!r},
        "description": (
            {DESCRIPTION!r}
        ),
        "status": (
            {STATUS!r}
        ),
    }},
'''
    updated, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f"expected one theorem-roadmap metadata record, found {count}")
    RECORDS.write_text(updated, encoding="utf-8")


def update_visual_atlas() -> None:
    text = VISUAL_ATLAS.read_text(encoding="utf-8")
    pattern = re.compile(
        r'<div class="figure-card"><img loading="lazy" decoding="async" '
        r'src="https://raw\.githubusercontent\.com/MahsaKeikha/'
        r'mathematical-consciousness-bridge/main/docs/figures/theorem_roadmap\.svg" '
        r'alt="Theorem roadmap"/><div><h3>Theorem roadmap</h3><p>.*?</p>'
        r'<a href="https://github\.com/MahsaKeikha/mathematical-consciousness-bridge/'
        r'blob/main/docs/theorem_roadmap\.md">Full roadmap .*?</a></div></div>',
        flags=re.DOTALL,
    )
    replacement = (
        '<div class="figure-card"><img loading="lazy" decoding="async" '
        f'src="{RAW_FIGURE}" alt="Complete theorem roadmap P1-P100"/>'
        '<div><h3>Complete theorem roadmap: P1-P100</h3>'
        '<p>Every proposition P1 through P100 is visible in this canonical figure. '
        'Solid arrows mark the core bridge-sufficiency lineage, while dashed connectors '
        'keep P25-P70 as connected physical, quantum, evidence, and calibration branches '
        'instead of implying that P71-P100 descends from the calibration branch.</p>'
        f'<a href="{GITHUB_FIGURE}">Open full-resolution figure</a> | '
        f'<a href="{GITHUB_ROADMAP}">Full roadmap</a></div></div>'
    )
    updated, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f"expected one theorem-roadmap Visual Atlas card, found {count}")
    VISUAL_ATLAS.write_text(updated, encoding="utf-8")


def update_research_map() -> None:
    text = RESEARCH_MAP.read_text(encoding="utf-8")
    start = "<!-- BEGIN COMPLETE THEOREM ROADMAP FIGURE -->"
    end = "<!-- END COMPLETE THEOREM ROADMAP FIGURE -->"
    section = f'''{start}
<section id="complete-theorem-roadmap-figure" class="theorem-frontier">
  <div class="section-head">
    <p class="eyebrow">Complete visual dependency map</p>
    <h2>Complete theorem roadmap: P1-P100</h2>
    <p>Every proposition from P1 through P100 appears as an individual labeled node in the same canonical roadmap figure used by the repository. The core P1-P24 to P71-P100 bridge lineage is visually separated from the connected P25-P70 physical, quantum, evidence, scheduling, and calibration branches.</p>
  </div>
  <div class="theorem-figure-shell">
    <a href="{GITHUB_FIGURE}"><img loading="eager" decoding="async" src="{RAW_FIGURE}" alt="Complete theorem roadmap P1-P100" /></a>
  </div>
  <p><strong>Reading rule:</strong> solid arrows mark the primary bridge-sufficiency lineage. Dashed connectors mark connected branch handoffs and do not assert universal pairwise prerequisites. P71-P100 returns to the P19 lineage rather than extending P61-P70.</p>
  <p><a href="{GITHUB_ROADMAP}">Open the complete theorem roadmap and proposition index</a></p>
</section>
{end}'''
    if start in text:
        pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), flags=re.DOTALL)
        text, count = pattern.subn(section, text, count=1)
        if count != 1:
            raise RuntimeError("could not replace existing complete roadmap website section")
    else:
        marker = '<section id="program-stages">'
        if text.count(marker) != 1:
            raise RuntimeError("could not locate unique program-stages insertion point")
        text = text.replace(marker, section + "\n\n" + marker, 1)
    RESEARCH_MAP.write_text(text, encoding="utf-8")


def update_test() -> None:
    TEST.write_text(
        '''import json\nimport re\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nFIGURE = ROOT / "docs" / "figures" / "theorem_roadmap.svg"\nCATALOG = ROOT / "docs" / "figure_catalog.md"\nMANIFEST = ROOT / "figures" / "manifest.json"\nVISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"\nRESEARCH_MAP = ROOT / "website" / "research-map.html"\n\n\ndef _frontier() -> int:\n    numbers: list[int] = []\n    for path in (ROOT / "docs").glob("proposition_*_*.md"):\n        match = re.match(r"proposition_(\\d+)_", path.name)\n        if match:\n            numbers.append(int(match.group(1)))\n    assert numbers\n    return max(numbers)\n\n\ndef test_theorem_roadmap_figure_has_exact_p1_through_current_frontier_nodes():\n    text = FIGURE.read_text(encoding="utf-8")\n    frontier = _frontier()\n    nodes = sorted(int(value) for value in re.findall(r'data-proposition="P(\\d+)"', text))\n    assert frontier == 100\n    assert nodes == list(range(1, frontier + 1))\n    assert len(nodes) == len(set(nodes)) == 100\n    assert "Complete theorem dependency map for P1-P100" in text\n    assert "Every proposition P1 through P100 appears explicitly" in text\n    assert "P71-P100 returns to the P19 bridge-sufficiency lineage" in text\n    assert 'class="chip current" data-proposition="P100"' in text\n    assert "P1-P31" not in text\n\n\ndef test_figure_catalog_and_manifest_publish_complete_roadmap_metadata():\n    catalog = CATALOG.read_text(encoding="utf-8")\n    assert "Complete theorem dependency map for P1-P100" in catalog\n    assert "complete theorem roadmap for Propositions 1 through 100" in catalog\n    assert "P1-P31" not in catalog\n\n    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))\n    record = next(\n        item\n        for item in manifest["figures"]\n        if item["path"] == "docs/figures/theorem_roadmap.svg"\n    )\n    assert record["title"] == "Complete theorem dependency map for P1-P100"\n    assert record["bytes"] == FIGURE.stat().st_size\n\n\ndef test_repository_and_website_use_the_same_complete_p1_p100_roadmap():\n    atlas = VISUAL_ATLAS.read_text(encoding="utf-8")\n    research = RESEARCH_MAP.read_text(encoding="utf-8")\n    for page in (atlas, research):\n        assert "theorem_roadmap.svg" in page\n        assert "Complete theorem roadmap: P1-P100" in page\n        assert "Complete theorem roadmap P1-P100" in page\n    assert 'id="complete-theorem-roadmap-figure"' in research\n    assert "Every proposition from P1 through P100 appears as an individual labeled node" in research\n''',
        encoding="utf-8",
    )


def main() -> None:
    FIGURE.write_text(build_svg(), encoding="utf-8")
    update_record()
    update_visual_atlas()
    update_research_map()
    update_test()


if __name__ == "__main__":
    main()
