---
type: taxonomy
title: Action Record
description: Tamper-evident, content-private, independently verifiable record of a
  single consequential action taken by an AI agent.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/23
tags:
- taxonomy
- audit
- traceability
- verification
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T02:52:52.621158+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-23
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/23
  author: giskard09
  last_modified: '2026-08-20T14:27:37+00:00'
- id: evt-wg-observability-and-traceability-pr-30
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/30
  author: narko4u
  last_modified: '2026-08-23T09:50:09+00:00'
---

# Overview
An action record is a tamper-evident, content-private, and independently verifiable data artifact certifying a single consequential action executed by an AI agent [^evt-wg-observability-and-traceability-pr-23] [^evt-wg-observability-and-traceability-pr-30]. In contrast to comprehensive session traces that record multi-turn dialogues and reasoning paths, an action record isolates an atomic state transition, external tool execution, or contractual commitment performed across an execution boundary [^evt-wg-observability-and-traceability-pr-23].

It serves as a core primitive for zero-trust dispute resolution, allowing auditors, courts, or external counterparties to verify the integrity and provenance of a reported action without relying on the credibility of the host reporting it [^evt-wg-observability-and-traceability-pr-23] [^evt-wg-observability-and-traceability-pr-30].

# Architecture / Specification
Action records function as an orthogonal accountability primitive operating beneath full-session telemetry [^evt-wg-observability-and-traceability-pr-23]:

- **Third-Party Verifiability**: Provides portable verification primitives (such as `action_ref` or anchored hash references) that allow third-party validation without exposing proprietary context or sensitive execution payloads [^evt-wg-observability-and-traceability-pr-23].
- **Cryptographic Provenance**: Employs Merkle chaining, cryptographic signatures, and RFC 3161 timestamps to establish non-repudiation and prevent retroactive tampering [^evt-wg-observability-and-traceability-pr-30].
- **Declared vs. Observed Linkage**: Binds the agent's declared action intent directly to the cryptographic receipt observed at the runtime or network boundary [^evt-wg-observability-and-traceability-pr-30].
- **Trace Integration**: Acts as an anchorable leaf node within the [Agent Behavior Trace Model](../standards/agent-behavior-trace-model.md) to support evidence-grade accountability ladders.

# Lifecycle History
- **2026-07**: Surveyed alongside post-hoc verifiability frameworks (e.g., `action_ref`) and established as a foundational primitive for Use Case E4 audit and dispute resolution in the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md) [^evt-wg-observability-and-traceability-pr-23] [^evt-wg-observability-and-traceability-pr-30].

[^evt-wg-observability-and-traceability-pr-23]: https://github.com/aaif/wg-observability-and-traceability/pull/23
[^evt-wg-observability-and-traceability-pr-30]: https://github.com/aaif/wg-observability-and-traceability/pull/30
