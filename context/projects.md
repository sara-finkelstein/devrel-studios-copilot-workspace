# Current Projects

<!-- Track what you're working on. Copilot uses this to stay relevant when you ask about priorities or next steps. -->

## Active

### MCP Dev Days — post-event on-demand episodes
- **Post Event hierarchy completed 8/27:** [Post Event 231954](https://dev.azure.com/devrel/Studios/_workitems/edit/231954) now directly contains eight New on-demand Episodes, [242418](https://dev.azure.com/devrel/Studios/_workitems/edit/242418) through [242425](https://dev.azure.com/devrel/Studios/_workitems/edit/242425), using Live Show Session IDs `[100]`–`[107]`.
- **Assignments and deadlines:** all eight Episodes and their Editing children are assigned to Chris Armstrong (RUN Studios LLC) and due September 15, 2026 at 9:00 AM Pacific. Speaker names are populated from the run-of-show workbook.
- **Hierarchy cleanup:** removed all generated Scheduling items and the obsolete `Edit on demand sessions (episodes pending)` branch. Each Episode retains only its Editing, Uploading, and Publishing children.
- **Source:** [MCP Dev Days September 9 run of show](https://microsoft.sharepoint.com/:x:/t/MicrosoftDeveloperStudiosChannel9/cQpWBMeu7uRnRJLzDYnLdhe2EgUCF3aerOLNuqf_ztn0xTLgFw). Remaining Episode fields will be populated from the workbook later.

### MCP Live! — production and social promotion
- **Social-promotion history captured 8/21:** [General 239709 — Social media promos](https://dev.azure.com/devrel/Studios/_workitems/edit/239709) now contains the complete 12:26 PM Cynthia Zanoni email plus one chronological source-of-truth timeline covering the Christian Booth and Doug/Cynthia Teams discussions. The record preserves source links and Outlook/Teams message IDs for deduplication.
- **Social decisions:** YouTube remains the primary livestream/view-count destination; promotion should use tracked Reactor/aka.ms registration links; the blue CTA pill can sit where Carlotta points; Doug will create YouTube Shorts and TikTok versions once the correct tracking codes are supplied.
- **Social follow-up:** obtain final YouTube Shorts and TikTok aka.ms codes, decide whether Bluesky needs a separate version/link, and compare burned-in CTA performance with Instagram's “link in bio” approach.
- **BOC status:** pricing confirmed 8/11; team notification still needed
- **Current FY27 BOC rate:** Streaming Support is **$300/hour with a 2-hour minimum** ($600 minimum). AI captions add $30/hour; human live captions add $170/hour.
- **Communication check:** no email or Teams message was found where Pamela Fox or Liam Hampton were explicitly told about the new BOC livestreaming fee. The Aug. 10 MCP Live! check-in covered StreamYard and livestream setup, but not pricing.
- **Related history:** Pamela mentioned "$7,500 for half day for Studios" on May 27; that appears to be a studio-booking cost, not the newer BOC livestream support charge.
- **Source:** [FY27 Production Studios Services Rate Card](https://microsoft.sharepoint.com/teams/CurrentRateCard/Shared%20Documents/Information/Services%20and%20Cost%20Rate%20Card/FY27_ProductionStudios_Services_RateCard.pdf?web=1)

### Microsoft To Do transition + Teams note-to-self capture
- **Status:** live (set up 7/24) — gradual migration from OneNote
- **What:** Six separate Microsoft To Do lists now match Sara's high-level projects: Fabric Tech Talk Fridays & Executive Insights, Behind the Code, MCP Dev Days, MVP Unplugged, Studios, and Startup Shorts. Existing OneNote content remains untouched; selected tasks are migrated intentionally.
- **Teams capture:** Sara sends herself a Teams message using `#todo Project | Task | due Date`. Scheduled scans run weekdays at 9am, 12pm, 3pm, and 5pm, classify the task, create it in the matching To Do list, and deduplicate by Teams message ID.
- **Safety:** `context/pinned-teams-digest.md` is an append-only backup; `context/pinned-teams-state.json` tracks processed, pending, and needs-confirmation message IDs. Ambiguous project names or dates are held for confirmation instead of guessed.
- **Important limitation:** Work IQ search does not expose Teams reaction metadata, so the original 📌 reaction trigger was retired. The current scheduled helper uses desktop To Do automation and therefore needs the computer awake and unlocked.
- **Next:** switch the scheduled helper to Outlook COM task creation, which successfully created and updated To Do tasks, notes, and due dates without manipulating the To Do interface.

### Fabric Tech Talk Fridays & Fabric Executive Insights — status tracking
- **Status:** assessed 7/20; iteration paths cleaned up
- **What:** Reviewed both ADO Shows (#174864 FTTF, #224267 FEI) for outstanding work.
- **Done 8/25 — PR #230 ready for re-review:** addressed Golnaz's three follow-up correctness requests by making holiday retrieval direction-aware for backward workbacks, validating every fully merged preset variant, and rejecting unusable timed-calendar configurations. Added regression coverage, pushed commit `d4a09eb`, resolved all review threads, marked the PR ready, and requested Golnaz's re-review; required checks pass.
- **Done 8/21 — durable Fabric control tower:** replaced the experimental session-scoped Copilot schedules with seven Windows Scheduled Tasks for AM/PM Graph calendar reconciliation, V2 day-before/due-today-fallback/overdue drafts, a 9:30 AM exception-only briefing, and publishing-readiness audits at 10:30 AM and 4:30 PM Pacific (updated 8/28). The readiness audit treats parent Episode state `Publication` as editor approval, then requires the final file, thumbnail, external metadata, publication date, caption link, and VTT/SRT/TTML attachments before alerting that delivery is ready; speaker social links are optional. The runner checks both `System.Description` and `Custom.Notes`, catches up newly installed tasks after their scheduled time, prevents overlap, retries package-startup failures, rejects partial/throttled runs through a machine-readable completion status, logs each workflow, and automatically expires dated Episode suppressions at 9:00 AM. [Draft PR #230](https://github.com/microsoft/mvp-copilot-plugins/pull/230) requires a durable external scheduler instead of implying `/every` or `/after` survives CLI restarts.
- **Done 8/19 — live Graph calendar repair:** reconciled FY27 Fabric ADO milestones with Sara's Outlook calendar and created 16 missing private events (all-day plus timed) for Kim/Nathalie final delivery, Kanwal/Yitzhak final delivery, and Ron Chang's remaining review, final-delivery, and publication milestones. Read-back verification confirmed all markers, dates, categories, reminders, privacy/free status, and ADO links; Yitzhak Kesselman short Episode 237659 was already fully synchronized.
- **Done 8/27 — Episode 236856 transcript and metadata:** [Power BI Agent Skills with Swetha Mannepalli and Emily Lisa](https://dev.azure.com/devrel/Studios/_workitems/edit/236856) is in Publication for 8/28 with its final file, external title/description, resource links, chapter markers, thumbnail, and caption link populated. The proofread 132-cue package contains 62 corrections with unchanged timestamps; validated VTT, SRT, and TTML files are attached and linked in Discussion. The Publishing child moved to `In Progress`; its missed automatic alert was recovered and recorded. Speaker social links remain blank because none were verified; Sara should complete the final YouTube publishing check.
- **Episode 233550 delayed 8/19:** suppress all automated ADO updates, Outlook drafts/emails, Teams notifications, calendar actions, and reminders through 9/2. Automatically re-enable the Fabric reminder workflow at 9:00 AM Pacific on Thursday, 9/3.
- **Done 8/18 — Graph-first calendar reconciliation:** Microsoft Graph event create/read/delete was validated through Work IQ, Sara's personal Fabric skill was migrated away from classic Outlook COM, and weekday 8:30 AM/4:30 PM reconciliation schedules were added. [Draft PR #230](https://github.com/microsoft/mvp-copilot-plugins/pull/230) was updated and pushed with the same Graph-first identity, polling, and safety contract for the team workflow.
- **Done 8/12 — shared production-schedule PR feedback:** updated [draft PR #230](https://github.com/microsoft/mvp-copilot-plugins/pull/230) to support shoot-date-forward and publication-date-backward planning, stable Outlook appointment identities, complete operational preset validation, and DST-safe local-time conversion. All review threads were answered and resolved; required checks pass and the PR awaits Golnaz's re-review.
- **Done 8/5 — FY27 FTTF SMB Episodes created:** [237854 — How Azure Pricing Works | SMB](https://dev.azure.com/devrel/Studios/_workitems/edit/237854) and [237855 — Azure SKU Selection and Buying Options | SMB](https://dev.azure.com/devrel/Studios/_workitems/edit/237855) were created under Show 236193. Each generated Scheduling, Editing, Thumbnails, Uploading, and Publishing children; Swetha Mannepalli is Host 1, Anita Sheares is Content Owner, Matt Scholz is Technical Director, and Scheduling is assigned to Allison Dunmire.
- **Done 8/4 — Episode 233550 V1 review:** created and verified an addressed Outlook draft for Kanwal Safdar/Yitzhak Kesselman with a next-business-day 9:00 AM Pacific internal deadline; Sara sent it. Future Fabric V1 review drafts must include clickable links to both the ADO Episode and Frame.io review.
- **FY27 volume clarification 8/4:** Sara directly asked Golnaz how many videos were promised to the Fabric team. Golnaz's July 28 answer was **85–95 videos for FY27** based on roughly $50K/year; this supersedes the earlier ~50-video meeting estimate. Anita's separate series work was discussed as additional per-episode funding.
- **FTTF outstanding (as of 7/20):** 4 episodes stuck in Publication (upload/publish subtasks not started): Shannon Lindsay (231676), Ashley Felts (231681), Porsche Cup & Kumulus (225198), AvePoint (228756). 2 on Hold: Kalyan Kaki (182347), Heini Ilmarinen (198295). 1 new unreviewed proposal: SMB Cost Clarity + Pricing series (236026, desired publish 9/7/26).
- **FEI outstanding (as of 7/20):** Post Production — dbt + Fabric (228786), Kim Manis/Nathalie D'Hers (232500). Production — Bogdan Crivat/Patrice Pelland (233043), Kanwal Safdar/Yitzhak Kesselman (233550, no movement since 6/25). Hold — Financial Services Leaders (227316), Open Data Interoperability (227885). Postmortem (224268) not started.
- **Done 7/20:** bulk-updated all 63 non-conforming FTTF child work items (Episodes, Editing/Uploading/Publishing, Graphics, Shorts) to Iteration Path `Studios\FY26`. FEI intentionally left untouched per Sara's request.
- **Done 7/21 — episode 228786 (dbt + Fabric) metadata pipeline practiced end-to-end:** downloaded Frame.io proxy via browser, transcribed locally (faster-whisper), generated full metadata package via DevRel agent, and wrote **chapter markers + resource links** to ADO. Title/description left untouched — `System.Description` note confirmed they're already approved (provided to team 6/9). Speaker social links still open — could not verify real LinkedIn/X URLs for Kyle Dempsey (dbt Labs) or Tino Tereshko (Microsoft) via web search; needs manual confirmation from Sara or the guests.
- **Publishing weekday confirmed 7/30:** Fabric Tech Talk Fridays publishes on Fridays; Fabric Executive Insights publishes on Tuesdays. Production schedules must use the correct series-specific weekday.
- **Done 7/30 — FY27 FEI schedule audit:** all non-dbt Episodes now have production schedules. Corrected publication dates and Publishing deadlines to Tuesdays for Kim/Nathalie (8/11), Kanwal/Yitzhak (8/18), and Bogdan/Patrice (9/22); V2 reminder dates were unchanged.
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
- **DDoS interview framing:** start by defining distributed denial of service in beginner-friendly language, then introduce protocol attacks with the transition, "But what if that traffic follows the rules?" Central hook: how Azure identifies legitimate-looking traffic being weaponized and stops the attack without blocking real customers. Core questions: how Azure distinguishes an attack from a genuine traffic surge; how attackers abuse normal internet rules; and how defenders protect customers without disrupting valid traffic.
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
- **ADO hierarchy created 7/24:** [Series #236646](https://dev.azure.com/devrel/Studios/_workitems/edit/236646), with Graphics #236648 and Postmortem #236647 generated by Studios automation. Four placeholder Episodes were created: #236649, #236650, #236655, and #236662; each received exactly one Scheduling, Editing, Uploading, and Publishing child.
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

### Complete Project Ingestion skill — Proposal to Episodes
- **Status:** draft team PR ready for Sara's review
- **GitHub:** [Issue #223](https://github.com/microsoft/mvp-copilot-plugins/issues/223) · [Draft PR #224](https://github.com/microsoft/mvp-copilot-plugins/pull/224)
- **What:** Replaced the stale Excel-first local Series workflow with a proposal-first team skill. Normal path: approved Proposal → `Ready for project automation` → Power Automate creates Series/Event/Moment → producer completes detailed editable intake → Copilot creates Episodes → verifies generated production children. Direct top-level creation is restricted to explicit owner-led tests/recovery.
- **Validated live 7/24:** Proposal moved to `Ingested` and gained the automation-created Series as parent; standard Episodes generated Scheduling/Editing/Uploading/Publishing; Thumbnails-enabled Episodes generated those four plus one Thumbnails child.
- **Quality gate:** GitHub checks passed; 46 Python/Node tests passed; `github-pr-review` found and drove fixes for Event routing/input/option propagation, then returned **Approve**.
- **Next:** Sara has a To Do reminder to review draft PR #224 before requesting Golnaz/team review. Also test the manual fallback on a suitable Episode: inspect existing children, create only missing Scheduling/Editing/Uploading/Publishing/optional Thumbnails items, link them correctly, and verify no duplicates.

### YouTube API Setup
- **Status:** complete
- **What:** Set up YouTube Data API OAuth and enhanced youtube-api.js with view count stats
- **Notes:** Tokens actually exist for **6 channels** — azd, dotnet, msdev, reactor, vs (+ credentials.json), not just 3. msdev re-authed 7/8. Quest to Compile Ep 1 had 2,526 views as of May 15.

## On Hold

## Recently Completed

### Transcript proofreading + ADO caption delivery enhancement
- **Status:** merged (7/23)
- **What:** Extended the existing shared `transcript-proofread` skill (rather than creating an overlapping skill) to generate synchronized SRT/VTT/TTML files and optionally attach them to a confirmed ADO Episode.
- **Validated with:** FEI episode 228786 (dbt + Fabric) — proofread all 298 cues, generated all three caption formats, and attached them to the Episode.
- **Safety:** the skill confirms the exact ADO work item ID and project before attaching; the helper verifies the item exists and is an Episode, then skips filenames already attached.
- **GitHub:** [Issue #221](https://github.com/microsoft/mvp-copilot-plugins/issues/221) · [Merged PR #222](https://github.com/microsoft/mvp-copilot-plugins/pull/222)
- **Plugin delivery:** automatic maintenance is configured locally; `devrel-studios` will move from the old direct 0.1.0 install to team version 0.3.0 after all active Copilot CLI windows close.

### Transcript-proofread skill validation (PR #217)
- **Status:** completed (7/10)
- **What:** Downloaded and tested the new `transcript-proofread` skill from `microsoft/mvp-copilot-plugins` PR #217 end-to-end using a real YouTube caption export, generated corrected clean captions, and uploaded the corrected track to YouTube.
- **PR outcome:** PR #217 is approved by Sara. Local hardening edits were intentionally left unpushed.
- **Reference video tested:** https://youtu.be/5YnH1gTI1Yg

### Copilot Workspace Setup
- **Status:** complete
- **What:** Forked from Cameron's template, added tool-awareness rule, ran setup interview to build `context/me.md`
- **Notes:** Identity, studio, references, and projects context files all populated
