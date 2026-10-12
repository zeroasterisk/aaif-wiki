---
type: pattern
title: Attested Isolated Runtime
description: Architectural security pattern isolating policy enforcement and evidence
  signing inside hardware-attested trusted execution environments while leaving untrusted
  agent execution outside.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-attested-isolated-runtime.md
tags:
- security
- tee
- attestation
- patterns
- confidential-computing
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:36:11.485979+00:00'
sources:
- id: evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-attested-isolated-runtime.md
  author: sagardashora
  last_modified: '2026-09-30T10:16:03-04:00'
---

# Overview
The Attested Isolated Runtime pattern establishes verifiable policy evaluation and cryptographic evidence generation inside a hardware-isolated Trusted Execution Environment (TEE), separating policy enforcement from the untrusted agent workload.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb] Also known as confidential agent execution or an attested enclave gateway, the pattern addresses scenarios where an agent operates on sensitive, regulated, or classified data hosted on untrusted infrastructure such as public cloud regions, partner multi-tenant clusters, or customer environments subject to audit.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]

When the host platform and infrastructure operator are within the threat model, software-only controls cannot prevent host administrators or compromised host kernels from swapping policy bundles, tampering with in-memory decisions, or fabricating execution logs.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb] By constraining the enclave boundary strictly to policy evaluation, secret unsealing, and evidence signing while leaving the resource-heavy agent orchestration outside, the pattern minimizes the enclave trusted computing base.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]

# Architecture / Specification

## Architectural Roles
The pattern defines four discrete organizational roles with divergent security interests:[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]
- **Data Owner:** Requires that inputs and execution context remain confidential and unexposed during processing.
- **Agent Operator:** Executes the workload and seeks broad runtime adoptability across heterogeneous environments.
- **Infrastructure Operator:** Controls the host operating system, hypervisor, and orchestration fabric; sits inside the threat model.
- **Relying Party:** A downstream tool, peer agent, auditor, or regulator that verifies proof of compliance without directly inspecting private data.

## Core Mechanics
1. **Isolate the Enforcement Point:** The policy engine and cryptographic signing modules run inside a hardware TEE, while the primary agent process, LLM inference, and external tooling run in the untrusted host environment.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]
2. **Internal Key Generation:** Signing and sealing keys are generated inside the enclave boundary and cryptographically bound to hardware measurement registers, ensuring private keys cannot be extracted by the host.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]
3. **Measurement Sealing and Appraisal:** Policies are sealed to enclave measurement quotes. Protected state and execution authorization are released only after appraisal passes against expected reference measurements.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]
4. **Verifiable Evidence Emission:** The isolated runtime emits signed [Action Records](../taxonomy/action-record.md) for each discrete unit of work, enabling external relying parties to independently verify policy enforcement and execution integrity.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]

# Lifecycle History
The draft pattern was authored by the Design Patterns workstream within the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) as the first pattern in the privacy-preserving execution topic area, evaluated across five independent hardware attestation architectures.[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]

[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-attested-isolated-runtime.md
