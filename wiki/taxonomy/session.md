---
type: taxonomy
title: Session
description: A bounded span of agent activity that shares one accumulated working
  state, beginning when that state is created and ending when it is discarded or handed
  off.
resource: https://github.com/aaif/ws-taxonomy-landscape/issues/45
tags:
- taxonomy
- universal
- runtime
- state
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-23T09:51:16.449718+00:00'
sources:
- id: evt-ws-taxonomy-landscape-issue-45
  resource: https://github.com/aaif/ws-taxonomy-landscape/issues/45
  author: asish-singh
  last_modified: '2026-08-22T12:07:55+00:00'
---

# Overview

A session is a bounded span of agent activity that shares one accumulated working state, beginning when that state is created and ending when it is discarded or handed off [^evt-ws-taxonomy-landscape-issue-45].

# Scope and Semantics

The boundary of a session is determined by the lifecycle of its working state rather than by wall-clock time, transport connection stability, or user-visible conversation intervals [^evt-ws-taxonomy-landscape-issue-45]. A single ongoing conversation can span several consecutive sessions when working state is summarized, compressed, and reloaded into a fresh execution context [^evt-ws-taxonomy-landscape-issue-45]. Conversely, a single session can serve several distinct user interactions or subtasks as long as they share the active working state [^evt-ws-taxonomy-landscape-issue-45].

The physical storage location of the accumulated working state—whether maintained directly within model context windows, agent harness memory structures, or external temporary caches—is an implementation choice that does not alter whether an execution window constitutes a session [^evt-ws-taxonomy-landscape-issue-45]. Durable artifacts that intentionally survive the session boundary, such as persistent databases or saved file artifacts, represent outputs left behind by the session rather than active session state [^evt-ws-taxonomy-landscape-issue-45]. Similarly, a long-running background process that performs stateless polling or accumulates no state constitutes a process rather than a session [^evt-ws-taxonomy-landscape-issue-45].

# Lifecycle History

The definition for Session was submitted as a universal taxonomy term to the Taxonomy and Landscape workstream in August 2026 to resolve an unpopulated placeholder [^evt-ws-taxonomy-landscape-issue-45].

# References

- [Context Exhaustion](../taxonomy/context-exhaustion.md)
- [Context](../taxonomy/context.md)
- [Agent Behavior Trace Model](../standards/agent-behavior-trace-model.md)
- [Workflows and Process Integration Working Group](../working-groups/workflows-and-process-integration.md)

[^evt-ws-taxonomy-landscape-issue-45]: https://github.com/aaif/ws-taxonomy-landscape/issues/45
