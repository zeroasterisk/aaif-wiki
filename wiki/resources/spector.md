---
type: resource
title: Spector Memory Engine
description: Open-source cognitive memory engine and MCP server providing multi-tier
  state retention, decay scoring, and namespace isolation for AI agents.
resource: https://github.com/aaif/project-proposals/issues/48
tags:
- memory
- mcp
- state-management
- sandbox-proposal
- runtime
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:18:03.150039+00:00'
sources:
- id: evt-project-proposals-issue-48
  resource: https://github.com/aaif/project-proposals/issues/48
  author: sbharatjoshi
  last_modified: '2026-10-02T02:31:54+00:00'
---

# Overview
Spector is an open-source cognitive memory engine designed to provide autonomous AI agents and multi-agent systems with durable, stateful memory substrates beyond stateless vector databases.[^evt-project-proposals-issue-48] It addresses context degradation and long-running session context loss by organizing memory traces across working, episodic, semantic, and procedural tiers with associative graph scoring and power-law decay.[^evt-project-proposals-issue-48]

# Architecture / Specification
Spector is implemented as a modular Java reactor utilizing Project Panama Foreign Function & Memory (FFM) and the Vector API to achieve SIMD-accelerated scoring off-heap with low garbage collection overhead.[^evt-project-proposals-issue-48] It implements the open Memory Fundamentals (MF-001) memory model specification.[^evt-project-proposals-issue-48]

Key architectural components include:
- **Tiered Memory Model**: Segregates experiential data into working, episodic, semantic, and procedural stores with power-law decay and consolidation routines.[^evt-project-proposals-issue-48]
- **Namespace Isolation**: Enforces physical on-disk tenant and agent namespace isolation boundaries to prevent cross-tenant data leakage.[^evt-project-proposals-issue-48]
- **Interface Layer**: Exposes an embedded Model Context Protocol (`spector-mcp`) server providing cognitive memory tools (`memory_remember`, `memory_recall`, `memory_reinforce`, `memory_introspect`, `memory_why_not`, `memory_status`), alongside REST/gRPC gateways and language SDKs (Python, TypeScript, Java).[^evt-project-proposals-issue-48]
- **Runtime Integration**: Interoperates with local execution harnesses such as [goose](../resources/goose.md) via stdio or HTTP MCP configurations.[^evt-project-proposals-issue-48]

# Lifecycle History
Spector was submitted to the AAIF Project Proposals intake for Sandbox stage incubation under Apache-2.0 licensing, targeting vendor-neutral standardization of agent memory infrastructure.[^evt-project-proposals-issue-48]

[^evt-project-proposals-issue-48]: https://github.com/aaif/project-proposals/issues/48
