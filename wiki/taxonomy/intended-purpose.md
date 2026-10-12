---
type: taxonomy
title: Intended Purpose
description: The documented use, conditions, and context for which an AI system is
  designated by its provider prior to deployment.
resource: https://github.com/aaif/ws-taxonomy-landscape/issues/65
tags:
- taxonomy
- governance
- regulatory
- compliance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-10-12T10:30:30.290810+00:00'
sources:
- id: evt-ws-taxonomy-landscape-issue-65
  resource: https://github.com/aaif/ws-taxonomy-landscape/issues/65
  author: smcd
  last_modified: '2026-09-23T23:33:57+00:00'
---

# Overview

Intended purpose defines the explicit use, context, and operational conditions for which an AI system is designated by its provider or developer, as documented in accompanying instructions and specifications.[^evt-ws-taxonomy-landscape-issue-65] It stands in contrast to runtime intent—the dynamic objective an agent or human operator pursues during execution—by establishing the pre-deployment legal and architectural boundary for authorized system behavior.[^evt-ws-taxonomy-landscape-issue-65]

# Architecture / Specification

Within the taxonomy coordinated alongside the [Governance, Risk and Regulatory Working Group](../working-groups/governance-risk-and-regulatory.md), intended purpose functions as an authoritative benchmark for evaluating operational integrity and compliance.[^evt-ws-taxonomy-landscape-issue-65]

Key characteristics include:
- **Provider ownership**: Intended purpose belongs strictly to the party designing or supplying the system and is authored prior to deployment, rather than being synthesized dynamically during an agent run.[^evt-ws-taxonomy-landscape-issue-65]
- **Misuse baseline**: Derived from statutory standards such as European Union AI Act Article 3(12), intended purpose acts as the reference baseline against which "reasonably foreseeable misuse" (Article 3(13)), agent derailment, and unauthorized exploitation are measured.[^evt-ws-taxonomy-landscape-issue-65]
- **Contrast with intent**: While runtime intent represents what an agent or principal attempts to achieve during task execution, intended purpose restricts the envelope of sanctioned functionality.[^evt-ws-taxonomy-landscape-issue-65]

# Lifecycle History

Proposed in issue discussions within the Taxonomy and Landscape workstream to resolve ambiguity caused by treating intended purpose as a synonym for runtime intent.[^evt-ws-taxonomy-landscape-issue-65]

[^evt-ws-taxonomy-landscape-issue-65]: https://github.com/aaif/ws-taxonomy-landscape/issues/65
