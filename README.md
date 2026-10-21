# Nuve

Alejandro's personalized Nuve pages for HVAC / plumbing contractors, one folder per company, hosted on GitHub Pages.
Adapted from Will Arana's `nuve-demo` generator.

Two kinds of page:

| Mode | For | Folder | Ends with |
|---|---|---|---|
| `cold` (default) | Cold outreach. "Here's your logo on the stat." | `<slug>/` | Book 15 min |
| `followup` | After a meeting. Recap, their pain points, ROI calculator, agreed next steps, their questions answered. | `<slug>-recap/` | Lock in next step |

## Build

    pip install numpy pillow scipy opencv-python-headless   # ffmpeg must be on PATH

    # cold
    python3 tools/make_page.py --company "Summit Heating & Air" --logo logo.png --first Mike --city Phoenix \
        --hook "Saw you just added a second truck in Phoenix."

    # follow-up
    python3 tools/make_page.py --mode followup --company "Summit Heating & Air" --short Summit --logo logo.png \
        --first Mike --met "on Tuesday" \
        --pains "Buying the same customer twice::~\$110/lead on Google Ads|Slow shoulder seasons" \
        --next "Send your logo::We build your stat + app mockup|Pick 10 pilot installs|30-day check-in" \
        --qa "How long to go live?::About two weeks after we get your logo." \
        --installs 300 --offer "Your pilot spot is held through Nov 15"

Each build writes `index.html`, `stat.png` (hero), `og.jpg` (iMessage preview) and branded clips into the folder,
plus `_check*.png` review images (not committed). List fields are `|`-separated; `Title::detail` adds a detail line.

Link: `https://nuveae.github.io/Nuve/<slug>/`

Options: `--slug`, `--short`, `--keep-dark`, `--scale 0.9`, `--nudge-x/--nudge-y`, `--color "#hex"`, `--tile-color`,
`--no-videos`, `--plumbing` (water-sensor section), `--servicetitan` (Works with ServiceTitan section).

## Where things are

- `tools/config.py` – your name, phone, email, booking link, GitHub user. Change here once.
- `tools/template_cold.html`, `tools/template_followup.html` – page copy and layout.
- `tools/make_page.py`, `tools/brand_videos.py`, `tools/stat_base.png` – the generator.
- `assets/` – shared clips and images. `alejandro.jpg` is a placeholder headshot; replace it with a real photo (same name).
- `skills/` – the two Claude skills that run this (cold-prospect-page, follow-up-page).
