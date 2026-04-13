# Evidence Directory

This directory is reserved for case evidence.

Operational rule:
Treat every file under this directory as read-only evidence. Do not edit, rename, or delete artifacts in place.

Recommended usage:

- Mount evidence here read-only when running inside SIFT or Docker.
- Store derived outputs under `logs/`, not beside the evidence.
- If a tool requires transformation, write the derived artifact somewhere outside this folder.
