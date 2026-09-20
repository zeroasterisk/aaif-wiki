from __future__ import annotations

import subprocess
from pathlib import Path
from unittest.mock import MagicMock

from aaif_wiki import publish
from aaif_wiki.cli import _publish
from aaif_wiki.config import Config
from aaif_wiki.models import Concept, Mutation
from aaif_wiki.publish import commit_paths, open_pull_request


def test_push_branch_tracks_remote(monkeypatch, tmp_path):
    calls = []
    monkeypatch.setattr(publish, "_git", lambda root, *args: calls.append((root, args)) or "")
    publish.push_branch(tmp_path, "wiki/update-1")
    assert calls == [(tmp_path, ("push", "-u", "origin", "wiki/update-1"))]


def test_open_pull_request_pushes_before_gh_pr_create(tmp_path, monkeypatch):
    cfg = Config(root=tmp_path)
    commands_executed = []

    def fake_run(cmd, *args, **kwargs):
        commands_executed.append(cmd)
        mock_proc = MagicMock()
        mock_proc.returncode = 0
        mock_proc.stdout = "https://github.com/zeroasterisk/aaif-wiki/pull/42\n"
        mock_proc.stderr = ""
        return mock_proc

    monkeypatch.setattr(subprocess, "run", fake_run)
    ok, url = open_pull_request(cfg, "wiki/update-123", "title", "body")

    assert ok is True
    assert "https://github.com/zeroasterisk/aaif-wiki/pull/42" in url
    # Verify push was executed BEFORE gh pr create
    assert len(commands_executed) >= 3
    # First is auth check
    assert commands_executed[0] == ["gh", "auth", "status"]
    # Second MUST be git push
    assert commands_executed[1] == ["git", "-C", str(tmp_path), "push", "-u", "origin", "wiki/update-123"]
    # Third is gh pr create
    assert commands_executed[2][:3] == ["gh", "pr", "create"]


def test_open_pull_request_fails_if_git_push_fails(tmp_path, monkeypatch):
    cfg = Config(root=tmp_path)

    def fake_run(cmd, *args, **kwargs):
        mock_proc = MagicMock()
        if cmd == ["gh", "auth", "status"]:
            mock_proc.returncode = 0
        elif "push" in cmd:
            mock_proc.returncode = 1
            mock_proc.stderr = "fatal: remote rejected"
        else:
            mock_proc.returncode = 0
            mock_proc.stdout = "url"
        return mock_proc

    monkeypatch.setattr(subprocess, "run", fake_run)
    ok, err = open_pull_request(cfg, "wiki/update-123", "title", "body")

    assert ok is False
    assert "git push failed" in err


def test_open_pull_request_auto_merge_fallback_on_clean_status(tmp_path, monkeypatch):
    cfg = Config(root=tmp_path)
    cfg.publish.auto_merge = True

    commands = []

    def fake_run(cmd, *args, **kwargs):
        commands.append(cmd)
        mock_proc = MagicMock()
        if cmd[:3] == ["gh", "pr", "merge"] and "--auto" in cmd:
            mock_proc.returncode = 1
            mock_proc.stderr = "Pull request is in clean status"
        else:
            mock_proc.returncode = 0
            mock_proc.stdout = "https://github.com/zeroasterisk/aaif-wiki/pull/42\n"
            mock_proc.stderr = ""
        return mock_proc

    monkeypatch.setattr(subprocess, "run", fake_run)
    ok, url = open_pull_request(cfg, "wiki/update-123", "title", "body")

    assert ok is True
    # Verify fallback direct squash merge was attempted
    assert any(cmd[:3] == ["gh", "pr", "merge"] and "--squash" in cmd and "--auto" not in cmd for cmd in commands)


def test_commit_paths_tolerates_missing_and_empty_directories(tmp_path):
    # Only "wiki" exists, "raw/exceptions" and "raw/reviews" do not exist
    (tmp_path / "wiki").mkdir(parents=True)
    (tmp_path / "wiki" / "term.md").write_text("# Test")

    # Should not raise exception
    paths = ["wiki", "raw/exceptions", "nonexistent"]
    # In a git repo
    subprocess.run(["git", "init", "-b", "main"], cwd=str(tmp_path), capture_output=True)
    subprocess.run(["git", "config", "user.name", "tester"], cwd=str(tmp_path), capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@test.com"], cwd=str(tmp_path), capture_output=True)

    sha = commit_paths(tmp_path, paths, "test commit")
    assert sha is not None


def test_publish_stages_bundle_reviews_and_exceptions(tmp_path, monkeypatch):
    cfg = Config(root=tmp_path)
    cfg.project.bundle_root = "wiki"
    cfg.publish.review_records = "raw/reviews"
    cfg.resolution.exceptions_dir = "raw/exceptions"

    staged_paths = []

    monkeypatch.setattr("aaif_wiki.publish.current_branch", lambda root: "main")
    monkeypatch.setattr("aaif_wiki.publish.create_branch", lambda root, branch: branch)
    monkeypatch.setattr(
        "aaif_wiki.publish.write_review_record",
        lambda cfg, mutations, branch, run_id: Path("record.json"),
    )
    def fake_commit_paths(root, paths, message):
        staged_paths.extend(paths)
        return "c0ffee12345"

    monkeypatch.setattr("aaif_wiki.publish.commit_paths", fake_commit_paths)
    monkeypatch.setattr(
        "aaif_wiki.publish.open_pull_request",
        lambda cfg, branch, title, body: (True, "https://github.com/pr/1"),
    )
    monkeypatch.setattr("aaif_wiki.publish._git", lambda *args, **kwargs: "")

    mut = Mutation(action="create", slug="taxonomy/x", concept=Concept(type="Term", title="x", description="x"))
    _publish(cfg, [mut], "run-test", {})

    assert "wiki" in staged_paths
    assert "raw/reviews" in staged_paths
    assert "raw/exceptions" in staged_paths


def test_weekly_workflow_uses_project_variable():
    workflow = Path(".github/workflows/weekly-refresh.yml").read_text()
    assert "${{ vars.GOOGLE_CLOUD_PROJECT }}" in workflow
    assert "GOOGLE_CLOUD_PROJECT: alanblount-demo" not in workflow
