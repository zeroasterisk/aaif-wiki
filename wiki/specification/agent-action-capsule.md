---
type: specification
title: Agent Action Capsule
description: A structured data format and mechanism serving as a middle layer between
  regulations and agent actions, recording dispatch, outcome, and verification status.
resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/meeting-minutes/2026-09-02.md
tags:
- observability
- traceability
- security
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-flash-latest
  at: '2026-09-21T10:05:10.819356+00:00'
sources:
- id: evt-wg-observability-and-traceability-file-ec358f3e3170-5d21c611
  resource: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/meeting-minutes/2026-09-02.md
  author: Pavan Sudheendra
  last_modified: '2026-09-03T14:11:22+01:00'
---

# Overview
The Agent Action Capsule is a proposed specification designed to serve as a middle layer between regulations and agent actions [^evt-wg-observability-and-traceability-file-ec358f3e3170-5d21c611].

It records key information about an agent's operation: what was dispatched, what happened, and whether the action was allowed to happen. This mechanism is intended to prevent tampering through the use of cryptographic proofs [^evt-wg-observability-and-traceability-file-ec358f3e3170-5d21c611].

# Architecture / Specification
The capsule enables verification and reconstruction of complete execution traces from multiple capsules via a ledger system. It is being explored for integration with existing traceability and observability efforts, particularly within the Observability and Traceability Working Group [^evt-wg-observability-and-traceability-file-ec358f3e3170-5d21c611].

[^evt-wg-observability-and-traceability-file-ec358f3e3170-5d21c611]: https://github.com/aaif/wg-observability-and-traceability/blob/360a22ba283785f22b215e8ff38c721a8c6cdca8/meeting-minutes/2026-09-02.md
