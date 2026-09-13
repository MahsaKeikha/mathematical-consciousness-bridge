"""Normalize scholarly publication text to the repository ASCII dash policy."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = (
    "docs/claim_evidence_standard.md",
    "website/sources.html",
    "website/start-here.html",
)


def main() -> None:
    forbidden = (chr(0x2013), chr(0x2014))
    for relative_path in TARGETS:
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        for character in forbidden:
            text = text.replace(character, "-")
        path.write_text(text, encoding="utf-8")

    offenders = []
    for relative_path in TARGETS:
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        if any(character in text for character in forbidden):
            offenders.append(relative_path)
    if offenders:
        raise RuntimeError(f"forbidden dash typography remains: {offenders}")


if __name__ == "__main__":
    main()
