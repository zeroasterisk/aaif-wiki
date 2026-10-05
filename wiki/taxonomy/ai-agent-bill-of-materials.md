---
type: taxonomy
title: AI Agent Bill of Materials
description: A machine-readable inventory detailing an AI agent's models, harness,
  callable tools, and underlying software dependencies, including suppliers and versions.
resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/10
tags:
- governance
- regulatory
- sbom
- supply-chain
- compliance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-05T05:50:41.603890+00:00'
sources:
- id: evt-wg-governance-risk-and-regulatory-issue-10
  resource: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/10
  author: smcd-personal
  last_modified: '2026-09-30T04:48:04+00:00'
---

# Overview

An AI agent bill of materials (AI-BOM) is a standardized, machine-readable inventory of the components an AI agent is composed of and depends upon, including its foundational models, runtime harness, callable tools, and third-party software dependencies along with their respective suppliers and versions [^evt-wg-governance-risk-and-regulatory-issue-10].

# Architecture / Specification

The AI-BOM concept extends traditional Software Bills of Materials (SBOM) into agentic environments [^evt-wg-governance-risk-and-regulatory-issue-10]:

- **Scope of Coverage:** Extends beyond executable binary code to encompass prompt harnesses, tools, skills, pre-trained model weights, and system prompts governing agent behavior [^evt-wg-governance-risk-and-regulatory-issue-10].
- **Regulatory Alignment:** Maps to supply chain and documentation requirements under the EU Cyber Resilience Act (Regulation 2024/2847, Art. 3(39) & Annex I) and the EU AI Act (Regulation 2024/1689, Annex IV point 2(a) & Art. 25(4)) [^evt-wg-governance-risk-and-regulatory-issue-10].
- **Format Agnosticism:** Accommodates existing and emerging packaging profiles including CycloneDX ML-BOM and SPDX 3.0.1 AI profile without mandating a single serialization standard [^evt-wg-governance-risk-and-regulatory-issue-10].

# References

- Proposed within the [Governance, Risk, and Regulatory Working Group](../working-groups/governance-risk-and-regulatory.md) in coordination with the [Taxonomy and Landscape Workstream](../workstreams/taxonomy-and-landscape.md) [^evt-wg-governance-risk-and-regulatory-issue-10].
- Related terms: [Agent Tool Supply Chain Terms](../taxonomy/agent-tool-supply-chain-terms.md).

[^evt-wg-governance-risk-and-regulatory-issue-10]: https://github.com/aaif/wg-governance-risk-and-regulatory/issues/10
