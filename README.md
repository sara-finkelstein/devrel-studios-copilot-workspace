# DevRel Studios — Copilot Workspace Template

Personal AI-assisted workspace for the DevRel Studios team. Clone this repo to get started with GitHub Copilot CLI, personal context, and shared team skills.

## Quick Start

1. **Use this template** — click "Use this template" on GitHub to create your own copy
2. **Clone your copy** locally
3. **Open in VS Code** — the `.vscode/` config is already wired up
4. **Run the setup interview** — open `skills/setup-interview.md`, copy the prompt into Copilot Chat, and answer the questions. It builds your `context/me.md` for you.
5. **Start using Copilot CLI** — `gh copilot suggest`, `gh copilot explain`

You don't need to fill anything in manually — the setup interview does it for you.

## How It Works

The `.github/copilot-instructions.md` file is automatically loaded by Copilot every session. It tells Copilot:
- Who you are and what you work on (from your `context/` files)
- How to behave and communicate
- To automatically save things it learns about you back to your context files

You don't need to manually maintain your context — Copilot updates it as you work. But you can always edit the files directly if you want.

## Structure

```
.github/
  copilot-instructions.md   <- auto-loaded by Copilot (don't delete)
context/
  me.md                     <- your role, tools, preferences
  projects.md               <- what you're working on
  learnings.md              <- tips and patterns you've picked up
  references.md             <- links, docs, resources you use
skills/
  README.md                 <- how to use and contribute skills
.vscode/
  settings.json             <- Copilot config
  extensions.json           <- recommended extensions
```

## Shared Skills

Team skills live in the [studio-copilot-skills](TODO) repo. You can reference them from here or copy ones you use frequently into your local `skills/` directory.
