---
type: pattern
title: Attested Isolated Runtime
description: Architectural security pattern isolating policy evaluation and evidence
  signing inside hardware-attested enclaves while keeping primary agent logic outside.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-attested-isolated-runtime.md
tags:
- security
- confidential-computing
- tee
- attestation
- patterns
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:38:42.139689+00:00'
sources:
- id: evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-attested-isolated-runtime.md
  author: sagardashora
  last_modified: '2026-09-30T10:16:03-04:00'
---

# Overview

The Attested Isolated Runtime pattern isolates runtime policy enforcement, verdict evaluation, and cryptographic evidence signing within a hardware-attested trusted execution environment (TEE), keeping the primary agent workload outside the enclave boundary [^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]. By decoupling policy enforcement from operator host privileges, the pattern ensures that relying parties can independently verify execution integrity even when the underlying host, hypervisor, or infrastructure operator is untrusted [^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb].

Also known as a TEE-isolated agent runtime, confidential agent execution, or an attested enclave gateway, this pattern addresses scenarios where an agent processes confidential or regulated data in third-party environments [^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb].

# Architecture / Specification

The pattern establishes distinct multi-organizational roles and operational constraints across four participants [^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]:

- **Data owner:** Requires that task inputs and context are not exposed during processing [^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb].
- **Agent operator:** Executes the agentic workload across external or hybrid cloud compute [^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb].
- **Infrastructure operator:** Controls the underlying host platform, hypervisors, and scheduling layers [^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb].
- **Relying party:** Evaluates execution integrity and policy adherence without direct inspection capability [^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb].

### Core Mechanisms

1. **External Enforcement Separation:** Rather than executing complex LLM harnesses inside constrained TEEs, policy evaluation points are isolated in the enclave while the agent runs outside [^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb].
2. **Enclave Key Generation:** Cryptographic signing keys are generated strictly inside the attested boundary, directly binding evidence artifacts to immutable hardware measurements [^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb].
3. **Policy Sealing:** Governance policies are sealed against hardware launch measurements and unlocked only upon valid appraisal by an attestation verifier [^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb].
4. **Verifiable Telemetry and Evidence:** Emits signed evidence records per unit of execution, enabling external verification via independent appraisal [^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb].

# Lifecycle History

Contributed as an initial design draft within the Security and Privacy Working Group's privacy-preserving execution workstream [^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]. Related runtime isolation approaches and sandboxing tooling include [resources/nono](../resources/nono.md) and related specifications such as [standards/evidence-record-spec](../standards/evidence-record-spec.md) [^evt-wg-security-and-privacy-file-3b2755238b15-1588e821].

[^evt-wg-security-and-privacy-file-d74b6b55d493-0ef833eb]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/workstreams/design-patterns/DRAFT-attested-isolated-runtime.md
