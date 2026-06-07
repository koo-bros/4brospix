# Overview

4brospix is an experimental AI animation production pipeline for organizing shots across generation, layout, paint-over, compositing, and final render stages.

The public repository is a sanitized lab notebook and workflow framework. It is designed to describe concepts and safe interfaces before exposing any implementation that might accidentally include private production state.

## Core Idea

The project starts with a shot manifest. Each shot can carry story intent, prompt data, frame ranges, provider job records, review status, and links to local outputs. Pipeline stages can then read and update structured records rather than relying on scattered filenames and manual notes.

## Scene01 Case Study

Scene01 shows the public workflow pattern in a concrete, sanitized form:

```text
GPT-generated image
  -> local Codex instruction
  -> Codex fills prompt/settings
  -> ComfyUI LTX single workflow
  -> generated tilt-up video
```

The internal test succeeded, but the raw image, raw workflow JSON, private scripts, and generated video are not included in the public repository.

- [Codex-controlled LTX autorender](codex_ltx_autorender.md)
- [Scene01 LTX tilt-up case study](case_studies/scene01_ltx_tiltup.md)
- [Scene01 shot manifest example](../examples/scene01/shot_manifest.example.json)

## Public Goals

- Keep shot planning and production metadata explicit.
- Support multiple AI image and video generation providers through adapters.
- Preserve handoff context for Blender, CSP, After Effects, and final render organization.
- Make local experiments reproducible without publishing private assets or credentials.
- Provide clean examples that other contributors can inspect safely.

## Non-Goals For This First Public Skeleton

- Shipping a finished product
- Publishing private development scripts
- Publishing generated media, production assets, provider credentials, or model weights
- Encoding one provider, one server, or one workstation as the default architecture

## Pipeline Summary

```text
Story / Shot Manifest
  -> AI image/video generation provider
  -> Upscale / interpolation / cleanup
  -> Blender layout / camera / scene pass
  -> CSP paint-over
  -> After Effects compositing
  -> Final render organization
```
