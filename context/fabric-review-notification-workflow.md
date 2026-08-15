# Fabric Review Draft and Notification Workflow

## Trigger

- Ask Copilot CLI to draft a Fabric review email.
- Provide the ADO Episode work item ID and Frame.io review link.

## Automated Draft Creation

- Copilot reads the Episode title and current production dates from ADO.
- It creates an addressed email in Sara's Outlook Drafts folder.
- The draft includes clickable links to the ADO Episode and Frame.io review.
- Copilot verifies the saved recipients, content, dates, and links.
- The stakeholder email is never sent automatically.

## Teams Notification

- After verification, Copilot posts to the dedicated **Meeting with Sara
  Finkelstein** Teams chat.
- The notification includes:
  - Episode work item ID and title
  - Clickable ADO Episode link
  - Direct Outlook draft link
- Copilot marks the Teams chat unread so it becomes bold and creates a taskbar
  notification.
- If the Teams post or mark-unread action fails, Copilot sends the notification
  to Sara by self-email.

## Manual Proof and Send

- Sara opens the exact Outlook draft from the Teams link.
- Sara checks the recipients, wording, review deadline, delivery date, and
  publication date.
- This proof step is intentional because production schedules can slip.
- Sara clicks **Send** when everything is correct.

## Automatic ADO Discussion Record

- After sending, Sara tells Copilot `I sent it`, provides the Episode ID, or
  pastes the email subject.
- Copilot retrieves the final message directly from Outlook Sent Items; Sara
  does not need to paste the email body.
- It scans Sent Items rather than Outbox because Outbox messages may not have
  been delivered yet.
- The final sent message is copied to the matching ADO Episode discussion.
- The ADO comment includes the complete email plus From, To, CC, subject, sent
  time, Frame.io link, and ADO link.
- The Outlook message ID is recorded so the same email is never copied twice.
- Drafts and unsent messages are never copied.
- Sara's only manual steps are proofreading, sending, and telling Copilot that
  the message was sent.

## Scheduled V2 Feedback Reminders

- Weekdays at 10:00 AM Pacific: check for feedback due the next business day.
- Weekdays at 9:00 AM Pacific: check for overdue feedback.
- Eligible reminders are created as Outlook drafts and are never sent
  automatically.
- Copilot posts the same detailed Teams notification and marks the chat unread.

## Daily Fabric Control-Tower Briefing

- At 9:30 AM Pacific on weekdays, Copilot reviews the live current-year Fabric
  backlog in ADO.
- It reports only exceptions and near-term milestones, not every healthy
  Episode.
- The briefing includes:
  - **Heads-up** items due within the next two business days
  - **Action today** items that are due now or overdue
  - Overdue, unassigned, undated, or conflicting work
  - Episodes waiting on stakeholders
  - One clear next action and owner for each actionable Episode
- Known upcoming deadlines are surfaced in advance rather than appearing for
  the first time on the due date.
- Every Episode has a clickable ADO link and shortened title or guest names.
- The briefing is posted to the dedicated Teams feed and marked unread so it
  becomes bold.
- When nothing needs attention, no message is posted.

## Publishing-Ready Alerts

- Copilot watches for a Fabric Publishing child moving from **New** to
  **In Progress**.
- Each qualifying transition produces one Teams notification containing the
  Episode details and clickable ADO link.
- Duplicate notifications are prevented.

## Outlook Calendar Callouts

- Copilot reads current Fabric review, final-delivery, and publication dates
  from ADO.
- Each milestone appears twice on Sara's Outlook calendar:
  - An all-day callout at the top of the calendar
  - A 15-minute appointment at the actual deadline time with a reminder
- Calendar items include the Episode title and clickable ADO Episode link.
- Categories make milestones easy to scan, such as **Feedback due**,
  **Version 2**, **Final delivery**, and **Publish**.
- Calendar items are private appointments, not meeting invitations, so guests
  and stakeholders are not contacted.
- Existing callouts are updated when ADO dates change rather than duplicated.
- Sara should still proof the Outlook email draft before sending because a
  schedule may change after a calendar callout was created.

## What Is Personal vs. Shareable

- The workflow pattern is shareable with other producers: ADO dates create
  calendar callouts, Outlook drafts remain unsent, and Teams links provide a
  proof-and-send handoff.
- Sara's exact Teams chat, recipients, Outlook categories, and Fabric schedule
  rules are personal configuration and should be replaced with each producer's
  own settings.
