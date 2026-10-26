---
type: resource
title: Agent Observability Prior Work Survey
description: Comparative landscape survey and evaluation of external standards, specifications,
  and platforms across multi-layer agent telemetry and verifiable execution.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/23
tags:
- resource
- observability
- telemetry
- survey
- standards
- traceability
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-26T10:14:59.044657+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-23
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/23
  author: giskard09
  last_modified: '2026-08-20T14:27:37+00:00'
---

# Overview
The Agent Observability Prior Work Survey is an AAIF landscape evaluation documenting existing telemetry specifications, logging frameworks, and verification protocols across the agentic ecosystem [^evt-wg-observability-and-traceability-pr-23]. Developed by the [Observability & Traceability Working Group](../working-groups/observability-and-traceability.md), the catalog establishes a comparative baseline to ensure AAIF initiatives achieve backward compatibility and architectural alignment with prior art [^evt-wg-observability-and-traceability-pr-23].

The survey evaluates both full session-trace telemetry specifications and targeted execution accountability primitives, including post-hoc verifiable records such as `action_ref` [^evt-wg-observability-and-traceability-pr-23].

# Architecture / Specification
The survey categorizes prior work across session structure modeling, runtime interception boundaries, and independent action verification:

### Session & Diagnostic Telemetry
Covers distributed trace standards (such as OpenTelemetry GenAI semantic conventions and W3C Trace Context) and logging platforms designed to trace multi-turn conversations, tool invocations, and agent-to-agent communications [^evt-wg-observability-and-traceability-pr-23].

### Verifiable Action Accountability
Evaluates narrow accountability primitives that operate complementarily underneath broader session-level tracing:
- **`action_ref` / Mycelium Trails**: A post-hoc, third-party-verifiable action accountability primitive anchored on Arbitrum and specified in an IETF individual draft (`draft-etcheverry-action-ref`) [^evt-wg-observability-and-traceability-pr-23]. Rather than reconstructing complete session flow graphs or replacing OpenTelemetry, `action_ref` addresses whether an isolated recorded action is mathematically and independently verifiable by an untrusted third party [^evt-wg-observability-and-traceability-pr-23].

# Lifecycle History
Maintained as an ongoing catalog by the [Observability & Traceability Working Group](../working-groups/observability-and-traceability.md) under the guiding principle of interoperability over reinvention [^evt-wg-observability-and-traceability-pr-23].

[^evt-wg-observability-and-traceability-pr-23]: https://github.com/aaif/wg-observability-and-traceability/pull/23
