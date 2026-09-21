---
type: landscape
title: Interactive map categorizing agent runtimes, protocols, security guardrails,
  observability, commerce
description: Interactive map categorizing agent runtimes, protocols, security guardrails,
  observability, commerce
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/28
tags:
- landscape
- taxonomy
- validation
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-21T10:11:02.862187+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-28
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/28
  author: thc1006
  last_modified: '2026-09-16T17:42:00+00:00'
- id: evt-ws-taxonomy-landscape-pr-44
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/44
  author: imran-siddique
  last_modified: '2026-09-16T17:42:29+00:00'
---

# Overview
The AAIF Landscape is an interactive map categorizing agent runtimes, protocols, security guardrails, observability, commerce, and related projects and specifications.

The landscape data structure (`landscape.yml`) is subject to strict validation checks during continuous integration (CI). These checks enforce schema conformance, field length limits, size caps (e.g., 512 KB byte cap, 500 item limit), and reject YAML features like aliases, cycles, and merge keys to ensure reliable parsing and rendering [^evt-ws-taxonomy-landscape-pr-28].

# Architecture / Specification
A proposed structural update introduces a new top-level category to cover projects focused on verifiable evidence [^evt-ws-taxonomy-landscape-pr-44]:

**Category: Attestation & Verifiable Evidence**
This category holds projects providing evidence a third party can verify without trusting the operator, filling a gap between prevention (Security Guardrails) and monitoring (Observability & Tracing Telemetry) [^evt-ws-taxonomy-landscape-pr-44].

Subcategories include:
1.  **Attestation Standards & Verification:** (e.g., IETF RATS, Veraison, Keylime)
2.  **Transparency & Provenance:** (e.g., IETF SCITT, in-toto, Sigstore, SLSA)
3.  **Agent Action & Runtime Evidence:** (e.g., [specification/agent-action-capsule](../specification/agent-action-capsule.md), TRACE, Agent Manifest) [^evt-ws-taxonomy-landscape-pr-44]

[^evt-ws-taxonomy-landscape-pr-28]: https://github.com/aaif/ws-taxonomy-landscape/pull/28
[^evt-ws-taxonomy-landscape-pr-44]: https://github.com/aaif/ws-taxonomy-landscape/pull/44
