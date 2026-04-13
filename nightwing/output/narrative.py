"""Narrative rendering for human-readable case reports."""

from __future__ import annotations

from nightwing.core.state import CaseState


def render_narrative(state: CaseState) -> str:
    lines = [
        f"Case `{state.case_id}` opened against evidence root `{state.evidence_root}`.",
        f"Robin surveyed {len(state.evidence)} artifacts before Nightwing deep-dived the flagged material.",
    ]
    if not state.findings:
        lines.append("No findings were produced from the available evidence.")
        return "\n".join(lines)

    lines.append("Findings:")
    for finding in state.findings:
        status = "verified" if finding.verified else "needs review"
        lines.append(
            f"- [{finding.severity}/{status}] {finding.title}: {finding.summary}"
        )
    return "\n".join(lines)
