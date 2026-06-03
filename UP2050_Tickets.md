# UP 2050 — Feature Ticket List & Sprint Board
## Hack2Skill × Google for Developers · 20 Tickets · 5 Epics · June 2026

---

## Sprint Overview

All work executes in a **single 5-day sprint (03–07 June 2026)**. Tickets are organized into 5 epics.

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

> Compile all data required for the poster's data visualizations. All sources must be credible (government / UN / World Bank). No made-up numbers.

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
Research NITI Aayog state vision docs, World Bank South Asia projections, and UP government budget documents. Extract GDP trajectory from 2024 to 2050. Store as `projections.json`.

**Acceptance Criteria**
JSON file exists at `src/data/projections.json` with GDP, urbanization, renewable energy, and literacy fields. All values sourced and noted.

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
Collect UN World Population Prospects data for UP state (Uttar Pradesh proxy from India national split). Build male/female age-group breakdown for 2024 and 2050. Store as `demographics.json`.

**Acceptance Criteria**
`demographics.json` contains `ageGroups` array with male/female counts for 2024 and 2050. Data verified against at least 2 sources.

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
Collect coordinates for: Ganga Expressway, Purvanchal Expressway, Bundelkhand Expressway, Agra-Lucknow Expressway, Jewar Airport, Kushinagar Airport, Varanasi Airport. Store as `infrastructure.json` with GeoJSON feature collection.

**Acceptance Criteria**
`infrastructure.json` contains valid GeoJSON `FeatureCollection`. All expressway paths render correctly on D3 Mercator projection centered on UP.

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
Create a source-attribution CSV that maps every displayed number on the poster to its source URL, publication year, and notes. This ensures defensibility if judges question data.

**Acceptance Criteria**
`source_attribution.csv` exists with columns: `metric, value, source_name, source_url, year, notes`. Minimum 10 rows.

---

## EPIC-2: Design System Setup

> Establish the visual foundation before any component work begins. All components pull from this system — no hardcoded colors or fonts in component files.

---

### `UP-005` · Set Up React + Vite + Tailwind Project

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 2 |
| **Due** | 03 Jun |
| **Epic** | EPIC-2: Design |
| **Dependencies** | — |

**Description**
Initialize project with `npm create vite@latest up2050 -- --template react`. Install and configure Tailwind CSS v3. Configure `vite.config.js`. Verify dev server runs at `localhost:5173`.

**Acceptance Criteria**
`npm run dev` launches without errors. Tailwind utility classes render correctly in browser. Project structure matches spec in TechArch doc.

---

### `UP-006` · Implement Color Token System

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 2 |
| **Due** | 04 Jun |
| **Epic** | EPIC-2: Design |
| **Dependencies** | UP-005 |

**Description**
Define all color tokens in `tailwind.config.js` `extend.colors` block using names from Frontend Spec section 2. Include: `ganga-blue`, `deep-saffron`, `gold`, `charcoal-night`, `varanasi-maroon`, `mint-green`, `pale-mist`.

**Acceptance Criteria**
All 7 color tokens resolve correctly in Tailwind classes (`bg-ganga-blue`, `text-gold`, etc.). Colors match hex values in Frontend Spec exactly.

---

### `UP-007` · Implement Typography System + Font Loading

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 3 |
| **Due** | 04 Jun |
| **Epic** | EPIC-2: Design |
| **Dependencies** | UP-005, UP-006 |

**Description**
Add Google Fonts import to `index.css` for Space Grotesk, Inter, Tiro Devanagari Hindi. Configure Tailwind `fontFamily` tokens. Implement `document.fonts.ready` guard in `main.jsx` before app renders.

**Acceptance Criteria**
All 3 fonts load correctly in browser. Font names match tokens in Tailwind config. Console shows no font-load errors.

---

### `UP-008` · Build PosterCanvas Skeleton (1080px fixed grid)

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 5 |
| **Due** | 04 Jun |
| **Epic** | EPIC-2: Design |
| **Dependencies** | UP-005, UP-006, UP-007 |

**Description**
Create `PosterCanvas.jsx` as the root poster container. Implement 6-zone vertical grid layout per Frontend Spec section 4.2. Each zone renders a placeholder `div` with correct height and label. Implement CSS scale transform for responsive viewing.

**Acceptance Criteria**
PosterCanvas renders at 1080px on desktop. Scale transform correctly adjusts poster to viewport width on mobile (375px test). All 6 zones visible with correct heights.

---

## EPIC-3: Poster Components

> Build each poster section as an isolated React component. Components are developed in order of visual priority (P0 first). All components receive data via props — no direct data imports inside components.

---

### `UP-009` · Build HeroSection Component

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 3 |
| **Due** | 04 Jun |
| **Epic** | EPIC-3: Components |
| **Dependencies** | UP-008 |

**Description**
Create `HeroSection.jsx`. Display large '2050' headline, tagline line, and subtext. Implement glow animation on '2050' text using CSS keyframe. Background: dark gradient. Export mode must disable animation.

**Acceptance Criteria**
HeroSection renders correctly in PosterCanvas zone 1. '2050' text displays at 96px Space Grotesk Bold. Animation plays in browser mode, stops when `exportMode=true`.

---

### `UP-010` · Build DataPulse Component (4 Metric Cards)

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 5 |
| **Due** | 05 Jun |
| **Epic** | EPIC-3: Components |
| **Dependencies** | UP-008, UP-001 |

**Description**
Create `DataPulse.jsx`. Render 4 metric cards in a 4-column grid. Each card shows icon, projected value (count-up animation), metric label, and delta vs baseline. Icons from `react-icons` or inline SVG. Count-up via `useEffect` + `requestAnimationFrame`.

**Acceptance Criteria**
All 4 metric cards render with correct data from `projections.json`. Count-up animation works in browser. Delta arrows show correct direction. Export mode: static final values shown, no animation.

---

### `UP-011` · Build InfraMap Component (D3 SVG Map)

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 5 |
| **Due** | 05 Jun |
| **Epic** | EPIC-3: Components |
| **Dependencies** | UP-008, UP-003 |

**Description**
Create `InfraMap.jsx` using D3 v7. Implement `geoMercator` projection centered on UP (lat 27.5, lon 80.9). Render expressway paths from `infrastructure.json` GeoJSON. Render airport dots and city dots. **No text labels on map.**

**Acceptance Criteria**
Map renders all 4 expressway routes as SVG paths. Airport dots visible at correct coordinates. Map fits within 1080×240px zone. No text labels visible on exported image.

---

### `UP-012` · Build SkylineIllustration Component (SVG Skyline)

| | |
|---|---|
| **Priority** | 🟡 P1 |
| **Points** | 5 |
| **Due** | 05 Jun |
| **Epic** | EPIC-3: Components |
| **Dependencies** | UP-008 |

**Description**
Create `SkylineIllustration.jsx` as a pure SVG illustration. Design three-city merged skyline: Varanasi ghats (left), Lucknow dome (center), Noida towers (right). Include window light elements. Sky gradient background.

**Acceptance Criteria**
SVG skyline clearly shows three distinct architectural identities. Renders crisply at 1080px width. **No raster images used** — pure SVG paths only.

---

### `UP-013` · Build CulturalLayer Component (Silhouette Overlays)

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 3 |
| **Due** | 05 Jun |
| **Epic** | EPIC-3: Components |
| **Dependencies** | UP-008 |

**Description**
Create `CulturalLayer.jsx` with 4 semi-transparent SVG silhouettes: Taj Mahal outline, Kashi Vishwanath spire, Ganga curve, Banarasi border pattern. Position as absolute overlays on the poster. Opacity values per Frontend Spec.

**Acceptance Criteria**
All 4 silhouettes render at correct positions and opacities. State identity is decodable without text labels. No visible text in component output.

---

### `UP-014` · Build DemographicPyramid Component

| | |
|---|---|
| **Priority** | 🟡 P1 |
| **Points** | 3 |
| **Due** | 05 Jun |
| **Epic** | EPIC-3: Components |
| **Dependencies** | UP-008, UP-002 |

**Description**
Create `DemographicPyramid.jsx` using D3. Classic horizontal bar chart mirrored for male/female. Show 2050 projection data only. Age groups on center Y axis, bar length = population. Color: male = Ganga Blue, female = Deep Saffron.

**Acceptance Criteria**
Pyramid renders with correct male/female bars for all age groups from `demographics.json`. No labels that mention state name. Fits within assigned poster zone.

---

## EPIC-4: Export & Deployment

> Critical path — without a working export, there is no submission. Treat these tickets as absolute P0 even if components are not 100% polished.

---

### `UP-015` · Implement Poster Export (html2canvas + FileSaver)

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 4 |
| **Due** | 06 Jun |
| **Epic** | EPIC-4: Export |
| **Dependencies** | UP-009 through UP-014 |

**Description**
Create `usePosterExport.js` hook. Implement:
1. Set `exportMode=true` on root
2. Wait for `document.fonts.ready`
3. Call `html2canvas` on `PosterCanvas` ref at `scale=2`
4. Convert canvas to blob
5. Use `FileSaver.js` to download `'UP2050_Poster.png'`
6. Set `exportMode=false`

**Acceptance Criteria**
Clicking export button downloads a valid PNG file. File is 2160×2160px (2× scale). All components visible in export. Fonts render correctly. No white boxes or missing elements.

---

### `UP-016` · Deploy to Vercel

| | |
|---|---|
| **Priority** | 🔴 P0 |
| **Points** | 2 |
| **Due** | 06 Jun |
| **Epic** | EPIC-4: Export |
| **Dependencies** | UP-015 |

**Description**
Push codebase to GitHub. Connect Vercel to repo. Configure build: `command=vite build`, `output=dist`. Trigger deploy. Verify live URL works. Share URL for hackathon portal submission.

**Acceptance Criteria**
Live URL accessible at `https://[project].vercel.app`. Poster renders correctly on desktop and mobile. Export button works on live site.

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
Manual audit of all rendered text in the exported PNG. Check:
1. Zero occurrences of 'Uttar Pradesh', 'UP', 'U.P.' or any district/city names that would make identification trivial
2. All data values match source attribution CSV
3. Tags/hashtag not in image (they go in caption)

**Acceptance Criteria**
Audit checklist signed off. Zero state name violations found. Data values verified. Image approved for upload.

---

## EPIC-5: Social Media & Submission

> The final mile. All technical work means nothing if the submission is rejected or the post is removed. Execute with precision.

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
Write final post caption using the template in Frontend Spec section 9. Must include: riddle framing, state clues (no name), `#WhichStateAmI` hashtag, `@Hack2skill` tag, `@Google for Developers` tag. Get a second pair of eyes to verify no state name slipped in.

**Acceptance Criteria**
Caption text reviewed and approved. Hashtag present. Both tags present. No state name visible. Caption is engaging — question format encourages comments.

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
Upload exported PNG to LinkedIn post (choose 'Photo' post type, not article). Add caption. Set visibility to **Public**. Post. Repeat on Instagram. Capture post URLs from both platforms.

**Acceptance Criteria**
Both posts live and publicly accessible. LinkedIn post URL copied. Instagram post URL copied. Both posts set to Public visibility.

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
Log in to Hack2Skill portal. Navigate to [Mini Challenge 2] Which State Am I? submission. Select challenge and theme 'Fast forward to 2050'. Paste LinkedIn post URL in submission field. Submit before **07/06/2026 11:59 PM IST**. Screenshot confirmation page.

**Acceptance Criteria**
Portal shows submission confirmed. Submission Attempts counter updates to 1/1. Screenshot of confirmation saved. Submitted before deadline.

---

## Ticket Summary

| # | Ticket | Epic | Pri | Pts | Due | Status |
|---|--------|------|-----|-----|-----|--------|
| UP-001 | Compile GDP & Economic Projections | E1 | 🔴 P0 | 3 | 03 Jun | To Do |
| UP-002 | Compile Demographic Data | E1 | 🔴 P0 | 3 | 03 Jun | To Do |
| UP-003 | Map Infrastructure Data | E1 | 🔴 P0 | 4 | 03 Jun | To Do |
| UP-004 | Source Attribution Table | E1 | 🟡 P1 | 3 | 04 Jun | To Do |
| UP-005 | React + Vite + Tailwind Setup | E2 | 🔴 P0 | 2 | 03 Jun | To Do |
| UP-006 | Color Token System | E2 | 🔴 P0 | 2 | 04 Jun | To Do |
| UP-007 | Typography + Font Loading | E2 | 🔴 P0 | 3 | 04 Jun | To Do |
| UP-008 | PosterCanvas Skeleton | E2 | 🔴 P0 | 5 | 04 Jun | To Do |
| UP-009 | HeroSection Component | E3 | 🔴 P0 | 3 | 04 Jun | To Do |
| UP-010 | DataPulse Component | E3 | 🔴 P0 | 5 | 05 Jun | To Do |
| UP-011 | InfraMap Component | E3 | 🔴 P0 | 5 | 05 Jun | To Do |
| UP-012 | SkylineIllustration Component | E3 | 🟡 P1 | 5 | 05 Jun | To Do |
| UP-013 | CulturalLayer Component | E3 | 🔴 P0 | 3 | 05 Jun | To Do |
| UP-014 | DemographicPyramid Component | E3 | 🟡 P1 | 3 | 05 Jun | To Do |
| UP-015 | Poster Export Implementation | E4 | 🔴 P0 | 4 | 06 Jun | To Do |
| UP-016 | Vercel Deployment | E4 | 🔴 P0 | 2 | 06 Jun | To Do |
| UP-017 | Pre-Export Compliance Audit | E4 | 🔴 P0 | 2 | 06 Jun | To Do |
| UP-018 | Write Post Caption | E5 | 🔴 P0 | 3 | 06 Jun | To Do |
| UP-019 | Post on LinkedIn + Instagram | E5 | 🔴 P0 | 2 | 07 Jun | To Do |
| UP-020 | Submit on Hack2Skill Portal | E5 | 🔴 P0 | 2 | 07 Jun | To Do |

**Total: 71 story points · 20 tickets · 5 epics · 5 days**

---

*— End of Feature Ticket List — · UP 2050 · Hack2Skill × Google for Developers*
