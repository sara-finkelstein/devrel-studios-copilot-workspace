# Frame.io Transcript Pipeline

## What it does
End-to-end pipeline for turning a Frame.io-exported timecoded transcript into
proofread `.srt`, `.vtt`, and `.ttml` caption files, then attaching all three
to the episode's ADO work item. Combines the `transcript-proofread` skill
(brand/spelling correction) with local format-conversion and ADO-attachment
scripts that live in this repo.

## When to use it
Triggers: "run the transcript pipeline for [episode]", "process the Frame.io
export for [episode]", "proofread and attach captions to ADO", or whenever a
Frame.io-exported caption file needs to become upload-ready `.srt`/`.vtt`/`.ttml`
and land on the Episode work item.

## Why this exists (vs. the `transcript-proofread` plugin skill alone)
- `transcript-proofread` (part of the `@microsoft/copilot-plugin-devrel-studios`
  plugin, owned by `@jamescon`) does the actual proofreading and knows the
  tech/brand glossary. This skill **calls into it** for that step — don't
  duplicate its proofreading logic here.
- The plugin only ships an SRT/VTT cleaner, not a TTML converter, and has no
  ADO-attachment step. Those two pieces are added here, in Sara's own
  workspace repo, so they're not at risk of being overwritten when the plugin
  is reinstalled/updated.
- Frame.io on this account has **no API access** — the transcript export is a
  manual download from the Frame.io UI. (If API access is ever enabled, Step 1
  is the only step that would change.)

## Prerequisites
- Azure CLI logged in (`az login`) with access to the `devrel` Azure DevOps
  org — `ado_attach_files.ps1` uses an `az` access token, not a PAT, since the
  ADO MCP server only supports attachment *download*, not upload.
- Python 3.8+ (standard library only).

## Workflow

### Step 1 — Get the Frame.io export
Ask the user for the local path to the timecoded transcript file they
downloaded from Frame.io (Review page → Transcript panel → Download →
`.srt` or `.vtt`). There is no API path on this Frame.io plan, so this is
always a manual hand-off.

### Step 2 — Proofread
Invoke the **`transcript-proofread`** skill on that file. Follow its normal
flow: parse, glossary pass, auto-apply high-confidence tech/brand fixes,
confirm ambiguous items with the user, then produce a clean, upload-ready
corrected file (its own Step 5). This is the "source of truth" file the rest
of this pipeline builds from — usually `<name>.corrected.srt` or `.vtt`.

### Step 3 — Generate all three formats
Run the converter in this repo against the corrected file from Step 2:

```
python skills/scripts/transcript_formats.py <corrected_file> --formats srt,vtt,ttml --outdir <same folder as input>
```

This writes `<stem>.srt`, `<stem>.vtt`, and `<stem>.ttml` (loss-lessly
re-parsing the corrected file, so all three stay in sync). Confirm with the
user that all three were generated and looks right if this is the first run
for a new episode.

### Step 4 — Find the ADO Episode work item
If the user hasn't given a work item ID, resolve it the same way as the
`ado-add-note` skill: search with `ado-search_workitem` using the episode
name/topic/speaker, confirm with the user if more than one plausible match
comes back. Confirm **Organization** (`devrel`) and **Project** (`Studios`
unless it's an MVP-project item).

### Step 5 — Attach the files to ADO
Run:

```powershell
skills/scripts/ado_attach_files.ps1 -Organization devrel -Project <Project> -WorkItemId <id> `
    -Files "<stem>.srt","<stem>.vtt","<stem>.ttml"
```

This uploads each file to the Attachments API and links it to the work item
via an `AttachedFile` relation, using an `az account get-access-token`
bearer token (no PAT needed). Requires `az login` to already be authenticated
against the `devrel` org.

### Step 6 — Confirm
Report back: number of cues, list of proofreading changes (from Step 2), the
three output file paths, and a link to the work item:
`https://dev.azure.com/devrel/<Project>/_workitems/edit/<id>`

## Notes
- `transcript_formats.py` and `ado_attach_files.ps1` are simple, standalone,
  and safe to reuse for any other caption-format or ADO-attachment need — they
  don't depend on the `transcript-proofread` plugin's internals.
- If the plugin's proofreading script paths ever change, only Step 2 is
  affected; Steps 3–5 are independent.
- Automation candidate: if Frame.io API access is ever added to the account,
  Step 1 could pull the transcript directly instead of a manual download.
