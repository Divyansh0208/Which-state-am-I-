"""
UP 2050 — Demographic Pyramid Renderer
"""

from matplotlib.patches import FancyBboxPatch
from utils.palette import (
    CHARCOAL_NIGHT, GANGA_BLUE, DEEP_SAFFRON,
    WHITE, PALE_MIST,
    FONT_BODY, SIZE_CAPTION,
    WEIGHT_MEDIUM
)


def render(ax, demographics_data, export_mode=True):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_facecolor(CHARCOAL_NIGHT)

    age_groups   = demographics_data['age_groups']
    n_groups     = len(age_groups)

    label_x      = 0.12
    center_x     = 0.48
    max_bar_w    = 0.30
    total_height = 0.72
    bar_height   = total_height / n_groups
    y_start      = 0.07
    gap          = 0.002

    max_val = max(
        max(g['male_2050']   for g in age_groups),
        max(g['female_2050'] for g in age_groups)
    )

    # Title
    ax.text(0.5, 0.97, 'POPULATION STRUCTURE 2050',
            fontsize=SIZE_CAPTION, fontweight='bold',
            fontfamily=FONT_BODY, color=PALE_MIST,
            ha='center', va='top', transform=ax.transAxes,
            alpha=0.5, zorder=5)

    # Legend
    ax.plot(0.22, 0.91, marker='s', color=GANGA_BLUE, markersize=5,
            alpha=0.8, transform=ax.transAxes, zorder=5)
    ax.text(0.25, 0.91, 'Male', fontsize=SIZE_CAPTION - 2,
            fontfamily=FONT_BODY, color=GANGA_BLUE,
            ha='left', va='center', transform=ax.transAxes, zorder=5)
    ax.plot(0.72, 0.91, marker='s', color=DEEP_SAFFRON, markersize=5,
            alpha=0.8, transform=ax.transAxes, zorder=5)
    ax.text(0.75, 0.91, 'Female', fontsize=SIZE_CAPTION - 2,
            fontfamily=FONT_BODY, color=DEEP_SAFFRON,
            ha='left', va='center', transform=ax.transAxes, zorder=5)

    for i, group in enumerate(age_groups):
        y  = y_start + i * bar_height
        bh = bar_height - gap

        male_w   = (group['male_2050']   / max_val) * max_bar_w
        female_w = (group['female_2050'] / max_val) * max_bar_w

        # Male bar
        bar_left = center_x - male_w
        ax.add_patch(FancyBboxPatch(
            (bar_left, y), male_w, bh,
            boxstyle="round,pad=0.001",
            facecolor=GANGA_BLUE, edgecolor='none',
            alpha=0.65, transform=ax.transAxes, zorder=2
        ))

        # Female bar
        ax.add_patch(FancyBboxPatch(
            (center_x + 0.004, y), female_w, bh,
            boxstyle="round,pad=0.001",
            facecolor=DEEP_SAFFRON, edgecolor='none',
            alpha=0.65, transform=ax.transAxes, zorder=2
        ))

        # Label — every other group only to prevent overlap
        if i % 2 == 0:
            ax.text(label_x, y + bh / 2, group['group'],
                    fontsize=SIZE_CAPTION - 1, fontweight=WEIGHT_MEDIUM,
                    fontfamily=FONT_BODY, color=WHITE,
                    ha='center', va='center', transform=ax.transAxes,
                    alpha=0.80, zorder=3)

    # Center line
    ax.plot([center_x, center_x],
            [y_start - 0.01, y_start + n_groups * bar_height],
            color=WHITE, linewidth=0.5, alpha=0.25,
            transform=ax.transAxes, zorder=1)