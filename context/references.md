# References

## References

## Team Resources
- [Copilot Workspace Template](https://github.com/camerontomisser2/devrel-studios-copilot-workspace) — Cameron's original template
- [My Workspace Fork](https://github.com/sara-finkelstein/devrel-studios-copilot-workspace) — personal fork
- [mvp-copilot-plugins](https://github.com/microsoft/mvp-copilot-plugins) — shared skills repo (youtube-description skill, PR #78)
- Team skills repo — TBD (will live under manager's GitHub)

## DevRel Studios Plugin (installed skills)
- Source: [mvp-copilot-plugins/plugins/devrel-studios](https://github.com/microsoft/mvp-copilot-plugins/tree/main/plugins/devrel-studios)
- Skills installed in `~/.copilot/skills/`: aka-redirect, create-event-episodes, create-studio-support, send-calendar-invite, video-staging, view-to-tam, vtt-metadata, youtube-analysis, youtube-collaborator, youtube-description, youtube-monthly-watchhours
- Shared scripts (plugin root): `~/.copilot/plugins/devrel-studios/scripts/` — parse-vtt.py, download-comments.py, download-playlist.py
- The `<PLUGIN_ROOT>` placeholder in vtt-metadata & youtube-analysis SKILL.md was patched to that absolute path
- Local `create-event-episodes` is extended to support Shows as well as Events. For FTTF FY27 it inherits the Show template and uses Matt Scholz as Technical Director; reapply this local extension after plugin refreshes until it is upstream.
- Requires `yt-dlp` (installed) — youtube-analysis scripts call `python -m yt_dlp`
- ADO MCP server (`ado`) from the plugin's `.mcp.json` is already configured in `~/.copilot/mcp-config.json`
- To update skills: re-download from the repo and re-patch `<PLUGIN_ROOT>`

### Sara's Skill Publication Tracker

Keep this table current when a skill is submitted, merged, superseded, or retired.

| Skill | What it does | Current status |
|---|---|---|
| `complete-project-ingestion` | Takes an approved ADO Proposal through project automation, detailed production intake, Episode creation, and verification of generated child tasks. | [Draft PR #224](https://github.com/microsoft/mvp-copilot-plugins/pull/224) — open, not merged |
| `create-episode-metadata-from-transcripts` | Generates a complete YouTube metadata package from a transcript, matches the series' established style, and writes the external metadata fields to the ADO Episode. | [PR #218](https://github.com/microsoft/mvp-copilot-plugins/pull/218) — open, not merged |
| `mvp-unplugged-links` | Extracts episode resource and speaker-social links from the shared MVP Unplugged PowerPoint deck and writes them to the ADO Episode. | Included in [PR #218](https://github.com/microsoft/mvp-copilot-plugins/pull/218) — open, not merged |
| `production-schedule` / `fabric-production-schedule` | Builds reusable production-schedule presets for the team; Sara's personal Fabric preset manages FTTF/FEI timelines, Graph-synchronized Outlook entries, review drafts, V2 reminders, publishing alerts, and an exception-only control tower. | Team version: [Draft PR #230](https://github.com/microsoft/mvp-copilot-plugins/pull/230) — updated 8/21 with a durable external-scheduler contract, health checks, catch-up, overlap protection, bounded retries, and logs. Personal preset: [open skill](file:///C:/Users/sfinkelstein/.copilot/skills/fabric-production-schedule/SKILL.md) |
| `content-autopsy` | Pulls retention, traffic sources, subscriber conversion, and core YouTube metrics for one video, with optional thumbnail impressions and CTR from a Studio CSV. | Local only — [open skill](file:///C:/Users/sfinkelstein/.copilot/skills/content-autopsy/SKILL.md) |
| `video-chapters` | Transcribes a local video, identifies topic changes, generates timestamped YouTube chapters, and can save them to the ADO Episode. | Local only — [open skill](file:///C:/Users/sfinkelstein/.copilot/skills/video-chapters/SKILL.md) |
| `ado-add-note` | Finds the correct Studios ADO work item from an ID or description and posts a signed discussion note after resolving any ambiguity. | Workspace-only and intentionally personal — [open skill](file:///C:/Users/sfinkelstein/devrel-studios-copilot-workspace/skills/ado-add-note.md) |

### What to say → which skill fires (kept current during repo sync checks)
Skills trigger automatically from natural language — no need to name them. Table below is refreshed each time a `mvp-copilot-plugins` sync/freshness check runs, so it always reflects what's actually installed.

| If you say something like... | Skill that kicks in | What you need to provide (starting point) |
|---|---|---|
| "Book studio time" / "schedule a recording" | create-studio-support | Speaker name, studio stage (A/B/C), start time |
| "Create episodes for this event" / paste a session list | create-event-episodes | The ADO Event ID + a pasted Topic/Speaker table, Loop doc, Excel export, or run-of-show |
| "Stage this video" / "upload to msdev" | video-staging | The finished `.mp4` file (transcript optional — I can generate metadata without one) |
| "Process this transcript/VTT" / "generate titles" | vtt-metadata | A `.vtt` or `.srt` transcript file |
| "Generate metadata and write it to ADO" (with a prior episode style to match) | create-episode-metadata-from-transcripts | A transcript/video + the Episode work item ID (I find a prior published episode myself to match house style) |
| "Pull the resource links from the deck" (MVP Unplugged only) | mvp-unplugged-links | The Episode work item ID (I locate the shared deck myself) |
| "Update YouTube description" / "sync ADO to YouTube" | youtube-description | The ADO Episode work item ID (fields must already be filled in there) |
| "Add a YouTube collaborator" | youtube-collaborator | The ADO work item ID or YouTube video URL + the collaborator's channel name |
| "Generate chapter markers" | video-chapters | The video file itself (I transcribe it locally) |
| "Draft the Fabric review email" | fabric-production-schedule | The Episode work item ID + Frame.io review link; dates come from ADO, the skill creates an addressed Outlook draft with clickable ADO and Frame.io links, then notifies Sara privately in Teams to check Drafts |
| "Tell me when a Fabric episode is ready to publish" | fabric-production-schedule | No per-Episode input; the scheduled watcher monitors FY27 FEI Show 236171 and FTTF Show 236193 |
| "Analyze YouTube/livestream comments" | youtube-analysis | The video, livestream, or playlist URL |
| "Content autopsy" / "why did this video do well" | content-autopsy | The YouTube video URL (channel token must exist); a Studio CSV export is optional for CTR data |
| "View to TAM" / "how did this video perform" | view-to-tam | The YouTube video URL |
| "Create an aka.ms redirect" | aka-redirect | Target URL, desired short path name, your alias |
| "Send calendar invite for a recording" | send-calendar-invite | The Episode work item ID |
| "Proofread this transcript" | transcript-proofread | A `.vtt`/`.srt` transcript file |
| "Review this PR" | github-pr-review (from `github-workflow` plugin) | The PR number or link |


## YouTube API
- Tokens: `~/.copilot/youtube-tokens/` — 6 channels: azd, dotnet, msdev, reactor, vs (+ credentials.json)
- Skills: `~/.copilot/skills/youtube-description/` (SKILL.md, youtube-api.js, auth.js)
- **Content Autopsy skill:** `~/.copilot/skills/content-autopsy/` (autopsy.js + SKILL.md) — diagnostic retention/traffic/CTR analysis (see projects.md)
- Re-auth a channel: `node ~/.copilot/youtube-tokens/auth.js <channel>` (needed ~weekly — app is in test mode)
- Channels authorized: azd, dotnet, msdev, reactor, vs

## Microsoft Internal
- [FY27 Production Studios Services Rate Card](https://microsoft.sharepoint.com/teams/CurrentRateCard/Shared%20Documents/Information/Services%20and%20Cost%20Rate%20Card/FY27_ProductionStudios_Services_RateCard.pdf?web=1) — current BOC pricing; streaming support is $300/hour with a 2-hour minimum
- General 222155 — Copilot onboarding work item
- Microsoft Foundry — sister team, Azure AI Foundry focus

## Azure DevOps (DevRel/Studios)
- **Org:** DevRel · **Project:** Studios
- **Project ID:** d583c19b-5f23-4bed-a650-1cc43436e5c9
- **URL:** https://dev.azure.com/devrel/Studios
- Series/episode automation: see `skills/ado-series-creation.md`

## Copilot CLI
- [GitHub Copilot CLI docs](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)
- `gh copilot suggest` — natural language to shell commands
- `gh copilot explain` — explain what a command does
- Work IQ — Microsoft 365 integration, pulls context from Graph (Teams, email, calendar, docs)

## External
- [GitHub Copilot instructions docs](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-instructions-for-github-copilot) — how copilot-instructions.md works
