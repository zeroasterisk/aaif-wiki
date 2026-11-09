---
type: resource
title: Zeko
description: Open-source agentic rollup protocol providing verifiable shared state,
  fast local confirmation, and zero-knowledge proof aggregation across agent applications.
resource: https://github.com/aaif/project-proposals/issues/68
tags:
- state
- rollup
- cryptography
- zero-knowledge
- aaif-proposal
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:33:45.576359+00:00'
sources:
- id: evt-project-proposals-issue-68
  resource: https://github.com/aaif/project-proposals/issues/68
  author: zekoxyz
  last_modified: '2026-11-06T21:15:00+00:00'
---

# Overview

Zeko is an open-source agentic rollup protocol designed to maintain verifiable shared state across distributed AI agent applications [^evt-project-proposals-issue-68]. Submitted as an AAIF Sandbox proposal, Zeko provides instant transaction confirmation at the rollup tier, enabling autonomous agents to coordinate against accepted state without waiting for base-layer blockchain finality [^evt-project-proposals-issue-68]. Systems leverage this shared state for task commitments, resource reservations, cross-agent accounting, and conditional machine payments [^evt-project-proposals-issue-68].

Originating from Mina cryptography and ZK smart contracts, Zeko also supports an Ethereum settlement architecture via SP1 zero-knowledge proof aggregation [^evt-project-proposals-issue-68].

# Architecture / Specification

Zeko allows operators to deploy sovereign rollups with localized keys, access policies, and hosting models, such as confidential computing enclaves [^evt-project-proposals-issue-68]. Its architectural components include:

- **Rollup State Ordering:** Resolves competing state transitions from concurrent agents with immediate local confirmation [^evt-project-proposals-issue-68].
- **Recursive Proof Aggregation:** Employs zero-knowledge proofs to allow multi-agent systems to verify complex state updates without re-executing computations or exposing private inputs [^evt-project-proposals-issue-68].
- **AAIF Ecosystem Integrations:** Interoperates with Model Context Protocol (MCP) and Agent-to-Agent (A2A) interfaces for coordinated tool actions and reservations; [Goose](../resources/goose.md) for external policy-enforced resource limits; [AgentGateway](../resources/agentgateway.md) for shared multi-gateway budgets; [Open Responses](../standards/open-responses.md) for state-linked receipts; and [OpenSandbox](../resources/opensandbox.md) for reproducible execution receipts [^evt-project-proposals-issue-68].

# Lifecycle History

Zeko was proposed for AAIF Sandbox status via Issue #68 on `aaif/project-proposals` [^evt-project-proposals-issue-68]. As an unmerged proposal, it remains in `draft` status within foundation tracking [^evt-project-proposals-issue-68].

[^evt-project-proposals-issue-68]: https://github.com/aaif/project-proposals/issues/68
