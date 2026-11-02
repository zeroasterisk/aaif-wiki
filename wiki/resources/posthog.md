---
type: resource
title: PostHog Reference Architecture
description: Reference architecture detailing PostHog's Capture API ingestion, PII
  sanitization, and session analysis with jurisdiction-specific privacy classifications.
resource: https://github.com/aaif/wg-observability-and-traceability/issues/55
tags:
- observability
- telemetry
- privacy
- compliance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:05:17.279542+00:00'
sources:
- id: evt-wg-observability-and-traceability-issue-55
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/55
  author: smcd
  last_modified: '2026-09-24T01:59:02+00:00'
---

# Overview

The PostHog reference architecture evaluates the ingestion pipeline, Capture API mechanics, and session telemetry methods used to track agent interactions and user journeys[^evt-wg-observability-and-traceability-issue-55]. It provides guidance on client-side sanitization, event batching, and privacy-preserving observability patterns[^evt-wg-observability-and-traceability-issue-55].

# Architecture / Specification

The architecture incorporates privacy and jurisdictional telemetry controls:
- **Installation Identifiers and Pseudonymity**: Addresses the classification of UUID-based installation identifiers. While technical claims describe random UUIDs as anonymous-by-design tracking without PII, regulatory frameworks such as GDPR (Recitals 26 and 30) and UK GDPR classify persistent tracking identifiers as pseudonymous personal data[^evt-wg-observability-and-traceability-issue-55].
- **Cross-Border Transfers**: Identifies data transfer constraints when telemetry payloads and pseudonymous identifiers are routed to US-based endpoints (such as `us.i.posthog.com`) under international transfer regulations[^evt-wg-observability-and-traceability-issue-55].
- **Regime-Keyed Classification**: Outlines the requirement for reference architectures to categorize data types (personal data, personal information, PII, none) explicitly against relevant legal regimes rather than relying solely on client-side regex redacting[^evt-wg-observability-and-traceability-issue-55].

# References

- Observability and Traceability Working Group [Issue #55](https://github.com/aaif/wg-observability-and-traceability/issues/55)[^evt-wg-observability-and-traceability-issue-55]

[^evt-wg-observability-and-traceability-issue-55]: https://github.com/aaif/wg-observability-and-traceability/issues/55
