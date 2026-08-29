---
name: jww-codex-maintenance
description: Audit and reduce Codex desktop and CLI local-state bloat without deleting history or editing private app state. Use when Codex feels slow, logs or sessions consume substantial disk space, stale task worktrees accumulate, configuration contains dead project paths, or the user wants a repeatable maintenance report. Default to a read-only audit; perform archival or rotation only when the user explicitly requests cleanup.
compatibility: >-
  Requires OpenAI Codex in the ChatGPT desktop app or Codex CLI; not intended
  for Claude Code, GitHub Copilot, or other agent harnesses.
---

# Maintain Codex Local State

## Xcode Availability

This skill is unavailable in Xcode. Its procedure depends on Codex Desktop or
CLI local state and supported Codex task-management operations, which Xcode
does not provide. Use it only in a Codex harness.

Separate diagnosis from cleanup. Large local state can correlate with a slow app,
but do not treat file size as proof of the cause or promise a speedup.

## Never

- Simulate archival by moving session JSONL files or editing the local-state
  database.
- Vacuum, rebuild, edit, or replace a Codex database without an explicit repair
  request backed by an official procedure.
- Kill background processes, language servers, or dev servers. Report them and
  let the user decide.
- Copy transcripts, logs, memories, config, databases, or credentials to a
  repository, shared folder, or cloud-synced location without explicit approval.
- Mutate live Codex files on a schedule.

## Select the Mode

Default to **Audit**. Switch only on an explicit request: the user says "clean
up", "rotate", "archive", or "delete" for **Apply**; "schedule" or "recurring
report" for **Automate**. Treat "make Codex faster" as an audit request, not
permission to mutate state.

- **Audit**: inspect and report without changing tasks, files, configuration,
  processes, or scheduled tasks.
- **Apply**: read [references/apply.md](references/apply.md), resolve the exact
  targets, and perform only the cleanup authorized by the user's request. When
  the request authorizes a category but not distinguishable targets within it,
  present those targets and obtain approval before changing them.
- **Automate**: create a recurring read-only audit and report.
  Read [references/automation.md](references/automation.md) before scheduling.

If the request is ambiguous, complete the audit and stop with a proposed cleanup
set.

## Inventory the Current State

1. Resolve `CODEX_HOME` from the environment when it is set; otherwise use
   `~/.codex`. Do not redefine `HOME`, `CODEX_HOME`, or another common system
   variable in shell commands.
2. Determine whether the desktop app, Codex CLI, scheduled runs, or other Codex
   processes are active. Report them; do not stop them automatically.
3. Record sizes, file counts, oldest and newest modification times, and largest
   files for:
   - active and archived session transcripts
   - Codex and desktop-app logs
   - app-managed and Git worktrees
   - configuration and profile files
   - local databases and their `-wal` and `-shm` sidecars
   - memories, skills, plugins, and scheduled-task metadata when present
4. Use host-supported task operations to list task status, pinning, age, and
   project association when available. Do not infer pinning or task state by
   rewriting an index or querying an undocumented database schema.
5. Inspect heavy development processes, especially long-lived language servers
   and dev servers, but report their command, working directory, age, and memory
   use instead of killing them.

On macOS, include `~/Library/Logs/com.openai.codex/YYYY/MM/DD`. Codex session
transcripts normally live in `$CODEX_HOME/sessions`, archived transcripts in
`$CODEX_HOME/archived_sessions`, and CLI logs in `$CODEX_HOME/log`. Discover
other locations from the running installation rather than assuming a private
layout.

## Classify Candidates

Classify each item and explain the evidence:

- **Task archival:** old, unpinned, inactive tasks with no running work. Treat an
  age threshold such as 7–10 days as a user preference, not a universal rule.
- **Large active task:** an unusually large transcript that may benefit from a
  handoff and a fresh task. Size alone does not make it safe to archive.
- **Scheduled-run worktree:** an old unpinned run whose task can be archived
  through the app. Frequent scheduled tasks can intentionally create many
  worktrees.
- **Repository worktree:** clean, unused, and associated with completed work.
  Confirm its branch and repository ownership before proposing removal.
- **Rotatable log:** an old or oversized log that is not currently being
  written.
- **Dead configuration path:** a configured project path that does not exist.
  Distinguish temporarily unavailable volumes from genuinely obsolete paths.
- **Path alias:** two spellings that resolve to the same location. On Windows,
  compare regular and extended-length paths canonically, but do not rewrite app
  state merely to normalize display text.

Exclude pinned tasks, running or otherwise active work, dirty worktrees, current
logs, and uncertain paths from cleanup. When the host cannot expose one of
those states, classify the target as uncertain rather than inferring that it is
safe.

## Verify and Report

Repeat the inventory and compare it with the baseline. Verify, as applicable:

- configuration still parses
- databases open read-only and pass a non-mutating integrity check
- intended tasks or scheduled runs are archived and pinned tasks are unchanged
- active-session bytes fell only by the intended archival amount
- archived-session bytes and counts changed consistently
- worktrees still registered with Git exist, and no dirty worktree was removed
- live log directories exist and fresh logs can be created after relaunch
- path-alias and dead-path findings are resolved without unrelated config edits

Ask the user to relaunch the desktop app and confirm the sidebar, active tasks,
scheduled tasks, and normal startup. Report measured disk-space changes
separately from perceived performance; never repeat an anecdotal “10x faster”
claim as an expected result.

The final report must include the mode, baseline, candidate set, excluded items,
exact changes, validation results, and remaining risks. In Apply mode, also
include the backup location, restore instructions, and the user-selected backup
retention or review decision; do not delete the backup implicitly.
