"""Validate the journal-facing P1-P100 publication package.

This verifier protects formatting and scientific-boundary contracts without
modifying the frozen theorem record.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLICATION = ROOT / "publication"
MANUSCRIPT = PUBLICATION / "manuscript.md"
REFERENCES = ROOT / "references.bib"

FORBIDDEN_PUNCTUATION = ("\u2013", "\u2014")
REQUIRED_HEADINGS = (
    "## Abstract",
    "# 1. Introduction",
    "# 2. Methods and Materials",
    "# 3. Results",
    "# 4. Discussion",
    "# 5. Summary and Conclusions",
)
REQUIRED_BOUNDARIES = (
    "does not establish that consciousness is nonphysical",
    "Failure to reject is not model acceptance",
    "not an empirical finding about consciousness",
    "current certification data to remain conditionally valid",
)
REQUIRED_FIGURES = (
    "docs/figures/theorem_roadmap.svg",
    "docs/figures/p19_fundamental_physical_sufficiency.svg",
    "docs/figures/p71_target_provenance_noncircularity.svg",
    "docs/figures/p92_exact_global_mixed_prevalence_distance.svg",
    "docs/figures/p100_anytime_sequential_eprocess.svg",
)


def _section(text: str, heading: str, next_heading_pattern: str = r"\n#") -> str:
    start = text.find(heading)
    if start < 0:
        raise AssertionError(f"missing section heading: {heading}")
    body_start = start + len(heading)
    match = re.search(next_heading_pattern, text[body_start:])
    end = body_start + match.start() if match else len(text)
    return text[body_start:end].strip()


def _word_count(text: str) -> int:
    clean = re.sub(r"\$.*?\$", " ", text, flags=re.DOTALL)
    clean = re.sub(r"\\\[.*?\\\]", " ", clean, flags=re.DOTALL)
    clean = re.sub(r"\[[^\]]+\]\([^\)]+\)", " ", clean)
    return len(re.findall(r"\b[\w'-]+\b", clean))


def _citation_keys(text: str) -> set[str]:
    return set(re.findall(r"@([A-Za-z0-9_:-]+)", text))


def _bib_keys(text: str) -> set[str]:
    return set(re.findall(r"@\w+\{\s*([^,\s]+)\s*,", text))


def validate() -> list[str]:
    errors: list[str] = []
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    references = REFERENCES.read_text(encoding="utf-8")

    for path in PUBLICATION.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        for mark in FORBIDDEN_PUNCTUATION:
            if mark in text:
                errors.append(
                    f"{path.relative_to(ROOT)} contains forbidden punctuation {mark!r}"
                )

    positions = [manuscript.find(heading) for heading in REQUIRED_HEADINGS]
    for heading, position in zip(REQUIRED_HEADINGS, positions, strict=True):
        if position < 0:
            errors.append(f"manuscript missing required heading: {heading}")
    if all(position >= 0 for position in positions) and positions != sorted(positions):
        errors.append("required Research Article headings are out of order")

    abstract = _section(manuscript, "## Abstract", r"\n\*\*Keywords:\*\*")
    abstract_words = _word_count(abstract)
    if abstract_words > 250:
        errors.append(f"abstract has {abstract_words} words; maximum is 250")
    if _citation_keys(abstract):
        errors.append("abstract contains citation keys")

    significance = _section(manuscript, "## Significance statement", r"\n# 1\.")
    significance_words = _word_count(significance)
    if significance_words > 120:
        errors.append(
            f"significance statement has {significance_words} words; maximum is 120"
        )

    keyword_match = re.search(r"^\*\*Keywords:\*\*\s*(.+)$", manuscript, re.MULTILINE)
    if keyword_match is None:
        errors.append("manuscript is missing keywords")
    else:
        keywords = [item.strip() for item in keyword_match.group(1).split(";") if item.strip()]
        if len(keywords) > 6:
            errors.append(f"manuscript has {len(keywords)} keywords; maximum is 6")

    used_keys = _citation_keys(manuscript)
    known_keys = _bib_keys(references)
    missing_keys = sorted(used_keys - known_keys)
    if missing_keys:
        errors.append("missing bibliography keys: " + ", ".join(missing_keys))

    for phrase in REQUIRED_BOUNDARIES:
        if phrase not in manuscript:
            errors.append(f"missing required scientific boundary: {phrase!r}")

    for figure in REQUIRED_FIGURES:
        if not (ROOT / figure).is_file():
            errors.append(f"missing required main figure: {figure}")

    exact_contracts = {
        "P89 linear benchmark": r"5/168|\\frac\{5\}\{168\}",
        "P92 exact distance": r"1/24|\\frac1\{24\}",
        "P99 e-value": r"25/2|\\frac\{25\}\{2\}",
        "P100 reserve factor": r"27/4|\\frac\{27\}\{4\}",
        "P100 two-round process": r"729/16|\\frac\{729\}\{16\}",
        "P100 two-round sample accounting": r"30,192|30192",
    }
    for label, pattern in exact_contracts.items():
        if re.search(pattern, manuscript) is None:
            errors.append(f"missing exact manuscript contract: {label}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"[publication] ERROR: {error}")
        return 1

    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    abstract = _section(manuscript, "## Abstract", r"\n\*\*Keywords:\*\*")
    significance = _section(manuscript, "## Significance statement", r"\n# 1\.")
    print(
        "[publication] manuscript validation passed; "
        f"abstract={_word_count(abstract)} words; "
        f"significance={_word_count(significance)} words; "
        f"citations={len(_citation_keys(manuscript))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
