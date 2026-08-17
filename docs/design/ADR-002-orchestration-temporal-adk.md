# ADR-002: Orchestration via a Pluggable `Orchestrator` Protocol (Local Default, Temporal Optional)

## Status
**Accepted** — supersedes the original Temporal-first decision recorded in the first revision of this ADR.

## Context
The first revision of ADR-002 made **Temporal a runtime prerequisite**: no Temporal dev server, no
pipeline. The 2026-08 architecture review (F1) found that this stacks three orchestration layers on
a single-operator batch job — Temporal workflows, the ADK 2.x graph-based Workflow Runtime (routing,
fan-out/fan-in, loops, retry, state management, human-in-the-loop, nested workflows), and the
harness loop of ADR-005 — where only one is needed to ship.

The counter-pressure is real and is the reason this ADR is not simply "drop Temporal":

- The pipeline is long-running, hits three flaky external systems (git, the GitHub REST API, an LLM
  endpoint), and is expensive to redo from scratch.
- The project owner trusts Temporal's resilience story and is only *partially* convinced by
  in-main-process durability. If flakiness shows up that cannot be resolved locally, he wants to
  switch to Temporal **without a rewrite**.

So the decision is not "which orchestrator" but "how do we make the orchestrator a swappable
detail?"

### Why Temporal was originally chosen (recorded so the history is not lost)
| Original driver | Still true? |
| :--- | :--- |
| Crash mid-run must not lose completed work | Yes — now served by checkpoint + event store (ADR-003) |
| Explicit per-activity retry policy at the network boundary | Yes — now a property of the activity registry, not the engine |
| Observability into every attempt, duration, and error | **Partially** — local mode has structured logs, not a UI |
| Distributed / multi-worker execution | Not needed today; single operator, single machine |
| Rate-limit backoff without blocking the process | Yes — but `asyncio.sleep` is sufficient at this scale |

Temporal was the right answer to the right questions. It is now optional because the same questions
have cheaper answers at a one-machine scale — not because the questions went away.

## Decision
We define an **`Orchestrator` protocol** with two implementations, and we constrain activity
authoring so that **every activity is Temporal-compatible by construction**.

```
                    ┌────────────────────────────────────────────────┐
                    │        Activity Registry (single source)       │
                    │  name → (fn, InputModel, OutputModel, Retry)   │
                    └───────────────────────┬────────────────────────┘
                                            │  same registry, both paths
                        ┌───────────────────┴───────────────────┐
                        ▼                                       ▼
        ┌────────────────────────────────┐      ┌────────────────────────────────┐
        │      LocalOrchestrator         │      │     TemporalOrchestrator       │
        │  (default; in-process)         │      │  (opt-in; config switch)       │
        ├────────────────────────────────┤      ├────────────────────────────────┤
        │ • asyncio sequencing           │      │ • @activity.defn wrappers      │
        │ • retry from registry policy   │      │ • RetryPolicy from registry    │
        │ • run checkpoint file          │      │ • Temporal event history       │
        │ • replay-safe via event store  │      │ • Web UI at :8233              │
        └────────────────────────────────┘      └────────────────────────────────┘
```

### 1. The activity contract (the load-bearing part of this ADR)
Every activity MUST satisfy all of the following. These are lint-enforced, not conventions:

1. Signature is exactly `async def activity(inp: SomeInput) -> SomeOutput`, where both types are
   Pydantic models — one argument in, one value out.
2. Input and output are **JSON-serializable**. No file handles, no live clients, no `Path` objects
   that assume a particular machine, no generators.
3. **No closures and no hidden state.** Clients (git, GitHub, LLM) are constructed from config
   inside the activity or resolved from a module-level factory — never captured from an enclosing
   scope.
4. Registered in `aaif_wiki/activities/registry.py` with an **explicit per-activity retry policy**
   (attempt count, initial interval, backoff coefficient, maximum interval, non-retryable error
   types). Attempt counts reference `config.yaml:temporal.retry_policy` rather than restating
   literals (see ADR-004).
5. Idempotent with respect to the event store: re-running a completed activity with the same input
   must produce the same *effect*, not necessarily the same *bytes* (LLM steps are re-derivable,
   not bit-identical — see ADR-003).

If an activity satisfies this contract, wrapping it in `@activity.defn` is mechanical. That is the
entire point.

### 2. `LocalOrchestrator` (default)
- Runs the pipeline in-process with `asyncio`, sequencing activities from the registry.
- Applies the registry's retry policy directly (full-jitter backoff, ADR-004 §2).
- Durability comes from **two** places:
  - a **run checkpoint file** (`raw/.runs/<run_id>/checkpoint.json`) recording, per activity,
    `{status, input_hash, output_ref, attempts, finished_at}`;
  - the **immutable event store** (ADR-003), which holds the actual ingested material.
- On restart, the orchestrator reloads the checkpoint, skips activities already marked `complete`
  with a matching input hash, and resumes at the first incomplete step. A crash at concept #180 of
  #200 does not re-ingest, re-summarize, or re-pay for #1–179.
- The checkpoint is a **derived, gitignored** artifact. Deleting it costs a re-run, never data.

### 3. `TemporalOrchestrator` (opt-in)
- Reads the **same registry**, emits `@activity.defn` wrappers and a workflow that sequences them,
  and maps each registry retry policy onto `temporal.common.RetryPolicy`.
- **No activity source changes.** The delta is a worker entrypoint and a config flag.
- Enabled with `orchestrator: temporal` plus `temporal.host` / `namespace` / `task_queue` in
  `config.yaml`.

### 4. Where ADK sits
ADK is the **agent execution framework inside an activity** (ADR-005), not a competing orchestrator.
The curation activity invokes an ADK agent; the orchestrator does not know or care. We do not use
ADK's Workflow Runtime for top-level pipeline sequencing, because the orchestrator boundary must
stay swappable and framework-independent.

### 5. Switching cost
```yaml
orchestrator: local        # or: temporal
```
Switch criteria, stated in advance so the decision is not made in a panic: move to Temporal if we
observe (a) repeated multi-hour runs failing in ways the checkpoint cannot resume, (b) a need to run
workers on more than one machine, or (c) a need for external run visibility by someone who is not at
the terminal.

## Consequences

### Positive
* **One orchestration layer, not three.** The default path has no daemon, no container, no ports —
  `uv run aaif-wiki run` and it goes. This is what makes the project contributable by someone who
  just cloned it.
* **Temporal stays a config change.** The activity contract is the insurance policy; it is paid for
  up front and continuously, by lint, rather than discovered to be unpaid at migration time.
* **Testability improves as a side effect.** Pure `async def (Pydantic) -> Pydantic` activities are
  directly unit-testable with no orchestrator at all, which is also what makes the golden-set
  regression suite in ADR-008 possible.
* **Checkpoint + event store separation is honest.** The expensive, irreplaceable thing (ingested
  events) is durable and versioned; the cheap thing (run progress) is disposable.

### Negative / Trade-offs
* **Local durability is genuinely weaker than Temporal's.** Naming exactly what is given up:
  - **No distributed guarantees.** Checkpoint writes are local file writes. A crash between
    "activity completed" and "checkpoint fsynced" re-runs that one activity. Temporal's event
    history closes that window; a file does not.
  - **No external visibility.** There is no Web UI, no query API, no "show me the state of the run
    from another terminal." Local mode gives structured logs and a JSON checkpoint you can `cat`.
  - **No timers, signals, or human-in-the-loop waits inside the run.** The publication gate
    (ADR-009) is deliberately *outside* the workflow, as a Pull Request, partly because local mode
    cannot durably park a workflow for days waiting on a human.
  - **No heartbeating or worker-failure detection.** If the process is `SIGKILL`ed, nothing notices
    until a human re-runs.
  - **No multi-worker parallelism or task-queue backpressure.** Concurrency is whatever `asyncio`
    plus our own semaphores provide, in one process.
* **The contract costs authoring freedom.** No convenient closures, no passing a live client into an
  activity, no returning a non-serializable handle. Contributors will hit the linter.
* **Two code paths, one of which is under-exercised.** `TemporalOrchestrator` will rot unless CI
  runs at least a smoke test against `temporal server start-dev`. That smoke test is a required
  deliverable of this ADR, not a nice-to-have.
