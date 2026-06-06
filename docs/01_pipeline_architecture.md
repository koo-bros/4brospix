# Pipeline Architecture

4brospix is organized around shot state rather than a single monolithic render command.

## Stage 1: Story / Shot Manifest

The manifest describes scenes and shots using stable IDs. A shot can include:

- Narrative purpose
- Prompt intent
- Frame range
- Aspect ratio
- Provider preferences
- References to safe local placeholder paths
- Review notes
- Output records

The manifest should be valid without any private files present.

## Stage 2: AI Image / Video Generation Provider

Provider adapters can translate a shot request into a provider-specific job. The public architecture should keep provider credentials, endpoints, account IDs, queue URLs, and machine names outside the manifest.

Examples of conceptual provider IDs:

- `comfyui`
- `wan`
- `future_openai_video`
- `runway`
- `kling`

## Stage 3: Upscale / Interpolation / Cleanup

Generated outputs may need resolution changes, frame interpolation, stabilization, denoising, cleanup, or metadata normalization. The pipeline should track these as derived artifacts rather than replacing the original generation record.

## Stage 4: Blender Layout / Camera / Scene Pass

Blender can provide camera planning, layout proxies, scene blocking, render passes, and spatial continuity. Public examples should use placeholder scene names and synthetic file paths only.

## Stage 5: CSP Paint-Over

CSP paint-over can refine frames, repair details, or establish key art. The handoff should preserve shot ID, frame number, source artifact, artist notes, and version.

## Stage 6: After Effects Compositing

After Effects can combine generated plates, Blender passes, paint-over layers, cleanup outputs, titles, and final delivery settings. Public docs should describe metadata conventions, not private project files.

## Stage 7: Final Render Organization

Final output organization should make versions, dates, shots, review state, and delivery candidates easy to audit. Large media belongs outside git unless intentionally published through a release or asset system.

## Versioning Principles

- Never overwrite the only copy of an artifact.
- Keep source and derived artifacts distinguishable.
- Store enough metadata to understand how an output was produced.
- Prefer relative, project-local paths in examples.
- Keep private absolute paths out of public commits.

