"""Configuration loader for Nightwing."""

from pydantic import BaseModel
from dotenv import load_dotenv
import os


class Settings(BaseModel):
    model: str = "gpt-4o-mini"
    evidence_path: str = "./evidence"
    mission_log_path: str = "./logs/mission_logs"
    case_file_path: str = "./logs/case_files"


def get_settings() -> Settings:
    load_dotenv()
    return Settings(
        model=os.getenv("NIGHTWING_MODEL", "gpt-4o-mini"),
        evidence_path=os.getenv("EVIDENCE_PATH", "./evidence"),
        mission_log_path=os.getenv("MISSION_LOG_PATH", "./logs/mission_logs"),
        case_file_path=os.getenv("CASE_FILE_PATH", "./logs/case_files"),
    )
