"""Narrative writer placeholder."""


def render_narrative(findings: list) -> str:
    return "\n".join(f"- {item}" for item in findings)
