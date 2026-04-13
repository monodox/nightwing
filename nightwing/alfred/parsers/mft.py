"""Small text parser for simplified MFT-style timeline exports."""

from __future__ import annotations


def parse_mft_lines(lines: list[str]) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for line in lines:
        if "|" not in line:
            continue
        timestamp, path, *rest = [part.strip() for part in line.split("|")]
        records.append(
            {
                "timestamp": timestamp,
                "path": path,
                "details": " | ".join(rest),
            }
        )
    return records
