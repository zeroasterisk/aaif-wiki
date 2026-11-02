---
type: guideline
title: Cross-Working Group Security Review Checklist
description: Lightweight assessment checklist and review workflow applied by the Security
  and Privacy WG to evaluate cross-working group specifications and surface scope
  overlaps.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/meeting-notes/2026-08-18.md
tags:
- guidelines
- security
- governance
- review
- cross-wg
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:06:52.448943+00:00'
sources:
- id: evt-wg-security-and-privacy-file-e1f76734d747-7511fba6
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/meeting-notes/2026-08-18.md
  author: Alex Frazer
  last_modified: '2026-09-25T13:05:21-04:00'
- id: evt-wg-security-and-privacy-pr-24
  resource: https://github.com/aaif/wg-security-and-privacy/pull/24
  author: awfrazer
  last_modified: '2026-09-25T17:05:22+00:00'
---

# Overview

The Cross-Working Group Security Review Checklist is an operational evaluation framework led by the `../working-groups/security-and-privacy.md` Working Group to assess proposals, standards, and architecture templates emerging across the foundation [^evt-wg-security-and-privacy-file-e1f76734d747-7511fba6]. The checklist provides a standardized lens for detecting boundary vulnerabilities, unmitigated tool authority risks, and scope overlaps among parallel AAIF working groups.

By engaging with cross-foundation initiatives early in their development lifecycle, the checklist prevents conflicting security guidance and ensures coherent threat mitigation across working group boundaries [^evt-wg-security-and-privacy-file-e1f76734d747-7511fba6].

# Architecture / Specification

### Review Focus Areas

The checklist interrogates incoming specifications against core risk vectors:

1. **Protocol and Gateway Mediation**: Reviewing how agent gateways, reverse proxies, and communication protocols (such as Model Context Protocol and Agent-to-Agent / A2A) enforce identity authentication, tool capability authorization, and egress boundaries [^evt-wg-security-and-privacy-file-e1f76734d747-7511fba6].
2. **Observability and Boundary Tracing**: Collaborating with the Observability and Traceability Working Group (chaired by Pavan Sudheendra) to ensure telemetry frameworks, such as the `../resources/cross-boundary-observability-model.md`, do not leak sensitive payloads or bypass runtime sandboxes [^evt-wg-security-and-privacy-file-e1f76734d747-7511fba6, ^evt-wg-security-and-privacy-pr-24].
3. **Scope and Overlap Deconfliction**: Identifying shared mandates across `../working-groups/identity-and-trust.md`, `../working-groups/accuracy-and-reliability.md`, and `../working-groups/workflows-and-process-integration.md` to prevent duplicate protocol or policy workstreams [^evt-wg-security-and-privacy-file-e1f76734d747-7511fba6].

### Operational Prerequisites

Effective execution of cross-WG security reviews relies on public running notes and structured git deliverables across all technical working groups [^evt-wg-security-and-privacy-file-e1f76734d747-7511fba6]. Where working groups fail to maintain transparent running notes or deliverables, review workstream leads conduct direct outreach with working group chairs to clarify architectural scopes [^evt-wg-security-and-privacy-file-e1f76734d747-7511fba6].

# Lifecycle History

- **2026-08-18**: Govindaraj Palanisamy reported progress on the cross-WG overlap checklist during the Security and Privacy WG meeting, highlighting gaps in running notes across sibling groups and routing Pavan Sudheendra's draft cross-boundary observability framework into the review workstream [^evt-wg-security-and-privacy-file-e1f76734d747-7511fba6, ^evt-wg-security-and-privacy-pr-24].

[^evt-wg-security-and-privacy-file-e1f76734d747-7511fba6]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/meeting-notes/2026-08-18.md
