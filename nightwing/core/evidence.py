"""Read-only evidence mount handler placeholder."""

from pathlib import Path


def list_evidence(path: str) -> list:
    base = Path(path)
    if not base.exists():
        return []
    return [str(p) for p in base.iterdir()]
