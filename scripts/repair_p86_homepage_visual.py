"""One-time guarded migration for the P86 homepage visual contract.

This helper extends the permanent ``sync_figure_publication.py`` contract so the
homepage, not only the Visual Atlas, is deterministically synchronized to the
current theorem frontier. Delete this helper after the migration is committed.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require_replace(text: str, old: str, new: str, *, label: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise RuntimeError(f"could not apply migration: {label}")
    return text.replace(old, new, 1)


def patch_syncer() -> None:
    path = ROOT / "scripts" / "sync_figure_publication.py"
    text = path.read_text(encoding="utf-8")
    text = require_replace(
        text,
        'VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"\nVERIFIER = ROOT / "scripts" / "verify_repository.py"',
        'VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"\nHOME = ROOT / "website" / "index.html"\nVERIFIER = ROOT / "scripts" / "verify_repository.py"',
        label="HOME constant",
    )

    function = '''

def _normalize_homepage(text: str) -> str:
    """Make P86 the first theorem visual and demote older homepage frontiers."""

    pattern = re.compile(r'\\s*<section id="p86-frontier".*?</section>\\s*', re.DOTALL)
    text, count = pattern.subn("\\n", text, count=1)
    if count != 1:
        raise RuntimeError(f"expected exactly one P86 homepage section, found {count}")

    replacements = (
        ("Current theorem frontier · P85", "Previous theorem frontier · P85"),
        ("The 84 results form several dependency branches.", "The 86 results form several dependency branches."),
        ("You do not need to read all 84 propositions in numerical order", "You do not need to read all 86 propositions in numerical order"),
        ("Focus on P19 and P71-P84, then read the falsification program.", "Focus on P19 and P71-P86, then read the falsification program."),
    )
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new, 1)
        elif new not in text:
            raise RuntimeError(f"homepage frontier normalization could not resolve: {old!r}")

    marker = "<!-- current-frontier-home: P86 -->"
    text = re.sub(r"\\s*" + re.escape(marker) + r"\\s*", "\\n", text)
    hero = re.search(r'<section class="hero">.*?</section>', text, re.DOTALL)
    if hero is None:
        raise RuntimeError("could not locate homepage hero section")

    prefix = text[: hero.end()].rstrip()
    suffix = text[hero.end() :].lstrip()
    insertion = "\\n\\n" + marker + "\\n" + _p86_visual_section() + "\\n\\n"
    result = prefix + insertion + suffix
    had_final_newline = result.endswith("\\n")
    result = "\\n".join(line.rstrip() for line in result.splitlines())
    return result + ("\\n" if had_final_newline else "")
'''
    anchor = "\n\ndef _expected_outputs() -> dict[Path, str]:"
    if "def _normalize_homepage" not in text:
        if anchor not in text:
            raise RuntimeError("could not locate expected-output anchor")
        text = text.replace(anchor, function + anchor, 1)

    text = require_replace(
        text,
        '    visual_source = VISUAL_ATLAS.read_text(encoding="utf-8")\n    return {',
        '    visual_source = VISUAL_ATLAS.read_text(encoding="utf-8")\n    home_source = HOME.read_text(encoding="utf-8")\n    return {',
        label="homepage source",
    )
    text = require_replace(
        text,
        "        VISUAL_ATLAS: _normalize_visual_atlas(visual_source),\n    }",
        "        VISUAL_ATLAS: _normalize_visual_atlas(visual_source),\n        HOME: _normalize_homepage(home_source),\n    }",
        label="homepage expected output",
    )
    path.write_text(text, encoding="utf-8")


def patch_tests() -> None:
    path = ROOT / "tests" / "test_figure_publication_sync.py"
    text = path.read_text(encoding="utf-8")
    text = require_replace(
        text,
        'VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"\nSYNCER =',
        'VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"\nHOME = ROOT / "website" / "index.html"\nSYNCER =',
        label="test HOME constant",
    )

    test_block = '''

def test_homepage_leads_with_p86_before_historical_frontiers() -> None:
    text = HOME.read_text(encoding="utf-8")
    p86 = text.index('id="p86-frontier"')
    plain = text.index('id="plain-language"')
    p84 = text.index('id="p84-frontier"')
    p85 = text.index('id="p85-frontier"')

    assert p86 < plain
    assert p86 < p84
    assert p86 < p85
    current = text[p86:plain]
    assert "Current theorem frontier · P86" in current
    assert P86_FIGURE in current
    assert "L85 = 0 &lt; L86 = 1/192" in current
    assert "weighted_quad_projection_parity_functional_separation.py" in current
    assert "test_weighted_quad_projection_parity_functional_separation.py" in current
    assert "Previous theorem frontier · P84" in text[p84:]
    assert "Previous theorem frontier · P85" in text[p85:]
    assert "Current theorem frontier · P85" not in text
    assert "The 84 results form several dependency branches." not in text
    assert "all 84 propositions" not in text
    assert "P71-P84, then read the falsification program" not in text
    assert "The 86 results form several dependency branches." in text
    assert "all 86 propositions" in text
'''
    anchor = "\n\ndef test_figure_publication_synchronizer_reports_zero_drift() -> None:"
    if "def test_homepage_leads_with_p86_before_historical_frontiers" not in text:
        if anchor not in text:
            raise RuntimeError("could not add homepage figure test")
        text = text.replace(anchor, test_block + anchor, 1)

    text = require_replace(
        text,
        '''    atlas = (site / "visual-atlas.html").read_text(encoding="utf-8")
    assert f'src="figures/{P86_FIGURE}"' in atlas
    assert f'src="{RAW_PREFIX}' not in atlas
''',
        '''    atlas = (site / "visual-atlas.html").read_text(encoding="utf-8")
    assert f'src="figures/{P86_FIGURE}"' in atlas
    assert f'src="{RAW_PREFIX}' not in atlas

    home = (site / "index.html").read_text(encoding="utf-8")
    assert f'src="figures/{P86_FIGURE}"' in home
    assert f'src="{RAW_PREFIX}' not in home
    assert home.index('id="p86-frontier"') < home.index('id="plain-language"')
    assert home.index('id="p86-frontier"') < home.index('id="p85-frontier"')
''',
        label="built homepage test",
    )
    path.write_text(text, encoding="utf-8")


def patch_workflow(path: Path, *, add_index_trigger: bool) -> None:
    text = path.read_text(encoding="utf-8")
    if add_index_trigger and '      - "website/index.html"\n' not in text:
        token = '      - "website/visual-atlas.html"\n'
        if token not in text:
            raise RuntimeError(f"could not add index trigger to {path}")
        text = text.replace(
            token,
            '      - "website/index.html"\n      - "website/visual-atlas.html"\n',
        )

    build_token = (
        "          grep -q 'src=\"figures/p86_exact_minimally_weighted_quad_projection_parity.svg\"' "
        "_site/visual-atlas.html\n"
    )
    if "homepage P86 ordering gate" not in text:
        if build_token not in text:
            raise RuntimeError(f"could not add homepage build gate to {path}")
        addition = build_token + (
            "          # homepage P86 ordering gate\n"
            "          grep -q 'src=\"figures/p86_exact_minimally_weighted_quad_projection_parity.svg\"' _site/index.html\n"
            "          python -c \"from pathlib import Path; t=Path('_site/index.html').read_text(encoding='utf-8'); p=t.index('id=\\\"p86-frontier\\\"'); assert p < t.index('id=\\\"plain-language\\\"'); assert p < t.index('id=\\\"p84-frontier\\\"'); assert p < t.index('id=\\\"p85-frontier\\\"'); assert 'Current theorem frontier · P85' not in t\"\n"
        )
        text = text.replace(build_token, addition, 1)
    path.write_text(text, encoding="utf-8")


def remove_duplicate_syncers() -> None:
    for path in (
        ROOT / "scripts" / "sync_visual_frontier.py",
        ROOT / "tests" / "test_visual_frontier_sync.py",
    ):
        if path.exists():
            path.unlink()


def main() -> None:
    patch_syncer()
    patch_tests()
    patch_workflow(ROOT / ".github" / "workflows" / "figures.yml", add_index_trigger=True)
    patch_workflow(ROOT / ".github" / "workflows" / "pages.yml", add_index_trigger=False)
    remove_duplicate_syncers()
    print("P86 homepage visual migration prepared")


if __name__ == "__main__":
    main()
