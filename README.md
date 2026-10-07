# DevOps A3 — Auto-updating README

   [![Update README](https://github.com/NIU1642329/devops-a3-readme-automation/actions/workflows/update-readme.yml/badge.svg)](https://github.com/NIU1642329/devops-a3-readme-automation/actions/workflows/update-readme.yml)
   [![Validate README](https://github.com/NIU1642329/devops-a3-readme-automation/actions/workflows/validate-readme.yml/badge.svg)](https://github.com/NIU1642329/devops-a3-readme-automation/actions/workflows/validate-readme.yml)
   
This README updates itself: a GitHub Actions workflow reads the latest repository
events from the GitHub API and rewrites the section below. Tracked in issue #1.

## 📈 Recent Activity

<!--START_SECTION:activity-->
1. ⬆️ Pushed [`c1f6ed4`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/c1f6ed4) to `main` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
2. 📌 Closed issue [#8](https://github.com/NIU1642329/devops-a3-readme-automation/issues/8): PR, review, merge by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
3. 📌 Closed issue [#7](https://github.com/NIU1642329/devops-a3-readme-automation/issues/7): Validation + preview workflows, Dependabot by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
4. 📌 Closed issue [#6](https://github.com/NIU1642329/devops-a3-readme-automation/issues/6): 'update-readme.yml' workflow by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
5. 📌 Closed issue [#5](https://github.com/NIU1642329/devops-a3-readme-automation/issues/5): Generator script (API, cache, backoff) by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
6. 📌 Closed issue [#4](https://github.com/NIU1642329/devops-a3-readme-automation/issues/4): Fine-grained token + 'REPO_TOKEN' secret by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
7. 📌 Closed issue [#3](https://github.com/NIU1642329/devops-a3-readme-automation/issues/3): README template with markers by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
8. 📌 Closed issue [#2](https://github.com/NIU1642329/devops-a3-readme-automation/issues/2): Planning: project board, issue, branch by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-06
9. ⬆️ Pushed [`1c213ba`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/1c213ba) to `1-auto-update-readme` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
10. ⬆️ Pushed [`451aef8`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/451aef8) to `main` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05

<sub>Last updated: 2026-10-07 06:00 UTC by the update-readme workflow</sub>
<!--END_SECTION:activity-->

## ⚙️ How it works

| Workflow | Trigger | What it does |
|---|---|---|
| `update-readme.yml` | every 6 h, manual, push to `main` | Regenerates the activity section and commits only if it changed |
| `validate-readme.yml` | every PR and push | Fails CI if the activity markers are missing or a token leaked |
| `preview-readme.yml` | every PR | Dry-runs the generator and shows the result in the job summary |

## 👤 About me

Laia Alcalde · DevOps (NTUST) · Student ID: F11515010
