---
type: reference-architecture
title: PostHog Product Analytics Reference Architecture
description: Reference architecture detailing PostHog event capture integration for
  product analytics, user adoption telemetry, and privacy classification boundaries.
resource: https://github.com/aaif/wg-observability-and-traceability/issues/55
tags:
- reference-architecture
- observability
- analytics
- privacy
- telemetry
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:14:13.366090+00:00'
sources:
- id: evt-wg-observability-and-traceability-issue-55
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/55
  author: smcd
  last_modified: '2026-09-24T01:59:02+00:00'
---

# Overview

The PostHog reference architecture details client-side and server-side product analytics integration for tracking agent usage, adoption metrics, and interaction funnels [^evt-wg-observability-and-traceability-issue-55].

# Architecture / Specification

### Telemetry and Identity Considerations

- **Identifier Semantics**: Implementations frequently utilize persistent installation identifiers (e.g., random UUIDs) to trace longitudinal usage [^evt-wg-observability-and-traceability-issue-55].
- **Jurisdictional Privacy Classification**: While often characterized as anonymous in US-centric contexts, persistent client identifiers constitute pseudonymous personal data under the EU GDPR (Recitals 26 and 30) and UK GDPR [^evt-wg-observability-and-traceability-issue-55]. Transmitting these identifiers across international boundaries (e.g., to hardcoded US endpoints) invokes applicable data protection and cross-border transfer obligations [^evt-wg-observability-and-traceability-issue-55].

# References

- [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md)
- [Agentic AI Security Best Practices Guide](../guidelines/agentic-ai-security-best-practices-guide.md)

[^evt-wg-observability-and-traceability-issue-55]: https://github.com/aaif/wg-observability-and-traceability/issues/55
