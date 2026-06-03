"""
UP 2050 — Cultural Layer Renderer
Semi-transparent silhouette overlays for cultural identity:
  - Taj Mahal outline (iconic dome + minarets)
  - Kashi Vishwanath spire
  - Ganga river curve (flowing across)
  - Banarasi sari border pattern (bottom strip)

All rendered as Matplotlib PathPatch objects with low alpha.
"""

import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Rectangle
from utils.palette import (
    CHARCOAL_NIGHT, GOLD, DEEP_SAFFRON, GANGA_BLUE,
    VARANASI_MAROON, WHITE, PALE_MIST,
    FONT_BODY, SIZE_CAPTION,
    SILHOUETTE_ALPHAS
)


def render(ax, export_mode=True):
    """Render cultural silhouette overlays into the given Axes.
    
    Args:
        ax: Matplotlib Axes for this zone.
        export_mode: If True, render static final state.
    """
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_facecolor(CHARCOAL_NIGHT)
    
    # Render layers bottom-to-top
    _draw_banarasi_border(ax)
    _draw_ganga_curve(ax)
    _draw_taj_silhouette(ax)
    _draw_kashi_spire(ax)
    
    # Cultural accent tagline
    ax.text(0.5, 0.93, 'FROM SILK TO SILICON  |  FROM GHATS TO GIGAWATTS',
            fontsize=SIZE_CAPTION + 1, fontweight='bold',
            fontfamily=FONT_BODY, color=GOLD,
            ha='center', va='center', transform=ax.transAxes,
            alpha=0.6, zorder=10)


def _draw_taj_silhouette(ax):
    """Draw Taj Mahal dome + minarets — bottom-left area."""
    alpha = SILHOUETTE_ALPHAS['taj']
    
    # Base platform
    base = Rectangle((0.05, 0.15), 0.35, 0.04,
                     facecolor=GOLD, edgecolor='none',
                     alpha=alpha * 0.6, transform=ax.transAxes, zorder=2)
    ax.add_patch(base)
    
    # Main dome — smooth onion shape
    dome_x = np.array([0.12, 0.14, 0.16, 0.18, 0.20, 0.22, 0.225,
                        0.23, 0.225, 0.22, 0.20, 0.18, 0.16, 0.14, 0.12])
    dome_y = np.array([0.19, 0.30, 0.42, 0.55, 0.65, 0.72, 0.76,
                        0.78, 0.76, 0.72, 0.65, 0.55, 0.42, 0.30, 0.19])
    
    # Mirror around center (0.225) for right side
    full_x = np.concatenate([dome_x, 0.45 - dome_x[::-1]])
    full_y = np.concatenate([dome_y, dome_y[::-1]])
    
    verts = list(zip(full_x, full_y))
    verts.append(verts[0])  # close
    codes = [Path.MOVETO] + [Path.LINETO] * (len(verts) - 2) + [Path.CLOSEPOLY]
    path = Path(verts, codes)
    patch = PathPatch(path, facecolor=GOLD, edgecolor='none',
                      alpha=alpha, transform=ax.transAxes, zorder=3)
    ax.add_patch(patch)
    
    # Finial spire on top
    ax.plot([0.225, 0.225], [0.78, 0.85], color=GOLD, linewidth=1.5,
            alpha=alpha + 0.05, transform=ax.transAxes, zorder=4)
    ax.plot(0.225, 0.86, marker='o', color=GOLD, markersize=2.5,
            alpha=alpha + 0.05, transform=ax.transAxes, zorder=4)
    
    # Left minaret
    _draw_minaret(ax, 0.07, alpha, GOLD)
    # Right minaret
    _draw_minaret(ax, 0.38, alpha, GOLD)


def _draw_minaret(ax, x_center, alpha, color):
    """Draw a single minaret tower."""
    w = 0.012
    verts = [
        (x_center - w, 0.19), (x_center - w, 0.58),
        (x_center - w * 0.6, 0.62), (x_center, 0.65),
        (x_center + w * 0.6, 0.62), (x_center + w, 0.58),
        (x_center + w, 0.19), (x_center - w, 0.19)
    ]
    codes = [Path.MOVETO] + [Path.LINETO] * 6 + [Path.CLOSEPOLY]
    path = Path(verts, codes)
    patch = PathPatch(path, facecolor=color, edgecolor='none',
                      alpha=alpha * 0.9, transform=ax.transAxes, zorder=2)
    ax.add_patch(patch)


def _draw_kashi_spire(ax):
    """Draw Kashi Vishwanath golden spire — right side."""
    alpha = SILHOUETTE_ALPHAS['kashi']
    
    # Main temple body
    body = Rectangle((0.72, 0.15), 0.10, 0.35,
                     facecolor=DEEP_SAFFRON, edgecolor='none',
                     alpha=alpha * 0.7, transform=ax.transAxes, zorder=2)
    ax.add_patch(body)
    
    # Shikhara (tower) — tapering upward
    spire_verts = [
        (0.73, 0.50), (0.74, 0.60), (0.755, 0.72),
        (0.77, 0.80), (0.77, 0.80),  # peak
        (0.785, 0.72), (0.80, 0.60), (0.81, 0.50),
        (0.73, 0.50)
    ]
    sp_codes = [Path.MOVETO] + [Path.LINETO] * 7 + [Path.CLOSEPOLY]
    path = Path(spire_verts, sp_codes)
    patch = PathPatch(path, facecolor=DEEP_SAFFRON, edgecolor='none',
                      alpha=alpha, transform=ax.transAxes, zorder=3)
    ax.add_patch(patch)
    
    # Trishul (trident) at top
    ax.plot([0.77, 0.77], [0.80, 0.88], color=DEEP_SAFFRON,
            linewidth=1.5, alpha=alpha + 0.05,
            transform=ax.transAxes, zorder=4)
    # Prongs
    ax.plot([0.76, 0.77], [0.85, 0.88], color=DEEP_SAFFRON,
            linewidth=0.8, alpha=alpha + 0.03,
            transform=ax.transAxes, zorder=4)
    ax.plot([0.78, 0.77], [0.85, 0.88], color=DEEP_SAFFRON,
            linewidth=0.8, alpha=alpha + 0.03,
            transform=ax.transAxes, zorder=4)
    
    # Smaller side shrine
    shrine_verts = [
        (0.85, 0.15), (0.85, 0.35), (0.86, 0.45),
        (0.865, 0.50), (0.87, 0.45), (0.88, 0.35),
        (0.88, 0.15), (0.85, 0.15)
    ]
    sh_codes = [Path.MOVETO] + [Path.LINETO] * 6 + [Path.CLOSEPOLY]
    sh_path = Path(shrine_verts, sh_codes)
    sh_patch = PathPatch(sh_path, facecolor=DEEP_SAFFRON, edgecolor='none',
                         alpha=alpha * 0.7, transform=ax.transAxes, zorder=2)
    ax.add_patch(sh_patch)


def _draw_ganga_curve(ax):
    """Draw Ganga river as a subtle flowing curve across the middle."""
    alpha = SILHOUETTE_ALPHAS['ganga']
    
    x = np.linspace(0, 1, 300)
    # Gentle S-curve
    y = 0.52 + 0.06 * np.sin(1.8 * np.pi * x) + 0.02 * np.sin(3.5 * np.pi * x)
    
    # River body — fill between
    ax.fill_between(x, y - 0.015, y + 0.015, color=GANGA_BLUE,
                    alpha=alpha, transform=ax.transAxes, zorder=1)
    
    # Highlight line
    ax.plot(x, y + 0.005, color=WHITE, linewidth=0.4, alpha=alpha * 0.5,
            transform=ax.transAxes, zorder=1)


def _draw_banarasi_border(ax):
    """Draw Banarasi sari border pattern at the bottom."""
    alpha = SILHOUETTE_ALPHAS['border']
    
    # Base strip
    border_bg = Rectangle((0, 0), 1, 0.10,
                          facecolor=VARANASI_MAROON, edgecolor='none',
                          alpha=alpha * 0.4, transform=ax.transAxes, zorder=1)
    ax.add_patch(border_bg)
    
    # Gold border lines
    ax.plot([0, 1], [0.10, 0.10], color=GOLD, linewidth=1.0,
            alpha=alpha, transform=ax.transAxes, zorder=2)
    ax.plot([0, 1], [0.003, 0.003], color=GOLD, linewidth=0.5,
            alpha=alpha * 0.6, transform=ax.transAxes, zorder=2)
    
    # Repeating butta (diamond + dot) motifs
    n_motifs = 20
    for i in range(n_motifs):
        cx = (i + 0.5) / n_motifs
        cy = 0.05
        
        diamond_verts = [
            (cx, cy + 0.025), (cx + 0.012, cy),
            (cx, cy - 0.025), (cx - 0.012, cy),
            (cx, cy + 0.025)
        ]
        d_codes = [Path.MOVETO, Path.LINETO, Path.LINETO,
                   Path.LINETO, Path.CLOSEPOLY]
        d_path = Path(diamond_verts, d_codes)
        d_patch = PathPatch(d_path, facecolor=GOLD, edgecolor='none',
                           alpha=alpha * 0.7, transform=ax.transAxes, zorder=3)
        ax.add_patch(d_patch)
