# UP 2050 — Technical Architecture Document
## Hack2Skill × Google for Developers · v1.0 · June 2026

---

## 1. Architecture Overview

The UP 2050 project has two layers: a **static image layer** (the primary deliverable) and an **optional interactive web layer** (bonus). The architecture supports both outputs from a single React codebase using server-side rendering and canvas export.

### 1.1 System Diagram — Component Layers

| Layer | Technology | Purpose | Output |
|-------|------------|---------|--------|
| Data Layer | JSON / CSV static files | Holds all UP 2050 projections, metrics | Consumed by viz components |
| Design System | Tailwind CSS + custom tokens | Color palette, typography, spacing | Applied to all UI components |
| Visualization Engine | D3.js v7 + Recharts | Data charts, maps, timelines | SVG renders inside poster |
| Poster Canvas | React + html2canvas | Composes all elements into poster | 1080×1080 PNG export |
| Web App Shell | React 18 + Vite | Dev server, hot reload, routing | localhost + Vercel deploy |
| Export Pipeline | html2canvas + FileSaver.js | High-res image export | PNG file for social upload |
| Deployment | Vercel (free tier) | Hosts interactive version | Live URL for hackathon link |

---

## 2. Tech Stack Decision Log

### 2.1 Core Stack

| Tool | Version | Why Chosen | Alternatives Rejected |
|------|---------|------------|----------------------|
| React | 18.x | Component-based poster construction, easy state management | Vue (less ecosystem for canvas export) |
| Vite | 5.x | Fast dev server, optimal build for Vercel deploy | CRA (slow), Next.js (overkill) |
| D3.js | 7.x | Best-in-class data viz, SVG control for poster elements | Chart.js (less control), Plotly (heavy) |
| Tailwind CSS | 3.x | Utility-first, easy responsive layout | Styled-components (verbose), CSS Modules |
| html2canvas | 1.4.x | Converts React DOM to canvas for PNG export | Puppeteer (server-side, complex) |
| Vercel | — | Free, instant deploy from GitHub, custom domain | Netlify (comparable), GitHub Pages (static only) |

### 2.2 Data Sources

| Data Point | Source | Format |
|------------|--------|--------|
| UP 2050 GDP Projection | NITI Aayog State Vision Documents | JSON (manual entry) |
| Population Pyramid 2050 | Census 2011 + UN World Population Prospects | CSV |
| Expressway Network Coordinates | UPEIDA official data | GeoJSON |
| Renewable Energy Targets | UP New & Renewable Energy Development Agency (UPNEDA) | JSON |
| Literacy Rate Trend | ASER / NFHS data + extrapolation | JSON |
| Urbanization Rate | World Bank India urbanization + UP state share | JSON |

---

## 3. Application Architecture

### 3.1 Folder Structure

```
up2050/
├── public/
│   └── assets/          # Static icons, silhouettes (SVG)
├── src/
│   ├── components/      # Poster section components
│   │   ├── HeroSection.jsx
│   │   ├── DataPulse.jsx
│   │   ├── InfraMap.jsx
│   │   ├── CulturalLayer.jsx
│   │   ├── SkylineIllustration.jsx
│   │   └── PosterCanvas.jsx
│   ├── data/            # Static JSON data files
│   │   ├── projections.json
│   │   ├── demographics.json
│   │   └── infrastructure.json
│   ├── hooks/           # Custom React hooks
│   │   └── usePosterExport.js
│   ├── utils/           # Helper functions
│   │   ├── dataTransform.js
│   │   └── colorPalette.js
│   ├── App.jsx
│   └── main.jsx
├── vite.config.js
└── package.json
```

### 3.2 Component Architecture

| Component | Responsibility | Key Props / State |
|-----------|---------------|-------------------|
| `PosterCanvas` | Root poster container — 1080px fixed width grid | `exportMode: bool` |
| `HeroSection` | 2050 headline, countdown, color sweep background | `year`, `tagline` |
| `DataPulse` | 4 key metric cards (GDP, Population, Renewables, Literacy) | `metrics: Array<{label, value, unit, delta}>` |
| `InfraMap` | SVG map of expressways + airports radiating from center | `routes: GeoJSON features` |
| `CulturalLayer` | Iconic silhouettes overlay (Taj, Ganga, Kashi spire) | `opacity`, `showLabels: false` |
| `SkylineIllustration` | 2050 city skyline SVG — Varanasi + Noida merged | `animated: bool` |
| `DemographicPyramid` | Population pyramid chart (D3) | `data: {male, female, ageGroups}` |
| `PosterExportBtn` | Triggers html2canvas + file download | `targetRef`, `filename` |

---

## 4. Data Flow

### 4.1 Data Pipeline

All data is static (no API calls at runtime). Data flows from JSON files through transformation utilities into D3/Recharts visualization components, which render inside the `PosterCanvas` container.

```
projections.json    → dataTransform.js → DataPulse.jsx         → SVG/HTML render
demographics.json   → dataTransform.js → DemographicPyramid.jsx → D3 SVG
infrastructure.json →                  → InfraMap.jsx           → D3 geo projection → SVG paths
```

### 4.2 Export Flow

1. User clicks **'Export Poster'** button
2. `usePosterExport` hook calls `html2canvas` on `PosterCanvas` ref
3. `html2canvas` renders DOM to `<canvas>` at 2× pixel ratio (2160×2160 for retina)
4. `canvas.toBlob()` → `FileSaver.js` saves as `'UP2050_Poster.png'`
5. User uploads PNG to LinkedIn/Instagram manually

> ⚠️ **Known Issue:** `html2canvas` has known issues with certain CSS transforms and web fonts. All custom fonts must be loaded before export trigger. Use a loading state guard.

---

## 5. Deployment Architecture

### 5.1 Vercel Deployment

| Step | Action | Command / Config |
|------|--------|-----------------|
| 1 | Push to GitHub repo | `git push origin main` |
| 2 | Connect Vercel to GitHub repo | Vercel dashboard → Import project |
| 3 | Set build command | `vite build` |
| 4 | Set output directory | `dist` |
| 5 | Auto-deploy on push | Vercel webhook (automatic) |
| 6 | Custom URL | `vercel.app` subdomain (free) or custom domain |

### 5.2 Performance Targets

| Metric | Target | Strategy |
|--------|--------|----------|
| First Contentful Paint | < 1.5s | Vite code splitting + CDN assets |
| Poster Export Time | < 4s | Lazy load non-critical components |
| Lighthouse Performance | > 90 | Preload fonts, optimize SVGs |
| Mobile compatibility | 375px+ viewport | Tailwind responsive utilities |
| Bundle Size | < 200KB gzipped | Tree-shaking D3 modules individually |

---

## 6. Security & Compliance

- No user data collected — fully static, no backend
- No API keys in client code — all data is static JSON
- GDPR not applicable — no PII collected
- Content compliance: zero state name in any rendered text (enforced via code review checklist)
- Image export: no third-party tracking pixels in PNG output

---

## 7. Development Environment Setup

```bash
# Prerequisites: Node.js 18+, npm 9+
git clone https://github.com/[your-username]/up2050
cd up2050
npm install
npm run dev          # Start dev server at localhost:5173
npm run build        # Production build → dist/
npm run preview      # Preview production build locally
```

### Dependencies

| Dependency | Version | Purpose |
|------------|---------|---------|
| `react` | ^18.3.0 | UI framework |
| `react-dom` | ^18.3.0 | DOM renderer |
| `vite` | ^5.4.0 | Build tool |
| `d3` | ^7.9.0 | Data visualization |
| `recharts` | ^2.12.0 | Charting (secondary) |
| `html2canvas` | ^1.4.1 | Poster export |
| `file-saver` | ^2.0.5 | File download |
| `tailwindcss` | ^3.4.0 | CSS framework |
| `@tailwindcss/vite` | ^4.0.0 | Tailwind Vite plugin |
| `lodash` | ^4.17.21 | Data utilities |

---

*— End of Technical Architecture Document — · UP 2050 · Hack2Skill × Google for Developers*
