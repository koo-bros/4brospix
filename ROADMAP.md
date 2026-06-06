# Roadmap

4brospix is early experimental work. The roadmap is intentionally practical and documentation-first so the public repository can grow without exposing private production state.

## Phase 0: Public Skeleton

- Publish sanitized project description, security policy, and workflow overview.
- Add example manifests and configuration templates.
- Define redaction expectations before any implementation is moved into public.
- Keep all private assets, credentials, logs, generated media, and machine details out of the repository.

## Phase 1: Manifest Contract

- Formalize a shot manifest schema.
- Define stable shot IDs, scene IDs, task states, provider job records, review notes, and render outputs.
- Add validation for example manifests.
- Add tests that use synthetic placeholder data only.

## Phase 2: Provider Adapter Interface

- Define a provider-agnostic job interface.
- Support conceptual adapters such as `comfyui`, `wan`, `future_openai_video`, `runway`, and `kling`.
- Separate public adapter contracts from private credentials and machine-specific execution details.
- Add local dry-run behavior for development and tests.

## Phase 3: Local Lab Workflow

- Add local-only commands for organizing synthetic shots and placeholder outputs.
- Document safe folder conventions for experiments, review media, and exports.
- Add redaction checks for common secret and private-path patterns.
- Keep generated media outside git by default.

## Phase 4: DCC and Compositing Handoff

- Document handoff conventions for Blender layout, CSP paint-over, and After Effects compositing.
- Define metadata sidecars for camera, frame range, version, and review status.
- Add examples that use mock media names and placeholder paths.

## Phase 5: Production Hardening

- Add stronger validation, resumable job tracking, reproducibility metadata, and audit logs.
- Improve provider capability discovery.
- Add CI checks for schema validation, formatting, and secret scanning.
- Keep production-specific orchestration private unless it can be fully sanitized.

