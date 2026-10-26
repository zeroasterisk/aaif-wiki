---
type: taxonomy
title: Action Record
description: Tamper-evident, content-private, and independently verifiable record
  proving what an agent executed, requested, or was denied during runtime execution.
resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
tags:
- taxonomy
- security
- audit
- traceability
- provenance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:51:37.206517+00:00'
sources:
- id: evt-wg-governance-risk-and-regulatory-issue-9
  resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
  author: narko4u
  last_modified: '2026-10-08T03:11:06+00:00'
---

# Overview
An action record is a tamper-evident, content-private, and verifiable record detailing actions executed, proposed, or denied during an agent's lifecycle. Rather than generic runtime logs or [self-reported](../taxonomy/self-reported.md) operational telemetry, an action record provides cryptographic and architectural guarantees enabling external auditors and systems to verify execution history independently.

# Architecture / Specification
Emerging international standards, including ISO/IEC 24970, prEN 18229-1, and IETF draft-sharif-agent-audit-trail, demonstrate structural convergence on the canonical shape of agent audit records[^evt-wg-governance-risk-and-regulatory-issue-9]:

- **Hash-Chaining and Integrity**: Records utilize cryptographic hashing to form immutable chains resistant to retroactive modification[^evt-wg-governance-risk-and-regulatory-issue-9].
- **Recording-Independence Gradient**: High-trust actions cannot rely solely on the acting agent as the single recorder, requiring independent observer or harness attestation[^evt-wg-governance-risk-and-regulatory-issue-9].
- **Pre-Execution Capture**: Mandatory pre-execution logging for denied actions, policy halts, and human escalations prior to external side effects[^evt-wg-governance-risk-and-regulatory-issue-9].
- **Temporal Anchoring**: Incorporation of deterministic local timestamps with support for external timestamp anchoring services[^evt-wg-governance-risk-and-regulatory-issue-9].
- **Decision Reproducibility Metadata**: Structured payload schemas capturing context, model identifiers, policy constraints, and prompt inputs necessary to reconstruct decisions during audits[^evt-wg-governance-risk-and-regulatory-issue-9].

# References
- [Governance, Risk, and Regulatory Working Group](../working-groups/governance-risk-and-regulatory.md)
- [Evidence Record Specification](../standards/evidence-record-spec.md)
- [Attested Isolated Runtime](../patterns/attested-isolated-runtime.md)

[^evt-wg-governance-risk-and-regulatory-issue-9]: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/9
