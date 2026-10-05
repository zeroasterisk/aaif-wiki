---
type: architecture
title: PostHog Reference Architecture
description: Open product analytics and event telemetry sink capturing sanitized behavioral
  events and adoption metrics from AI agent runtimes.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
tags:
- observability
- telemetry
- analytics
- privacy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:33:25.575442+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

PostHog operates as an external telemetry and product analytics sink for AI agent frameworks, capturing structured adoption, session lifecycle, and error metrics without exposing personally identifiable information (PII) or sensitive prompts [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]. Within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), PostHog represents an ingestion pattern for high-level practitioner usage analytics distinct from low-level execution tracing.

# Architecture / Specification

Agent runtimes, such as [Goose](../reference-architectures/goose.md), interface directly with the PostHog Capture API (`https://us.i.posthog.com/capture/` or `eu.i.posthog.com`) using lightweight HTTPS POST payloads without requiring full vendor SDKs [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]:

- **Client Pipeline**: Implements an installation tracker (generating a persistent UUID v4), event builders for lifecycle phases (`session_start`, `error`, `onboarding_*`), and a dedicated PII sanitizer stripping paths, tokens, emails, and API keys [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].
- **Payload Format**: Sends JSON containing `api_key`, `event`, `distinct_id`, `properties`, and `timestamp` directly to the PostHog ingestion pipeline [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].
- **Storage and Processing**: Ingested events flow through Kafka into ClickHouse, enabling cohort segmentation, funnel analysis, and feature flag management [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].

# References

- PostHog Reference Architecture in [Observability and Traceability WG](../working-groups/observability-and-traceability.md) [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].

[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]: https://github.com/aaif/wg-observability-and-traceability/blob/fc52a1585af40a02b2b29f86d1bc5f98af126b7d/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
