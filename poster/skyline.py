"""
UP 2050 — Skyline Renderer
Three-city merged skyline via Matplotlib Path patches:
  Left:   Varanasi ghats + temple spires
  Center: Lucknow — Rumi Darwaza dome + Bara Imambara
  Right:  Noida tech towers + glass buildings

All pure Matplotlib vector paths. No raster images.
"""

import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Rectangle
from matplotlib.colors import LinearSegmentedColormap
from utils.palette import (
    CHARCOAL_NIGHT, NIGHT_SKY, GANGA_BLUE, DEEP_SAFFRON,
    GOLD, WHITE, DARK_BLUE, GLOW_CYAN,
    FONT_DISPLAY, SIZE_CAPTION, WEIGHT_BOLD
)


def render(ax, export_mode=True):
    """Render the three-city skyline into the given Axes.
    
    Args:
        ax: Matplotlib Axes for this zone.
        export_mode: If True, render static final state.
    """
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_facecolor(CHARCOAL_NIGHT)
    
    # Sky gradient background
    gradient = np.linspace(0, 1, 256).reshape(-1, 1)
    gradient = np.hstack([gradient] * 50)
    cmap = LinearSegmentedColormap.from_list('sky_grad', [
        NIGHT_SKY, DARK_BLUE, GANGA_BLUE
    ])
    ax.imshow(gradient, aspect='auto', cmap=cmap, extent=[0, 1, 0, 1],
              alpha=0.3, zorder=0)
    
    # === VARANASI GHATS (Left zone: 0.0 - 0.33) ===
    _draw_varanasi_ghats(ax)
    
    # === LUCKNOW (Center zone: 0.33 - 0.66) ===
    _draw_lucknow(ax)
    
    # === NOIDA TECH TOWERS (Right zone: 0.66 - 1.0) ===
    _draw_noida_towers(ax)
    
    # Ground line / water reflection
    ax.plot([0, 1], [0.08, 0.08], color=GANGA_BLUE, linewidth=1.5,
            alpha=0.4, transform=ax.transAxes, zorder=5)
    
    # Subtle water reflection
    for i in range(3):
        y = 0.06 - i * 0.015
        ax.plot([0, 1], [y, y], color=GANGA_BLUE, linewidth=0.5,
                alpha=0.1 - i * 0.03, transform=ax.transAxes, zorder=5)


def _draw_varanasi_ghats(ax):
    """Draw Varanasi ghat steps + temple spires on the left."""
    building_color = '#1A2A3A'
    
    # Ghat steps (staircase descending to water)
    steps = [
        (0.02, 0.08, 0.06, 0.30),
        (0.04, 0.08, 0.05, 0.35),
        (0.07, 0.08, 0.04, 0.40),
        (0.10, 0.08, 0.05, 0.45),
        (0.13, 0.08, 0.04, 0.38),
    ]
    for x, y_base, w, h in steps:
        rect = Rectangle((x, y_base), w, h, 
                         facecolor=building_color, edgecolor=GANGA_BLUE,
                         linewidth=0.3, alpha=0.8,
                         transform=ax.transAxes, zorder=2)
        ax.add_patch(rect)
    
    # Temple spire 1 (tall, pointed)
    spire_verts = [
        (0.16, 0.08), (0.16, 0.55), (0.175, 0.72),
        (0.19, 0.55), (0.19, 0.08), (0.16, 0.08)
    ]
    spire_codes = [Path.MOVETO, Path.LINETO, Path.LINETO,
                   Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
    path = Path(spire_verts, spire_codes)
    patch = PathPatch(path, facecolor=building_color, edgecolor=GOLD,
                      linewidth=0.5, alpha=0.9,
                      transform=ax.transAxes, zorder=3)
    ax.add_patch(patch)
    
    # Kashi Vishwanath-inspired spire (taller, with crown)
    spire2_verts = [
        (0.21, 0.08), (0.21, 0.50), (0.22, 0.65),
        (0.225, 0.78), (0.23, 0.65), (0.24, 0.50),
        (0.24, 0.08), (0.21, 0.08)
    ]
    spire2_codes = [Path.MOVETO] + [Path.LINETO] * 6 + [Path.CLOSEPOLY]
    path2 = Path(spire2_verts, spire2_codes)
    patch2 = PathPatch(path2, facecolor=building_color, edgecolor=DEEP_SAFFRON,
                       linewidth=0.5, alpha=0.9,
                       transform=ax.transAxes, zorder=3)
    ax.add_patch(patch2)
    
    # Small temple finial on spire
    ax.plot(0.225, 0.80, marker='o', color=GOLD, markersize=3,
            alpha=0.8, transform=ax.transAxes, zorder=4)
    
    # More ghat buildings
    for x, h in [(0.26, 0.42), (0.29, 0.35), (0.31, 0.30)]:
        rect = Rectangle((x, 0.08), 0.025, h,
                         facecolor=building_color, edgecolor=GANGA_BLUE,
                         linewidth=0.2, alpha=0.7,
                         transform=ax.transAxes, zorder=2)
        ax.add_patch(rect)
    
    # Window lights on ghat buildings
    _add_windows(ax, 0.03, 0.12, 0.28, 0.45, count=8)


def _draw_lucknow(ax):
    """Draw Lucknow — Rumi Darwaza arch + Bara Imambara dome."""
    building_color = '#1A2A3A'
    
    # Bara Imambara base
    rect = Rectangle((0.38, 0.08), 0.24, 0.35,
                     facecolor=building_color, edgecolor=WHITE,
                     linewidth=0.3, alpha=0.8,
                     transform=ax.transAxes, zorder=2)
    ax.add_patch(rect)
    
    # Central dome (Rumi Darwaza inspired arch)
    dome_verts = [
        (0.42, 0.43), (0.43, 0.55), (0.45, 0.64),
        (0.47, 0.70), (0.50, 0.73), (0.53, 0.70),
        (0.55, 0.64), (0.57, 0.55), (0.58, 0.43),
        (0.42, 0.43)
    ]
    dome_codes = [Path.MOVETO] + [Path.LINETO] * 8 + [Path.CLOSEPOLY]
    path = Path(dome_verts, dome_codes)
    patch = PathPatch(path, facecolor=building_color, edgecolor=GOLD,
                      linewidth=0.8, alpha=0.9,
                      transform=ax.transAxes, zorder=3)
    ax.add_patch(patch)
    
    # Dome finial
    ax.plot(0.50, 0.75, marker='o', color=GOLD, markersize=3,
            alpha=0.9, transform=ax.transAxes, zorder=4)
    ax.plot([0.50, 0.50], [0.73, 0.78], color=GOLD, linewidth=0.8,
            alpha=0.7, transform=ax.transAxes, zorder=4)
    
    # Side minarets
    for x_pos in [0.38, 0.62]:
        minaret_verts = [
            (x_pos - 0.01, 0.08), (x_pos - 0.01, 0.55),
            (x_pos, 0.62), (x_pos + 0.01, 0.55),
            (x_pos + 0.01, 0.08), (x_pos - 0.01, 0.08)
        ]
        m_codes = [Path.MOVETO] + [Path.LINETO] * 4 + [Path.CLOSEPOLY]
        m_path = Path(minaret_verts, m_codes)
        m_patch = PathPatch(m_path, facecolor=building_color,
                           edgecolor=WHITE, linewidth=0.3, alpha=0.8,
                           transform=ax.transAxes, zorder=3)
        ax.add_patch(m_patch)
        # Minaret top
        ax.plot(x_pos, 0.63, marker='o', color=GOLD, markersize=2,
                alpha=0.7, transform=ax.transAxes, zorder=4)
    
    # Archway (Rumi Darwaza arch opening)
    arch_verts = [
        (0.46, 0.08), (0.46, 0.30), (0.47, 0.36),
        (0.50, 0.38), (0.53, 0.36), (0.54, 0.30),
        (0.54, 0.08), (0.46, 0.08)
    ]
    arch_codes = [Path.MOVETO] + [Path.LINETO] * 6 + [Path.CLOSEPOLY]
    arch_path = Path(arch_verts, arch_codes)
    arch_patch = PathPatch(arch_path, facecolor=CHARCOAL_NIGHT,
                          edgecolor=GOLD, linewidth=0.5, alpha=0.9,
                          transform=ax.transAxes, zorder=4)
    ax.add_patch(arch_patch)
    
    # Window lights
    _add_windows(ax, 0.39, 0.15, 0.60, 0.40, count=10)


def _draw_noida_towers(ax):
    """Draw Noida tech towers — modern glass buildings."""
    building_color = '#1A2A3A'
    glass_color = '#1E3A5F'
    
    # Tower definitions: (x, width, height)
    towers = [
        (0.68, 0.03, 0.65),  # Tall thin tower
        (0.72, 0.04, 0.55),  # Medium tower
        (0.77, 0.035, 0.70), # Tallest tower
        (0.82, 0.03, 0.48),  # Short tower
        (0.86, 0.04, 0.60),  # Medium-tall tower
        (0.91, 0.03, 0.40),  # Short tower
        (0.95, 0.035, 0.52), # Medium tower
    ]
    
    for x, w, h in towers:
        # Main tower body
        rect = Rectangle((x, 0.08), w, h,
                         facecolor=glass_color, edgecolor=GLOW_CYAN,
                         linewidth=0.3, alpha=0.85,
                         transform=ax.transAxes, zorder=2)
        ax.add_patch(rect)
        
        # Antenna/spire on top
        ax.plot([x + w/2, x + w/2], [0.08 + h, 0.08 + h + 0.04],
                color=GLOW_CYAN, linewidth=0.5, alpha=0.6,
                transform=ax.transAxes, zorder=3)
        
        # Horizontal floor lines
        n_floors = int(h * 20)
        for floor in range(n_floors):
            floor_y = 0.08 + (floor / n_floors) * h
            ax.plot([x, x + w], [floor_y, floor_y],
                    color=GLOW_CYAN, linewidth=0.15, alpha=0.2,
                    transform=ax.transAxes, zorder=3)
    
    # Window lights for tech towers
    _add_windows(ax, 0.68, 0.12, 0.98, 0.70, count=20, color=GLOW_CYAN)


def _add_windows(ax, x_min, y_min, x_max, y_max, count=10, color=GOLD):
    """Add random window light dots in the given region."""
    np.random.seed(42)  # Reproducible
    xs = np.random.uniform(x_min, x_max, count)
    ys = np.random.uniform(y_min, y_max, count)
    alphas = np.random.uniform(0.3, 0.7, count)
    sizes = np.random.uniform(1.0, 2.5, count)
    
    for x, y, a, s in zip(xs, ys, alphas, sizes):
        ax.plot(x, y, marker='s', color=color, markersize=s,
                alpha=a, transform=ax.transAxes, zorder=6)
