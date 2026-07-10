# Patterns

<!-- Copilot maintains this file automatically. It logs patterns it notices in how you work — repeated tasks, friction points, and automation candidates. Review this periodically and promote useful patterns to skills. -->

## Repeated Workflows
<!-- Tasks you do more than twice that could become a skill or automation -->

## Friction Points
<!-- Things that take multiple attempts, require manual steps, or slow you down -->

- **YouTube transcript mode mistaken for subtitle track output** — after uploading a corrected caption file, transcript view looked different and appeared "wrong" even though the standard caption track was uploaded successfully. *Takeaway:* always verify from the player CC track picker first, not transcript panel rendering.
- **YouTube OAuth app is in test mode → ~7-day token expiry** — refresh tokens die about weekly ("Token has been expired or revoked"), forcing a browser re-auth (`node ~/.copilot/youtube-tokens/auth.js <channel>`, listens on localhost:3847). **Real fix:** publish the Google Cloud OAuth app (team-lead/admin task) so tokens stop expiring. *Takeaway:* if an Analytics/Data API call suddenly 401s, re-auth first before debugging.
- **Doc generate → close-in-Word → regenerate loop** — generating the FY26 report from a Python script meant every tweak required Sara to close the doc in Word or hit `PermissionError`/`-v2` fallback saves, and she couldn't hand-edit without being clobbered on regen. **Resolved:** switched to doc-as-source-of-truth ("Path A") — Sara hand-edits the OneDrive master, Copilot stops regenerating and hands over paste-ready snippets instead. *Takeaway:* for collaborative/near-final docs, hand editing beats regeneration; offer the switch early. (Recurred 7/9 on the MVP Unplugged doc — resolved by saving to a `(v2)` filename.)
- **Accepting YouTube collaboration invites** — repeatedly a sticking point across sessions: confusion over which account/channel must be active and which direction the accept URL goes. Resolved (collaborator-first URL + collaborator as active channel); now documented in the youtube-collaborator skill and learnings.md.

## Skill Candidates
<!-- Patterns ready to be turned into reusable skills -->

- **Caption QA + upload verification checklist** — recurring friction in "is this the right track?" after subtitle uploads (transcript view vs CC track picker). *Suggested skill:* run post-upload checks (track kind, last updated, expected terms), then provide a quick human verification checklist in YouTube player. Promote at 3+ uses.
- **YouTube Studio CTR export walkthrough** — recurring need to export the Advanced Mode Content CSV (Impressions + Impressions click-through rate %) to feed the Content Autopsy. Studio video-ID column = `Content` (trim leading space on IDs starting with `-`), skip the `Total` row, and **filter the table** to dodge the ~500-row export cap. Seen 2x (7/8, 7/9). *Suggested skill:* a guided "export CTR for [these videos]" checklist. Promote at 3+ uses.

- **Capture meeting follow-ups into the to-do list** — pull action items from a recorded/transcribed meeting (via Work IQ), then drop them into the project-grouped `To-Do-List.xlsx` under the right project band. Seen 1x (6/24, MVP intro chat w/ Martin Tatar). *Suggested skill:* "capture my action items from [meeting] into my to-do list" — find meeting via Work IQ, extract owner/task/due, map to existing project section (or create one), set Status=Open. Promote at 3+ uses.

## Promoted to Skills
<!-- Patterns that became skills — kept here for history -->

- **Add a note to an ADO work item** → `skills/ado-add-note.md` (promoted 7/8, after 3× use). Resolve item by plain-language search, confirm if >1 match, post comment signed `Written by ADO MCP server via CLI`. Kept local (not team-shared) — signature is Sara's personal convention.
