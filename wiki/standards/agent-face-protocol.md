---
type: standard
title: Agent Face Protocol
description: Transport-agnostic JSON specification enabling AI agents to communicate
  operational state, facial expressions, reactions, and speech visemes to human users.
resource: https://github.com/aaif/project-proposals/issues/66
tags:
- standard
- protocol
- ux
- human-agent-interaction
- mcp
- proposal
status: draft
generated:
  by: agent:aaif-wiki-curator/gemini-3.8-flash
  at: '2026-11-02T10:31:15.104701+00:00'
sources:
- id: evt-project-proposals-issue-66
  resource: https://github.com/aaif/project-proposals/issues/66
  author: bwndapp
  last_modified: '2026-10-30T05:10:02+00:00'
---

# Overview

The Agent Face Protocol (AFP) is a lightweight, transport-agnostic JSON specification designed to give autonomous AI agents an interpretable visual and conversational face.[^evt-project-proposals-issue-66] Proposed to the AAIF as a Sandbox stage project alongside the open-source `bbot` reference renderer, AFP provides a neutral vocabulary for agents to display operational lifecycle states (`thinking`, `working`, `waiting`, `error`), nuanced expressions, reactive gestures, and speech with lip-sync.[^evt-project-proposals-issue-66]

# Architecture / Specification

## Protocol Components

The protocol decouples emotional and operational state semantics from graphical rendering engines, exposing four foundational signaling primitives:[^evt-project-proposals-issue-66]

- **Operational States**: Standardized high-level statuses indicating background agent execution (such as tool execution, waiting for human approval, or encountering exceptions).
- **Expressions**: A catalog of thirty distinct emotional expressions paired with plain-language glosses to support accessibility captions and screen readers.[^evt-project-proposals-issue-66]
- **Reactions**: Discrete one-shot non-verbal reactions (such as `nod` or `shake`).
- **Speech and Visemes**: Timed phonetic viseme sequences enabling real-time lip synchronization with speech synthesis backends.[^evt-project-proposals-issue-66]

## Integration Surfaces

- **Model Context Protocol (MCP)**: AFP defines standard MCP tool bindings (`face_state`, `face_express`, `face_react`, `face_look`, `face_speak`), allowing any MCP-compliant agent host to manipulate avatar rendering via direct tool calls.[^evt-project-proposals-issue-66]
- **Agent Host Integrations**: Sits at the human-facing edge of execution hosts like [Goose](../resources/goose.md) to visualize multi-minute background tasks such as code generation and tool negotiation.[^evt-project-proposals-issue-66]
- **Skills Discovery**: Ships with structured discovery manifests compatible with [Agent Skills](../standards/agent-skills.md) conventions (`SKILL.md` and `llms.txt`) enabling coding agents to provision visual interfaces autonomously.[^evt-project-proposals-issue-66]

[^evt-project-proposals-issue-66]: https://github.com/aaif/project-proposals/issues/66
