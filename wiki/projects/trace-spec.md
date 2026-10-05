---
type: project
title: TRACE Specification
description: Open specification and verification suite for signed, verifiable agent
  execution trust records and hardware runtime attestations.
resource: https://github.com/aaif/project-proposals/issues/42
tags:
- project
- attestation
- security
- compliance
- tee
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T06:00:17.540946+00:00'
sources:
- id: evt-project-proposals-issue-42
  resource: https://github.com/aaif/project-proposals/issues/42
  author: imran-siddique
  last_modified: '2026-10-02T02:32:06+00:00'
---

# Overview
The TRACE (Trust, Runtime Attestation, and Compliance Evidence) Specification defines an open, vendor-neutral format for generating signed, verifiable evidence records of AI agent executions that can be appraised by third parties without requiring trust in the executing operator[^evt-project-proposals-issue-42]. A TRACE Trust Record binds executed model identifiers and weights digests, platform execution environments and hardware measurements, policy bundles, data classification tags, and tool call transcripts into a tamper-evident structure[^evt-project-proposals-issue-42].

# Architecture / Specification
TRACE builds upon established IETF cryptographic and attestation standards: RFC 9711 (CBOR/JSON Encoded Attestation Token / EAT), RFC 9334 (Remote Attestation Procedures / RATS), RFC 8785 (Canonical JSON), and SCITT transparency logging[^evt-project-proposals-issue-42]. The specification defines three distinct conformance tiers[^evt-project-proposals-issue-42]:
- **Level 0 (Software Signed)**: Digitally signed claims for first-party internal auditing and non-confidential environments.
- **Level 1 (Hardware Attested)**: Cryptographically anchored to hardware Trusted Execution Environments (TEEs) and security modules (including Intel TDX, AMD SEV-SNP, NVIDIA H100/Blackwell, AWS Nitro, Arm CCA, Google Confidential Space, and TPM 2.0).
- **Level 2 (Transparency Anchored)**: Augments hardware attestation with public, append-only inclusion proofs registered on transparency ledgers.

# Protocol Interoperability
TRACE operates out-of-band alongside core agent protocols:
- **Model Context Protocol (MCP)**: Tool transcripts bind session tool invocations through gateway envelopes like cMCP[^evt-project-proposals-issue-42].
- **Agent-to-Agent (A2A)**: Multi-hop delegation graphs bind parent record hashes across tasks orchestrated through [A2A](../projects/a2a.md)[^evt-project-proposals-issue-42].

# Lifecycle History
Announced under Linux Foundation Projects, LLC in August 2026 with contributions from AMD, Intel, Microsoft, OPAQUE, and TII, TRACE was submitted as a project proposal to AAIF in September 2026[^evt-project-proposals-issue-42].

[^evt-project-proposals-issue-42]: https://github.com/aaif/project-proposals/issues/42
