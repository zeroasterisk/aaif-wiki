---
type: working-group
title: Security and Privacy Working Group
description: AAIF working group establishing security and privacy threat models, shared
  taxonomies, design patterns, and cross-discipline review mechanisms across agentic
  AI systems.
resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-02-17.md
tags:
- working-group
- security
- privacy
- governance
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-08-17T23:45:08.823628+00:00'
sources:
- id: evt-wg-security-and-privacy-file-e080ea2d4af5-49d9592e
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-02-17.md
  author: Alex Frazer
  last_modified: '2026-03-07T17:18:26-05:00'
- id: evt-wg-security-and-privacy-file-563e910f8be2-6ff86a0d
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-03-03.md
  author: Alex Frazer
  last_modified: '2026-03-07T17:18:26-05:00'
- id: evt-wg-security-and-privacy-file-822dcec9cbfd-b1d860ec
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-03-17.md
  author: Alex Frazer
  last_modified: '2026-03-17T15:42:03-04:00'
- id: evt-wg-security-and-privacy-file-f9b60c3f43ba-8b4c1f35
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-03-31.md
  author: Alex Frazer
  last_modified: '2026-04-03T12:31:43-04:00'
- id: evt-wg-security-and-privacy-file-4cd71dcfd1ce-c26f3151
  resource: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-04-14.md
  author: Alex Frazer
  last_modified: '2026-04-16T09:23:12-04:00'
---

# Overview

The Security and Privacy Working Group (SP WG) is an Agentic AI Foundation body chartered to advance security and privacy as shared disciplines across the agentic AI ecosystem [^evt-wg-security-and-privacy-file-f9b60c3f43ba-8b4c1f35]. The working group is chaired by Alex Frazer with Junjie Bu serving as co-chair [^evt-wg-security-and-privacy-file-563e910f8be2-6ff86a0d] [^evt-wg-security-and-privacy-file-822dcec9cbfd-b1d860ec].

The group operates on a bi-weekly cadence to develop threat models, reference architectures, best practice guides, and review criteria that providers, consumers, and peer working groups can adopt to share responsibility for trustworthy agentic systems [^evt-wg-security-and-privacy-file-e080ea2d4af5-49d9592e] [^evt-wg-security-and-privacy-file-f9b60c3f43ba-8b4c1f35].

# Architecture / Specification

## Scope and Boundaries

The working group focuses on technical security and privacy engineering controls across the agentic lifecycle while coordinating with adjacent bodies [^evt-wg-security-and-privacy-file-f9b60c3f43ba-8b4c1f35]:

- **Security Architecture and Design Patterns**: Covers controls for agent memory, tools, skills, interceptors, and privacy-preserving execution such as zero-knowledge proofs and Trusted Execution Environments (TEEs) [^evt-wg-security-and-privacy-file-563e910f8be2-6ff86a0d] [^evt-wg-security-and-privacy-file-f9b60c3f43ba-8b4c1f35] [^evt-wg-security-and-privacy-file-4cd71dcfd1ce-c26f3151].
- **Threat Modeling and Attack Surfaces**: Focuses on prompt injection, multi-agent persuasion, derailment, blast radius containment, and data isolation [^evt-wg-security-and-privacy-file-563e910f8be2-6ff86a0d] [^evt-wg-security-and-privacy-file-4cd71dcfd1ce-c26f3151].
- **Commerce and Payments Security**: Evaluates guardrails against unauthorized fund draining and payment credential exposure [^evt-wg-security-and-privacy-file-563e910f8be2-6ff86a0d] [^evt-wg-security-and-privacy-file-f9b60c3f43ba-8b4c1f35].
- **Out-of-Scope Delegations**: Value judgments, ethics, and legal compliance interpretation are deferred to the Governance and Regulatory Alignment Working Group [^evt-wg-security-and-privacy-file-563e910f8be2-6ff86a0d] [^evt-wg-security-and-privacy-file-f9b60c3f43ba-8b4c1f35]. Core identity and authorization protocols are maintained in collaboration with the Identity and Trust Working Group [^evt-wg-security-and-privacy-file-822dcec9cbfd-b1d860ec] [^evt-wg-security-and-privacy-file-f9b60c3f43ba-8b4c1f35].

## Initial Deliverables

The working group formally approved five deliverables for its initial 3–6 month cycle [^evt-wg-security-and-privacy-file-4cd71dcfd1ce-c26f3151]:

1. **Taxonomy**: A living reference document establishing standardized security and privacy terminology across the AAIF [^evt-wg-security-and-privacy-file-4cd71dcfd1ce-c26f3151].
2. **Agentic AI Threat Modeling Gap Analysis and Framework Design**: Research identifying domain-specific attack vectors beyond conventional frameworks like OWASP or NIST [^evt-wg-security-and-privacy-file-4cd71dcfd1ce-c26f3151].
3. **Security and Privacy Design Patterns Catalog**: Technical blueprints covering human-in-the-loop controls, MCP interceptors, and semantic execution constraints [^evt-wg-security-and-privacy-file-4cd71dcfd1ce-c26f3151].
4. **Agentic Security Best Practices Guide**: Practical operational guidance on sensitive data handling, secrets management, and safe tool execution [^evt-wg-security-and-privacy-file-4cd71dcfd1ce-c26f3151].
5. **Cross-Working Group Review Checklist**: An assessment checklist enabling other AAIF working groups to evaluate security and privacy implications early in their specification lifecycles [^evt-wg-security-and-privacy-file-4cd71dcfd1ce-c26f3151].

# Lifecycle History

- **2026-02-17**: Orientation and ideation session hosted by Linux Foundation leadership; working group established [^evt-wg-security-and-privacy-file-e080ea2d4af5-49d9592e].
- **2026-03-03**: Alex Frazer elected as chair; initial charter theme breakdown and scoping begun [^evt-wg-security-and-privacy-file-563e910f8be2-6ff86a0d].
- **2026-03-17**: Junjie Bu named co-chair; five candidate deliverables and cross-working-group review model introduced [^evt-wg-security-and-privacy-file-822dcec9cbfd-b1d860ec].
- **2026-03-31**: Formal mission statement adopted unanimously [^evt-wg-security-and-privacy-file-f9b60c3f43ba-8b4c1f35].
- **2026-04-14**: Full working group charter, scope, and five initial deliverables approved unanimously prior to Technical Committee review [^evt-wg-security-and-privacy-file-4cd71dcfd1ce-c26f3151].

[^evt-wg-security-and-privacy-file-4cd71dcfd1ce-c26f3151]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-04-14.md
[^evt-wg-security-and-privacy-file-563e910f8be2-6ff86a0d]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-03-03.md
[^evt-wg-security-and-privacy-file-822dcec9cbfd-b1d860ec]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-03-17.md
[^evt-wg-security-and-privacy-file-e080ea2d4af5-49d9592e]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-02-17.md
[^evt-wg-security-and-privacy-file-f9b60c3f43ba-8b4c1f35]: https://github.com/aaif/wg-security-and-privacy/blob/3a3d0ef5367e0beb6aafa56908ae277a73f133e0/meeting-notes/2026-03-31.md
