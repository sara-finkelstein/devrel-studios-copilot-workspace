# Create an ADO Series with Episodes

## What it does
Creates a complete Series hierarchy in DevRel/Studios: the parent Series, its automation-generated Series children, the requested Episodes, and each Episode's automation-generated production work items.

## When to use it
Use this when someone asks to create, set up, or stand up a new Series in ADO, with or without a finalized episode lineup. It supports named Episodes, numbered placeholders, or episode data from a CSV/Excel file.

## ADO Project Reference
- **Organization:** DevRel
- **Project:** Studios
- **Project ID:** d583c19b-5f23-4bed-a650-1cc43436e5c9
- **URL:** https://dev.azure.com/devrel/Studios
- **Series area:** `Studios\Series`

## Prompt

```text
Create a new ADO Series in DevRel/Studios and complete the full Episode hierarchy.

Series title: [series title]
Episode source: [named list / number of placeholders / CSV or Excel path]

Follow this workflow:

1. Check for an existing Series with the same or a confusingly similar title. If a
   plausible duplicate exists, stop and ask before creating anything.

2. Present a prefilled intake table or editable intake form containing all Series and
   Episode settings. Ask the user to edit the values and confirm the complete intake
   once, rather than asking every field as a separate question. Ask an individual
   follow-up only when a required value remains missing or ambiguous.

   The intake must include:
   - Series title
   - Graphics, long-form/full-course, and Series Upwork choices
   - Executive Producer, Content Owner, Associate Producer, and ADO assignee
   - YouTube channel and filming location
   - Public title and description
   - Additional stakeholders
   - Episode source, count or titles
   - Episode Shorts, Thumbnails, Upwork, and Teleprompter choices
   - Optional SharePoint, Figma, Frame.io, playlist, run-of-show, raw file,
     publishing platform, target publish date, graphics due date, and long-form URL

3. Read the live Series work item schema before writing. Use current allowed picklist
   values and the current Studios iteration. Do not rely on stale hardcoded choices.

4. Create the Series in ONE initial request with all automation-driving values:
   - `System.State` = `Active`
   - `System.AreaPath` = `Studios\Series`
   - current `System.IterationPath`
   - `System.AssignedTo`
   - `Custom.ExecutiveProducer`
   - `Custom.ContentOwner`
   - `Custom.YouTubeChannel`
   - `Custom.FilmingLocation`
   - `Custom.Graphics`
   - `Custom.Upwork`
   - `Custom.longformseries`
   - `Custom.Seriestitleext`

   Identity fields must use a resolvable email address, not free text.

5. Do NOT manually create Series child work items. Pause 90-120 seconds for the
   Studios automation, then verify:
   - Postmortem: always created
   - Graphics: created only when `Custom.Graphics` is true
   - Full course video Episode: created only when `Custom.longformseries` is true
   - Upwork: created only when `Custom.Upwork` is true

6. Create Episodes sequentially and link each to the Series as its parent.
   - Named Episode title: use the provided title.
   - Placeholder title: `Episode 1`, `Episode 2`, and so on.
   - Spreadsheet title: use the source's episode/session title and numbering.
   - Set the parent Series relationship immediately.
   - Carry the Series ownership, channel, filming location, area, and iteration into
     each Episode unless the user provides Episode-specific values.

7. Collect any Episode automation choices before creation. The live required Boolean
   fields include:
   - `Custom.YouTubeshorts`
   - `Custom.Thumbnails`
   - `Custom.Upwork`
   - `Custom.Teleprompter`

   Default these to false only when the user asks for plain placeholders and has not
   requested those deliverables. Set all of them in the initial Episode create request.

8. Do NOT manually create Episode child work items. After all Episodes are created,
   pause 90-120 seconds for automation. Then verify every Episode has exactly one:
   - Scheduling
   - Editing
   - Uploading
   - Publishing

   Also verify optional child items requested through Episode Boolean fields. When
   `Custom.Thumbnails` is true, the expected child work item type is `Thumbnails`.

9. Verify the complete hierarchy:
   - Every Episode has `System.Parent` equal to the Series ID.
   - Every automated child has `System.Parent` equal to its Episode or Series ID.
   - No duplicate or orphaned child items exist.
   - Automated children were created by `dsautomation-la1`.
   - Do not assume work item ID order matches Episode order.

10. Report the Series and Episode IDs with clickable links. Summarize which automated
    children were created. Do not claim completion until the automation has run and
    the hierarchy has been verified.
```

## Optional CSV/Excel Episode Mapping

When episode metadata comes from a spreadsheet, treat it as the authoritative source and map only fields that exist in both the source and ADO.

| Spreadsheet column | ADO field |
|---|---|
| Video/Session Title | `Custom.Videotitleext` |
| Video/Session Description | `Custom.Videodescriptionexternal` |
| Chapter Markers | `Custom.Chaptermarkersexternal` |
| CTA Links | `Custom.Resourcelinksexternal` |
| Social Handle(s) | `Custom.Speakersociallinksexternal` |
| Link to RAW files | `Custom.Rawfile` |
| Link to Final Files | `Custom.Finalfile` |
| Thumbnail Image URL | `Custom.Thumbnail` |
| Speaker email(s) | `Custom.Host1`, `Custom.Host2` |

For HTML-backed multiline fields, use `<br>` for line breaks rather than `\n`.

## Critical Safeguards

- Set automation-driving fields during the initial create. Changing them afterward may not backfill the corresponding children.
- Never create Scheduling, Editing, Uploading, Publishing, Thumbnails, Postmortem,
  Graphics, Full course video, or Upwork children manually unless the automation has
  definitively failed and the user approves a fallback.
- Pause before verification; automation is asynchronous and can take more than a minute.
- Use the live ADO schema and picklists. Current known values include `Microsoft Developer` and `On Location Filming`, but they must still be validated before reuse.
- Link the Episode to the Series as a parent relationship and verify `System.Parent`.
- If a partial failure occurs, inspect the existing hierarchy before retrying so retries do not create duplicates.

## Automation Fallback

If automation appears to have failed:

1. Wait at least one full automation window and retry the hierarchy check.
2. Compare the existing children against the expected types for each Series or Episode.
3. Show the user exactly which items are missing and ask for confirmation before
   manually creating anything.
4. After confirmation, create only missing child types, link each to the correct parent,
   and verify the completed hierarchy.
5. Never recreate a type that already exists. If delayed automation later creates a
   duplicate, flag it immediately rather than deleting or changing it silently.

## Validated Example

**Series:** `Behind the Code` ([#236646](https://dev.azure.com/devrel/Studios/_workitems/edit/236646))

- Active, assigned to Sara Finkelstein
- Executive Producer and Content Owner: Sara Finkelstein
- YouTube channel: Microsoft Developer
- Filming location: On Location Filming
- Graphics: yes
- Long-form: no
- Upwork: no
- Automation created one Graphics and one Postmortem child

**Episodes:** four numbered placeholders

- [Episode 1 #236649](https://dev.azure.com/devrel/Studios/_workitems/edit/236649)
- [Episode 2 #236650](https://dev.azure.com/devrel/Studios/_workitems/edit/236650)
- [Episode 3 #236655](https://dev.azure.com/devrel/Studios/_workitems/edit/236655)
- [Episode 4 #236662](https://dev.azure.com/devrel/Studios/_workitems/edit/236662)

Automation created exactly one Scheduling, Editing, Uploading, Publishing, and
Thumbnails child under every Episode.
