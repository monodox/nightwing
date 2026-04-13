"""Log analysis tools placeholders."""


def parse_evtx(path: str) -> dict:
    return {"tool": "parse_evtx", "path": path}


def extract_syslog(path: str) -> list:
    return [{"tool": "extract_syslog", "path": path}]
