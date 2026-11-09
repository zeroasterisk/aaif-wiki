---
type: pattern
title: Attested Isolated Runtime
description: Architectural security pattern isolating policy evaluation, credential
  release, and evidence signing inside hardware-attested trusted execution environments.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-attested-isolated-runtime.md
tags:
- security
- confidential-computing
- attestation
- runtime-isolation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:09:49.644342+00:00'
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
The Attested Isolated Runtime pattern isolates policy enforcement, credential release, and audit log signing inside a hardware-rooted Trusted Execution Environment (TEE) separate from untrusted host infrastructure.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb] Merged as the inaugural pattern under the privacy-preserving execution domain in the [Security and Privacy Design Patterns Catalog](../resources/security-and-privacy-design-patterns-catalog.md), it provides cryptographic verification for relying parties when the infrastructure operator lies within the threat model.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb][^evt-wg-security-and-privacy-pr-26]

# Architecture / Specification
The pattern formalizes a four-party stakeholder model comprising the data owner, agent operator, infrastructure operator, and relying party, structured across four foundational operational pillars:[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]

1. **Isolate Enforcement and Exclude Agent Workloads**: The policy evaluation engine, signing keys, and credential managers execute inside the hardware enclave, while large language model reasoning and agent orchestration remain outside to minimize the Trusted Computing Base (TCB).[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]
2. **Internal Key Generation**: Cryptographic signing and identity keys are generated strictly inside the enclave boundary and sealed to platform measurements, preventing host extractability.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]
3. **Policy Sealing and Data Release on Appraisal**: Decryption keys and policy rules are only released to the enclave after external verification of hardware attestation evidence against expected identity measurements.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]
4. **Per-Unit Verifiable Evidence**: The enclave produces signed evidence records for each atomic evaluation or tool invocation, which independent relying parties verify without inspecting underlying private prompt data.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]

## Inter-Pattern Relationships
- **[Kill Switch](../patterns/kill-switch.md)**: Relies on the attested enclave to safeguard credential revocation logic and prevent untrusted hosts from tampering with isolation policies.[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]
- **[Approval Checkpoint](../patterns/approval-checkpoint.md)**: Utilizes enclave-signed evidence to establish tamper-proof audit trails for policy decisions.[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]

# Lifecycle History
- Submitted to the design patterns workstream and merged via PR #26 as candidate architectural guidance for privacy-preserving execution.[^evt-wg-security-and-privacy-pr-26]

[^evt-wg-security-and-privacy-file-8fb7a6935b72-65c58be5]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-approval_checkpoint_pattern.md
[^evt-wg-security-and-privacy-file-d2691d0f1f64-8e9abf01]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-kill_switch_pattern.md
[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-attested-isolated-runtime.md
[^evt-wg-security-and-privacy-pr-26]: https://github.com/aaif/wg-security-and-privacy/pull/26
