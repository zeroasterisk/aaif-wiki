---
type: pattern
title: Attested Isolated Runtime
description: Architectural security pattern isolating policy evaluation and evidence
  signing inside hardware-attested enclaves to secure agent governance when operating
  on untrusted infrastructure.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-attested-isolated-runtime.md
tags:
- security
- confidential-computing
- attestation
- privacy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:21:56.668978+00:00'
sources:
- id: evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-attested-isolated-runtime.md
  author: sagardashora
  last_modified: '2026-09-30T10:16:03-04:00'
- id: evt-wg-security-and-privacy-pr-26
  resource: https://github.com/aaif/wg-security-and-privacy/pull/26
  author: sagardashora
  last_modified: '2026-09-30T14:16:03+00:00'
---

# Overview
The Attested Isolated Runtime pattern (also known as TEE-isolated agent runtime or confidential agent execution) isolates policy enforcement and audit evidence generation within a hardware-attested Trusted Execution Environment (TEE), leaving the primary agent workload outside the enclave boundary.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb] Developed by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md), the pattern addresses scenarios where an agent processes regulated or confidential data on infrastructure operated by an untrusted third party (such as public cloud providers or partner tenants), rendering policy verdicts, execution measurements, and audit trails tamper-evident against privileged host operators.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb][^evt-wg-security-and-privacy-pr-26]

# Architecture / Specification
The pattern structures confidential governance across four architectural requirements:

1. **Enforcement Isolation**: The policy enforcement point runs inside a hardware enclave while the LLM or agent runtime remains outside, mitigating the threat of privileged host inspection or in-memory manipulation.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]
2. **Enclave Key Generation**: Cryptographic signing keys are generated inside the enclave boundary and sealed to hardware measurement registers, ensuring that relying parties can verify that logs and decisions originated from untampered policy bundles.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]
3. **Policy Sealing and Appraisal**: Governance policies are sealed to specific measurement baselines, releasing secrets or authority credentials only when remote attestation appraisal succeeds.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]
4. **Verifiable Unit-of-Work Evidence**: Emits verifiable attestation evidence per transaction, enabling relying parties (such as peer agents, tool APIs, or external auditors) to appraise compliance without direct access to runtime infrastructure.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]

# Lifecycle History
Drafted as the initial pattern under the Privacy-Preserving Execution topic area in the [Security and Privacy Design Patterns Catalog](../resources/security-and-privacy-design-patterns-catalog.md).[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb][^evt-wg-security-and-privacy-pr-26] Works in tandem with [Kill Switch](kill-switch.md) for scoped credential release and [Approval Checkpoint](approval-checkpoint.md) for immutable decision logging.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]

# References
- Catalog Draft: `workstreams/design-patterns/DRAFT-attested-isolated-runtime.md`[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]

[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-attested-isolated-runtime.md
[^evt-wg-security-and-privacy-pr-26]: https://github.com/aaif/wg-security-and-privacy/pull/26
