"""Prepare the static research website for GitHub Pages deployment.

The repository keeps page content as plain HTML files. This build step copies the
website into a deployment directory, injects shared publication assets, and
bundles the canonical ``docs/figures`` tree into the same Pages artifact. Image
``src`` URLs that point at raw GitHub ``main`` figures are rewritten to the local
artifact copy, so the HTML and SVGs shown by one deployment come from the exact
same checked-out commit.
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_FIGURES = ROOT / "docs" / "figures"
RAW_FIGURE_PREFIX = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/"
)
CURRENT_FRONTIER_FIGURE = "p86_exact_minimally_weighted_quad_projection_parity.svg"

ASSET_VERSION = "20260912-nav14-reader"
SCRIPT_TAG = f'<script defer src="app.js?v={ASSET_VERSION}"></script>'
READER_LINKS_SCRIPT_TAG = '<script defer src="reader-links.js"></script>'
FOOTER_SCRIPT_TAG = '<script defer src="footer.js"></script>'
NAVIGATION_STYLE_TAG = '<link rel="stylesheet" href="navigation.css" />'
NAVIGATION_V2_STYLE_TAG = (
    f'<link rel="stylesheet" href="navigation-v2.css?v={ASSET_VERSION}" />'
)
PUBLICATION_STYLE_TAG = '<link rel="stylesheet" href="publication.css" />'
PUBLICATION_V2_STYLE_TAG = '<link rel="stylesheet" href="publication-v2.css" />'
RESEARCH_GUIDE_STYLE_TAG = (
    f'<link rel="stylesheet" href="research-guide-v2.css?v={ASSET_VERSION}" />'
)
CONTRAST_STYLE_TAG = (
    f'<link rel="stylesheet" href="contrast-v2.css?v={ASSET_VERSION}" />'
)
READER_EXPERIENCE_STYLE_TAG = (
    f'<link rel="stylesheet" href="reader-experience-v2.css?v={ASSET_VERSION}" />'
)

APP_SCRIPT_PATTERN = re.compile(
    r'<script\s+defer\s+src="app\.js(?:\?v=[^"]+)?"></script>'
)
NAVIGATION_V2_STYLE_PATTERN = re.compile(
    r'<link\s+rel="stylesheet"\s+href="navigation-v2\.css(?:\?v=[^"]+)?"\s*/?>'
)
RESEARCH_GUIDE_STYLE_PATTERN = re.compile(
    r'<link\s+rel="stylesheet"\s+href="research-guide-v2\.css(?:\?v=[^"]+)?"\s*/?>'
)
CONTRAST_STYLE_PATTERN = re.compile(
    r'<link\s+rel="stylesheet"\s+href="contrast-v2\.css(?:\?v=[^"]+)?"\s*/?>'
)
READER_EXPERIENCE_STYLE_PATTERN = re.compile(
    r'<link\s+rel="stylesheet"\s+href="reader-experience-v2\.css(?:\?v=[^"]+)?"\s*/?>'
)
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
    '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge">GitHub ↗</a>'
)


def _normalize_navigation_assets(text: str) -> str:
    """Replace stale shared asset URLs with cache-busted canonical URLs."""

    text = APP_SCRIPT_PATTERN.sub(SCRIPT_TAG, text)
    text = NAVIGATION_V2_STYLE_PATTERN.sub(NAVIGATION_V2_STYLE_TAG, text)
    text = RESEARCH_GUIDE_STYLE_PATTERN.sub(RESEARCH_GUIDE_STYLE_TAG, text)
    text = CONTRAST_STYLE_PATTERN.sub(CONTRAST_STYLE_TAG, text)
    text = READER_EXPERIENCE_STYLE_PATTERN.sub(READER_EXPERIENCE_STYLE_TAG, text)
    return text


def _normalize_topbar_fallback(text: str) -> str:
    """Keep the no-JavaScript fallback compact instead of exposing the old flat bar."""

    return TOPBAR_NAV_PATTERN.sub(
        lambda match: f"{match.group(1)}{FALLBACK_NAV}{match.group(2)}",
        text,
        count=1,
    )


def _localize_figure_sources(text: str) -> str:
    """Use the exact-commit figure copies bundled into the Pages artifact."""

    return text.replace(f'src="{RAW_FIGURE_PREFIX}', 'src="figures/')


def _copy_canonical_figures(output: Path) -> None:
    if not CANONICAL_FIGURES.is_dir():
        raise FileNotFoundError(
            f"canonical figure directory not found: {CANONICAL_FIGURES}"
        )
    shutil.copytree(CANONICAL_FIGURES, output / "figures", dirs_exist_ok=True)


def prepare_website(source: Path, output: Path) -> None:
    """Copy ``source`` and the canonical figures into one auditable Pages build."""

    if not source.is_dir():
        raise FileNotFoundError(f"website source directory not found: {source}")

    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(source, output)
    _copy_canonical_figures(output)

    html_files = sorted(output.glob("*.html"))
    if not html_files:
        raise RuntimeError("website build contains no HTML pages")

    for path in html_files:
        text = path.read_text(encoding="utf-8")
        if "</head>" not in text:
            raise RuntimeError(f"missing </head> in {path}")

        text = _normalize_navigation_assets(text)
        text = _normalize_topbar_fallback(text)
        text = _localize_figure_sources(text)

        additions: list[str] = []
        if NAVIGATION_STYLE_TAG not in text:
            additions.append(NAVIGATION_STYLE_TAG)
        if NAVIGATION_V2_STYLE_TAG not in text:
            additions.append(NAVIGATION_V2_STYLE_TAG)
        if PUBLICATION_STYLE_TAG not in text:
            additions.append(PUBLICATION_STYLE_TAG)
        if PUBLICATION_V2_STYLE_TAG not in text:
            additions.append(PUBLICATION_V2_STYLE_TAG)
        if RESEARCH_GUIDE_STYLE_TAG not in text:
            additions.append(RESEARCH_GUIDE_STYLE_TAG)
        if CONTRAST_STYLE_TAG not in text:
            additions.append(CONTRAST_STYLE_TAG)
        if READER_EXPERIENCE_STYLE_TAG not in text:
            additions.append(READER_EXPERIENCE_STYLE_TAG)
        if SCRIPT_TAG not in text:
            additions.append(SCRIPT_TAG)
        if READER_LINKS_SCRIPT_TAG not in text:
            additions.append(READER_LINKS_SCRIPT_TAG)
        if FOOTER_SCRIPT_TAG not in text:
            additions.append(FOOTER_SCRIPT_TAG)
        if additions:
            text = text.replace("</head>", "".join(additions) + "</head>", 1)
        path.write_text(text, encoding="utf-8")

    required_assets = (
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
    for asset in required_assets:
        if not (output / asset).is_file():
            raise RuntimeError(f"website build is missing {asset}")

    visual_atlas_path = output / "visual-atlas.html"
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("website"))
    parser.add_argument("--output", type=Path, default=Path("_site"))
    args = parser.parse_args()
    prepare_website(args.source, args.output)
    print(f"prepared website with exact-commit figures: {args.output}")


if __name__ == "__main__":
    main()
