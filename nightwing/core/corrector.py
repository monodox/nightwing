"""Simple correction helpers for unsupported findings."""

from __future__ import annotations

from nightwing.core.state import Finding


def correct_output(findings: list[Finding]) -> list[Finding]:
    corrected: list[Finding] = []
    for finding in findings:
        if finding.verified:
            corrected.append(finding)
            continue
        finding.summary = f"{finding.summary} [Needs analyst review]"
        finding.severity = "low"
        corrected.append(finding)
    return corrected
