---
type: resource
title: Meshllm
description: Distributed compute pooling framework enabling safe LLM inference across
  edge, consumer, and isolated server hardware through standard APIs.
resource: https://github.com/aaif/project-proposals/issues/70
tags:
- compute
- inference
- distributed-systems
- proposal
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:37:17.639051+00:00'
sources:
- id: evt-project-proposals-issue-70
  resource: https://github.com/aaif/project-proposals/issues/70
  author: michaelneale
  last_modified: '2026-11-17T10:35:02+00:00'
---

# Overview
Meshllm is an open-source distributed compute pooling project proposed to the Agentic AI Foundation that aggregates consumer edge devices, isolated servers, and GPUs to host and serve large language model workloads [^evt-project-proposals-issue-70]. The project seeks to make underutilized distributed hardware accessible for agentic reasoning and model inference through standardized consumption APIs [^evt-project-proposals-issue-70].

# Architecture / Specification
Meshllm implements several core capabilities:
- **Cross-Platform Compute Pooling**: Aggregates compute capacity across diverse hardware architectures and operating systems into a unified execution pool [^evt-project-proposals-issue-70].
- **Standardized API Interfaces**: Exposes inference endpoints using standard interfaces including [OpenResponses](../standards/open-responses.md), allowing chat interfaces, agent harnesses, and client applications to consume pooled models transparently [^evt-project-proposals-issue-70].
- **Agent Framework Integration**: Built adjacent to the [Goose](../resources/goose.md) agent framework to enable community compute sharing, with integrations supporting the Model Context Protocol (MCP), [Agent Skills](../standards/agent-skills.md), and [Agent Client Protocol](../standards/agent-client-protocol.md) [^evt-project-proposals-issue-70].
- **Planned Synergy**: Explores mediation through [AgentGateway](../resources/agentgateway.md) for traffic routing and integration with [OpenSandbox](../resources/opensandbox.md) for pooled workload execution [^evt-project-proposals-issue-70].

# Lifecycle History
Submitted as an open project proposal to the Technical Committee under issue #70 licensed under Apache 2.0 [^evt-project-proposals-issue-70].

[^evt-project-proposals-issue-70]: https://github.com/aaif/project-proposals/issues/70
