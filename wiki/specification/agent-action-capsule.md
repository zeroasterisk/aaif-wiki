---
type: specification
title: Agent Action Capsule
description: A verifiable data structure used as a middle layer between regulations
  and agent actions, recording dispatched actions, outcomes, and verification status
  using cryptographic proofs.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/meeting-minutes/2026-09-02.md
tags:
- observability
- traceability
- security
- protocol
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-20T17:59:42.449434+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-ec358f3e3170-5d21c611
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/meeting-minutes/2026-09-02.md
  author: Pavan Sudheendra
  last_modified: '2026-09-03T14:11:22+01:00'
---

# Overview
The Agent Action Capsule is a data structure designed to serve as a middle layer between regulatory requirements and agent actions. It records what action was dispatched by the agent, what happened as a result, and whether the action was allowed to happen [^evt-wg-observability-and-traceability-file-ec358f3e3170-5d21c611].

# Specification
The capsule prevents tampering through the use of cryptographic proofs. It is designed to be verifiable, allowing the reconstruction of a complete execution trace from multiple capsules via a ledger system [^evt-wg-observability-and-traceability-file-ec358f3e3170-5d21c611]. The Observability and Traceability WG is exploring its integration with traceability efforts.

[^evt-wg-observability-and-traceability-file-ec358f3e3170-5d21c611]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/meeting-minutes/2026-09-02.md
