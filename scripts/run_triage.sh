#!/usr/bin/env bash
set -euo pipefail

CASE_ID="${1:-demo-case}"
EVIDENCE_PATH="${2:-./evidence}"

python -m nightwing.main run --case-id "$CASE_ID" --evidence-path "$EVIDENCE_PATH"
