# Accuracy Report

This repository currently ships with a deterministic MVP pipeline rather than a benchmarked production model. That means the current accuracy posture should be read as an implementation baseline, not a final performance claim.

## What Is Measured Today

- Artifact discovery is deterministic and reproducible.
- File hashing and previews are directly derived from source evidence.
- Findings are linked to supporting tool outputs.
- Oracle performs a simple support check before findings reach the report.

## Current Limitations

- The validator uses lexical support checks, not semantic contradiction analysis.
- Alfred wrappers currently parse simplified text exports rather than live SIFT tool output.
- No precision, recall, or false-positive metrics have been generated yet against the known-good datasets.

## Next Benchmark Steps

1. Execute `scripts/benchmark.sh`.
2. Compare JSON case output against `tests/known_good/`.
3. Record true positives, false positives, false negatives, and unsupported-but-plausible findings.
4. Expand Oracle validation rules before making accuracy claims in a submission.
