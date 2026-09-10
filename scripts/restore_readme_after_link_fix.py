from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
GOOD_COMMIT = "80ea03cf5501ee0945bd73eff30484a704a78416"

original = subprocess.check_output(
    ["git", "show", f"{GOOD_COMMIT}:README.md"],
    cwd=ROOT,
    text=True,
)
old = "[Quantum foundations atlas](docs/quantum_foundations_atlas.md)"
new = "[Quantum foundations and bridge test](docs/quantum_foundations_and_bridge_test.md)"
if original.count(old) != 1:
    raise RuntimeError(f"expected exactly one stale quantum link, found {original.count(old)}")
restored = original.replace(old, new, 1)
README.write_text(restored, encoding="utf-8")
