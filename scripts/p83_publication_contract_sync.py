"""One-shot synchronization of the remaining P83 publication-contract gaps."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, path: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected one anchor in {path}, found {count}: {old[:100]!r}")
    return text.replace(old, new, 1)


def sync_readme() -> None:
    path = "README.md"
    text = read(path)
    sentence = "Read the complete P1 to P83 detailed proposition record"
    if sentence not in text:
        anchor = "| Physical-to-experiential bridge | **Open** |\n"
        addition = (
            anchor
            + "\n"
            + "Read the complete P1 to P83 detailed proposition record in "
            + "[docs/detailed_proposition_record.md](docs/detailed_proposition_record.md) "
            + "for proposition-by-proposition assumptions, statements, proofs, implementations, tests, and scientific boundaries.\n"
        )
        text = replace_once(text, anchor, addition, path)
        write(path, text)


def sync_source_boundary() -> None:
    path = "src/consciousness_bridge/projection_parity_model_separation.py"
    text = read(path)
    old = (
        "This certificate does not validate the P75 model, does not identify a latent\n"
        "state with consciousness, and does not close the physical-to-experiential bridge."
    )
    new = (
        "This certificate does not validate the P75 model, does not identify a latent state with consciousness,\n"
        "and does not close the physical-to-experiential bridge."
    )
    if "identify a latent state with consciousness" not in text:
        text = replace_once(text, old, new, path)
        write(path, text)


def sync_research_map() -> None:
    path = "website/research-map.html"
    text = read(path)
    if "p82_equation_provenance.md" not in text:
        old = (
            '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/'
            'docs/proposition_82_exact_nested_projection_contrast.md">Open P82 →</a></article>'
        )
        new = (
            '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/'
            'docs/proposition_82_exact_nested_projection_contrast.md">Open P82 →</a> '
            '<a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/'
            'docs/p82_equation_provenance.md">Audit P82 provenance →</a></article>'
        )
        text = replace_once(text, old, new, path)
        write(path, text)


def restore_v082_changelog() -> None:
    path = "CHANGELOG.md"
    text = read(path)
    if "# 0.82.0 - 2026-09-12" in text:
        return
    marker = "# 0.81.0 - 2026-09-11"
    section = """# 0.82.0 - 2026-09-12

- Added Proposition 82, Exact Nested Projection-Contrast Certificate for Continuous P75 Separation.
- Added 256 genuinely new nested residual-event contrasts while retaining every P81 projection-event lower bound.
- Computed residual-event parameter-box ranges directly from the common P75 latent-branch factorization rather than subtracting separate P81 intervals.
- Defined `L82(B) = max(L81(B), L_nested(B))`, establishing `L82 >= L81 >= L80 >= L78` on every parameter box.
- Added an exact-rational strict-improvement witness with `L80=0`, `L81=1/16`, and `L82=1/12`.
- Preserved the proved P78 mesh-width upper certificate and the P79 one-sided exact-rational sampling-radius rejection gate.
- Added exact implementation, regression tests, proof, equation provenance, theorem figure, reader navigation, website integration, and archival release documentation.
- Published v0.82.0 with 82 proposition-level results, 70 paper-facing equation-driven figures, and 140 SVG assets in the complete visual record.
- Preserved the interpretation boundary that P82 is a conditional model-distance theorem and does not identify a latent state with consciousness or close the physical-to-experiential bridge.

"""
    text = replace_once(text, marker, section + marker, path)
    write(path, text)


def main() -> None:
    sync_readme()
    sync_source_boundary()
    sync_research_map()
    restore_v082_changelog()

    required = {
        "README.md": "Read the complete P1 to P83 detailed proposition record",
        "src/consciousness_bridge/projection_parity_model_separation.py": "identify a latent state with consciousness",
        "website/research-map.html": "p82_equation_provenance.md",
        "CHANGELOG.md": "# 0.82.0 - 2026-09-12",
    }
    for path, token in required.items():
        if token not in read(path):
            raise RuntimeError(f"publication token missing after sync: {path}: {token}")
    print("P83 publication contract synchronized")


if __name__ == "__main__":
    main()
