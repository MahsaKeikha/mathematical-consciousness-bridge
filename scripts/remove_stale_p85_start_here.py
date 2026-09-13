"""Remove the obsolete duplicate P85 current-frontier block from Start Here."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    start_path = ROOT / "website" / "start-here.html"
    start = start_path.read_text(encoding="utf-8")
    stale_section = '''  <section class="theorem-frontier"><div class="section-head"><p class="eyebrow">Current frontier · P85</p><h2>P85 exact three-event shared-parameter certificate</h2><p>P85 asks whether three canonical parity observations can share one P75 parameter assignment when lower-order certificates remain silent. The exact witness gives P84 = 0 and P85 = 1/32.</p></div><p>This is a conditional model-separation theorem and does not claim that consciousness has been derived from physics. The physical-to-experiential bridge remains open.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_85_exact_triple_projection_parity_functional.md">Read P85</a> · <a href="visual-atlas.html">Visual Atlas</a> · <a href="research-map.html">Research Map</a></p></section>\n'''
    if stale_section in start:
        start = start.replace(stale_section, "", 1)
    if "Current frontier · P85" in start:
        raise RuntimeError("stale P85 current-frontier block remains in Start Here")
    if start.count("P86 is the current exact frontier.") != 1:
        raise RuntimeError("Start Here must expose exactly one P86 current-frontier statement")
    start_path.write_text(start, encoding="utf-8")

    test_path = ROOT / "tests" / "test_reader_experience.py"
    test = test_path.read_text(encoding="utf-8")
    stale_anchor = '        "<strong>85</strong><span>proposition-level results</span>",\n'
    stale_marker = '        "Current frontier · P85",\n'
    if stale_marker not in test:
        if stale_anchor not in test:
            raise RuntimeError("reader stale-token anchor missing")
        test = test.replace(stale_anchor, stale_marker + stale_anchor, 1)
    p86_assert = '    assert "P86 is the current exact frontier." in start\n'
    no_p85_assert = '    assert "Current frontier · P85" not in start\n'
    if no_p85_assert not in test:
        if p86_assert not in test:
            raise RuntimeError("reader P86 assertion anchor missing")
        test = test.replace(p86_assert, p86_assert + no_p85_assert, 1)
    test_path.write_text(test, encoding="utf-8")

    verifier_path = ROOT / "scripts" / "verify_repository.py"
    verifier = verifier_path.read_text(encoding="utf-8")
    verifier_anchor = '    "<strong>85</strong><span>proposition-level results</span>",\n'
    verifier_marker = '    "Current frontier · P85",\n'
    if verifier_marker not in verifier:
        if verifier_anchor not in verifier:
            raise RuntimeError("verifier stale-token anchor missing")
        verifier = verifier.replace(verifier_anchor, verifier_marker + verifier_anchor, 1)
    verifier_path.write_text(verifier, encoding="utf-8")


if __name__ == "__main__":
    main()
