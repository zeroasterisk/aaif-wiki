---
type: guideline
title: Agentic AI Security Best Practices
description: Practical implementation guidance, control feature matrix, and architectural
  controls across people, process, and technology pillars.
resource: https://github.com/aaif/wg-security-and-privacy/pull/20
tags:
- security
- best-practices
- governance
- controls
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:59:46.074542+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-20
  resource: https://github.com/aaif/wg-security-and-privacy/pull/20
  author: erinmfarr
  last_modified: '2026-10-01T17:23:21+00:00'
---

# Overview
The Agentic AI Security Best Practices guideline provides defensive architectural controls, operational procedures, and implementation patterns for securing autonomous agent deployments [^evt-wg-security-and-privacy-pr-20]. Maintained by the [Security & Privacy Working Group](../working-groups/security-and-privacy.md), it links technical enforcement mechanisms with organizational governance and skills training [^evt-wg-security-and-privacy-pr-20].

# Architecture / Specification
The guideline organizes security controls across a three-pillar feature matrix to ensure balanced implementation [^evt-wg-security-and-privacy-pr-20]:

- **People**: Features requiring specialized training, operational skills, security awareness, and human readiness across all personnel interacting with agentic systems [^evt-wg-security-and-privacy-pr-20].
- **Process**: Features requiring formalized policies, documented operational procedures, compliance reviews, and governance strategies for security execution [^evt-wg-security-and-privacy-pr-20].
- **Technology**: Features enforced via physical or digital tools, hardware roots of trust, runtime execution sandboxes, automated authorization gates, and cryptographic telemetry pipelines [^evt-wg-security-and-privacy-pr-20].

These capabilities directly inform runtime patterns such as the [Attested Isolated Runtime](../patterns/attested-isolated-runtime.md) and [Kill Switch](../patterns/kill-switch.md).

[^evt-wg-security-and-privacy-pr-20]: https://github.com/aaif/wg-security-and-privacy/pull/20
