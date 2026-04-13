from pathlib import Path

import pytest


@pytest.fixture()
def sample_evidence_dir(tmp_path: Path) -> Path:
    (tmp_path / "triage.evtx").write_text(
        "2026-04-13T09:10:00Z|4624|Successful logon for analyst\n",
        encoding="utf-8",
    )
    (tmp_path / "memory.mem").write_text(
        "powershell.exe|444|EncodedCommand present\n",
        encoding="utf-8",
    )
    (tmp_path / "traffic.pcap").write_text(
        "10.0.0.2:51515 -> 8.8.8.8:53 dns query\n",
        encoding="utf-8",
    )
    return tmp_path
