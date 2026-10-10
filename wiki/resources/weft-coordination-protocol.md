---
type: resource
title: Weft Coordination Protocol and Agent Hooks Core
description: Vendor-neutral hook interoperability layer and real-time edit coordination
  protocol preventing concurrent agent merge conflicts via ordered event logs and
  diagnostics.
resource: https://github.com/aaif/project-proposals/issues/53
tags:
- protocols
- coordination
- hooks
- coding-agents
- multi-agent
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.7-flash
  at: '2026-10-10T15:24:22.444967+00:00'
sources:
- id: evt-project-proposals-issue-53
  resource: https://github.com/aaif/project-proposals/issues/53
  author: celador
  last_modified: '2026-10-10T01:09:23+00:00'
---

# Overview

The Weft Coordination Protocol (WCP) and Agent Hooks Core is an open protocol suite designed to coordinate concurrent coding agents operating across shared codebases [^evt-project-proposals-issue-53]. Rather than deferring conflict resolution to merge time, WCP enables edit-time coordination by routing agent tool invocations through pre-execution hooks to a per-repository coordinator that maintains a strictly ordered event log and delivers mid-turn diagnostics [^evt-project-proposals-issue-53].

# Architecture / Specification

The protocol specification is structured into two decoupled layers [^evt-project-proposals-issue-53]:

### 1. Agent Hooks Core (v0.1)

A lightweight, vendor-neutral interoperability layer standardizing coding agent harness hooks:
- **Common Event Envelopes**: Standardized data interchange formats representing tool-call events, allow/deny/ask policy decisions, and runtime diagnostics [^evt-project-proposals-issue-53].
- **Capability Declarations**: Standardized host capability manifests enabling hooks to discover host feature sets across diverse agent harnesses (including Claude Code, Codex, Cursor, Gemini CLI, and OpenCode) [^evt-project-proposals-issue-53].
- **Conformance Suite**: Standalone conformance runner (`wcp-hook-conformance`) providing validation fixtures and adapter compliance tests [^evt-project-proposals-issue-53].

### 2. Weft Coordination Protocol (WCP v0)

A distributed coordination extension operating on top of the Hooks Core [^evt-project-proposals-issue-53]:
- **Ordered Event Log & Replay**: Per-repository event journal guaranteeing deterministic replay of concurrent agent edits [^evt-project-proposals-issue-53].
- **Fine-Grained Conflict Tracking**: Symbol-level read/write set registration and lease-based claim management (soft and firm claims) [^evt-project-proposals-issue-53].
- **Arbitration and In-Loop Feedback**: Proactive diagnostic generation alerting an agent mid-turn when a target symbol has been modified concurrently, accompanied by stop/commit gating to prevent closing turns with unresolved conflicts [^evt-project-proposals-issue-53].

# Lifecycle History

- Proposed as an AAIF project by John Nelson on 2026-10-10 under issue #53 [^evt-project-proposals-issue-53].

[^evt-project-proposals-issue-53]: https://github.com/aaif/project-proposals/issues/53
