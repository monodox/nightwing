from nightwing.alfred.server import create_server
from nightwing.alfred.tools.logs import parse_evtx


def test_create_server_ready():
    result = create_server()
    assert result["status"] == "ready"
    assert result["mode"] == "read-only"


def test_parse_evtx_returns_tool_execution(sample_evidence_dir):
    result = parse_evtx(str(sample_evidence_dir / "triage.evtx"))
    assert result.tool_name == "logs.parse_evtx"
    assert result.output["events"][0]["event_id"] == "4624"
