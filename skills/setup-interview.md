# Setup Interview

## What it does
Interactive onboarding questionnaire that builds out your `context/me.md` file from your answers. Run this once when you first set up your workspace.

## When to use it
First time setting up your Copilot workspace, or when you want to rebuild your profile from scratch.

## How to run it
Copy the prompt below and paste it into Copilot CLI or VS Code Copilot Chat. Answer each question — Copilot will use your responses to generate a complete `context/me.md`.

## Prompt

```
I'm setting up my Copilot workspace for the first time. Walk me through an interview to build out my context/me.md file. Ask me the following questions ONE AT A TIME — wait for my answer before moving to the next question. After all questions are answered, generate a complete context/me.md file I can review and save.

Questions:

ROLE & RESPONSIBILITIES
1. What's your job title?
2. In one sentence, what does your day-to-day work actually look like?
3. What do you own or contribute to regularly? (projects, processes, deliverables)

TOOLS & ENVIRONMENT
4. What software and tools do you use most days? (editors, apps, services, platforms)
5. How comfortable are you with the terminal / command line? (never used it / basics / comfortable / power user)
6. Do you write code as part of your work? If so, what languages or platforms?

WORK STYLE & COMMUNICATION
7. When you ask an AI a question, do you want:
   a) Just the answer — short and direct
   b) The answer with a brief explanation of why
   c) A thorough walkthrough so you understand the full picture
8. How do you prefer information structured?
   a) Bullet points — scannable, concise
   b) Short paragraphs — conversational
   c) Step-by-step instructions — sequential
9. When there are multiple ways to do something, do you want:
   a) Just the best option — decide for me
   b) Two options with trade-offs — let me pick
   c) All viable options laid out
10. How do you feel about being corrected or getting pushback from AI?
    a) Go for it — tell me if I'm wrong
    b) Suggest alternatives gently
    c) Just do what I ask

SKILLS & GROWTH
11. What are you strongest at in your current role?
12. What are you actively trying to learn or get better at?
13. Is there anything you regularly struggle with or find tedious that you'd love help automating?

TEAM CONTEXT
14. Is there anything specific about your team's workflow, tools, or conventions that Copilot should know about?

After I answer all questions, generate my context/me.md using the format in this repo and show it to me for review before saving.
```

## What good output looks like
The generated me.md should:
- Use the person's actual words and specifics, not generic filler
- Capture their communication preferences as behavioral instructions (e.g., "Be direct — I prefer bullet points over paragraphs")
- Reflect their real skill level honestly (don't inflate or deflate)
- Include the "tedious tasks" answer as context for future pattern detection
