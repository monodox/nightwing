"""Robin performs initial triage across all evidence artifacts."""

from __future__ import annotations

from nightwing.core.state import CaseState, MissionLogEntry


def run_triage(state: CaseState) -> CaseState:
    state.triage_notes = [
        f"Robin identified {item.category} artifact {item.name} ({item.size_bytes} bytes)."
        for item in state.evidence
    ]
    state.mission_log.append(
        MissionLogEntry(
            case_id=state.case_id,
            agent="robin",
            message="Completed evidence survey.",
            details={"artifacts": len(state.evidence)},
        )
    )
    return state
