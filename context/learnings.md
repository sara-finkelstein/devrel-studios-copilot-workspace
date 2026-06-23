# Learnings

<!-- Copilot adds to this file as you work together. Format:
- **[Topic]** — what you learned. *Why it matters:* [context]
-->

## Copilot Tips

- **Tool awareness rule** — Copilot should always search its available tools before claiming it can't do something. *Why it matters:* prevents wasted time when MCP tools like ADO are available but not discovered
- **Custom instructions** — `~/.copilot/copilot-instructions.md` loads globally; `.github/copilot-instructions.md` loads per-repo. *Why it matters:* per-repo is better for team workflows
- **Launch from workspace folder** — `cd ~\devrel-studios-copilot-workspace && copilot` loads all instructions and context automatically

## Workflow Tips

- **Accepting a YouTube collaboration invite (brand channels)** — dotnet, Microsoft Developer, and Microsoft Reactor are all brand channels under Sara's single Google account, so you never sign out or use InPrivate (a private window just starts with no session). To accept: (1) switch the active channel to the collaborator via avatar → switch channel, then (2) open the **collaborator-first** URL `studio.youtube.com/channel/{collaboratorChannelId}/collaboration/{ownerChannelId}`. *Why it matters:* the owner-first URL always shows "Oops, you don't have permission" — both conditions must be true to see the Accept prompt.
- **YouTube API OAuth setup** — run `node ~/.copilot/youtube-tokens/auth.js <channel>` for each channel, authorize in browser, tokens auto-refresh
- **YouTube video stats** — `node ~/.copilot/skills/youtube-description/youtube-api.js <channel> get <videoId>` returns views, likes, comments

## Tool Tips

- **YouTube API channels set up:** msdev, azd, vs — tokens at `~/.copilot/youtube-tokens/`
- **youtube-api.js** enhanced to include statistics (views, likes, comments) in `get` command
