---
type: resource
title: PostHog Agent Telemetry Reference Architecture
description: Product analytics and telemetry reference architecture capturing pseudonymous
  agent behavioral funnels and operational metrics via direct Capture API calls and
  client-side PII sanitization.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
tags:
- observability
- posthog
- telemetry
- privacy
- analytics
- goose
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:15:10.316983+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

PostHog functions as a product analytics and behavioral event telemetry sink for AI agent frameworks, exemplified by its reference integration in Goose.[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75] Rather than capturing low-level function spans or kernel call graphs, PostHog ingests discrete session lifecycle events, feature adoption statistics, and error states while enforcing strict client-side privacy sanitization.[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]

# Architecture / Specification

## Ingestion Pipeline

Agent runtimes communicate directly with PostHog's Capture API (`https://us.i.posthog.com/capture/` or self-hosted instances) via HTTPS POST operations containing a project API key (`phc_*`).[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75] Ingestion does not require heavy SDK runtimes or local telemetry daemons; the agent runtime constructs and dispatches typed JSON payloads directly.[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]

## Telemetry Payload and Identity Model

The core transmission unit is the `CaptureEvent` payload, containing:
- `api_key`: Client project identifier embedded in the agent distribution.[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]
- `event`: Lifecycle action name (such as `session_start`, `error`, or `onboarding_*`).[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]
- `distinct_id`: Pseudonymous installation identifier generated as a random UUIDv4 stored on the local filesystem, avoiding association with user account identities or network hardware addresses.[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]
- `properties`: Metadata map detailing operational properties and execution environments.[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]
- `timestamp`: UTC event generation time.[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]

## Client-Side PII Sanitization

To preserve operational privacy, the client telemetry module (such as Goose's `posthog.rs`) routes all outgoing property fields through regex-based sanitization pipelines before serialization.[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75] The filter scrubs filesystem paths, API keys, email addresses, authorization tokens, and arbitrary UUIDs, ensuring that local workspace context and sensitive developer credentials are never transmitted to analytics storage.[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]

# References

- `../resources/goose.md`
- `../resources/agent-tool-cli-boundary.md`
- `../standards/agent-behavior-trace-model.md`
- `../working-groups/observability-and-traceability.md`

[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
