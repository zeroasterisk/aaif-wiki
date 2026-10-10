---
type: taxonomy
title: AI Agent Bill of Materials
description: Machine-readable inventory defining the foundation models, harness software,
  tools, and third-party dependencies comprising an AI agent system.
resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/10
tags:
- taxonomy
- governance
- sbom
- supply-chain
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:13:19.023330+00:00'
sources:
- id: evt-wg-governance-risk-and-regulatory-issue-10
  resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/10
  author: smcd-personal
  last_modified: '2026-09-30T04:48:04+00:00'
---

# Overview
An AI Agent Bill of Materials (AI-BOM) is a standardized, machine-readable inventory detailing the constituent components and supply chain dependencies of an AI agent[^evt-wg-governance-risk-and-regulatory-issue-10]. It extends traditional Software Bill of Materials (SBOM) concepts by capturing behavioral drivers including foundation models, runtime harnesses, invocable tools, and underlying software dependencies along with supplier identity and version metadata[^evt-wg-governance-risk-and-regulatory-issue-10].

# Architecture / Specification
AI-BOM manifests map agent dependency graphs across multiple abstraction layers, providing structured provenance compatible with standards such as SPDX 3.0 AI profiles and CycloneDX ML-BOM specifications[^evt-wg-governance-risk-and-regulatory-issue-10]. The inventory encompasses base model weights, prompt harnesses, tool schemas, and third-party library dependencies required for regulatory transparency and supply chain traceability[^evt-wg-governance-risk-and-regulatory-issue-10].

[^evt-wg-governance-risk-and-regulatory-issue-10]: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/10
