---
type: resource
title: PostHog Agent Telemetry Reference Architecture
description: Reference architecture detailing PostHog's Capture API ingestion, PII
  sanitization, and session analytics for agent runtimes.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
tags:
- observability
- telemetry
- analytics
- privacy
- posthog
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:13:28.544386+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview
PostHog serves as an external analytics and behavioral telemetry sink capturing agent session lifecycles, user adoption funnels, and command metrics [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]. Within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) landscape, PostHog demonstrates how privacy-conscious client-side agents like [Goose](../resources/goose.md) stream structured analytics payloads over HTTPS without embedding heavy vendor SDKs [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].

# Architecture / Specification
The reference architecture outlines the ingestion pipeline and client runtime architecture [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]:
- **Ingestion Surface:** Agents send direct HTTPS POST payloads to PostHog's Capture API (`/capture/`) containing API project keys, event types, anonymous `distinct_id` identifiers, and custom properties.
- **Client-Side Telemetry Module:** Exemplified by Goose's `posthog.rs`, the client manages an installation tracker UUID persisted on disk, an event builder for session lifecycles (`session_start`, onboarding milestones), and an active regex-based PII sanitizer stripping paths, tokens, emails, and keys.
- **Sink Storage and Analytics:** PostHog processes inbound events through an ingestion pipeline into a ClickHouse-backed event store, computing behavioral funnels, cohort segmentation, and feature flag states.
- **Privacy Boundaries:** Strict separation is maintained between pseudonymous product telemetry and raw conversational prompt data, preventing sensitive context leakage.

# References
- [PostHog Reference Architecture](https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md)
- Related agent framework: [Goose](../resources/goose.md)

[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
