---
type: resource
title: PostHog for Agent Telemetry
description: Product analytics telemetry sink and ingestion architecture capturing
  behavioral agent events via the Capture API with client-side PII sanitization.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
tags:
- observability
- posthog
- analytics
- privacy
- pii-sanitization
- goose
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:01:14.908330+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
PostHog serves as an external product analytics and telemetry sink for AI agent frameworks, capturing adoption metrics, session lifecycles, and behavioral events [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]. Operating outside the agent runtime as either a cloud-hosted service or self-hosted platform, PostHog provides structured event storage, funnel analysis, cohort segmentation, and feature flag management for agent deployments such as Goose [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].

# Architecture / Specification
The reference architecture defines how agent runtimes integrate with PostHog's ingestion layer while enforcing privacy safeguards [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]:

- **Client Ingestion Architecture**: Agents emit telemetry directly via HTTP POST requests to the PostHog Capture API (`/capture/`) using project API keys (`phc_*`), requiring no heavy SDK dependencies inside the agent binary [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].
- **Runtime Telemetry Module**: Exemplified by Goose's `posthog.rs` implementation, the agent runtime encapsulates an on-disk installation tracker (UUID-based distinct ID), an event builder (recording `session_start`, `error`, and `onboarding_*` events), and a dedicated PII sanitizer [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].
- **Client-Side PII Sanitization**: To protect user privacy, regex-based sanitization strips filesystem paths, API keys, email addresses, authentication tokens, and user UUIDs from event properties prior to transmission [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].
- **Ingestion Pipeline**: The PostHog backend buffers events into Kafka, stores raw and processed records in ClickHouse, and links events to anonymous or distinct person profiles for cohort and funnel analysis [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].

# References
- [PostHog GitHub Repository](https://github.com/PostHog/posthog)
- Related resource: [Goose Agent Runtime](../resources/goose.md)
- Related working group: [Observability and Traceability WG](../working-groups/observability-and-traceability.md)

[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
