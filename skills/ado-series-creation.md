# ADO Series Creation & Episode Automation

## What it does
Automates building a video Series in Azure DevOps from a CSV/Excel data source: creates the parent Series, bulk-creates Episode work items, adds the 4 standard child work items per episode (Scheduling, Editing, Uploading, Publishing), and populates episode fields (titles, descriptions, chapter markers, links, hosts) from the source data.

## When to use it
You have a CSV or Excel (e.g., a conference/show "Video Details" sheet) and need to stand up or update a full Series hierarchy in ADO without doing it by hand, one work item at a time.

## ADO Project Reference
- **Organization:** DevRel
- **Project:** Studios
- **Project ID:** d583c19b-5f23-4bed-a650-1cc43436e5c9
- **URL:** https://dev.azure.com/devrel/Studios
- **Purpose:** Video production workflow management, pre-production through publication

## Prompt

```
I have a [CSV/Excel] file at [path] with one row per session. Build (or update) the ADO Series in DevRel/Studios from it.

Follow these rules:
1. Treat the spreadsheet as the AUTHORITATIVE source — only map fields that exist in BOTH the sheet and ADO; ADO is updated to match the sheet.
2. If Excel: read the "Video Details" sheet specifically (not production schedule sheets). Headers are in row 3 (header=2). Filter out sample rows (e.g., Session Number = 'aa') and coerce session numbers to numeric.
3. Create the parent Series work item first; record its ID.
4. Bulk-create Episode work items, linking each to the Series as a child (link from Series → Episode with type "child").
5. Add 4 child work items per episode: Scheduling, Editing, Uploading, Publishing. Child titles are the type name ONLY — no episode numbers.
6. Populate episode fields using the mapping table below.
7. Set System.Title to "Session X: [Video/Session Title]".
8. Process in batches of 10, sequentially (not parallel). Verify HTTP 200 + incremented revisions after each batch.
9. After all batches, verify: every episode has exactly ONE of each child type, no duplicates, no orphans, parent links intact.

Show me a tracking tree (Series → Episodes → child items with IDs and ✓) as you go.
```

## Excel/CSV → ADO Field Mappings

Each row = one Session/Episode work item.

| Spreadsheet Column | ADO Field |
|--------------------|-----------|
| Video/Session Title | Video title ext (`Custom.Videotitleext`) |
| Video/Session Description | Video description external (`Custom.Videodescriptionexternal`) |
| Chapter Markers | Chapter markers external (`Custom.Chaptermarkersexternal`) |
| CTA Links | Resource links external (`Custom.Resourcelinksexternal`) |
| Social Handle(s) | Speaker social links external (`Custom.Speakersociallinksexternal`) |
| Link to RAW files | Raw file (`Custom.Rawfile`) |
| Link to Final Files | Final file (`Custom.Finalfile`) |
| Thumbnail Image URL | Thumbnail (`Custom.Thumbnail`) |
| Speaker email(s) | Host 1 / Host 2 (`Custom.Host1`) |

## Critical Gotchas

- **Identity fields (Host 1/2):** require an ADO user identity, NOT free text. Put a real Microsoft email in the sheet (e.g., `Eleanor Boyd <eleanorboyd@microsoft.com>`), extract the email, and set the field to the email — ADO auto-resolves the display name and profile.
  - Example op: `{"op":"add","path":"/fields/Custom.Host1","value":"eleanorboyd@microsoft.com"}`
- **Multi-line HTML fields:** Chapter markers, descriptions, resource links, and social links use `multilineFieldsFormat: "html"`. Use `<br>` for line breaks, NOT `\n` — otherwise ADO shows literal `\n`.
  - Before (wrong): `00:00 — Intro\n00:09 — Overview`
  - After (right): `00:00 — Intro<br>00:09 — Overview`
- **Work item ID order:** Session numbers run reverse to IDs (Session 1 often has a HIGHER ID than Session 60). Don't assume ID order = session order — map explicitly.
- **Linking direction:** Link Series (parent) → Episode (child) with `type: "child"`. Linking the other way creates a broken hierarchy. Always verify `System.Parent` is populated.
- **Don't mix work item types in one batch call** (e.g., don't create Scheduling + Editing in the same batch).

## Title Conventions
- **Episodes:** `Session X: [Title]` (number + descriptive title)
- **Child work items:** type name only — `Scheduling`, `Editing`, `Uploading`, `Publishing` (no numbers)

## Relevant ADO MCP tools
- `mcp_ado_wit_create_work_item` — create individual work items
- `mcp_ado_wit_add_child_work_items` — create children with automatic parent linking
- `mcp_ado_wit_update_work_items_batch` — bulk updates (batches of 10)
- `mcp_ado_wit_get_work_items_batch_by_ids` — retrieve multiple work items
- `mcp_ado_wit_work_items_link` — manual parent-child linking

## Verification checklist
- [ ] Each episode has exactly ONE Scheduling, Editing, Uploading, Publishing
- [ ] No duplicate or orphaned child work items
- [ ] All `System.Parent` relationships populated correctly
- [ ] Titles match the conventions above
- [ ] Multi-line fields render with `<br>`, not literal `\n`
- [ ] Batch updates returned HTTP 200 with incremented revisions

## Example
**Input row (Session 1):** Title "Making your own MCP server in VS Code", speaker `Eleanor Boyd <eleanorboyd@microsoft.com>`, 13 chapter markers, Frame.io raw link, YouTube final link, thumbnail URL.

**Result:** ADO work item 186479 →
- `System.Title` = "Session 1: Making your own MCP server in VS Code"
- `Custom.Videotitleext`, `Custom.Videodescriptionexternal`, `Custom.Chaptermarkersexternal` (with `<br>`), `Custom.Rawfile`, `Custom.Finalfile`, `Custom.Thumbnail`, social/resource links all populated
- `Custom.Host1` resolved from `eleanorboyd@microsoft.com` to the Eleanor Boyd identity
- Parent = Series; children = Scheduling/Editing/Uploading/Publishing
