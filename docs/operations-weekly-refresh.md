# Weekly unattended refresh

The `Weekly wiki refresh` GitHub Actions workflow runs Mondays at 09:17 UTC and
can also be dispatched manually. It scans sources, curates pending events,
applies the autonomous resolution ladder, runs deterministic OKF validation,
opens a PR, and requests GitHub auto-merge. The PR is the audit trail; merge
happens only after required deterministic CI checks pass.

## One-time repository setup

Add these Actions secrets under **Settings → Secrets and variables → Actions**:

1. `GCP_VERTEX_SERVICE_ACCOUNT_JSON`: the complete service account JSON for
   `instinct@alanblount-demo.iam.gserviceaccount.com`.
2. `JEV_API_KEY`: optional TypeSafe API key. If omitted, Jev fails open and the
   Vertex/deterministic pipeline still runs.

The workflow's `GITHUB_TOKEN` needs repository write permission. The workflow
requests `contents: write` and `pull-requests: write`; organization/repository
policy can still cap it. In **Settings → Actions → General**, set Workflow
permissions to **Read and write permissions** and allow GitHub Actions to create
and approve pull requests if the first run reports a permission error.

Repository auto-merge must be enabled in **Settings → General → Pull Requests**.
Branch protection or rulesets should require the deterministic CI job. The CLI
requests squash auto-merge only after creating the refresh PR.

The service-account JSON stored in Instinct's vault cannot be copied into a
GitHub Actions secret. Alan must add `GCP_VERTEX_SERVICE_ACCOUNT_JSON` once in
GitHub. This is the only unavoidable manual credential bridge.
