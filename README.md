# Awesome Agent Orchestration [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated open-source tools that already solve governed multi-agent work: tickets/runs, software factories, worktree isolation, and control planes.

Do not build another private control plane for these problems. Pick an existing tool below, adopt it, and contribute upstream if it is missing a piece you need.

This list replaces a discontinued experiment (`anhermon/agent-infra`) that reinvented the same surface. Prefer free/open-source options.

## Contents

- [The problem map](#the-problem-map)
- [Agent company / control planes](#agent-company--control-planes)
- [Local-first coding factories](#local-first-coding-factories)
- [Ticket → pipeline → PR](#ticket--pipeline--pr)
- [Related: observability](#related-observability)
- [Anti-patterns](#anti-patterns)

## The problem map

| If you need… | Start here |
|---|---|
| Org chart, budgets, goals, multi-agent “company” governance | [Paperclip](https://github.com/paperclipai/paperclip) |
| Shared project tasks, manager delegation, persistent sandboxes, and human review | [Tale](https://github.com/tale-project/tale) |
| Local SQLite + multi-repo worktrees + ticket sync + agent workflows | [Conductor](https://github.com/artushin/conductor-ai) |
| Software factory: plan → execute → review in isolated worktrees | [Fusion](https://github.com/Runfusion/Fusion) |
| Markdown tickets → staged pipelines → any CLI agent | [Kontora](https://github.com/worksonmyai/kontora) |
| External tickets (GitHub / Linear / Jira) → specialized agents → PR | [SprintFoundry](https://github.com/Sagart-cactus/SprintFoundry) |

## Agent company / control planes

- [Paperclip](https://github.com/paperclipai/paperclip) - MIT. Self-hosted control plane for teams of AI agents: companies, org charts, tasks, heartbeats, budgets, board governance. Bring your own runtimes (Claude Code, Codex, CLI agents, webhooks). Prefer this over inventing another ticket/run OS.
- [Tale](https://github.com/tale-project/tale) - MIT. Shared project workspace for people and AI agents, with manager delegation, persistent sandbox workspaces, and human review of reports and delivered files. Self-hosted or managed deployment.

## Local-first coding factories

- [Conductor](https://github.com/artushin/conductor-ai) - Local-first multi-repo orchestration: git worktrees, GitHub/Jira ticket sync, SQLite state, workflow DSL, Claude agents in tmux, CLI/TUI/web.
- [Fusion](https://github.com/Runfusion/Fusion) - MIT software factory. Multi-agent plan/build/review loops in isolated worktrees, workflows, dashboard, any model.
- [Kontora](https://github.com/worksonmyai/kontora) - Tickets as markdown; multi-stage pipelines with retries; one worktree and tmux session per ticket; web + TUI kanban; any CLI agent.

## Ticket → pipeline → PR

- [SprintFoundry](https://github.com/Sagart-cactus/SprintFoundry) - Pulls tickets from GitHub, Linear, or Jira; runs specialized agents (plan, implement, QA, …); lands tested pull requests.

## Related: observability

Orchestration is not observability. For tracing, evals, guardrails, and MCP tooling see [awesome-agent-observability](https://github.com/anhermon/awesome-agent-observability).

## Anti-patterns

- Building a private “shared agent infra” monorepo when Paperclip or Conductor already cover tickets, runs, adapters, and governance.
- Treating dual ticket/run state machines as a reason to own the whole stack — extract a library only after two or more real consumers need the same code.
- Fork-only control planes that never ship a usable CLI/UI and accumulate permanence through backlog documents.

## Contributing

PRs welcome for tools that are open source (or clearly documented hosted products), actively maintained, and that map cleanly to a row in the problem map. Prefer describing what the tool does, not its marketing.

To the extent possible under law, Angel Hermon has waived all copyright and related or neighboring rights to this work. CC0 1.0, 2026.
