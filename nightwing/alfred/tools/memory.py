"""Memory forensics tools placeholders."""


def parse_volatility(path: str) -> dict:
    return {"tool": "parse_volatility", "path": path}


def extract_processes(path: str) -> list:
    return [{"tool": "extract_processes", "path": path}]
