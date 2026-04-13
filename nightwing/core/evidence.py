"""Evidence discovery utilities that never mutate source material."""

from __future__ import annotations

import hashlib
from pathlib import Path

from nightwing.config import get_settings
from nightwing.core.state import EvidenceRecord


def mount_evidence(path: str | Path) -> Path:
    """Resolve and validate the evidence root as an existing directory."""

    evidence_root = Path(path).resolve()
    if not evidence_root.exists():
        raise FileNotFoundError(f"Evidence path does not exist: {evidence_root}")
    if not evidence_root.is_dir():
        raise NotADirectoryError(f"Evidence path must be a directory: {evidence_root}")
    return evidence_root


def _hash_file(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def _preview_lines(path: Path, limit: int = 5) -> list[str]:
    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            return [line.strip() for _, line in zip(range(limit), handle) if line.strip()]
    except OSError:
        return []


def classify_artifact(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".mft", ".img", ".dd"}:
        return "disk"
    if suffix in {".mem", ".raw"}:
        return "memory"
    if suffix in {".evtx", ".log"}:
        return "logs"
    if suffix in {".pcap", ".pcapng"}:
        return "network"
    if suffix in {".pf"}:
        return "prefetch"
    return "other"


def list_evidence(path: str | Path) -> list[EvidenceRecord]:
    """Return structured evidence metadata for all allowed files."""

    evidence_root = mount_evidence(path)
    settings = get_settings()
    records: list[EvidenceRecord] = []
    for artifact in sorted(p for p in evidence_root.rglob("*") if p.is_file()):
        if artifact.name.startswith("."):
            continue
        if artifact.suffix and artifact.suffix.lower() not in settings.allowed_extensions:
            continue
        records.append(
            EvidenceRecord(
                path=str(artifact),
                name=artifact.name,
                category=classify_artifact(artifact),
                size_bytes=artifact.stat().st_size,
                sha256=_hash_file(artifact),
                preview=_preview_lines(artifact),
            )
        )
    return records
