---
type: working-group
title: Security and Privacy Working Group
description: AAIF working group establishing security best practices, threat modeling
  frameworks, and cross-WG security baselines for autonomous agent runtimes.
resource: https://github.com/aaif/wg-security-and-privacy/pull/25
tags:
- working-group
- security
- privacy
- threat-modeling
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:24:05.666762+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-25
  resource: https://github.com/aaif/wg-security-and-privacy/pull/25
  author: awfrazer
  last_modified: '2026-10-01T05:08:24+00:00'
---

# Overview

The Security and Privacy Working Group develops baseline security architectures, threat modeling methodologies, privacy engineering principles, and design pattern catalogs for autonomous agentic systems[^evt-wg-security-and-privacy-pr-25]. The working group evaluates adversarial risks unique to autonomous execution boundaries, secret distribution across MCP tooling, and hardware-assisted isolation.

The group collaborates with the [Identity and Trust Working Group](../working-groups/identity-and-trust.md) on cryptographic identity boundaries and reports governance escalations to the [Technical Committee](../governance/technical-committee.md)[^evt-wg-security-and-privacy-pr-25].

# Architecture / Specification

### Workstreams and Deliverables
- **Security Best Practices Guide**: Living baseline artifact detailing practical architectural controls and operational security measures across secrets handling and protocol layers[^evt-wg-security-and-privacy-pr-25] (see [Agentic AI Security Best Practices Guide](../guidelines/agentic-ai-security-best-practices-guide.md)).
- **Threat Modeling Gap Analysis**: Comparative framework evaluating industry matrices (OWASP, MITRE ATLAS, CSA MAESTRO, NIST AI RMF) to identify threat vectors unaddressed in agentic execution[^evt-wg-security-and-privacy-pr-25] (see [Threat Modeling Gap Analysis](../assessments/agentic-ai-threat-modeling-gap-analysis.md)).
- **Design Patterns Catalog**: Architectural security patterns including [Approval Checkpoint](../patterns/approval-checkpoint.md), [Kill Switch](../patterns/kill-switch.md), and [Attested Isolated Runtime](../patterns/attested-isolated-runtime.md)[^evt-wg-security-and-privacy-pr-25].

### Operational Governance
- **Deliverable Authoring Rules**: Pull request authors may not self-merge deliverables into the WG repository; changes require designated workstream lead sign-off[^evt-wg-security-and-privacy-pr-25].
- **Regional Participation**: The WG conducts dual-region meeting schedules, including an alternate-week APAC time slot to support global community engagement[^evt-wg-security-and-privacy-pr-25].

# Lifecycle History

- **September 2026**: Merged the Security Best Practices Guide as a living Draft deliverable and Threat Modeling Gap Analysis v0.1[^evt-wg-security-and-privacy-pr-25]. Released the initial Design Patterns Catalog drafts covering Approval Checkpoint, Kill Switch, and Attested Isolated Runtime[^evt-wg-security-and-privacy-pr-25]. Requested TC decision regarding formal bidirectional information exchange with ETSI TC SAI[^evt-wg-security-and-privacy-pr-25].

[^evt-wg-security-and-privacy-pr-25]: https://github.com/aaif/wg-security-and-privacy/pull/25
