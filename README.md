# DevOps A3 — Auto-updating README

This README updates itself: a GitHub Actions workflow reads the latest repository
events from the GitHub API and rewrites the section below. Tracked in issue #1.

## 📈 Recent Activity

<!--START_SECTION:activity-->
1. 📌 Closed issue [#9](https://github.com/NIU1642329/devops-a3-readme-automation/issues/9): Verification, screenshots, report by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
2. 🔀 Labeled PR [#13](https://github.com/NIU1642329/devops-a3-readme-automation/pull/13) by [@dependabot[bot]](https://github.com/dependabot[bot]) · 2026-10-05
3. 🔀 Labeled PR [#13](https://github.com/NIU1642329/devops-a3-readme-automation/pull/13) by [@dependabot[bot]](https://github.com/dependabot[bot]) · 2026-10-05
4. 🔀 Labeled PR [#13](https://github.com/NIU1642329/devops-a3-readme-automation/pull/13) by [@dependabot[bot]](https://github.com/dependabot[bot]) · 2026-10-05
5. 🔀 Labeled PR [#13](https://github.com/NIU1642329/devops-a3-readme-automation/pull/13) by [@dependabot[bot]](https://github.com/dependabot[bot]) · 2026-10-05
6. 🔀 Opened PR [#13](https://github.com/NIU1642329/devops-a3-readme-automation/pull/13) by [@dependabot[bot]](https://github.com/dependabot[bot]) · 2026-10-05
7. 🌱 Created branch `dependabot/github_actions/actions/checkout-7.0.1` by [@dependabot[bot]](https://github.com/dependabot[bot]) · 2026-10-05
8. 📌 Closed issue [#1](https://github.com/NIU1642329/devops-a3-readme-automation/issues/1): As repo owner, I want the README to auto-update with recent… by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
9. 🔀 Merged PR [#12](https://github.com/NIU1642329/devops-a3-readme-automation/pull/12) by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
10. ⬆️ Pushed [`100be63`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/100be63) to `1-auto-update-readme` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05

<sub>Last updated: 2026-10-05 16:17 UTC by the update-readme workflow</sub>
<!--END_SECTION:activity-->

## ⚙️ How it works

| Workflow | Trigger | What it does |
|---|---|---|
| `update-readme.yml` | every 6 h, manual, push to `main` | Regenerates the activity section and commits only if it changed |
| `validate-readme.yml` | every PR and push | Fails CI if the activity markers are missing or a token leaked |
| `preview-readme.yml` | every PR | Dry-runs the generator and shows the result in the job summary |

## 👤 About me

Laia Alcalde · DevOps (NTUST) · Student ID: F11515010
