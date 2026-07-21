# Current Projects

<!-- Track what you're working on. Copilot uses this to stay relevant when you ask about priorities or next steps. -->

## Active

### 📌 Teams-reaction → OneNote to-do capture (new automation)
- **Status:** live (set up 7/21) — recurring scan running
- **What:** Sara reacts 📌 to any Teams message with an action item. A scheduled Copilot prompt (weekdays 9am/12pm/3pm/6pm) scans for newly-pinned messages via Work IQ, classifies each into one of Sara's 6 OneNote themes, and appends a checkbox line to `context/pinned-teams-digest.md` for Sara to paste into her real OneNote herself.
- **Why manual paste, not direct write:** Work IQ has no OneNote API access at all, and OneNote desktop COM automation is broken on this machine ("Library not registered" — likely Click-to-Run typelib issue). There's also a real prior incident where an automated write overwrote/overlapped Sara's OneNote content via sync conflict. See `context/learnings.md` and `patterns.md` (Friction Points).
- **Files:** `context/pinned-teams-digest.md` (staging area, grouped by theme), `context/pinned-teams-state.json` (dedup tracking).
- **Next:** revisit direct OneNote automation only if an Office repair/reinstall resolves the COM registration error.

### Fabric Tech Talk Fridays & Fabric Executive Insights — status tracking
- **Status:** assessed 7/20; iteration paths cleaned up
- **What:** Reviewed both ADO Shows (#174864 FTTF, #224267 FEI) for outstanding work.
- **FTTF outstanding (as of 7/20):** 4 episodes stuck in Publication (upload/publish subtasks not started): Shannon Lindsay (231676), Ashley Felts (231681), Porsche Cup & Kumulus (225198), AvePoint (228756). 2 on Hold: Kalyan Kaki (182347), Heini Ilmarinen (198295). 1 new unreviewed proposal: SMB Cost Clarity + Pricing series (236026, desired publish 9/7/26).
- **FEI outstanding (as of 7/20):** Post Production — dbt + Fabric (228786), Kim Manis/Nathalie D'Hers (232500). Production — Bogdan Crivat/Patrice Pelland (233043), Kanwal Safdar/Yitzhak Kesselman (233550, no movement since 6/25). Hold — Financial Services Leaders (227316), Open Data Interoperability (227885). Postmortem (224268) not started.
- **Done 7/20:** bulk-updated all 63 non-conforming FTTF child work items (Episodes, Editing/Uploading/Publishing, Graphics, Shorts) to Iteration Path `Studios\FY26`. FEI intentionally left untouched per Sara's request.
- **Open:** Swetha flagged a thumbnail change needed on episode 228786 (dbt + Fabric, FEI) before it can publish — specifics TBD, confirm with Swetha/graphics.

### "Infra Series" (new show, under development) — Azure infrastructure/Kubernetes content
- **Status:** guest discovery + booking sheet in progress
- **What:** New DevRel Studios series covering Azure's cloud infrastructure layer — the technology that runs Kubernetes (the system that manages containers, the small packaged units of software companies run at scale), container registries, networking, and the reliability engineering behind it.
- **Booking sheet:** `Documents\Behind the Code\Infra Series - Producer Booking Sheet.xlsx` — tabs: "Producer Booking Sheet" (episodes, has an added "Location" column), "Resource Links", "Presenter Talks" (candidate pool, unbooked names go here first).
- **Org structure to know (Azure Core, under Girish Bablani → Scott Guthrie → Satya Nadella):**
  - **Girish Bablani** — leads all of Azure Core (compute, storage, networking — the whole thing).
  - **Brendan Burns** — reports to Girish Bablani; co-creator of Kubernetes; leads the "Cloud Native & Management" pillar within Azure Core (containers, control planes) — this is the specific slice the series is about. Has 17 direct reports.
  - Not everyone relevant to the series reports through Brendan Burns — e.g. **Karthik Uthaman** (Azure Networking/Front Door, DDoS protection) reports through a separate networking chain (Varun Chawla → Abhishek Tiwari → Igor Sakhnov → Girish Bablani), bypassing Brendan Burns entirely.
- **NOT actually booked — all under research (corrected 7/17):** the episode list below is Sara's research candidates, not confirmed bookings. Episode order in the sheet was renumbered 7/17: **Ep1** Chandan Aggarwal/Neha Aggarwal (Agent Fabric network security); **Ep2** Karthik Uthaman (Azure Stormbreaker DDoS protection); **Ep3** Ravi Kiran Reddy (VMSS instance placement); **Ep4** Gunjan Bansal/Dishant Upadhaye (EagleAI diagnostics); **Ep5** Mauricio Garcia/Hozefa Karachiwala (AI infrastructure) — **moved to last + flagged ineligible**: not confirmed part of Azure Core, and not confirmed local (Redmond/Kirkland). Noted directly on the row in the sheet; cannot use unless a local Azure Core Baremetal engineer is found. Other guests (Ep1-4) not yet re-validated against the Azure-Core + local bar.
- **Candidate presenters added (not yet booked), all Brendan Burns' direct reports:**
  - **Sajay Antony** — Group Engineering Manager, Azure Container Registry. Based in Redmond, WA. Strong on-camera presence (MVP-circuit speaker, ~15 talks on Kubernetes/containers/security/observability). Public talk: "Introduction to project ORAS" on Open at Microsoft (with Toddy Mladenov). Story angle: shipped IPv6 dual-stack endpoints for Azure Container Registry as public preview (June 2026) — good hook for a cost/tradeoff-of-upgrading-internet-addressing episode.
  - **Akash Singhal** — Software Engineer II, Azure Container Registry. Based in Redmond, WA (Seattle area). Built the "artifact cache" feature (lets teams cache public container images locally instead of re-pulling every time — saves cost/speed, avoids public registry rate limits).
  - **Khaled "Kal" Henidak** — Principal Software Engineer; Kubernetes networking expert (dual-stack IPv4/IPv6, Azure CNI); KubeCon keynote speaker. Location not yet verified.
  - **Jake Welch** — Principal Group Engineering Manager, Site Reliability Engineering; based in **New York City** (not Redmond — confirmed by Sara 7/17). Started Azure's first SRE pilot (2014); USENIX/SREcon speaker on Azure Storage reliability.
- **Content pillars for the series:** supply chain security (containers), Kubernetes/container networking, site reliability engineering, control plane architecture, cost/reliability tradeoffs of infrastructure upgrades.
- **Next:** vet Vitaly Voloshin, Ganesh Gopal, Pritesh Patwa (other Brendan Burns reports, no public speaking history found yet); confirm booking order/scheduling for the 3 viable new candidates (Jake Welch removed — based in NYC, out of filming range).
- **Guest filming eligibility:** Redmond campus or nearby (e.g., Kirkland) only — see `studio.md`. Sajay Antony, Akash Singhal, and Khaled Henidak all qualify.

- **Content briefing (plain-language, for Sara's own understanding):**
  - **Kubernetes** — an "orchestration layer": it doesn't run application code itself, it manages where and how containers (small self-contained packages of software) run across many servers — starting them, restarting failures, spreading load, coordinating updates. Think of a conductor directing musicians. Microsoft co-created it (Brendan Burns is one of its original creators).
  - **What worries people about AI + orchestration/cloud computing** (rich territory for episode angles):
    - **Cost** — AI workloads are expensive; usage spikes unpredictably, hard to forecast/control spend.
    - **Scale/capacity** — AI demand spikes are huge and sudden; can the system keep up without crashing or queueing?
    - **Reliability** — long-running AI jobs (training, big inference batches) don't restart cleanly like a simple web app if a container fails mid-task.
    - **Security/isolation** — AI workloads handle sensitive data; containers/agents increasingly talk to each other automatically, raising fear that one compromised piece reaches data/resources it shouldn't (maps to Ep2's "what breaks when agents talk to each other").
    - **Specialized hardware** — AI needs specific chips; scheduling "put this container only on a machine with the right chip, without wasting an idle expensive one" is much harder than regular cloud computing.
    - **Complexity/opacity** — as more AI-driven automation gets added (e.g. Ep5's "AI diagnosing Azure itself"), people worry about trusting a system they can't fully see inside of.

### Content Analytics / Post-Production Intelligence
- **Status:** Phase 0 + Phase 1 done (7/8–7/9); usable now
- **What:** Diagnostic "content autopsy" of published videos — retention curves, traffic sources, subscriber conversion, and thumbnail CTR — to surface post-production blind spots beyond views/likes.
- **Content Autopsy skill (BUILT):** `~/.copilot/skills/content-autopsy/` (`autopsy.js` + `SKILL.md`). Pulls retention/traffic/core metrics live from the YouTube Analytics API; merges thumbnail Impressions + CTR from a YouTube Studio "Table data" CSV export. Auto-loads. Trigger: *"run a content autopsy on [video]"*. Run: `node autopsy.js <channel> --video <id>|--query "<search>" [--ctr-csv "<path>"] [--compact]`.
- **First real use:** full **MVP Unplugged** series analysis (all 4 episodes, msdev) → shareable Word doc for Justin at `Documents\YT Analytics\MVP Unplugged - Content Performance Review (v2 softened).docx` (tone softened for a senior audience — findings framed as observations + questions).
- **Key finding:** all 4 episodes below the 3.12% channel CTR baseline → packaging is the series-wide weakness; weak first-10% hooks second; discovery/search third. Foundry ep (best CTR + search) got the most impressions — algorithmic flywheel visible.
- **Next / phases available:** Phase 2 = build channel baselines; Phase 3 = show-level trend intelligence across more series; Bonus = retrofit `youtube-monthly-watchhours` to pull retention/CTR live.

### FY26 Impact & ROI Report (for James — leadership)
- **Status:** near-final; master owned by Sara, pending a few manual edits
- **What:** Single leadership Word doc + companion Excel workbook — *what we did → how much we saved vs. outsourcing → impact.* Straightforward tone (not braggy). Headline reach = all-up ~80M views / 3.2M watch hours (Aurea's numbers); flagship YouTube table as supporting detail.
- **Source of truth = the doc (Path A):** master is Sara's hand-edited OneDrive file `OneDrive - Microsoft\FY26 Impact Report\DevRel-Studios-FY26-Impact-Report.docx` (shared folder, also holds the `.xlsx`). Copilot does NOT regenerate/overwrite it — the `gen_combined_report.py`/`gen_report_workbook.py` generators are retired; Copilot provides paste-ready snippets instead.
- **Cost-avoidance total:** $7,752,323, going to **$7,777,323** once the new "Executive communication (bespoke production)" line (+$25K, bottom-up agency estimate) is added. Point-by-point to-do list for that edit already delivered (6 number swaps + 2 new table rows).
- **Money ledgers never summed:** cost avoidance vs. funded-by-others ($78,604 cross-charges) vs. promo ad-buys ($318,000).
- **Open follow-ups:** (1) Sara to hand-apply the exec-comm line edits; (2) confirm Imagine Cup scope (may lower below $400K); (3) authoritative series view counts from Aurea; (4) click Share on the OneDrive folder to grant James + Patrick access; (5) mirror the exec-comm line into the workbook.
- **Note:** Anthropic appears twice (MCP Dev Days partnership) — verified accurate from the July MBR; Sara chose to keep.

### "Behind the Code" — one-slide pitch (boss's template)
- **Status:** slide built, in review (2 open cosmetic follow-ups)
- **What:** Added a new **SHOW 04 · Behind the Code** slide to the July Studio Update deck by cloning the existing "Built It" show-slide template (PowerPoint COM `Duplicate()`), then mapping the pitch into the FORMAT / THE PITCH / 3-blocks / SUCCESS skeleton.
- **File:** `~/Downloads/StudioJulyUpdate2026_SF_BehindTheCode.pptx` → **slide 6**. Saved natively by PowerPoint (opens clean).
- **Open follow-ups:** (1) shorten the tag "AT THE WHITEBOARD · DECISION WALKTHROUGH" so it fits one line (it currently wraps + crowds the photos); (2) swap the 3 thumbnail photos inherited from Built It for Behind the Code imagery (PM-at-whiteboard shots).
- **Source template:** Sara's OneDrive copy `StudioJulyUpdate2026_SF.pptx` (boss Golnaz's original is in *her* OneDrive, `…/p/golnazal/…`). Deck was generated by PptxGenJS.

### Microsoft Scout (formerly "Clawpilot") install
- **Status:** blocked — needs admin to enable
- **What:** Downloaded the **x64** installer (aka.ms/msscout) for Sara's Intel i7-1265U / Win11 build 26200. Prereqs OK. Hit "Ask your admin to enable Microsoft Scout."
- **Why blocked:** two admin gates, both required — (1) Copilot Frontier in M365 admin center, (2) Intune policy + Frontier attestation. Needs M365 Copilot + GitHub Copilot Business/Enterprise licenses.
- **Next:** an admin-request email was drafted but not yet sent (no recipient chosen). Admin docs: learn.microsoft.com/en-us/microsoft-scout/admin-access-overview

### Shared youtube-collaborator skill with Chris (team editor)
- **Status:** done (one resend pending)
- **What:** Sent Chris (v-chrisar@microsoft.com, RUN Studios LLC) a plain-language guide + a zip of the skill (SKILL.md + INSTALL.md) via Teams so she can run "add a collaborator" herself.
- **Note:** the sent zip predates the later "⚠️ Reliability & Sharing" edit to SKILL.md — offered to resend the updated version (not yet done).

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
- **What:** Set up YouTube Data API OAuth and enhanced youtube-api.js with view count stats
- **Notes:** Tokens actually exist for **6 channels** — azd, dotnet, msdev, reactor, vs (+ credentials.json), not just 3. msdev re-authed 7/8. Quest to Compile Ep 1 had 2,526 views as of May 15.

## On Hold

## Recently Completed

### Transcript-proofread skill validation (PR #217)
- **Status:** completed (7/10)
- **What:** Downloaded and tested the new `transcript-proofread` skill from `microsoft/mvp-copilot-plugins` PR #217 end-to-end using a real YouTube caption export, generated corrected clean captions, and uploaded the corrected track to YouTube.
- **PR outcome:** PR #217 is approved by Sara. Local hardening edits were intentionally left unpushed.
- **Reference video tested:** https://youtu.be/5YnH1gTI1Yg

### Copilot Workspace Setup
- **Status:** complete
- **What:** Forked from Cameron's template, added tool-awareness rule, ran setup interview to build `context/me.md`
- **Notes:** Identity, studio, references, and projects context files all populated
