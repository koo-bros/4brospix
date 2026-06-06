# Provider Abstraction

4brospix should support multiple image and video generation providers without making one provider the core data model.

## Adapter Concept

A provider adapter is responsible for translating a neutral shot request into a provider-specific job and translating the provider result back into neutral pipeline metadata.

Conceptual adapter IDs may include:

- `comfyui`
- `wan`
- `future_openai_video`
- `runway`
- `kling`

These are examples only. They do not imply bundled credentials, endpoints, workflows, or account access.

## Neutral Job Shape

A neutral generation request can include:

- `shot_id`
- `provider`
- `task_type`
- `prompt`
- `negative_prompt`
- `duration_frames`
- `fps`
- `aspect_ratio`
- `seed`
- `inputs`
- `output_expectations`

## Provider-Specific Data

Provider-specific details should live behind adapter boundaries. Public manifests should avoid storing:

- API keys or tokens
- Internal URLs
- Private hostnames
- Account IDs
- Queue names that reveal infrastructure
- Local absolute paths
- Proprietary workflow files that are not safe to publish

## Capability Discovery

Future adapters can expose capability metadata such as:

- Supported task types
- Supported resolutions
- Supported duration limits
- Whether image conditioning is supported
- Whether video extension is supported
- Whether deterministic seeds are supported

This lets the pipeline choose compatible providers without hardcoding one service.

## Dry-Run Mode

Public development should include a dry-run provider that validates manifests and writes placeholder job records without calling external services. This makes tests safe and repeatable.

