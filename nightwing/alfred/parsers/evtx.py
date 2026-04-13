"""Parses line-based Windows event exports into structured records."""

from __future__ import annotations


def parse_evtx_lines(lines: list[str]) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        parts = [part.strip() for part in line.split("|")]
        if len(parts) < 3:
            continue
        records.append(
            {
                "timestamp": parts[0],
                "event_id": parts[1],
                "message": " | ".join(parts[2:]),
            }
        )
    return records
