---
type: resource
title: Agentic AI Landscape
description: Interactive CNCF Landscape2 market map and project directory cataloging
  runtimes, protocols, security guardrails, observability stacks, and attestation
  systems.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/44
tags:
- ecosystem
- landscape
- architecture
- attestation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:49:00.800948+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-44
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/44
  author: imran-siddique
  last_modified: '2026-09-28T20:30:37+00:00'
---

# Overview
The Agentic AI Landscape provides an interactive, structured overview of open-source and member-driven projects, protocols, runtimes, and tooling across the agent ecosystem [^evt-ws-taxonomy-landscape-pr-44]. Maintained by the [Taxonomy and Landscape Workstream](../workstreams/taxonomy-and-landscape.md), it organizes technologies across core functional layers to ensure architectural clarity and discoverability.

# Architecture / Specification
The landscape is structured into defined categories and subcategories that reflect the lifecycle and operational boundaries of AI agents [^evt-ws-taxonomy-landscape-pr-44]:

- **Security Guardrails & Firewalls**: Preventative boundary controls, policy enforcement points, and prompt safety filters operating before execution.
- **Observability & Tracing Telemetry**: Runtime monitoring, tracing, metrics collection, and evaluation telemetry capturing execution paths while and after actions occur [^evt-ws-taxonomy-landscape-pr-44].
- **Attestation & Verifiable Evidence**: Mechanisms and standards providing third-party verifiable proof without requiring total trust in the execution operator [^evt-ws-taxonomy-landscape-pr-44]. Subcategories include:
  - *Attestation Standards & Verification*: Hardware and enclave verification frameworks including IETF RATS, Veraison, and Keylime [^evt-ws-taxonomy-landscape-pr-44].
  - *Transparency & Provenance*: Supply chain and transparency ledgers including IETF SCITT, in-toto, Sigstore, and SLSA [^evt-ws-taxonomy-landscape-pr-44].
  - *Agent Action & Runtime Evidence*: Signed execution proof and action capsules such as Agent Action Capsule, TRACE, and Agent Manifest [^evt-ws-taxonomy-landscape-pr-44].

# Lifecycle History
Proposed additions to the landscape schema require cross-working-group review, notably spanning [Identity and Trust](../working-groups/identity-and-trust.md), [Security and Privacy](../working-groups/security-and-privacy.md), and [Governance, Risk, and Regulatory](../working-groups/governance-risk-and-regulatory.md) working groups prior to final inclusion [^evt-ws-taxonomy-landscape-pr-44].

[^evt-ws-taxonomy-landscape-pr-44]: https://github.com/aaif/ws-taxonomy-landscape/pull/44
