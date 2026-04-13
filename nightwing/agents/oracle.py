"""Oracle validates findings against raw tool output."""

from __future__ import annotations

from nightwing.core.corrector import correct_output
from nightwing.core.state import CaseState, MissionLogEntry
from nightwing.core.validator import validate_finding


def validate_findings(state: CaseState) -> CaseState:
    state.findings = [validate_finding(finding) for finding in state.findings]
    state.findings = correct_output(state.findings)
    state.mission_log.append(
        MissionLogEntry(
            case_id=state.case_id,
            agent="oracle",
            message="Validated findings against supporting tool output.",
            details={
                "verified": sum(1 for finding in state.findings if finding.verified),
                "needs_review": sum(1 for finding in state.findings if not finding.verified),
            },
        )
    )
    return state
