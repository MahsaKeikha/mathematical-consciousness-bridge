from pathlib import Path

import migrate_remaining_p90_contracts as migration


def replace_if_present(path: str, old: str, new: str) -> None:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    if old in text:
        file_path.write_text(text.replace(old, new), encoding="utf-8")


def main() -> None:
    migration.replace_required = replace_if_present
    migration.main()

    replace_if_present(
        "docs/glossary.md",
        "The current public frontier is **P89**.",
        "The current public frontier is **P90**.",
    )
    replace_if_present(
        "CITATION.md",
        "This is the preferred citation for the research program at the current documented frontier, P89.",
        "This is the preferred citation for the research program at the current documented frontier, P90.",
    )
    replace_if_present(
        "CITATION.md",
        "The current citation metadata identify Version **0.82.0** and theorem frontier **P89**.",
        "The current citation metadata identify Version **0.82.0** and theorem frontier **P90**.",
    )
    replace_if_present(
        "CITATION.md",
        "The current documented theorem frontier is **P89**. The formal package release remains **Version 0.82.0**. P89 closes the declared complete real linear parity-functional class on the stated P75 box with exact value `L89 = 5/168`; it does not close the physical-to-experiential bridge.",
        "The current documented theorem frontier is **P90**. The formal package release remains **Version 0.82.0**. P90 gives the exact nonlinear rank-one model-separation value `L90 = 5/72 = (7/3)L89` on the declared P75 strict box. P89 remains the complete real linear parity-functional subfrontier at `L89 = 5/168`. Neither result closes the physical-to-experiential bridge.",
    )
    replace_if_present(
        "CITATION.md",
        "[Detailed proposition record](docs/detailed_proposition_record.md): P1 through P89 chronological theorem record.",
        "[Detailed proposition record](docs/detailed_proposition_record.md): P1 through P90 chronological theorem record.",
    )


if __name__ == "__main__":
    main()
