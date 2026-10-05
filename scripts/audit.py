#!/usr/bin/env python3
"""Mechanical health check for every GitHub-hosted entry in README.md.

Flags repositories that are gone, archived, renamed or transferred, or whose
last commit is older than the 12-month bar. It cannot judge quality or whether
a description is still accurate; that is the hands-on re-audit.

Usage: GITHUB_TOKEN=... python3 scripts/audit.py [README.md]
Prints a Markdown report. Exit code is 0 unless the API is unreachable.
"""
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request

STALE_DAYS = 365
WARN_DAYS = 270
ENTRY = re.compile(r"^- \[(?P<name>[^\]]+)\]\((?P<url>https?://[^)]+)\)")
REPO = re.compile(r"^https://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/#?]+)")


def parse(text):
    """Return [(name, url, (owner, repo) or None)] for each list entry."""
    out = []
    for line in text.splitlines():
        m = ENTRY.match(line)
        if not m:
            continue
        r = REPO.match(m["url"])
        out.append((m["name"], m["url"], (r["owner"], r["repo"]) if r else None))
    return out


def gh_get(path):
    req = urllib.request.Request(
        "https://api.github.com" + path,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + os.environ.get("GITHUB_TOKEN", ""),
            "User-Agent": "awesome-list-audit",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, json.load(resp)
    except urllib.error.HTTPError as e:
        return e.code, None


def judge(name, owner, repo, meta, last_commit, now):
    """Return a list of (severity, message) findings for one entry."""
    found = []
    full = meta["full_name"]
    if full.lower() != f"{owner}/{repo}".lower():
        found.append(("fix", f"moved to `{full}`; update the link"))
    if meta.get("archived"):
        found.append(("remove", "repository is archived"))
    if meta.get("disabled"):
        found.append(("remove", "repository is disabled"))
    if last_commit is None:
        found.append(("check", "could not read the last commit"))
    else:
        age = (now - last_commit).days
        if age > STALE_DAYS:
            found.append(("remove", f"last commit {age} days ago ({last_commit:%Y-%m-%d})"))
        elif age > WARN_DAYS:
            found.append(("watch", f"last commit {age} days ago; goes stale in {STALE_DAYS - age} days"))
    if not (meta.get("license") or {}).get("spdx_id"):
        found.append(("check", "no license detected by GitHub"))
    return found


def last_commit_date(owner, repo):
    status, data = gh_get(f"/repos/{owner}/{repo}/commits?per_page=1")
    if status != 200 or not data:
        return None
    return dt.datetime.fromisoformat(data[0]["commit"]["committer"]["date"].replace("Z", "+00:00"))


def main(path="README.md"):
    now = dt.datetime.now(dt.timezone.utc)
    report, api_failures = [], 0
    entries = parse(open(path).read())
    for name, url, repo in entries:
        if repo is None:
            report.append(("manual", name, "not a GitHub repo; check the link and claims by hand"))
            continue
        owner, rname = repo
        status, meta = gh_get(f"/repos/{owner}/{rname}")
        if status == 404:
            report.append(("remove", name, f"{url} returns 404"))
            continue
        if status != 200:
            api_failures += 1
            report.append(("check", name, f"GitHub API returned {status}"))
            continue
        for sev, msg in judge(name, owner, rname, meta, last_commit_date(owner, rname), now):
            report.append((sev, name, msg))
    order = ["remove", "fix", "check", "watch", "manual"]
    print(f"# Entry audit, {now:%Y-%m-%d}\n")
    print(f"{len(entries)} entries checked, {len(report)} findings.\n")
    for sev in order:
        rows = [r for r in report if r[0] == sev]
        if rows:
            print(f"## {sev}\n")
            for _, name, msg in rows:
                print(f"- **{name}**: {msg}")
            print()
    return 1 if api_failures == len(entries) else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
