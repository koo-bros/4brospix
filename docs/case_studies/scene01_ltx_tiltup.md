# Scene01: Codex-Controlled LTX Tilt-Up

Scene01 is a sanitized case study for a successful internal LTX video generation test controlled by Codex.

The original internal output filename was:

```text
scene01_true_tiltup_v02_camera_prompt_strong_v63_00001.mp4
```

The raw video is not included in this repository.

## Story

The public workflow story is:

```text
GPT-generated image
  -> local Codex instruction
  -> Codex fills prompt/settings
  -> ComfyUI LTX single workflow runs
  -> generated tilt-up video is saved to an output path
```

## What Was Proven

- A single source image can be used as a shot anchor.
- Codex can operate as a controller that turns a natural-language instruction into structured render settings.
- A ComfyUI LTX workflow can execute those settings as a single video-generation run.
- The result can be recorded in a run manifest without exposing private machine details.

## Public Inputs

The public package includes examples only:

- `examples/scene01/shot_manifest.example.json`
- `examples/scene01/codex_instruction.example.md`
- `examples/scene01/run_manifest.redacted.json`
- `examples/scene01/ltx_workflow.template.json`

These files are templates. They are not raw production artifacts.

## Private Materials Not Published

- original source image
- raw ComfyUI workflow JSON
- private run/test scripts
- generated output video
- generated still frames
- model paths and local runtime paths
- private prompts and internal iteration notes

## Video Policy

The successful internal MP4 was found, but it is not committed here. It should only be published later as a small preview or release asset after separate approval, size checks, and visual review.

## Reproducible Public Shape

A contributor can reproduce the shape of the workflow by:

1. Creating a safe input image.
2. Filling `shot_manifest.example.json`.
3. Writing a local Codex instruction similar to `codex_instruction.example.md`.
4. Adapting `ltx_workflow.template.json` to their own ComfyUI/LTX setup.
5. Running `scripts/comfyui_ltx_autorender.py` with local configuration.
6. Recording a redacted result like `run_manifest.redacted.json`.
