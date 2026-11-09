---
type: resource
title: PostHog Agent Telemetry Reference Architecture
description: Product analytics and session telemetry backend mapping agent behavioral
  events through direct HTTPS Capture API ingestion and client-side PII sanitization.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T09:47:35.806001+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

PostHog functions as an external agent telemetry sink providing product analytics, adoption metrics, cohort segmentation, and behavioral event collection for AI agent frameworks [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]. Rather than capturing fine-grained distributed execution spans, it focuses on high-level lifecycle events, user onboarding funnels, error telemetry, and aggregate feature usage across desktop and CLI runtimes.

The reference architecture assesses PostHog's role within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), specifically evaluating privacy preservation boundaries during product event ingestion as exemplified by the [Goose](goose.md) agent runtime.

# Architecture / Specification

The integration pattern relies on an out-of-band HTTPS telemetry client without requiring heavy dependency SDKs [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]:

- **Client Ingestion Module:** The agent runtime embeds an HTTP telemetry module that writes directly to PostHog's Capture API (`/capture/`). Payloads consist of structured `CaptureEvent` records containing an API project key (`phc_*`), event identifier, pseudonymous `distinct_id` (persisted on disk as a UUID v4), timestamp, and key-value properties.
- **PII Sanitizer:** Before dispatch, client-side regex filters strip sensitive material including file system paths, authentication keys, email addresses, bearer tokens, and internal UUIDs from event payloads.
- **Storage Pipeline:** Events ingested by PostHog are buffered via Apache Kafka and persisted into ClickHouse for aggregate query evaluation and user profile correlation.

# References

- PostHog Capture API Reference and Ingestion Architecture [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]
- Goose 1.39.0 Telemetry Implementation (`posthog.rs`) [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]

[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
