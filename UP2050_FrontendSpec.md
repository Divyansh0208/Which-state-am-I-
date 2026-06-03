# UP 2050 — Frontend Design & Component Specification (Python Stack)
## Hack2Skill × Google for Developers · v2.0 · June 2026

---

## 1. Design Philosophy

Same three principles — unchanged by stack migration:

- **Data Honesty** — every number has a source
- **Visual Restraint** — no clutter; state identity from negative space + detail
- **Cultural Authenticity** — North Indian visual language, not generic futurism

Aesthetic: ISRO mission posters × NYT data journalism × Indian modernist print. Bold, structured, deeply informative — beautiful. Rendered entirely via Python (Matplotlib + Pillow).

---

## 2. Color System

### 2.1 Primary Palette

Derived from UP's natural and cultural identity — Ganga blue, saffron, gold, Varanasi maroon — reinterpreted for 2050.

| Token Name | Hex | Python Constant | Usage |
|------------|-----|-----------------|-------|
| `GANGA_BLUE` | `#1A6B8A` | `palette.GANGA_BLUE` | Headlines, data accents, map paths |
| `DEEP_SAFFRON` | `#FF6B00` | `palette.DEEP_SAFFRON` | CTAs, highlighted metrics, hero glow |
| `GOLD` | `#FFD700` | `palette.GOLD` | Cultural highlights, border accents |
| `CHARCOAL_NIGHT` | `#1A1A2E` | `palette.CHARCOAL_NIGHT` | Poster background |
| `VARANASI_MAROON` | `#8B1A1A` | `palette.VARANASI_MAROON` | Cultural iconography, silk border |
| `MINT_GREEN` | `#00C853` | `palette.MINT_GREEN` | Growth arrows, positive delta indicators |
| `PALE_MIST` | `#E8EAF6` | `palette.PALE_MIST` | Secondary text, subtitles |
| `WHITE` | `#FFFFFF` | `palette.WHITE` | Primary text on dark background |

All constants defined in `utils/palette.py`. No hardcoded hex strings in any render module.

### 2.2 Dark Background Rationale

Poster uses `CHARCOAL_NIGHT` (`#1A1A2E`) background. Same rationale as v1: colored data viz pops, space-mission aesthetic, photographs well for social screenshots. Set via `fig.patch.set_facecolor(CHARCOAL_NIGHT)` and `ax.set_facecolor(CHARCOAL_NIGHT)` on all axes.

---

## 3. Typography System

| Role | Font | Size (pt) | Weight | Color | Usage |
|------|------|-----------|--------|-------|-------|
| Display Headline | Space Grotesk | 72–96pt | 700 | `WHITE` | 2050 year, main headline |
| Section Title | Space Grotesk | 32–40pt | 600 | `GANGA_BLUE` | Section headers |
| Data Label | Inter | 18–24pt | 500 | `GOLD` | Metric values, percentages |
| Body Copy | Inter | 14–16pt | 400 | `PALE_MIST` | Descriptions, subtitles |
| Accent Script | Tiro Devanagari Hindi | 24–32pt | 400 | `GOLD` | Hindi text overlays |
| Caption | Inter Mono | 12pt | 400 | `#888888` | Data source footnotes |

### 3.1 Font Registration (Python)

```python
# In utils/palette.py — register before any figure creation
import matplotlib.font_manager as fm
import os

FONT_DIR = os.path.join(os.path.dirname(__file__), '..', 'web', 'static', 'fonts')

fm.fontManager.addfont(os.path.join(FONT_DIR, 'SpaceGrotesk-Bold.ttf'))
fm.fontManager.addfont(os.path.join(FONT_DIR, 'Inter-Regular.ttf'))
fm.fontManager.addfont(os.path.join(FONT_DIR, 'TiroDevanagariHindi-Regular.ttf'))
```

> **CRITICAL:** Font registration must happen before `plt.figure()` or `Figure()` is called. Place at module import time in `palette.py`. Download TTF files from Google Fonts and store in `web/static/fonts/`.

---

## 4. Grid & Layout System

### 4.1 Poster Canvas Dimensions

| Format | Dimensions | Aspect Ratio | Matplotlib figsize |
|--------|------------|-------------|-------------------|
| Instagram Square | 1080 × 1080px | 1:1 | `(10.8, 10.8)` @ 100dpi |
| Instagram Portrait | 1080 × 1350px | 4:5 | `(10.8, 13.5)` @ 100dpi |
| LinkedIn Landscape | 1200 × 627px | 1.91:1 | `(12.0, 6.27)` @ 100dpi |
| Story Format | 1080 × 1920px | 9:16 | `(10.8, 19.2)` @ 100dpi |

Primary build target: **1080×1080 square** (`figsize=(10.8, 10.8), dpi=100`). Export at 2× via `dpi=216`.

### 4.2 Poster GridSpec Layout (1080×1080)

| Zone | Height Ratio | Content | Module |
|------|-------------|---------|--------|
| Hero Band | 0.185 | 2050 headline + tagline | `hero_section.py` |
| Skyline Strip | 0.167 | City skyline path illustration | `skyline.py` |
| Data Row | 0.148 | 4 metric cards | `data_pulse.py` |
| Map Zone | 0.222 | Expressway + airport infrastructure map | `infra_map.py` |
| Cultural Footer | 0.148 | Iconic silhouettes + heritage border | `cultural_layer.py` |
| Caption Bar | 0.130 | Riddle caption + clue text | `caption_bar.py` |

```python
# In poster/canvas.py
from matplotlib.gridspec import GridSpec
fig = Figure(figsize=(10.8, 10.8), dpi=100)
gs = GridSpec(6, 1, figure=fig,
              height_ratios=[0.185, 0.167, 0.148, 0.222, 0.148, 0.130],
              hspace=0)
```

---

## 5. Component Specifications

### 5.1 `hero_section.py`

Renders top band. Large '2050' display with glow effect (Matplotlib `shadow=True` + `bbox`), sub-headline tagline.

```python
# Signature
def render(ax, year='2050', tagline='...', subtext='...', export_mode=False):
    ax.set_facecolor(CHARCOAL_NIGHT)
    # Background gradient via imshow or LinearSegmentedColormap
    ax.text(0.5, 0.6, year,
            fontsize=96, fontweight='bold', fontfamily='Space Grotesk',
            color=WHITE, ha='center', va='center', transform=ax.transAxes)
    # Glow: render same text offset with alpha=0.3, GANGA_BLUE
```

---

### 5.2 `data_pulse.py`

Four metric cards. Uses `GridSpecFromSubplotSpec` for 4-column subgrid.

| Metric Card | 2024 Baseline | 2050 Projection | Visual |
|-------------|--------------|-----------------|--------|
| GDP (USD Trillion) | $0.28T | $1.2T | Bar fill + gold number |
| Population (Millions) | 241M | 298M | Pop icon + green delta |
| Renewable Energy % | 18% | 72% | Circular progress ring via `wedge` |
| Literacy Rate % | 73% | 96% | Upward arrow + mint color |

```python
# Signature
def render(ax, metrics: list[dict], export_mode=False):
    # metrics = [{'label': str, 'baseline': num, 'projected': num, 'unit': str}]
    # Card bg: FancyBboxPatch with alpha=0.06
    # Value: ax.text(..., fontsize=36, color=GOLD)
    # Delta: '▲' in MINT_GREEN or '▼' in RED
```

---

### 5.3 `infra_map.py`

GeoPandas Mercator map. No labels — purely visual.

```python
# Signature
def render(ax, geojson_path='data/infrastructure.json'):
    import geopandas as gpd
    gdf = gpd.read_file(geojson_path)
    gdf_proj = gdf.to_crs(epsg=3857)   # Web Mercator
    # Expressways: color=GANGA_BLUE, linewidth=2, alpha=0.8
    # Airports: ax.scatter(..., color=DEEP_SAFFRON, s=60)
    # Cities: ax.scatter(..., color=GOLD, s=30)
    # State boundary: edgecolor=WHITE, alpha=0.2, facecolor='none'
```

---

### 5.4 `cultural_layer.py`

Overlay silhouettes as `PathPatch` objects with low alpha.

| Silhouette | Position | Alpha | Color |
|------------|----------|-------|-------|
| Taj Mahal outline | Bottom-left | 0.15 | `GOLD` |
| Kashi Vishwanath spire | Bottom-right | 0.12 | `DEEP_SAFFRON` |
| Ganga river curve | Center horizontal | 0.08 | `GANGA_BLUE` |
| Banarasi sari border | Bottom strip | 0.25 | `VARANASI_MAROON` |

---

### 5.5 `skyline.py`

Pure Matplotlib vector paths. No raster images.

```python
# Signature
def render(ax):
    # Sky gradient: imshow with LinearSegmentedColormap
    # Silhouette fill: #1A2A3A
    # Three zones: Varanasi (left), Lucknow (center), Noida (right)
    # Window lights: Rectangle patches, color=GOLD, alpha=0.6
    # Glow: PathEffects.withSimplePatchShadow on tower paths
```

---

## 6. Responsive Behavior

### 6.1 Web Version (Flask + Jinja2)

The Flask web preview serves the poster as a static `<img>` tag. Responsive scaling via CSS only — no re-render at different sizes.

```css
/* In web/static/style.css */
.poster-canvas {
  max-width: 1080px;
  width: 100%;
  height: auto;
  display: block;
  margin: 0 auto;
}
```

| Breakpoint | Viewport | Poster Behavior |
|------------|----------|----------------|
| Mobile S | 375px | CSS scales img to 375px |
| Tablet | 768px | img at 700px centered |
| Desktop | 1200px+ | img at full 1080px |

---

## 7. Animation Specifications

Animations are **web-only** (CSS/JS in Jinja2 template). The Python poster generator always runs in `export_mode=True` equivalent — static final-state values only.

| Animation | Web Implementation | Export Behavior |
|-----------|-------------------|----------------|
| Metric count-up | CSS counter via JS `requestAnimationFrame` in template | Final value shown static |
| Expressway draw | SVG `stroke-dashoffset` animation in HTML | Static paths in PNG |
| Cultural fade-in | CSS `@keyframes` opacity | Full opacity in PNG |
| Hero glow pulse | CSS `@keyframes` box-shadow | Single glow state in PNG |

> **Rule:** Matplotlib render always produces the final static state. No animation state in Python code.

---

## 8. Accessibility

- Poster PNG: no embedded alt text (set on `<img>` tag in Flask template)
- Flask template `<img>` alt: `"Data visualization poster showing India's most populous state projected to 2050"`
- Download button: `aria-label="Download UP 2050 poster as PNG"`
- Web page has text description block for screen readers
- Color contrast ≥ 4.5:1 for all text on dark background (WCAG AA) — verify with `coolors.co/contrast-checker`

---

## 9. Social Media Caption Template

Same as v1 — unchanged:

> *240 million people. 1 river. 2 of the world's holiest cities. India's most ancient heartland — reimagined for 2050. From silk to silicon. From ghats to gigawatts. Which state am I? Drop your guess below.*
>
> `#WhichStateAmI` `@Hack2skill` `@Google for Developers`

---

*— End of Frontend Specification Document — · UP 2050 · Hack2Skill × Google for Developers*
