# DevOps A3 — Auto-updating README

This README updates itself: a GitHub Actions workflow reads the latest repository
events from the GitHub API and rewrites the section below. Tracked in issue #1.

## 📈 Recent Activity

<!--START_SECTION:activity-->
1. 📌 Closed issue [#1](https://github.com/NIU1642329/devops-a3-readme-automation/issues/1): As repo owner, I want the README to auto-update with recent… by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
2. 🔀 Merged PR [#12](https://github.com/NIU1642329/devops-a3-readme-automation/pull/12) by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
3. ⬆️ Pushed [`100be63`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/100be63) to `1-auto-update-readme` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
4. ⬆️ Pushed [`ba6aac4`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/ba6aac4) to `1-auto-update-readme` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
5. 🔀 Opened PR [#12](https://github.com/NIU1642329/devops-a3-readme-automation/pull/12) by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
6. ⬆️ Pushed [`9bf5e91`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/9bf5e91) to `1-auto-update-readme` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
7. ⬆️ Pushed [`0434f22`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/0434f22) to `1-auto-update-readme` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
8. ⬆️ Pushed [`0434f22`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/0434f22) to `1-auto-update-readme` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
9. ⬆️ Pushed [`1225218`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/1225218) to `1-auto-update-readme` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05
10. ⬆️ Pushed [`603a737`](https://github.com/NIU1642329/devops-a3-readme-automation/commit/603a737) to `1-auto-update-readme` by [@NIU1642329](https://github.com/NIU1642329) · 2026-10-05

<sub>Last updated: 2026-10-05 15:59 UTC by the update-readme workflow</sub>
<!--END_SECTION:activity-->

## ⚙️ How it works

| Workflow | Trigger | What it does |
|---|---|---|
| `update-readme.yml` | every 6 h, manual, push to `main` | Regenerates the activity section and commits only if it changed |
| `validate-readme.yml` | every PR and push | Fails CI if the activity markers are missing or a token leaked |
| `preview-readme.yml` | every PR | Dry-runs the generator and shows the result in the job summary |

## 👤 About me

Laia Alcalde · DevOps (NTUST) · Student ID: F11515010
