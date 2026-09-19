"""Prepare the static research website for GitHub Pages deployment.

The website is copied into an auditable deployment directory, canonical figures
from ``docs/figures`` are bundled into that artifact, shared publication assets
are injected consistently, and the deployed reader surfaces are validated
against the current Research II frontier and the completed Research III
foundational framework.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

if __package__:
    from scripts.synchronize_research_three_website import (
        CURRENT_HOME_MARKER,
        CURRENT_RESEARCH_THREE_PIN,
        LEGACY_RESEARCH_THREE_PINS,
        MEASUREMENT_SCIENCE_REQUIRED_MARKERS,
        synchronize_site,
    )
else:
    from synchronize_research_three_website import (
        CURRENT_HOME_MARKER,
        CURRENT_RESEARCH_THREE_PIN,
        LEGACY_RESEARCH_THREE_PINS,
        MEASUREMENT_SCIENCE_REQUIRED_MARKERS,
        synchronize_site,
    )

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_WEBSITE = ROOT / "website"
CANONICAL_FIGURES = ROOT / "docs" / "figures"
RAW_FIGURE_PREFIX = (
    "https://raw.githubusercontent.com/MahsaKeikha/"
    "mathematical-consciousness-bridge/main/docs/figures/"
)
FIGURE_MANIFEST = ROOT / "figures" / "manifest.json"
_FRONTIER_MANIFEST = json.loads(FIGURE_MANIFEST.read_text(encoding="utf-8"))
CURRENT_FRONTIER_LABEL = str(_FRONTIER_MANIFEST["current_frontier"])
CURRENT_FRONTIER = int(CURRENT_FRONTIER_LABEL.removeprefix("P"))
CURRENT_FRONTIER_FIGURE = Path(str(_FRONTIER_MANIFEST["current_frontier_figure"])).name
CURRENT_RECORD_TEXT = (
    f"Current record:</strong> {CURRENT_FRONTIER} proposition-level results "
    f"through P{CURRENT_FRONTIER}"
)
MEASUREMENT_REPO = "https://github.com/MahsaKeikha/consciousness-measurement-science"
MEASUREMENT_PIN = CURRENT_RESEARCH_THREE_PIN
FULL_SITE_SURFACES = (
    "index.html",
    "visual-atlas.html",
    "measurement-science.html",
    "research-lineage.html",
)

ASSET_VERSION = "20260919-r3-publication-visual-system"
SCRIPT_TAG = f'<script defer src="app.js?v={ASSET_VERSION}"></script>'
READER_LINKS_SCRIPT_TAG = '<script defer src="reader-links.js"></script>'
FOOTER_SCRIPT_TAG = '<script defer src="footer.js"></script>'
BASE_STYLE_TAG = f'<link rel="stylesheet" href="styles.css?v={ASSET_VERSION}" />'
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
BASE_STYLE_PATTERN = re.compile(
    r'<link\s+rel="stylesheet"\s+href="styles\.css(?:\?v=[^"]+)?"\s*/?>'
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
    '<a href="measurement-science.html">Research III</a>'
    '<a href="visual-atlas.html">Explore</a>'
    '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge">GitHub</a>'
)


def _is_full_site(site: Path) -> bool:
    """Return whether ``site`` contains every reader surface used by release gates."""

    return all((site / name).is_file() for name in FULL_SITE_SURFACES)


def _normalize_navigation_assets(text: str) -> str:
    """Replace stale shared asset URLs with cache-busted canonical URLs."""

    text = APP_SCRIPT_PATTERN.sub(SCRIPT_TAG, text)
    text = BASE_STYLE_PATTERN.sub(BASE_STYLE_TAG, text)
    text = NAVIGATION_V2_STYLE_PATTERN.sub(NAVIGATION_V2_STYLE_TAG, text)
    text = RESEARCH_GUIDE_STYLE_PATTERN.sub(RESEARCH_GUIDE_STYLE_TAG, text)
    text = CONTRAST_STYLE_PATTERN.sub(CONTRAST_STYLE_TAG, text)
    text = READER_EXPERIENCE_STYLE_PATTERN.sub(READER_EXPERIENCE_STYLE_TAG, text)
    return text


def _normalize_topbar_fallback(text: str) -> str:
    """Keep the no-JavaScript fallback compact and Research III aware."""

    return TOPBAR_NAV_PATTERN.sub(
        lambda match: f"{match.group(1)}{FALLBACK_NAV}{match.group(2)}",
        text,
        count=1,
    )


def _localize_figure_sources(text: str) -> str:
    """Use exact-commit copies of Research II figures bundled into Pages."""

    return text.replace(f'src="{RAW_FIGURE_PREFIX}', 'src="figures/')


def _copy_canonical_figures(output: Path) -> None:
    if not CANONICAL_FIGURES.is_dir():
        raise FileNotFoundError(
            f"canonical figure directory not found: {CANONICAL_FIGURES}"
        )
    shutil.copytree(CANONICAL_FIGURES, output / "figures", dirs_exist_ok=True)


def _require_once(text: str, token: str, surface: str) -> None:
    count = text.count(token)
    if count != 1:
        raise RuntimeError(
            f"{surface} must contain exactly one {token!r}; observed {count}"
        )


def _validate_current_frontier_pages(output: Path) -> None:
    """Require the deployed site to match the declared current frontier."""

    frontier_figure = output / "figures" / CURRENT_FRONTIER_FIGURE
    if not frontier_figure.is_file():
        raise RuntimeError(
            "website build is missing the current theorem figure: "
            f"{frontier_figure}"
        )

    local_frontier_src = f'src="figures/{CURRENT_FRONTIER_FIGURE}"'

    visual_atlas_path = output / "visual-atlas.html"
    if not visual_atlas_path.is_file():
        raise RuntimeError("website build is missing visual-atlas.html")
    visual_atlas = visual_atlas_path.read_text(encoding="utf-8")
    if local_frontier_src not in visual_atlas:
        raise RuntimeError("Visual Atlas does not use the bundled current theorem figure")
    if f'src="{RAW_FIGURE_PREFIX}' in visual_atlas:
        raise RuntimeError("Visual Atlas still depends on raw GitHub main for figures")
    _require_once(visual_atlas, f'id="p{CURRENT_FRONTIER}-frontier"', "Visual Atlas")

    homepage_path = output / "index.html"
    if not homepage_path.is_file():
        raise RuntimeError("website build is missing index.html")
    homepage = homepage_path.read_text(encoding="utf-8")
    if local_frontier_src not in homepage:
        raise RuntimeError("Homepage does not use the bundled current theorem figure")
    if f'src="{RAW_FIGURE_PREFIX}' in homepage:
        raise RuntimeError("Homepage still depends on raw GitHub main for figures")
    if CURRENT_RECORD_TEXT not in homepage:
        raise RuntimeError("Homepage Project at a glance is not synchronized to the current frontier")
    _require_once(homepage, f'id="p{CURRENT_FRONTIER}-frontier"', "Homepage")
    _require_once(homepage, CURRENT_HOME_MARKER, "Homepage source marker")

    reader_css = (output / "reader-experience-v2.css").read_text(encoding="utf-8")
    for token in ("#reproduce .equation", "contain: inline-size", "#reproduce.two-col > *"):
        if token not in reader_css:
            raise RuntimeError(f"reproducibility containment CSS is missing: {token}")

    stale_tokens = (
        "Current theorem frontier · P87",
        "Current record:</strong> 87 proposition-level results through P87",
        "Current theorem frontier · P86",
        "Current record:</strong> 86 proposition-level results through P86",
    )
    stale = [token for token in stale_tokens if token in homepage]
    if stale:
        raise RuntimeError(f"Homepage contains stale pre-P93 reader text: {stale}")


def _validate_research_three(output: Path) -> None:
    measurement_path = output / "measurement-science.html"
    if not measurement_path.is_file():
        raise RuntimeError("website build is missing measurement-science.html")
    measurement = measurement_path.read_text(encoding="utf-8")
    required = (
        "Research III · Consciousness Measurement Science",
        MEASUREMENT_REPO,
        "what can be identified, bounded, predicted, or falsified",
        "M0-M7",
        "Implemented now versus not yet established",
        "CEP JSON schema",
        "Claim JSON schema",
        "Assumption registry",
        "Failure-mode registry",
        "Software and reproducibility",
        *MEASUREMENT_SCIENCE_REQUIRED_MARKERS,
        f"research-three-snapshot: {MEASUREMENT_PIN}",
        f"consciousness-measurement-science/{MEASUREMENT_PIN}/docs/figures/measurement_architecture.svg",
        f"consciousness-measurement-science/blob/{MEASUREMENT_PIN}/schemas/cep.schema.json",
        f"consciousness-measurement-science/blob/{MEASUREMENT_PIN}/schemas/claim.schema.json",
        f"consciousness-measurement-science/blob/{MEASUREMENT_PIN}/docs/electromagnetic-field-program.md",
        f"consciousness-measurement-science/{MEASUREMENT_PIN}/docs/figures/v16_v20_electromagnetic_validation.svg",
        "Claim ceiling today:",
    )
    missing = [token for token in required if token not in measurement]
    if missing:
        raise RuntimeError(f"Research III page is missing required content: {missing}")

    stale_claims = (
        "<strong>23</strong><span>tests in each CI job",
        "<strong>98</strong><span>tests in each CI job",
        "<strong>V1-V15</strong><span>formal validation stages</span>",
        "23</strong><span>scientific visuals: 9 architecture + 14 validation",
        "planned by the roadmap",
    )
    stale = [token for token in stale_claims if token in measurement]
    if stale:
        raise RuntimeError(f"Research III page contains stale implementation claims: {stale}")

    for legacy_pin in LEGACY_RESEARCH_THREE_PINS:
        if legacy_pin in measurement:
            raise RuntimeError(
                f"Research III page contains stale snapshot pin: {legacy_pin}"
            )

    lineage_path = output / "research-lineage.html"
    if not lineage_path.is_file():
        raise RuntimeError("website build is missing research-lineage.html")
    lineage = lineage_path.read_text(encoding="utf-8")
    for token in (
        "Research III · consciousness measurement science",
        f"<strong>{CURRENT_FRONTIER}</strong><span>proposition-level results</span>",
        f"<strong>P{CURRENT_FRONTIER}</strong><span>current theorem frontier</span>",
        "<strong>v0.82.0</strong><span>current documented release</span>",
        "The three repositories form a research progression",
        MEASUREMENT_PIN,
    ):
        if token not in lineage:
            raise RuntimeError(f"Research lineage is missing current stage content: {token}")
    for stale in ("<strong>81</strong>", "<strong>P81</strong>", "v0.81.0"):
        if stale in lineage:
            raise RuntimeError(f"Research lineage contains stale Research II state: {stale}")
    for legacy_pin in LEGACY_RESEARCH_THREE_PINS:
        if legacy_pin in lineage:
            raise RuntimeError(f"Research lineage contains stale Research III pin: {legacy_pin}")

    app = (output / "app.js").read_text(encoding="utf-8")
    if "measurement-science.html" not in app or "Research III" not in app:
        raise RuntimeError("app.js does not expose Research III navigation")
    if app.count("const direct = card.querySelector('a[href]');") != 1:
        raise RuntimeError("app.js contains the clickable-card declaration more than once")


def prepare_website(source: Path, output: Path) -> None:
    """Copy source and canonical figures into one auditable Pages build."""

    if not source.is_dir():
        raise FileNotFoundError(f"website source directory not found: {source}")

    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(source, output)

    full_site = _is_full_site(output)

    # Release-only synchronization needs the complete canonical reader surface.
    # Small synthetic source trees used by unit tests still exercise the shared
    # asset builder without being forced to emulate the whole public website.
    if full_site:
        synchronize_site(output, write=True)
    _copy_canonical_figures(output)

    html_files = sorted(output.glob("*.html"))
    if not html_files:
        raise RuntimeError("website build contains no HTML pages")

    required_tags = (
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

    for path in html_files:
        text = path.read_text(encoding="utf-8")
        if "</head>" not in text:
            raise RuntimeError(f"missing </head> in {path}")

        text = _normalize_navigation_assets(text)
        text = _normalize_topbar_fallback(text)
        text = _localize_figure_sources(text)

        additions = [tag for tag in required_tags if tag not in text]
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

    if full_site:
        _validate_current_frontier_pages(output)
        _validate_research_three(output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("website"))
    parser.add_argument("--output", type=Path, default=Path("_site"))
    args = parser.parse_args()
    prepare_website(args.source, args.output)
    print(
        f"prepared website with Research II P{CURRENT_FRONTIER} and Research III "
        f"{MEASUREMENT_PIN}: {args.output}"
    )


if __name__ == "__main__":
    main()
