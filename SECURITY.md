# Security Policy

This repository is public. Do not commit private production data.

## Supported Scope

The current public repository contains documentation and example templates only. Security reports are most useful when they identify accidental exposure risks, unsafe defaults, secret-handling mistakes, or private-data leakage paths in public files.

## Do Not Commit

- API keys, provider tokens, cookies, passwords, SSH keys, or service-account files
- `.env` files or local credential stores
- Private IP addresses, hostnames, usernames, internal paths, or deployment details
- Generated videos, generated frames, review exports, final renders, or production assets
- Model weights, checkpoints, LoRAs, embeddings, datasets, caches, or downloaded provider artifacts
- Logs, crash dumps, temporary files, and machine-specific editor state

## Reporting Issues

Open a GitHub issue for public security hardening suggestions that do not disclose sensitive material.

If you believe sensitive data was accidentally published, avoid repeating the secret in an issue title or body. Use a minimal description, identify the affected file path and commit if known, and request maintainer review.

## Redaction Baseline

Before public commits, run local checks for:

- Secret-like names such as `API_KEY`, `TOKEN`, `PASSWORD`, `SECRET`, and `PRIVATE_KEY`
- Private network ranges used for local or internal infrastructure
- Local absolute paths from macOS, Linux, or Windows workstations
- Generated media extensions and large binary assets

See [docs/04_security_and_redaction.md](docs/04_security_and_redaction.md).
