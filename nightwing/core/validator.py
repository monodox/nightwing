"""Validation helpers that reduce unsupported claims before reporting."""

from __future__ import annotations

from nightwing.core.state import Finding


def validate_claim(claim: str, evidence: str) -> bool:
    normalized_claim = [token for token in claim.lower().split() if len(token) > 3]
    evidence_text = evidence.lower()
    return any(token in evidence_text for token in normalized_claim)


def validate_finding(finding: Finding) -> Finding:
    combined_output = " ".join(
        str(tool.output) for tool in finding.supporting_tools
    )
    is_supported = validate_claim(finding.summary, combined_output)
    finding.verified = is_supported
    note = (
        "Oracle confirmed supporting tool output matched the summary."
        if is_supported
        else "Oracle could not find sufficient support in raw tool output."
    )
    finding.verification_notes.append(note)
    return finding
