"""
UP 2050 — Hero Section Renderer
Renders the top band: large '2050' headline with glow effect,
tagline text, and gradient background.
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

# Local constant — gradient color
DARK_BLUE_HEX = '#0D3F5E'


def render(ax, year='2050', tagline='The Future Is Ancient',
           subtext='A State Reimagined', export_mode=True):
    """Render the hero section into the given Axes.
    
    Args:
        ax: Matplotlib Axes for this zone.
        year: Display year (default '2050').
        tagline: Main tagline text.
        subtext: Secondary subtext.
        export_mode: If True, render static final state.
    """
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_facecolor(CHARCOAL_NIGHT)
    
    # Background gradient: dark bottom to slightly lighter top
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    gradient = np.vstack([gradient] * 50)
    cmap = LinearSegmentedColormap.from_list('hero_grad', [
        NIGHT_SKY, CHARCOAL_NIGHT, DARK_BLUE_HEX
    ])
    ax.imshow(gradient.T, aspect='auto', cmap=cmap, extent=[0, 1, 0, 1],
              alpha=0.5, zorder=0)
    
    # Glow effect behind the year text — rendered first, offset, with alpha
    ax.text(0.5, 0.55, year,
            fontsize=SIZE_HERO + 4, fontweight=WEIGHT_BOLD,
            fontfamily=FONT_DISPLAY, color=GLOW_CYAN,
            ha='center', va='center', transform=ax.transAxes,
            alpha=GLOW_ALPHA, zorder=1)
    
    # Main year text
    ax.text(0.5, 0.55, year,
            fontsize=SIZE_HERO, fontweight=WEIGHT_BOLD,
            fontfamily=FONT_DISPLAY, color=WHITE,
            ha='center', va='center', transform=ax.transAxes,
            zorder=2)
    
    # Tagline
    ax.text(0.5, 0.22, tagline.upper(),
            fontsize=SIZE_HERO_SUB, fontweight=WEIGHT_BOLD,
            fontfamily=FONT_DISPLAY, color=GOLD,
            ha='center', va='center', transform=ax.transAxes,
            zorder=2)
    
    # Subtext line
    ax.text(0.5, 0.06, subtext,
            fontsize=SIZE_BODY, fontweight=WEIGHT_REGULAR,
            fontfamily=FONT_BODY, color=PALE_MIST,
            ha='center', va='center', transform=ax.transAxes,
            alpha=0.7, zorder=2)
    
    # Decorative accent lines
    ax.plot([0.15, 0.40], [0.38, 0.38], color=GOLD, linewidth=1.0,
            alpha=0.4, transform=ax.transAxes, zorder=2)
    ax.plot([0.60, 0.85], [0.38, 0.38], color=GOLD, linewidth=1.0,
            alpha=0.4, transform=ax.transAxes, zorder=2)
    
    # Small diamond accent at center of lines
    ax.plot(0.5, 0.38, marker='D', color=GOLD, markersize=4,
            alpha=0.6, transform=ax.transAxes, zorder=2)


