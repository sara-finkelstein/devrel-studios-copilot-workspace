# Learnings

<!-- Copilot adds to this file as you work together. Format:
- **[Topic]** — what you learned. *Why it matters:* [context]
-->

## Copilot Tips

- **Tool awareness rule** — Copilot should always search its available tools before claiming it can't do something. *Why it matters:* prevents wasted time when MCP tools like ADO are available but not discovered
- **Custom instructions** — `~/.copilot/copilot-instructions.md` loads globally; `.github/copilot-instructions.md` loads per-repo. *Why it matters:* per-repo is better for team workflows
- **Launch from workspace folder** — `cd ~\devrel-studios-copilot-workspace && copilot` loads all instructions and context automatically

## Workflow Tips

- **YouTube API OAuth setup** — run `node ~/.copilot/youtube-tokens/auth.js <channel>` for each channel, authorize in browser, tokens auto-refresh
- **YouTube video stats** — `node ~/.copilot/skills/youtube-description/youtube-api.js <channel> get <videoId>` returns views, likes, comments

## Tool Tips

- **YouTube API channels set up:** msdev, azd, vs — tokens at `~/.copilot/youtube-tokens/`
- **youtube-api.js** enhanced to include statistics (views, likes, comments) in `get` command
