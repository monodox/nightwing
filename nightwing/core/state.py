"""LangGraph state schema placeholder."""

from typing import TypedDict, List


class CaseState(TypedDict, total=False):
    case_id: str
    evidence_files: List[str]
    findings: List[dict]
