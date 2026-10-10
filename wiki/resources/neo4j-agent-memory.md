---
type: resource
title: Neo4j Agent Memory
description: Open-source graph-native persistent memory framework structuring short-term
  conversations, POLE+O long-term knowledge, and reasoning decision traces.
resource: https://github.com/aaif/project-proposals/issues/52
tags:
- memory
- knowledge-graph
- mcp
- provenance
- reasoning
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:22:44.663639+00:00'
sources:
- id: evt-project-proposals-issue-52
  resource: https://github.com/aaif/project-proposals/issues/52
  author: johnymontana
  last_modified: '2026-10-08T02:42:57+00:00'
---

# Overview

Neo4j Agent Memory is an open-source, graph-native memory layer designed for AI agents that integrates short-term conversation history, long-term entity-relationship graphs, and reasoning traces into a unified property graph model [^evt-project-proposals-issue-52]. The project separates stored context into conversation messages, a POLE+O (Person, Object, Location, Event, Organization) structured knowledge graph, and auditable reasoning memory that logs decision steps, tool calls, and provenance nodes [^evt-project-proposals-issue-52].

# Architecture / Specification

The framework provides framework-neutral memory abstractions across three functional tiers [^evt-project-proposals-issue-52]:

- **Short-Term Memory**: Sequential conversation history recorded as message chains.
- **Long-Term Knowledge Graph**: Entity and relationship extraction utilizing spaCy, GLiNER, and LLMs mapped to standard or user-defined ontologies.
- **Reasoning Memory**: First-class graph nodes capturing decisions, rationale, tool invocations, and multi-hop provenance for historical introspection and post-execution auditing.

Integration surfaces include typed Python and TypeScript SDKs, a Model Context Protocol (MCP) server exposing 16 memory tools, and native adapters for orchestrators including LangChain, LlamaIndex, Pydantic AI, CrewAI, OpenAI Agents SDK, and Google ADK [^evt-project-proposals-issue-52].

# Lifecycle History

Originally launched within Neo4j Labs in January 2026 under the Apache-2.0 license, the project was proposed as a Sandbox project to the Agentic AI Foundation to establish vendor-neutral governance and multi-backend storage independence [^evt-project-proposals-issue-52].

[^evt-project-proposals-issue-52]: https://github.com/aaif/project-proposals/issues/52
