"""Require all permanent scholarly provenance files in repository verification."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "scripts" / "verify_repository.py"
REQUIRED = (
    "docs/claim_source_matrix.md",
    "docs/reference_audit.md",
    "docs/literature_map.md",
)


def main() -> None:
    text = PATH.read_text(encoding="utf-8")
    core_start = text.index("CORE_FILES = (")
    core_end = text.index("\n)\n\nLINK_SURFACES", core_start)
    core = text[core_start:core_end]

    anchor = '    "docs/claim_evidence_standard.md",\n'
    if anchor not in core:
        raise RuntimeError("missing CORE_FILES scholarly anchor")

    missing = [path for path in REQUIRED if f'    "{path}",' not in core]
    if missing:
        insertion = "".join(f'    "{path}",\n' for path in missing)
        absolute_anchor = text.index(anchor, core_start, core_end) + len(anchor)
        text = text[:absolute_anchor] + insertion + text[absolute_anchor:]

    # Re-read the isolated CORE_FILES block and prove the repair occurred there,
    # not merely elsewhere in the verifier.
    core_start = text.index("CORE_FILES = (")
    core_end = text.index("\n)\n\nLINK_SURFACES", core_start)
    core = text[core_start:core_end]
    absent = [path for path in REQUIRED if f'    "{path}",' not in core]
    if absent:
        raise RuntimeError(f"scholarly files still absent from CORE_FILES: {absent}")

    PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
