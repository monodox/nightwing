"""Case file writers for Markdown and JSON output."""

from __future__ import annotations

import json
from pathlib import Path

from nightwing.core.state import CaseState


def write_casefile(case_state: CaseState, out_dir: str) -> tuple[Path, Path]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    markdown_path = out / f"{case_state.case_id}.md"
    json_path = out / f"{case_state.case_id}.json"

    markdown_path.write_text(case_state.narrative, encoding="utf-8")
    json_path.write_text(
        json.dumps(case_state.model_dump(mode="json"), indent=2),
        encoding="utf-8",
    )
    return markdown_path, json_path
