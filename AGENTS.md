# Repository Guidelines

## Project Structure

This repository contains reusable Codex skills. Each skill lives in its own
directory under `skills/` and contains:

- `SKILL.md`: the skill's instructions and front matter.
- `agents/openai.yaml`: display metadata for the Codex skill picker.
- `assets/`: optional icons and other packaged visual assets.
- `references/`: optional detail loaded only for the applicable mode or task.
- `prompts/<harness>/`: optional invocation wrappers for a harness whose
  slash-command format differs from `SKILL.md`.
- `hooks/`: optional harness-specific scripts that automate the skill.
- `INSTALL.md`: required when a skill ships `prompts/` or `hooks/`.

Keep `SKILL.md` the single source of the procedure. A wrapper in `prompts/`
selects a mode and points at the skill; it must not restate the procedure.
Confine harness-specific configuration to `hooks/` and `INSTALL.md` so the
skill body stays tool-neutral.

Keep files belonging to a skill within `skills/<directory-name>/`. Use
lowercase, hyphenated directory names prefixed with `jww-`, such as
`jww-swift-style`. The front-matter `name` must match the directory name. Place
images and similar resources in `assets/`, and reference packaged resources
with paths relative to the skill directory.

## Authoring Skills

Write `SKILL.md` in Markdown with YAML front matter containing at least `name`
and `description`. Make the description precise about when the skill applies
and when it does not. Organize instructions under short headings, favor
actionable rules, and include examples only where they eliminate ambiguity.

The Agent Skills spec defines six front-matter fields: `name`, `description`,
`license`, `compatibility`, `metadata`, and `allowed-tools`. Claude Code
accepts many more, such as `argument-hint`, `when_to_use`, `paths`, `model`,
and `effort`.

Filesystem distribution, which is how these skills are installed, does not
validate front matter, so a Claude Code field is worth using when it improves
that harness. The cost is confined to three publishing paths: claude.ai
uploads, the Skills API, and `package_skill.py` reject an unlisted field with a
hard error rather than ignoring it. Keep a skill to the six spec fields only
when it needs to publish that way, which includes enabling it for Cowork and
cloud sessions.

Other harnesses are expected to ignore front matter they do not recognize, but
this is unverified. Keep anything a skill depends on for correct behavior in
the body rather than in a harness-specific field, and put harness-specific
invocation details in a `prompts/<harness>/` wrapper.

Put the key use case at the start of the `description`. A listing that
overflows its budget is shortened from the end, and each entry is capped at
1,536 characters regardless.

Set `name` to match the directory name. For a personal or project skill the
invoked command comes from the directory, and `name` only sets the display
label, so a mismatch produces a skill whose listed name and command differ.

Keep skill guidance specific to its domain. Do not duplicate general safety,
Git, or contributor guidance that is supplied by the hosting environment.
Ensure instructions remain tool-neutral unless a particular tool is required.

## Style and Naming

Use clear American English, direct imperative language, and wrapped Markdown
paragraphs. Use fenced blocks with a language tag for code or configuration.
Preserve the existing YAML style: two-space indentation, quoted display text,
and relative asset paths. Name files by their role (`SKILL.md`, `openai.yaml`)
rather than introducing alternate spellings.

## Validation

There is no build or test runner in this repository. Before submitting a
change, review each edited file for valid Markdown and YAML, verify referenced
asset paths exist, and confirm the front-matter `name` matches the skill
directory's intended identifier. Check the working tree with `git diff --check`
to catch whitespace errors.

## Commits and Pull Requests

The repository has no commit history yet, so use the shared convention: a
focused, capitalized, present-tense subject of at most 50 characters (for
example, `Add Swift style skill`). Keep commits limited to one skill or one
cohesive metadata change. Pull requests should explain the skill's purpose,
list validation performed, link the relevant issue when applicable, and include
screenshots only when picker metadata or visual assets change.
