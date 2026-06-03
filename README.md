# 🚀 Project: Which State Am I? (2050 Edition)

## 📌 Challenge Details
* **Organizer:** Hack2skill & Google for Developers
* **Challenge:** Mini Challenge 2 - Which State Am I?
* **Theme:** Fast forward to 2050
* **Deadline:** 07/06/2026 11:59:00 PM (IST)
* **Core Rule:** NEVER mention the state name anywhere on the poster or social media post. Compliance is strict.

## 🛠️ Tech Stack 
*(Switched from JS/React to Python Data Science Stack)*
* **Visuals & Rendering:** Python, Matplotlib, Pillow
* **Geospatial:** GeoPandas
* **Web Server/API:** Flask
* **Deployment:** Render (Free Tier)

## 📊 Current Production Stage: **Phase 3 - Asset Generation (COMPLETED)**
* ✅ **Phase 1: Planning** - Docs updated to Python architecture (PRD, TechArch, FrontendSpec).
* ✅ **Phase 2: Environment** - Folder structure and requirements mapped.
* ✅ **Phase 3: Poster Engine** - Python scripts built to render data, culture, and skyline layers.
* ✅ **Phase 4: Bug Squashing** - 
  * Removed white box artifacts (transparent backgrounds fixed).
  * Enforced compliance (Removed actual state name from data layer).
  * Upgraded skyline (Added Rumi Darwaza and Ghats elements).

## ⏭️ Next Steps
1. **Phase 5: Web Wrapper & Deployment**
   * Wrap the Matplotlib generation logic in a Flask web app (`web/app.py`).
   * Add `render.yaml` and deploy to Render.
2. **Phase 6: Social & Final Submission**
   * Draft compliant LinkedIn/Instagram caption.
   * Add required tags: `@Hack2skill`, `@Google for Developers`, `#WhichStateAmI`.
   * Submit link on portal before deadline (4 days remaining).

## 📂 Project Structure
```text
project_root/
├── poster/               # Core image generation modules
│   ├── __init__.py
│   ├── cultural.py       # Heritage elements (Taj, Kashi)
│   ├── data_layer.py     # Stats and metrics (2050 futuristic data)
│   ├── skyline.py        # Tech city + heritage skyline
│   └── generator.py      # Main composition script (GridSpec)
├── web/                  # Web server wrappers
│   └── app.py            # Flask app to serve generated image
├── utils/                # Helpers
│   └── palette.py        # Color constants
├── requirements.txt      # Python dependencies
├── render.yaml           # Deployment config
└── README.md             # You are here
