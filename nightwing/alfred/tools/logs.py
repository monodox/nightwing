"""Typed wrappers for Windows event and syslog-style artifacts."""

from __future__ import annotations

from pathlib import Path

from nightwing.alfred.parsers.evtx import parse_evtx_lines
from nightwing.core.state import ToolExecution


def parse_evtx(path: str) -> ToolExecution:
    artifact = Path(path)
    lines = artifact.read_text(encoding="utf-8", errors="replace").splitlines()[:50]
    events = parse_evtx_lines(lines)
    return ToolExecution(
        tool_name="logs.parse_evtx",
        artifact_path=str(artifact),
        summary=f"Parsed {len(events)} event records.",
        output={"events": events[:10]},
    )


def extract_syslog(path: str) -> ToolExecution:
    artifact = Path(path)
    lines = artifact.read_text(encoding="utf-8", errors="replace").splitlines()[:25]
    return ToolExecution(
        tool_name="logs.extract_syslog",
        artifact_path=str(artifact),
        summary=f"Collected {len(lines)} syslog lines.",
        output={"lines": lines},
    )
