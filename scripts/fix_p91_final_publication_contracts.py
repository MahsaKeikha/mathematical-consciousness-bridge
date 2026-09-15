from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected exactly one match, found {count}: {old!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> None:
    implementation = "website/implementation.html"
    replace_once(
        implementation,
        '<a href="#stage-06"><strong>6 · P73-P90</strong>Channel recovery, adequacy & certified separation</a>',
        '<a href="#stage-06"><strong>6 · P73-P91</strong>Channel recovery, adequacy & certified separation</a>',
    )
    replace_once(
        implementation,
        '<p class="stage-number">Stage 06 · P73-P90</p>',
        '<p class="stage-number">Stage 06 · P73-P91</p>',
    )
    replace_once(
        implementation,
        'P73-P90 build a continuous chain from channel recovery to certified model-family separation. The certified full-law separation subchain P77-P87 progressively strengthens exact rejection certificates while preserving the same declared target-measurement family.',
        'P73-P91 build a continuous chain from channel recovery to certified model-family separation. The certified full-law separation subchain P77-P91 progressively strengthens exact rejection certificates while preserving the same declared target-measurement family.',
    )
    replace_once(
        implementation,
        '<strong>Frontier continuation:</strong> P77-P89 strengthen this branch from individual adequacy constraints to certified separation from the complete continuous model family.',
        '<strong>Frontier continuation:</strong> P77-P91 strengthen this branch from individual adequacy constraints to certified separation from the complete continuous model family.',
    )
    replace_once(
        implementation,
        '<a href="index.html#p90-frontier">current P89 frontier</a>',
        '<a href="index.html#p91-frontier">current P91 frontier</a>',
    )

    atlas = "website/visual-atlas.html"
    replace_once(
        atlas,
        '<article class="frontier-summary-card"><h3>Beyond P89</h3><p><strong>L90 = 5/72 = (7/3)L89</strong>. The gain comes from nonlinear image structure, not a larger linear coefficient search.</p></article>',
        '<article class="frontier-summary-card"><h3>Beyond P89</h3><p><strong>L89 = 5/168</strong> and <strong>L90 = 5/72 = (7/3)L89</strong>. The gain comes from nonlinear image structure, not a larger linear coefficient search.</p></article>',
    )

    sources = "website/sources.html"
    replace_once(
        sources,
        '<p>The rank-two identity is standard linear algebra for a two-component product mixture. The selected exact witness and interval certificate are repository-original. The result does not identify consciousness or prove nonphysicality.</p>',
        '<p>The rank-two identity is standard linear algebra for a two-component product mixture. The selected exact witness and interval certificate are repository-original. P91 certifies <strong>1/42 &lt; d_inf(P_emp, M75) &lt;= 1/24</strong> over the full declared P75 parameter cube. The upper endpoint 1/24 is a constructive upper bound, not a claimed exact global optimum. The result does not identify consciousness or prove nonphysicality.</p>',
    )

    print("P91 final publication contract fixes applied")


if __name__ == "__main__":
    main()
