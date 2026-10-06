# DevOps A3 — Auto-updating README

This README updates itself: a GitHub Actions workflow reads the latest repository
events from the GitHub API and rewrites the section below. Tracked in issue #1.

## 📈 Recent Activity

<!--START_SECTION:activity-->
1. 📌 Closed issue [#8](https://github.com/NIU1642329/devops-a3-readme-automation/issues/8): PR, review, merge by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
2. 📌 Closed issue [#7](https://github.com/NIU1642329/devops-a3-readme-automation/issues/7): Validation + preview workflows, Dependabot by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
3. 📌 Closed issue [#6](https://github.com/NIU1642329/devops-a3-readme-automation/issues/6): 'update-readme.yml' workflow by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
4. 📌 Closed issue [#5](https://github.com/NIU1642329/devops-a3-readme-automation/issues/5): Generator script (API, cache, backoff) by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
5. 📌 Closed issue [#4](https://github.com/NIU1642329/devops-a3-readme-automation/issues/4): Fine-grained token + 'REPO_TOKEN' secret by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
6. 📌 Closed issue [#3](https://github.com/NIU1642329/devops-a3-readme-automation/issues/3): README template with markers by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
7. 📌 Closed issue [#2](https://github.com/NIU1642329/devops-a3-readme-automation/issues/2): Planning: project board, issue, branch by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
8. ⬆️ Pushed [`b97ccf0`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/b97ccf0) to `main` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
9. ⬆️ Pushed [`d2664df`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/d2664df) to `1-auto-update-readme` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
10. ⬆️ Pushed [`d761bed`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/d761bed) to `main` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05

<sub>Last updated: 2026-10-06 01:39 UTC by the update-readme workflow</sub>
<!--END_SECTION:activity-->

## ⚙️ How it works

| Workflow | Trigger | What it does |
|---|---|---|
| `update-readme.yml` | every 6 h, manual, push to `main` | Regenerates the activity section and commits only if it changed |
| `validate-readme.yml` | every PR and push | Fails CI if the activity markers are missing or a token leaked |
| `preview-readme.yml` | every PR | Dry-runs the generator and shows the result in the job summary |

## 👤 About me

Laia Alcalde · DevOps (NTUST) · Student ID: F11515010
