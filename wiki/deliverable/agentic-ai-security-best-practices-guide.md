---
type: deliverable
title: Agentic AI Security Best Practices Guide
description: A guide establishing actionable security guidance, guardrails, secrets
  management, and forensics across agentic AI lifecycles.
resource: https://github.com/aaif/wg-security-and-privacy/blob/d33f37911676bbe623b62164b720dbc4ec500c5b/workstreams/best-practices/README.md
tags:
- security
- best-practices
- guardrails
- forensics
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-09-20T17:57:08.301998+00:00'
sources:
- id: evt-wg-security-and-privacy-file-e24f19bec4ac-ea047250
  resource: https://github.com/aaif/wg-security-and-privacy/blob/d33f37911676bbe623b62164b720dbc4ec500c5b/workstreams/best-practices/README.md
  author: Alex Frazer
  last_modified: '2026-08-26T22:02:33-04:00'
- id: evt-wg-security-and-privacy-pr-21
  resource: https://github.com/aaif/wg-security-and-privacy/pull/21
  author: awfrazer
  last_modified: '2026-08-27T02:02:39+00:00'
---

# Overview
The Agentic AI Security Best Practices Guide provides practical, high-level operational and architectural guidance for builders and operators of agentic AI systems [^evt-wg-security-and-privacy-file-e24f19bec4ac-ea047250]. While complementary design pattern catalogs detail how to implement specific components, this guide articulates recommended practices, guardrails, and external reference frameworks [^evt-wg-security-and-privacy-file-e24f19bec4ac-ea047250].

# Architecture / Specification
The guide focuses on core security practices across the agent lifecycle [^evt-wg-security-and-privacy-file-e24f19bec4ac-ea047250]:
- **Secrets Management:** Credential isolation, ephemeral token handling, and runtime key protection.
- **Secure Tool Invocation:** Safe tool dispatch, schema validation, and boundary enforcement during agent action execution.
- **Guardrails:** Policy enforcement and input/output guardrails mitigating prompt injection and out-of-scope behaviors.
- **Evaluation Frameworks:** Standardized testing, red-teaming, and security evaluation methodology.
- **Post-Incident Forensics:** Telemetry retention, audit logs, and diagnostic paths for post-compromise investigation.
- **External Framework References:** Curated mappings and pointers to external security frameworks and standards.

# Lifecycle History
- Workstream Leads: Fernando Lucktemberg (SAP) and Matthew Khouzam (Ericsson) [^evt-wg-security-and-privacy-file-e24f19bec4ac-ea047250].
- Contributors: Aditya Gidh (IBM), Allie Howe (Keycard), Alon Mazor (Ocean Security), Bar Kaduri (Capsule), Brad Tumy (Twilio), Dan Kommatas (Circle), Erin Farr (IBM), Govindaraj Palanisamy (Global Payments), Hsiao-Ying Lin (Huawei), Jonas Pfoh (Bluerock), Mitesh Bhawsar (Equinix), Mithil Patel (Equinix), Philipp Tiesel (SAP), Sagar Dashora (JPMorgan Chase), Saquib Saifee (IBM), Sohrab Farooq (TELUS), and Tom Sheffler (Lenovo) [^evt-wg-security-and-privacy-file-e24f19bec4ac-ea047250] [^evt-wg-security-and-privacy-pr-21].

[^evt-wg-security-and-privacy-file-e24f19bec4ac-ea047250]: https://github.com/aaif/wg-security-and-privacy/blob/d33f37911676bbe623b62164b720dbc4ec500c5b/workstreams/best-practices/README.md
[^evt-wg-security-and-privacy-pr-21]: https://github.com/aaif/wg-security-and-privacy/pull/21
