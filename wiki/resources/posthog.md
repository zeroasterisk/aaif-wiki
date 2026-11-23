---
type: resource
title: PostHog Agent Analytics Reference Architecture
description: Product analytics telemetry sink and ingestion architecture capturing
  behavioral agent events, session properties, and cross-border data transfer boundaries.
resource: https://github.com/aaif/wg-observability-and-traceability/issues/55
tags:
- observability
- analytics
- privacy
- gdpr
- telemetry
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:07:52.630853+00:00'
sources:
- id: evt-wg-observability-and-traceability-issue-55
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/55
  author: smcd
  last_modified: '2026-09-24T01:59:02+00:00'
---

# Overview

The PostHog reference architecture documents telemetry collection, behavioral product analytics, and session inspection pipelines for agentic software deployments.

While PostHog provides deep user-journey tracking and client-side event ingestion, deployment within enterprise agent workflows requires strict alignment with data protection jurisdictions regarding pseudonymous identifiers and cross-border telemetry routing [^evt-wg-observability-and-traceability-issue-55].

# Architecture / Specification

## Identifier Tracking and Jurisdictional Classification

Telemetry architectures tracking longitudinal agent or user activity often assign random UUID identifiers (e.g., `installation_id`) to track lifecycle journeys without directly collecting plain-text names or emails [^evt-wg-observability-and-traceability-issue-55]:

- **Pseudonymity vs. Anonymity**: Under EU GDPR and UK GDPR (Recitals 26 and 30), a persistent identifier used to single out an installation or session across time is classified as pseudonymous personal data, not anonymous data [^evt-wg-observability-and-traceability-issue-55].
- **Cross-Border Transfers**: Hardcoded ingestion endpoints directed toward US infrastructure (e.g., `us.i.posthog.com`) trigger international data transfer regulations when collecting telemetry from EU or UK deployments [^evt-wg-observability-and-traceability-issue-55].
- **Jurisdiction-Aware Governance**: Rather than relying solely on pattern-matching regex filters for PII, observability templates must incorporate explicit data classification fields (personal data, personal information, PII, none) evaluated against the deployer's regulatory regime [^evt-wg-observability-and-traceability-issue-55].

# References

- Cross-Boundary Observability Model: [./cross-boundary-observability-model.md](./cross-boundary-observability-model.md)
- Agentic AI Security Best Practices: [../guidelines/agentic-ai-security-best-practices.md](../guidelines/agentic-ai-security-best-practices.md)

[^evt-wg-observability-and-traceability-issue-55]: https://github.com/aaif/wg-observability-and-traceability/issues/55
