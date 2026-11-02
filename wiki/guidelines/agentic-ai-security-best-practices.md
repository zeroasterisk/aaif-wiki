---
type: guideline
title: Agentic AI Security Best Practices
description: Actionable security implementation guide detailing threat models, kernel-enforced
  sandboxing, in-hook policy decision points, and MITRE ATLAS / OWASP ASI controls.
resource: https://github.com/aaif/wg-security-and-privacy/pull/39
tags:
- security
- threat-modeling
- sandbox
- authorization
- mitre-atlas
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:24:44.279360+00:00'
sources:
- id: evt-wg-security-and-privacy-pr-39
  resource: https://github.com/aaif/wg-security-and-privacy/pull/39
  author: barka-bee
  last_modified: '2026-10-12T12:30:29+00:00'
- id: evt-wg-security-and-privacy-pr-40
  resource: https://github.com/aaif/wg-security-and-privacy/pull/40
  author: barka-bee
  last_modified: '2026-10-12T12:41:45+00:00'
- id: evt-wg-security-and-privacy-pr-41
  resource: https://github.com/aaif/wg-security-and-privacy/pull/41
  author: barka-bee
  last_modified: '2026-10-12T12:51:05+00:00'
---

# Overview
The Agentic AI Security Best Practices guide establishes vendor-neutral implementation controls, threat mitigations, and architectural safeguards for agentic systems across execution runtimes, tool boundaries, and authorization workflows.[^evt-wg-security-and-privacy-pr-39] Developed by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md), the guide maps concrete operational countermeasures against taxonomy attack vectors such as [tool poisoning](../taxonomy/tool-poisoning.md) and [rug pulls](../taxonomy/rug-pull.md).[^evt-wg-security-and-privacy-pr-40]

The guide articulates explicit execution boundaries, clarifying that sandbox modes narrow the scope of exposure rather than providing absolute containment unless reinforced by kernel-level primitives.[^evt-wg-security-and-privacy-pr-41] Furthermore, runtime authorizations are governed through a multi-stage policy decision point at the hook, preventing compromised or prompt-injected agents from labeling their own exfiltration operations as routine.[^evt-wg-security-and-privacy-pr-39]

# Architecture / Specification

## Policy Decision Point at the Hook
Section 4 defines an authorization control architecture placing a Policy Decision Point (PDP) directly at the agent execution hook.[^evt-wg-security-and-privacy-pr-39] The PDP intercepts the complete invocation payload—including the target tool, call arguments, and run context—and returns one of four decisions: `allow`, `deny`, `modify`, or `ask`.[^evt-wg-security-and-privacy-pr-39] Keying decisions on full argument payloads ensures that destructive actions using common tools (e.g., shell executions or file deletions) are isolated from benign invocations.[^evt-wg-security-and-privacy-pr-39]

Evaluation proceeds across three decoupled stages where the originating agent has no execution or modification path into any evaluation tier:[^evt-wg-security-and-privacy-pr-39]
1. **Deterministic Rules Engine**: First-stage deterministic rules evaluate immutable constraints (such as immediate blocking of Tier 4 destructive destinations) prior to any hand-off.[^evt-wg-security-and-privacy-pr-39]
2. **Automated Secondary Classifier**: Calls handed off by deterministic rules undergo evaluation by an independent classifier, model, or deterministic verification agent.[^evt-wg-security-and-privacy-pr-39]
3. **Escalated Ask Path**: A human-in-the-loop approval gate is invoked solely when an `ask` verdict is rendered.[^evt-wg-security-and-privacy-pr-39] This design counters approval fatigue, grounded by empirical findings where 97% of unsegmented prompts are reflexively approved by operators and only 13.6% of human reviewers detect planted hazardous commands without automated pre-filtering.[^evt-wg-security-and-privacy-pr-39]

## Sandbox Confinement and Egress Boundaries
Section 3.2 specifies that sandbox execution modes narrow an unverified artifact's accessibility from the broader user account to an isolated working directory.[^evt-wg-security-and-privacy-pr-41] However, logical sandboxes do not guarantee isolation against network egress or external host execution unless supported by kernel-enforced mechanisms:[^evt-wg-security-and-privacy-pr-41]
- **Kernel Enforcement**: Full isolation requires kernel-enforced filesystem confinement, Linux namespaces, and syscall filtering (such as seccomp or [nono](../resources/nono.md)).[^evt-wg-security-and-privacy-pr-41]
- **Egress Gaps**: Application-level proxies that restrict standard utilities (e.g., `curl`) can be bypassed if the agent leverages secondary runtimes or HTTP client libraries; egress filtering must be strictly enforced at the network proxy layer with allowlisting.[^evt-wg-security-and-privacy-pr-41]
- **Host Component Escapes**: Sandboxes do not protect against attacks where the agent writes payloads to the filesystem that are subsequently executed by unconfined, trusted host processes outside the boundary.[^evt-wg-security-and-privacy-pr-41]

## Framework Mappings: MITRE ATLAS and OWASP ASI
Clauses across tool implementation, input/output validation, and execution controls are tagged against industry threat frameworks:[^evt-wg-security-and-privacy-pr-40]
- **MITRE ATLAS v5.6.0**: Key behaviors are aligned with ATLAS technique identifiers, including technique AML.T0109 (*AI Supply Chain Rug Pull*) applied to tool definition drift, hash verification, and silent package updates, alongside AML.T0110 and AML.T0051.001.[^evt-wg-security-and-privacy-pr-40]
- **OWASP Top 10 for Agentic Applications 2026**: Clauses map directly to Agentic Security Issues (ASI codes such as ASI02 and ASI04), enforcing controls such as the Rule of Two and mitigations for the lethal trifecta (autonomous write access, untrusted inputs, and unauthenticated tools).[^evt-wg-security-and-privacy-pr-40]

# Lifecycle History
The guide was initially drafted by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md). In October 2026, PR #39 restructured the Section 4 authorization framework behind an in-hook Policy Decision Point,[^evt-wg-security-and-privacy-pr-39] PR #40 introduced inline tagging against MITRE ATLAS v5.6.0 and OWASP ASI 2026,[^evt-wg-security-and-privacy-pr-40] and PR #41 refined Section 3.2 to detail the operational limits and kernel requirements of sandbox containment.[^evt-wg-security-and-privacy-pr-41]

[^evt-wg-security-and-privacy-pr-39]: https://github.com/aaif/wg-security-and-privacy/pull/39
[^evt-wg-security-and-privacy-pr-40]: https://github.com/aaif/wg-security-and-privacy/pull/40
[^evt-wg-security-and-privacy-pr-41]: https://github.com/aaif/wg-security-and-privacy/pull/41
