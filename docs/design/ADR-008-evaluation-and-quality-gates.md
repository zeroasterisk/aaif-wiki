# ADR-008: Evaluation, Golden Sets & Deterministic Quality Gates

## Status
**Proposed** — the gate design is settled; the golden set does not exist yet because no real run has
produced concepts to freeze.

## Context
Every other ADR in this set describes how the pipeline produces knowledge. None of them describe how
we know the output is any good, and "the model seemed to do a reasonable job" is not a quality bar
for a corpus intended for donation (ADR-010).

Two distinct problems, which need two distinct mechanisms:

1. **Regression.** A prompt tweak, a model bump (the Flash line moves roughly every three weeks —
   ADR-005 §D5), or a schema change silently degrades output. Replay (ADR-003 §8) proves the inputs
   were preserved; it says nothing about whether the outputs got worse. And because LLM output is
   **re-derivable, not bit-identical**, a naive `diff` of generated prose reports noise on every run
   and is therefore useless as a gate.
2. **Correctness of form.** Broken links, `sources[]` entries pointing at event ids that do not
   exist, orphan pages nothing links to, frontmatter that violates the OKF profile. These are not
   judgement calls — they are mechanically checkable, and they are the failures a reader notices
   first.

Problem 2 must never require an LLM to detect. Problem 1 must tolerate non-determinism without
becoming meaningless.

## Decision
Two layers. The deterministic layer blocks merge; the golden set informs the human reviewing the PR.

```
   ┌──────────────────────────────────────────────────────────────────────────┐
   │ Layer 2 · GOLDEN-SET REGRESSION            (advisory; runs on PR)        │
   │   frozen input events → expected mutations → structural diff             │
   │   surfaces "what changed and why" for a human. Does not block.           │
   └──────────────────────────────────────────────────────────────────────────┘
   ┌──────────────────────────────────────────────────────────────────────────┐
   │ Layer 1 · DETERMINISTIC VALIDATORS         (BLOCKING; runs in CI)        │
   │   no LLM · no network · no judgement · pass/fail                         │
   │   V1 schema  V2 links  V3 provenance  V4 orphans  V5 OKF conformance     │
   │   V6 status discipline   V7 tier discipline                              │
   └──────────────────────────────────────────────────────────────────────────┘
                                    ▲
                                    │ correction pairs harvested from
   ┌──────────────────────────────────────────────────────────────────────────┐
   │ ADR-009 PR review records  —  human edits to machine output              │
   │ feed new golden cases and new validator rules                            │
   └──────────────────────────────────────────────────────────────────────────┘
```

### Layer 1 · Deterministic validators (blocking)
`aaif-wiki validate` runs in CI on every pull request, including the curator's own publication PRs
(ADR-009). No LLM, no network, no non-determinism. **A failure blocks merge.** Each validator
reports file, line, and the offending value — not a summary count.

| ID | Validator | Rule |
| :--- | :--- | :--- |
| **V1** | Frontmatter schema conformance | Every page parses as YAML frontmatter + Markdown body, and validates against the project's Pydantic OKF **profile** model. Unknown fields are reported, not silently accepted. |
| **V2** | Internal links resolve | Every relative markdown link (and image, and reference definition) resolves to a file that exists in the bundle. **Root-absolute links (`/architectures/x.md`) are a hard failure** — they break on GitHub Pages project sub-paths and in Obsidian (ADR-001). |
| **V3** | Provenance integrity | Every `sources[]` entry maps to a real `event_id` present in `raw/events/`. Every concept has at least one source. Every footnote reference in the body (e.g. `[^evt-spaa-pr11]`) has a matching definition and a matching `sources[]` id. |
| **V4** | No orphan concepts | Every page except the bundle root `index.md` has at least one inbound relative link from another page. Unreachable pages are content nobody will ever find. |
| **V5** | OKF v0.2 conformance | `type` present on every concept (the **only** field OKF v0.2 actually requires). `generated: {by, at}` present and well-formed. No v0.1-style `timestamp` field (superseded by `generated.at`). No body `# Citations` list (superseded by frontmatter `sources`). Bundle root `index.md` carries `okf_version: "0.2"`. `stale_after`, where present, is an absolute date, not a duration. `Attested Computation` concepts carry the runtime/parameters/computation/executor/attester keys and a `# Computation` heading. **Producer extensions must be namespaced** — any non-spec field, including any typed-edge field, must carry the project prefix, because OKF v0.2 has no typed-relationship field and an unprefixed one would misrepresent the spec. |
| **V6** | Status discipline | Any concept whose `sources[]` contains a non-`merged` event carries `status: draft` (ADR-003 §5). No machine-generated concept carries a `verified` entry (ADR-007 §1.3 — `verified` is not in the mutation schema, so a hit here means something bypassed the applier). Every `verified` entry has a well-formed actor and ISO-8601 `at`. |
| **V7** | Tier discipline | Frontmatter `description` is exactly one line and a complete sentence. Exactly one H1. No skipped heading levels. `# Overview`'s first paragraph is self-contained (ADR-006). |

Plus the outbound gates from ADR-007, which run at export rather than at validate: the leak-guard
regex audit and the link allowlist.

### Layer 2 · Golden-set regression (advisory)
A golden case is `(frozen input events, expected output)` committed under `tests/golden/<case>/`:

```
tests/golden/attested-isolated-runtime/
├── events/          # frozen RawEvent JSON — pointer events with vendored blob text
├── expected/        # expected ConceptMutation objects (NOT expected prose)
└── case.yaml        # model pin, prompt revision, why this case exists
```

**We diff mutations, not prose.** ADR-005 §D2 makes the curator emit structured `ConceptMutation`
objects rather than free-form files, and that is what makes regression testing possible at all. A
mutation diff is meaningful:

- **Hard signals (a real regression, reported as such):** a `sources[]` entry disappeared or points
  somewhere new; `status` flipped from `draft` to `stable`; a link target changed; a required profile
  field went missing; a concept id changed; a `verified` entry appeared.
- **Soft signals (reported, never failed):** prose wording changed, section ordering changed,
  description rephrased. These are expected — the model is not deterministic and pretending
  otherwise produces a suite everyone learns to ignore.

Golden cases pin the model id and prompt revision in `case.yaml`, so a diff is always attributable:
model bump, prompt change, or genuine logic regression. Running the suite costs LLM calls, so it runs
on prompt/model/schema-touching PRs rather than on every commit, and its spend is drawn from the
ADR-004 ceilings like any other run.

The golden set is **advisory**. It informs the human reviewing the PR; it does not block merge. A
blocking gate whose failures are half noise gets bypassed within a month, and then it protects
nothing.

### Feeding the loop from ADR-009
The structured review records produced by the publication gate (ADR-009) are the intended source of
new test cases. When a human edits a machine-generated concept during review, that edit is a labelled
correction pair — `(input events, machine output, human-corrected output)`. Harvesting is a
deliberate act, not automatic:

1. `aaif-wiki evals harvest` lists correction pairs from merged review records.
2. A human triages each: is this a **recurring class** (→ new golden case, or better, a new
   deterministic validator) or a **one-off** (→ ignore)?
3. Corrections that can be expressed as a mechanical rule are **promoted out of the golden set into
   Layer 1**. That is the preferred outcome every time: a deterministic validator is free, fast,
   unambiguous, and blocking, where a golden case costs tokens and only advises.

### CI wiring
| Trigger | Runs | Blocking |
| :--- | :--- | :--- |
| Every PR, every push | Layer 1 validators, unit tests, config-invariant checks (ADR-004 §3) | **Yes** |
| PR touching prompts, model pin, or mutation schema | Layer 2 golden set | No — posts a diff comment |
| Curator publication PR (ADR-009) | Layer 1 + export guards (ADR-007 §2, §3) | **Yes** |
| Nightly | Layer 1 against the full bundle, to catch drift from upstream tombstones | **Yes** (opens an issue) |

## Consequences

### Positive
* **The failures readers actually hit are caught mechanically** — broken links, dangling provenance,
  orphan pages, malformed frontmatter — with no model, no cost, and no ambiguity.
* **Non-determinism is handled honestly.** Diffing structured mutations with an explicit
  hard/soft signal split gives a suite that stays useful instead of one that cries wolf.
* **`verified` forgery is detectable.** V6 is a tripwire on the ADR-007 structural control.
* **The review corpus becomes an asset.** Human corrections flow back as validators and golden
  cases, so the same mistake is caught for free the second time.
* **Donation readiness is measurable.** "Passes V1–V7 and conforms to OKF v0.2" is a claim AAIF can
  verify themselves by running the validators (ADR-010).

### Negative / Trade-offs
* **No golden set exists yet.** Layer 2 is a plan until a real run produces output worth freezing;
  this is why the status is Proposed.
* **Golden cases cost money and go stale.** Each run is LLM spend, and every model bump produces a
  wave of soft-signal diffs a human has to read past to find the hard ones.
* **Advisory gates get ignored.** We accept this risk deliberately in exchange for not building a
  blocking gate that people route around. Mitigation is the promotion path: anything important
  enough to block on becomes a Layer 1 validator.
* **V4 (orphans) will produce false positives** for pages that are legitimately new and not yet
  linked. Requires either an allowlist or accepting that the curator must add an index entry in the
  same mutation — we choose the latter, which is one more constraint on the mutation schema.
* **Layer 1 cannot check whether the content is true.** It checks form, provenance, and internal
  consistency. Semantic accuracy is the human reviewer's job (ADR-009), and no validator here should
  be read as evidence otherwise.
