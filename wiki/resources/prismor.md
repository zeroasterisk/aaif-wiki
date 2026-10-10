---
type: resource
title: Prismor
description: Self-hosted runtime control plane and proxy intercepting agent tool calls
  to enforce policy-as-code and audit logging.
resource: https://github.com/aaif/project-proposals/issues/51
tags:
- security
- policy-as-code
- mcp-gateway
- runtime-guardrails
- sandbox-proposal
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:18:03.150039+00:00'
sources:
- id: evt-project-proposals-issue-51
  resource: https://github.com/aaif/project-proposals/issues/51
  author: Ar9av
  last_modified: '2026-10-02T02:31:33+00:00'
---

# Overview
Prismor is an open-source, self-hosted control plane for AI agents that performs tool call interception and evaluates actions against versioned policy-as-code before execution.[^evt-project-proposals-issue-51] It acts as a runtime governance layer that issues allow, block, transform, or human approval verdicts independently of model-context instructions.[^evt-project-proposals-issue-51]

# Architecture / Specification
Prismor provides runtime enforcement across multiple deployment touchpoints using a unified policy engine:[^evt-project-proposals-issue-51]

- **MCP Gateway Proxy**: Intercepts downstream `tools/call` invocations across [mcp-gateway-registry](../resources/mcp-gateway-registry.md) routes, evaluating arguments before forwarding and scanning returned payloads before context re-entry.[^evt-project-proposals-issue-51]
- **In-Process SDK Adapters & Coding Hooks**: Integrates directly into agent runtimes and coding harnesses to intercept tool executions at the client boundary.[^evt-project-proposals-issue-51]
- **Evaluation Modes**: Supports *observe mode* for auditing and impact measurement without disruption, and *enforce mode* for deterministic intervention and blocking.[^evt-project-proposals-issue-51]
- **Policy-as-Code Engine**: Ingests declarative YAML policies scoped across organization, project, repository, or session levels, generating signed audit trails and attestation bundles.[^evt-project-proposals-issue-51]

# Lifecycle History
Originally created as `immunity-agent`, the project was rebranded to `prismor` in 2026 and submitted to the AAIF as a proposed Sandbox project to provide runtime policy enforcement complementing agent protocols and frameworks.[^evt-project-proposals-issue-51]

[^evt-project-proposals-issue-51]: https://github.com/aaif/project-proposals/issues/51
