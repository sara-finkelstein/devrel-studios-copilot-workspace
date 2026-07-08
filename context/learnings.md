# Learnings

<!-- Copilot adds to this file as you work together. Format:
- **[Topic]** — what you learned. *Why it matters:* [context]
-->

## Office / PowerPoint Automation

- **Download a OneDrive/SharePoint file from a share link (headless)** — in signed-in Edge (Playwright), resolve the file via the shares API: `…/personal/<user>_microsoft_com/_api/v2.0/shares/u!<base64url(sharingUrl)>/driveItem?$select=@content.downloadUrl`. That returns a pre-authenticated `download.aspx?...&tempauth=…` URL you can save with `Invoke-WebRequest`. *Why it matters:* boss's decks/files live in OneDrive, not locally; this grabs them without manual download. (`microsoft-my.sharepoint.com/p/<user>` = that person's personal OneDrive.)
- **Sensitivity-labeled Office files are encrypted at rest** — header `D0 CF 11 E0` (OLE compound file) instead of `PK` (zip). python-pptx / automation CANNOT read them. Fix: open in *desktop* PowerPoint → set a non-encrypting label (e.g. "General") → **Save As** → header flips to `PK` and it's editable. *Why it matters:* internal decks carry MIP labels; must strip before any programmatic editing. (Decryption only happens in memory; saving is what writes unencrypted bytes.)
- **Clone a slide so PowerPoint accepts it: use COM `Slides(n).Duplicate()`, NOT python-pptx XML copy** — python-pptx clones open fine in python but PowerPoint/COM reject them ("PowerPoint could not open the file"). Drive PowerPoint via `pywin32` (`win32com.client.Dispatch("PowerPoint.Application")`), `Duplicate()` the source slide (also copies the slide-level `<p:bg>` background), edit text, `SaveAs(path, 24)` natively. *Why it matters:* reliable, PowerPoint-valid PPT editing. (python-pptx shape-copy misses slide-level `<p:bg>`, causing wrong/grey backgrounds.)
- **Render a PPTX slide to PNG headlessly** — PowerPoint COM `Slides(n).Export(path, "PNG", 1920, 1080)`; needs no other PowerPoint instance running. *Why it matters:* preview slides directly in the terminal.
- **Grab a screenshot straight from the clipboard** — after Win+Shift+S: `Add-Type -AssemblyName System.Windows.Forms,System.Drawing; [System.Windows.Forms.Clipboard]::GetImage().Save($path)` then view the PNG. *Why it matters:* fastest way for Sara to show Copilot what's on her screen — no file save/attach needed.
- **Read Office files that download as OLE (not zip)** — SharePoint/OneDrive downloads here often arrive as OLE2 (`D0 CF 11 E0`) under `.docx`/`.xlsx` names even without a MIP label; python-docx/openpyxl throw `PackageNotFoundError`/`BadZipFile`. Fix: read via Word/Excel COM, or resave to modern format — Excel `wb.SaveAs(path, 51)`, Word save — to flip the header back to `PK` zip so python can parse it. *Why it matters:* lets you programmatically read/parse colleagues' and boss's files.
- **Find anyone's file across M365** — Graph `POST /search/query` with `entityTypes:["driveItem"]` + a name query (via Work IQ `do_action`) returns owner, webUrl, and driveId/itemId fast. *Why it matters:* fastest way to locate "the spreadsheet X uses" without knowing the folder path.
- **Download a cross-user OneDrive file (tokens walled)** — az/CLI Graph tokens are Conditional-Access blocked (403) for other people's OneDrive, and Work IQ reads metadata but not raw bytes. Reliable path: Playwright `browser_navigate` to the file's webUrl in the already-signed-in Edge session — it auto-fires the download; then move it from `.playwright-mcp\`. *Why it matters:* grabbing colleagues' shared files when API tokens are blocked.

## Copilot Tips

- **ADO comments can't be edited via the API** — the `wit_add_work_item_comment` MCP tool only creates new comments; there's no edit/update for an existing one. To amend a note (e.g. add a signature after the fact), post a short follow-up comment referencing the prior one. *Why it matters:* set the full comment (including any required sign-off) correctly the first time to avoid double comments.

- **Installing plugin skills manually** — skills from mvp-copilot-plugins are just folders; download each `SKILL.md` (+ any scripts) into `~/.copilot/skills/`. Shared scripts go in a plugin root (`~/.copilot/plugins/devrel-studios/`) and the `<PLUGIN_ROOT>` placeholder in SKILL.md must be replaced with that absolute path. *Why it matters:* memory storage is blocked (enterprise billing), so durable setup notes belong in these context files, not Copilot memory.

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
