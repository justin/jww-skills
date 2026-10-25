---
name: jww-issue-reconciliation
description: Reconcile tracked issues with implementation, pull requests, and established decisions. Use for backlog audits, release scope, missing work, stale blockers, or feature parity across repositories. Do not use for ordinary issue creation or a single implementation task.
---

# Issue Reconciliation

Determine whether the tracker accurately describes the work that remains.
Follow the project's definitions of scope, completion, and dependencies.
Keep project names, release criteria, and source locations in project guidance.

## Establish the Comparison

Identify the requested repositories, release or feature scope, and code baseline.
Use the requested revision; distinguish local work, open pull requests, merged
implementation, and deployed behavior. Record the revision and observation date
so the findings have a clear basis.

Read the relevant issue bodies and replies, linked pull requests and their
status, and available decision sources named by the project or request. Follow
links that could change scope or resolve an apparent blocker. Search existing
decisions before presenting a question as unanswered. If a source is
unavailable or decisions conflict, identify that gap rather than inventing a
resolution.

## Reconcile the Evidence

- Check claimed implementation against the owning source and relevant
  validation. A closed issue or merged pull request alone does not establish
  complete behavior, client integration, or deployment.
- Check whether an apparent gap is already covered by another issue, a
  follow-up, an open pull request, or an explicit deferral before proposing
  another ticket.
- For parity audits, compare user capabilities and acceptance criteria across
  clients. Different platforms need not have identical issue counts or UI.
- Separate missing implementation, pending validation, unresolved decisions,
  and tracker-only corrections. Keep excluded or deferred scope explicit.
- Distinguish hard prerequisites from coordination links and historical
  context. Use the tracker's native dependency relationships when available;
  do not substitute blocker labels for those relationships.

## Report or Apply Corrections

For each discrepancy, provide the issue or capability, observed state,
supporting source, and smallest useful correction. Group shared causes rather
than listing the same backend gap separately for every client. State which
repositories and sources were checked and which were unavailable.

An audit produces findings; apply tracker changes when the request includes
them. Before applying a correction, recheck the affected record for intervening
updates. Preserve unrelated fields and verify the resulting scope, links, and
dependencies. Close an issue only when its acceptance criteria are satisfied
or an established decision explicitly supersedes it.

Leave implementation, Git operations, and repository validation to their
existing workflows. Do not turn reconciliation into unrequested feature work.
