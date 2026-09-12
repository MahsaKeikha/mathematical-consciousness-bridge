"""One-time helper to update release-era guards for the P82 candidate."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def project_version() -> str:
    text = read("pyproject.toml")
    match = re.search(r'^version = "([0-9]+\.[0-9]+\.[0-9]+)"$', text, re.MULTILINE)
    if match is None:
        raise RuntimeError("project version missing from pyproject.toml")
    return match.group(1)


def update_readme_citation() -> None:
    version = project_version()
    text = read("README.md")
    marker = "# Citation\n\n"
    release_line = f"Current release: **Version {version}**. Current theorem frontier: **P82**.\n\n"
    if release_line not in text:
        if marker not in text:
            raise RuntimeError("README citation heading missing")
        text = text.replace(marker, marker + release_line, 1)
    write("README.md", text)


def update_reproducibility_guard() -> None:
    path = "tests/test_reproducibility_contract.py"
    text = read(path)
    if "def _project_version()" not in text:
        text = text.replace(
            "from pathlib import Path\n",
            "import re\nfrom pathlib import Path\n",
            1,
        )
        marker = (
            "def _read(relative: str) -> str:\n"
            "    return (ROOT / relative).read_text(encoding=\"utf-8\")\n\n"
        )
        helper = (
            "def _project_version() -> str:\n"
            "    source = _read(\"pyproject.toml\")\n"
            "    match = re.search(\n"
            "        r'^version = \"([0-9]+\\.[0-9]+\\.[0-9]+)\"$',\n"
            "        source,\n"
            "        re.MULTILINE,\n"
            "    )\n"
            "    assert match is not None\n"
            "    return match.group(1)\n\n"
        )
        if marker not in text:
            raise RuntimeError("reproducibility guard read helper missing")
        text = text.replace(marker, marker + "\n" + helper, 1)

    old = (
        "def test_plot_generators_use_deterministic_svg_metadata_and_ids() -> None:\n"
        "    for path in (\n"
        "        \"scripts/generate_quantitative_atlas.py\",\n"
        "        \"scripts/generate_quantum_foundations_atlas.py\",\n"
        "    ):\n"
        "        source = _read(path)\n"
        "        assert '\"svg.hashsalt\": \"mathematical-consciousness-bridge-v0.81.0\"' in source\n"
        "        assert '\"Date\": None' in source\n"
        "        assert '\"Creator\": \"Mathematical Consciousness Bridge v0.81.0\"' in source\n"
    )
    new = (
        "def test_plot_generators_use_deterministic_svg_metadata_and_ids() -> None:\n"
        "    version = _project_version()\n"
        "    for path in (\n"
        "        \"scripts/generate_quantitative_atlas.py\",\n"
        "        \"scripts/generate_quantum_foundations_atlas.py\",\n"
        "    ):\n"
        "        source = _read(path)\n"
        "        assert (\n"
        "            f'\"svg.hashsalt\": \"mathematical-consciousness-bridge-v{version}\"'\n"
        "            in source\n"
        "        )\n"
        "        assert '\"Date\": None' in source\n"
        "        assert f'\"Creator\": \"Mathematical Consciousness Bridge v{version}\"' in source\n"
    )
    if old in text:
        text = text.replace(old, new, 1)
    elif "mathematical-consciousness-bridge-v0.81.0" in text:
        raise RuntimeError("unexpected hard-coded reproducibility guard layout")
    write(path, text)


def update_website_orientation_guard() -> None:
    path = "tests/test_website_research_orientation.py"
    text = read(path)
    text = text.replace(
        'hero = text.index("Eighty results, one dependency-aware scientific program")',
        'hero = text.index("Eighty-two results, one dependency-aware scientific program")',
    )
    for token in (
        '        "proposition_81_projection_event_model_separation.md",\n',
        '        "proposition_82_exact_nested_projection_contrast.md",\n',
        '        "p82_equation_provenance.md",\n',
    ):
        if token not in text:
            insertion_point = '        "proposition_80_simplex_coupled_model_separation.md",\n'
            if insertion_point not in text:
                raise RuntimeError("P80 audit-path guard missing")
            text = text.replace(insertion_point, insertion_point + token, 1)

    old = (
        "def test_research_map_presents_p77_through_p80_in_dependency_order():\n"
        "    text = MAP.read_text(encoding=\"utf-8\")\n"
        "    assert \"through Proposition 80\" in text\n\n"
        "    p77 = text.index(\"IV-G · Full-law model-set separation\")\n"
        "    p78 = text.index(\"IV-H · Certified continuous-family separation\")\n"
        "    p79 = text.index(\"IV-I · Certified sampling radius\")\n"
        "    p80 = text.index(\"IV-J · Tighter continuous-family relaxation\")\n"
        "    assert p77 < p78 < p79 < p80\n\n"
        "    assert text.count(\"P78: Certified continuous P75 model separation\") == 1\n"
        "    assert text.count(\"How is P77 made rigorous for the continuous P75 family?\") == 1\n"
        "    assert \"only the certified global lower bound can feed the P77 rejection gate\" in text\n"
        "    assert \"P80 tightens the continuous lower bound\" in text\n"
    )
    new = (
        "def test_research_map_presents_p77_through_p82_in_dependency_order():\n"
        "    text = MAP.read_text(encoding=\"utf-8\")\n"
        "    assert \"through Proposition 82\" in text\n"
        "    frontier = text.index('id=\"continuous-model-frontier\"')\n"
        "    p77 = text.index(\"Open P77 →\", frontier)\n"
        "    p78 = text.index(\"Open P78 →\", frontier)\n"
        "    p79 = text.index(\"Open P79 →\", frontier)\n"
        "    p80 = text.index(\"Open P80 →\", frontier)\n"
        "    p81 = text.index(\"Open P81 →\", frontier)\n"
        "    p82 = text.index(\"Open P82 →\", frontier)\n"
        "    assert p77 < p78 < p79 < p80 < p81 < p82\n\n"
        "    assert text.count(\"P78: Certified continuous P75 model separation\") == 1\n"
        "    assert text.count(\"How is P77 made rigorous for the continuous P75 family?\") == 1\n"
        "    assert \"only the certified global lower bound can feed the P77 rejection gate\" in text\n"
        "    assert \"Simplex coupling\" in text\n"
        "    assert \"256 genuinely new residual events\" in text\n"
        "    assert \"P81 = 1/16 to P82 = 1/12\" in text\n"
    )
    if old not in text:
        raise RuntimeError("old P77-P80 website guard not found")
    text = text.replace(old, new, 1)
    write(path, text)


def main() -> None:
    update_readme_citation()
    update_reproducibility_guard()
    update_website_orientation_guard()
    print("P82 release guards updated")


if __name__ == "__main__":
    main()
