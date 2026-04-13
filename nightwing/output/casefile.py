"""Case file generator placeholder."""

import json
from pathlib import Path


def write_casefile(case_id: str, data: dict, out_dir: str) -> Path:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{case_id}.json"
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path
