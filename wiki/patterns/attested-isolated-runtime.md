---
type: pattern
title: Attested Isolated Runtime
description: Architectural security pattern isolating policy enforcement and evidence
  signing inside hardware-attested enclaves while bounding guest software bearer token
  lifecycles.
resource: https://github.com/aaif/wg-security-and-privacy/issues/37
tags:
- pattern
- security
- confidential-computing
- attestation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T10:51:49.114172+00:00'
sources:
- id: evt-wg-security-and-privacy-issue-37
  resource: https://github.com/aaif/wg-security-and-privacy/issues/37
  author: imran-siddique
  last_modified: '2026-10-05T15:26:00+00:00'
---

# Overview
The Attested Isolated Runtime pattern executes agent policy engines, cryptographic signing keys, and privileged tool execution environments within hardware-enforced trusted execution environments (TEEs) or confidential virtual machines. By decoupling runtime trust from the underlying host and hypervisor, the pattern provides remote attestation of software integrity and protects sensitive memory state against infrastructure operators and adjacent tenants.

# Architecture / Specification

## Enclave Isolation and Remote Attestation
The runtime leverages hardware TEE mechanisms (such as AMD SEV-SNP, Intel TDX, or ARM CCA) to guarantee memory encryption and state isolation:
- **Cryptographic Measurement:** Emits hardware-signed measurement quotes verifying the firmware, kernel, and agent runtime layers before cluster admission.
- **Report Payload Claims:** Attestation report payloads (such as Azure confidential VM REPORT_DATA) bind a cryptographic hash of runtime claims, including the virtual TPM key, guest configuration, and caller-supplied data[^evt-wg-security-and-privacy-issue-37].
- **Evidence Signing:** Signs [action records](../taxonomy/action-record.md) and telemetry directly within the protected boundary using hardware-derived keys.

## Threat Model Scope and Credential Exposure Boundaries
Security Working Group analysis defines the precise boundaries of hardware isolation models[^evt-wg-security-and-privacy-issue-37]:
- **Guest Software within TCB:** Hardware attestation defends guest memory against unauthorized hypervisor and host access, but guest application software remains inside the trusted computing base[^evt-wg-security-and-privacy-issue-37].
- **Bearer Token Lifespans:** Hardware enclaves do not compress or limit token lifetimes; if a guest component or agent tool leaks a bearer token, the exposure window is determined by token validity and revocation mechanisms, while the blast radius is governed by token permissions[^evt-wg-security-and-privacy-issue-37].
- **Layered Controls:** Enclave isolation must operate in tandem with short-lived, narrowly scoped credentials and internal compartmentalization restricting which guest components may access sensitive tokens[^evt-wg-security-and-privacy-issue-37].

# Lifecycle History
Established by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) as a foundational hardware-attested trust pattern. Enclave threat model boundaries and bearer token lifetime specifications clarified during post-merge review discussions[^evt-wg-security-and-privacy-issue-37].

[^evt-wg-security-and-privacy-issue-37]: https://github.com/aaif/wg-security-and-privacy/issues/37
