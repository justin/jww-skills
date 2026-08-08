---
name: handoff
description: Write or resume the canonical work handoff.
agent: agent
argument-hint: "mode=write|resume slug=<task-slug>"
---

Follow the procedure in the `jww-handoff` skill, reading it first if it is not
already in context. It is installed at `~/.agents/skills/jww-handoff/SKILL.md`.

Mode: `${input:mode:write or resume}`. Task slug: `${input:slug:task slug, or
infer from the branch}`.

In `resume` mode, read the existing handoff and verify it against the branch,
the working tree, and each file it claims to have changed before reading other
source. In `write` mode, create or update the handoff using the template in the
skill, and state the file path you wrote.
