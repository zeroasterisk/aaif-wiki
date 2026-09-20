---
type: deliverable
title: Agentic AI Threat Modeling Gap Analysis and Framework Design
description: A comparative gap analysis and threat modeling framework evaluating agentic
  AI risks against existing security baselines.
resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/2026-07-report.md
tags:
- deliverable
- security
- threat-modeling
- framework
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:50:01.179685+00:00'
sources:
- id: evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/2026-07-report.md
  author: Alex Frazer
  last_modified: '2026-08-13T07:57:15-04:00'
- id: evt-wg-security-and-privacy-pr-10
  resource: https://github.com/aaif/wg-security-and-privacy/pull/10
  author: awfrazer
  last_modified: '2026-08-13T11:57:16+00:00'
- id: evt-wg-security-and-privacy-file-75f22d914368-03de91f5
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-08-04.md
  author: Alex Frazer
  last_modified: '2026-08-13T08:00:29-04:00'
---

# Overview
The Agentic AI Threat Modeling Gap Analysis and Framework Design is an AAIF deliverable produced by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) evaluating existing threat modeling methodologies against unique agentic AI threat vectors[^evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed].

# Architecture / Specification
The workstream is led by Alon Mazor and Fernando Lucktemberg[^evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed]. The deliverable synthesizes threat landscape data across eight core areas by benchmarking against established security frameworks:
- MITRE ATLAS[^evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed]
- OWASP agentic AI security and governance publications[^evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed]
- MAESTRO framework[^evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed]
- NIST AI Risk Management Framework (AI RMF)[^evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed]

The workstream also investigates the adaptation of classical threat modeling methodologies, such as STRIDE and PASTA, to autonomous agent architectures, Model Context Protocol (MCP) tool invocation surfaces, and human-user-agent interaction interfaces[^evt-wg-security-and-privacy-file-75f22d914368-03de91f5].

# Lifecycle History
- **2026-07-31**: Initial gap review draft published as PR #8 on the working group repository[^evt-wg-security-and-privacy-pr-10].
- **2026-08-04**: Working group reviewed feedback incorporating STRIDE/PASTA mapping, UI/HUA considerations, and recent MCP security developments[^evt-wg-security-and-privacy-file-75f22d914368-03de91f5].

[^evt-wg-security-and-privacy-file-75f22d914368-03de91f5]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-08-04.md
[^evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/2026-07-report.md
[^evt-wg-security-and-privacy-pr-10]: https://github.com/aaif/wg-security-and-privacy/pull/10
