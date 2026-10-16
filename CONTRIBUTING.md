# Contributing

## What belongs here

Open-source tools for governed multi-agent work: tickets and runs, worktree isolation, supervisors and task routing, kanban boards and control planes, harness and runtime coordination, and workflow engines whose job is to drive agents. General agent frameworks and libraries (LangGraph, CrewAI, Microsoft Agent Framework, the OpenAI Agents SDK, Google ADK, the Claude Agent SDK) are excluded as general-purpose libraries unless orchestration is their core purpose; that is a maintainer judgment call, and none of them is listed today. General team workspaces, chat front ends, and single-agent wrappers are out of scope. Tracing, evals, and guardrails belong in [awesome-agent-observability](https://github.com/anhermon/awesome-agent-observability).

### Hosted and proprietary products

The main sections are open-source only and that bar does not change. A hosted or proprietary product can appear only in the separate "Hosted and proprietary products" section, never mixed into the open-source sections, when all of these hold:

- Coordinating several agents is a shipped, documented feature (agents hand off work, a lead supervises child agents, or agents run in parallel under one management surface), not a roadmap item or a keynote claim, and the product is generally available or in a public beta that anyone can join.
- It is at least 8 weeks past its public launch, and its public docs explain setup and usage.
- It has a dated changelog, release note, or documented update within the last 12 months, and no retirement notice.
- The entry says it is proprietary (and hosted or local) and says whether anything was run. What stays unchecked (isolation between agents, failure handling, data handling) is named in the section intro for every entry, and an entry that checked some of it says which. It describes behavior the docs state, not positioning, and names an account or plan only where the docs state one.
- It was checked from the vendor's public docs by someone outside the vendor. A hands-on trial is welcome where a free tier or trial exists; either way the entry says whether anything was run. The PR gives a dated source for each claim: the page URL, the date it was read, and the page's own date when it has one. The one exception to the outside-the-vendor check is a product the maintainer has explicitly decided to list under the self-listing rule below; its entry stays limited to what the vendor's public docs say, and the README names the exception.
- There are no vendor self-listings: a vendor, its employees, and its own agents do not submit the vendor's product. If the maintainer or an agent they run uses the product, the maintainer decides explicitly whether to list it and the PR records that decision.

Thresholds 1 to 6 and 9 to 10 apply as written, reading "repository" as "product page and docs". Threshold 7 becomes "the entry states it is proprietary". Threshold 8 becomes "read from the vendor's public docs, with a hands-on trial where practical, and the entry says whether anything was run", and the entry does not claim what was not checked. Single-user personal assistants and chat products that do not coordinate several agents are out of scope.

## Thresholds

These are the thresholds every entry is held to, at submission and at each audit.

| # | Threshold | Test | Action when it fails |
|---|-----------|------|----------------------|
| 1 | Alive | The link resolves (HTTP 200, or a redirect to the same project), points at the canonical repo, and the repository is not archived or disabled. | Fix the link if the project moved; remove if gone or archived. |
| 2 | Maintained | Last commit on the default branch is within 12 months. At 9 months without a commit it goes on the watch list. | Remove past 12 months. |
| 3 | Not end-of-life | No retirement, sunset, or maintenance-mode-only notice from the maintainers, even if commits continue. | Remove, citing the notice. |
| 4 | Old enough to judge | The project is at least 8 weeks old, counted from repository creation or first public release. | Decline; the author can resubmit once it passes. |
| 5 | Real docs | A README or docs site with install and usage steps. Mostly generated boilerplate does not count. | Decline or remove. |
| 6 | In scope | It coordinates, supervises, routes work to, or isolates coding or other agents (see "What belongs here"). | Decline, recategorize, or remove. |
| 7 | License stated | A license file in the repository, and the license named in the entry. Open-core (any `ee/` or `enterprise/` directory under a separate license), source-available, AGPL, and hosted-backend projects say so in the entry. | Fix the entry; decline if there is no license file. |
| 8 | Hands-on | You installed or built it, ran a task with a stub agent (a shell script is enough), and confirmed that work is isolated. Where the tool records runs, a failure must be recorded as a failure; session managers without run logs say so in the entry. A terminal multiplexer or session manager that has no file isolation of its own (isolation absent or opt-in) can be listed only if the entry says so. The PR says what you ran and what you could not check. | Decline. |
| 9 | One entry, one place | Each project appears once, in the category it best fits. | Merge or move. |
| 10 | Format | `- [Name](link) - What it actually does.` Sentence case, one line, one sentence, ends with a period, describes behavior rather than positioning, and names the license inside that sentence. Preview or alpha status is stated in the entry. No marketing words, no feature lists copied from a landing page. | Reword. |

Entries are roughly ordered by how central they are to the category, not alphabetically.

## How the list is maintained

A weekly workflow (`scripts/audit.py`) opens or updates one tracking issue listing entries whose repository is gone, archived, renamed, or past the 12-month bar (thresholds 1 and 2). A monthly hands-on pass re-runs entries with a stub agent and re-checks descriptions against the project (thresholds 3 to 10), which the script cannot do: sunset notices, licensing, scope, and whether the description is still true.

## Removals

Open an issue or pull request with evidence: last commit date, archive or sunset banner, redirect target, or a failing run.

## Process

1. Fork, add your entry, run `npx awesome-lint`.
2. Open a pull request using the template, with the evidence for each threshold: stars and age, last commit, license, and what you ran.
