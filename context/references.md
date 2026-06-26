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

## YouTube API
- Tokens: `~/.copilot/youtube-tokens/` (msdev.json, azd.json, vs.json)
- Skills: `~/.copilot/skills/youtube-description/` (SKILL.md, youtube-api.js, auth.js)
- Channels authorized: msdev, azd, vs

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
