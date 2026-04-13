"""Parses line-based volatility command output."""

from __future__ import annotations


def parse_volatility_lines(lines: list[str]) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for raw_line in lines:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [part.strip() for part in line.split("|")]
        if len(parts) < 2:
            continue
        records.append(
            {
                "process": parts[0],
                "pid": parts[1],
                "details": " | ".join(parts[2:]),
            }
        )
    return records
