"""Shared state and typed records for the Nightwing investigation flow."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field


class EvidenceRecord(BaseModel):
    """Represents a single read-only evidence artifact."""

    path: str
    name: str
    category: Literal["disk", "memory", "logs", "network", "prefetch", "other"]
    size_bytes: int
    sha256: str
    preview: list[str] = Field(default_factory=list)


class ToolExecution(BaseModel):
    """Captures an Alfred tool call and the evidence it inspected."""

    tool_name: str
    artifact_path: str
    summary: str
    output: dict[str, Any] = Field(default_factory=dict)
    executed_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


class Finding(BaseModel):
    """A forensic observation produced by an agent."""

    agent: str
    title: str
    severity: Literal["low", "medium", "high"]
    summary: str
    evidence_path: str
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)
    supporting_tools: list[ToolExecution] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    verified: bool = False
    verification_notes: list[str] = Field(default_factory=list)


class MissionLogEntry(BaseModel):
    """Structured mission log line for auditability."""

    case_id: str
    agent: str
    message: str
    details: dict[str, Any] = Field(default_factory=dict)
    timestamp: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class CaseState(BaseModel):
    """Full workflow state passed across the Nightwing pipeline."""

    case_id: str
    evidence_root: str
    started_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    evidence: list[EvidenceRecord] = Field(default_factory=list)
    triage_notes: list[str] = Field(default_factory=list)
    findings: list[Finding] = Field(default_factory=list)
    mission_log: list[MissionLogEntry] = Field(default_factory=list)
    narrative: str = ""
    report_markdown_path: str | None = None
    report_json_path: str | None = None

    def resolved_root(self) -> Path:
        return Path(self.evidence_root).resolve()
