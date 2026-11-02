---
type: taxonomy
title: Agent Registry
description: Centralized or federated directory storing validated identities, metadata,
  capabilities, and governance policies for discoverable AI agents.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/92
tags:
- taxonomy
- governance
- registry
- discovery
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:26:35.776719+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-92
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/92
  author: kjamithash
  last_modified: '2026-10-15T16:19:27+00:00'
---

# Overview
An agent registry is an indexed catalog and discovery service that stores validated agent identities, capability definitions, endpoint metadata, and operational governance constraints[^evt-ws-taxonomy-landscape-pr-92]. Registries enable runtime discovery, access control, and policy enforcement across heterogeneous agent-to-agent and client-to-agent architectures[^evt-ws-taxonomy-landscape-pr-92].

# Architecture / Specification

## Core Capabilities
Agent registries maintain machine-readable records facilitating secure inter-agent coordination[^evt-ws-taxonomy-landscape-pr-92]:
- **Identity and Metadata Management**: Catalogs verifiable credentials, public keys, and cryptographic attestations for registered agents (see [Identity and Trust WG](../working-groups/identity-and-trust.md)).
- **Capability Discovery**: Exposes discoverable skills, supported protocol bindings, and tool definitions for autonomous or human-mediated delegation (see [Agentic Resource Discovery](../standards/agentic-resource-discovery.md)).
- **Policy Enforcement**: Integrates with runtime boundary gateways and mediation proxies to verify admission criteria and regulatory constraints prior to session establishment (see [AgentGateway](../resources/agentgateway.md) and [Context Forge](../resources/context-forge.md)).

[^evt-ws-taxonomy-landscape-pr-92]: https://github.com/aaif/ws-taxonomy-landscape/pull/92
