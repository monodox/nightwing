# Nightwing

Nightwing is an autonomous incident response agent built for the SANS SIFT Workstation. It is designed to help defenders investigate evidence with the speed of automation while preserving the skepticism, traceability, and discipline expected from a senior forensic analyst.

The system is organized around four agents:

- `Robin` triages evidence and maps the initial investigation surface.
- `Nightwing` performs deeper artifact-specific analysis.
- `Oracle` validates every finding against raw tool output to reduce hallucinations.
- `Report Agent` assembles the final case narrative and mission log.

Alfred exposes the forensic tooling layer through safe, typed, read-only wrappers. In this MVP repository, Alfred operates as a deterministic manifest plus wrappers that inspect evidence without any write-paths or destructive commands.

## Quick Start

1. Copy `.env.example` to `.env`.
2. Install dependencies.

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. Place sample evidence under `./evidence`.
4. Run Nightwing.

```bash
python -m nightwing.main run --case-id demo-case
```

## Outputs

- Markdown case reports are written to `logs/case_files/<case-id>.md`
- JSON case reports are written to `logs/case_files/<case-id>.json`
- Mission logs are written to `logs/mission_logs/<case-id>.jsonl`

## Trust Boundary

- Evidence discovery is read-only.
- Alfred wrappers only read local files and return typed structured output.
- Every finding carries the exact tool executions that produced it.
- Oracle marks unsupported summaries for analyst review before reporting.

## Testing

```bash
pytest -q
```
