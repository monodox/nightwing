"""Nightwing performs deeper artifact-specific analysis."""

from __future__ import annotations

from nightwing.alfred.tools.disk import extract_mft_timeline, get_amcache
from nightwing.alfred.tools.logs import extract_syslog, parse_evtx
from nightwing.alfred.tools.memory import extract_processes, parse_volatility
from nightwing.alfred.tools.network import analyze_pcap, extract_connections
from nightwing.alfred.tools.prefetch import analyze_prefetch, get_shimcache
from nightwing.core.state import CaseState, Finding, MissionLogEntry, ToolExecution


def _tool_pair(category: str, path: str) -> list[ToolExecution]:
    if category == "disk":
        return [get_amcache(path), extract_mft_timeline(path)]
    if category == "memory":
        return [parse_volatility(path), extract_processes(path)]
    if category == "logs":
        return [parse_evtx(path), extract_syslog(path)]
    if category == "network":
        return [analyze_pcap(path), extract_connections(path)]
    if category == "prefetch":
        return [analyze_prefetch(path), get_shimcache(path)]
    return []


def run_analysis(state: CaseState) -> CaseState:
    for artifact in state.evidence:
        tools = _tool_pair(artifact.category, artifact.path)
        if not tools:
            continue
        summary = tools[0].summary
        state.findings.append(
            Finding(
                agent="nightwing",
                title=f"{artifact.category.title()} artifact reviewed: {artifact.name}",
                severity="medium",
                summary=summary,
                evidence_path=artifact.path,
                confidence=0.74,
                supporting_tools=tools,
                tags=[artifact.category, "read-only-analysis"],
            )
        )
    state.mission_log.append(
        MissionLogEntry(
            case_id=state.case_id,
            agent="nightwing",
            message="Completed artifact analysis.",
            details={"findings": len(state.findings)},
        )
    )
    return state
