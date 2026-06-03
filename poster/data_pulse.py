"""
UP 2050 — Data Pulse Renderer
Renders 4 metric cards: GDP, Population, Renewable Energy, Literacy Rate.
Each card has a glass-effect background, large value, label, and delta arrow.
"""

import numpy as np
from matplotlib.patches import FancyBboxPatch
from matplotlib.gridspec import GridSpecFromSubplotSpec
from utils.palette import (
    CHARCOAL_NIGHT, GANGA_BLUE, DEEP_SAFFRON, GOLD, MINT_GREEN,
    WHITE, PALE_MIST, GRID_LINE, GLASS_ALPHA,
    FONT_DISPLAY, FONT_BODY,
    SIZE_DATA_VALUE, SIZE_DATA_LABEL, SIZE_BODY, SIZE_CAPTION,
    WEIGHT_BOLD, WEIGHT_MEDIUM, WEIGHT_REGULAR
)


def render(ax, metrics, export_mode=True):
    """Render 4 metric cards into the given Axes.
    
    Args:
        ax: Matplotlib Axes for this zone.
        metrics: List of metric dicts from projections.json.
        export_mode: If True, render static final state.
    """
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_facecolor(CHARCOAL_NIGHT)
    
    # Card layout: 4 cards evenly spaced
    n_cards = min(len(metrics), 4)
    card_width = 0.20
    gap = (1.0 - n_cards * card_width) / (n_cards + 1)
    
    for i, metric in enumerate(metrics[:4]):
        x = gap + i * (card_width + gap)
        y = 0.08
        h = 0.84
        
        _render_card(ax, metric, x, y, card_width, h, i)


def _render_card(ax, metric, x, y, w, h, index):
    """Render a single metric card.
    
    Args:
        ax: Parent Axes.
        metric: Dict with label, baseline_value, projected_value, unit, prefix, delta_direction.
        x, y: Bottom-left position in axes coordinates.
        w, h: Width and height in axes coordinates.
        index: Card index (0-3) for color variation.
    """
    # Glass-effect background card
    card_colors = [GANGA_BLUE, DEEP_SAFFRON, MINT_GREEN, GOLD]
    accent_color = card_colors[index % len(card_colors)]
    
    card_bg = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02",
        facecolor=accent_color,
        edgecolor=accent_color,
        alpha=GLASS_ALPHA,
        linewidth=0.5,
        transform=ax.transAxes,
        zorder=1
    )
    ax.add_patch(card_bg)
    
    # Top accent line
    ax.plot([x + 0.02, x + w - 0.02], [y + h - 0.02, y + h - 0.02],
            color=accent_color, linewidth=2.0, alpha=0.6,
            transform=ax.transAxes, zorder=2)
    
    # Format value
    projected = metric['projected_value']
    prefix = metric.get('prefix', '')
    unit = metric.get('unit', '')
    
    if isinstance(projected, float) and projected < 10:
        value_text = f"{prefix}{projected:.1f}{unit}"
    else:
        value_text = f"{prefix}{int(projected)}{unit}"
    
    # Large projected value
    ax.text(x + w / 2, y + h * 0.65, value_text,
            fontsize=SIZE_DATA_VALUE, fontweight=WEIGHT_BOLD,
            fontfamily=FONT_DISPLAY, color=WHITE,
            ha='center', va='center', transform=ax.transAxes,
            zorder=3)
    
    # Delta arrow and percentage change
    baseline = metric['baseline_value']
    if baseline > 0:
        delta_pct = ((projected - baseline) / baseline) * 100
    else:
        delta_pct = 0
    
    direction = metric.get('delta_direction', 'up')
    arrow = '▲' if direction == 'up' else '▼'
    arrow_color = MINT_GREEN if direction == 'up' else '#FF4444'
    
    delta_text = f"{arrow} {delta_pct:.0f}%"
    ax.text(x + w / 2, y + h * 0.42, delta_text,
            fontsize=SIZE_BODY, fontweight=WEIGHT_MEDIUM,
            fontfamily=FONT_BODY, color=arrow_color,
            ha='center', va='center', transform=ax.transAxes,
            zorder=3)
    
    # Baseline reference
    if isinstance(baseline, float) and baseline < 10:
        baseline_text = f"from {prefix}{baseline:.2f}{unit}"
    else:
        baseline_text = f"from {prefix}{int(baseline)}{unit}"
    
    ax.text(x + w / 2, y + h * 0.30, baseline_text,
            fontsize=SIZE_CAPTION, fontweight=WEIGHT_REGULAR,
            fontfamily=FONT_BODY, color=PALE_MIST,
            ha='center', va='center', transform=ax.transAxes,
            alpha=0.6, zorder=3)
    
    # Label at bottom
    label = metric['label']
    ax.text(x + w / 2, y + h * 0.12, label,
            fontsize=SIZE_DATA_LABEL - 2, fontweight=WEIGHT_MEDIUM,
            fontfamily=FONT_BODY, color=GOLD,
            ha='center', va='center', transform=ax.transAxes,
            zorder=3)
