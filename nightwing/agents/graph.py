"""Sequential state graph for the Nightwing investigation pipeline."""

from __future__ import annotations

from nightwing.agents.nightwing import run_analysis
from nightwing.agents.oracle import validate_findings
from nightwing.agents.reporter import build_report
from nightwing.agents.robin import run_triage
from nightwing.config import get_settings
from nightwing.core.evidence import list_evidence
from nightwing.core.state import CaseState
from nightwing.output.mission_log import append_log


def build_graph() -> dict:
    return {
        "nodes": ["robin", "nightwing", "oracle", "reporter"],
        "edges": [
            ("robin", "nightwing"),
            ("nightwing", "oracle"),
            ("oracle", "reporter"),
        ],
    }


def run_case(case_id: str, evidence_root: str) -> CaseState:
    settings = get_settings()
    state = CaseState(
        case_id=case_id,
        evidence_root=evidence_root,
        evidence=list_evidence(evidence_root),
    )
    for step in (run_triage, run_analysis, validate_findings, build_report):
        state = step(state)
    log_path = settings.mission_log_path / f"{case_id}.jsonl"
    for entry in state.mission_log:
        append_log(entry, str(log_path))
    return state
