# Awesome Agent Orchestration [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated open-source tools that already solve governed multi-agent work: tickets and runs, worktree isolation, software factories, and control planes.

Before building a private control plane for these problems, check whether one of the tools below already does the job, adopt it, and contribute upstream if it is missing a piece you need.

Entries say what a project does, not what it markets, and carry its license and maturity where that matters. Tools that could not be run, or that were dormant, young, or undocumented-in-practice, were left out. Hands-on checks are recorded on the pull request for the tools that were actually run; this list does not claim that every entry was checked.

## Contents

- [The problem map](#the-problem-map)
- [Agent company / control planes](#agent-company--control-planes)
- [Local-first coding factories](#local-first-coding-factories)
- [Related: observability](#related-observability)
- [Anti-patterns](#anti-patterns)

## The problem map

- Org chart, budgets, goals, and governance for a multi-agent "company": Paperclip.
- Markdown tickets, staged pipelines with retries, any CLI agent: Kontora.
- Many coding agents in parallel, each in its own Git worktree, with PR and CI state on one board: Agent Orchestrator.
- GitHub issues to per-issue worktrees and PR status, headless agent CLIs: Vigilante.
- Plan, build, and review loops in isolated worktrees (early preview): Fusion.
- Parallel agent sessions in a terminal, one worktree each: Claude Squad.

## Agent company / control planes

- [Paperclip](https://github.com/paperclipai/paperclip) - Self-hosted MIT-licensed control plane for teams of AI agents, with companies, org charts, tasks, heartbeats, budgets, and board governance, running your own runtimes (Claude Code, Codex, CLI agents, webhooks); telemetry is on by default.

## Local-first coding factories

- [Kontora](https://github.com/worksonmyai/kontora) - Apache-2.0 tool that keeps tickets as markdown files and runs them through multi-stage pipelines with retries, one worktree and tmux session per ticket, a web and TUI kanban, and any CLI agent.
- [Agent Orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) - Apache-2.0 local daemon and desktop app that spawns coding agents (Claude Code, Codex, Cursor, opencode, and others) into per-task Git worktrees, with an orchestrator agent and a board of PR, CI, and review state, and ticket intake behind a flag.
- [Vigilante](https://github.com/aliengiraffe/vigilante) - Apache-2.0 Go CLI and daemon that turns GitHub issues into per-issue Git worktrees and branches, launches a headless coding-agent CLI (Codex, Claude Code, Gemini, opencode) in each, and records session state, blocked reasons, and PR status, with GitHub as the only issue backend and one dominant author.
- [Fusion](https://github.com/Runfusion/Fusion) - Early-preview MIT-licensed software factory that runs plan, build, and review loops in isolated worktrees, with workflows and a dashboard, against any model.
- [Claude Squad](https://github.com/smtg-ai/claude-squad) - AGPL-3.0-licensed terminal app on tmux that runs Claude Code, Codex, Gemini, Aider, and other CLI agents in parallel, one Git worktree and branch per session, managing sessions only, with no tickets and no run log.

## Related: observability

Orchestration is not observability. For tracing, evals, guardrails, and MCP tooling see [awesome-agent-observability](https://github.com/anhermon/awesome-agent-observability).

## Anti-patterns

- Building a private "shared agent infra" monorepo when an adoptable tool above already covers tickets, runs, adapters, and governance.
- Owning a second ticket and run state machine alongside the one your tracker already has. Extract a library only after two or more real consumers need the same code.
- Adopting a control plane on its README. Run it with a stub agent first and check that it records a failed run as failed, keeps work isolated, and leaves your main checkout clean; several popular-looking tools fail one of these.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs welcome for tools that are open source, actively maintained, and map to an item on the problem map. Show what you ran.

To the extent possible under law, Angel Hermon has waived all copyright and related or neighboring rights to this work. CC0 1.0, 2026.
