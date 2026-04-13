from nightwing.agents.graph import run_case
from nightwing.core.evidence import list_evidence
from nightwing.core.state import CaseState
from nightwing.agents.robin import run_triage


def test_robin_triage(sample_evidence_dir):
    state = CaseState(
        case_id="case-1",
        evidence_root=str(sample_evidence_dir),
        evidence=list_evidence(sample_evidence_dir),
    )
    result = run_triage(state)
    assert len(result.triage_notes) == 3


def test_full_pipeline_writes_report(sample_evidence_dir, monkeypatch, tmp_path):
    monkeypatch.setenv("CASE_FILE_PATH", str(tmp_path / "case_files"))
    monkeypatch.setenv("MISSION_LOG_PATH", str(tmp_path / "mission_logs"))
    state = run_case("case-2", str(sample_evidence_dir))
    assert state.report_markdown_path is not None
    assert state.report_json_path is not None
    assert len(state.findings) == 3
