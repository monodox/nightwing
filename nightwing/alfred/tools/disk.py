"""Disk forensics tools placeholders."""


def get_amcache(path: str) -> dict:
    return {"tool": "get_amcache", "path": path}


def extract_mft_timeline(path: str) -> list:
    return [{"tool": "extract_mft_timeline", "path": path}]
