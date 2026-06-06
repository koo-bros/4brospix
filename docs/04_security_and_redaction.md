# Security And Redaction

4brospix must assume the public repository is visible to everyone.

## Public Commit Checklist

Before committing, check for:

- API keys, tokens, passwords, cookies, and private keys
- `.env` files and local credential files
- Private IP addresses and internal hostnames
- Local usernames and absolute machine paths
- Generated videos, generated frames, production renders, and review exports
- Model weights, checkpoints, LoRAs, embeddings, and datasets
- Logs, stack traces, crash dumps, and temporary files
- Provider account identifiers or queue details

## Example Local Checks

Run local checks for secret-like assignments, private network ranges, absolute workstation paths, and generated binary media references. Keep the exact command patterns in local notes or CI configuration if they would otherwise self-match the public documentation.

These checks are not complete. They are a baseline for obvious leaks and should be expanded in CI as implementation files are added.

## Redaction Principles

- Replace real provider names, account IDs, hosts, and paths with placeholders when needed.
- Prefer relative paths in examples.
- Keep real credentials in local ignored files or external secret managers.
- Do not publish production media unless it has gone through explicit release review.
- Remove logs before committing, even if they appear harmless.

## Handling Accidental Exposure

If sensitive material is committed:

1. Stop adding new commits that reference the secret.
2. Rotate the exposed credential if applicable.
3. Remove the sensitive file or value.
4. Rewrite history only after deciding that it is necessary and safe for collaborators.
5. Document the remediation without repeating the secret.
