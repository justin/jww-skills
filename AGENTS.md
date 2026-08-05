# Repository Guidelines

## Project Structure

This repository contains reusable Codex skills. Each skill lives in its own
directory under `skills/` and contains:

- `SKILL.md`: the skill's instructions and front matter.
- `agents/openai.yaml`: display metadata for the Codex skill picker.
- `assets/`: optional icons and other packaged visual assets.

Keep files belonging to a skill within `skills/<directory-name>/`. Use
lowercase, hyphenated directory names prefixed with `jww-`, such as
`jww-swift-style`. The front-matter `name` must match the directory name. Place
images and similar resources in `assets/`, and reference them with paths
relative to the skill directory.

## Authoring Skills

Write `SKILL.md` in Markdown with YAML front matter containing at least `name`
and `description`. Make the description precise about when the skill applies
and when it does not. Organize instructions under short headings, favor
actionable rules, and include examples only where they eliminate ambiguity.

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
