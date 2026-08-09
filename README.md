# JWW Skills

Reusable agent skills for JWW projects. Each skill is a self-contained
directory whose runtime instructions are in `SKILL.md`.

## Installation

Install a skill globally with the Skills CLI, replacing `<skill-name>` with its
installed skill identifier. Repeat `-a` for each agent; a comma-separated list
is rejected:

```sh
npx skills add justin/jww-skills \
  --skill <skill-name> \
  -a claude-code -a codex -a github-copilot \
  --global
```

`jww-codex-maintenance` is Codex-only. Install it separately with only the
Codex target; its `compatibility` field documents the requirement but does not
replace agent-specific installation:

```sh
npx skills add justin/jww-skills \
  --skill jww-codex-maintenance \
  -a codex \
  --global
```

Skills install to `~/.agents/skills/<skill-name>/` and are wired into each
agent's own skills directory from there. The whole directory is preserved, so
any `prompts/` and `hooks/` a skill ships arrive with it. Run
`npx skills add justin/jww-skills -a <agent> --list` to see the agents the CLI
supports, and `npx skills update` to refresh installed skills.

Install from a local checkout to test a skill before it is pushed:

```sh
npx skills add . --skill <skill-name> -a claude-code --global
```

Available skills are `jww-bounded-investigation`, `jww-codex-maintenance`,
`jww-git-workflow`, `jww-handoff`, `jww-repository-validation`, and
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

Invoke an installed skill by name. In Claude Code, skills and slash commands
are the same mechanism, so a skill is invocable directly:

```text
/jww-swift-style
```

In Codex, reference the skill in a prompt:

```text
Use $jww-swift-style to implement this Swift change.
```

An agent also loads a skill on its own when the request matches the skill's
`description`, unless the skill's front matter restricts that.

| Installed name | Directory | Purpose |
| --- | --- | --- |
| `jww-bounded-investigation` | [`skills/jww-bounded-investigation/`](skills/jww-bounded-investigation/) | Evidence ledger and search delegation for multi-file investigation. Pairs with `jww-handoff`. |
| `jww-codex-maintenance` | [`skills/jww-codex-maintenance/`](skills/jww-codex-maintenance/) | Codex-only local-state audits, reversible cleanup, and maintenance reporting. |
| `jww-git-workflow` | [`skills/jww-git-workflow/`](skills/jww-git-workflow/) | Safe Git, pull-request, and publishing workflows. |
| `jww-handoff` | [`skills/jww-handoff/`](skills/jww-handoff/) | Canonical handoff file for work spanning sessions or phases. See its [`INSTALL.md`](skills/jww-handoff/INSTALL.md) for slash-command and hook setup. |
| `jww-repository-validation` | [`skills/jww-repository-validation/`](skills/jww-repository-validation/) | Proportionate validation for repository changes. |
| `jww-swift-style` | [`skills/jww-swift-style/`](skills/jww-swift-style/) | JWW Swift style conventions for application, package, extension, and test code. |

## Adding a Skill

Create a lowercase, hyphenated directory under `skills/`, such as
`skills/jww-swift-style/`, with this structure:

```text
skills/skill-name/
├── SKILL.md            # Instructions and YAML front matter
├── INSTALL.md          # Required when shipping prompts/ or hooks/
├── agents/openai.yaml  # Optional Codex picker metadata
├── prompts/<harness>/  # Optional per-harness invocation wrappers
├── hooks/              # Optional harness-specific automation scripts
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
