# Contributing

## What belongs here

Open-source tools for governed multi-agent work: tickets and runs, worktree isolation, software factories, and control planes. General agent frameworks and libraries (LangGraph, CrewAI and the like) are building blocks, not orchestration products, and are out of scope. Tracing, evals, and guardrails belong in [awesome-agent-observability](https://github.com/anhermon/awesome-agent-observability).

## Requirements

- The link resolves and points at the canonical repo. Follow redirects and use the current owner.
- Updated within the last 12 months, not archived, not sunsetting.
- A license file in the repository, and the license stated in the entry.
- You ran it. Build or install it, run a task with a stub agent (a shell script is enough), and confirm that work is isolated, that the run is recorded, and that a failure is recorded as a failure. Say what you ran in the PR. Tools that are only a README, only weeks old, or mostly generated boilerplate do not make the list.
- Preview or alpha status is stated in the entry.
- Format: `- [Name](link) - License. What it actually does.` One line, sentence case, no marketing words.

## How the list is maintained

A weekly workflow (`scripts/audit.py`) opens or updates one tracking issue listing entries whose repository is gone, archived, renamed, or past the 12-month bar. A monthly hands-on pass re-runs entries with a stub agent and re-checks descriptions, which the script cannot do.

## Removals

Open an issue with evidence: last commit date, archive or sunset banner, redirect target, or a failing run.

## Process

1. Fork, add your entry, run `npx awesome-lint`.
2. Open a pull request using the template.
