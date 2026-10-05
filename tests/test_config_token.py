from aaif_wiki.config import GitHubCfg


def test_sources_token_takes_precedence(monkeypatch):
    monkeypatch.setenv("GH_TOKEN", "workflow")
    monkeypatch.setenv("GITHUB_TOKEN", "github")
    monkeypatch.setenv("AAIF_SOURCES_TOKEN", "sources")
    assert GitHubCfg().token() == "sources"


def test_falls_back_to_workflow_token(monkeypatch):
    monkeypatch.delenv("AAIF_SOURCES_TOKEN", raising=False)
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    monkeypatch.setenv("GH_TOKEN", "workflow")
    assert GitHubCfg().token() == "workflow"


def test_empty_sources_token_ignored(monkeypatch):
    # Unset GitHub secrets render as "" in workflow env.
    monkeypatch.setenv("AAIF_SOURCES_TOKEN", "")
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    monkeypatch.setenv("GH_TOKEN", "workflow")
    assert GitHubCfg().token() == "workflow"
