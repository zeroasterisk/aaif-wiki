---
type: resource
title: Zeko
description: Open-source agentic rollup protocol providing zero-knowledge state verification
  and instant transaction ordering for multi-agent coordination.
resource: https://github.com/aaif/project-proposals/issues/68
tags:
- resource
- rollup
- zero-knowledge
- shared-state
- sandbox-proposal
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:43:19.607440+00:00'
sources:
- id: evt-project-proposals-issue-68
  resource: https://github.com/aaif/project-proposals/issues/68
  author: zekoxyz
  last_modified: '2026-11-06T21:15:00+00:00'
---

# Overview
Zeko is an open-source agentic rollup protocol designed to provide verifiable shared state, instant transaction confirmation, and recursive zero-knowledge proofs for autonomous AI agent coordination.[^evt-project-proposals-issue-68] Originating from the Mina ecosystem and extending to Ethereum settlement via SP1 and o1Labs, Zeko enables concurrent agents to coordinate resource reservations, execution budgets, conditional payments, and work commitments against verified state transitions without relying on centralized databases.[^evt-project-proposals-issue-68]

In March 2026, Zeko Labs submitted a project proposal seeking entry into the [Technical Committee](../governance/technical-committee.md) Sandbox stage.[^evt-project-proposals-issue-68]

# Architecture / Specification

## Rollup Mechanics
Zeko provides an off-chain rollup layer that confirms and orders competing agent transactions immediately, avoiding settlement latency on base-layer blockchains:[^evt-project-proposals-issue-68]
- **Recursive Proof Aggregation:** Uses zero-knowledge smart contracts to verify execution correctness and state transitions without requiring participants to re-execute every computational operation.[^evt-project-proposals-issue-68]
- **Settlement and Bridging:** Connects sovereign rollups to Ethereum testnets and mainnet via SP1 zero-knowledge verifiers, supporting optional confidential compute deployments on Phala TEE environments.[^evt-project-proposals-issue-68]
- **Selective Disclosure:** Leverages zero-knowledge proofs so applications can validate policy and budget compliance while protecting private inputs.[^evt-project-proposals-issue-68]

## AAIF Ecosystem Alignments
The proposal details reference integrations with foundational AAIF protocols and frameworks:[^evt-project-proposals-issue-68]
- **Model Context Protocol (MCP) and A2A:** Enabling concurrent agents to coordinate reservations and tool commitments against shared accepted state.[^evt-project-proposals-issue-68]
- **Goose:** Enforcing user-approved budget limits and recording authority transitions outside model context windows.[^evt-project-proposals-issue-68]
- **Agent Gateway:** Synchronizing decentralized resource accounting so requests routed through distinct proxies consume shared budgets.[^evt-project-proposals-issue-68]
- **OpenSandbox and OpenEnv:** Persisting verifiable resource allocations and job receipts across container restarts and reinforcement learning episode resets.[^evt-project-proposals-issue-68]

# Lifecycle History
- **2026-03-02:** Project proposal submitted by Zeko Labs for admission to the AAIF Sandbox stage (`evt-project-proposals-issue-68`).[^evt-project-proposals-issue-68]

# References
- AAIF Project Proposal Issue #68: Zeko.[^evt-project-proposals-issue-68]

[^evt-project-proposals-issue-68]: https://github.com/aaif/project-proposals/issues/68
