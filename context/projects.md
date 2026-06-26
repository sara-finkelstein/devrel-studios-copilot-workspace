# Current Projects

<!-- Track what you're working on. Copilot uses this to stay relevant when you ask about priorities or next steps. -->

## Active

### ⏸️ RESUME HERE — Fix "DevRel Studios" terminal profile
- **Status:** in progress / blocked by Defender intercept
- **Goal:** Make the taskbar "DevRel Studios" profile launch in the workspace so global + repo instructions + context all load
- **The bug:** profile's `startingDirectory` pointed to `C:\Users\sfinkelstein\Documents\Copilot\devrel-studios-copilot-workspace` (does NOT exist). Correct path: `C:\Users\sfinkelstein\devrel-studios-copilot-workspace`. A second hidden "GitHub Copilot" profile had the same wrong path.
- **What happened:** edited Windows Terminal `settings.json` (changed path + set "DevRel Studios" to `cmd.exe /k copilot`). Windows Terminal showed a "reset to defaults" warning and an enterprise Defender policy hook (`HKLM_Software_Policies_GitHub_Copilot_Defender`) started intercepting tool calls — likely tripped by the auto-launch command.
- **Backup exists:** `settings.json.bak` in `...\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\`
- **Next steps after restart:** (1) confirm settings.json is intact (Terminal → Ctrl+, → Open JSON file); restore the .bak if needed. (2) Fix ONLY the `startingDirectory` path on both profiles — skip the `cmd.exe /k copilot` auto-launch since that likely triggered Defender. (3) Then just type `copilot` after the profile opens.

### ADO Series Creation skill — align with new structures
- **Status:** follow-up / not started
- **What:** Verify `skills/ado-series-creation.md` matches the current ROS template structure (now in OneDrive\Documents\Team Biz\DevRelStudios-ROS) and the current ADO work item structure before relying on it
- **Why:** Skill was migrated from the old testMCP playbook; ROS and ADO structures have changed since
- **Also:** once validated, consider sharing to the team skills repo (see references.md)

### YouTube API Setup
- **Status:** complete
- **What:** Set up YouTube Data API OAuth for 3 channels (msdev, azd, vs) and enhanced youtube-api.js with view count stats
- **Notes:** Quest to Compile Ep 1 has 2,526 views as of May 15

## On Hold

## Recently Completed

### Copilot Workspace Setup
- **Status:** complete
- **What:** Forked from Cameron's template, added tool-awareness rule, ran setup interview to build `context/me.md`
- **Notes:** Identity, studio, references, and projects context files all populated
