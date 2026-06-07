# 4brospix

4brospix is an experimental open-source AI animation production pipeline where Codex can control local generation workflows.

It connects story and shot manifests, AI image/video generation providers, ComfyUI/Wan-style workflows, Blender layout, CSP paint-over, After Effects compositing, and final render organization.

This repository is the public, sanitized starting point for the project. Private development and production experiments existed before this public repository, but private files, assets, machine details, credentials, logs, generated media, model weights, and production-specific paths are intentionally not included here.

## Why It Exists

AI animation production involves many tools that do not naturally share a common structure. 4brospix explores a manifest-driven workflow where shots, prompts, references, provider jobs, review passes, layout data, paint-over notes, compositing outputs, and final renders can be organized without locking the project to a single vendor or local machine.

The goal is not to present a finished product. The goal is to make a public OSS lab notebook and workflow framework that can evolve safely.

## Current Status

Early experimental.

This repository currently contains documentation, example manifests, and configuration templates only. Implementation code, production assets, generated media, private provider workflows, and internal automation are not part of this first public commit.

## Scene01: Codex-Controlled LTX Video Generation

Scene01 is the first sanitized public case study.

```text
GPT-generated image
  -> local Codex instruction
  -> Codex fills prompt/settings
  -> ComfyUI LTX single workflow
  -> generated tilt-up video
```

Status: successful internal test, sanitized public case study with a small input preview and one demo MP4.

The raw workflow JSON and private run scripts are not committed to git. The public package documents the workflow shape, includes a small input preview, includes one demo MP4, and provides template files:

- [Codex-controlled LTX autorender](docs/codex_ltx_autorender.md)
- [Scene01 LTX tilt-up case study](docs/case_studies/scene01_ltx_tiltup.md)
- [Watch the Scene01 demo in browser](https://koo-bros.github.io/4brospix/demo/scene01.html)
- [Scene01 input preview](docs/media/scene01_input_preview.png)
- [Scene01 output demo MP4](docs/media/scene01_output_demo.mp4)
- [Scene01 demo release asset](https://github.com/koo-bros/4brospix/releases/tag/scene01-demo-v0.1)
- [Scene01 examples](examples/scene01/)

This repository includes one small demo MP4. Future generated demos should replace `docs/media/scene01_output_demo.mp4` rather than adding many video files.

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
|   |-- 04_security_and_redaction.md
|   |-- codex_ltx_autorender.md
|   |-- media/
|   |   `-- scene01_input_preview.png
|   `-- case_studies/
|       `-- scene01_ltx_tiltup.md
|-- examples/
|   `-- scene01/
|       |-- shot_manifest.example.json
|       |-- codex_instruction.example.md
|       |-- run_manifest.redacted.json
|       `-- ltx_workflow.template.json
|-- scripts/
|   `-- comfyui_ltx_autorender.py
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
