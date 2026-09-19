from pathlib import Path

from aaif_wiki import publish


def test_push_branch_tracks_remote(monkeypatch, tmp_path):
    calls = []
    monkeypatch.setattr(publish, "_git", lambda root, *args: calls.append((root, args)) or "")
    publish.push_branch(tmp_path, "wiki/update-1")
    assert calls == [(tmp_path, ("push", "-u", "origin", "wiki/update-1"))]


def test_weekly_workflow_uses_project_variable():
    workflow = Path(".github/workflows/weekly-refresh.yml").read_text()
    assert "${{ vars.GOOGLE_CLOUD_PROJECT }}" in workflow
    assert "GOOGLE_CLOUD_PROJECT: alanblount-demo" not in workflow
