"""Mission log JSONL writer."""

from __future__ import annotations

from pathlib import Path

from nightwing.core.state import MissionLogEntry


def append_log(entry: MissionLogEntry, log_file: str) -> None:
    path = Path(log_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(entry.model_dump_json() + "\n")
