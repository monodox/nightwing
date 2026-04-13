"""Typed wrappers for simplified prefetch and shimcache artifacts."""

from __future__ import annotations

from pathlib import Path

from nightwing.core.state import ToolExecution


def analyze_prefetch(path: str) -> ToolExecution:
    artifact = Path(path)
    lines = artifact.read_text(encoding="utf-8", errors="replace").splitlines()[:25]
    executed = [line for line in lines if "exe" in line.lower()]
    return ToolExecution(
        tool_name="prefetch.analyze_prefetch",
        artifact_path=str(artifact),
        summary=f"Observed {len(executed)} executable references in prefetch data.",
        output={"executables": executed[:10]},
    )


def get_shimcache(path: str) -> ToolExecution:
    artifact = Path(path)
    lines = artifact.read_text(encoding="utf-8", errors="replace").splitlines()[:25]
    return ToolExecution(
        tool_name="prefetch.get_shimcache",
        artifact_path=str(artifact),
        summary=f"Collected {len(lines)} shimcache lines.",
        output={"entries": lines},
    )
