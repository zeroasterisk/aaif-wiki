---
type: resource
title: Security and Privacy Design Patterns Catalog
description: Vendor-neutral catalog of reusable architectural design patterns addressing
  runtime governance, agent isolation, and fail-safe execution.
resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-09-report.md
tags:
- security
- patterns
- resource
- architecture
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-09T10:19:16.159967+00:00'
sources:
- id: evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1
  resource: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-09-report.md
  author: Alex Frazer
  last_modified: '2026-10-09T08:54:25-06:00'
- id: evt-wg-security-and-privacy-pr-25
  resource: https://github.com/aaif/wg-security-and-privacy/pull/25
  author: awfrazer
  last_modified: '2026-10-09T14:54:26+00:00'
---

# Overview
The Security and Privacy Design Patterns Catalog is an architectural catalog maintained by the [Security and Privacy Working Group](../working-groups/security-and-privacy.md) providing repeatable, verifiable design patterns for securing agentic systems.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1] Led by Dan Kommatas and Sagar Dashora, the workstream standardizes architectural controls across agent harnesses, tool runtimes, and external communication boundaries.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]

# Architecture / Specification
The catalog requires each design pattern to follow a standardized specification template defining context, forces, structural invariants, and runtime trade-offs.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1] The foundational pattern set includes:
- [Approval Checkpoint](../patterns/approval-checkpoint.md): Binds external authorization to action payloads prior to runtime side effects.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]
- [Kill Switch](../patterns/kill-switch.md): Provides out-of-band execution termination, token revocation, and state quarantine mechanisms.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]
- [Attested Isolated Runtime](../patterns/attested-isolated-runtime.md): Enforces isolated policy evaluation, cryptographic evidence generation, and credential release boundaries.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]

Subsequent patterns in the workstream pipeline address memory boundaries, context poisoning prevention, and multi-agent interaction isolation.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]

# Lifecycle History
The catalog landing page, pattern template, and the first four pattern drafts merged via PR #26 on 2026-09-30 under `workstreams/design-patterns/`.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1] External PR #11 was superseded by and incorporated into PR #26, and follow-up PR #28 initiated subsequent revisions to the Approval Checkpoint pattern.[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]

[^evt-wg-security-and-privacy-file-60f28464dd94-24e4fdf1]: https://github.com/aaif/wg-security-and-privacy/blob/22c3f9a2cdac4fcf092502fa06154b08b4df09b8/reporting/2026-09-report.md
