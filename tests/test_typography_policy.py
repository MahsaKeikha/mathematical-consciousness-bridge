from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_CODEPOINTS = {
    "\u2013": "Unicode en dash",
    "\u2014": "Unicode em dash",
}
TEXT_SUFFIXES = {
    ".md",
    ".html",
    ".svg",
    ".py",
    ".toml",
    ".cff",
    ".yml",
    ".yaml",
    ".bib",
    ".txt",
    ".css",
    ".js",
    ".json",
}
EXACT_TEXT_FILES = {
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
}


def _public_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        relative = path.relative_to(ROOT)
        if path.suffix.lower() in TEXT_SUFFIXES or str(relative) in EXACT_TEXT_FILES:
            yield path


def test_repository_contains_no_en_dash_or_em_dash_characters():
    violations = []
    for path in _public_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for character, label in FORBIDDEN_CODEPOINTS.items():
            if character not in text:
                continue
            lines = [
                number
                for number, line in enumerate(text.splitlines(), start=1)
                if character in line
            ]
            violations.append(
                f"{path.relative_to(ROOT)}: {label} on lines {lines[:12]}"
            )

    assert not violations, "Forbidden dash typography found:\n" + "\n".join(violations)
