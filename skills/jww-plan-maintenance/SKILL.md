---
name: jww-plan-maintenance
description: Reconcile existing execution plans with delivered work and outstanding acceptance. Use to audit active plans, archive completed plans, consolidate duplicate tracking, or identify the next useful slice. Do not use to author a new implementation plan or capture a session handoff.
---

# Plan Maintenance

Keep execution plans accurate enough to guide the next piece of work. Follow
the repository's plan format, lifecycle, and archive conventions; do not
introduce a parallel planning system.

## Establish Actual State

Read the relevant plans and their linked issues, pull requests, and decisions.
Check completion claims against the requested code baseline and recorded
validation. Distinguish work on a branch from work merged or deployed. Identify
missing evidence as uncertainty rather than treating an unchecked box as proof
that implementation is absent.

If issue status or scope needs substantial reconciliation, use
`jww-issue-reconciliation` when available. Keep this workflow focused on what
the resulting evidence means for the planning documents.

## Reconcile the Plans

- Mark completed work with its supporting revision, pull request, or check.
  Preserve decision rationale that still explains the implementation.
- Separate unfinished implementation from acceptance checks, external
  dependencies, and deferred scope. A local passing check does not satisfy
  device, integration, or deployment acceptance it did not exercise.
- Archive a plan when its agreed completion criteria are met. When the
  repository permits remaining work to move to an issue or another plan,
  retain a durable link and explain the disposition before archiving.
- Consolidate duplicate tracking into the existing canonical issue or plan.
  Preserve unique requirements and evidence, and update references to the
  surviving record so readers following old references still find the remaining
  work. Do not create a second ledger of the same work.
- Remove obsolete tasks only when implementation evidence or an established
  scope decision makes them obsolete. Age, inconvenience, or an apparently
  minor verification step is not enough to waive acceptance.

Apply document cleanup when requested; for a status-only question, report the
needed corrections. Do not silently change product scope or close linked
issues merely because a planning document is archived.

## Identify the Next Slice

When requested, recommend the smallest independently useful outcome supported
by existing decisions. State the behavior it delivers, the actual prerequisite,
and what it unblocks. Separate optional cleanup from that outcome. Check linked
discussions before asking for a decision that may already have been made.

Report which plans were archived, consolidated, or left active and why, with
the evidence gaps and remaining acceptance made explicit. Use `jww-handoff`
for session continuity when needed; do not copy its session record into every
plan. Follow the existing Git and validation workflows for document changes.
