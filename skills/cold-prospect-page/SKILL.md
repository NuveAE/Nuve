---
name: cold-prospect-page
description: Alejandro's Nuve cold-outreach demo page. Puts a contractor's logo on the Nuve stat, builds their personalized phone page on GitHub Pages, and returns the link plus a ready-to-send text. Use for /cold-prospect-page, "make a cold page for [company]", or a logo + "build their demo".
---
# Nuve cold prospect page

Alejandro texts or emails cold prospects a link to a phone page built for their company: their logo on the Nuve stat, the Nuve story, five real contractor testimonials, the Ismael section, and his HubSpot calendar at the bottom. The iMessage link preview is their stat on a dark background. The goal is to spark interest and get a 15-minute call booked.

Everything lives in the repo **NuveAE/Nuve** (GitHub Pages, branch `main`, root). The generator and templates are in the repo, so this skill only runs them. Never hand-edit a page per prospect; change `tools/template_cold.html` if the copy needs to change for everyone.

- Script: `tools/make_page.py` (default mode is cold; template `tools/template_cold.html`)
- Rep details (name, phone (949) 912-1816, email, booking link https://meetings.hubspot.com/alejandro677): `tools/config.py`
- Live URL: `https://nuveae.github.io/Nuve/<slug>/`

## Steps

1. **Get the inputs.**
   - Company name: from the message, the logo file name, or the HubSpot company.
   - Website: the URL in the message, else the `domain` on the HubSpot company.
   - Optional: decision-maker first name and city. If given a HubSpot link or only a company name, look it up in HubSpot (read only: company name, city, domain, associated contact first name). Never write to HubSpot from this skill.
   - Hook (optional but makes it land): one short, true, specific line about why you're reaching out, e.g. something from their site or Google profile ("Saw you just opened a second location in Irvine."). Only use facts you actually found. If nothing solid, skip it.
   - Flags: `--servicetitan` if they run ServiceTitan (their site, job posts, or HubSpot say so); `--plumbing` if they also do plumbing.

2. **Get the logo.** Use the file Alejandro attached. If he didn't attach one, try fetching it from their website; if the site can't be reached from here, ask him to attach the logo (PNG with transparent background is best). Don't invent or redraw a logo.

3. **Clone or update the repo** (`git clone https://github.com/NuveAE/Nuve` or `git pull`). Install deps if missing: `pip install numpy pillow scipy opencv-python-headless --break-system-packages`, and ffmpeg.

4. **Build.**
   ```
   python3 tools/make_page.py --company "<Company>" --logo <logo> [--first <Name>] [--city <City>] [--hook "<line>"] [--short <Short>] [--servicetitan] [--plumbing]
   ```

5. **Check the output before pushing.** Open `<slug>/_check.png` (logo on the stat), `<slug>/og.jpg` (iMessage preview) and `<slug>/_check_videos.png` / `_check_more.png`. If the logo is too big, small, off-center or washed out, rebuild with `--scale 0.85`, `--nudge-x/-y`, `--keep-dark` or `--color "#hex"`. Don't commit `_check*` files (gitignored).

6. **Publish.** `git add <slug> && git commit -m "Add cold page for <Company>" && git push`. Pages updates in about a minute; confirm the URL returns 200 before handing it over.

7. **Hand back** the link and a ready-to-send first-touch text, short and in Alejandro's voice, no hype words:
   > Hey <First>, Alejandro with Nuve. Made this for <Company>, it's your logo on the thermostat your customers would see every day: <link>. Worth 15 min?

   Also offer a one-line email version if he's emailing instead.
