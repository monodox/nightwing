# Architecture

Nightwing is structured as a four-stage investigative pipeline that runs entirely inside a controlled forensic environment.

## Components

- `nightwing/main.py` is the CLI entry point used by investigators and judges.
- `nightwing/agents/graph.py` orchestrates the pipeline from triage to reporting.
- `nightwing/core/state.py` defines the typed case state, findings, tool executions, and mission logs.
- `nightwing/core/evidence.py` performs evidence discovery and hashing without mutating source material.
- `nightwing/alfred/` contains the safe tooling facade. Its wrappers expose typed, read-only access patterns rather than raw shell execution.
- `nightwing/output/` renders the final report and writes durable case artifacts.

## Agent Roles

### Robin

Robin performs the first sweep of the evidence set. It inventories artifacts, groups them by category, and records triage notes that establish the initial investigative surface.

### Nightwing

Nightwing performs the deeper forensic pass. It chooses the matching Alfred wrappers for each artifact category and produces structured findings with supporting tool execution records.

### Oracle

Oracle acts as the trust boundary inside the agent pipeline. It validates Nightwing's summaries against raw tool output and downgrades unsupported statements for analyst review.

### Report Agent

The reporting stage compiles the validated findings into a concise narrative, serializes the full case state to JSON, and writes an audit-friendly mission log.

## Trust Boundary

The central design principle is that evidence safety is enforced structurally, not by convention.

- Evidence is only discovered and read from disk.
- Alfred does not expose write, delete, or modify operations.
- Findings remain linked to supporting tool executions.
- Validation happens before the report is finalized.

## Data Flow

1. The investigator points Nightwing at an evidence directory.
2. Evidence metadata is collected, hashed, and previewed.
3. Robin records the initial triage survey.
4. Nightwing invokes category-specific Alfred wrappers.
5. Oracle validates each finding against supporting tool output.
6. Reporter writes Markdown, JSON, and JSONL outputs for review and audit.
