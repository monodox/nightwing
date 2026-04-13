"""Typed memory-analysis wrappers backed by safe local reads."""

from __future__ import annotations

from pathlib import Path

from nightwing.alfred.parsers.volatility import parse_volatility_lines
from nightwing.core.state import ToolExecution


def parse_volatility(path: str) -> ToolExecution:
    artifact = Path(path)
    lines = artifact.read_text(encoding="utf-8", errors="replace").splitlines()[:50]
    records = parse_volatility_lines(lines)
    return ToolExecution(
        tool_name="memory.parse_volatility",
        artifact_path=str(artifact),
        summary=f"Parsed {len(records)} volatility-style rows.",
        output={"records": records[:10]},
    )


def extract_processes(path: str) -> ToolExecution:
    parsed = parse_volatility(path)
    processes = [
        {"process": record["process"], "pid": record["pid"]}
        for record in parsed.output.get("records", [])
    ]
    return ToolExecution(
        tool_name="memory.extract_processes",
        artifact_path=parsed.artifact_path,
        summary=f"Extracted {len(processes)} process candidates.",
        output={"processes": processes},
    )
