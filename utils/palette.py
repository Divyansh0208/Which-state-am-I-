"""
UP 2050 — Design System: Color Tokens, Typography, and Constants
All visual constants in one place. No hardcoded hex strings elsewhere.
"""

# ─── Color Palette ────────────────────────────────────────────────
# Derived from cultural identity: Ganga, saffron, gold, Varanasi
GANGA_BLUE = '#1A6B8A'
DEEP_SAFFRON = '#FF6B00'
GOLD = '#FFD700'
CHARCOAL_NIGHT = '#1A1A2E'
VARANASI_MAROON = '#8B1A1A'
MINT_GREEN = '#00C853'
PALE_MIST = '#E8EAF6'
WHITE = '#FFFFFF'

# Extended palette for gradients and accents
DARK_BLUE = '#0D3F5E'
NIGHT_SKY = '#0F0F23'
GLOW_CYAN = '#00BCD4'
SOFT_GOLD = '#FFE082'
GRID_LINE = '#2A2A4E'

# ─── Typography ───────────────────────────────────────────────────
# Font families — using system-available fallbacks
# When custom TTFs are registered, update these names
FONT_DISPLAY = 'sans-serif'       # Headlines (Space Grotesk replacement)
FONT_BODY = 'sans-serif'          # Body text (Inter replacement)
FONT_MONO = 'monospace'           # Captions
FONT_DEVANAGARI = 'sans-serif'    # Hindi text (Tiro Devanagari replacement)

# Font sizes (in points, for 10.8x10.8 inch figure)
SIZE_HERO = 96
SIZE_HERO_SUB = 36
SIZE_SECTION_TITLE = 32
SIZE_DATA_VALUE = 40
SIZE_DATA_LABEL = 16
SIZE_BODY = 14
SIZE_CAPTION = 11
SIZE_ACCENT = 24

# Font weights
WEIGHT_BOLD = 'bold'
WEIGHT_SEMIBOLD = 'semibold'
WEIGHT_MEDIUM = 'medium'
WEIGHT_REGULAR = 'normal'

# ─── Canvas Constants ─────────────────────────────────────────────
POSTER_WIDTH = 10.8    # inches (1080px at 100dpi)
POSTER_HEIGHT = 10.8   # inches (1080px at 100dpi)
POSTER_DPI = 100       # base DPI
EXPORT_DPI = 216       # 2x export quality

# GridSpec height ratios (6 zones)
ZONE_RATIOS = [0.185, 0.167, 0.148, 0.222, 0.148, 0.130]

# ─── Visual Effects ───────────────────────────────────────────────
GLASS_ALPHA = 0.06     # Semi-transparent card background
GLOW_ALPHA = 0.3       # Text glow/shadow
SILHOUETTE_ALPHAS = {
    'taj': 0.15,
    'kashi': 0.12,
    'ganga': 0.08,
    'border': 0.25,
}
