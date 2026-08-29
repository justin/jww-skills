# Automate the Audit

Read this reference only when the user requests a scheduled or recurring Codex
maintenance report.

Create or update an automation through the host-supported operation. Keep the
recurring work read-only: inventory sizes and counts, identify archival
candidates, flag large logs and stale worktrees, and return a report for review.
Test the audit prompt manually before scheduling it.

State the local execution constraints that apply to the selected automation.
Local projects require the relevant computer and Codex environment to be
available, and frequent runs may create additional worktrees or task history.

Do not schedule offline log rotation, database copying, task archival, or other
cleanup. Those actions belong in an explicitly authorized interactive Apply
run.
