# UP 2050 — Technical Architecture Document (Python Stack)
## Hack2Skill × Google for Developers · v2.0 · June 2026

---

## 1. Architecture Overview

UP 2050 has two layers: a **static image layer** (primary deliverable) and an **optional interactive web layer** (bonus). Python stack generates the poster via Matplotlib/Pillow, serves the web version via Flask, and exports PNG for social upload.

### 1.1 System Diagram — Component Layers

| Layer | Technology | Purpose | Output |
|-------|------------|---------|--------|
| Data Layer | JSON / CSV static files | Holds all UP 2050 projections, metrics | Consumed by viz modules |
| Design System | Python constants (`palette.py`) | Color tokens, font sizes, spacing | Imported by all render modules |
| Visualization Engine | Matplotlib + GeoPandas + Shapely | Data charts, maps, SVG overlays | PNG/SVG renders inside poster |
| Poster Canvas | Pillow (PIL) + Matplotlib Figure | Composes all elements into poster | 1080×1080 PNG export |
| Web App Shell | Flask + Jinja2 | Dev server, routing, HTML preview | localhost:5000 + Render deploy |
| Export Pipeline | Pillow `Image.save()` | High-res image export | PNG file for social upload |
| Deployment | Render (free tier) | Hosts interactive version | Live URL for hackathon link |

---

## 2. Tech Stack Decision Log

### 2.1 Core Stack

| Tool | Version | Why Chosen | Alternatives Rejected |
|------|---------|------------|----------------------|
| Python | 3.11+ | Ecosystem for data viz + image gen | — |
| Matplotlib | 3.9.x | Full poster layout, subplots, custom artists | Plotly (browser-first, harder PNG export) |
| GeoPandas | 0.14.x | GeoJSON map rendering with Mercator projection | D3 (JS only) |
| Pillow (PIL) | 10.x | Compositing layers, final PNG export, 2× scale | OpenCV (heavy) |
| Flask | 3.x | Lightweight web preview server | Django (overkill), FastAPI (no Jinja2 SSR) |
| Jinja2 | 3.x | HTML template for web version | React (JS, off-stack) |
| Render | — | Free Python web service deploy from GitHub | Vercel (Node-optimized), Railway (comparable) |

### 2.2 Data Sources

| Data Point | Source | Format |
|------------|--------|--------|
| UP 2050 GDP Projection | NITI Aayog State Vision Documents | JSON (manual entry) |
| Population Pyramid 2050 | Census 2011 + UN World Population Prospects | CSV |
| Expressway Network Coordinates | UPEIDA official data | GeoJSON |
| Renewable Energy Targets | UPNEDA | JSON |
| Literacy Rate Trend | ASER / NFHS data + extrapolation | JSON |
| Urbanization Rate | World Bank India + UP state share | JSON |

---

## 3. Application Architecture

### 3.1 Folder Structure

```
up2050/
├── data/
│   ├── projections.json
│   ├── demographics.json
│   ├── infrastructure.json
│   └── source_attribution.csv
├── poster/
│   ├── canvas.py            # Root poster compositor (Matplotlib Figure)
│   ├── hero_section.py      # 2050 headline + tagline axes
│   ├── data_pulse.py        # 4 metric cards (Matplotlib subplots)
│   ├── infra_map.py         # GeoPandas expressway + airport map
│   ├── cultural_layer.py    # SVG silhouette overlays via Matplotlib patches
│   ├── skyline.py           # SVG skyline via Matplotlib path patches
│   └── demographic_pyramid.py  # Population pyramid (Matplotlib barh)
├── utils/
│   ├── palette.py           # Color tokens + font sizes as Python constants
│   ├── data_transform.py    # JSON/CSV loaders + transform helpers
│   └── export.py            # Pillow save + 2× upscale logic
├── web/
│   ├── app.py               # Flask app
│   ├── templates/
│   │   └── index.html       # Jinja2 HTML poster preview + download button
│   └── static/
│       └── style.css        # Minimal CSS for web shell
├── generate_poster.py       # CLI entry point: python generate_poster.py
├── requirements.txt
└── render.yaml              # Render deployment config
```

### 3.2 Module Architecture

| Module | Responsibility | Key Inputs / Outputs |
|--------|---------------|----------------------|
| `canvas.py` | Root compositor — creates 1080×1080 Matplotlib figure, calls all section renderers | `export_mode: bool` → PNG |
| `hero_section.py` | Renders 2050 headline, tagline, dark gradient background via Matplotlib axes | `year`, `tagline` → Axes |
| `data_pulse.py` | 4 metric cards as subplot panels — value, label, delta arrow | `metrics: list[dict]` → Axes |
| `infra_map.py` | GeoPandas Mercator map, expressway paths, airport/city dots | `infrastructure.json` → Axes |
| `cultural_layer.py` | Semi-transparent SVG silhouettes (Taj, Ganga, Kashi) as Matplotlib patches | `opacity` settings → Axes |
| `skyline.py` | Three-city SVG skyline via Matplotlib path patches | `animated: bool` → Axes |
| `demographic_pyramid.py` | Horizontal mirrored bar chart for 2050 population | `demographics.json` → Axes |
| `export.py` | Saves figure at 2× DPI (216 dpi → 2160×2160 effective), writes PNG | `fig`, `filename` → .png |

---

## 4. Data Flow

### 4.1 Data Pipeline

All data is static — no runtime API calls. JSON/CSV files are loaded by `data_transform.py` and passed into each render module.

```
projections.json    → data_transform.py → data_pulse.py          → Matplotlib subplot
demographics.json   → data_transform.py → demographic_pyramid.py → Matplotlib barh
infrastructure.json →                   → infra_map.py           → GeoPandas plot → Axes
```

### 4.2 Export Flow

1. Run `python generate_poster.py`
2. `canvas.py` creates a 1080×1080pt Matplotlib `Figure`
3. All section modules render into their assigned `Axes` regions
4. `export.py` calls `fig.savefig('UP2050_Poster.png', dpi=216, bbox_inches='tight')`
5. Pillow optionally upscales to 2160×2160 for retina quality
6. File saved as `UP2050_Poster.png` in project root
7. User uploads PNG to LinkedIn/Instagram manually

> ⚠️ **Known Issue:** Matplotlib custom fonts require `matplotlib.font_manager` registration. Register Space Grotesk and Tiro Devanagari Hindi TTF files before figure creation. Use `fm.fontManager.addfont()` in `palette.py`.

---

## 5. Deployment Architecture

### 5.1 Render Deployment

| Step | Action | Command / Config |
|------|--------|-----------------|
| 1 | Push to GitHub repo | `git push origin main` |
| 2 | Connect Render to GitHub repo | Render dashboard → New Web Service |
| 3 | Set runtime | Python 3.11 |
| 4 | Set build command | `pip install -r requirements.txt` |
| 5 | Set start command | `gunicorn web.app:app` |
| 6 | Auto-deploy on push | Render webhook (automatic) |
| 7 | Custom URL | `onrender.com` subdomain (free) |

### 5.2 `render.yaml`

```yaml
services:
  - type: web
    name: up2050
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn web.app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

### 5.3 Performance Targets

| Metric | Target | Strategy |
|--------|--------|----------|
| Poster generation time (CLI) | < 10s | Pre-load fonts + static data |
| Web page load | < 2s | Serve pre-generated PNG; no runtime render |
| PNG file size | < 3MB | Matplotlib PNG compression |
| Mobile compatibility | 375px+ viewport | CSS max-width + responsive img tag |

---

## 6. Security & Compliance

- No user data collected — fully static, no database
- No API keys in code — all data is static JSON/CSV
- GDPR not applicable — no PII collected
- Content compliance: zero state name in any rendered text (enforced via `grep` checklist on all `.py` string literals)
- PNG export: no metadata or tracking in output file

---

## 7. Development Environment Setup

```bash
# Prerequisites: Python 3.11+, pip
git clone https://github.com/[your-username]/up2050
cd up2050
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python generate_poster.py       # Generate poster PNG
python web/app.py               # Start Flask dev server at localhost:5000
```

### Dependencies (`requirements.txt`)

| Package | Version | Purpose |
|---------|---------|---------|
| `matplotlib` | >=3.9.0 | Core poster layout + all visualizations |
| `geopandas` | >=0.14.0 | GeoJSON map rendering |
| `shapely` | >=2.0.0 | Geometry for map paths |
| `Pillow` | >=10.0.0 | Image compositing + PNG export |
| `numpy` | >=1.26.0 | Numeric operations for viz |
| `pandas` | >=2.2.0 | CSV/JSON data loading |
| `flask` | >=3.0.0 | Web preview server |
| `gunicorn` | >=21.0.0 | Production WSGI server for Render |
| `Jinja2` | >=3.1.0 | HTML templating (Flask dep, explicit) |
| `pyproj` | >=3.6.0 | Coordinate projection for GeoPandas |

---

*— End of Technical Architecture Document — · UP 2050 · Hack2Skill × Google for Developers*
