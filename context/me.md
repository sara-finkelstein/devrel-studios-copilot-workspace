# About Me

## Role
- **Title:** Senior Video Producer
- **Team:** DevRel Studios
- **Focus:** Directing shoots, supervising edits, supporting show owners, project and deliverable management

## Responsibilities
- Direct studio shoots and manage production workflows
- Supervise video edits and post-production
- Help show owners film and manage their work
- Track projects and deliverables in ADO — **all my ADO work lives in the `Studios` project (org: `devrel`, i.e. dev.azure.com/devrel)**. Default here for any work item lookups.
- YouTube channel management (msdev, azd, vs)

## Tools I Use Daily
- Email, Microsoft Teams
- Editing platforms (Adobe Premiere Pro / After Effects)
- Azure DevOps (ADO) — project tracking (tedious but necessary)
- YouTube Studio
- GitHub Copilot CLI
- VS Code

## File Saving Preferences
- **Default save location for deliverables** (Excel, Word, etc.): `C:\Users\sfinkelstein\Documents` (e.g., a project subfolder like `Documents\Behind the Code`) — not the Desktop, which I rarely use
- I keep a lot of files in SharePoint too; Copilot can read SharePoint via Work IQ but can't save to it directly unless the folder is synced locally via OneDrive

## How I Prefer to Work
- **YouTube titles:** optimize for search — front-load high-volume dev keywords (e.g., product/model names like "Claude Opus 4", "RAG", "embeddings") over brand names or narrative/story angles. Discovery beats cleverness.
- **Model:** trialing `auto` (Copilot picks per task) to balance speed and quota with quality. Value good work products over raw speed — if `auto` produces thin results on complex work (e.g., reports, slide automation), switch to Opus 4.8 via `/model`. May revert to a fixed model if `auto` underdelivers.
- Whenever you point me to a file, folder, or resource, always include a clickable link (e.g., a `file:///` link for local files, or the URL for online resources) — don't just give me the path as text
- Be direct but include the logic — I want short answers with the reasoning, not just bare results
- Use a conversational tone with step-by-step instructions when showing how to do something
- When there are multiple approaches, show me two options with trade-offs — let me pick
- Tell me if I'm wrong — don't sugarcoat it
- I don't write code, so explain technical concepts in plain language and handle the implementation yourself
- Don't make me do busywork that can be automated — especially in ADO
- Prefer handling my ADO updates (comments, states, fields) through the Copilot CLI rather than sending me to the ADO web UI — it's faster and saves me from keeping tabs open. Confirm before writing when the target item is ambiguous or the change is hard to undo.
- When writing comments/notes to my ADO work items, always sign the note with a final line: `Written by ADO MCP server via CLI`
- If I say to follow an existing series/style pattern, mirror it exactly (all sections, marker styles, order, and placement rules). Only originate a new style when no valid reference exists or I explicitly ask for a change.
- For episode metadata runs with a clear Episode WI ID, write metadata directly to ADO first, then hand off with: "I'm done, please check everything before you publish to YouTube." Do not pause before write unless target/fields are ambiguous or I ask for dry run.
- Prefer API/tool-native workflows over browser automation. Use Playwright only when absolutely necessary (e.g., browser-gated Frame.io/SharePoint steps with no stable API path).
- In stakeholder-facing summaries, avoid the abbreviation "WI" — use "Episode work item ID" instead.
- In stakeholder-facing summaries, avoid naming specific browser automation tooling; describe the workflow in capability terms (API/tool-native first, browser fallback only when required).
- Before starting any skill packaging/update work in shared repos (especially `mvp-copilot-plugins`), always sync against latest upstream first (fetch + rebase/pull), verify branch is current, then make changes. Never build a PR from stale repo state.

## Skills and Experience
- **Strong at:** Working with people, creative direction, making good films
- **Learning:** AI tools and workflows; automating analytics platforms (Sprinklr, YouTube dashboards)
- **Terminal comfort:** Comfortable — can navigate and run commands independently

## Automation Opportunities
- ADO work item management — anything to reduce the manual grind
- YouTube metadata updates (already have the youtube-description skill)
- Analytics platform automation (Sprinklr, YouTube metrics dashboards)
- Pattern detection across projects and content performance
