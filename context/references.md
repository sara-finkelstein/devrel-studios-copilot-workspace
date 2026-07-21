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
- Requires `yt-dlp` (installed) — youtube-analysis scripts call `python -m yt_dlp`
- ADO MCP server (`ado`) from the plugin's `.mcp.json` is already configured in `~/.copilot/mcp-config.json`
- To update skills: re-download from the repo and re-patch `<PLUGIN_ROOT>`

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
