# Which State Am I? — 2050 Edition

> A data-driven visual poster that encodes India's most populous state's identity through the lens of its 2050 future — **without naming the state once.**

**Hackathon:** Hack2Skill x Google for Developers — Mini Challenge 2  
**Theme:** Fast Forward to 2050  
**Stack:** Python (Matplotlib + Pillow + Flask)  
**Live:** https://which-state-am-i.onrender.com

---
## Vision

What if a state's identity could be communicated without ever naming it?

This project transforms demographic, economic, cultural, and infrastructure data into an immersive visual narrative that challenges viewers to infer a region's identity through data-driven storytelling. By imagining the state in 2050, the poster demonstrates how complex information can be made engaging, memorable, and accessible through design, encouraging people to explore the connection between heritage, growth, and future potential.


<img width="2332" height="2332" alt="MysteryState2050_Poster (1)" src="https://github.com/user-attachments/assets/5178fde9-4c2d-4219-9d9f-f87f02d230fd" />


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
├── web/                           # Flask web app
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
# System Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                     DATA SOURCES LAYER                      │
├─────────────────────────────────────────────────────────────┤
│ projections.json                                            │
│ demographics.json                                           │
│ infrastructure.json                                         │
│ source_attribution.csv                                      │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    DATA PROCESSING LAYER                    │
├─────────────────────────────────────────────────────────────┤
│ utils/data_transform.py                                     │
│                                                             │
│ • Load JSON / CSV datasets                                  │
│ • Validate schema                                           │
│ • Normalize values                                          │
│ • Prepare visualization-ready structures                    │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                 VISUALIZATION COMPONENT LAYER               │
├─────────────────────────────────────────────────────────────┤
│ poster/hero_section.py                                      │
│ poster/skyline.py                                           │
│ poster/data_pulse.py                                        │
│ poster/infra_map.py                                         │
│ poster/cultural_layer.py                                    │
│ poster/demographic_pyramid.py                               │
│                                                             │
│ Independent reusable rendering modules                      │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                  COMPOSITION ENGINE LAYER                   │
├─────────────────────────────────────────────────────────────┤
│ poster/canvas.py                                            │
│                                                             │
│ • GridSpec Layout Manager                                   │
│ • Zone Allocation                                           │
│ • Component Assembly                                        │
│ • Visual Consistency Enforcement                            │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                     EXPORT PIPELINE LAYER                   │
├─────────────────────────────────────────────────────────────┤
│ utils/export.py                                             │
│                                                             │
│ • High-DPI Rendering                                        │
│ • Pillow Validation                                         │
│ • Dimension Verification                                    │
│ • PNG Export                                                │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                     GENERATED ARTIFACT                      │
├─────────────────────────────────────────────────────────────┤
│ MysteryState2050_Poster.png                                 │
│ 2332 × 2332 px                                              │
│ Retina Quality Output                                       │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                FUTURE DEPLOYMENT LAYER (Phase 5)            │
├─────────────────────────────────────────────────────────────┤
│ Flask Application                                           │
│ Render Deployment                                           │
│ Poster Preview Interface                                    │
│ Download Endpoint                                           │
└─────────────────────────────────────────────────────────────┘
```


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
## Impact

In an age of information overload, communicating the identity and future potential of a region through raw statistics alone is often ineffective. This project explores a more engaging approach: transforming complex demographic, economic, cultural, and infrastructure data into a single visual narrative that can be understood at a glance.

By presenting a state's projected 2050 future without explicitly naming it, the poster encourages observation, curiosity, and data-driven discovery. Viewers are challenged to connect cultural landmarks, infrastructure networks, population trends, and economic indicators to infer the region's identity for themselves.

### Real-World Applications

* **Education & Learning** – Make geography, demographics, and economic development more engaging for students through visual storytelling.
* **Data Journalism** – Transform complex datasets into accessible narratives that improve public understanding.
* **Tourism & Cultural Promotion** – Showcase regional identity and heritage through modern visual communication.
* **Policy Communication** – Help governments and organizations communicate long-term development goals in a clear and compelling format.
* **Future-State Visualization** – Enable comparative visualizations of states, cities, or regions to support strategic planning and public awareness.

### Long-Term Vision

The architecture is designed to be scalable and data-driven. By replacing the underlying datasets, the same framework can automatically generate future-state posters for any region, creating an extensible platform for visual storytelling, civic education, and data communication at scale.

Rather than simply displaying numbers, this project demonstrates how data can be transformed into a memorable experience—turning statistics into stories and projections into possibilities.

---

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
