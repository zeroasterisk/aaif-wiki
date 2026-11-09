---
type: resource
title: Agent Observability Prior Work Survey
description: Comparative landscape survey evaluating specifications, platforms, and
  hosted protocols across agent telemetry, mediation, and verification surfaces.
resource: https://github.com/aaif/wg-observability-and-traceability/pull/31
tags:
- observability
- landscape
- a2a
- agentgateway
- prior-work
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:01:05.181025+00:00'
sources:
- id: evt-wg-observability-and-traceability-pr-31
  resource: https://github.com/aaif/wg-observability-and-traceability/pull/31
  author: narko4u
  last_modified: '2026-09-19T04:53:51+00:00'
---

# Overview
The Agent Observability Prior Work Survey provides a structured comparative evaluation of industry platforms, open specifications, and AAIF-hosted technologies covering agent instrumentation, tracing, and mediation[^evt-wg-observability-and-traceability-pr-31]. It tracks maturity, adoption, protocol layers, and structural architectural gaps across runtime ecosystems[^evt-wg-observability-and-traceability-pr-31].

# Architecture / Specification
The survey assesses key protocols, gateways, and frameworks across operational layers:
- **Agent-to-Agent (A2A)**: Joined AAIF as a hosted project in August 2026 to provide an interoperability layer for direct agent communications[^evt-wg-observability-and-traceability-pr-31]. While A2A v1.0 introduced signed agent cards, verifying card identity claims against actual runtime behavior remains an unresolved challenge[^evt-wg-observability-and-traceability-pr-31].
- **agentgateway**: Contributed by solo.io and joined AAIF in June 2026, offering traffic mediation, policy enforcement, and proxy controls across Model Context Protocol (MCP) and A2A traffic deployable across hyperscaler cloud marketplaces[^evt-wg-observability-and-traceability-pr-31].
- **The Evidence Layer Gap**: Identifies a fundamental gap between network/protocol mediation and tamper-evident behavioral verification, motivating cross-working-group efforts between [Observability and Traceability](../working-groups/observability-and-traceability.md) and [Attestation and Evidence](../working-groups/attestation-and-evidence.md)[^evt-wg-observability-and-traceability-pr-31].

# Lifecycle History
Maintained by the [Observability and Traceability Working Group](../working-groups/observability-and-traceability.md). Updated in September 2026 to incorporate A2A and agentgateway entries following their addition as hosted AAIF projects[^evt-wg-observability-and-traceability-pr-31].

[^evt-wg-observability-and-traceability-pr-31]: https://github.com/aaif/wg-observability-and-traceability/pull/31
