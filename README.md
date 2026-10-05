# DevOps A3 — Auto-updating README

This README updates itself: a GitHub Actions workflow reads the latest repository
events from the GitHub API and rewrites the section below. Tracked in issue #1.

## 📈 Recent Activity

<!--START_SECTION:activity-->
1. ⬆️ Pushed [`85bcd66`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/85bcd66) to `main` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
2. 🔀 Merged PR [#10](https://github.com/NIU1642329/devops-a3-readme-automation/pull/10) by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
3. 🔀 Opened PR [#10](https://github.com/NIU1642329/devops-a3-readme-automation/pull/10) by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
4. 🌱 Created branch `1-auto-update-readme` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-04
5. 📌 Opened issue [#9](https://github.com/NIU1642329/devops-a3-readme-automation/issues/9): Verification, screenshots, report by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-04
6. 📌 Opened issue [#8](https://github.com/NIU1642329/devops-a3-readme-automation/issues/8): PR, review, merge by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-04
7. 📌 Opened issue [#7](https://github.com/NIU1642329/devops-a3-readme-automation/issues/7): Validation + preview workflows, Dependabot by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-04
8. 📌 Opened issue [#6](https://github.com/NIU1642329/devops-a3-readme-automation/issues/6): 'update-readme.yml' workflow by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-04
9. 📌 Opened issue [#5](https://github.com/NIU1642329/devops-a3-readme-automation/issues/5): Generator script (API, cache, backoff) by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-04
10. 🌱 Created branch `main` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-04

<sub>Last updated: 2026-10-05 15:19 UTC by the update-readme workflow</sub>
<!--END_SECTION:activity-->

## ⚙️ How it works

| Workflow | Trigger | What it does |
|---|---|---|
| `update-readme.yml` | every 6 h, manual, push to `main` | Regenerates the activity section and commits only if it changed |
| `validate-readme.yml` | every PR and push | Fails CI if the activity markers are missing or a token leaked |
| `preview-readme.yml` | every PR | Dry-runs the generator and shows the result in the job summary |

## 👤 About me

Laia Alcalde · DevOps (NTUST) · Student ID: F11515010
