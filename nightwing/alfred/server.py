"""Alfred MCP-like manifest for safe, typed, read-only tools."""

from __future__ import annotations


def create_server() -> dict:
    tools = {
        "disk": ["get_amcache", "extract_mft_timeline"],
        "memory": ["parse_volatility", "extract_processes"],
        "logs": ["parse_evtx", "extract_syslog"],
        "network": ["analyze_pcap", "extract_connections"],
        "prefetch": ["analyze_prefetch", "get_shimcache"],
    }
    return {
        "name": "alfred",
        "status": "ready",
        "mode": "read-only",
        "description": "Safe typed wrappers around forensic tooling with no destructive commands.",
        "tools": tools,
    }
