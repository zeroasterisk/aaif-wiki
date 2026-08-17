"""Command line interface."""

from __future__ import annotations

import asyncio
import json
import logging
from datetime import UTC, datetime
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from . import __version__
from .config import get_config
from .models import RunMode

app = typer.Typer(
    name="aaif-wiki",
    help="Autonomous OKF v0.2 knowledge engine for the Agentic AI Foundation (unofficial).",
    no_args_is_help=True,
    add_completion=False,
)
console = Console()


def _setup_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.INFO if verbose else logging.WARNING,
        format="%(levelname)-7s %(name)s: %(message)s",
    )


def _make_orchestrator(run_id: str, resume: bool = True):
    from .orchestration import get_orchestrator

    cfg = get_config()
    backend = cfg.orchestrator.backend
    if backend == "local":
        return get_orchestrator(
            "local",
            checkpoint_path=cfg.root / cfg.orchestrator.checkpoint_path,
            run_id=run_id,
            resume=resume,
        )
    return get_orchestrator(
        "temporal",
        host=cfg.orchestrator.host,
        namespace=cfg.orchestrator.namespace,
        task_queue=cfg.orchestrator.task_queue,
    )


@app.command()
def version() -> None:
    """Show version and resolved configuration."""
    cfg = get_config()
    console.print(f"[bold]aaif-wiki[/bold] {__version__}")
    console.print(f"  orchestrator : {cfg.orchestrator.backend}")
    console.print(f"  model        : {cfg.curator.model} (fallback: {cfg.curator.fallback_model})")
    console.print(f"  vertex       : {cfg.curator.vertex.resolved_project()} @ {cfg.curator.vertex.location}")
    console.print(f"  bundle       : {cfg.bundle_dir}")
    console.print(f"  events       : {cfg.events_dir}")
    console.print(f"  budget       : ${cfg.budget.max_usd_per_run}/run (hard cap ${cfg.budget.hard_usd_ceiling})")


@app.command()
def doctor() -> None:
    """Check that everything this tool depends on is actually reachable."""
    import shutil
    import subprocess

    cfg = get_config()
    table = Table("check", "status", "detail")

    table.add_row("git", "ok" if shutil.which("git") else "MISSING", shutil.which("git") or "")

    gh = shutil.which("gh")
    if gh:
        auth = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
        table.add_row("gh auth", "ok" if auth.returncode == 0 else "NOT LOGGED IN",
                      "PR creation needs this" if auth.returncode else "")
    else:
        table.add_row("gh", "MISSING", "PR creation will emit manual instructions")

    try:
        from .connectors import GitHubConnector

        conn = GitHubConnector(cfg.sources.github, cfg.cache_dir)
        rl = conn.rate_limit()
        note = "authenticated" if cfg.sources.github.token() else "unauthenticated (60/hr)"
        table.add_row("github api", "ok", f"{rl['remaining']}/{rl['limit']} remaining, {note}")
    except Exception as exc:  # noqa: BLE001
        table.add_row("github api", "FAIL", str(exc)[:60])

    project = cfg.curator.vertex.resolved_project()
    if not project:
        table.add_row("vertex", "NO PROJECT", "set GOOGLE_CLOUD_PROJECT or curator.vertex.project")
    else:
        try:
            from .vertex_compat import prepare_environment

            applied = prepare_environment()
            if applied:
                table.add_row("vertex compat", "applied", f"set {', '.join(applied)} (mTLS opt-out)")
            from google import genai

            client = genai.Client(vertexai=True, project=project, location=cfg.curator.vertex.location)
            resp = client.models.generate_content(model=cfg.curator.model, contents="say OK")
            table.add_row("vertex", "ok", f"{cfg.curator.model} -> {(resp.text or '').strip()[:20]}")
        except Exception as exc:  # noqa: BLE001
            table.add_row("vertex", "FAIL", str(exc)[:70])

    try:
        import temporalio  # noqa: F401

        table.add_row("temporal", "installed", "backend available")
    except ImportError:
        table.add_row("temporal", "not installed", "optional: uv sync --extra temporal")

    try:
        import mcp  # noqa: F401

        table.add_row("mcp", "installed", "okf mcp server available")
    except ImportError:
        table.add_row("mcp", "not installed", "optional: uv sync --extra mcp")

    console.print(table)


@app.command()
def ingest(
    mode: str = typer.Option("incremental", help="bootstrap | incremental | replay"),
    repo: list[str] = typer.Option(None, "--repo", help="Limit to specific repos (repeatable)"),
    max_events: int = typer.Option(0, help="Cap events this run (0 = unbounded)"),
    no_curate: bool = typer.Option(False, "--no-curate", help="Ingest only; skip the LLM"),
    batch_size: int = typer.Option(6, help="Events per curation call"),
    fresh: bool = typer.Option(False, "--fresh", help="Ignore the resume checkpoint"),
    publish: bool = typer.Option(False, "--publish", help="Commit to a branch and open a PR"),
    verbose: bool = typer.Option(False, "-v", "--verbose"),
) -> None:
    """Scan sources, curate concepts, apply and validate."""
    _setup_logging(verbose)
    cfg = get_config()
    from . import pipeline  # noqa: F401  (registers activities)
    from .pipeline import run_pipeline

    run_id = datetime.now(UTC).strftime("%Y%m%dT%H%M%S")
    orch = _make_orchestrator(run_id, resume=not fresh)

    console.print(f"[bold]run {run_id}[/bold] mode={mode} backend={orch.backend}")
    summary = asyncio.run(
        run_pipeline(
            orch,
            mode=RunMode(mode),
            repos=list(repo) if repo else None,
            max_events=max_events,
            batch_size=batch_size,
            curate=not no_curate,
        )
    )

    mutations = summary.pop("_mutations", [])
    _print_summary(summary)

    if publish and mutations:
        _publish(cfg, mutations, run_id, summary)


def _print_summary(summary: dict) -> None:
    table = Table("metric", "value")
    table.add_row("repos scanned", str(len(summary.get("repos_scanned", []))))
    table.add_row("new events", str(summary.get("new_events", 0)))
    table.add_row("pending curation", str(summary.get("pending_curation", 0)))
    table.add_row("mutations", str(summary.get("mutations", 0)))
    table.add_row("applied", str(summary.get("applied", 0)))
    table.add_row("tokens", f"{summary.get('tokens', 0):,}")
    table.add_row("cost", f"${summary.get('usd', 0.0):.4f}")
    table.add_row("model", summary.get("model", "") or "-")
    console.print(table)

    if summary.get("skipped"):
        console.print(f"[yellow]skipped repos:[/yellow] {', '.join(summary['skipped'])}")
    if summary.get("halted"):
        console.print(f"[yellow]halted:[/yellow] {summary['halted']}")

    issues = summary.get("issues", [])
    errors = [i for i in issues if i["severity"] == "error"]
    warnings = [i for i in issues if i["severity"] == "warning"]
    if errors:
        console.print(f"\n[red]{len(errors)} validation error(s)[/red]")
        for i in errors[:15]:
            console.print(f"  [red]x[/red] {i['path']}: [{i['check']}] {i['message']}")
    if warnings:
        console.print(f"[yellow]{len(warnings)} warning(s)[/yellow]")
        for i in warnings[:8]:
            console.print(f"  [yellow]![/yellow] {i['path']}: [{i['check']}] {i['message']}")
    if not issues:
        console.print("[green]validation clean[/green]")


def _publish(cfg, mutations, run_id: str, summary: dict) -> None:
    from . import publish as pub

    branch = f"{cfg.publish.branch_prefix}-{run_id}"
    original = pub.current_branch(cfg.root)
    try:
        pub.create_branch(cfg.root, branch)
        record = pub.write_review_record(cfg, mutations, branch, run_id)
        sha = pub.commit_paths(
            cfg.root,
            [cfg.project.bundle_root, cfg.publish.review_records],
            f"feat(wiki): automated update {run_id}\n\n{len(mutations)} mutation(s). "
            f"All concepts are draft/unverified pending human review (ADR-009).",
        )
        if not sha:
            console.print("[yellow]no changes to commit[/yellow]")
            pub._git(cfg.root, "checkout", original)
            return
        console.print(f"committed {sha[:8]} on [bold]{branch}[/bold] (review record: {record.name})")

        ok, detail = pub.open_pull_request(
            cfg, branch,
            f"wiki: automated update {run_id}",
            pub.pr_body(mutations, run_id, summary),
        )
        console.print(f"[green]PR: {detail}[/green]" if ok else f"[yellow]{detail}[/yellow]")
    except Exception as exc:  # noqa: BLE001
        console.print(f"[red]publish failed:[/red] {exc}")


@app.command()
def validate() -> None:
    """Run the deterministic (LLM-free) validators. Exit 1 on error."""
    cfg = get_config()
    from .store import EventStore
    from .validate import validate_bundle

    store = EventStore(cfg.events_dir)
    known = {e.event_id for e in store.iter_events()}
    result = validate_bundle(
        cfg.bundle_dir,
        known_event_ids=known,
        link_allowlist=cfg.trust.link_allowlist,
        forbidden_patterns=cfg.trust.forbidden_patterns,
    )
    console.print(f"checked {result.checked} concept(s)")
    for issue in result.issues:
        colour = "red" if issue.severity == "error" else "yellow"
        console.print(f"  [{colour}]{issue.severity}[/{colour}] {issue.path}: [{issue.check}] {issue.message}")
    if result.ok:
        console.print("[green]OK[/green]")
    raise typer.Exit(0 if result.ok else 1)


@app.command()
def export(
    target: str = typer.Argument("graph", help="graph | digest"),
) -> None:
    """Export a projection of the bundle into dist/."""
    cfg = get_config()
    if target == "graph":
        from .exporters.graph import GraphExporter

        result = GraphExporter(cfg).export()
    elif target == "digest":
        from .exporters.gist import GistExporter

        result = GistExporter(cfg).export()
    else:
        console.print(f"[red]unknown target: {target}[/red]")
        raise typer.Exit(2)

    console.print(("[green]ok[/green] " if result.ok else "[red]blocked[/red] ") + result.message)
    for path in result.artifacts:
        console.print(f"  -> {path}")
    for blocked in result.blocked:
        console.print(f"  [red]blocked:[/red] {blocked}")
    raise typer.Exit(0 if result.ok else 1)


@app.command()
def events(
    limit: int = typer.Option(20),
    repository: str = typer.Option("", "--repo"),
    lifecycle: str = typer.Option("", help="merged | open | draft | closed"),
) -> None:
    """Inspect the event store."""
    cfg = get_config()
    from .models import Lifecycle
    from .store import EventIndex, EventStore

    store = EventStore(cfg.events_dir)
    stats = store.stats()
    console.print(f"[bold]{stats['total']}[/bold] events across {len(stats['repositories'])} repos")
    console.print(f"  by lifecycle: {stats['by_lifecycle']}")
    console.print(f"  by type     : {stats['by_source_type']}")

    with EventIndex(cfg.index_db_path) as index:
        if index.count() == 0:
            index.rebuild(store.iter_events())
        rows = index.query(
            repository=repository or None,
            lifecycle=Lifecycle(lifecycle) if lifecycle else None,
            limit=limit,
        )
    table = Table("event_id", "lifecycle", "repo", "ref", "title")
    for row in rows:
        table.add_row(
            row["event_id"][:34], row["lifecycle"],
            row["repository"].split("/")[-1], row["reference_id"][:24], row["title"][:44],
        )
    console.print(table)


@app.command("index")
def index_cmd(rebuild: bool = typer.Option(False, "--rebuild")) -> None:
    """Rebuild the derived SQLite index from the event store."""
    cfg = get_config()
    from .store import EventIndex, EventStore

    store = EventStore(cfg.events_dir)
    with EventIndex(cfg.index_db_path) as index:
        if rebuild:
            n = index.rebuild(store.iter_events())
            console.print(f"[green]rebuilt[/green] {n} events -> {cfg.index_db_path}")
        else:
            console.print(f"{index.count()} events indexed at {cfg.index_db_path}")


@app.command()
def cursor() -> None:
    """Show the incremental cursor, derived from the event store (no state file)."""
    cfg = get_config()
    from .store import EventStore

    data = EventStore(cfg.events_dir).cursor()
    console.print(json.dumps(data, indent=2) if data else "no events ingested yet")


@app.command()
def mcp(
    bundle: Path = typer.Option(None, help="OKF bundle directory (defaults to configured bundle)"),
) -> None:
    """Serve any OKF v0.2 bundle over MCP."""
    cfg = get_config()
    bundle_dir = bundle or cfg.bundle_dir
    try:
        from .exporters.mcp_server import build_server
    except ImportError:
        console.print("[red]mcp extra not installed:[/red] uv sync --extra mcp")
        raise typer.Exit(1) from None
    console.print(f"serving OKF bundle: {bundle_dir}")
    build_server(bundle_dir).run()


@app.command()
def worker() -> None:
    """Run a Temporal worker (requires the temporal extra)."""
    cfg = get_config()
    from . import pipeline  # noqa: F401  (registers activities)

    try:
        from .orchestration.temporal import run_worker
    except ImportError:
        console.print("[red]temporal extra not installed:[/red] uv sync --extra temporal")
        raise typer.Exit(1) from None
    console.print(f"worker on {cfg.orchestrator.host} queue={cfg.orchestrator.task_queue}")
    asyncio.run(
        run_worker(
            host=cfg.orchestrator.host,
            namespace=cfg.orchestrator.namespace,
            task_queue=cfg.orchestrator.task_queue,
        )
    )


@app.command()
def activities() -> None:
    """List registered activities and their retry policies."""
    from . import pipeline  # noqa: F401
    from .orchestration.base import REGISTRY

    table = Table("activity", "input", "output", "attempts")
    for name in REGISTRY.names():
        act = REGISTRY.get(name)
        table.add_row(name, act.input_type.__name__, act.output_type.__name__, str(act.retry.maximum_attempts))
    console.print(table)


if __name__ == "__main__":
    app()
