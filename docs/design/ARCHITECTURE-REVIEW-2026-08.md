# Architecture Review — `aaif-wiki`

**Date:** 2026-08-17
**Reviewer:** Cowork (agentic review pass)
**Scope:** `README.md`, `config.yaml`, `pyproject.toml`, `.gitignore`, `docs/design/ADR-001` … `ADR-007`
**Commit under review:** `1e76078` — *feat(init): bootstrap aaif-wiki with OKF v0.2, Temporal + ADK architecture, and ADRs 001-007*

---

## 0. Verdict

The design is **coherent, well-written, and over-built for the problem it actually has.**

The individual ADRs are competent in isolation. The failure is at the seams: three separate
subsystems (Temporal durability, event sourcing, agent-harness guardrails) are each justified
by the same underlying fear — *"a long agent run might die partway and waste tokens"* — and
none of the three ADRs acknowledges that the other two exist to solve the same thing. Meanwhile
the two risks that are genuinely novel and specific to this project — **an LLM authoring
"consensus" definitions for a Linux Foundation body with no human in the loop**, and **an
agent ingesting arbitrary untrusted text from public PRs and then publishing to a public Gist** —
have no ADR at all.

The workload, stated plainly: *~15 markdown-heavy repos, scanned on a bi-weekly cadence,
producing a few dozen concept pages.* That is a batch job measured in minutes. The architecture
specified is one appropriate for a continuously-running, multi-tenant, high-throughput ingestion
platform.

Three things to change, in priority order:

1. **Delete an orchestrator.** ADK 2.0 — already a hard dependency at `>=2.5.0` — ships a
   graph-based Workflow Runtime with retry, fan-out/fan-in, loops, state persistence and
   human-in-the-loop breakpoints. Temporal adds a daemon prerequisite and a second, divergent
   execution path (ADR-002 already concedes a `--direct` fallback runner) to buy durability that
   the event store in ADR-003 largely already provides.
2. **Add a review gate.** Nothing currently stands between "LLM wrote a taxonomy definition" and
   "published as an AAIF consensus term." OKF v0.2 hands you the exact vocabulary for this
   (`status`, `verified`) and ADR-001 declines to use it.
3. **Treat ingested content as hostile.** ADR-007's privacy boundary is pointed outward
   (don't leak corporate paths). The unguarded direction is inward.

*An earlier draft of this review listed a fourth headline item claiming `gemini-3.7-flash` was
not a real model. That was a verification error on my part — the model shipped 2026-08-13 and
the config was correct. See F5 for the retraction and the residual (minor) point.*

---

## 1. What is genuinely good

Worth stating plainly, because the critique below is long:

- **OKF as the storage format is the right call, for the right reasons.** Markdown + YAML in
  git, no runtime, no proprietary store, inspectable with `cat` and `git diff`. This is correct
  and the ADR-001 rationale holds up against the actual spec.
- **Separating the raw event log from the projected wiki (ADR-003) is a real architectural
  insight,** not decoration. Being able to change the prompt and re-derive is the thing that
  makes an agentic wiki maintainable rather than a one-way ratchet.
- **Naming iteration budgets and no-progress halts as *architecture* (ADR-004) rather than
  leaving them as implementation detail** is a level of rigor most agent projects skip.
- **The ADR discipline itself.** Seven records with Context/Decision/Consequences and an index
  table, before any code — the review criteria in `docs/design/README.md` are the right four
  questions. The findings below are largely *the answers to those questions being "no."*

---

## 2. Findings

Severity: **S1** = fix before writing code · **S2** = fix before first public output · **S3** = correctness / hygiene

### S1 — Foundational

---

#### F1 · Two orchestrators, one of which is redundant with the other two ADRs
**Where:** ADR-002; ADR-003; `pyproject.toml`; `config.yaml:temporal`

ADR-002 adopts Temporal for durability. But durability is *already* being purchased twice more:

| Mechanism | ADR | What it protects |
| :-- | :-- | :-- |
| Temporal workflow state | ADR-002 | Resume mid-pipeline after crash |
| Immutable event store + replay | ADR-003 | Re-derive everything from raw inputs |
| Iteration budgets / no-progress halt | ADR-004 | Bound a single agent run |

ADR-002's headline benefit is *"if an LLM call fails at repository #14 with a 429, Temporal
resumes at repo #14 without repeating repos #1–13."* But ADR-003 already writes each repo's
events to disk as they are extracted. A re-run that skips repos whose events are already on
disk gets the same property for roughly twenty lines of idempotency check — no daemon, no
task queue, no namespace, no worker process.

What Temporal costs here:
- A prerequisite background service for every run (ADR-002 lists this as the sole trade-off,
  which understates it — it also blocks the obvious deployment target, GitHub Actions).
- **Two execution paths that will diverge.** ADR-002 §Execution Modes already specifies
  `aaif-wiki run --direct` as a Temporal-free fallback "for fast local unit testing." Every
  bug will now need reproducing twice, and the `--direct` path will silently rot.
- Determinism constraints on workflow code that are subtle and easy to violate.

And what makes it hard to justify in 2026: **ADK 2.0 already is the orchestrator.** Per the
`google-adk` 2.x release notes, the Workflow Runtime provides *"routing, fan-out/fan-in, loops,
retry, state management, dynamic nodes, human-in-the-loop, and nested workflows."* That is
ADR-002's entire feature list, from a dependency already pinned at `>=2.5.0`, with no daemon.

**Recommendation.** Default to **ADK 2.0 Workflow Runtime, triggered by a GitHub Actions cron**,
with idempotency derived from the event store. Define a narrow `Orchestrator` interface and keep
Temporal as an *optional* backend for anyone who later needs multi-hour or multi-tenant runs.
Rewrite ADR-002 accordingly; do not delete it — the analysis is worth keeping as the record of
why Temporal was considered and deferred.

> If the real motivation is *"I want to demonstrate Temporal + ADK together"* — that is a
> perfectly legitimate goal for a portfolio/reference project, but it should be written down
> as the goal in ADR-002's Context. Right now the ADR justifies Temporal on operational grounds
> that this workload does not generate. See **Q1**.

---

#### F2 · "Deterministic replayability" is claimed but not achievable, and nothing measures quality
**Where:** ADR-003 §Consequences; `docs/design/README.md` review criterion #1

ADR-003 states replay mode *"rebuilds the knowledge graph deterministically."* It does not.
Replay wipes `wiki/` and re-derives it by feeding events through an LLM at `temperature: 0.2`.
That is **re-derivable, not deterministic** — two replays of identical inputs will produce
different prose, different link choices, and potentially different concept boundaries.

This matters beyond pedantry, because `docs/design/README.md` sets the review bar as
*"Can the knowledge graph be reconstructed from raw events without context drift?"* — and as
specified there is **no mechanism anywhere in the seven ADRs that would detect drift if it
happened.** No golden outputs, no schema conformance test, no link-validity check, no factuality
eval, no CI. The `wiki/` directory is wiped and regenerated on the operator's trust.

**Recommendation.**
- Restate the property honestly in ADR-003: *"reproducible by re-derivation; not bit-identical."*
- Add **ADR-008: Evaluation & Quality Gates** covering: (a) a frozen golden set of ~20 events →
  expected concepts, diffed on every prompt change; (b) deterministic validators that need no
  LLM — YAML schema conformance, every internal link resolves, every `sources[]` entry maps to a
  real `event_id`, no orphan concepts; (c) these run in CI and block merge.
- Make replay non-destructive by default: render to `wiki.replay/` and diff against `wiki/`,
  rather than `rm -rf` and hope.

The deterministic validators in (b) are cheap, catch the majority of real failures, and are the
single highest-value thing that can be built before the curator agent exists at all.

---

#### F3 · No human review gate on machine-authored "consensus" for a Linux Foundation body
**Where:** absent from all ADRs; `config.yaml:sources.github.include_open_prs: true`; ADR-007

The pipeline as designed is: ingest → LLM curates → write to `wiki/` → publish a public Gist.
There is no point at which a human approves anything.

The content being generated is not neutral. `wiki/taxonomy/` is described in ADR-001 as
*"Consensus terms and definitions"* and ADR-007's `GistExporter` publishes a
*"bi-weekly executive briefing."* AAIF is a real Linux Foundation body with real working groups
and a real Technical Committee. An LLM inferring that a term is "consensus" — from a corpus that
`include_open_prs: true` deliberately includes **unmerged, unaccepted proposals** — and then
publishing that inference is a governance problem before it is a quality problem. A vendor
participating in a WG could reasonably object to a machine-generated page asserting their
draft PR represents foundation consensus.

**Recommendation.** This is where OKF v0.2 pays for itself (see F6):
- Curator output lands on a branch and opens a **pull request**; `main` is never written directly.
- Every generated concept ships `status: draft` and carries no `verified` entry. Under the v0.2
  trust-tier convention that places it in the **unverified** tier — machine-readably distinct
  from reviewed content, with no extra vocabulary invented.
- A human merging the PR adds a `verified: [{by: "human:<id>", at: ...}]` entry, promoting the
  concept to `status: stable` and the **human-reviewed** tier.
- Concepts derived from open PRs are pinned to `status: draft` permanently until the PR merges.
- The `GistExporter` publishes **only** human-reviewed concepts. Draft content never leaves the repo.

ADK 2.0's native human-in-the-loop breakpoints make this a first-class workflow node rather
than a bolt-on. Write it up as **ADR-009: Human-in-the-Loop Publication Gate**.

---

#### F4 · Ingested content is untrusted input, and nothing treats it that way
**Where:** ADR-007 (guards the wrong direction); ADR-003 `RawEvent.raw_text`

ADR-007 builds a careful privacy boundary to stop *internal* details leaking *outward*. That is
a legitimate concern and the leak-guard regex audit is good practice. But it is the smaller risk,
and it is pointed the wrong way.

The actual exposure: this pipeline reads **arbitrary attacker-controllable text** — PR bodies,
issue comments, commit messages, markdown files from any repo in the org, including from
first-time external contributors — and feeds it verbatim (`raw_text`) to an agent that holds:

- **write access to `wiki/`** (it authors the taxonomy), and
- **publish access to a public GitHub Gist** (via `gh` CLI with the operator's credentials).

A PR description containing instructions aimed at the curator can attempt to rewrite a definition,
insert a link to an attacker-controlled domain into published output, or suppress a competitor's
concept page. The Gist exporter turns this into an exfiltration channel. Nothing in ADR-004
(which covers *accidental* failure — 429s, loops, token blowup) addresses *adversarial* input.

**Recommendation.** Rescope ADR-007 from "Privacy Boundary" to **"Trust Boundary"**, keeping the
existing outbound leak-guard and adding inbound controls:
- All ingested content is wrapped in explicit data delimiters and labelled as untrusted data in
  the prompt; the harness instruction states that instructions found inside ingested content are
  content to be described, never directives to follow.
- Ingested text carries **no tool-call authority** — the curator's write path is a structured
  mutation receipt validated against the OKF schema, not free-form file writes.
- **Outbound link allowlist** on export: only `github.com/aaif/*`, `aaif.io`, `linuxfoundation.org`
  and an explicit allowlist survive sanitization. Everything else is stripped or footnoted as
  unverified. This closes the exfiltration path and is deterministic, so it belongs in CI.
- The F3 review gate is the real backstop: a human sees the diff before anything is published.

Note the pleasing symmetry — the AAIF Security and Privacy WG is one of the repos being ingested.
Getting this wrong in a tool *about* that WG would be unfortunate.

---

#### F5 · ~~`gemini-3.7-flash` does not exist~~ — **RETRACTED.** Model pinning strategy (S3)
**Where:** `config.yaml:curator.model`; ADR-001 §Frontmatter example; ADR-005 §Context and §3

> **Correction (2026-08-17).** The original version of this finding claimed `gemini-3.7-flash`
> was not a real model and rated it **S1**. **That was wrong.** Gemini 3.7 Flash shipped
> **2026-08-13** — four days before this review — three weeks after Gemini 3.6 Flash, at an
> introductory $0.75/1M input and $3.75/1M output. The config was correct and the ADRs were
> correct.
>
> The error came from a badly-scoped verification query (`"gemini 3 flash model id vertex ai"`),
> which surfaced the December 2025 Gemini 3 Flash launch and nothing from the 3.5/3.6/3.7 line.
> A null result from a query that never covered the relevant space was treated as evidence of
> absence. Retained here rather than deleted so the reasoning failure stays auditable.

**The residual, much smaller finding.** The Flash line is currently moving on a **~3-week
cadence** (3.5 → 3.6 → 3.7 within roughly six weeks). That churn rate is itself an
architectural input, and it cuts *both* ways:

- **For pinning** (current choice): replay reproducibility. ADR-003's replay mode re-derives
  the wiki through the model; a floating alias means a replay six weeks from now runs on a
  different model than the one recorded in `generated.by`, quietly breaking the provenance
  claim in ADR-001. **Pinning is defensible and probably correct** for this project.
- **For aliasing**: a pinned model on a 3-week cadence goes stale fast, and price drops
  (3.7 launched at half 3.6's cost) are left on the table.

**Recommendation.** Keep the pin, but make the choice explicit rather than incidental:
- Record the model in `generated.by` frontmatter **as the resolved id**, never as an alias,
  so replay provenance stays truthful regardless of which the operator configures.
- Add an explicit `fallback_model` — ADR-005 claims model-agnostic routing via `DispatchingLlm`,
  but the config offers exactly one model and no route to a second, so the claim is **untested
  by construction**. This is the part of the original finding that still stands.
- Target **Vertex AI on the `global` endpoint with ADC** as the default auth path, AI Studio
  key as fallback.
- Gemini 3.x exposes thinking-effort levels; a curator doing schema-constrained extraction
  should set this deliberately rather than inherit a default. Note it in ADR-005.
- Add a note to ADR-005 that the pinned model is expected to be revisited on roughly a
  quarterly basis, so the pin is a decision with a review date rather than a fossil.

---

### S2 — Major

---

#### F6 · The OKF v0.2 profile omits precisely the fields that solve ADR-001's stated problem
**Where:** ADR-001 §Frontmatter Schema

This is the sharpest finding in the review, because the ADR argues *against itself*.

ADR-001 §Context opens by naming the problem:

> **Opaque Retrieval**: Black-box vector search cannot distinguish between historical drafts,
> active proposals, and merged standards.

OKF v0.2 — the spec this ADR adopts — added fields whose entire purpose is that distinction:

| v0.2 field | Purpose | In ADR-001? |
| :-- | :-- | :-- |
| `status` | `draft` → `stable` → `deprecated` (absent = stable) | **No** |
| `stale_after` | absolute date; freshness as a plain date comparison | **No** |
| `verified[]` | `{by, at}`; consumer derives unverified / machine-confirmed / human-reviewed | **No** |
| `sources[].author`, `.last_modified`, `.usage_count` | per-source credibility signals | **Partial** — ADR-001 has only `id` + `resource` |
| `generated: {by, at}` | provenance of the generating actor | **Yes** ✓ |

The ADR adopts the one v0.2 field family it already had a v0.1 habit for (`generated`) and skips
the four that were the actual reason v0.2 shipped. For a corpus that is *by definition* a mix of
merged standards and open PRs, `status` is not optional polish — it is the feature.

Secondary conformance issues in the same ADR:

- **Over-strict MUSTs.** ADR-001 mandates `type`, `title`, `description`, `resource`, `tags`,
  `generated`, `sources` on every document. In OKF, **`type` is the only required field**; the
  rest are *recommended*. Being stricter internally is fine and probably right — but the document
  should say it is defining a **profile of OKF**, not restating OKF. (Note the upstream reference
  implementation has the same drift, requiring four keys against a one-key spec — so this is a
  known trap, not an original error.)
- **Missing `okf_version: "0.2"`** in the bundle-root `wiki/index.md`. This is the spec's version
  marker (bundle-root index metadata, not per-concept) and it is how a consumer knows which
  fallbacks to apply. Cheap to add, and its absence makes the "OKF v0.2" badge in the README
  unverifiable by tooling.
- **Citation style is v0.1.** ADR-001 §Body Structure specifies a `# References` heading. In v0.2
  the body `# Citations` list is **superseded by frontmatter `sources`**, with per-claim
  attribution via markdown footnotes keyed to the source id (`[^evt-spaa-pr11]`). Per-claim
  footnotes are strictly better for this project anyway — a concept page synthesized from nine
  PRs is far more auditable when each sentence points at its event.
- **Link style is self-contradictory and will break.** §3 calls them *"relative Markdown links"*
  and then gives `[Attested Isolated Runtime](/architectures/attested-isolated-runtime.md)` — a
  leading `/` is **root-absolute**. That resolves wrongly on a GitHub Pages project sub-path
  (`/aaif-wiki/...`), in Obsidian, and in any nested-bundle consumer. Use true relative paths
  (`../architectures/…`) and add a link-resolution check to the CI validators from F2.
- **Typed edges are a local invention.** README and ADR-007 refer to *"directional wikilink
  edges"* and a `related_topics` graph (ADR-006). OKF has **no typed-relationship field** — typed
  relationships are an open upstream proposal, not spec. Any edge typing here is a producer
  extension and must be namespaced so downstream consumers don't mistake it for standard OKF.

**Recommendation.** Rewrite ADR-001's schema block to the full v0.2 vocabulary, restyle it as
*"the AAIF profile of OKF v0.2,"* fix the link style, move citations to footnotes, and add
`okf_version` to the bundle root. This single edit also unlocks F3 at zero additional cost.

---

#### F7 · The event store duplicates git, in a format that diffs badly
**Where:** ADR-003 §Technical Schema (`raw_text`); `.gitignore`

`RawEvent` inlines the full `raw_text` of every changed file, and `raw/events/` is committed to
git. For a corpus that is *itself* markdown files in git repos, this means every document version
is stored twice: once in the upstream repo's git history, once again as a JSON-escaped string
blob in this repo.

Consequences the ADR waves off as *"Storage Footprint … mitigated by text compression"*:

- JSON-escaped markdown produces unreadable diffs (`"# Overview\n\nThe **attested**…"` on one
  line), defeating ADR-001's stated virtue of git-diff auditability.
- Every bootstrap re-run risks re-emitting near-identical blobs, and the repo grows monotonically
  because git history is permanent.
- It re-implements content-addressed storage inside a system already built on content-addressed
  storage. The schema even carries `content_sha256` — git already computed that.

**Recommendation.** Split by reproducibility:

- **Git-reproducible sources** (files in AAIF repos): store a **pointer** —
  `{repo, commit_sha, path, blob_sha}` — plus the derived `diff_summary`. Content is rehydrated
  on demand from a local shallow mirror under the already-gitignored `raw/cache/`. Offline replay
  still works; the mirror is the offline copy.
- **Ephemeral sources** (PR review comments, issue threads, meeting notes, anything editable or
  deletable upstream): inline the text — git *cannot* reproduce these, so they must be captured.

You keep full replayability and lose the duplication. Update ADR-003's schema and its Consequences.

---

#### F8 · No consumption story — and AAIF's own projects are the obvious answer
**Where:** ADR-006, ADR-007; absent as a first-class decision

Two exporters are specified: a public Gist digest and a static D3 graph for GitHub Pages. Both
are for **humans browsing**. But the README's premise is *"an auditable living wiki for AI agents
and human contributors,"* and the agent half has no serving path in Phase 1 — it is deferred to
ADR-006 (P2) behind a third-party vector database.

Look at what AAIF actually stewards: **MCP**, **AGENTS.MD**, **goose**, **agentgateway**. A
knowledge base *about* AAIF whose agent-facing interface is a ByteDance vector store, while the
foundation's own flagship project is the standard protocol for exactly this, is a strange
alignment — and it is the one recommendation in this review that is free marketing for the project.

**Recommendation.**
- **Promote an MCP server to a Phase 1 exporter.** A read-only MCP server over the bundle
  (`search_concepts`, `get_concept`, `list_working_groups`, `get_recent_changes`) is a few hundred
  lines over content you already have on disk, needs no vector store, and makes the wiki
  consumable by Claude, Gemini CLI, goose, and anything else speaking MCP on day one.
- **Ship an `AGENTS.md`** at the repo root pointing agents at the bundle — using AAIF's own
  convention, in a repo about AAIF.
- **Demote ADR-006 (OpenViking) from "P2 Target" to "Considered."** OpenViking is real and good
  — the L0/L1/L2 model is sound (`.abstract.md` ~100 tokens, `.overview.md` ~2k, full content on
  demand) and its benchmarks are credible. But it also *ships its own MCP server*, so if it is
  ever adopted it slots in behind the same interface. And the L0/L1/L2 mapping table in ADR-006
  is worth keeping regardless: it is really a **document-structure discipline** (one-line
  `description`, a self-contained `# Overview` first paragraph, strict heading hierarchy), and
  that discipline is valuable whether or not OpenViking is ever installed. Say that explicitly —
  it's the durable half of the ADR.
- Fix `exporters.visualizer.output_dir: "wiki"` — see F18.

---

#### F9 · No stated position on legitimacy for an unofficial wiki about a foundation
**Where:** absent; implied by README framing and ADR-007

The README describes the project as *"Autonomous Knowledge Graph & Living Wiki Engine for the
Agentic AI Foundation (AAIF),"* uses AAIF's name in the project name, and publishes public
briefings about AAIF's work. The repo is `zeroasterisk/aaif-wiki` — a personal repo, not an
`aaif/` repo. Nothing states the relationship.

This is genuinely ambiguous to a reader, and the ambiguity gets worse the more useful the project
becomes. A machine-generated "executive briefing" about a foundation's working groups, published
on a bi-weekly cadence under that foundation's name, will eventually be cited as if authoritative.

**Recommendation.** Add **ADR-010: Project Positioning & Attribution** — cheap to write, expensive
to retrofit:
- Explicit disclaimer in `README.md`, in `wiki/index.md`, and in the header of every published
  Gist: unofficial, not endorsed by or affiliated with AAIF or the Linux Foundation, all content
  machine-derived from public sources, canonical source always linked.
- Every concept page links to its upstream canonical artifact (`resource` frontmatter already
  carries this — use it in the rendered header, not just the metadata).
- Confirm the **license and attribution requirements of the ingested repos** and carry required
  attribution into derived pages. LF projects are typically Apache-2.0 or CC-BY-4.0; a derived
  work republishing substantial content inherits obligations. This is currently unexamined.
- State the **donation path**: if this proves useful, the intent is to offer it to AAIF (e.g. via
  `project-proposals`, which is already in the ingest list). Saying so up front converts a
  potential territorial problem into a contribution.

---

#### F10 · ADR-005 forks the upstream Horizon recipe, and the vendor-neutrality claim is false
**Where:** ADR-005; `pyproject.toml`

Two separate problems in one ADR.

**(a) Forking a live upstream.** The `long-horizon-harness` recipe landed in `google/adk-samples`
in **August 2026** — days before this repo was created. ADR-005 re-describes its patterns
(3-tier prompt assembly, `HorizonSummarizer`, `DispatchingLlm`) as local architecture to be
reimplemented under `aaif_wiki/curator/`. Reimplementing a recipe that is actively being developed
upstream means diverging from it in week one and inheriting none of its fixes.

**Recommendation:** depend on or vendor the upstream recipe with a pinned commit and a note on how
to re-sync. Reduce ADR-005 to *"we adopt the Horizon recipe; here is our configuration of it and
here is where we deviate and why."* An ADR that documents a **delta** stays true; an ADR that
restates someone else's design goes stale silently.

**(b) The neutrality claim is not true.** ADR-005 §Consequences claims *"Model Agnostic: Fully
decoupled from any single vendor SDK,"* and `docs/design/README.md` lists **Vendor Neutrality** as
a review criterion. The project hard-depends on `google-adk` and `google-genai`, defaults to a
Gemini model, and adopts a Google harness recipe.

Depending on ADK is a **fine and defensible choice** — it is a good framework and the author works
on it. The problem is only the claim. Vendor-neutrality lives in the *artifact* here, not the
*pipeline*: the output is plain markdown in git, readable with `cat`, portable to any consumer,
which is a genuinely strong neutrality story. Say that instead. Replace "vendor neutrality" in the
review criteria with **"output portability"** and let the pipeline be unapologetically ADK-native.

---

#### F11 · No lifecycle story for deletion, renames, or history rewrites; the cursor is a mutable SPOF
**Where:** ADR-003 §Ingestion Lifecycle Modes; `raw/.state.json`

The three modes (bootstrap / incremental / replay) cover the happy path only. Unhandled:

- **Upstream document deleted.** Does the concept page vanish, get tombstoned, or go
  `status: deprecated`? Event sourcing has no opinion unless you give it one — and silently
  keeping a page for a withdrawn proposal is exactly the staleness the project exists to prevent.
- **Repo renamed or archived.** WGs get restructured; AAIF is young and actively adding repos.
- **Force-push / rewritten history upstream.** Commit SHAs recorded in `sources` become dangling.
- **Concept renamed or merged.** Every inbound relative link breaks. There is no redirect or
  `superseded_by` convention (and note: `supersedes`/`superseded_by` are *not* in OKF v0.2 —
  they are open upstream proposals, so this would be a namespaced local extension).

Separately: **`raw/.state.json` is a single mutable file holding the incremental cursor**, inside
an architecture whose entire premise is immutability. It appears in neither `.gitignore` nor any
ADR's discussion of what is committed. Both options are bad: committed, it conflicts on every
concurrent run; uncommitted, incremental mode is not reproducible across machines or in CI.

**Recommendation.** Derive the cursor **from the event store itself** — the max ingested commit
SHA per repo is a `max()` over the events already on disk. Delete `.state.json`; one less thing
to corrupt, and it makes incremental mode reproducible anywhere the events are. Then add an
explicit tombstone event type (`source_type: deletion`) that projects to `status: deprecated`
rather than removing the file, preserving inbound links and the audit trail.

---

#### F12 · The cost ADR has no cost numbers
**Where:** ADR-004; `config.yaml`

ADR-004 is titled around resilience and rate limiting and lists *"Cost & Token Protection"* as a
headline benefit. It contains no numbers: no expected tokens per run, no expected wall-clock, no
per-run ceiling, no alert threshold, no estimate of event volume for 15 repos at bootstrap. The
only quantified guard is `iteration_budget: 15` turns per *concept batch* — which bounds a single
batch but says nothing about total spend, since nothing bounds the number of batches.

A bootstrap over 15 repos with `include_open_prs: true` is plausibly a few thousand documents.
That is the single most expensive operation the system will ever perform, and it is unestimated.

**Recommendation.** Add to `config.yaml` and enforce in the workflow: `max_tokens_per_run`,
`max_usd_per_run`, `max_concepts_per_run`. Hard-abort with a partial-progress commit on breach —
the event store makes resumption safe, so aborting is cheap. Record a measured cost figure in
ADR-004 after the first real bootstrap and keep it updated; an unfalsifiable cost claim is worse
than none.

---

### S3 — Correctness & hygiene

---

#### F13 · The context compactor can never fire
`config.yaml`: `iteration_budget: 15` · `compaction_threshold: 40`

ADR-004 hard-caps the agent at 15 reasoning turns. ADR-005 triggers `HorizonSummarizer` compaction
at *">40 tool turns."* The agent is terminated by the budget guard 25 turns before the compactor
becomes reachable. One of the two numbers is wrong, and as written **the entire compaction
mechanism in ADR-005 is dead code.** Decide which control is authoritative and set
`compaction_threshold` below `iteration_budget` (e.g. 15 / 10).

#### F14 · Retry attempts disagree between ADR and config
ADR-004 code block: `maximum_attempts=6` · `config.yaml`: `maximum_attempts: 5`. Pick one. The
config should be the single source of truth and the ADR should reference it rather than restating
a literal — restated literals in ADRs drift by default.

#### F15 · "Full jitter" is mislabeled
ADR-004 §2 calls `min(t_max, t_init × 2^n) × uniform(0.8, 1.2)` *"exponential backoff with full
jitter."* That is **equal jitter** at ±20%. Canonical *full* jitter is `uniform(0, backoff)`.
The distinction is operationally real: ±20% barely decorrelates a thundering herd, which is the
whole point of jittering. Either implement `uniform(0, backoff)` or rename it "bounded jitter."
Also note this hand-rolled sleep is largely redundant with the retry policy above it in the same
ADR — the `Retry-After` header extraction is the part worth keeping.

#### F16 · The truncation strategy is for source code, not prose
ADR-004 §4 summarizes oversized diffs via *"structured AST metadata (file paths, symbols modified,
export signatures)"* and strips *"lockfiles, compiled binaries, minified bundles."* This corpus is
`.md`, `.markdown`, `.yaml`, `.yml` (per `config.yaml:doc_extensions`). There are no export
signatures in a WG charter. This reads as inherited from a code-documentation design — OpenWiki,
cited as inspiration, is explicitly codebase-first — without adaptation. Replace with a prose
strategy: heading-tree extraction, section-level diffing, frontmatter-only for unchanged bodies.
The lockfile stripping is harmless but will never trigger given the extension filter.

#### F17 · Root-absolute links described as relative
Covered in F6; repeated here because it is a one-line fix with a CI check attached.

#### F18 · Build artifacts inside the canonical bundle
`wiki/graph.json` (ADR-001 §1) and `exporters.visualizer.output_dir: "wiki"` both write **derived**
artifacts into the **canonical** OKF bundle. Consequences: consumers must know to skip non-concept
files; `graph.json` is a guaranteed merge-conflict on any concurrent run; and a regenerable file
is version-controlled alongside source-of-truth content. Emit derived output to `dist/` and
generate it at export time. Keep `wiki/` as pure OKF: concepts, `index.md`, `log.md`.

#### F19 · Working-group count is wrong, and the repo list should not be hardcoded
README claims *"8 Working Group concept pages"* and ADR-001 *"8 working groups."* AAIF publishes
**seven** working groups — Identity and Trust; Governance, Risk, and Regulatory; Workflows and
Process Integration; Accuracy and Reliability; Security and Privacy; Agentic Commerce;
Observability and Traceability — plus **one cross-group workstream**, Taxonomy and Landscape.
`config.yaml` gets the repo list right (7 × `wg-*` + 1 × `ws-*`) but the prose collapses the
distinction, and that distinction is *governance-meaningful* — a workstream is not a WG.

Related: the 15 repos are hardcoded. AAIF is actively growing (`project-proposals`,
`working-group-proposals`, `public-agents`, `aaif-landscape` are all recent). **Discover repos
from the org API** with an optional exclude-list; a wiki that silently misses a new WG because a
YAML list wasn't updated fails at its one job.

#### F20 · No LICENSE file, no CI, no tests, no CONTRIBUTING
`README.md` badges Apache-2.0 and links to `LICENSE`. **The file does not exist** — the badge is a
broken link. There is also no `.github/`, no workflow, no test directory, and no contribution
guide, in a project whose entire subject is open-source foundation governance. `pyproject.toml`
declares `pytest`/`pytest-asyncio`/`ruff` in dev extras with nothing to run.

#### F21 · Seven "Accepted" ADRs, zero lines of implementation
`aaif_wiki/{connectors,curator,exporters,workflows}/` are **empty** — no `__init__.py`, no
`agent.py`, no `config.py`, no `cli.py`. But `pyproject.toml` declares the entry point
`aaif-wiki = "aaif_wiki.cli:app"` and the README Quickstart instructs `uv run aaif-wiki ingest`,
which cannot work. `wiki/` and `raw/events/` are likewise empty.

The deeper issue is process, not tidiness: **seven ADRs marked "Accepted" before a single spike
validated any of them.** F1, F5 and F13 are all findings that a two-hour walking skeleton would
have surfaced immediately — the model id fails on the first API call, the compactor never fires,
and the Temporal dependency reveals its cost the moment you try to run in CI.

**Recommendation.** Demote ADR-002, -004, -005 to **Proposed** until a walking skeleton exercises
them end-to-end on **one** repo. Keep ADR-001 and ADR-003 as Accepted — format and event-sourcing
are load-bearing and correct in substance. Fix the README Quickstart or mark it aspirational; a
copy-pasteable block that cannot run is worse than no block.

#### F22 · `.gitignore` ignores `lib/`
A setuptools-era artifact. Harmless today, but it will silently swallow a legitimate `lib/`
directory later. Drop it, along with the other pre-`uv` entries (`develop-eggs/`, `.eggs/`,
`parts/`, `.installed.cfg`) since the build backend is hatchling. Also worth an inline comment
explaining that `raw/cache/` is ignored while `raw/events/` is committed — that asymmetry is
deliberate and load-bearing (F7) but currently unexplained.

#### F23 · Missing `okf_version` marker · #F24 · v0.1-style citations
Both covered in F6.

---

## 3. Recommended target architecture

Concretely, the shape this should take:

```
GitHub Actions (cron: bi-weekly)  ── or ──  local `uv run aaif-wiki`
                │
                ▼
   ADK 2.0 Workflow Runtime          ◄── ADR-002 rewritten; Temporal = optional backend
                │
     ┌──────────┼──────────┬──────────────┐
     ▼          ▼          ▼              ▼
   Scan      Curate     Validate       Export
  (repos    (Horizon   (deterministic,  (MCP · Gist · dist/graph.json)
  via org    recipe,     no LLM)              │
  API)       upstream)      │                 │
     │          │           │                 │
     ▼          ▼           ▼                 ▼
 raw/events  wiki/ on a   CI gate        published only if
 (pointers,   branch      blocks          status: stable
  not blobs)     │        merge          + verified by human
                 ▼
          Pull Request ──► human review ──► merge ──► verified[] + status: stable
```

Load-bearing changes vs. today: one orchestrator instead of two; a validation stage that needs no
LLM; a human gate before publication; MCP as a first-class Phase 1 output; pointers rather than
blobs in the event store.

---

## 4. Proposed ADR change list

| ADR | Action | Summary |
| :-- | :-- | :-- |
| ADR-001 | **Amend** | Full v0.2 vocabulary (`status`, `stale_after`, `verified`, source signals); reframe as "AAIF profile of OKF v0.2"; fix root-absolute links; footnote citations; add `okf_version` to bundle root; move `graph.json` out of `wiki/` |
| ADR-002 | **Supersede** | ADK 2.0 Workflow Runtime + GH Actions as default; Temporal behind an optional `Orchestrator` backend; keep the original as the record of why |
| ADR-003 | **Amend** | Pointers for git-reproducible sources, inline only for ephemeral; drop "deterministic"; non-destructive replay; tombstone events; derive cursor from event store, delete `.state.json` |
| ADR-004 | **Amend** → *Proposed* | Fix `maximum_attempts`, fix jitter naming, fix budget/compaction inversion, replace AST truncation with prose strategy, add token/USD/concept ceilings |
| ADR-005 | **Amend** → *Proposed* | Depend on upstream Horizon recipe, document only the delta; drop the vendor-neutrality claim; correct the model id; add thinking-budget config |
| ADR-006 | **Demote** | "Proposed (P2)" → "Considered"; keep the L0/L1/L2 mapping as authoring discipline, which is the durable half |
| ADR-007 | **Rescope** | "Privacy Boundary" → "Trust Boundary"; keep outbound leak-guard, add untrusted-input handling and an outbound link allowlist |
| **ADR-008** | **New** | Evaluation & Quality Gates — golden set, deterministic validators, CI enforcement |
| **ADR-009** | **New** | Human-in-the-Loop Publication Gate — PR flow, `status`/`verified` promotion, drafts never published |
| **ADR-010** | **New** | Project Positioning & Attribution — unofficial disclaimer, upstream licensing, donation path |
| `docs/design/README.md` | **Amend** | Replace "Vendor Neutrality" criterion with "Output Portability"; add "Human Accountability" and "Adversarial Input" as criteria |

Immediate non-ADR fixes: add `LICENSE`; correct `config.yaml:curator.model`; correct the WG count;
fix or caveat the README Quickstart; add a CI workflow running `ruff` + validators.

---

## 5. Question pack

Batched for a single async pass. Each carries a recommended default — **if you don't answer,
I'll proceed with the recommendation** and note the assumption in the relevant ADR.

**Q1 · Orchestration.** Is Temporal a *requirement* (you want it demonstrated) or a *means*
(you want durable runs)? → **Rec:** means. Move to ADK Workflow Runtime + GH Actions, keep
Temporal as an optional backend. If it's a requirement, say so in ADR-002's Context and I'll
leave it as the default but still cut the `--direct` second path.

**Q2 · Publication gate.** Should the curator open a PR for human review, or commit to `main`
directly? → **Rec:** PR + `status: draft` until a human `verified` entry lands; drafts never
reach the Gist.

**Q3 · Positioning.** Is this a personal project, a proposal you intend to donate to AAIF, or
something you have already discussed with the TC? → **Rec:** write it as unofficial-with-a-
donation-path (ADR-010) regardless; the disclaimer costs nothing and the donation path is
strictly upside.

**Q4 · Primary consumer.** Rank: MCP server / Gist digest / D3 visualizer / OpenViking.
→ **Rec:** MCP first (AAIF's own protocol, no vector store, works day one), Gist second,
visualizer third, OpenViking deferred.

**Q5 · Event store.** Pointers-to-git, or keep inlining `raw_text`? → **Rec:** pointers for
git-reproducible files, inline for PR comments / issues / notes.

**Q6 · Model & budget.** Confirm `gemini-flash-latest` on Vertex `global` with ADC, and give me
a per-run USD ceiling. → **Rec:** yes on the model; **$5/run** ceiling as a starting guess for
incremental, **$50** for bootstrap — correct me, these are unmeasured.

**Q7 · Ingest scope.** `include_open_prs: true` is what makes the "consensus" problem sharp.
Keep open PRs (status-tagged `draft`), or restrict Phase 1 to merged content only?
→ **Rec:** merged-only for Phase 1; add open PRs once the review gate from Q2 exists.

**Q8 · Sequencing.** Walking skeleton first (one repo, end-to-end, ADRs demoted to Proposed), or
finish the design pass first? → **Rec:** skeleton first. F1/F5/F13 are all things a two-hour
spike would have caught, which is the strongest available argument for the order.

---

## Appendix · Verification notes

External claims in the ADRs were checked rather than assumed. Recording the outcome so this
review is auditable and so the next reviewer doesn't repeat the work.

**Confirmed accurate:**
- **OKF v0.2** — real. `GoogleCloudPlatform/knowledge-catalog/okf/SPEC.md`. v0.1 published
  2026-06-12, v0.2 2026-07-24/25. Additive and backward-compatible. `type` remains the only
  required field; `title`/`description`/`resource`/`tags` recommended. v0.2 added `sources`
  (with `author`, `usage_count`, `last_modified`, `usage_window`), `generated`, `verified`,
  `status`, `stale_after`, the `Attested Computation` type, and the `# Computation` heading.
  `timestamp` → `generated.at`; body `# Citations` → frontmatter `sources`. Bundle-root marker
  is `okf_version` in `index.md`. **Typed relationships are an open proposal, not spec.**
- **`langchain-ai/openwiki`** — real. TypeScript CLI, ~14.2k stars, v0.3.3, built on DeepAgents,
  ships a GitHub Action for scheduled updates. Note it is **codebase-documentation-first**, which
  is the likely origin of the code-shaped assumptions in F16.
- **`volcengine/OpenViking`** — real. ByteDance. `viking://` URIs, L0 `.abstract.md` (~100 tokens)
  / L1 `.overview.md` (~2k) / L2 full, Python 3.10+, **includes its own MCP server**, benchmarked
  on LoCoMo and tau2-bench. ADR-006's characterization is fair.
- **`google/adk-samples` long-horizon-harness** — real, merged **August 2026**, i.e. days before
  this repo was created. See F10 on forking a moving target.
- **`google-adk` 2.5.0** — real (released 2026-07-16; latest 2.7.0). ADK **2.0** introduced the
  graph-based Workflow Runtime (routing, fan-out/fan-in, loops, retry, state, HITL, nested
  workflows) and the Task API, with breaking changes from 1.x. This is the basis of F1.
- **AAIF** — real, Linux Foundation. Projects: MCP, goose, AGENTS.MD, agentgateway.
  **7 working groups + 1 cross-group workstream** (see F19).

**Reviewer error — corrected:**
- **`gemini-3.7-flash` is REAL.** Gemini 3.7 Flash shipped **2026-08-13**, three weeks after
  3.6 Flash, at an introductory $0.75/1M input and $3.75/1M output; available in Vertex AI,
  Gemini Enterprise Agent Platform, AI Studio and the Gemini app. The config and ADRs were
  correct. This review initially claimed the opposite as an S1 finding — see the correction
  block in F5. **Root cause:** the verification query was scoped to "gemini 3 flash", which
  returned the December 2025 Gemini 3 Flash launch and never covered the 3.5/3.6/3.7 line;
  a null result was then treated as evidence of absence. **Lesson for the next reviewer:**
  when checking whether a fast-moving model/version exists, query the exact string, and treat
  "my search didn't find it" as inconclusive rather than falsifying — especially in a domain
  with a three-week release cadence.

**Confirmed wrong (in the repo, not in this review):**
- **"8 working groups"** — 7 WGs + 1 cross-group workstream. See F19.
- **`LICENSE`** — badged in README, file absent. See F20.

**Unverified — please confirm:**
- `google-agents-cli>=0.6.0` (dev extra) — could not confirm this package name.
- `openviking>=0.1.0` — project is at 0.3.22+; if the extra is kept, the floor looks stale.
