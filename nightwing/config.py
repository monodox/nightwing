"""Runtime configuration for Nightwing."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel, Field


class Settings(BaseModel):
    model: str = "gpt-5.4-mini"
    evidence_path: Path = Path("./evidence")
    mission_log_path: Path = Path("./logs/mission_logs")
    case_file_path: Path = Path("./logs/case_files")
    allowed_extensions: tuple[str, ...] = Field(
        default=(
            ".txt",
            ".json",
            ".jsonl",
            ".log",
            ".evtx",
            ".csv",
            ".pcap",
            ".pf",
            ".mft",
            ".mem",
            ".img",
            ".dd",
        )
    )


def get_settings() -> Settings:
    load_dotenv()
    return Settings(
        model=os.getenv("NIGHTWING_MODEL", "gpt-5.4-mini"),
        evidence_path=Path(os.getenv("EVIDENCE_PATH", "./evidence")),
        mission_log_path=Path(os.getenv("MISSION_LOG_PATH", "./logs/mission_logs")),
        case_file_path=Path(os.getenv("CASE_FILE_PATH", "./logs/case_files")),
    )
