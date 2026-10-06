# DevOps A3 — Auto-updating README

This README updates itself: a GitHub Actions workflow reads the latest repository
events from the GitHub API and rewrites the section below. Tracked in issue #1.

## 📈 Recent Activity

<!--START_SECTION:activity-->
1. 📌 Closed issue [#9](https://github.com/NIU1642329/devops-a3-readme-automation/issues/9): Verification, screenshots, report by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
2. 🔀 Labeled PR [#13](https://github.com/NIU1642329/devops-a3-readme-automation/pull/13) by [@dependabot[bot]](https://github.com/dependabot[bot]) · 2026-10-05
3. 🔀 Labeled PR [#13](https://github.com/NIU1642329/devops-a3-readme-automation/pull/13) by [@dependabot[bot]](https://github.com/dependabot[bot]) · 2026-10-05
4. ⬆️ Pushed [`b97ccf0`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/b97ccf0) to `main` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
5. ⬆️ Pushed [`d2664df`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/d2664df) to `1-auto-update-readme` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
6. ⬆️ Pushed [`0b6b1b6`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/0b6b1b6) to `main` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
7. ⬆️ Pushed [`d761bed`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/d761bed) to `main` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
8. ⬆️ Pushed [`1cb6f42`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/1cb6f42) to `main` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
9. ⬆️ Pushed [`c8e8cdc`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/c8e8cdc) to `main` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
10. ⬆️ Pushed [`8a8cb39`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/8a8cb39) to `1-auto-update-readme` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05

<sub>Last updated: 2026-10-06 00:04 UTC by the update-readme workflow</sub>
<!--END_SECTION:activity-->

## ⚙️ How it works

| Workflow | Trigger | What it does |
|---|---|---|
| `update-readme.yml` | every 6 h, manual, push to `main` | Regenerates the activity section and commits only if it changed |
| `validate-readme.yml` | every PR and push | Fails CI if the activity markers are missing or a token leaked |
| `preview-readme.yml` | every PR | Dry-runs the generator and shows the result in the job summary |

## 👤 About me

Laia Alcalde · DevOps (NTUST) · Student ID: F11515010
