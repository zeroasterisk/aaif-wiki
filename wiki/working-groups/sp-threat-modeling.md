---
type: workstream
title: 'Security & Privacy: Threat Modeling Workstream'
description: Evaluates existing AI threat frameworks against agentic-specific threats
  and develops comprehensive threat modeling frameworks.
resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/2026-07-report.md
tags:
- threat-modeling
- security
- mitre-atlas
- owasp
- stride
- pasta
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-21T09:52:51.379319+00:00'
sources:
- id: evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/2026-07-report.md
  author: Alex Frazer
  last_modified: '2026-08-13T07:57:15-04:00'
- id: evt-wg-security-and-privacy-file-75f22d914368-03de91f5
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-08-04.md
  author: Alex Frazer
  last_modified: '2026-08-13T08:00:29-04:00'
- id: evt-wg-security-and-privacy-pr-10
  resource: https://github.com/aaif/wg-security-and-privacy/pull/10
  author: awfrazer
  last_modified: '2026-08-13T11:57:16+00:00'
---

# Overview

The Threat Modeling workstream of the [Security and Privacy Working Group](./security-and-privacy.md) develops an open threat modeling framework tailored specifically to agentic AI systems [^evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed]. The effort evaluates existing AI and classical cybersecurity frameworks to identify gaps in addressing autonomous agent architectures, multi-agent coordination, and tool execution risks [^evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed].

# Architecture / Specification

- **Lead Contributors**: Fernando Lucktemberg and Alon Mazor [^evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed].
- **Evaluated Baseline Frameworks**: Gap analysis assesses coverage against MITRE ATLAS, OWASP, MAESTRO, and the NIST AI Risk Management Framework (AI RMF) across eight defined security areas [^evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed].
- **Methodology Evaluation**: The workstream is actively evaluating alignment between agentic threat models and classical methodologies including STRIDE and PASTA [^evt-wg-security-and-privacy-file-75f22d914368-03de91f5].
- **Scope Integrations**: Deliverable revisions incorporate UI/Human-User Accountability (HUA) considerations, supply-chain vulnerabilities, and emerging protocol security developments such as Model Context Protocol (MCP) stateless operation and tool attestation [^evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed, ^evt-wg-security-and-privacy-file-75f22d914368-03de91f5].

# Lifecycle History

- **July 2026**: Initial gap analysis across the eight target areas drafted and submitted as a pull request to the working group repository [^evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed, ^evt-wg-security-and-privacy-pr-10].
- **August 2026**: Review cycle opened for community feedback and integration of STRIDE/PASTA mappings and UI/HUA considerations [^evt-wg-security-and-privacy-file-75f22d914368-03de91f5].

[^evt-wg-security-and-privacy-file-75f22d914368-03de91f5]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-08-04.md
[^evt-wg-security-and-privacy-file-fa4050a9f626-fb1414ed]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/reporting/2026-07-report.md
