"""
UP 2050 — Hero Section Renderer
"""

import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from utils.palette import (
    CHARCOAL_NIGHT, NIGHT_SKY, GANGA_BLUE, DEEP_SAFFRON,
    GOLD, WHITE, PALE_MIST, GLOW_CYAN,
    FONT_DISPLAY, FONT_BODY,
    SIZE_HERO, SIZE_HERO_SUB, SIZE_BODY,
    WEIGHT_BOLD, WEIGHT_REGULAR, GLOW_ALPHA
)

DARK_BLUE_HEX = '#0D3F5E'


def render(ax, year='2050', tagline='The Future Is Ancient',
           subtext='A State Reimagined', export_mode=True):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_facecolor(CHARCOAL_NIGHT)

    # Background gradient
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    gradient = np.vstack([gradient] * 50)
    cmap = LinearSegmentedColormap.from_list('hero_grad', [
        NIGHT_SKY, CHARCOAL_NIGHT, DARK_BLUE_HEX
    ])
    ax.imshow(gradient.T, aspect='auto', cmap=cmap, extent=[0, 1, 0, 1],
              alpha=0.5, zorder=0)

    # Glow behind year
    ax.text(0.5, 0.70, year,
            fontsize=SIZE_HERO + 4, fontweight=WEIGHT_BOLD,
            fontfamily=FONT_DISPLAY, color=GLOW_CYAN,
            ha='center', va='center', transform=ax.transAxes,
            alpha=GLOW_ALPHA, zorder=1)

    # Main year
    ax.text(0.5, 0.70, year,
            fontsize=SIZE_HERO, fontweight=WEIGHT_BOLD,
            fontfamily=FONT_DISPLAY, color=WHITE,
            ha='center', va='center', transform=ax.transAxes,
            zorder=2)

    # Tagline — pushed down, smaller
    ax.text(0.5, 0.32, tagline.upper(),
            fontsize=SIZE_HERO_SUB - 6, fontweight=WEIGHT_BOLD,
            fontfamily=FONT_DISPLAY, color=GOLD,
            ha='center', va='center', transform=ax.transAxes,
            zorder=2)

    # Subtext
    ax.text(0.5, 0.10, subtext,
            fontsize=SIZE_BODY - 2, fontweight=WEIGHT_REGULAR,
            fontfamily=FONT_BODY, color=PALE_MIST,
            ha='center', va='center', transform=ax.transAxes,
            alpha=0.7, zorder=2)

    # Accent lines — repositioned to sit between year and tagline
    ax.plot([0.15, 0.38], [0.50, 0.50], color=GOLD, linewidth=1.0,
            alpha=0.4, transform=ax.transAxes, zorder=2)
    ax.plot([0.62, 0.85], [0.50, 0.50], color=GOLD, linewidth=1.0,
            alpha=0.4, transform=ax.transAxes, zorder=2)
    ax.plot(0.5, 0.50, marker='D', color=GOLD, markersize=4,
            alpha=0.6, transform=ax.transAxes, zorder=2)