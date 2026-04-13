"""Report agent that assembles final narrative and artifacts."""

from __future__ import annotations

from nightwing.config import get_settings
from nightwing.core.state import CaseState, MissionLogEntry
from nightwing.output.casefile import write_casefile
from nightwing.output.narrative import render_narrative


def build_report(state: CaseState) -> CaseState:
    settings = get_settings()
    state.narrative = render_narrative(state)
    state.mission_log.append(
        MissionLogEntry(
            case_id=state.case_id,
            agent="reporter",
            message="Generated case report artifacts.",
            details={},
        )
    )
    markdown_path, json_path = write_casefile(state, str(settings.case_file_path))
    state.report_markdown_path = str(markdown_path)
    state.report_json_path = str(json_path)
    state.mission_log[-1].details = {
        "markdown_path": state.report_markdown_path,
        "json_path": state.report_json_path,
    }
    return state
