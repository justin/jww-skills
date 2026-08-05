# JWW Skills

Reusable Codex skills for JWW projects. Each skill is a self-contained
directory whose runtime instructions are in `SKILL.md`.

## Installation

Install the Swift style skill globally with the Skills CLI:

```sh
npx skills add justin/jww-skills \
  --skill jww-swift-style \
  --agent codex \
  --global
```

```sh
npx skills add justin/jww-skills --list
```

For a manual installation, copy the desired skill directory into your agent
harness's skills directory, preserving its internal structure:

```sh
cp -R skills/jww-swift-style /path/to/your/skills/jww-swift-style
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

### JWW Swift Style

[`skills/jww-swift-style/`](skills/jww-swift-style/) guides Swift changes across
JWW projects, including application and package code, extensions, and tests.
It is a personal style companion, not a platform-specific implementation guide.

It treats the target file, nearby source, and applicable `AGENTS.md` files as
the authority. Its defaults cover source layout, access control, SwiftLint
limits, platform boundaries, and test conventions.

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
