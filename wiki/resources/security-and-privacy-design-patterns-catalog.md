---
type: resource
title: Security and Privacy Design Patterns Catalog
description: Architectural catalog defining reusable, implementation-independent security
  and privacy design patterns for autonomous agentic systems.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-09-report.md
tags:
- security
- privacy
- patterns
- architecture
- catalog
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:29:55.745427+00:00'
sources:
- id: evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-09-report.md
  author: Alex Frazer
  last_modified: '2026-10-09T08:54:25-06:00'
- id: evt-wg-security-and-privacy-pr-25
  resource: https://github.com/aaif/wg-security-and-privacy/pull/25
  author: awfrazer
  last_modified: '2026-10-09T14:54:26+00:00'
---

# Overview
The Security and Privacy Design Patterns Catalog is an architectural resource curated by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) documenting reusable, implementation-neutral design patterns for securing agent systems.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]

Led by Sagar Dashora and Dan Kommatas, the catalog provides standardized design templates and reference specifications that address critical agentic risks such as runaway execution, unverified actions, and compromised runtime environments.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]

# Architecture / Specification
The catalog establishes a uniform pattern structure and incorporates initial foundational patterns:
- **Pattern Template**: Standardized schema ensuring consistency across problem statements, architectural diagrams, threat mappings, and implementation tradeoffs.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]
- **[Approval Checkpoint](../patterns/approval-checkpoint.md)**: Cryptographically or policy-bound authorization gates for high-impact actions.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]
- **[Kill Switch](../patterns/kill-switch.md)**: Independent, out-of-band containment mechanisms to immediately halt rogue or misbehaving agent processes.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]
- **[Attested Isolated Runtime](../patterns/attested-isolated-runtime.md)**: Hardware-attested, isolated execution boundaries safeguarding policy evaluation and secret handling.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]

# Lifecycle History
The catalog landing page and its first three architectural pattern drafts merged into `main` on 2026-09-30 via PR #26.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1] Subsequent work includes follow-up refinements and the development of memory-related security patterns.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]

[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-09-report.md
