# Skills

Reusable prompts and workflows for common tasks. Each skill is a markdown file with a structured prompt you can give to Copilot.

## How to Use a Skill

1. Open the skill file
2. Copy the prompt (or reference it by name if Copilot has context)
3. Paste into Copilot CLI or VS Code Copilot Chat
4. Fill in any `[placeholders]` with your specifics

## How to Create a Skill

Create a new `.md` file in this directory with:

```markdown
# Skill Name

## What it does
[One-line description]

## When to use it
[What situation triggers this skill]

## Prompt
[The actual prompt to give Copilot — include placeholders for variable parts]

## Example
[A filled-in example so people can see how it works]
```

## Contributing to Team Skills

If you build a skill that others would find useful, add it to the [studio-copilot-skills](TODO) repo so the whole team can use it.
