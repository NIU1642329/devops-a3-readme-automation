#!/usr/bin/env python3
"""Refresh the README "Recent Activity" section from the GitHub Events API.

- ETag cache in .cache/activity.json (304 responses don't count against the rate limit)
- Rate-limit aware retries with exponential backoff (configurable through env vars)
- Multi-repo aggregation (REPOS="owner/a,owner/b")
- Idempotent: the README is only rewritten when the activity list really changes
- Ignores the workflow's own commits, so it never reports itself (no self-update loop)
- DRY_RUN=true writes a preview to the job summary without touching any file
The token comes from the GH_TOKEN env var and is never printed.
"""
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

START = "<!--START_SECTION:activity-->"
END = "<!--END_SECTION:activity-->"
STAMP = "<sub>Last updated:"
BOT_EMAIL = "41898282+github-actions[bot]@users.noreply.github.com"

README = Path(os.getenv("README_PATH", "README.md"))
CACHE = Path(os.getenv("CACHE_PATH", ".cache/activity.json"))
REPOS = [r.strip() for r in (os.getenv("REPOS") or os.getenv("GITHUB_REPOSITORY", "")).split(",") if r.strip()]
MAX_ITEMS = int(os.getenv("MAX_ITEMS", "10"))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "4"))
BACKOFF_BASE = float(os.getenv("BACKOFF_BASE", "2"))
MAX_WAIT = float(os.getenv("MAX_WAIT", "60"))
IGNORE_ACTORS = {a.strip() for a in os.getenv("IGNORE_ACTORS", "github-actions[bot]").split(",") if a.strip()}
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"
TOKEN = os.getenv("GH_TOKEN", "")

stats = {"HTTP calls": 0, "304 Not Modified (free)": 0, "Retries": 0,
         "Fell back to cache": 0, "Rate limit remaining": "n/a"}


class TransientError(Exception):
    """Retries exhausted: keep the last known data instead of failing the job."""


def fail(message):
    print(f"::error::{message}")
    sys.exit(1)


def append_file(env_var, text):
    path = os.getenv(env_var)
    if path:
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(text)


def fetch_events(repo, etag):
    """Return (events, etag). events is None when GitHub answers 304 Not Modified."""
    url = f"https://api.github.com/repos/{repo}/events?per_page=50"
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28",
               "User-Agent": "readme-activity-workflow"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    if etag:
        headers["If-None-Match"] = etag

    for attempt in range(MAX_RETRIES + 1):
        stats["HTTP calls"] += 1
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as resp:
                stats["Rate limit remaining"] = resp.headers.get("X-RateLimit-Remaining", "n/a")
                return json.load(resp), resp.headers.get("ETag")
        except urllib.error.HTTPError as err:
            stats["Rate limit remaining"] = err.headers.get("X-RateLimit-Remaining", "n/a")
            if err.code == 304:
                stats["304 Not Modified (free)"] += 1
                return None, etag
            rate_limited = err.code == 429 or (err.code == 403 and (
                err.headers.get("Retry-After") or err.headers.get("X-RateLimit-Remaining") == "0"))
            if not rate_limited and err.code < 500:
                # 401/403/404 = wrong or expired token, or no access. Never print the response body.
                fail(f"GitHub API returned HTTP {err.code} for {repo}. "
                     "Check that REPO_TOKEN is valid, not expired and can read this repository.")
            wait = BACKOFF_BASE ** attempt
            if err.headers.get("Retry-After"):
                wait = float(err.headers["Retry-After"])
            elif err.headers.get("X-RateLimit-Remaining") == "0" and err.headers.get("X-RateLimit-Reset"):
                wait = float(err.headers["X-RateLimit-Reset"]) - time.time()
            reason = f"HTTP {err.code}"
        except (urllib.error.URLError, TimeoutError):
            wait, reason = BACKOFF_BASE ** attempt, "network error"
        if attempt == MAX_RETRIES or wait > MAX_WAIT:
            raise TransientError(f"{reason} for {repo} after {attempt + 1} attempt(s)")
        stats["Retries"] += 1
        print(f"{reason} for {repo}; retrying in {max(wait, 1):.0f}s ({attempt + 1}/{MAX_RETRIES})")
        time.sleep(max(wait, 1))
    raise TransientError(f"retries exhausted for {repo}")


def own_commit_shas():
    """SHAs of the commits this workflow made, so their PushEvents can be ignored."""
    try:
        log = subprocess.run(["git", "log", "-n", "200", "--format=%H %ae"],
                             capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return set()
    return {line.split()[0] for line in log.splitlines() if line.endswith(BOT_EMAIL)}


def clean(text, limit=60):
    """Titles and branch names are user input: they must not break the markers or the Markdown."""
    text = str(text or "").replace("\n", " ").replace("<", "").replace(">", "").replace("`", "'")
    return text if len(text) <= limit else text[: limit - 1] + "…"


def describe(ev):
    kind = ev.get("type", "")
    p = ev.get("payload") or {}
    base = f"https://github.com/{ev.get('repo', {}).get('name', '')}"
    if kind == "PushEvent":
        branch = clean((p.get("ref") or "").removeprefix("refs/heads/"))
        sha = (p.get("head") or "")[:7]
        return f"⬆️ Pushed [`{sha}`]({base}/commit/{sha}) to `{branch}`"
    if kind == "PullRequestEvent":
        pr = p.get("pull_request") or {}
        num = pr.get("number") or p.get("number")
        action = p.get("action", "updated")
        if action == "closed" and pr.get("merged"):
            action = "merged"
        title = f": {clean(pr['title'])}" if pr.get("title") else ""
        return f"🔀 {action.capitalize()} PR [#{num}]({base}/pull/{num}){title}"
    if kind == "IssuesEvent":
        issue = p.get("issue") or {}
        num = issue.get("number")
        title = f": {clean(issue['title'])}" if issue.get("title") else ""
        return f"📌 {p.get('action', 'updated').capitalize()} issue [#{num}]({base}/issues/{num}){title}"
    if kind == "IssueCommentEvent":
        num = (p.get("issue") or {}).get("number")
        return f"💬 Commented on [#{num}]({base}/issues/{num})"
    if kind == "PullRequestReviewEvent":
        num = (p.get("pull_request") or {}).get("number")
        return f"✅ Reviewed PR [#{num}]({base}/pull/{num})"
    if kind == "CreateEvent":
        ref = f" `{clean(p['ref'])}`" if p.get("ref") else ""
        return f"🌱 Created {p.get('ref_type', 'ref')}{ref}"
    if kind == "DeleteEvent":
        return f"🗑️ Deleted {p.get('ref_type', 'ref')} `{clean(p.get('ref'))}`"
    if kind == "ReleaseEvent":
        return f"🚀 Published release `{clean((p.get('release') or {}).get('tag_name'))}`"
    if kind == "WatchEvent":
        return "⭐ Starred the repository"
    if kind == "ForkEvent":
        return "🍴 Forked the repository"
    return f"🔧 {clean(kind.removesuffix('Event'))}"


def to_item(ev):
    repo = ev.get("repo", {}).get("name", "")
    actor = ev.get("actor", {}).get("login", "someone")
    where = f" in [{repo}](https://github.com/{repo})" if len(REPOS) > 1 else ""
    date = (ev.get("created_at") or "")[:10]
    line = f"{describe(ev)}{where} by [@{actor}](https://github.com/{actor}) · {date}"
    return {"id": ev.get("id"), "at": ev.get("created_at", ""), "line": line}


def main():
    if not REPOS:
        fail("No repository configured: set REPOS or run inside GitHub Actions.")
    readme = README.read_text(encoding="utf-8")
    if readme.count(START) != 1 or readme.count(END) != 1 or readme.index(START) > readme.index(END):
        fail(f"{README} must contain exactly one {START} followed by exactly one {END}.")

    try:
        cache = json.loads(CACHE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        cache = {"repos": {}}
    own_shas = own_commit_shas()
    new_cache, items = {"repos": {}}, []

    for repo in REPOS:
        cached = cache.get("repos", {}).get(repo, {})
        try:
            events, etag = fetch_events(repo, cached.get("etag"))
        except TransientError as exc:
            print(f"::warning::{exc}. Keeping the last cached activity.")
            stats["Fell back to cache"] += 1
            events, etag = None, cached.get("etag")
        if events is None:
            repo_items = cached.get("items", [])
        else:
            repo_items = [
                to_item(ev) for ev in events
                if ev.get("actor", {}).get("login") not in IGNORE_ACTORS
                and not (ev.get("type") == "PushEvent"
                         and (ev.get("payload") or {}).get("head") in own_shas)
            ][:MAX_ITEMS]
        new_cache["repos"][repo] = {"etag": etag, "items": repo_items}
        items.extend(repo_items)

    items.sort(key=lambda i: i["at"], reverse=True)
    body = "\n".join(f"{n}. {i['line']}" for n, i in enumerate(items[:MAX_ITEMS], 1))
    body = body or "_No recent activity yet._"

    before, rest = readme.split(START, 1)
    current, after = rest.split(END, 1)
    current_body = "\n".join(line for line in current.strip().splitlines()
                             if not line.startswith(STAMP)).strip()
    changed = current_body != body

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    section = f"{START}\n{body}\n\n{STAMP} {stamp} by the update-readme workflow</sub>\n{END}"

    if not DRY_RUN:
        if changed:
            README.write_text(before + section + after, encoding="utf-8")
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        CACHE.write_text(json.dumps(new_cache, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    append_file("GITHUB_OUTPUT", f"changed={'true' if changed and not DRY_RUN else 'false'}\n")
    table = "\n".join(f"| {k} | {v} |" for k, v in stats.items())
    summary = (f"### README activity {'preview (dry run)' if DRY_RUN else 'update'}\n\n"
               f"README changed: **{changed}**\n\n| Metric | Value |\n|---|---|\n{table}\n")
    if DRY_RUN:
        summary += f"\n#### Section as it would look after merge\n\n{body}\n"
    append_file("GITHUB_STEP_SUMMARY", summary)
    print(f"README changed: {changed}; " + "; ".join(f"{k}: {v}" for k, v in stats.items()))


if __name__ == "__main__":
    main()
