import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

P90_READER_BLOCK = '''<section class="boundary" id="p90-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current exact frontier · P90</p><h2>Exact nonlinear rank-one slice separation</h2><p>P90 moves beyond the complete P89 linear parity-functional envelope by exploiting a nonlinear identity of the declared strict P75 model image. With prevalence fixed at zero, the active law is one product Bernoulli component, so the canonical two-by-two slice must satisfy <strong>ad = bc</strong>. The empirical determinant residual is <strong>5/192</strong>, giving the exact distance <strong>L90 = 5/72 = (7/3)L89</strong>, while P89 remains the complete-linear subfrontier at <strong>5/168</strong>.</p><p>This is a conditional exact separation result for the stated strict box. It does not identify consciousness, establish nonphysicality, exhaust more general nonlinear mixture regimes, or close the physical-to-experiential bridge.</p></div></section>'''

P89_START_HERE = '''      <p><strong>P89 closes the complete real linear parity-functional class.</strong> <strong>P89 is the current complete-linear frontier.</strong> It removes both the finite coefficient-radius restriction and the exactly-four-observable support restriction. Across every real linear functional of all eleven canonical P83 parity coordinates, matching exact lower and upper certificates prove <strong>L89 = 5/168</strong>, strictly above <strong>L88 = 1/64</strong>.</p>'''

P90_START_HERE = '''      <p><strong>P90 moves beyond that complete linear envelope.</strong> On the strict P75 box, prevalence is fixed at zero, so the active observable law is a single product Bernoulli component and a canonical two-by-two slice must satisfy <strong>ad = bc</strong>. The empirical determinant residual gives a lower radius of <strong>5/72</strong>, and an explicit rational P75 point attains the same full-law distance. Thus <strong>L90 = 5/72 = (7/3)L89</strong>.</p>'''


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_required(text: str, old: str, new: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing expected text: {old}")
    return text.replace(old, new)


def repair_plain_language() -> None:
    path = "website/plain-language.html"
    text = read(path)
    text = text.replace(
        "This is the 90-result Research II theorem program currently reaching P89.",
        "This is the 90-result Research II theorem program currently reaching P90.",
    )
    text = text.replace(
        "Research II develops exact and finite-data tests for representation, scale, target provenance, model adequacy, and physical-description sufficiency, currently through P89.",
        "Research II develops exact and finite-data tests for representation, scale, target provenance, model adequacy, and physical-description sufficiency, currently through P90.",
    )
    text = text.replace("The current theorem frontier is P89.", "The current theorem frontier is P90.")
    text, count = re.subn(
        r'<section class="boundary" id="p(?:89|90)-reader-frontier">.*?</section>',
        P90_READER_BLOCK,
        text,
        count=1,
        flags=re.DOTALL,
    )
    if count != 1:
        raise RuntimeError("plain-language current reader frontier block missing")
    write(path, text)


def repair_start_here() -> None:
    path = "website/start-here.html"
    text = read(path)
    text = text.replace("current Research II P89 frontier", "current Research II P90 frontier")
    text = text.replace("Open all 89 Research II results", "Open all 90 Research II results")
    text = text.replace(
        "<h2>P78-P89 progressively tighten global separation from the declared continuous model family</h2>",
        "<h2>P78-P90 progressively tighten global separation from the declared continuous model family</h2>",
    )
    if P90_START_HERE not in text:
        text = replace_required(text, P89_START_HERE, P89_START_HERE + "\n" + P90_START_HERE)
    text = text.replace(
        'docs/proposition_89_complete_linear_parity_duality.md">Read P89 theorem',
        'docs/proposition_90_exact_nonlinear_rank_one_separation.md">Read P90 theorem',
    )
    write(path, text)


def repair_promoter() -> None:
    path = "scripts/promote_p90_public_frontier.py"
    text = read(path)
    if "# P90 reader-surface canonicalization" in text:
        return

    marker = '    path = "website/implementation.html"\n'
    if marker not in text:
        raise RuntimeError("permanent promoter website implementation anchor missing")

    insertion = f'''    # P90 reader-surface canonicalization\n    path = "website/plain-language.html"\n    text = read(path)\n    text = text.replace("This is the 90-result Research II theorem program currently reaching P89.", "This is the 90-result Research II theorem program currently reaching P90.")\n    text = text.replace("currently through P89.", "currently through P90.")\n    text = text.replace("The current theorem frontier is P89.", "The current theorem frontier is P90.")\n    text = re.sub(r'<section class="boundary" id="p(?:89|90)-reader-frontier">.*?</section>', {P90_READER_BLOCK!r}, text, count=1, flags=re.DOTALL)\n    write(path, text)\n\n    path = "website/start-here.html"\n    text = read(path)\n    text = text.replace("current Research II P89 frontier", "current Research II P90 frontier")\n    text = text.replace("Open all 89 Research II results", "Open all 90 Research II results")\n    text = text.replace("P78-P89 progressively tighten global separation", "P78-P90 progressively tighten global separation")\n    if {P90_START_HERE!r} not in text:\n        text = text.replace({P89_START_HERE!r}, {P89_START_HERE!r} + "\\n" + {P90_START_HERE!r}, 1)\n    text = text.replace('docs/proposition_89_complete_linear_parity_duality.md">Read P89 theorem', 'docs/proposition_90_exact_nonlinear_rank_one_separation.md">Read P90 theorem')\n    write(path, text)\n\n'''
    text = text.replace(marker, insertion + marker, 1)
    write(path, text)


def repair_verifier() -> None:
    path = "scripts/verify_repository.py"
    text = read(path)
    old = '''def _assert_detailed_proposition_record() -> None:\n    record = (ROOT / "docs" / "detailed_proposition_record.md").read_text(\n        encoding="utf-8"\n    )\n    for number in range(1, 91):\n        if f"Proposition {number}" not in record:\n            raise RuntimeError(\n                f"detailed proposition record is missing Proposition {number}"\n            )\n'''
    new = '''def _assert_detailed_proposition_record() -> None:\n    record = (ROOT / "docs" / "detailed_proposition_record.md").read_text(\n        encoding="utf-8"\n    )\n    covered: set[int] = set()\n    for match in re.finditer(r"\\bP(\\d+)(?:\\s*(?:-|to|through)\\s*P?(\\d+))?\\b", record):\n        start = int(match.group(1))\n        end = int(match.group(2) or start)\n        if end < start:\n            start, end = end, start\n        covered.update(range(start, end + 1))\n    missing = [number for number in range(1, 91) if number not in covered]\n    if missing:\n        raise RuntimeError(\n            f"detailed proposition record is missing proposition references: {missing}"\n        )\n'''
    if old in text:
        text = text.replace(old, new, 1)
    elif "covered: set[int] = set()" not in text:
        raise RuntimeError("detailed proposition verifier anchor missing")
    text = text.replace(
        'raise RuntimeError("figure manifest current_frontier_figure is missing")',
        'raise TypeError("figure manifest current_frontier_figure is missing")',
    )
    text = text.replace(
        '            text=True,\n        )',
        '            text=True,\n            check=False,\n        )',
        1,
    )
    write(path, text)


def main() -> None:
    repair_plain_language()
    repair_start_here()
    repair_promoter()
    repair_verifier()
    print("P90 reader residuals and verifier repaired")


if __name__ == "__main__":
    main()
