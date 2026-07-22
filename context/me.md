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

## People I Work With
- **Manager:** Golnaz Alibeigi

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
- **Voice profile caution:** always show drafts using the Teams/chat voice profile before sending anything — don't auto-send. The profile is based on a small sample of messages, so don't let a few examples get over-magnified into "rules." Treat it as a loose guide, adjust per Sara's feedback each time, and confirm before locking in any tone she hasn't explicitly signed off on.
- **Writing tone/voice:** default to informal, plain language, minimal jargon — that's how I actually talk. Reserve clear/halfway-formal "corporate" tone only for content going to executives or their assistants (e.g., exec-facing emails, invites to senior stakeholders). Don't default to formal corporate-speak for everyday drafts, Teams messages, or internal notes.
- **YouTube titles:** optimize for search — front-load high-volume dev keywords (e.g., product/model names like "Claude Opus 4", "RAG", "embeddings") over brand names or narrative/story angles. Discovery beats cleverness.
- **Model:** trialing `auto` (Copilot picks per task) to balance speed and quota with quality. Value good work products over raw speed — if `auto` produces thin results on complex work (e.g., reports, slide automation), switch to Opus 4.8 via `/model`. May revert to a fixed model if `auto` underdelivers.
- Whenever you point me to a file, folder, or resource, always include a clickable link (e.g., a `file:///` link for local files, or the URL for online resources) — don't just give me the path as text
- Be direct but include the logic — I want short answers with the reasoning, not just bare results
- Use a conversational tone with step-by-step instructions when showing how to do something
- When there are multiple approaches, show me two options with trade-offs — let me pick
- Tell me if I'm wrong — don't sugarcoat it
- I don't write code, so explain technical concepts in plain language and handle the implementation yourself
- Don't make me do busywork that can be automated — especially in ADO
- Proactively alert me once daily about publishing dates that are 2 days away or less across my projects
- Prefer handling my ADO updates (comments, states, fields) through the Copilot CLI rather than sending me to the ADO web UI — it's faster and saves me from keeping tabs open. Confirm before writing when the target item is ambiguous or the change is hard to undo.
- When writing comments/notes to my ADO work items, always sign the note with a final line: `Written by ADO MCP server via CLI`
- If I say to follow an existing series/style pattern, mirror it exactly (all sections, marker styles, order, and placement rules). Only originate a new style when no valid reference exists or I explicitly ask for a change.
- For episode metadata runs with a clear Episode WI ID, write metadata directly to ADO first, then hand off with: "I'm done, please check everything before you publish to YouTube." Do not pause before write unless target/fields are ambiguous or I ask for dry run.
- Prefer API/tool-native workflows over browser automation. Use Playwright only when absolutely necessary (e.g., browser-gated Frame.io/SharePoint steps with no stable API path).
- In stakeholder-facing summaries, avoid the abbreviation "WI" — use "Episode work item ID" instead.
- In stakeholder-facing summaries, avoid naming specific browser automation tooling; describe the workflow in capability terms (API/tool-native first, browser fallback only when required).
- Before starting any skill packaging/update work in shared repos (especially `mvp-copilot-plugins`), always sync against latest upstream first (fetch + rebase/pull), verify branch is current, then make changes. Never build a PR from stale repo state.
- **Standing instruction — installing/updating plugins from `microsoft/mvp-copilot-plugins` (private repo):** `copilot plugin marketplace add microsoft/mvp-copilot-plugins` fails (`fatal: unable to get password from user`) because Copilot's internal clone doesn't inherit the git credential-manager config, even though `gh auth setup-git` is set up. Workaround, and the standing procedure to use automatically whenever this marketplace needs adding or refreshing (e.g., after Golnaz or anyone shares a new plugin link from this repo): (1) `gh repo clone microsoft/mvp-copilot-plugins <temp-path>` (or `git -C <temp-path> pull` if already cloned) to get/refresh a local copy using `gh`'s working auth, (2) `copilot plugin marketplace add <temp-path>` (local path, not `OWNER/REPO`) to register/refresh it, (3) `copilot plugin install <plugin-name>@mvp-copilot-plugins` to install/update the specific plugin. Do this proactively without being asked again whenever a new mvp-copilot-plugins link/plugin comes up or an already-installed one needs updating.
- **Standing instruction — keep skills reference table current:** every time a `mvp-copilot-plugins` freshness/sync check runs (see repo freshness rule below), also refresh the "What to say → which skill fires" table in `context/references.md` to match whatever's actually installed at that moment (added/removed/renamed skills, new plugins like `github-workflow`). Don't wait to be asked.
- **Standing instruction — repo freshness auto-check (Sara is not a coder, don't rely on her to know/ask for this):** Any time work touches a local clone of a shared repo Sara doesn't own outright (especially `mvp-copilot-plugins`, and her personal fork of it at `C:\Users\sfinkelstein\mvp-copilot-plugins`), proactively check freshness *before* starting work, without being asked: confirm `origin` vs `upstream` remotes exist and diff, `git fetch` both, and if her fork/local branch is behind real upstream, sync it (push `upstream/main` → fork `main`, rebase her working branch) before any packaging/PR/demo work. Surface only genuine content conflicts for her decision — never resolve shared-file conflicts unilaterally. Explain any git concept in plain language each time (she doesn't know git terminology) rather than assuming familiarity. This directly caused a "wrong repo version" incident with her manager Golnaz on 7/15 — treat prevention of repeat incidents as a priority.

## My Teams/Chat Voice (for informal drafts)
Pulled from real Teams messages (7/21) to calibrate casual writing:
- Conversational, close to spoken language — not email-formal
- Softeners: "yah", "ah", "hey", "all good", "no worries"
- Self-deprecating humor shows up often ("if i were a video game character, i'd need a power pill")
- Generous exclamation points, used for warmth not urgency
- Thinks out loud — shares reasoning, not just conclusions ("hmmm... let's chat about that before we finalize")
- Shorthand/informal punctuation: "w/", "atm", trailing "....", double "!!"
- Thanks people a lot, reassures, offers help unprompted
- Coaching tone with colleagues — asks follow-ups, explains process rather than just directing
- **Don't over-apologize, but context is welcome.** When something's on me (late scheduling, a delay, a mistake), skip repeated "sorry"s — one clean acknowledgment of ownership is enough. But DO keep the "why" when it matters: reassures people they're not deprioritized/it's not personal ("team's maxed right now"), explains a real cause worth knowing, or helps prevent it next time. People who understand the why are more likely to be flexible — it shows we're juggling a lot, not being careless or dismissive. That's context, not an excuse. Just don't stack apology after apology on top of it.
- Examples: "I can!" / "aHA! It's not me messing up ADO this time...." / "ah no worries!! just send it out. All good!"

## Skills and Experience
- **Strong at:** Working with people, creative direction, making good films
- **Learning:** AI tools and workflows; automating analytics platforms (Sprinklr, YouTube dashboards)
- **Terminal comfort:** Comfortable — can navigate and run commands independently

## Automation Opportunities
- ADO work item management — anything to reduce the manual grind
- YouTube metadata updates (already have the youtube-description skill)
- Analytics platform automation (Sprinklr, YouTube metrics dashboards)
- Pattern detection across projects and content performance
