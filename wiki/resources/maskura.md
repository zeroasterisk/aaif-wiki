---
type: resource
title: Maskura
description: Open-source policy boundary proxy intercepting agent S3 storage calls
  to enforce PII redaction, hybrid post-quantum encryption, and passkey approvals.
resource: https://github.com/aaif/project-proposals/issues/62
tags:
- storage
- security
- privacy
- policy
- encryption
- s3
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T11:08:09.484639+00:00'
sources:
- id: evt-project-proposals-issue-62
  resource: https://github.com/aaif/project-proposals/issues/62
  author: amit231self
  last_modified: '2026-10-22T16:37:52+00:00'
---

# Overview

Maskura is an open-source security and policy boundary proxy operating between autonomous AI agents and S3-compatible object storage backends[^evt-project-proposals-issue-62]. Created by Amit Mor (231self) and submitted as an AAIF Sandbox proposal under the Apache-2.0 license, Maskura provides a mediation layer governing which data representation—plaintext, PII-filtered, or envelope-encrypted—crosses into agent or tool context[^evt-project-proposals-issue-62].

# Architecture / Specification

## Storage Interception and Cryptographic Controls

Maskura exposes an S3-compliant interface supporting AWS CLI/SDK clients, Model Context Protocol servers, and direct agent calls with streaming and multipart upload support[^evt-project-proposals-issue-62]:
- **PII Filtering**: Automated redaction and masking applied to object representations before data is dispatched to models or agent harnesses[^evt-project-proposals-issue-62].
- **Post-Quantum Hybrid Envelope Encryption**: Per-field encryption combining X25519 and ML-KEM-768 with AES-256-GCM, maintaining legacy RSA-OAEP decrypt support[^evt-project-proposals-issue-62].
- **Sandboxed Transforms**: In-flight data transformation pipelines executed inside WebAssembly sandboxes powered by Wasmtime[^evt-project-proposals-issue-62].
- **Signed Policy and Passkey Approvals**: Policy updates signed with Ed25519 and encoded in CBOR, paired with WebAuthn passkey approvals producing verifiable evidence bundles[^evt-project-proposals-issue-62].
- **Agent Identity Scoping**: Per-key workspace boundaries restricting agent access to dedicated storage partitions[^evt-project-proposals-issue-62].

## Working Group Alignment

Maskura coordinates with several AAIF working groups:
- [Identity & Trust Working Group](../working-groups/identity-and-trust.md): Scoped credentials and policy-bound object access across storage APIs[^evt-project-proposals-issue-62].
- [Security & Privacy Working Group](../working-groups/security-and-privacy.md): Fail-closed policy gates, isolated transform sandboxes, and auditable evidence outputs[^evt-project-proposals-issue-62].
- [Governance, Risk, and Regulatory Working Group](../working-groups/governance-risk-and-regulatory.md): Verifiable records documenting exact policy executions and agent data visibility[^evt-project-proposals-issue-62].

# Lifecycle History

- **October 2026**: Submitted to the Technical Committee as an open-source project proposal for the AAIF Sandbox stage (Issue #62)[^evt-project-proposals-issue-62].

# References

- [Maskura Repository](https://github.com/231self/maskura)
- [AAIF Project Proposal #62](https://github.com/aaif/project-proposals/issues/62)

[^evt-project-proposals-issue-62]: https://github.com/aaif/project-proposals/issues/62
