---
type: resource
title: Goose
description: Open-source general-purpose AI agent runtime and autonomous execution
  framework hosted by the AAIF with built-in telemetry and extensible tool integration.
resource: https://github.com/aaif/ws-taxonomy-landscape/pull/27
tags:
- runtime
- agent
- framework
- tool-use
- aaif-hosted
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-16T10:34:13.154434+00:00'
sources:
- id: evt-ws-taxonomy-landscape-pr-27
  resource: https://github.com/aaif/ws-taxonomy-landscape/pull/27
  author: thc1006
  last_modified: '2026-10-12T03:30:56+00:00'
---

# Overview

Goose is an open-source, general-purpose autonomous AI agent runtime hosted by the Agentic AI Foundation (AAIF) [^evt-ws-taxonomy-landscape-pr-27]. Originally developed by Block, Goose provides a modular execution engine capable of interacting with host environments, invoking shell operations, calling external APIs, and managing local workflows through automated context and tool dispatch.

# Architecture / Specification

Goose functions as an autonomous execution harness that executes developer-driven and operational tasks through modular plugins and protocol integrations. Key architectural characteristics include:

- **Runtime Execution**: Operates as a local or containerized agent runtime handling model interaction, multi-turn reasoning loops, and deterministic action execution.
- **Protocol Interoperability**: Integrates native support for the Model Context Protocol (MCP) to access tools, persistent context, and external data services.
- **Telemetry and Observability**: Exposes structured execution traces and operational metrics compatible with open telemetry pipelines.
- **Landscape Categorization**: Positioned within the [Agentic AI Landscape](../resources/agentic-ai-landscape.md) under the Autonomous Agent Frameworks subcategory as an official AAIF member-hosted project [^evt-ws-taxonomy-landscape-pr-27].

# Lifecycle History

Goose was donated to the Linux Foundation's Agentic AI Foundation at the foundation's public launch alongside the Model Context Protocol [^evt-ws-taxonomy-landscape-pr-27]. Following its donation, the primary source repository transitioned from `block/goose` to the foundation-managed `aaif-goose/goose` organization, with official documentation maintained at `goose-docs.ai` [^evt-ws-taxonomy-landscape-pr-27].

# References

- [Goose Source Repository](https://github.com/aaif-goose/goose)

[^evt-ws-taxonomy-landscape-pr-27]: https://github.com/aaif/ws-taxonomy-landscape/pull/27
