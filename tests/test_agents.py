from nightwing.agents.robin import run_triage


def test_robin_triage():
    result = run_triage({"hello": "world"})
    assert result["status"] == "triaged"
