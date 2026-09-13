"""Repair source-level contracts used by the layered P88 publication migration.

This script is deliberately narrow, deterministic, and idempotent. It repairs
historical migration templates that encoded monolithic-README assumptions and
updates the canonical P88 Research Map block so publication regeneration cannot
silently discard its proof/provenance/code/test audit path.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def _write(relative: str, text: str) -> None:
    path = ROOT / relative
    normalized = text.rstrip() + "\n"
    if path.read_text(encoding="utf-8") != normalized:
        path.write_text(normalized, encoding="utf-8")


def _replace_once(text: str, old: str, new: str, *, label: str) -> str:
    # Check the historical form first. Some repaired blocks are strict prefixes
    # of the historical block, so checking `new in text` first can incorrectly
    # treat an unrepaired source as already migrated.
    if old in text:
        return text.replace(old, new, 1)
    if new in text:
        return text
    raise RuntimeError(f"repair anchor missing: {label}")


def repair_migration_generator() -> None:
    relative = "scripts/migrate_layered_publication_tests.py"
    text = _read(relative)

    text = _replace_once(
        text,
        '    combined = "\\n".join((proof, provenance, source)).lower()',
        '    combined = "\\\\n".join((proof, provenance, source)).lower()',
        label="frontier integration newline escaping",
    )

    text = _replace_once(
        text,
        '''    for number in range(1, 89):
        assert f"proposition_{number}_" in record''',
        '''    assert "Complete P1 to P88 chronology" in record
    for number in range(1, 89):
        proofs = list((ROOT / "docs").glob(f"proposition_{number}_*.md"))
        assert len(proofs) == 1, number''',
        label="archive completeness assertion",
    )

    text = _replace_once(
        text,
        '''        assert len(proofs) == 1
        assert figures
        assert proofs[0].name in record
    for proposition in range(61, 71):''',
        '''        assert len(proofs) == 1
        assert figures
    assert "Complete P1 to P88 chronology" in record
    for proposition in range(61, 71):''',
        label="historical theorem archive layering",
    )

    old_fundamental = '''    for phrase in (
        "There is currently no experimentally established Theory of Everything",
        "T(\\\\Omega)=\\\\bigl(G(\\\\Omega),Q(\\\\Omega),C(\\\\Omega)\\\\bigr)",
        "fundamental_theory_consciousness_map.svg",
    ):
        assert phrase in program'''
    intermediate_fundamental = '''    for phrase in (
        "There is currently no experimentally established Theory of Everything",
        "T(\\\\Omega)=\\\\bigl(G(\\\\Omega),Q(\\\\Omega),C(\\\\Omega)\\\\bigr)",
        "fundamental_theory_consciousness_map.svg",
    ):
        assert phrase in program.replace("**", "")'''
    new_fundamental = '''    for phrase in (
        "There is currently no experimentally established Theory of Everything",
        "T(\\\\Omega)=\\\\bigl(G(\\\\Omega),Q(\\\\Omega),C(\\\\Omega)\\\\bigr)",
    ):
        assert phrase in program.replace("**", "")
    assert MAP.is_file()'''
    if old_fundamental in text:
        text = text.replace(old_fundamental, new_fundamental, 1)
    elif intermediate_fundamental in text:
        text = text.replace(intermediate_fundamental, new_fundamental, 1)
    elif new_fundamental not in text:
        raise RuntimeError("repair anchor missing: fundamental-theory interface test")

    text = _replace_once(
        text,
        '''    assert "# 0.{number}.0" in changelog
    assert "Proposition {number}" in changelog''',
        '''    assert "# 0.{number}.0" in changelog''',
        label="versioned release-history assertion",
    )

    _write(relative, text)


def repair_p88_promoter() -> None:
    relative = "scripts/promote_p88_public_frontier.py"
    text = _read(relative)

    text = _replace_once(
        text,
        '''The complete family contains 632 sign-normalized coefficient patterns per four-event subset and 208,560 exact functionals. On the established rational witness it strictly improves the certified full-law bound from L87 = 1/96 to L88 = 1/64.</p></article>''',
        '''The complete family contains 632 sign-normalized coefficient patterns per four-event subset and 208,560 exact functionals. On the established rational witness it strictly improves the certified full-law bound through <strong>L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64</strong>.</p></article>''',
        label="P88 Research Map exact hierarchy",
    )

    text = _replace_once(
        text,
        '''<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROOF}">Read Proposition 88</a></div></div></section>''',
        '''<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROOF}">Read Proposition 88</a></div></div><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{P88_PROVENANCE}">Audit P88 provenance</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{P88_IMPLEMENTATION}">implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{P88_TEST}">exact tests</a> · <a href="index.html#p88-frontier">current-frontier overview</a></p></section>''',
        label="P88 Research Map audit path",
    )

    _write(relative, text)


def main() -> None:
    repair_migration_generator()
    repair_p88_promoter()
    print("Repaired layered publication source contracts")


if __name__ == "__main__":
    main()
