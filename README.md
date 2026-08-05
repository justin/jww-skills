# JWW Skills

Reusable Codex skills for JWW projects. Each skill is a self-contained
directory whose runtime instructions are in `SKILL.md`.

## Installation

Install a skill globally with the Skills CLI, replacing `<skill-name>` with its
installed skill identifier:

```sh
npx skills add justin/jww-skills \
  --skill <skill-name> \
  --agent codex \
  --global
```

Available skills are `jww-git-workflow`, `jww-repository-validation`, and
`jww-swift-style`.

```sh
npx skills add justin/jww-skills --list
```

For a manual installation, copy the desired skill directory into your agent
harness's skills directory, preserving its internal structure:

```sh
cp -R skills/<directory-name> /path/to/your/skills/<skill-name>
```

Restart the agent session or reload installed skills after copying it. The
`SKILL.md` file is required; `agents/openai.yaml` and `assets/` provide Codex
picker metadata and its icon.

## Usage

Invoke an installed skill by name. For example, use the Swift style skill in a
Codex prompt:

```text
Use $jww-swift-style to implement this Swift change.
```

| Installed name | Directory | Purpose |
| --- | --- | --- |
| `jww-git-workflow` | [`skills/jww-git-workflow/`](skills/jww-git-workflow/) | Safe Git, pull-request, and publishing workflows. |
| `jww-repository-validation` | [`skills/jww-repository-validation/`](skills/jww-repository-validation/) | Proportionate validation for repository changes. |
| `jww-swift-style` | [`skills/jww-swift-style/`](skills/jww-swift-style/) | JWW Swift style conventions for application, package, extension, and test code. |

## Adding a Skill

Create a lowercase, hyphenated directory under `skills/`, such as
`skills/jww-swift-style/`, with this structure:

```text
skills/skill-name/
├── SKILL.md            # Instructions and YAML front matter
├── agents/openai.yaml  # Optional Codex picker metadata
└── assets/             # Referenced icons and other resources
```

Include `name` and `description` in `SKILL.md` front matter. State when the
skill applies and when it does not. Keep instructions domain-specific,
actionable, and tool-neutral unless a tool is required.

## Validation

Review changed Markdown and YAML, confirm referenced assets exist, then run:

```sh
git diff --check
```

See [AGENTS.md](AGENTS.md) for contribution conventions.
