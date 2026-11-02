---
type: taxonomy
title: Action Record
description: Tamper-evident, content-private, and independently verifiable record
  proving what an agent executed, distinct from operator telemetry and authorization
  grants.
resource: https://github.com/aaif/wg-identity-and-trust/blob/69e73d0e0a5005d4d44af40ffbd068807169f30f/reporting/2026-06-report.md
tags:
- taxonomy
- action-record
- evidence
- attestation
- identity
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T09:41:16.242857+00:00'
sources:
- id: evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758
  resource: https://github.com/aaif/wg-identity-and-trust/blob/69e73d0e0a5005d4d44af40ffbd068807169f30f/reporting/2026-06-report.md
  author: Alper Dedeoglu
  last_modified: '2026-08-04T00:23:33+02:00'
---

# Overview

An **Action Record** is a tamper-evident, content-private, independently verifiable record proving that an agent executed a specific, consequential action [^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758]. Distinct from operational telemetry, audit logs, and identity/authorization tokens, an action record serves as legal and technical evidence for external counterparties, auditors, or adjudicators [^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758].

# Architecture / Specification

Within the [Identity and Trust Working Group](../working-groups/identity-and-trust.md) taxonomy, action records maintain distinct functional boundaries [^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758]:

- **Boundary with Observability/Tracing:** Observability telemetry answers *"what is my agent doing?"* for internal operators during development, debugging, and performance monitoring. In contrast, an Action Record answers *"what did this agent verifiably do?"* for counterparties, compliance auditors, or courts [^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758].
- **Boundary with Authorization:** Identity tokens and authorization assertions attest to permissions granted *prior* to execution; Action Records attest to what took place *during or after* execution, binding the agent identity, intent, and delegation proof to the resulting artifact [^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758].
- **Selective Disclosure:** Action records support content privacy, allowing selective redaction or zero-knowledge revelation of sensitive parameters without invalidating third-party cryptographic verification [^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758].

# Lifecycle History

- **2026-07:** Formalized as a distinct concept within the Identity & Trust WG Taxonomy sub-group [^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758].

[^evt-wg-identity-and-trust-file-a17a580f85c2-1f6ad758]: https://github.com/aaif/wg-identity-and-trust/blob/69e73d0e0a5005d4d44af40ffbd068807169f30f/reporting/2026-06-report.md
