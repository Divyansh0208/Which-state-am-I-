# UP 2050 — Feature Ticket List & Sprint Board (Python Stack)
## Hack2Skill × Google for Developers · 20 Tickets · 5 Epics · June 2026

---

## Sprint Overview

All work executes in a **single 5-day sprint (03–07 June 2026)**. Tickets organized into 5 epics.

- **P0** tickets are blockers — nothing ships without them
- **P1** tickets improve quality
- **P2** are bonus enhancements

| Epic | Tickets | Points | Priority | Status |
|------|---------|--------|----------|--------|
| EPIC-1: Data & Research | 4 tickets | 13 pts | P0 | In Progress |
| EPIC-2: Design System | 4 tickets | 16 pts | P0 | To Do |
| EPIC-3: Components | 6 tickets | 24 pts | P0/P1 | To Do |
| EPIC-4: Export & Deploy | 3 tickets | 10 pts | P0 | To Do |
| EPIC-5: Social & Submit | 3 tickets | 8 pts | P0 | To Do |
| **Total** | **20 tickets** | **71 pts** | | |

---

## EPIC-1: Data & Research

> Compile all data for poster visualizations. All sources must be credible (government / UN / World Bank). No made-up numbers.

---

### `UP-001` · Compile UP 2050 GDP & Economic Projections

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 3 |
| **Due** | 03 Jun |
| **Epic** | EPIC-1: Data |
| **Dependencies** | — |

**Description**
Research NITI Aayog state vision docs, World Bank South Asia projections, UP government budget documents. Extract GDP trajectory 2024–2050. Store as `data/projections.json`. Load via `pandas.read_json()` in `data_transform.py`.

**Acceptance Criteria**
`data/projections.json` exists with GDP, urbanization, renewable energy, literacy fields. All values sourced. `data_transform.py` loads file without errors.

---

### `UP-002` · Compile Demographic Data (Population Pyramid 2050)

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 3 |
| **Due** | 03 Jun |
| **Epic** | EPIC-1: Data |
| **Dependencies** | UP-001 |

**Description**
Collect UN World Population Prospects data for UP (India national split). Build male/female age-group breakdown for 2024 and 2050. Store as `data/demographics.json`. Load via `pandas` in `data_transform.py`.

**Acceptance Criteria**
`data/demographics.json` contains `ageGroups` array with male/female counts for 2024 and 2050. Data verified against 2+ sources. Pandas loads cleanly.

---

### `UP-003` · Map Infrastructure Data (Expressways + Airports)

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 4 |
| **Due** | 03 Jun |
| **Epic** | EPIC-1: Data |
| **Dependencies** | — |

**Description**
Collect coordinates for: Ganga Expressway, Purvanchal Expressway, Bundelkhand Expressway, Agra-Lucknow Expressway, Jewar Airport, Kushinagar Airport, Varanasi Airport. Store as `data/infrastructure.json` (valid GeoJSON FeatureCollection). Verify renders via `geopandas.read_file()`.

**Acceptance Criteria**
`data/infrastructure.json` is valid GeoJSON. `geopandas.read_file()` loads without errors. All expressway paths render on Mercator projection centered on UP (lat 27.5, lon 80.9).

---

### `UP-004` · Fact-Check & Source Attribution Table

| | |
|---|---|
| **Priority** | 🟡 P1 |
| **Points** | 3 |
| **Due** | 04 Jun |
| **Epic** | EPIC-1: Data |
| **Dependencies** | UP-001, UP-002, UP-003 |

**Description**
Create `data/source_attribution.csv` mapping every displayed number to source URL, publication year, notes. Load with `pandas.read_csv()` for reference.

**Acceptance Criteria**
CSV exists with columns: `metric, value, source_name, source_url, year, notes`. Minimum 10 rows. Loads cleanly via pandas.

---

## EPIC-2: Design System Setup

> Establish visual foundation before component work. All modules import from `utils/palette.py` — no hardcoded colors or font sizes anywhere else.

---

### `UP-005` · Set Up Python Project + Virtual Environment

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 2 |
| **Due** | 03 Jun |
| **Epic** | EPIC-2: Design |
| **Dependencies** | — |

**Description**
Initialize Python 3.11 project. Create `venv`. Install all packages from `requirements.txt`. Verify `python generate_poster.py` runs (even with placeholder output). Set up `web/app.py` Flask stub. Confirm Flask runs at `localhost:5000`.

**Acceptance Criteria**
`pip install -r requirements.txt` succeeds. `python generate_poster.py` runs without import errors. `flask run` starts dev server. Folder structure matches TechArch doc section 3.1.

---

### `UP-006` · Implement Color Token System (`palette.py`)

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 2 |
| **Due** | 04 Jun |
| **Epic** | EPIC-2: Design |
| **Dependencies** | UP-005 |

**Description**
Create `utils/palette.py` with all color constants as Python hex strings. Define: `GANGA_BLUE`, `DEEP_SAFFRON`, `GOLD`, `CHARCOAL_NIGHT`, `VARANASI_MAROON`, `MINT_GREEN`, `PALE_MIST`, `WHITE`. Also define font-size constants and register custom fonts via `matplotlib.font_manager`.

**Acceptance Criteria**
All 8 color constants defined. Importing `from utils.palette import GANGA_BLUE` works in any module. Matplotlib renders correct colors in test figure.

---

### `UP-007` · Register Custom Fonts in Matplotlib

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 3 |
| **Due** | 04 Jun |
| **Epic** | EPIC-2: Design |
| **Dependencies** | UP-005, UP-006 |

**Description**
Download Space Grotesk, Inter, and Tiro Devanagari Hindi TTF files into `web/static/fonts/`. Register via `matplotlib.font_manager.fontManager.addfont()` in `palette.py`. Verify each font renders in a test `matplotlib.text` call. Document font registration order in comments.

**Acceptance Criteria**
All 3 fonts render in Matplotlib without fallback to DejaVu. Devanagari text renders Hindi numerals/script correctly. No font warnings in console.

---

### `UP-008` · Build PosterCanvas Skeleton (1080×1080 Matplotlib Figure)

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 5 |
| **Due** | 04 Jun |
| **Epic** | EPIC-2: Design |
| **Dependencies** | UP-005, UP-006, UP-007 |

**Description**
Create `poster/canvas.py`. Use `matplotlib.figure.Figure(figsize=(10.8, 10.8), dpi=100)` for 1080×1080pt canvas. Use `GridSpec` to define 6 zones per Frontend Spec section 4.2. Each zone renders a placeholder `Axes` with correct height ratio and label. Call `export.py` to save PNG.

**Acceptance Criteria**
`python generate_poster.py` outputs `UP2050_Poster.png` at 1080×1080px. All 6 zones visible with correct proportions. File saves without errors.

---

## EPIC-3: Poster Components

> Build each poster section as an isolated Python module. Modules receive data as arguments — no direct file reads inside render modules.

---

### `UP-009` · Build `hero_section.py`

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 3 |
| **Due** | 04 Jun |
| **Epic** | EPIC-3: Components |
| **Dependencies** | UP-008 |

**Description**
Create `poster/hero_section.py`. Render '2050' headline in Space Grotesk 96pt Bold, tagline, subtext. Background: dark gradient via `ax.set_facecolor()` + custom gradient patch. In `export_mode=True`, skip any animation code paths.

**Acceptance Criteria**
Hero section renders in PosterCanvas zone 1. '2050' text at correct size and color. Dark gradient background visible. Module accepts `ax` (Matplotlib Axes) as first argument.

---

### `UP-010` · Build `data_pulse.py` (4 Metric Cards)

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 5 |
| **Due** | 05 Jun |
| **Epic** | EPIC-3: Components |
| **Dependencies** | UP-008, UP-001 |

**Description**
Create `poster/data_pulse.py`. Render 4 metric cards in 4-column `GridSpec` subgrid. Each card: semi-transparent background patch, large value text, label, delta arrow (▲/▼) with color. Data loaded from `projections.json` via `data_transform.py`.

**Acceptance Criteria**
All 4 cards render with correct values. Delta arrows show correct direction/color. Glass-effect background via `Rectangle` patch with alpha. No animation in export mode.

---

### `UP-011` · Build `infra_map.py` (GeoPandas Map)

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 5 |
| **Due** | 05 Jun |
| **Epic** | EPIC-3: Components |
| **Dependencies** | UP-008, UP-003 |

**Description**
Create `poster/infra_map.py`. Load GeoJSON via `geopandas.read_file()`. Plot expressways via `gdf.plot(ax=ax)` with Mercator projection. Add airport dots via `ax.scatter()`. Add city dots. **No text labels on map.**

**Acceptance Criteria**
All 4 expressway routes render as lines. Airport/city dots at correct coordinates. Map fits 1080×240px zone. Transparent background. Zero text labels in output.

---

### `UP-012` · Build `skyline.py` (Matplotlib Path Skyline)

| | |
|---|---|
| **Priority** | 🟡 P1 |
| **Points** | 5 |
| **Due** | 05 Jun |
| **Epic** | EPIC-3: Components |
| **Dependencies** | UP-008 |

**Description**
Create `poster/skyline.py` using `matplotlib.patches.PathPatch` and `matplotlib.path.Path`. Design three-city merged skyline: Varanasi ghats (left), Lucknow dome (center), Noida towers (right). Add `Rectangle` window lights. Sky gradient via `LinearSegmentedColormap`.

**Acceptance Criteria**
SVG-equivalent skyline clearly shows three distinct architectural identities. Crisp at 1080px. No raster images — pure Matplotlib vector paths only.

---

### `UP-013` · Build `cultural_layer.py` (Silhouette Overlays)

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 3 |
| **Due** | 05 Jun |
| **Epic** | EPIC-3: Components |
| **Dependencies** | UP-008 |

**Description**
Create `poster/cultural_layer.py` with 4 semi-transparent silhouette patches: Taj Mahal outline, Kashi Vishwanath spire, Ganga curve, Banarasi border pattern. Render using `PathPatch` with `alpha` values per Frontend Spec. Position as absolute overlays via `ax.set_zorder()`.

**Acceptance Criteria**
All 4 silhouettes render at correct positions and opacities. State identity decodable without text. No text in module output.

---

### `UP-014` · Build `demographic_pyramid.py`

| | |
|---|---|
| **Priority** | 🟡 P1 |
| **Points** | 3 |
| **Due** | 05 Jun |
| **Epic** | EPIC-3: Components |
| **Dependencies** | UP-008, UP-002 |

**Description**
Create `poster/demographic_pyramid.py` using `ax.barh()`. Classic mirrored horizontal bar chart for male/female 2050 data. Age groups on center Y axis. Color: male = `GANGA_BLUE`, female = `DEEP_SAFFRON`. Load data from `demographics.json`.

**Acceptance Criteria**
Pyramid renders correct male/female bars for all age groups. No state-name labels. Fits assigned poster zone. Bars align correctly at center axis.

---

## EPIC-4: Export & Deployment

> Critical path — without working export, no submission. P0 regardless of component polish.

---

### `UP-015` · Implement Poster Export (`export.py` + CLI)

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 4 |
| **Due** | 06 Jun |
| **Epic** | EPIC-4: Export |
| **Dependencies** | UP-009 through UP-014 |

**Description**
Create `utils/export.py`. Implement:
1. Set `export_mode=True` in canvas call
2. Call `fig.savefig('UP2050_Poster.png', dpi=216, bbox_inches='tight', facecolor=CHARCOAL_NIGHT)`
3. Use Pillow to verify output dimensions (2160×2160 at 2× DPI)
4. Optionally upscale via `Image.resize()` if needed

`generate_poster.py` CLI: `python generate_poster.py [--output path] [--dpi 216]`

**Acceptance Criteria**
Running CLI downloads valid PNG. File is ~2160×2160px. All components visible. Fonts render correctly. No blank zones or missing elements.

---

### `UP-016` · Deploy to Render

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 2 |
| **Due** | 06 Jun |
| **Epic** | EPIC-4: Export |
| **Dependencies** | UP-015 |

**Description**
Push codebase to GitHub. Connect Render to repo. Configure: `buildCommand = pip install -r requirements.txt`, `startCommand = gunicorn web.app:app`. Add `render.yaml`. Trigger deploy. Verify live URL. Flask app serves pre-generated PNG via `/` route and `/download` route.

**Acceptance Criteria**
Live URL accessible at `https://[project].onrender.com`. Poster image renders on desktop + mobile. Download button serves PNG file.

---

### `UP-017` · Pre-Export Compliance Audit

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 2 |
| **Due** | 06 Jun |
| **Epic** | EPIC-4: Export |
| **Dependencies** | UP-015 |

**Description**
Run `grep -r "Uttar Pradesh\|U\.P\.\| UP " poster/ web/ data/` to catch any state name leaks in code strings. Manual visual audit of exported PNG. Verify all data values match `source_attribution.csv`.

**Acceptance Criteria**
`grep` returns zero matches. Visual audit signed off. Data values verified. Image approved for upload.

---

## EPIC-5: Social Media & Submission

> Final mile. All technical work means nothing if submission is rejected. Execute with precision.

---

### `UP-018` · Write & Finalize LinkedIn/Instagram Caption

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 3 |
| **Due** | 06 Jun |
| **Epic** | EPIC-5: Social |
| **Dependencies** | UP-017 |

**Description**
Write final caption using template from Frontend Spec section 9. Must include riddle framing, clues (no state name), `#WhichStateAmI`, `@Hack2skill`, `@Google for Developers`. Second-pair review to confirm no state name slipped in.

**Acceptance Criteria**
Caption reviewed and approved. Hashtag present. Both tags present. No state name. Engaging question format encourages comments.

---

### `UP-019` · Post on LinkedIn + Instagram

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 2 |
| **Due** | 07 Jun |
| **Epic** | EPIC-5: Social |
| **Dependencies** | UP-018 |

**Description**
Upload exported PNG to LinkedIn (Photo post, not article). Add caption. Set to **Public**. Post. Repeat on Instagram. Capture post URLs from both platforms.

**Acceptance Criteria**
Both posts live and publicly accessible. LinkedIn post URL copied. Instagram post URL copied. Both set to Public visibility.

---

### `UP-020` · Submit Link on Hack2Skill Portal

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 2 |
| **Due** | 07 Jun |
| **Epic** | EPIC-5: Social |
| **Dependencies** | UP-019 |

**Description**
Log in to Hack2Skill portal. Navigate to [Mini Challenge 2] Which State Am I? Select theme 'Fast forward to 2050'. Paste LinkedIn post URL. Submit before **07/06/2026 11:59 PM IST**. Screenshot confirmation page.

**Acceptance Criteria**
Portal shows submission confirmed. Attempts counter updates to 1/1. Screenshot saved. Submitted before deadline.

---

## Ticket Summary

| # | Ticket | Epic | Pri | Pts | Due | Status |
|---|--------|------|-----|-----|-----|--------|
| UP-001 | Compile GDP & Economic Projections | E1 | 🔴 P0 | 3 | 03 Jun | To Do |
| UP-002 | Compile Demographic Data | E1 | 🔴 P0 | 3 | 03 Jun | To Do |
| UP-003 | Map Infrastructure Data | E1 | 🔴 P0 | 4 | 03 Jun | To Do |
| UP-004 | Source Attribution Table | E1 | 🟡 P1 | 3 | 04 Jun | To Do |
| UP-005 | Python Project + Venv Setup | E2 | 🔴 P0 | 2 | 03 Jun | To Do |
| UP-006 | Color Token System (`palette.py`) | E2 | 🔴 P0 | 2 | 04 Jun | To Do |
| UP-007 | Font Registration in Matplotlib | E2 | 🔴 P0 | 3 | 04 Jun | To Do |
| UP-008 | PosterCanvas Skeleton (Matplotlib GridSpec) | E2 | 🔴 P0 | 5 | 04 Jun | To Do |
| UP-009 | `hero_section.py` | E3 | 🔴 P0 | 3 | 04 Jun | To Do |
| UP-010 | `data_pulse.py` | E3 | 🔴 P0 | 5 | 05 Jun | To Do |
| UP-011 | `infra_map.py` (GeoPandas) | E3 | 🔴 P0 | 5 | 05 Jun | To Do |
| UP-012 | `skyline.py` (Path patches) | E3 | 🟡 P1 | 5 | 05 Jun | To Do |
| UP-013 | `cultural_layer.py` | E3 | 🔴 P0 | 3 | 05 Jun | To Do |
| UP-014 | `demographic_pyramid.py` | E3 | 🟡 P1 | 3 | 05 Jun | To Do |
| UP-015 | Poster Export (`export.py` + CLI) | E4 | 🔴 P0 | 4 | 06 Jun | To Do |
| UP-016 | Render Deployment | E4 | 🔴 P0 | 2 | 06 Jun | To Do |
| UP-017 | Pre-Export Compliance Audit | E4 | 🔴 P0 | 2 | 06 Jun | To Do |
| UP-018 | Write Post Caption | E5 | 🔴 P0 | 3 | 06 Jun | To Do |
| UP-019 | Post on LinkedIn + Instagram | E5 | 🔴 P0 | 2 | 07 Jun | To Do |
| UP-020 | Submit on Hack2Skill Portal | E5 | 🔴 P0 | 2 | 07 Jun | To Do |

**Total: 71 story points · 20 tickets · 5 epics · 5 days**

---

*— End of Feature Ticket List — · UP 2050 · Hack2Skill × Google for Developers*