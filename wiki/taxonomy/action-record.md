---
type: taxonomy
title: Action Record
description: Tamper-evident, content-private, and independently verifiable record
  proving what an agent executed for counterparties, auditors, and courts.
resource: https://github.com/aaif/wg-identity-and-trust/blob/69e73d0e0a5005d4d44af40ffbd068807169f30f/reporting/2026-06-report.md
tags:
- identity
- trust
- audit
- governance
- taxonomy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:07:27.988549+00:00'
sources:
- id: evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758
  resource: https://github.com/aaif/wg-identity-and-trust/blob/69e73d0e0a5005d4d44af40ffbd068807169f30f/reporting/2026-06-report.md
  author: Alper Dedeoglu
  last_modified: '2026-08-04T00:23:33+02:00'
---

# Overview
An Action Record is a tamper-evident, content-private, independently verifiable record of a single consequential action taken by an agent.[^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758] It provides cryptographic and evidentiary proof answering "what did this agent verifiably do?" for counterparties, auditors, or legal authorities, distinct from internal operational logs.[^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758]

# Boundary Distinctions
The Action Record occupies a distinct technical boundary from observability telemetry and identity tokens:[^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758]
- **Observability and Tracing:** Internal execution telemetry answers "what is my agent doing?" for the operator managing execution flow.[^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758] Action records answer "what did this agent verifiably do?" for an external recipient or verifying counterparty.[^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758]
- **Identity and Authorization:** Identity artifacts and OAuth tokens authorize an agent to act, whereas the action record proves what specific consequence occurred under that authority, maintaining content privacy through selective disclosure.[^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758]
- **Consent Receipts:** Consent artifacts establish authorization granted by a principal, whereas an action record binds that consent and delegation chain to the executed state changes.[^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758]

# Architecture / Specification
Within the [WG Identity and Trust](../working-groups/identity-and-trust.md) framework, Action Records incorporate several architectural requirements:[^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758]
- **Tamper Evidence:** Cryptographically signed and structured so that post-execution modifications invalidate verification proofs.[^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758]
- **Content Privacy and Selective Disclosure:** Verifiers can confirm that an authorized action took place within valid parameters without exposing sensitive internal payloads or operational context.[^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758]
- **Delegation Binding:** Binds actions back through the agent delegation chain to ensure permissions do not exceed initiating user entitlements.[^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758]

[^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758]: https://github.com/aaif/wg-identity-and-trust/blob/69e73d0e0a5005d4d44af40ffbd068807169f30f/reporting/2026-06-report.md
