# Local Lab Workflow

This repository is designed to grow from safe local experiments. Local workflows should keep generated media and private configuration outside git by default.

## Suggested Local Flow

1. Create or update a shot manifest using placeholder-safe metadata.
2. Validate the manifest.
3. Run a dry-run provider adapter or a local provider adapter configured outside git.
4. Store generated outputs in an ignored local output directory.
5. Track derived artifacts with sidecar metadata.
6. Review and select candidates.
7. Hand off selected frames or clips to Blender, CSP, or After Effects.
8. Organize final renders outside git unless explicitly prepared for public release.

## Directory Conventions

Example public-safe conventions:

```text
project_root/
|-- manifests/
|-- configs/
|-- docs/
|-- work/
|   |-- generated/
|   |-- blender/
|   |-- csp/
|   |-- ae/
|   `-- renders/
`-- tmp/
```

The `work/` and `tmp/` directories should remain ignored unless they contain intentionally sanitized fixtures.

## Configuration

Use `configs/env.example` and `configs/paths.example.yaml` as templates. Real local configuration should be copied to ignored files such as:

- `.env`
- `configs/env.local`
- `configs/paths.local.yaml`

## Review Records

Review notes should reference shot IDs, artifact IDs, and versions. Avoid comments that include private account data, local usernames, private paths, or production-sensitive client information.

## Public Fixture Rule

Any fixture committed to this repository should be synthetic, small, and safe to redistribute.

