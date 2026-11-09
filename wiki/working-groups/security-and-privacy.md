---
type: working-group
title: Security and Privacy Working Group
description: Technical working group establishing open threat models, security design
  patterns, and operational controls for agentic AI systems.
resource: https://github.com/aaif/wg-security-and-privacy/pull/43
tags:
- working-group
- security
- privacy
- threat-modeling
- aaif
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:29:37.606945+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-43
  resource: https://github.com/aaif/wg-security-and-privacy/pull/43
  author: awfrazer
  last_modified: '2026-10-30T16:49:49+00:00'
---

# Overview

The Security and Privacy Working Group is an AAIF technical body developing vendor-neutral threat models, architectural security patterns, and operational best practices for agentic AI deployments.[^evt-wg-security-and-privacy-pr-43] The working group establishes runtime boundary controls, cross-working-group review criteria, and defensive design patterns addressing agent-specific vulnerabilities such as privilege escalation, context poisoning, and unauthorized tool execution.[^evt-wg-security-and-privacy-pr-43]

# Architecture / Specification

The working group coordinates several foundational security workstreams across the foundation:[^evt-wg-security-and-privacy-pr-43]

- **Best Practices Guide**: A living operational manual detailing runtime hook enforcement, credential boundaries, and network gating; opened to external community contributions in October 2026 under designated maintainer reviews.[^evt-wg-security-and-privacy-pr-43]
- **Agentic Threat Modeling**: An analytical framework synthesizing STRIDE and PASTA methodologies with MITRE ATLAS and OWASP Artificial Security Intelligence (ASI) matrices to classify agent failure modes.[^evt-wg-security-and-privacy-pr-43]
- **Design Patterns Catalog**: A library of reusable architectural controls, including the [Kill Switch](../patterns/kill-switch.md) pattern and containment mechanisms for credential revocation protocols.[^evt-wg-security-and-privacy-pr-43]
- **Cross-WG Security Review Checklist**: Review workflows aligning observability, [Agentic Commerce](../working-groups/agentic-commerce.md), and governance workstreams against unified baseline controls.[^evt-wg-security-and-privacy-pr-43]

# Lifecycle History

- **2026-10-26**: Merged core security and privacy vocabulary into the foundation-wide cross-WG taxonomy.[^evt-wg-security-and-privacy-pr-43]
- **2026-10-27**: Reviewed kill switch credential revocation protocol mappings within the design patterns track.[^evt-wg-security-and-privacy-pr-43]
- **2026-10**: Launched an alternate-week APAC meeting track on Mondays at 9 pm Eastern to support distributed global community participation.[^evt-wg-security-and-privacy-pr-43]

[^evt-wg-security-and-privacy-pr-43]: https://github.com/aaif/wg-security-and-privacy/pull/43
