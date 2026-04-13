"""Typed disk forensics wrappers backed by read-only file inspection."""

from __future__ import annotations

from pathlib import Path

from nightwing.alfred.parsers.mft import parse_mft_lines
from nightwing.core.state import ToolExecution


def get_amcache(path: str) -> ToolExecution:
    artifact = Path(path)
    preview = artifact.read_text(encoding="utf-8", errors="replace").splitlines()[:10]
    return ToolExecution(
        tool_name="disk.get_amcache",
        artifact_path=str(artifact),
        summary=f"Collected {len(preview)} preview lines from potential Amcache artifact.",
        output={"preview": preview},
    )


def extract_mft_timeline(path: str) -> ToolExecution:
    artifact = Path(path)
    lines = artifact.read_text(encoding="utf-8", errors="replace").splitlines()[:50]
    timeline = parse_mft_lines(lines)
    return ToolExecution(
        tool_name="disk.extract_mft_timeline",
        artifact_path=str(artifact),
        summary=f"Parsed {len(timeline)} simplified MFT timeline entries.",
        output={"timeline": timeline[:10]},
    )
