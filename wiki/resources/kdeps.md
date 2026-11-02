---
type: resource
title: kdeps
description: Open-source AI appliance builder packaging declarative YAML agent workflows
  into containers, Kubernetes deployments, or standalone binaries with built-in MCP
  client support.
resource: https://github.com/aaif/project-proposals/issues/65
tags:
- orchestration
- deployment
- packaging
- mcp
- kubernetes
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:28:52.572037+00:00'
sources:
- id: evt-project-proposals-issue-65
  resource: https://github.com/aaif/project-proposals/issues/65
  author: jjuliano
  last_modified: '2026-10-28T10:39:53+00:00'
---

# Overview

kdeps is an open-source AI appliance builder written in Go that compiles declarative YAML agent and workflow definitions into deployable artifacts such as Docker container images, Kubernetes manifests, or standalone binaries.[^evt-project-proposals-issue-65] Maintained under an Apache-2.0 license, the project enables reproducible agent packaging and execution across local runtimes (such as Ollama and llamafile) and remote cloud foundation models via langchaingo.[^evt-project-proposals-issue-65]

In March 2025, kdeps was submitted to the Agentic AI Foundation as a proposed [Sandbox](../policies/project-lifecycle-policy.md) project under the foundation's [project proposal process](../policies/project-proposal-process.md).[^evt-project-proposals-issue-65]

# Architecture and Capabilities

kdeps structures agent systems around a declarative `workflow.yaml` schema, generating portable deployment units tailored for both cloud and air-gapped enterprise environments:[^evt-project-proposals-issue-65]

- **Appliance Packaging**: Produces immutable execution units packaged as container images, Kubernetes deployments, or Go binaries with integrated local model runners.[^evt-project-proposals-issue-65]
- **Protocol Integration**: Ships an integrated Model Context Protocol (MCP) client (`pkg/tools/mcp`) for external tool invocation, with planned extensions for server mode.[^evt-project-proposals-issue-65]
- **Instruction Ingestion**: Collects context and agent configuration from repository root instruction files including `AGENTS.md`, `KDEPS.md`, and platform-specific manifests.[^evt-project-proposals-issue-65]
- **Air-Gapped Operation**: Designed to execute in restricted network environments without mandatory cloud dependencies, supporting private infrastructure deployments.[^evt-project-proposals-issue-65]

[^evt-project-proposals-issue-65]: https://github.com/aaif/project-proposals/issues/65
