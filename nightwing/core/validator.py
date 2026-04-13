"""Hallucination detection placeholder."""


def validate_claim(claim: str, evidence: str) -> bool:
    return claim.lower() in evidence.lower()
