"""Typed wrappers for safe PCAP-derived text summaries."""

from __future__ import annotations

from pathlib import Path

from nightwing.core.state import ToolExecution


def analyze_pcap(path: str) -> ToolExecution:
    artifact = Path(path)
    lines = artifact.read_text(encoding="utf-8", errors="replace").splitlines()[:50]
    suspicious = [line for line in lines if any(token in line.lower() for token in ("443", "8080", "dns", "http"))]
    return ToolExecution(
        tool_name="network.analyze_pcap",
        artifact_path=str(artifact),
        summary=f"Reviewed {len(lines)} network-summary lines and flagged {len(suspicious)} notable entries.",
        output={"lines": lines[:10], "suspicious": suspicious[:10]},
    )


def extract_connections(path: str) -> ToolExecution:
    artifact = Path(path)
    lines = artifact.read_text(encoding="utf-8", errors="replace").splitlines()[:50]
    connections = []
    for line in lines:
        if "->" in line:
            source, destination = [part.strip() for part in line.split("->", 1)]
            connections.append({"source": source, "destination": destination})
    return ToolExecution(
        tool_name="network.extract_connections",
        artifact_path=str(artifact),
        summary=f"Extracted {len(connections)} connection records.",
        output={"connections": connections[:10]},
    )
