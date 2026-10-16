# Awesome Agent Orchestration [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated open-source tools that already solve governed multi-agent work: tickets and runs, worktree isolation, software factories, and control planes.

Before building a private control plane for these problems, check whether one of the tools below already does the job, adopt it, and contribute upstream if it is missing a piece you need.

Entries say what a project does, not what it markets, and carry its license and maturity where that matters. Tools that could not be run, or that were dormant, young, or undocumented-in-practice, were left out. Hands-on checks are recorded on the pull request for the tools that were actually run; this list does not claim that every entry was checked. Several entries are written mostly by one person (Kontora, Vigilante, Fusion, ccmanager, Cline Kanban, Bernstein, takt), and herdr, Agent Deck, Archon, Claudexor and dmux have a clear lead author too, so check the bus factor before you depend on any of them.

## Contents

- [The problem map](#the-problem-map)
- [Agent company / control planes](#agent-company--control-planes)
- [Local-first coding factories](#local-first-coding-factories)
- [Boards and governed runs](#boards-and-governed-runs)
- [Workflow engines](#workflow-engines)
- [Terminal session managers](#terminal-session-managers)
- [Related: observability](#related-observability)
- [Anti-patterns](#anti-patterns)

## The problem map

- Org chart, budgets, goals, and governance for a multi-agent "company": Paperclip.
- Markdown tickets, staged pipelines with retries, any CLI agent: Kontora.
- Many coding agents in parallel, each in its own Git worktree, with PR and CI state on one board: Agent Orchestrator.
- A desktop app and scriptable CLI that run agents side by side, a worktree each, with a headless runtime: Orca.
- GitHub issues to per-issue worktrees and PR status, headless agent CLIs: Vigilante.
- Plan, build, and review loops in isolated worktrees (early preview): Fusion.
- Parallel agent sessions in a terminal, one worktree each: Claude Squad, ccmanager, dmux.
- Terminal session status across agents, with optional per-session worktrees: Agent Deck, Agent of Empires.
- A persistent terminal runtime with an API agents can drive and optional worktrees: herdr.
- A local board that runs CLI agents in parallel, one worktree per card (research preview): Cline Kanban.
- A plan of tasks run across many CLI agents, a worktree per task, with a hash-chained run journal and auto-merge: Bernstein.
- YAML workflows of agent steps, one worktree per run, with a recorded run status and transcript: Archon.
- Queued tasks run through multi-step plan, implement, and review workflows in isolated clones: takt.
- One control plane over several agent CLIs, with write turns kept as patches until you apply them: Claudexor.

## Agent company / control planes

- [Paperclip](https://github.com/paperclipai/paperclip) - Self-hosted MIT-licensed control plane for teams of AI agents, with companies, org charts, tasks, heartbeats, budgets, and board governance, running your own runtimes (Claude Code, Codex, CLI agents, webhooks); telemetry is on by default.
- [Claudexor](https://github.com/razzant/claudexor) - MIT local control plane that runs Claude Code, Codex, Cursor CLI, and OpenCode behind one interface, keeps write turns as patches in a separate workspace until you apply them, records each run's status and artifacts, and offers best-of-N runs across harnesses; its CONTRIBUTING says it is developed largely by external AI coding agents, and its README names one human author.

## Local-first coding factories

- [Kontora](https://github.com/worksonmyai/kontora) - Apache-2.0 tool that keeps tickets as markdown files and runs them through multi-stage pipelines with retries, one worktree and tmux session per ticket, a web and TUI kanban, and any CLI agent.
- [Agent Orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) - Apache-2.0 local daemon and desktop app that spawns coding agents (Claude Code, Codex, Cursor, opencode, and others) into per-task Git worktrees, with an orchestrator agent and a board of PR, CI, and review state, ticket intake behind a flag, and remote telemetry in production desktop releases that can include your GitHub owner or username.
- [Orca](https://github.com/stablyai/orca) - MIT Electron desktop app with a scriptable `orca` CLI and a headless `orca serve` runtime that launches CLI agents (Claude Code, Codex, OpenCode, and others) in one Git worktree per task outside the repository with permission prompts skipped by default, records no failure beyond the terminal output, and documents anonymous usage telemetry with an off switch.
- [Vigilante](https://github.com/aliengiraffe/vigilante) - Apache-2.0 Go CLI and daemon that turns GitHub issues into per-issue Git worktrees and branches, launches a headless coding-agent CLI (Codex, Claude Code, Gemini, opencode) in each, and records session state, blocked reasons, and PR status, with GitHub as the only issue backend.
- [Fusion](https://github.com/Runfusion/Fusion) - Early-preview MIT-licensed software factory that runs plan, build, and review loops in isolated worktrees, with workflows and a dashboard, against any model.

## Boards and governed runs

- [Cline Kanban](https://github.com/cline/kanban) - Apache-2.0 local web board that runs CLI agents (Claude Code, Codex, Gemini, and others) in parallel, one ephemeral Git worktree per card, and records each session's state and exit code; Research Preview.
- [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) - Apache-2.0 Python orchestrator that runs a plan file or goal across CLI agent adapters (Claude Code, Codex, Gemini, and many more), one Git worktree and branch per task, writes a hash-chained run journal, and merges each task's branch back into the current branch.

## Workflow engines

- [Archon](https://github.com/coleam00/Archon) - MIT workflow engine that runs YAML-defined workflows of agent steps (Claude Code, Codex, or Pi) in one Git worktree per run outside the repository, records each run's status and transcript, and sends usage telemetry tied to a random install ID by default.
- [takt](https://github.com/nrslib/takt) - MIT CLI that queues tasks and runs each through a multi-step workflow (plan, implement, review, fix) in an isolated clone outside the repository on its own branch, across agent providers such as Claude Code, Codex, OpenCode, Cursor, and Copilot, with a session log per run and failed tasks marked as failed.

## Terminal session managers

- [Claude Squad](https://github.com/smtg-ai/claude-squad) - AGPL-3.0-licensed terminal app on tmux that runs Claude Code, Codex, Gemini, Aider, and other CLI agents in parallel, one Git worktree and branch per session, managing sessions only, with no tickets and no run log.
- [ccmanager](https://github.com/kbwo/ccmanager) - MIT terminal app that runs Claude Code, Gemini CLI, Codex CLI, and other CLI agents in parallel, one Git worktree per session, shows busy, waiting, and idle states without needing tmux, and manages sessions only, with no tickets, run log, or failure record.
- [Agent Deck](https://github.com/asheshgoplani/agent-deck) - MIT terminal session manager for Claude, Gemini, OpenCode, Codex, and other agents that can place a session in its own Git worktree under the repository's .worktrees folder and shows session status, including errors.
- [herdr](https://github.com/herdrdev/herdr) - Apache-2.0 terminal runtime with a persistent background server that hosts agent panes, can create a Git worktree for a workspace outside the repository, and exposes a socket and CLI API that agents can drive, with no run log or failure record.
- [Agent of Empires](https://github.com/agent-of-empires/agent-of-empires) - MIT Rust terminal session manager that runs each CLI agent (Claude Code, OpenCode, and others) in its own tmux session, with an optional Git worktree per session outside the repository and an Error state when the agent exits non-zero; about half its commits carry AI co-author trailers, and its telemetry is off unless you enable it.
- [dmux](https://github.com/standardagents/dmux) - MIT TUI that runs inside tmux and gives each task a pane, a branch, and a Git worktree under `.dmux/worktrees/` in the repository, launching CLI agents (Claude Code, Codex, OpenCode, and others) with permission prompts skipped by default and offering merge-back from a menu, with no run log or failure record.

## Related: observability

Orchestration is not observability. For tracing, evals, guardrails, and MCP tooling see [awesome-agent-observability](https://github.com/anhermon/awesome-agent-observability).

## Anti-patterns

- Building a private "shared agent infra" monorepo when an adoptable tool above already covers tickets, runs, adapters, and governance.
- Owning a second ticket and run state machine alongside the one your tracker already has. Extract a library only after two or more real consumers need the same code.
- Adopting a control plane on its README. Run it with a stub agent first and check that it records a failed run as failed, keeps work isolated, and leaves your main checkout clean; several popular-looking tools fail one of these.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs welcome for tools that are open source, actively maintained, and map to an item on the problem map. Show what you ran.

To the extent possible under law, Angel Hermon has waived all copyright and related or neighboring rights to this work. CC0 1.0, 2026.
