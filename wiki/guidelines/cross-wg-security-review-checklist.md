---
type: guideline
title: Cross-Working Group Security and Privacy Review Checklist
description: Operational review checklist and intake framework guiding early identification
  of security and privacy considerations across AAIF deliverables.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-08-report.md
tags:
- guidelines
- security
- privacy
- review-checklist
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:10:57.892768+00:00'
sources:
- id: evt-wg-security-and-privacy-file-922f59c26329-785b273f
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-08-report.md
  author: Alex Frazer
  last_modified: '2026-09-28T08:37:25-04:00'
- id: evt-wg-security-and-privacy-pr-22
  resource: https://github.com/aaif/wg-security-and-privacy/pull/22
  author: awfrazer
  last_modified: '2026-09-28T12:37:32+00:00'
---

# Overview
The Cross-Working Group Security and Privacy Review Checklist is an operational intake framework maintained by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) [^evt-wg-security-and-privacy-file-922f59c26329-785b273f]. Led by Govindaraj Palanisamy, the checklist establishes structured criteria to ensure early identification and remediation of security and privacy concerns across AAIF technical deliverables [^evt-wg-security-and-privacy-file-922f59c26329-785b273f].

# Architecture / Specification
The framework provides an overlap analysis checklist designed to evaluate cross-cutting specifications and reference architectures across working groups [^evt-wg-security-and-privacy-file-922f59c26329-785b273f]. Key review criteria include:

- **Surface Exposure**: Identification of external protocol boundaries, tool calling capabilities, and network communication channels.
- **Identity and Delegation**: Verification that agent authorization, credential scoping, and user delegation align with standards defined by the [Identity and Trust Working Group](../working-groups/identity-and-trust.md) [^evt-wg-security-and-privacy-file-922f59c26329-785b273f].
- **Auditability and Evidence**: Assessment of event logging and attestation records compatible with [Observability and Traceability](../working-groups/observability-and-traceability.md) telemetry models.

# Lifecycle History
The review checklist workstream convened its initial cross-group syncs in August 2026 with four AAIF working group leads to build the overlap matrix and clarify deliverable scopes across repository workspaces [^evt-wg-security-and-privacy-file-922f59c26329-785b273f][^evt-wg-security-and-privacy-pr-22].

[^evt-wg-security-and-privacy-file-922f59c26329-785b273f]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-08-report.md
[^evt-wg-security-and-privacy-pr-22]: https://github.com/aaif/wg-security-and-privacy/pull/22
