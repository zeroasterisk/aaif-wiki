---
type: taxonomy
title: AI Agent Bill of Materials
description: Machine-readable inventory detailing an AI agent's constituent models,
  harness components, callable tools, and underlying software dependencies with supplier
  and version provenance.
resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/10
tags:
- governance
- compliance
- supply-chain
- taxonomy
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T10:18:51.650896+00:00'
sources:
- id: evt-wg-governance-risk-and-regulatory-issue-10
  resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/10
  author: smcd-personal
  last_modified: '2026-09-30T04:48:04+00:00'
---

# Overview

An AI agent bill of materials (abbreviated as AI-BOM) is a machine-readable inventory of what an AI agent is built from and relies on, covering its models, the harness around them, the tools it can call, and the third-party software beneath them, each annotated with supplier provenance and version information.[^evt-wg-governance-risk-and-regulatory-issue-10]

# Architecture / Specification

The AI-BOM extends traditional Software Bill of Materials (SBOM) frameworks beyond static code packages to encompass the dynamic behavioral and operational dependencies governing agentic execution.[^evt-wg-governance-risk-and-regulatory-issue-10]

Core component categories captured in an AI-BOM include:
- **Models**: Pre-trained foundation models, fine-tuned weights, adapters, and deployment configurations.[^evt-wg-governance-risk-and-regulatory-issue-10]
- **Harness Scaffolding**: Orchestration frameworks, prompt templates, agent loops, and execution policies.[^evt-wg-governance-risk-and-regulatory-issue-10]
- **Tools and Capabilities**: Callable API integrations, Model Context Protocol (MCP) servers, plugins, and tool runtime environments.[^evt-wg-governance-risk-and-regulatory-issue-10]
- **Underlying Software**: Third-party libraries, host operating system packages, container base layers, and runtime execution dependencies.[^evt-wg-governance-risk-and-regulatory-issue-10]

The term is format-agnostic, encompassing emerging artifact schemas such as the SPDX 3.0 AI profile and CycloneDX ML-BOM.[^evt-wg-governance-risk-and-regulatory-issue-10] It aligns technical agent transparency with regulatory mandates, including the EU Cyber Resilience Act (Regulation (EU) 2024/2847) SBOM obligations and EU AI Act (Regulation (EU) 2024/1689) Annex IV technical documentation requirements for high-risk systems.[^evt-wg-governance-risk-and-regulatory-issue-10]

# References

- EU Cyber Resilience Act, Regulation (EU) 2024/2847 [^evt-wg-governance-risk-and-regulatory-issue-10]
- EU AI Act, Regulation (EU) 2024/1689 [^evt-wg-governance-risk-and-regulatory-issue-10]
- SPDX 3.0.1 AI Profile and CycloneDX ML-BOM [^evt-wg-governance-risk-and-regulatory-issue-10]

[^evt-wg-governance-risk-and-regulatory-issue-10]: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/10
