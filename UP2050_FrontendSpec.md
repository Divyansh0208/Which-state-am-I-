# UP 2050 — Frontend Design & Component Specification
## Hack2Skill × Google for Developers · v1.0 · June 2026

---

## 1. Design Philosophy

The UP 2050 poster is designed on three principles:

- **Data Honesty** — every number has a source
- **Visual Restraint** — no clutter; the state identity must emerge from negative space as much as detail
- **Cultural Authenticity** — the visual language must feel North Indian, not generic futurism

The aesthetic sits at the intersection of ISRO mission posters, NYT data journalism, and Indian modernist print design. Think bold, structured, deeply informative — but beautiful.

---

## 2. Color System

### 2.1 Primary Palette

The palette is derived from UP's natural and cultural identity — Ganga blue, saffron, gold, and deep Varanasi silk maroon — reinterpreted for a 2050 futuristic lens.

| Token Name | Hex | Usage |
|------------|-----|-------|
| `color-primary` · Ganga Blue | `#1A6B8A` | Headlines, data accents, map paths |
| `color-accent` · Deep Saffron | `#FF6B00` | CTAs, highlighted metrics, hero glow |
| `color-gold` · Gold | `#FFD700` | Cultural layer highlights, border accents |
| `color-background` · Charcoal Night | `#1A1A2E` | Main poster background |
| `color-heritage` · Varanasi Maroon | `#8B1A1A` | Cultural iconography, silk border |
| `color-growth` · Mint Green | `#00C853` | Growth arrows, positive delta indicators |
| `color-text-muted` · Pale Mist | `#E8EAF6` | Secondary text, subtitles |
| `color-text-primary` · Pure White | `#FFFFFF` | Primary text on dark background |

### 2.2 Dark Background Rationale

The poster uses a dark (`#1A1A2E`) background. This is a deliberate design choice — it makes colored data visualizations pop, creates a 'space mission' aesthetic appropriate for 2050, and photographs well for social media screenshots.

---

## 3. Typography System

| Role | Font | Size | Weight | Color | Usage |
|------|------|------|--------|-------|-------|
| Display Headline | Space Grotesk | 72–96px | 700 | `#FFFFFF` | 2050 year, main headline |
| Section Title | Space Grotesk | 32–40px | 600 | `#1A6B8A` | Section headers |
| Data Label | Inter | 18–24px | 500 | `#FFD700` | Metric values, percentages |
| Body Copy | Inter | 14–16px | 400 | `#E8EAF6` | Descriptions, subtitles |
| Accent Script | Tiro Devanagari Hindi | 24–32px | 400 | `#FFD700` | Hindi text overlays |
| Caption | Inter Mono | 12px | 400 | `#888888` | Data source footnotes |

### 3.1 Font Loading

```css
/* In index.css — load via Google Fonts */
@import url('https://fonts.googleapis.com/css2?
  family=Space+Grotesk:wght@400;500;600;700&
  family=Inter:wght@400;500;600&
  family=Tiro+Devanagari+Hindi&display=swap');
```

> **CRITICAL:** All fonts must be fully loaded before triggering `html2canvas` export. Use `document.fonts.ready` promise in `usePosterExport` hook.

---

## 4. Grid & Layout System

### 4.1 Poster Canvas Dimensions

| Format | Dimensions | Aspect Ratio | Use Case |
|--------|------------|-------------|----------|
| Instagram Square | 1080 × 1080px | 1:1 | Primary — Instagram feed |
| Instagram Portrait | 1080 × 1350px | 4:5 | Better reach on Instagram algorithm |
| LinkedIn Landscape | 1200 × 627px | 1.91:1 | LinkedIn link preview card |
| Story Format | 1080 × 1920px | 9:16 | Instagram/LinkedIn Stories |

Primary build target: **1080×1080 square**. Other formats derived via CSS scale transforms of same component tree.

### 4.2 Poster Grid Layout (1080×1080)

| Zone | Height | Content | Component |
|------|--------|---------|-----------|
| Hero Band | 200px | 2050 headline + tagline | `HeroSection` |
| Skyline Strip | 180px | City skyline SVG illustration | `SkylineIllustration` |
| Data Row | 160px | 4 metric cards (GDP, Pop, RE, Literacy) | `DataPulse` |
| Map Zone | 240px | Expressway + airport infrastructure map | `InfraMap` |
| Cultural Footer | 160px | Iconic silhouettes + heritage border | `CulturalLayer` |
| Caption Bar | 140px | Riddle caption + clue text (no state name) | `CaptionBar` |

---

## 5. Component Specifications

### 5.1 HeroSection

Renders the top band of the poster. Large `2050` year display with animated glow, sub-headline tagline, and subtle background gradient pulse.

```
Props:       { year: string, tagline: string, subtext: string }
Size:        1080px wide × 200px tall
Background:  linear-gradient from #1A1A2E to #0D2137
Headline:    '2050' — Space Grotesk 96px Bold, color #FFFFFF
Tagline:     Space Grotesk 28px, color #1A6B8A
Subtext:     'Which State Am I?' prompt — Inter 18px, color #888888
```

---

### 5.2 DataPulse

Four metric cards showing key UP 2050 projections. Each card shows: metric icon, value (large), label, and delta arrow vs 2024 baseline.

| Metric Card | 2024 Baseline | 2050 Projection | Visual |
|-------------|--------------|-----------------|--------|
| GDP (USD Trillion) | $0.28T | $1.2T | Bar fill + gold number |
| Population (Millions) | 241M | 298M | Population icon + green delta |
| Renewable Energy % | 18% | 72% | Circular progress ring |
| Literacy Rate % | 73% | 96% | Upward arrow + mint color |

```
Props:    { metrics: Array<{id, label, baseline, projected, unit, icon}> }
Layout:   CSS grid, 4 columns, 270px per card
Card bg:  rgba(255,255,255,0.06) — semi-transparent glass effect
Value:    Space Grotesk 36px 700, color #FFD700
Delta:    Green (#00C853) positive / Red negative
```

---

### 5.3 InfraMap

SVG map showing UP's geographic footprint with expressway lines, airport dots, and city nodes. No labels — purely visual. Uses D3 geo projection.

```
Props:       { routes: GeoJSON, cities: Array<{name, coords, type}> }
Projection:  d3.geoMercator() centered on UP (~80.9E, 27.5N)
Expressways: stroke #1A6B8A, strokeWidth 2, opacity 0.8
Airports:    circle r=6, fill #FF6B00 (international/upcoming)
City nodes:  circle r=4, fill #FFD700
State boundary: stroke #FFFFFF opacity 0.2, fill none
Background:  transparent (sits on poster dark bg)
```

---

### 5.4 CulturalLayer

Overlay of iconic silhouettes that encode state identity without text. SVG paths, semi-transparent, positioned absolutely over the poster.

| Silhouette | Position | Opacity | Color |
|------------|----------|---------|-------|
| Taj Mahal outline | Bottom-left quadrant | 0.15 | `#FFD700` |
| Kashi Vishwanath spire | Bottom-right | 0.12 | `#FF6B00` |
| Ganga river curve | Center horizontal band | 0.08 | `#1A6B8A` |
| Banarasi sari border pattern | Bottom strip | 0.25 | `#8B1A1A` |

---

### 5.5 SkylineIllustration

Hand-crafted SVG skyline merging three UP cities: Varanasi ghats (left), Lucknow's Imambara dome (center), Noida tech towers (right) — unified under a single horizon.

```
Implementation:  Pure SVG paths (no raster images)
Dimensions:      1080px × 180px
Silhouette fill: #1A2A3A against gradient sky
Sky gradient:    #0D1B2A (top) to #1A3A5C (bottom) — night city glow
Window lights:   Small rect elements, fill #FFD700, opacity 0.6
Glow effect:     CSS filter drop-shadow on tower tops
```

---

## 6. Responsive Behavior

### 6.1 Web Version Breakpoints

| Breakpoint | Viewport | Poster Behavior |
|------------|----------|----------------|
| Mobile S | 375px | Poster scales to 375px width, aspect ratio maintained |
| Mobile L | 414px | Poster scales to 414px, scroll enabled |
| Tablet | 768px | Poster at 700px centered, export button visible |
| Desktop | 1200px+ | Poster at full 1080px, side panel with export |

```css
/* Poster scaling CSS */
.poster-canvas {
  width: 1080px;
  transform-origin: top center;
  transform: scale(min(1, calc(100vw / 1080px)));
}
```

---

## 7. Animation Specifications

| Animation | Trigger | Duration | Easing | Component |
|-----------|---------|----------|--------|-----------|
| Metric count-up | On mount | 1.5s | easeOutCubic | DataPulse |
| Expressway route draw | On mount | 2s | linear | InfraMap |
| Cultural silhouette fade-in | 500ms delay | 1s | easeIn | CulturalLayer |
| Skyline build-up | On mount | 1.8s | easeOutBack | SkylineIllustration |
| Hero glow pulse | Continuous loop | 3s | easeInOut | HeroSection |

> **IMPORTANT:** All animations must be **paused/disabled** when `exportMode = true`. `html2canvas` captures a single DOM frame — animated states will produce inconsistent exports. Apply `.no-animate` CSS class to root when export is triggered.

---

## 8. Accessibility

- All SVG elements have `aria-hidden="true"` (poster is a decorative visual)
- Export button: `aria-label="Export UP 2050 poster as PNG"`
- Web page has a text description of poster content for screen readers
- Color contrast ratio ≥ 4.5:1 for all text on dark background (WCAG AA)
- Keyboard navigation: Tab to export button, Enter to download

---

## 9. Social Media Caption Template

The caption is as important as the image. It must be engaging, use clues, and strictly avoid naming the state.

> *240 million people. 1 river. 2 of the world's holiest cities. India's most ancient heartland — reimagined for 2050. From silk to silicon. From ghats to gigawatts. Which state am I? Drop your guess below.*
>
> `#WhichStateAmI` `@Hack2skill` `@Google for Developers`

---

*— End of Frontend Specification Document — · UP 2050 · Hack2Skill × Google for Developers*
