# 4brospix

4brospix is an experimental open-source AI animation production pipeline.

It connects story and shot manifests, AI image/video generation providers, ComfyUI/Wan-style workflows, Blender layout, CSP paint-over, After Effects compositing, and final render organization.

This repository is the public, sanitized starting point for the project. Private development and production experiments existed before this public repository, but private files, assets, machine details, credentials, logs, generated media, model weights, and production-specific paths are intentionally not included here.

## Why It Exists

AI animation production involves many tools that do not naturally share a common structure. 4brospix explores a manifest-driven workflow where shots, prompts, references, provider jobs, review passes, layout data, paint-over notes, compositing outputs, and final renders can be organized without locking the project to a single vendor or local machine.

The goal is not to present a finished product. The goal is to make a public OSS lab notebook and workflow framework that can evolve safely.

## Current Status

Early experimental.

This repository currently contains documentation, example manifests, and configuration templates only. Implementation code, production assets, generated media, private provider workflows, and internal automation are not part of this first public commit.

## Pipeline

```text
Story / Shot Manifest
  -> AI image/video generation provider
  -> Upscale / interpolation / cleanup
  -> Blender layout / camera / scene pass
  -> CSP paint-over
  -> After Effects compositing
  -> Final render organization
```

## Provider-Agnostic Direction

4brospix should not hardcode one provider. A future implementation can model providers as adapters with shared concepts such as:

- `comfyui`
- `wan`
- `future_openai_video`
- `runway`
- `kling`

These names are conceptual examples only. This public repository does not include private endpoints, credentials, account data, internal workflow files, or provider-specific production settings.

## Repository Structure

```text
.
|-- README.md
|-- ROADMAP.md
|-- SECURITY.md
|-- LICENSE
|-- docs/
|   |-- 00_overview.md
|   |-- 01_pipeline_architecture.md
|   |-- 02_provider_abstraction.md
|   |-- 03_local_lab_workflow.md
|   `-- 04_security_and_redaction.md
|-- manifests/
|   `-- shot_manifest.example.json
|-- configs/
|   |-- env.example
|   `-- paths.example.yaml
`-- .gitignore
```

## What Is Intentionally Not Included

- Private source trees or scripts from earlier development
- Private IP addresses, hostnames, usernames, passwords, API keys, tokens, or `.env` files
- Internal server details or deployment notes
- Production assets, generated frames, generated videos, final renders, or review media
- Model weights, checkpoints, LoRAs, embeddings, caches, or downloaded datasets
- Logs, temporary files, machine-specific paths, and editor state
- Proprietary provider workflows or account-specific settings

## Security Note

Treat this repository as public by default. Do not commit secrets, generated production media, provider credentials, private machine names, or internal paths. See [SECURITY.md](SECURITY.md) and [docs/04_security_and_redaction.md](docs/04_security_and_redaction.md).

## Roadmap

See [ROADMAP.md](ROADMAP.md) for the public development direction.

