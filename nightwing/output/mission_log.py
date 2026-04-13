"""Mission log JSONL writer placeholder."""

import json
from pathlib import Path


def append_log(entry: dict, log_file: str) -> None:
    path = Path(log_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
