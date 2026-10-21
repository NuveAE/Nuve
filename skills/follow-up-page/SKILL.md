---
name: follow-up-page
description: Alejandro's Nuve post-meeting recap page. After a call or demo with a contractor, builds their branded recap on GitHub Pages (their logo on the stat, what they told him, how Nuve fixes it, ROI calculator, their questions answered, agreed next steps, booking) and returns the link plus a follow-up text. Use for /follow-up-page, "make a follow-up for [company]", or "recap page for my meeting with [name]".
---
# Nuve follow-up recap page

After Alejandro meets with a lead, he sends a recap page to push them over the edge. It shows their logo on the Nuve stat again, then uses what they said in the meeting: their pain points in their own terms, how each Nuve feature fixes it, a live ROI calculator seeded with their install volume, answers to the questions they asked, the next steps you agreed on, and his HubSpot calendar to lock in the next step.

Everything lives in the repo **NuveAE/Nuve** (GitHub Pages, branch `main`, root). The generator and templates are in the repo, so this skill only runs them. Never hand-edit a page per prospect; change `tools/template_followup.html` if the copy needs to change for everyone.

- Script: `tools/make_page.py --mode followup` (template `tools/template_followup.html`)
- Rep details (name, phone (949) 912-1816, email, booking link https://meetings.hubspot.com/alejandro677): `tools/config.py`
- Live URL: `https://nuveae.github.io/Nuve/<slug>-recap/` (separate from any cold page for the same company)

## Steps

1. **Gather what happened in the meeting.** In order of preference:
   - Notes Alejandro pastes or tells you.
   - HubSpot (read only): the company and contact, plus meeting, call and note engagements logged in the last couple of weeks.
   - The calendar event and any email thread with the contact.
   If there's nothing about the meeting anywhere, ask him for 3 quick things: what's hurting them, what they asked, what you agreed to do next. Don't make up pain points, quotes or numbers.

2. **Turn the notes into inputs.** Use their words, keep each item short.
   - `--first`, `--company`, `--short` (what they call themselves), `--city`.
   - `--met`: when you talked ("on Tuesday", "this morning").
   - `--pains`: 2 to 4 things they said are costing them, `Title::detail|Title::detail`. Put a real number in the detail if they gave one (lead cost, slow months, membership count).
   - `--next`: the steps you actually agreed on, `Step::detail|...`. If none were agreed, use: send logo → pick pilot installs → go live.
   - `--qa`: questions they asked with honest answers, `Question::Answer|...`. Only answer with what Alejandro said or what you know is true about Nuve; if unsure, leave that question out and flag it to him.
   - `--installs`: their installs + replacements per year if they mentioned it (seeds the calculator).
   - `--offer`: only if Alejandro actually offered something time-bound. Never invent urgency or pricing.
   - `--servicetitan` / `--plumbing` when true for them.
   - `--audience owner` when they aren't a contractor (property owners, rentals, venues, property managers). Swaps the lead/service-ticket copy and calculator for branding, messaging and run-time savings.

3. **Get the logo.** Reuse it from their cold page folder if one exists (`<slug>/stat.png` can't be reused, but the original logo file may be in the conversation or HubSpot); otherwise the attached file, else fetch from their site, else ask.

4. **Clone or update the repo** and install deps if missing (`numpy pillow scipy opencv-python-headless`, ffmpeg).

5. **Build.**
   ```
   python3 tools/make_page.py --mode followup --company "<Company>" --logo <logo> --first <Name> --met "<when>" \
     --pains "..." --next "..." [--qa "..."] [--installs N] [--offer "..."] [--short X] [--city Y] [--servicetitan] [--plumbing]
   ```

6. **Check before pushing.** Look at `_check.png`, `og.jpg`, and skim the built `index.html` copy: every pain point and next step should read like something the prospect would recognize from the call. Fix logo placement with `--scale`, `--nudge-x/-y`, `--keep-dark`, `--color`.

7. **Publish.** `git add <slug>-recap && git commit -m "Add recap page for <Company>" && git push`. Confirm the URL returns 200.

8. **Hand back** the link and a follow-up text in Alejandro's voice that references the meeting, short:
   > <First>, great talking <when>. Put everything we covered in one place for <Short>, including what it's worth on your numbers: <link>. Next step is <first agreed step>, want to lock in a time?

   Offer a short email version too. If HubSpot is connected, offer (don't do it unasked) to log a note on the contact with the link.
