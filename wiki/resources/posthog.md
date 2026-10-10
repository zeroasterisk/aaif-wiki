---
type: resource
title: PostHog Agent Telemetry Integration
description: Open-source product analytics and behavioral event capture backend for
  privacy-preserving AI agent telemetry and session tracking.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
tags:
- telemetry
- analytics
- privacy
- observability
- sink
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T14:56:56.659838+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

PostHog is an analytics telemetry backend utilized by agent frameworks to collect product usage analytics, adoption funnels, and operational error events while enforcing strict client-side PII sanitization [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]. Within agent architectures like [Goose](../resources/goose.md), PostHog operates as an asynchronous, out-of-process event sink capturing structured session metadata without impeding execution loops [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].

# Architecture / Specification

The PostHog integration pattern consists of three core operational layers within the agent runtime [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]:

- **Installation Tracking**: Persists an anonymous disk-bound UUID to correlate multi-session agent lifecycles without tying events to personal identities [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].
- **Event Construction & Filtering**: Packages agent lifecycle events (`session_start`, `error`, `onboarding_*`) into JSON payload schemas conforming to PostHog's Capture API [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].
- **PII Sanitizer**: Executes regex-based stripping pipelines across event properties to remove file paths, auth keys, tokens, emails, and sensitive identifiers before network dispatch [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].
- **Ingestion Sink**: Ingests batched events over HTTPS POST directly into PostHog's Kafka and ClickHouse ingestion pipeline for cohort analysis, retention metrics, and feature flag evaluation [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].

[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]: https://github.com/aaif/wg-observability-and-traceability/blob/ecdd24bcbb59140ce89b608a8ddf815a38140a2b/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
