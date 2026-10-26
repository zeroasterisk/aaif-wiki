---
type: pattern
title: Inherited Security Floor
description: Architectural pattern enforcing consistent security baselines across
  heterogeneous agent surfaces through single-source policy declaration and transport
  inheritance.
resource: https://github.com/aaif/wg-security-and-privacy/issues/29
tags:
- security
- patterns
- boundaries
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:45:03.901065+00:00'
sources:
- id: evt-wg-security-and-privacy-issue-29
  resource: https://github.com/aaif/wg-security-and-privacy/issues/29
  author: andreibesleaga
  last_modified: '2026-10-01T08:41:47+00:00'
---

# Overview

The Inherited Security Floor pattern (also described as Declare–Pin–Inherit–Prove) provides an architectural approach to preventing policy drift across disparate agent exposure surfaces [^evt-wg-security-and-privacy-issue-29]. Rather than permitting individual transports—such as local tool servers, browser client tools, static task boards, or agent-to-agent interfaces—to maintain independent security definitions, systems implementing this pattern require every surface to inherit an immutable security floor declared in a centralized discovery manifest [^evt-wg-security-and-privacy-issue-29].

This pattern was submitted as a candidate design pattern to the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) to address divergence in safety rules across multi-transport deployments [^evt-wg-security-and-privacy-issue-29].

# Architecture / Specification

The pattern organizes agent interface security around four operational principles [^evt-wg-security-and-privacy-issue-29]:

1. **Unified Tool Contracts and Payload Strictness**: Heterogeneous transports expose identical tool signatures and argument types, guaranteeing value equivalence across protocols. Result payloads enforce fixed metadata fields (`source`, `trust`, `license`, `type`, and `body`), with the `trust` attribute permanently pinned to `untrusted`. Arguments strictly accept opaque entity identifiers rather than raw file paths, URLs, or shell strings.
2. **Human-Gated Consequential Writes**: Modifying actions are isolated behind reviewed proposals and [human approval gates](../patterns/human-approval-gate.md). Transports lacking configuration authority (such as client-side browser execution) are restricted to local-only operations and forbidden from direct network mutation.
3. **Peer Fetching and SSRF Protection**: Inbound and outbound peer federation is constrained to HTTPS endpoints checked against IANA special-purpose address denial lists. The runtime enforces hop, fan-out, and redirect limits, re-verifying socket remote IP addresses post-connection to defeat DNS rebinding attacks.
4. **Static State Export**: Multi-agent boards (such as [agent-to-agent](../taxonomy/agent-to-agent.md) coordination boards) are published as immutable static files reflecting engine states verbatim, allowing peer consumption without exposing writable execution surfaces.

# Lifecycle History

Proposed in issue #29 within the AAIF Security and Privacy Working Group as candidate input for open threat models and design pattern deliverables [^evt-wg-security-and-privacy-issue-29]. It remains a draft community proposal pending formal alignment and working group consensus.

# References

- Security guidance: [Agentic AI Security Best Practices](../guidelines/agentic-ai-security-best-practices.md)
- Approval controls: [Human Approval Gate](../patterns/human-approval-gate.md)
- Governance: [Security and Privacy Working Group](../working-groups/security-and-privacy.md)

[^evt-wg-security-and-privacy-issue-29]: https://github.com/aaif/wg-security-and-privacy/issues/29
