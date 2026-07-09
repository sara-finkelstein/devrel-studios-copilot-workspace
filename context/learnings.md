# Learnings

<!-- Copilot adds to this file as you work together. Format:
- **[Topic]** — what you learned. *Why it matters:* [context]
-->

## YouTube Analytics & Content Autopsy

- **YouTube Analytics API ≠ Data API** — host `youtubeanalytics.googleapis.com`, path `/v2/reports`, scope `yt-analytics.readonly` (msdev token already had it). Returns core metrics, the **audience retention curve** (`metrics=audienceWatchRatio,relativeRetentionPerformance` + `dimensions=elapsedVideoTimeRatio`, 100 points), and **traffic sources**. Query shape: `?ids=channel==MINE&startDate=X&endDate=Y&filters=video==ID&metrics=...&dimensions=...`. *Why it matters:* this is what powers diagnostic post-production analysis beyond vanity metrics; occasional HTTP 500s just need a retry.
- **Thumbnail CTR & impressions are NOT in the Analytics API** — `impressions` and `impressionsClickThroughRate` are rejected as "Unknown identifier" (only card/annotation CTR exists). They also **cannot be derived** — impressions (the denominator) live nowhere in the API and views ≠ impressions. Only source = **YouTube Studio → Advanced Mode → Content → Export CSV**. *Why it matters:* any CTR feature must take a manual Studio export as input.
- **Studio CSV shape & gotchas** — headers: `Content,Video title,Video publish time,Duration,Views,Watch time (hours),Subscribers,Estimated revenue (USD),Impressions,Impressions click-through rate (%)`. The `Content` column = video ID (**trim** the leading space on IDs starting with `-`); row 2 = `Total` (skip). Export has a **row cap** — the Advanced Mode table lazy-loads ~500 rows and exports only what's loaded, so low-view videos get cut. **Fix: filter the table** (Filter box → title contains "X") to export just the target videos. Also: a custom date range needs the **Apply** button or it silently doesn't take. *Why it matters:* saves a lot of re-export churn.
- **Sprinklr dead-end for YouTube CTR** — msdev/"Microsoft Developer" is NOT provisioned to Sara's Sprinklr user (Account filter empty, "No results" for MSDev), and its Social Engagement > YouTube dashboard only carries standard YouTube-API metrics (no thumbnail CTR). *Why it matters:* don't route YouTube CTR through Sprinklr — use the Studio export.

## Office / Document Generation (Windows)

- **docx validator crashes on Windows console encoding** — the docx skill's `validate.py` prints a `→` arrow and dies with a cp1252 `UnicodeEncodeError`, and can misreport a fake `numbering.xml` error. **Fix:** set `$env:PYTHONUTF8="1"; $env:PYTHONIOENCODING="utf-8"` before running it — then it passes cleanly. *Why it matters:* the doc was fine; only the validator's stdout was broken.
- **No local PPTX/PDF render for docx** — the skill's `soffice.py` shim is Unix-only (`socket.AF_UNIX`) and `pdftoppm` isn't installed, so docx→image preview fails on this machine. *Why it matters:* validate structurally instead; can't visually preview a generated .docx here.
- **Generated .docx locked while open in Word** — regenerating over a file Sara has open throws `EBUSY`. *Why it matters:* save to a new filename (e.g. `(v2)`) rather than fighting the lock, same lesson as the FY26 report.

## Work IQ

- **Read a spreadsheet's actual rows by passing its file URL** — a plain Work IQ `ask` about presenters in the "Past and upcoming talks" sheet only surfaced 2 of 8; passing the file's SharePoint URL directly via the `fileUrls` parameter made it read the real rows and return all 8 with deck/recording links. *Why it matters:* for guest discovery from the Talks catalog, hand Work IQ the file URL — don't rely on open enterprise search, which misses most rows.

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

- **YouTube API channels set up:** azd, dotnet, msdev, reactor, vs (6 total, +credentials.json) — tokens at `~/.copilot/youtube-tokens/`
- **youtube-api.js** enhanced to include statistics (views, likes, comments) in `get` command
