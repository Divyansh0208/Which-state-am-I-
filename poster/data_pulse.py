"""
UP 2050 — Data Pulse Renderer
"""

from matplotlib.patches import FancyBboxPatch
from utils.palette import (
    CHARCOAL_NIGHT, GANGA_BLUE, DEEP_SAFFRON, GOLD, MINT_GREEN,
    WHITE, PALE_MIST,
    FONT_DISPLAY, FONT_BODY,
    SIZE_DATA_VALUE, SIZE_DATA_LABEL, SIZE_BODY, SIZE_CAPTION,
    WEIGHT_BOLD, WEIGHT_MEDIUM, WEIGHT_REGULAR
)


def render(ax, metrics, export_mode=True):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_facecolor(CHARCOAL_NIGHT)

    n_cards = min(len(metrics), 4)
    card_width = 0.21
    gap = (1.0 - n_cards * card_width) / (n_cards + 1)

    for i, metric in enumerate(metrics[:4]):
        x = gap + i * (card_width + gap)
        _render_card(ax, metric, x, 0.05, card_width, 0.90, i)


def _render_card(ax, metric, x, y, w, h, index):
    card_colors = [GANGA_BLUE, DEEP_SAFFRON, MINT_GREEN, GOLD]
    accent = card_colors[index % len(card_colors)]

    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.015",
        facecolor=accent, edgecolor=accent,
        alpha=0.18, linewidth=0.8,
        transform=ax.transAxes, zorder=1
    ))

    ax.plot([x + 0.015, x + w - 0.015], [y + h - 0.01, y + h - 0.01],
            color=accent, linewidth=1.5, alpha=0.7,
            transform=ax.transAxes, zorder=2)

    projected = metric['projected_value']
    prefix    = metric.get('prefix', '')
    unit      = metric.get('unit', '')
    baseline  = metric['baseline_value']

    value_text = (f"{prefix}{projected:.1f}{unit}"
                  if isinstance(projected, float) and projected < 10
                  else f"{prefix}{int(projected)}{unit}")

    # Value — top third of card
    ax.text(x + w / 2, y + h * 0.72, value_text,
            fontsize=SIZE_DATA_VALUE, fontweight=WEIGHT_BOLD,
            fontfamily=FONT_DISPLAY, color=WHITE,
            ha='center', va='center', transform=ax.transAxes, zorder=3)

    # Delta — middle
    delta_pct   = ((projected - baseline) / baseline * 100) if baseline > 0 else 0
    direction   = metric.get('delta_direction', 'up')
    arrow       = '▲' if direction == 'up' else '▼'
    arrow_color = MINT_GREEN if direction == 'up' else '#FF4444'

    ax.text(x + w / 2, y + h * 0.50, f"{arrow} {delta_pct:.0f}%",
            fontsize=SIZE_BODY, fontweight=WEIGHT_MEDIUM,
            fontfamily=FONT_BODY, color=arrow_color,
            ha='center', va='center', transform=ax.transAxes, zorder=3)

    # Baseline — below delta
    baseline_text = (f"from {prefix}{baseline:.2f}{unit}"
                     if isinstance(baseline, float) and baseline < 10
                     else f"from {prefix}{int(baseline)}{unit}")

    ax.text(x + w / 2, y + h * 0.35, baseline_text,
            fontsize=SIZE_CAPTION, fontweight=WEIGHT_REGULAR,
            fontfamily=FONT_BODY, color=PALE_MIST,
            ha='center', va='center', transform=ax.transAxes,
            alpha=0.65, zorder=3)

    # Label — bottom
    ax.text(x + w / 2, y + h * 0.16, metric['label'],
            fontsize=SIZE_DATA_LABEL, fontweight=WEIGHT_MEDIUM,
            fontfamily=FONT_BODY, color=GOLD,
            ha='center', va='center', transform=ax.transAxes, zorder=3)