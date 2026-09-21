---
type: reference-architecture
title: PostHog Agent Telemetry Reference Architecture
description: Reference architecture evaluating PostHog Capture API ingestion for agent
  behavioral telemetry, product analytics, and PII sanitization.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
tags:
- observability
- telemetry
- posthog
- agent-analytics
- reference-architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:56:04.506283+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

PostHog is an analytics and telemetry sink utilized by agent frameworks to collect behavioral event data, feature usage metrics, and adoption statistics [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]. In AI agent architectures (such as the reference implementation in Goose), PostHog operates as an external event ingestion sink via its HTTP Capture API.

# Architecture / Specification

- **Agent Ingestion Module**: Agent runtimes build structured `CaptureEvent` payloads containing distinct anonymous installation UUIDs, event names, sanitized session metadata, and timestamps [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].
- **Privacy and PII Sanitization**: Client-side regex sanitization scrubs file paths, API tokens, email addresses, and secret keys prior to network transmission.
- **Storage and Analytics Pipeline**: Ingested payloads are queued via Kafka and stored within ClickHouse for user session analysis, retention cohorting, and telemetry-driven feature flagging.

[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
