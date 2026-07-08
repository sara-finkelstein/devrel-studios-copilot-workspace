# Add a Note to an ADO Work Item

## What it does
Finds an ADO work item from a plain-language description and posts a comment (note) to it — confirming the target first when the match is ambiguous, and always signing the note with Sara's standard signature.

## When to use it
You want to jot a quick status update or note onto a work item (Proposal, Episode, Action, etc.) without opening the ADO web UI or keeping tabs open. Example triggers: "add a note to the Michael Washington episode…", "leave a comment on the MVP intro proposal saying…".

## ADO Project Reference
- **Organization:** DevRel
- **Project:** Studios (default; some MVP items live in the MVP project)
- **Project ID:** d583c19b-5f23-4bed-a650-1cc43436e5c9
- **URL:** https://dev.azure.com/devrel/Studios

## Prompt

```
Add a note to the ADO work item described as "[description]".
The note text is: "[note text]".

Follow these rules:
1. Find the work item with ado-search_workitem using the description (person's name,
   series/show, episode number, proposal title, etc.). Broaden the search if the first
   query returns nothing.
2. If exactly one item matches, proceed. If more than one plausible item matches, STOP
   and ask me which one before writing (show id, type, title, project, state).
3. Post the note as a comment via ado-wit_add_work_item_comment, using the correct
   project (Studios unless the item is in the MVP project).
4. Append this signature as the final line of the comment (one comment, not two):

       Written by ADO MCP server via CLI

5. Confirm with the work item id, the exact note text posted, and a clickable link:
   https://dev.azure.com/devrel/<Project>/_workitems/edit/<id>
```

## Example

**Input:**
> Add a note to the Michael Washington episode saying "Justin sent the video to Michael for approval by EOW."

**What Copilot does:**
1. `ado-search_workitem "Michael Washington episode"` → single match: **#222346 · Ep 5: Michael Washington** (Episode, Studios, Post Production)
2. Single match, so proceeds without asking
3. Posts the comment:
   > Justin sent the video to Michael for approval by EOW.
   >
   > Written by ADO MCP server via CLI
4. Confirms with a link to [#222346](https://dev.azure.com/devrel/Studios/_workitems/edit/222346)

## Notes
- ADO comments can't be edited via the API — get the full comment (including the signature) right the first time; otherwise you'll need a second follow-up comment.
- The signature line is Sara's personal convention. If this is ever shared to the team skills repo, make the signature configurable first.
