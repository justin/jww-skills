# Apply Cleanup

Read this reference only after the user has requested Apply mode. Resolve the
authorized cleanup categories and exact targets before changing state.

## Back Up Affected State

1. Resolve a timestamped backup directory outside the live source directories
   and confirm that it has enough free space.
2. Back up only the state the authorized cleanup can affect, plus the config and
   indexes needed to restore it. Record source paths, sizes, timestamps, and
   checksums in a manifest.
3. Do not copy authentication credentials unless the user specifically requests
   an encrypted credential backup.
4. When a database is live, use a supported backup operation. Otherwise require
   Codex to be closed and copy the database with its relevant sidecars.
5. Verify that the backup can be read before changing the source.

If the desktop app is open, limit cleanup to supported task or scheduled-run
operations. For log rotation or direct app-owned file movement, provide the
offline runbook and wait for the user to quit the app or continue from a
separate CLI session.

## Apply Authorized Categories

- For a large task that must remain resumable, use `jww-handoff` when available
  and verify the handoff against current source before archiving the task.
- Archive tasks and scheduled runs through host-supported operations. Preserve
  pinned tasks.
- Archive app-managed worktrees through their owning task or run. For ordinary
  Git worktrees, inspect `git worktree list --porcelain` and
  `git worktree prune --dry-run`; do not move worktree directories manually.
- With Codex stopped, move rotatable logs into the backup directory and leave
  the expected live log directory in place. Prefer rotation or compression to
  deletion.
- Patch dead project entries only in the documented config source. Preserve
  unrelated settings and comments, then parse the resulting configuration.

Do not remove a repository worktree or patch a distinguishable configuration
entry unless the user authorized that exact target. Do not delete the backup as
part of the cleanup; report its location and ask the user to choose its
retention after verification.
