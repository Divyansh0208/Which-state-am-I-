# Which State Am I? — 2050 Edition

> A data-driven visual poster that encodes India's most populous state's identity through the lens of its 2050 future — **without naming the state once.**

**Hackathon:** Hack2Skill x Google for Developers — Mini Challenge 2  
**Theme:** Fast Forward to 2050  
**Deadline:** 07/06/2026 11:59 PM IST  
**Stack:** Python (Matplotlib + Pillow + Flask)

---

## Quick Start

```bash
# 1. Clone & enter
git clone https://github.com/Divyansh0208/Which-state-am-I-.git
cd Which-state-am-I-

# 2. Create virtual environment
python -m venv env
env\Scripts\activate          # Windows
# source env/bin/activate     # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Generate the poster
python generate_poster.py

# Output: MysteryState2050_Poster.png (2332x2332px, ~320 KB)
```

### CLI Options

```bash
python generate_poster.py --output my_poster.png --dpi 300
```

| Flag | Default | Description |
| --- | --- | --- |
| `--output`, `-o` | `MysteryState2050_Poster.png` | Output filename |
| `--dpi`, `-d` | `216` | Export DPI (216 = 2x retina quality) |

### Web Preview

```bash
python -m flask --app web.app run
# Open http://localhost:5000
```

---

## Project Progress

### Completed

| Phase | Status | What Was Done |
| --- | --- | --- |
| **Phase 1: Data & Research** | ✅ Done | Compiled 2050 projections (GDP, population, energy, literacy), demographics pyramid, infrastructure GeoJSON, and source attribution table |
| **Phase 2: Environment Setup** | ✅ Done | Project structure, `requirements.txt`, color palette system (`palette.py`), data loaders, export pipeline |
| **Phase 3: Poster Engine** | ✅ Done | All 6 poster components built — hero section, skyline, data pulse, infrastructure map, cultural layer, demographic pyramid |
| **Phase 4: Bug Squashing** | ✅ Done | Fixed transparency artifacts, enforced compliance (zero state name leaks), upgraded skyline with Rumi Darwaza + ghats, fixed mirrored pyramid bars, squared output |
| **Phase 5: Web Wrapper & Deploy** | ✅ Done | Flask web app (`web/app.py`), Jinja2 template with poster preview + download button, `render.yaml`, deployed to Render free tier |

### Remaining

| Phase | Status | What's Left |
| --- | --- | --- |
| **Phase 6: Social & Submission** | ⏳ Pending | Draft compliant LinkedIn/Instagram caption (no state name!), add required tags (`@Hack2skill`, `@Google for Developers`, `#WhichStateAmI`), post publicly, submit link on Hack2Skill portal |

---

## Project Structure

```text
project_root/
├── data/                          # Static data files (no API calls)
│   ├── projections.json           #   GDP, urbanization, renewable, literacy
│   ├── demographics.json          #   Population pyramid (17 age groups x 2 years)
│   ├── infrastructure.json        #   GeoJSON: 4 expressways, 5 airports, 6 cities
│   └── source_attribution.csv     #   Every number mapped to credible source
│
├── poster/                        # Matplotlib render modules
│   ├── __init__.py
│   ├── canvas.py                  #   Root compositor (6-zone GridSpec)
│   ├── hero_section.py            #   "2050" headline + glow + gradient
│   ├── skyline.py                 #   3-city skyline (Varanasi | Lucknow | Noida)
│   ├── data_pulse.py              #   4 metric cards with glass effect
│   ├── infra_map.py               #   Expressway lines + airport/city dots
│   ├── cultural_layer.py          #   Taj, Kashi spire, Ganga curve, Banarasi border
│   └── demographic_pyramid.py     #   Mirrored horizontal bar chart (male/female)
│
├── utils/                         # Shared utilities
│   ├── __init__.py
│   ├── palette.py                 #   Color tokens, font sizes, canvas constants
│   ├── data_transform.py          #   JSON/CSV data loaders
│   └── export.py                  #   PNG save + Pillow verification
│
├── web/                           #  Flask web app
│   ├── app.py                     #   Routes: / (preview) + /download + /generate
│   ├── templates/
│   │   └── index.html             #   Jinja2 poster preview page
│   └── static/
│       └── style.css              #   Dark theme CSS (matches poster palette)
│
├── generate_poster.py             # CLI entry point
├── requirements.txt               # Python dependencies
├── render.yaml                    # Render deployment config
├── .gitignore
└── README.md                      # You are here
```

---

## Poster Architecture

The poster is a **1080x1080pt Matplotlib Figure** exported at 2x DPI (216) for retina quality.

```text
┌─────────────────────────────────────┐
│          HERO SECTION               │  "2050" headline + glow + tagline
│          (16.0%)                    │
├─────────────────────────────────────┤
│          SKYLINE STRIP              │  Varanasi → Lucknow → Noida
│          (14.0%)                    │
├─────────────────────────────────────┤
│  $1.2T │ 298M │  72%  │  96%       │  4 metric cards with deltas
│          (16.0%)                    │
├─────────────────────────────────────┤
│      INFRASTRUCTURE MAP             │  Expressway lines + airport dots
│          (20.0%)                    │
├─────────────────────────────────────┤
│       CULTURAL FOOTER               │  Taj + Kashi + Ganga + Banarasi
│          (14.0%)                    │
├─────────────────────────────────────┤
│     DEMOGRAPHIC PYRAMID             │  Male ◄──── ────► Female
│          (20.0%)                    │
└─────────────────────────────────────┘
```

### Color Palette

| Token | Hex | Usage |
| --- | --- | --- |
| Ganga Blue | `#1A6B8A` | Headlines, map paths, male bars |
| Deep Saffron | `#FF6B00` | Highlights, airports, female bars |
| Gold | `#FFD700` | Metric values, cultural accents |
| Charcoal Night | `#1A1A2E` | Background |
| Varanasi Maroon | `#8B1A1A` | Banarasi border |
| Mint Green | `#00C853` | Growth arrows |

---

## Deployment

Deployed on Render free tier. Auto-deploys on every push to `main`.

```yaml
# render.yaml (root)
buildCommand: pip install -r requirements.txt && python generate_poster.py
startCommand: gunicorn web.app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
```

---

## Compliance Rules

> **CRITICAL:** The state name must NEVER appear anywhere in the poster, caption, alt text, or social media post.

- Zero mentions of the state name, abbreviation, or any district name in rendered text
- Verified via automated `findstr` / `grep` audit on all source files
- Identity communicated purely through visual clues: Taj silhouette, Ganga curve, Kashi spire, Banarasi border, expressway network

---

## Data Sources

| Metric | Source |
| --- | --- |
| GDP Projections | NITI Aayog State Vision Document, World Bank |
| Population 2050 | UN World Population Prospects 2024 |
| Renewable Energy | UPNEDA, Ministry of New & Renewable Energy |
| Literacy Rate | ASER Reports, NFHS-5 |
| Infrastructure | UPEIDA, UDAN Scheme, AAI Master Plan |
| Demographics | Census 2011 + UN Projections |

Full attribution in [`data/source_attribution.csv`](data/source_attribution.csv).

---

## Tech Stack

| Tool | Version | Purpose |
| --- | --- | --- |
| Python | 3.11+ | Core runtime |
| Matplotlib | >= 3.9 | Poster layout, all visualizations |
| Pillow | >= 10.0 | Image export, dimension verification |
| NumPy | >= 1.26 | Numeric operations |
| Pandas | >= 2.2 | Data loading |
| Flask | >= 3.0 | Web preview server |
| Gunicorn | >= 21.0 | Production WSGI server |

---

## License

See [LICENSE](LICENSE) for details.

---

*Built for Hack2Skill x Google for Developers — Mini Challenge 2: Which State Am I?*
