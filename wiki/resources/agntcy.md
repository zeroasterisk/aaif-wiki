---
type: resource
title: AGNTCY Multi-Agent Infrastructure
description: Open-source multi-agent infrastructure framework providing agent directory
  discovery, OASF schemas, SLIM secure messaging, identity credentials, and SHADI
  runtime sandboxing.
resource: https://github.com/aaif/project-proposals/issues/57
tags:
- multi-agent
- discovery
- identity
- messaging
- sandboxing
- observability
- project-proposal
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-19T11:11:30.472250+00:00'
sources:
- id: evt-project-proposals-issue-57
  resource: https://github.com/aaif/project-proposals/issues/57
  author: jparello
  last_modified: '2026-10-13T15:35:39+00:00'
---

# Overview
AGNTCY is an open-source infrastructure suite for multi-agent systems providing decentralized capability discovery, cryptographic identity, secure messaging, runtime sandboxing, and behavioral observability[^evt-project-proposals-issue-57]. Submitted to the Agentic AI Foundation ([AAIF](../governance/technical-committee.md)) as a Growth-stage project intake proposal, AGNTCY operates as a unified project bridging agent directories, transport protocols, secure hosts, and semantic telemetry[^evt-project-proposals-issue-57].

Rather than implementing cognitive planning loops or reasoning runtimes, AGNTCY targets the connective fabric between autonomous agents, external tools, and host operating systems[^evt-project-proposals-issue-57]. It complements protocols such as [A2A](../standards/agent-network-protocol.md) and [Agent Skills](../standards/agent-skills.md), and mediation proxies like [agentgateway](../resources/agentgateway.md), without attempting to replace them[^evt-project-proposals-issue-57].

# Architecture / Specification
AGNTCY comprises several modular components governed under a common infrastructure framework[^evt-project-proposals-issue-57]:

- **Agent Directory (`dir`)**: A distributed discovery layer for Model Context Protocol (MCP) servers, [A2A](../standards/agent-network-protocol.md) servers, and [Agent Skills](../standards/agent-skills.md)[^evt-project-proposals-issue-57]. It leverages Open Container Initiative (OCI) registries for metadata artifact storage and a Distributed Hash Table (DHT) for peer-to-peer network discovery[^evt-project-proposals-issue-57].
- **Open Agentic Schema Framework (OASF)**: An object schema derived from the Open Cybersecurity Schema Framework (OCSF) providing standardized machine records describing agents, tools, and capability interfaces, interoperating with A2A Agent Cards[^evt-project-proposals-issue-57].
- **Secure Low-Latency Interactive Messaging (SLIM)**: A multi-agent transport protocol and custom binding for A2A supporting multicast RPC across cloud-native and edge environments[^evt-project-proposals-issue-57]. SLIM secures group communication channels using Messaging Layer Security (MLS, RFC 9420) over HTTP/2 transport[^evt-project-proposals-issue-57].
- **Identity**: A credential and policy framework issuing verifiable credentials, W3C Decentralized Identifiers (DIDs), and agent badges, enabling Tool Based Access Control (TBAC) for granular agent-to-tool policy enforcement[^evt-project-proposals-issue-57].
- **Observe**: An observability SDK and Metrics Compute Engine (MCE) extending [OpenTelemetry](../resources/opentelemetry.md) GenAI/LLM semantic conventions downstream with agent-specific spans and computed output-quality metrics[^evt-project-proposals-issue-57].
- **Secure Host for Agentic AI Dynamic Instantiation (SHADI)**: A Rust-based host runtime (`shadictl`, `shadi_sandbox`, `agent_secrets`, `shadi_memory`, `agent_transport_slim`) enforcing OS-level process sandboxing, encrypted SQLCipher memory, and keychain secret release verification gates[^evt-project-proposals-issue-57].
- **AgentBridge**: A CLI interconnect distributed within SHADI that bridges standard A2A client and server interfaces to external coding harnesses (such as Claude Code, Copilot, or Cursor Agent)[^evt-project-proposals-issue-57].
- **coffeeAGNTCY**: An end-to-end multi-agent reference application and enterprise sandbox used to demonstrate AGNTCY patterns across discovery, identity, messaging, and coordination[^evt-project-proposals-issue-57].

# Lifecycle History
AGNTCY was open-sourced in March 2025 by Cisco alongside LangChain and Galileo, entering the Linux Foundation in July 2025 with support from Cisco, Dell Technologies, Google Cloud, Oracle, and Red Hat[^evt-project-proposals-issue-57]. In August 2026, maintainers submitted an intake proposal to the AAIF Technical Committee under the [Project Proposal Process](../policies/project-proposal-process.md) requesting an intra-foundation transfer to AAIF at the Growth maturity stage[^evt-project-proposals-issue-57].

[^evt-project-proposals-issue-57]: https://github.com/aaif/project-proposals/issues/57
