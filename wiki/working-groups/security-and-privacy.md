---
type: working-group
title: Security and Privacy Working Group
description: Technical working group establishing threat models, security best practices,
  design patterns, and cross-surface boundary controls.
resource: https://github.com/aaif/wg-security-and-privacy/issues/29
tags:
- governance
- working-groups
- security
- threat-modeling
- privacy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T03:13:00.577812+00:00'
sources:
- id: evt-wg-security-and-privacy-issue-29
  resource: https://github.com/aaif/wg-security-and-privacy/issues/29
  author: andreibesleaga
  last_modified: '2026-10-01T08:41:47+00:00'
---

# Overview

The Security and Privacy Working Group establishes open threat models, security best practices, architectural defense patterns, and boundary protection standards for agentic AI deployments across the Agentic AI Foundation[^evt-wg-security-and-privacy-issue-29]. The group's scope covers runtime isolation, tool invocation controls, prompt defense, and multi-agent network boundaries.

# Architecture / Specification

The working group actively researches and standardizes key security deliverables:

- **Cross-Surface Security Floors:** Evaluating design patterns (such as 'declare-pin-inherit-prove') where node publishers declare their exposed interaction surfaces in discovery documents and inherit a single unified security floor rather than managing divergent safety baselines across interfaces[^evt-wg-security-and-privacy-issue-29].
- **Tool and Payload Strictness:** Defining input validation standards where tool arguments require typed identifiers over raw paths or shell commands, JSON output envelopes maintain fixed untrusted trust annotations, and natural language fields are treated strictly as data[^evt-wg-security-and-privacy-issue-29].
- **Network and SSRF Mitigations:** Formulating transport constraints for peer discovery and task delegation, including mandatory HTTPS, IANA special-purpose address rejection, hop-by-hop redirect evaluation, and post-connection socket address re-verification to counter DNS rebinding[^evt-wg-security-and-privacy-issue-29].
- **Boundary Authorizations:** Coordinating with governance patterns such as the [proposal-execution split](../patterns/proposal-execution-split.md) and [human-approval gate](../patterns/human-approval-gate.md) to ensure external modifications require explicit, reviewable human sign-off[^evt-wg-security-and-privacy-issue-29].

# Lifecycle History

Chartered to deliver foundational threat models and operational security guidance, the group regularly reviews community contributions. Issue #29 introduced proposals for inherited surface security baselines and strict payload controls as prospective inputs for the group's design-pattern deliverables[^evt-wg-security-and-privacy-issue-29].

[^evt-wg-security-and-privacy-issue-29]: https://github.com/aaif/wg-security-and-privacy/issues/29
