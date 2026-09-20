---
type: deliverable
title: PostHog Reference Architecture
description: A reference architecture evaluating PostHog event capture APIs and privacy-preserving
  analytics patterns for AI agent runtimes.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
tags:
- observability
- telemetry
- posthog
- analytics
- agent-frameworks
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:53:02.650946+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
  author: Matthew Khouzam
  last_modified: '2026-08-19T20:04:48+01:00'
---

# Overview

PostHog is an open-source analytics platform and telemetry sink that receives structured product, adoption, and behavioral events from AI agent runtimes while enforcing client-side privacy controls [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]. It provides ingestion APIs, event storage on ClickHouse, cohort segmentation, funnel tracking, and feature flag management for both cloud-hosted and self-hosted deployments [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].

Within the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md), PostHog represents an application and product telemetry backend, complementing distributed tracing patterns seen in the [OpenTelemetry Reference Architecture](../deliverable/opentelemetry-reference-architecture.md) [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].

# Architecture / Specification

The integration pattern exemplifies how AI agent frameworks (such as Goose) stream telemetry to PostHog [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]:
- **Client Runtime Sanitization**: In-process modules sanitize telemetry payloads using regular expression filtering to strip file paths, API keys, email addresses, and environment secrets prior to dispatch [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].
- **Capture API**: Direct HTTP POST payloads containing anonymous UUIDs (`distinct_id`), event identifiers, and sanitized properties sent over TLS [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].
- **Ingestion and Analytics Engine**: PostHog processes incoming events through Kafka into ClickHouse stores for dashboarding, cohort tracking, and behavioral queries [^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75].

[^evt-wg-observability-and-traceability-file-d36a782a2588-bde0dd75]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/tracing_landscape/05-ai-agent-observability/AAIF-REF-ARCH-POSTHOG.md
