# Scene01: Codex-Controlled LTX Tilt-Up

Scene01 is a sanitized case study for a successful internal LTX video generation test controlled by Codex.

The original internal output filename was:

```text
scene01_true_tiltup_v02_camera_prompt_strong_v63_00001.mp4
```

The repository includes one demo MP4, and the same file is also published as a GitHub Release asset:

- [Browser demo](https://koo-bros.github.io/4brospix/demo/scene01.html)
- [Scene01 output demo MP4](../media/scene01_output_demo.mp4)
- [scene01-demo-v0.1](https://github.com/koo-bros/4brospix/releases/tag/scene01-demo-v0.1)

<table>
  <tr>
    <td width="50%" align="center">
      <strong>Input image</strong><br>
      <img src="../media/scene01_input_preview.png" width="420">
    </td>
    <td width="50%" align="center">
      <strong>Generated video preview</strong><br>
      <a href="https://koo-bros.github.io/4brospix/demo/scene01.html">
        <img src="../media/scene01_output_preview.gif" width="420">
      </a>
    </td>
  </tr>
</table>

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

- [`docs/media/scene01_input_preview.png`](../media/scene01_input_preview.png)
- [`docs/media/scene01_output_demo.mp4`](../media/scene01_output_demo.mp4)
- `examples/scene01/shot_manifest.example.json`
- `examples/scene01/codex_instruction.example.md`
- `examples/scene01/run_manifest.redacted.json`
- `examples/scene01/ltx_workflow.template.json`

The preview image is a small public reference image for the case study. The JSON and Markdown files are templates, not raw production artifacts.

## Private Materials Not Published

- raw ComfyUI workflow JSON
- private run/test scripts
- additional generated videos beyond the single tracked demo
- generated still frames
- model paths and local runtime paths
- private prompts and internal iteration notes

## Video Policy

The successful MP4 is intentionally tracked as a single public demo file at `docs/media/scene01_output_demo.mp4`. Future generated demos should replace this file rather than adding many video files. The same file is attached to the `scene01-demo-v0.1` GitHub Release for direct download.

## Reproducible Public Shape

A contributor can reproduce the shape of the workflow by:

1. Creating a safe input image.
2. Filling `shot_manifest.example.json`.
3. Writing a local Codex instruction similar to `codex_instruction.example.md`.
4. Adapting `ltx_workflow.template.json` to their own ComfyUI/LTX setup.
5. Running `scripts/comfyui_ltx_autorender.py` with local configuration.
6. Recording a redacted result like `run_manifest.redacted.json`.
