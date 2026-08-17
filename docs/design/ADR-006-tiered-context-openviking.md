# ADR-006: Tiered Context Discipline (OpenViking Export Considered)

## Status
**Considered** — demoted from "Proposed (P2 Target)". OpenViking export is *not* on the roadmap. The
L0/L1/L2 authoring discipline it motivated **is** adopted and is binding on every generated page.

## Context
Downstream agents want hierarchical retrieval — a cheap summary for routing, a structural outline for
planning, the full document only when they commit to reading it. Flat vector chunking destroys that
hierarchy.

[`volcengine/OpenViking`](https://github.com/volcengine/OpenViking) is a filesystem-paradigm context
database engineered around exactly that L0/L1/L2 split, and the previous revision of this ADR made
"compile-compatible with OpenViking" a Phase-2 deliverable.

Two things changed:

1. **The consumer model was clarified (ADR-007).** The canonical artifact is the OKF v0.2 bundle in
   git. Everything else — MCP server, visualizer, digest, OpenViking — is an *exporter layered over
   that bundle*. Under that model, OpenViking is one possible exporter among several, not an
   architectural target that the core schema must be shaped around.
2. **There is no demand for it.** No user, no consumer, no concrete workload. Committing to an
   OpenViking dependency and a vector-generation step to serve a hypothetical is scope we cannot
   justify against a $200-ceiling budget (ADR-004).

But the *reason* the mapping worked in the first place is durable: it works because well-structured
documents already contain their own tiers. That part survives.

## Decision
**Do not build an OpenViking exporter now.** Record it as a considered, viable option.

**Do adopt, permanently and unconditionally, the L0/L1/L2 authoring discipline** as a hard
requirement on every page the curator generates. This is the durable takeaway and it is enforced by
the ADR-008 validators.

```
   ┌──────────────────────────────────────────────────────────────────┐
   │        Canonical OKF v0.2 Bundle  (wiki/*.md, in git)            │
   │                                                                  │
   │   Every page is authored so its tiers are extractable            │
   │   deterministically, with no model in the loop:                  │
   │                                                                  │
   │     L0 ◄── frontmatter `description` (one line)                  │
   │     L1 ◄── heading tree (strict H1 → H2 → H3) + outbound links   │
   │     L2 ◄── the full body                                         │
   └────────────────────────────────┬─────────────────────────────────┘
                                    │
        ┌───────────────┬───────────┴────────────┬──────────────────┐
        ▼               ▼                        ▼                  ▼
  OKF MCP server   Visualizer            Digest exporter    OpenViking export
  (ADR-007)        (graph.json)          (ADR-009/010)      ── CONSIDERED ──
                                                            not built
```

### The authoring discipline (binding)
| Tier | Source in the page | Rule |
| :--- | :--- | :--- |
| **L0 — summary** | Frontmatter `description` | Exactly one line. A complete sentence. Must make sense with zero other context — no "This document describes the above." No trailing period-less fragments. |
| **L1 — outline** | Heading tree + first paragraph of `# Overview` | The `# Overview` first paragraph must be **self-contained**: readable in isolation, naming the concept and its working group. Headings follow a **strict hierarchy** — exactly one H1, no skipped levels (`##` never appears under an `#` that has no intervening content, `###` never follows `#` directly). Conventional headings per ADR-001, plus `# Computation` for `Attested Computation` concepts. |
| **L2 — full asset** | The complete Markdown body | Everything else: specification tables, examples, lifecycle history, references. |

Three properties make this worth enforcing regardless of who consumes it:

- **Deterministic extraction.** L0 and L1 are pulled by a parser, not summarized by a model. Free,
  reproducible, and cheap enough to run in CI.
- **It is just good writing.** A one-line description and a self-contained opening paragraph are
  what a human skimming the index needs too. This discipline pays for itself on the human path.
- **It makes any future tiered exporter trivial.** OpenViking, a RAG index, an MCP `list` response,
  or a digest blurb all read the same three tiers. If we ever want OpenViking, the corpus is already
  shaped for it — that is the whole point of recording this as Considered rather than Rejected.

### Reconsideration criteria
Revisit OpenViking export when *all* of: (a) a concrete consumer asks for tiered retrieval that the
generic OKF MCP server (ADR-007) cannot serve; (b) the bundle exceeds a size where full-document
loading is actually the bottleneck; (c) OpenViking's API has stabilized enough that the exporter is
maintainable by one person. Until then, the mapping table above is the entire deliverable.

## Consequences

### Positive
* **Scope reduction with no lost optionality.** We shed a dependency and a vector-generation step
  while keeping the corpus shaped so the exporter stays a weekend's work if it is ever wanted.
* **The discipline is enforceable today.** Strict heading hierarchy, one-line `description`, and
  self-contained `# Overview` are all checkable by a deterministic validator in CI (ADR-008) — no
  LLM, no judgement call.
* **Human readers benefit first.** The same structure that serves tiered agent retrieval is what
  makes the index skimmable and the pages usable in Obsidian.
* **Honest status.** "Considered" describes reality. "Proposed (P2 Target)" implied a commitment
  that nobody had made.

### Negative / Trade-offs
* **No tiered retrieval today.** Agents consuming the bundle load whole documents or implement their
  own tiering from the heading tree. Acceptable at current corpus size; a real cost if the corpus
  grows an order of magnitude.
* **Authoring constraints bind the curator.** Strict heading hierarchy and a one-line description
  are extra rules in the Stable prompt tier and extra ways for a generation to fail validation and
  need a retry, which costs tokens.
* **A discipline with no current consumer can rot.** Mitigated only because the validators run in
  CI and block merge — without that enforcement this section would be aspiration, not architecture.
