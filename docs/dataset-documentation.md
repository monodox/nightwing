# Dataset Documentation

Nightwing is intended to run against investigator-supplied evidence mounted into the `evidence/` directory or an alternate path passed at runtime.

## Repository Test Fixtures

The automated tests generate small synthetic artifacts at runtime:

- `triage.evtx` for event-log parsing
- `memory.mem` for volatility-style process extraction
- `traffic.pcap` for connection extraction

These fixtures are intentionally tiny and deterministic so the pipeline can be validated in CI without real forensic images.

## Known-Good References

The `tests/known_good/` directory is reserved for benchmark truth data:

- `disk_image_findings.json`
- `memory_capture_findings.json`

These files should contain the expected findings for curated datasets once benchmarking is complete.

## Evidence Handling Assumptions

- Evidence is mounted or copied into a read-only accessible path.
- Original evidence is never modified by Nightwing.
- Large binary artifacts may need pre-generated text summaries for the current MVP wrappers.
