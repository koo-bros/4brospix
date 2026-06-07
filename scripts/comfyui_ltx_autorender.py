#!/usr/bin/env python3
"""Small public example for submitting a template-style LTX render.

This script is intentionally generic. It expects local users to provide their
own ComfyUI endpoint, input image, prompt, and output location.
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.request
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def replace_placeholders(value: Any, replacements: dict[str, str]) -> Any:
    if isinstance(value, str):
        for key, replacement in replacements.items():
            value = value.replace(key, replacement)
        return value
    if isinstance(value, list):
        return [replace_placeholders(item, replacements) for item in value]
    if isinstance(value, dict):
        return {
            key: replace_placeholders(item, replacements)
            for key, item in value.items()
        }
    return value


def submit_workflow(endpoint: str, workflow: dict[str, Any]) -> dict[str, Any]:
    payload = json.dumps({"prompt": workflow["workflow"]}).encode("utf-8")
    request = urllib.request.Request(
        endpoint.rstrip("/") + "/prompt",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Submit a public LTX template.")
    parser.add_argument("--template", required=True, type=Path)
    parser.add_argument("--input-image", required=True)
    parser.add_argument("--output-path", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--negative-prompt", default="")
    parser.add_argument("--seed", default="12345")
    parser.add_argument("--frames", default="97")
    parser.add_argument("--width", default="1024")
    parser.add_argument("--height", default="576")
    parser.add_argument("--steps", default="30")
    parser.add_argument("--guidance", default="3.5")
    parser.add_argument(
        "--endpoint",
        default=os.environ.get("COMFYUI_ENDPOINT", "http://127.0.0.1:8188"),
    )
    args = parser.parse_args()

    template = load_json(args.template)
    replacements = {
        "<INPUT_IMAGE_PATH>": args.input_image,
        "<OUTPUT_VIDEO_PATH>": args.output_path,
        "<PROMPT_TEXT>": args.prompt,
        "<NEGATIVE_PROMPT_TEXT>": args.negative_prompt,
        "<SEED>": args.seed,
        "<FRAME_COUNT>": args.frames,
        "<WIDTH>": args.width,
        "<HEIGHT>": args.height,
        "<STEP_COUNT>": args.steps,
        "<GUIDANCE_VALUE>": args.guidance,
        "<MODEL_PATH>": "configured-locally",
    }
    workflow = replace_placeholders(template, replacements)
    result = submit_workflow(args.endpoint, workflow)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
