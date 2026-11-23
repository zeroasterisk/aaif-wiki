---
type: resource
title: anySQL
description: Open-source Python library and relational telemetry schema mapping LLM
  agent interactions and RAG pipelines into queryable Apache Arrow tables.
resource: https://github.com/aaif/project-proposals/issues/72
tags:
- resource
- telemetry
- sql
- observability
- arrow
- duckdb
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T10:37:33.064753+00:00'
sources:
- id: evt-project-proposals-issue-72
  resource: https://github.com/aaif/project-proposals/issues/72
  author: sadayamuthu
  last_modified: '2026-11-22T04:25:35+00:00'
---

# Overview

anySQL is an open-source Python library that captures telemetry from LLM applications, autonomous agents, and retrieval-augmented generation (RAG) pipelines, formatting the records into standardized relational tables queryable via standard SQL[^evt-project-proposals-issue-72]. It operates without hosted dependencies, buffering traces in memory or local SQLite files and executing in-process queries using DuckDB[^evt-project-proposals-issue-72].

The library normalizes heterogeneous execution streams into six canonical Apache Arrow tables: `llm_responses`, `eval_results`, `pipeline_runs`, `agent_tool_calls`, `agent_trace`, and `rag_chunks`[^evt-project-proposals-issue-72]. Shared join keys—notably `session_id`, a monotonic `step_order`, and `query_id`—enable cross-boundary relational analysis across retrieval, tool calling, and model evaluation stages[^evt-project-proposals-issue-72].

# Architecture / Specification

anySQL incorporates:
- **Client Instrumentation**: Provides transparent interceptors for OpenAI and Anthropic SDKs alongside specialized agent and RAG tracers[^evt-project-proposals-issue-72].
- **Relational Schema**: Six fixed Apache Arrow tables bound by `session_id` and sequential `step_order`, enabling multi-turn step attribution, tool-loop detection, and prompt-injection tracing via declarative SQL joins[^evt-project-proposals-issue-72].
- **anysql-proxy**: A local HTTP mediation proxy that intercepts traffic from coding assistants (e.g., Claude Code, Cursor, Continue) to record tokens, latency, cost metrics, and editor context directly into DuckDB[^evt-project-proposals-issue-72].

# Lifecycle History

- Created by Karthikeyan Sadayamuthu in March 2026 (v0.1.0)[^evt-project-proposals-issue-72].
- Served as the measurement engine for academic research on prompt-injection compromise detection in agent telemetry (accepted at IEEE CSTA 2026)[^evt-project-proposals-issue-72].
- Proposed for AAIF Sandbox project incubation under the Technical Committee review process via issue #72[^evt-project-proposals-issue-72].

[^evt-project-proposals-issue-72]: https://github.com/aaif/project-proposals/issues/72
