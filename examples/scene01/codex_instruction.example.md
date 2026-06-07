# Scene01 Codex Instruction Example

Use this as a public template for a local Codex-controlled LTX render.

## Goal

Create a short image-to-video tilt-up from the provided GPT-generated source image.

## Inputs

- Source image: `<INPUT_IMAGE_PATH>`
- Workflow template: `examples/scene01/ltx_workflow.template.json`
- Shot manifest: `examples/scene01/shot_manifest.example.json`

## Render Direction

- Use the source image as the visual anchor.
- Generate a slow upward camera tilt.
- Preserve scene identity and composition.
- Avoid unrelated camera drift.
- Avoid adding new story elements not present in the source image.

## Required Codex Actions

1. Read the shot manifest.
2. Fill the LTX workflow template with the shot prompt and settings.
3. Submit the workflow to the configured ComfyUI endpoint.
4. Save the generated video to `<OUTPUT_VIDEO_PATH>`.
5. Write a redacted run manifest with the result status.

## Public Safety Requirements

- Do not include local machine paths in public examples.
- Do not include private prompts or private assets.
- Do not include model paths.
- Do not include generated output paths.
- Do not include credentials or local runtime details.
