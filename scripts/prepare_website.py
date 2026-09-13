"""Prepare the static research website for GitHub Pages.

The source HTML intentionally stays simple and readable. The deployed site needs
additional shared navigation/publication styles and scripts used by ``app.js``.
This build step injects those assets into every page, bundles the exact-commit
figure tree, localizes figure URLs, and validates the reader-first P1-P87 public
state before GitHub Pages publishes it.
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_WEBSITE = ROOT / "website"
CANONICAL_FIGURES = ROOT / "docs" / "figures"
RAW_FIGURE_PREFIX = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/"
)
CURRENT_FRONTIER_FIGURE = "p87_exact_bounded_primitive_quad_projection_parity.svg"

ASSET_VERSION = "20260913-live-repair1"
SCRIPT_TAG = f'<script defer src="app.js?v={ASSET_VERSION}"></script>'
READER_LINKS_SCRIPT_TAG = '<script defer src="reader-links.js"></script>'
FOOTER_SCRIPT_TAG = '<script defer src="footer.js"></script>'
BASE_STYLE_TAG = f'<link rel="stylesheet" href="styles.css?v={ASSET_VERSION}" />'
NAVIGATION_STYLE_TAG = '<link rel="stylesheet" href="navigation.css" />'
NAVIGATION_V2_STYLE_TAG = f'<link rel="stylesheet" href="navigation-v2.css?v={ASSET_VERSION}" />'
PUBLICATION_STYLE_TAG = '<link rel="stylesheet" href="publication.css" />'
PUBLICATION_V2_STYLE_TAG = '<link rel="stylesheet" href="publication-v2.css" />'
RESEARCH_GUIDE_STYLE_TAG = f'<link rel="stylesheet" href="research-guide-v2.css?v={ASSET_VERSION}" />'
CONTRAST_STYLE_TAG = f'<link rel="stylesheet" href="contrast-v2.css?v={ASSET_VERSION}" />'
READER_EXPERIENCE_STYLE_TAG = f'<link rel="stylesheet" href="reader-experience-v2.css?v={ASSET_VERSION}" />'

APP_SCRIPT_PATTERN = re.compile(r'<script\s+defer\s+src="app\.js(?:\?v=[^"]+)?"></script>')
BASE_STYLE_PATTERN = re.compile(r'<link\s+rel="stylesheet"\s+href="styles\.css(?:\?v=[^"]+)?"\s*/?>')
NAVIGATION_V2_STYLE_PATTERN = re.compile(r'<link\s+rel="stylesheet"\s+href="navigation-v2\.css(?:\?v=[^"]+)?"\s*/?>')
RESEARCH_GUIDE_STYLE_PATTERN = re.compile(r'<link\s+rel="stylesheet"\s+href="research-guide-v2\.css(?:\?v=[^"]+)?"\s*/?>')
CONTRAST_STYLE_PATTERN = re.compile(r'<link\s+rel="stylesheet"\s+href="contrast-v2\.css(?:\?v=[^"]+)?"\s*/?>')
READER_EXPERIENCE_STYLE_PATTERN = re.compile(r'<link\s+rel="stylesheet"\s+href="reader-experience-v2\.css(?:\?v=[^"]+)?"\s*/?>')
TOPBAR_NAV_PATTERN = re.compile(
    r'(<header\s+class="topbar">.*?<nav(?:\s[^>]*)?>).*?(</nav>)',
    flags=re.DOTALL,
)

FALLBACK_NAV = (
    '<a href="index.html">Overview</a>'
    '<a href="plain-language.html">Plain Language</a>'
    '<a href="start-here.html">Start Here</a>'
    '<a href="research-map.html">Research</a>'
    '<a href="visual-atlas.html">Explore</a>'
    '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge">GitHub</a>'
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

INJECTED_ASSET_TAGS = (
    BASE_STYLE_TAG,
    NAVIGATION_STYLE_TAG,
    NAVIGATION_V2_STYLE_TAG,
    PUBLICATION_STYLE_TAG,
    PUBLICATION_V2_STYLE_TAG,
    RESEARCH_GUIDE_STYLE_TAG,
    CONTRAST_STYLE_TAG,
    READER_EXPERIENCE_STYLE_TAG,
    SCRIPT_TAG,
    READER_LINKS_SCRIPT_TAG,
    FOOTER_SCRIPT_TAG,
)

REQUIRED_ASSETS = (
    "app.js",
    "reader-links.js",
    "footer.js",
    "styles.css",
    "navigation.css",
    "navigation-v2.css",
    "publication.css",
    "publication-v2.css",
    "research-guide-v2.css",
    "contrast-v2.css",
    "reader-experience-v2.css",
)


def _normalize_assets(text: str) -> str:
    text = APP_SCRIPT_PATTERN.sub(SCRIPT_TAG, text)
    text = BASE_STYLE_PATTERN.sub(BASE_STYLE_TAG, text)
    text = NAVIGATION_V2_STYLE_PATTERN.sub(NAVIGATION_V2_STYLE_TAG, text)
    text = RESEARCH_GUIDE_STYLE_PATTERN.sub(RESEARCH_GUIDE_STYLE_TAG, text)
    text = CONTRAST_STYLE_PATTERN.sub(CONTRAST_STYLE_TAG, text)
    text = READER_EXPERIENCE_STYLE_PATTERN.sub(READER_EXPERIENCE_STYLE_TAG, text)
    return text


def _normalize_topbar_fallback(text: str) -> str:
    return TOPBAR_NAV_PATTERN.sub(
        lambda match: f"{match.group(1)}{FALLBACK_NAV}{match.group(2)}",
        text,
        count=1,
    )


def _localize_figure_sources(text: str) -> str:
    return text.replace(f'src="{RAW_FIGURE_PREFIX}', 'src="figures/')


def _assert_order(text: str, values: tuple[str, ...], page: str) -> None:
    positions = []
    for value in values:
        position = text.find(value)
        if position < 0:
            raise RuntimeError(f"{page} is missing canonical value: {value}")
        positions.append(position)
    if positions != sorted(positions):
        raise RuntimeError(f"{page} has canonical research items out of order")


def _validate_public_state(output: Path) -> None:
    required_pages = (
        "index.html",
        "plain-language.html",
        "start-here.html",
        "research-map.html",
        "research-navigation.html",
        "visual-atlas.html",
        "implementation.html",
    )
    for name in required_pages:
        path = output / name
        if not path.is_file():
            raise RuntimeError(f"website build is missing required public page: {name}")
        text = path.read_text(encoding="utf-8")
        for tag in INJECTED_ASSET_TAGS:
            if tag not in text:
                raise RuntimeError(f"{name} is missing deployed shared asset tag: {tag}")

    for asset in REQUIRED_ASSETS:
        if not (output / asset).is_file():
            raise RuntimeError(f"website build is missing shared asset: {asset}")

    frontier_figure = output / "figures" / CURRENT_FRONTIER_FIGURE
    if not frontier_figure.is_file():
        raise RuntimeError(f"website build is missing P87 theorem figure: {frontier_figure}")

    stale_tokens = (
        "Explore all 86 results",
        "86 proposition-level results",
        "all 86 propositions",
        "Current theorem frontier · P86",
        "Current frontier · P86",
    )
    for path in output.glob("*.html"):
        text = path.read_text(encoding="utf-8")
        stale = [token for token in stale_tokens if token in text]
        if stale:
            raise RuntimeError(f"{path.name} contains stale pre-P87 text: {stale}")

    homepage = (output / "index.html").read_text(encoding="utf-8")
    for token in (
        "Explore all 87 results",
        "P87 is result 87, not result 86",
        "P1-P18",
        "P19-P44",
        "P45-P70",
        "P71-P87",
    ):
        if token not in homepage:
            raise RuntimeError(f"homepage is missing reader-first P87 token: {token}")

    branch_labels = tuple(label for label, _ in CANONICAL_BRANCHES)
    branch_ranges = tuple(result_range for _, result_range in CANONICAL_BRANCHES)
    for name in ("research-map.html", "research-navigation.html"):
        text = (output / name).read_text(encoding="utf-8")
        _assert_order(text, branch_labels, name)
        _assert_order(text, branch_ranges, name)

    atlas = (output / "visual-atlas.html").read_text(encoding="utf-8")
    if "P87 is the 87th public result" not in atlas:
        raise RuntimeError("Visual Atlas does not expose the P87/87-result frontier")

    local_frontier_src = f'src="figures/{CURRENT_FRONTIER_FIGURE}"'
    for name in ("index.html", "visual-atlas.html"):
        text = (output / name).read_text(encoding="utf-8")
        if local_frontier_src not in text:
            raise RuntimeError(f"{name} does not use the bundled P87 theorem figure")
        if f'src="{RAW_FIGURE_PREFIX}' in text:
            raise RuntimeError(f"{name} still depends on mutable raw-GitHub figure URLs")


def prepare_website(source: Path, output: Path) -> None:
    if not source.is_dir():
        raise FileNotFoundError(f"website source directory not found: {source}")
    if not CANONICAL_FIGURES.is_dir():
        raise FileNotFoundError(f"canonical figure directory not found: {CANONICAL_FIGURES}")

    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(source, output)
    shutil.copytree(CANONICAL_FIGURES, output / "figures", dirs_exist_ok=True)

    html_files = sorted(output.glob("*.html"))
    if not html_files:
        raise RuntimeError("website build contains no HTML pages")

    for path in html_files:
        text = path.read_text(encoding="utf-8")
        if "</head>" not in text:
            raise RuntimeError(f"missing </head> in {path}")
        text = _normalize_assets(text)
        text = _normalize_topbar_fallback(text)
        text = _localize_figure_sources(text)
        additions = [tag for tag in INJECTED_ASSET_TAGS if tag not in text]
        if additions:
            text = text.replace("</head>", "".join(additions) + "</head>", 1)
        path.write_text(text, encoding="utf-8")

    _validate_public_state(output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("website"))
    parser.add_argument("--output", type=Path, default=Path("_site"))
    args = parser.parse_args()
    prepare_website(args.source, args.output)
    print(f"prepared styled reader-first P1-P87 website: {args.output}")


if __name__ == "__main__":
    main()
