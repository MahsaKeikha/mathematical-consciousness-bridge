from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from verify_reader_linkability import verify_reader_linkability


def test_reader_linkability_contract() -> None:
    verify_reader_linkability()
