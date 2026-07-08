# Patterns

<!-- Copilot maintains this file automatically. It logs patterns it notices in how you work — repeated tasks, friction points, and automation candidates. Review this periodically and promote useful patterns to skills. -->

## Repeated Workflows
<!-- Tasks you do more than twice that could become a skill or automation -->

- **Update ADO work items via CLI** — find the work item by plain-language description (search_workitem), confirm the target when ambiguous, then add a comment / change state via the ADO MCP tools instead of the ADO web UI. Seen 3x on 7/8 (Proposal #232484 note, Episode #222346 note, signature follow-ups). Faster than the web UI and lets Sara skip keeping ADO tabs open. *Suggested skill:* "add a note to [work item description]" → resolve item, confirm if >1 match, post comment signed `Written by ADO MCP server via CLI`. Strong skill candidate at 3+ uses.

## Friction Points
<!-- Things that take multiple attempts, require manual steps, or slow you down -->

- **Doc generate → close-in-Word → regenerate loop** — generating the FY26 report from a Python script meant every tweak required Sara to close the doc in Word or hit `PermissionError`/`-v2` fallback saves, and she couldn't hand-edit without being clobbered on regen. **Resolved:** switched to doc-as-source-of-truth ("Path A") — Sara hand-edits the OneDrive master, Copilot stops regenerating and hands over paste-ready snippets instead. *Takeaway:* for collaborative/near-final docs, hand editing beats regeneration; offer the switch early.
- **Accepting YouTube collaboration invites** — repeatedly a sticking point across sessions: confusion over which account/channel must be active and which direction the accept URL goes. Resolved (collaborator-first URL + collaborator as active channel); now documented in the youtube-collaborator skill and learnings.md.

## Skill Candidates
<!-- Patterns ready to be turned into reusable skills -->

- **Capture meeting follow-ups into the to-do list** — pull action items from a recorded/transcribed meeting (via Work IQ), then drop them into the project-grouped `To-Do-List.xlsx` under the right project band. Seen 1x (6/24, MVP intro chat w/ Martin Tatar). *Suggested skill:* "capture my action items from [meeting] into my to-do list" — find meeting via Work IQ, extract owner/task/due, map to existing project section (or create one), set Status=Open. Promote at 3+ uses.

## Promoted to Skills
<!-- Patterns that became skills — kept here for history -->
