---
name: create-episode-metadata-from-transcripts
description: >
  Use when the user wants end-to-end YouTube metadata for a DevRel Studios episode and
  wants it written to the ADO Episode work item — including requests like "generate metadata
  for this episode", "write the description to ADO", "make the metadata match our show style",
  "stage this episode's metadata", or when they provide a video/transcript for a known series.
  Acquires a transcript, generates a full metadata package with the DevRel M365 agent, MATCHES
  THE SERIES' HOUSE STYLE by referencing a prior published episode, and writes the external
  fields to the Azure DevOps Episode work item. Works for any show/series, not just one.
---

# Create episode metadata from transcripts

End-to-end skill: turn an episode recording (or transcript) into YouTube-ready metadata that
**matches the established style of that specific series**, then write it to the Azure DevOps
Episode work item.

The critical differentiator vs. a generic metadata generator: **every show has its own house
style** (title suffix, description boilerplate, chapter header format, where hashtags live,
speaker-bio conventions). This skill learns that style from a *prior published episode of the
same series* before writing anything — so output is consistent across a show.

## Where the work lives (defaults)

- **ADO org/project:** `dev.azure.com/devrel`, project **`Studios`**. All DevRel Studios
  episodes live here. Do not ask the user which project unless the work item isn't found.
- **Work item type:** `Episode`. Each Episode sits under a Show (its `System.AreaPath`,
  e.g. `Studios\Shows\Microsoft MVP Unplugged`).

## Prerequisites

- **Azure DevOps MCP server** (`ado-*` tools) — for reading/writing work items.
- **Work IQ** (`work-iq-ask`) — to call the DevRel metadata agent (see Step 3).
- **A transcript** — `.srt`/`.vtt`. If you only have a video, use the **`video-chapters`**
  skill's pipeline to produce one (Frame.io share link → browser download → local
  faster-whisper). See that skill for the hardened, working path.
- **Automation policy:** API/tool-native path first. Use Playwright only as a fallback when the
  asset is browser-gated and no reliable API route is available.

---

## Workflow

### Step 1 — Identify the Episode and its series

1. Resolve the ADO Episode work item ID. It's often embedded in the video filename
   (e.g. `MUP_222346_...` → work item `222346`). Confirm by fetching it:
   `ado-wit_get_work_item` and check `System.WorkItemType = Episode` and `System.Title`.
2. Note the **series** from `System.AreaPath` (e.g. `Studios\Shows\Microsoft MVP Unplugged`)
   and the host/guest fields (`Custom.Host1`, `Custom.Remotepresenters`).

### Step 2 — Get the transcript

- If a `.srt`/`.vtt` is provided or already on disk, use it.
- Otherwise run the **`video-chapters`** pipeline to transcribe the source video.
- Always read the FULL transcript before generating output.
- Offer to also save a clean **proofing `.txt`** (readable, light `[m:ss]` anchors) using
  `skills/video-chapters/srt-to-txt.js <input.srt> <output.txt>` (input = argv[2],
  output = argv[3]; it refuses to run if output == input).

### Step 3 — Generate the metadata package (DevRel M365 agent)

Call the **DevRel metadata agent** via Work IQ. It produces titles, a structured description,
chapters, tags/keywords, and hashtags from a transcript.

- Tool: `work-iq-ask`
- **agentId:** `T_0428a450-e4c0-56de-d33f-205c21eedc48.e55bd3b5-d403-4700-b434-52ad50219626`
  ("DevRel Agent v2")
- Reuse the returned `conversationId` for follow-ups.
- In the prompt, provide: show name, host, guest (name + title/company + any links),
  the transcript (SRT preferred for accurate chapter timing), and **cleanup notes** for any
  mis-transcribed terms (product/model names, etc.). Ask for the "full package."

> The agent's default output is generic. It is Step 4's job to reshape it into the series style.

### Step 4 — ⭐ STYLE REFERENCE CHECK (do this BEFORE writing to ADO)

**Never write generic metadata.** First learn the series' house style from a prior published
episode, then conform the generated metadata to it.

**Decision rule (hard):**
- If a valid reference episode exists, run in **Pattern-Lock mode**: mirror the existing pattern
  exactly across structure, section set, markers, and formatting conventions. Do **not** invent
  new stylistic elements.
- Only originate or change style when **no valid reference exists** or the producer explicitly
  asks to change it.

1. **Find sibling episodes** in the same series (same `AreaPath`) with `ado-wit_query_by_wiql`:
   ```sql
   SELECT [System.Id], [System.Title], [System.State]
   FROM WorkItems
   WHERE [System.WorkItemType] = 'Episode'
     AND [System.AreaPath] = '<the show's area path>'
   ORDER BY [System.ChangedDate] DESC
   ```
2. **Pick a reference episode**: the most recent one that is **published/`Completed`** AND has
   populated external fields. Skip the current episode and any with empty metadata.
3. **Read the reference's external fields** (`ado-wit_get_work_item`, expand=fields):
   `Custom.Videotitleext`, `Custom.Videodescriptionexternal`, `Custom.Chaptermarkersexternal`,
   `Custom.Resourcelinksexternal`, `Custom.Speakersociallinksexternal`.
   (Fields are HTML — parse with a quick `ConvertFrom-Json` in PowerShell if the payload is large.)
4. **Extract the conventions** and apply them to the generated metadata:
   - **Title** — suffix/branding pattern (e.g. `… | <Show Name>`), casing, length.
   - **Description** — the fixed opening sentence(s), section headers and emoji
     (e.g. `⭐ What You'll Learn`, `👥 Speakers`), whether **full speaker bios + social links**
     are expected (host bio is often reusable boilerplate), and any **About <Show>** boilerplate
     block that should be copied verbatim. Also match the **bullet marker style** under
     `What You'll Learn` (e.g., plain bullets vs `✅` prefixed bullets) from the reference
     episode.
   - **Chapters** — header text (e.g. `✅ Chapter Markers`), timestamp format
     (`MM:SS – Title` with en-dash and leading zeros vs. `M:SS - Title`), standardized first
     entries (e.g. `00:00 – Intro to <Show>`, `00:20 – Meet <Guest>`), and **granularity**
     (some shows want ~30+ granular markers, not a trimmed 10 — match the reference unless the
     producer says otherwise).

     - **⭐ Write SEO-optimized chapter headings, not generic ones.** YouTube indexes chapter
       titles (they surface as "key moments" and add keyword coverage), so treat each heading as
       a search asset. **Front-load high-value, searchable terms** — product/app names, model
       names, and technique keywords (e.g. `AI Story Builders`, `Claude Opus 4`, `RAG (Retrieval
       Augmented Generation)`, `Cosine Similarity`, `Knowledge Graphs`, `Microsoft Store`).
       Avoid filler that buries keywords (`Demo: the app`, `Under the hood`, `How it's built`,
       `Settings & setup`). Prefer `03:31 – AI Story Builders Demo & Install (Microsoft Store)`
       over `03:31 – Demo: the app & how to install`.
     - **Note the style-vs-SEO tension:** the house style may favor *descriptive/fun* headings
       while SEO favors *keyword-front-loading*. Lean SEO for discovery, keep it accurate, and
       surface the trade-off to the producer so they can choose.
   - **Resource links** — header/emoji-bullet format, the Subscribe CTA, and **where hashtags
     live** (in some shows the hashtags sit at the bottom of the resource-links field, not in a
     separate field).
   - **Speaker social links** — format (e.g. simple LinkedIn URLs).
5. Note any per-episode gaps the style requires (guest bio, guest GitHub/repo, LinkedIn URLs)
   and either gather them or flag them for the producer.
6. **Section parity check (required):** compare reference vs draft and ensure no section is
   dropped/added unintentionally. The same section set must be present:
   - Description intro + second paragraph
   - `⭐ What You'll Learn` (including marker style)
   - `👥 Speakers`
   - `About <Show>`
   - `✅ Chapter Markers`
   - `🔗 Resources & Links` + Subscribe CTA + hashtags placement
   - Speaker social links block

### Step 5 — Prepare final metadata package

Show the producer the styled metadata (title, description, chapters, resource links, speaker
links), and call out which reference episode you matched (`Ep N: <name>`, ID). Flag any
placeholders that need real URLs/handles before publishing. Let them pick/adjust the title —
**default to keyword-first titles** (front-load high-volume dev search terms).

### Step 6 — Write to ADO (default behavior)

Write the styled metadata to the Episode's external fields with
`ado-wit_update_work_items_batch` (op `Replace`, `format: "Html"`).

**Field map:**

| Field | Reference name |
|---|---|
| Video title (External) | `Custom.Videotitleext` |
| Video description (External) | `Custom.Videodescriptionexternal` |
| Chapter markers (External) | `Custom.Chaptermarkersexternal` |
| Resource links (External) | `Custom.Resourcelinksexternal` |
| Speaker social links (External) | `Custom.Speakersociallinksexternal` |

Rules:
- **Chapters go in `Custom.Chaptermarkersexternal`**, not in the description field.
- **Never auto-overwrite** a field that already has content — show existing vs. generated and
  ask per field.
- Values are HTML (use `<div>`/`<br>`, escape `&`, `"`, quotes).
- **Title field guardrail:** `Custom.Videotitleext` should be plain display text, not HTML-escaped
  text. Write `&`, not `&amp;` in the final title value.
- **Speaker links guardrail:** keep `Custom.Speakersociallinksexternal` terse (one line per person,
  link-first). Do not paste bios here. Put bios only in `Custom.Videodescriptionexternal`.
- **Execution policy:** when a clear Episode WI ID is provided and target fields are unambiguous,
  write updates to ADO in the same run (no pre-write pause). Only pause before writing when target
  is ambiguous or the producer explicitly asks for a dry run.
- After writing, give the producer the direct link:
  `https://dev.azure.com/devrel/Studios/_workitems/edit/<ID>`.

### Step 7 — Post-write formatting QA (required)

Immediately re-read all five external fields and validate these exact checks before calling done:

1. `Custom.Videotitleext` has no escaped entities (`&amp;`, `&quot;`, etc.) unless intentional.
2. `Custom.Videodescriptionexternal` contains sections in order:
   intro → second paragraph → `⭐ What You'll Learn` → `👥 Speakers` → `About <Show>`.
   Bullet marker style in `What You'll Learn` must match the reference episode.
3. `Custom.Chaptermarkersexternal` has `✅ Chapter Markers` and one `MM:SS – Title` per line.
4. `Custom.Resourcelinksexternal` includes `🔗 Resources & Links`, Subscribe CTA, and hashtags at
   the very bottom.
5. `Custom.Speakersociallinksexternal` is concise, one speaker per line, with only social/site
   links (no long-form bio text).
6. **Pattern-Lock parity:** if a reference exists, no unapproved stylistic drift from reference in
   headers, marker style, section presence, or placement rules.
7. Completion handoff message should be explicit:
   **"I'm done, please check everything before you publish to YouTube."**

---

## Reference: Microsoft MVP Unplugged house style

Captured from the published Ep 2 (Veronika Kolesnikova, WI 198162). Use as the template for
this series; re-derive per series for other shows.

- **Title:** `<keyword-rich descriptive title> | MVP Unplugged`
- **Description structure:**
  1. `Welcome to the next **MVP Unplugged**, where Microsoft MVPs share real-world projects and
     insights from the field! In this episode, host **Justin Garrett** sits down with Microsoft
     MVP **<Guest>** to explore <topic>…`
  2. A second paragraph: "<Guest> walks through <their process>…"
  3. `⭐ What You'll Learn` — bulleted list
  4. `👥 Speakers` — **full bio + LinkedIn** for guest AND host. Justin's bio is reusable
     boilerplate: *"Justin Garrett is host of MVP Unplugged, Principal PM in Developer Relations
     which is part of Microsoft Cloud + AI…"* + `https://www.linkedin.com/in/justgar/`
  5. `About MVP Unplugged` — fixed boilerplate paragraph (copy verbatim from a prior episode)
- **Chapters (`Custom.Chaptermarkersexternal`):** header `✅ Chapter Markers`; format
  `MM:SS – Title` (en-dash, leading zeros); first two entries standardized:
  `00:00 – Intro to MVP Unplugged`, `00:20 – Meet Microsoft MVP <Guest>`; **granular (~30+
  markers)** across the full runtime.
- **Resource links (`Custom.Resourcelinksexternal`):** header `🔗 Resources & Links`; emoji
  bullets (`🎁` free trial, `📚`/`📘` docs, `💻` guest repo, `🚀` Try GitHub Copilot); a bold
  Subscribe CTA; **hashtags line at the bottom of THIS field** (e.g.
  `#MicrosoftDeveloper #MVPUnplugged …`).
- **Speaker social links (`Custom.Speakersociallinksexternal`):** simple LinkedIn URLs for
  guest and host.

---

## Edge cases

- **No prior published episode** (brand-new series): there's no style to match — generate clean
  metadata, tell the producer no reference existed, and treat this episode as the future template.
- **Reference fields are empty/partial:** fall back to the next-most-recent published episode.
- **Producer overrides the style** (e.g. "only 10 chapters this time"): honor the producer;
  the style check informs, it doesn't dictate.
- **Missing per-episode assets** (guest LinkedIn, repo URL, Store link): insert a clearly
  marked `[confirm before publishing]` placeholder rather than guessing/fabricating a URL.
- **Work item not found in `Studios`:** only then ask the user for the project/ID.
