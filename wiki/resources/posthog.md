---
type: resource
title: PostHog AI Agent Analytics Reference Architecture
description: Product analytics and telemetry reference architecture capturing pseudonymous
  agent behavioral funnels, feature adoption, and longitudinal usage tracking.
resource: https://github.com/aaif/wg-observability-and-traceability/issues/55
tags:
- analytics
- telemetry
- privacy
- gdpr
- observability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:37:58.858547+00:00'
sources:
- id: evt-wg-observability-and-traceability-issue-55
  resource: https://github.com/aaif/wg-observability-and-traceability/issues/55
  author: smcd
  last_modified: '2026-09-24T01:59:02+00:00'
---

# Overview
The PostHog reference architecture provides design patterns and architectural specifications for integrating product analytics into AI agent harnesses and developer tools [^evt-wg-observability-and-traceability-issue-55]. It establishes telemetry capture for agent user journeys, feature discovery, and session completion metrics [^evt-wg-observability-and-traceability-issue-55].

# Architecture / Specification
The integration architecture standardizes client event dispatch, property capture, and funnel reporting.

### Identity and Privacy Classification
Telemetry implementations commonly generate persistent per-installation identifiers (`installation_id`, typically formatted as a random UUID) to measure cohort behavior and longitudinal usage without directly linking human identity [^evt-wg-observability-and-traceability-issue-55].

However, architectural review within the Observability and Traceability Working Group emphasizes that data privacy classifications depend on jurisdictional definitions rather than implementer labels [^evt-wg-observability-and-traceability-issue-55]:
- **Pseudonymity vs. Anonymity**: Under the EU General Data Protection Regulation (GDPR, Recitals 26 and 30) and the UK GDPR, persistent identifiers used for longitudinal user tracking constitute pseudonymous personal data, rather than anonymous data [^evt-wg-observability-and-traceability-issue-55].
- **Cross-Border Transfers**: Hardcoded telemetry endpoints directed to US ingest nodes (e.g., `us.i.posthog.com`) trigger international data transfer compliance duties when transmitting pseudonymous personal data originating from EU/UK jurisdictions [^evt-wg-observability-and-traceability-issue-55].
- **Template Schema Recommendations**: The working group proposes keying reference architecture privacy attributes (`personal data`, `personal information`, `PII`, `none`) directly to governing regulatory regimes rather than asserting absolute "privacy by design" claims [^evt-wg-observability-and-traceability-issue-55].

# Lifecycle History
- **2026-09**: Regulatory review identified that persistent installation UUIDs constitute pseudonymous personal data under GDPR/UK GDPR, initiating revisions to architectural classification standards [^evt-wg-observability-and-traceability-issue-55].

[^evt-wg-observability-and-traceability-issue-55]: https://github.com/aaif/wg-observability-and-traceability/issues/55
