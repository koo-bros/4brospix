# Overview

4brospix is an experimental AI animation production pipeline for organizing shots across generation, layout, paint-over, compositing, and final render stages.

The public repository is a sanitized lab notebook and workflow framework. It is designed to describe concepts and safe interfaces before exposing any implementation that might accidentally include private production state.

## Core Idea

The project starts with a shot manifest. Each shot can carry story intent, prompt data, frame ranges, provider job records, review status, and links to local outputs. Pipeline stages can then read and update structured records rather than relying on scattered filenames and manual notes.

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

