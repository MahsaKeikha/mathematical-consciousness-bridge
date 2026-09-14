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


if __name__ == "__main__":
    main()
