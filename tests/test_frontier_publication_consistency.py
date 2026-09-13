import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_current_frontier_publication_surfaces_are_consistent() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "verify_frontier_publication.py")],
        cwd=ROOT,
        check=True,
    )
