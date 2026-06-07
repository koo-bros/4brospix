# Codex-Controlled LTX Autorender

This note describes a sanitized pattern for using Codex as a local controller for an LTX video generation workflow in ComfyUI.

The public version is intentionally architecture-first. It does not include private machine names, local paths, model paths, raw prompts, or generated media.

## Control Flow

```text
GPT-generated image
  -> local Codex instruction
  -> Codex fills shot prompt and render settings
  -> ComfyUI LTX single workflow runs
  -> generated video is written to a configured output location
```

## Roles

- GPT-generated image: visual starting point for the shot.
- Codex: local workflow controller that prepares shot metadata, prompt text, and settings.
- ComfyUI: execution runtime for the LTX workflow.
- LTX workflow: image-to-video generation graph.
- Run manifest: redacted record of the request, settings, and result.

## Public Safety Boundary

Public examples should use placeholders for:

- input image path
- output video path
- model path
- ComfyUI endpoint
- prompt text
- seed and run identifiers

Raw workflow JSON and generated media should stay private until they are separately reviewed and converted into examples.

## Minimal Execution Shape

```text
1. Prepare a shot manifest.
2. Write a Codex instruction that names the shot goal and constraints.
3. Fill a template workflow with placeholder-safe prompt/settings fields.
4. Submit the workflow to a configured ComfyUI endpoint.
5. Record the result in a redacted run manifest.
```

See the Scene01 case study and examples:

- [Scene01 LTX tilt-up case study](case_studies/scene01_ltx_tiltup.md)
- [Scene01 shot manifest](../examples/scene01/shot_manifest.example.json)
- [Scene01 Codex instruction](../examples/scene01/codex_instruction.example.md)
- [Scene01 redacted run manifest](../examples/scene01/run_manifest.redacted.json)
- [Scene01 workflow template](../examples/scene01/ltx_workflow.template.json)
