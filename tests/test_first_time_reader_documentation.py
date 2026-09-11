from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
START_HERE = ROOT / "docs" / "START_HERE.md"
GLOSSARY = ROOT / "docs" / "plain_language_glossary.md"
NAVIGATION = ROOT / "docs" / "research_navigation.md"


def test_start_here_is_prominent_before_long_form_readme() -> None:
    text = README.read_text(encoding="utf-8")
    start_link = "[Start Here: First-Time Reader Guide](docs/START_HERE.md)"
    glossary_link = "[Plain-Language Glossary](docs/plain_language_glossary.md)"

    assert start_link in text
    assert glossary_link in text
    assert text.index(start_link) < text.index("# What this project is trying to achieve, in plain language")


def test_start_here_explains_core_logic_and_scientific_boundaries() -> None:
    text = START_HERE.read_text(encoding="utf-8")
    required = (
        "The shortest possible summary",
        "The research in eight layers",
        "What has actually been established?",
        "What has not been established?",
        "Three recommended reading paths",
        "P71-P79",
        "non-separation is not model acceptance",
        "physical-to-experiential bridge remains open",
    )
    for token in required:
        assert token in text, token


def test_glossary_covers_core_terms_and_common_confusions() -> None:
    text = GLOSSARY.read_text(encoding="utf-8")
    required = (
        "Physical descriptor",
        "Target, $E$",
        "Bridge, $B$",
        "Fiber of a descriptor",
        "Collision",
        "Conditional mutual information",
        "Target-measurement channel",
        "Identifiability",
        "Model adequacy",
        "Certified non-separation",
        "Do not confuse",
        "failure of one physical descriptor",
        "failure of physics",
    )
    for token in required:
        assert token in text, token


def test_research_navigation_has_layered_reader_paths() -> None:
    text = NAVIGATION.read_text(encoding="utf-8")
    required = (
        "First-time or non-specialist reader",
        "Technical reader",
        "Audit and reproducibility reader",
        "START_HERE.md",
        "plain_language_glossary.md",
    )
    for token in required:
        assert token in text, token
