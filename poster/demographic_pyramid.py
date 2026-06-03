"""
UP 2050 — Demographic Pyramid Renderer
Classic mirrored horizontal bar chart showing population distribution by age group.
Male bars extend left (GANGA_BLUE), Female bars extend right (DEEP_SAFFRON).
Uses 2050 projection data.
"""

import numpy as np
from matplotlib.patches import Rectangle, FancyBboxPatch
from utils.palette import (
    CHARCOAL_NIGHT, GANGA_BLUE, DEEP_SAFFRON, GOLD,
    WHITE, PALE_MIST, GRID_LINE,
    FONT_BODY, SIZE_CAPTION, SIZE_DATA_LABEL,
    WEIGHT_MEDIUM, WEIGHT_REGULAR
)


def render(ax, demographics_data, export_mode=True):
    """Render population pyramid into the given Axes.
    
    Args:
        ax: Matplotlib Axes for this zone.
        demographics_data: Dict from demographics.json with 'age_groups'.
        export_mode: If True, render static final state.
    """
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_facecolor(CHARCOAL_NIGHT)
    
    age_groups = demographics_data['age_groups']
    n_groups = len(age_groups)
    
    # Layout constants
    center_x = 0.50
    max_bar_width = 0.35
    total_height = 0.78
    bar_height = total_height / n_groups
    y_start = 0.10
    gap = 0.003
    
    # Find max value for normalization
    max_val = max(
        max(g['male_2050'] for g in age_groups),
        max(g['female_2050'] for g in age_groups)
    )
    
    # Section title
    ax.text(0.5, 0.96, 'POPULATION STRUCTURE 2050',
            fontsize=SIZE_CAPTION, fontweight='bold',
            fontfamily=FONT_BODY, color=PALE_MIST,
            ha='center', va='top', transform=ax.transAxes,
            alpha=0.5, zorder=5)
    
    # Legend
    ax.plot(0.08, 0.93, marker='s', color=GANGA_BLUE, markersize=5,
            alpha=0.8, transform=ax.transAxes, zorder=5)
    ax.text(0.11, 0.93, 'Male', fontsize=SIZE_CAPTION - 2,
            fontfamily=FONT_BODY, color=GANGA_BLUE,
            ha='left', va='center', transform=ax.transAxes, zorder=5)
    ax.plot(0.85, 0.93, marker='s', color=DEEP_SAFFRON, markersize=5,
            alpha=0.8, transform=ax.transAxes, zorder=5)
    ax.text(0.88, 0.93, 'Female', fontsize=SIZE_CAPTION - 2,
            fontfamily=FONT_BODY, color=DEEP_SAFFRON,
            ha='left', va='center', transform=ax.transAxes, zorder=5)
    
    # Draw bars for each age group
    for i, group in enumerate(age_groups):
        y = y_start + i * bar_height
        bh = bar_height - gap
        
        male_val = group['male_2050']
        female_val = group['female_2050']
        
        # Normalize to max bar width
        male_width = (male_val / max_val) * max_bar_width
        female_width = (female_val / max_val) * max_bar_width
        
        # Male bar — extends LEFT from center
        male_rect = FancyBboxPatch(
            (center_x - male_width, y), male_width, bh,
            boxstyle="round,pad=0.001",
            facecolor=GANGA_BLUE, edgecolor='none',
            alpha=0.65, transform=ax.transAxes, zorder=2
        )
        ax.add_patch(male_rect)
        
        # Female bar — extends RIGHT from center
        female_rect = FancyBboxPatch(
            (center_x + 0.005, y), female_width, bh,
            boxstyle="round,pad=0.001",
            facecolor=DEEP_SAFFRON, edgecolor='none',
            alpha=0.65, transform=ax.transAxes, zorder=2
        )
        ax.add_patch(female_rect)
        
        # Age group label at center (only show every other to reduce clutter)
        if i % 2 == 0:
            ax.text(center_x, y + bh / 2, group['group'],
                    fontsize=SIZE_CAPTION - 3, fontweight=WEIGHT_MEDIUM,
                    fontfamily=FONT_BODY, color=WHITE,
                    ha='center', va='center', transform=ax.transAxes,
                    alpha=0.7, zorder=3,
                    bbox=dict(boxstyle='round,pad=0.1', facecolor=CHARCOAL_NIGHT,
                              edgecolor='none', alpha=0.7))
    
    # Center axis line
    ax.plot([center_x, center_x], [y_start - 0.01, y_start + n_groups * bar_height],
            color=WHITE, linewidth=0.5, alpha=0.25,
            transform=ax.transAxes, zorder=1)
