---
type: working-group
title: Identity and Trust Working Group
description: AAIF technical working group establishing vendor-neutral architectures,
  delegation models, attestation formats, and authority verification for autonomous
  agents.
resource: https://github.com/aaif/wg-identity-and-trust/pull/17
tags:
- working-groups
- identity
- trust
- attestation
- authorization
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:53:39.874323+00:00'
sources:
- id: evt-wg-identity-and-trust-pr-17
  resource: https://github.com/aaif/wg-identity-and-trust/pull/17
  author: astrogilda
  last_modified: '2026-10-10T23:53:46+00:00'
---

# Overview

The Identity and Trust Working Group establishes vendor-neutral architectures, cryptographic delegation models, attestation standards, and authority verification mechanisms for autonomous agents. The group coordinates identity standards across execution boundaries to ensure verifiability and non-repudiation in multi-agent and human-agent collaborations.

# Architecture / Specification

The working group's technical deliverables focus on runtime delegation and dispatch-time authority verification:

- **Authority-at-Dispatch Catalogue**: A comparative benchmark evaluating authority verification architectures (including MintID, Proofable, and Alakris reference runs) at the exact moment of tool or task dispatch [^evt-wg-identity-and-trust-pr-17].
- **Versioned Contract Identifiers**: Trace requirements mandating that execution traces include explicit, versioned contract identifiers; readers reject traces lacking these identifiers [^evt-wg-identity-and-trust-pr-17].
- **Evidence Freshness Limits**: Explicit limits and age metadata embedded within authority evidence to prevent replay attacks and out-of-date credential utilization [^evt-wg-identity-and-trust-pr-17].
- **Observer Automation**: Integration with automated readers like `agent-evidence-observer` to run reference test cases and validate traces in CI workflows [^evt-wg-identity-and-trust-pr-17].

# References

- [Evidence Record Specification](../standards/evidence-record-spec.md)
- [Agent Behavior Trace Model](../standards/agent-behavior-trace-model.md)
- [Hardware-Bound Human Authorization](../patterns/hardware-bound-human-authorization.md)

[^evt-wg-identity-and-trust-pr-17]: https://github.com/aaif/wg-identity-and-trust/pull/17
