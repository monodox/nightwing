from nightwing.core.state import Finding, ToolExecution
from nightwing.core.validator import validate_claim, validate_finding


def test_validate_claim_true():
    assert validate_claim("Successful logon", "zzz successful logon zzz") is True


def test_validate_finding_marks_supported_summary_verified():
    finding = Finding(
        agent="nightwing",
        title="Event review",
        severity="medium",
        summary="Successful logon observed in event output",
        evidence_path="C:/evidence/triage.evtx",
        supporting_tools=[
            ToolExecution(
                tool_name="logs.parse_evtx",
                artifact_path="C:/evidence/triage.evtx",
                summary="parsed",
                output={"events": [{"message": "Successful logon observed in event output"}]},
            )
        ],
    )
    validated = validate_finding(finding)
    assert validated.verified is True
