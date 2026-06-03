"""
UP 2050 — Poster Canvas Compositor
Root compositor: creates the 1080x1080 Matplotlib Figure with 6-zone GridSpec,
calls all section renderers, and returns the assembled figure.
"""

from matplotlib.figure import Figure
from matplotlib.gridspec import GridSpec

from utils.palette import (
    CHARCOAL_NIGHT, POSTER_WIDTH, POSTER_HEIGHT, POSTER_DPI, ZONE_RATIOS
)
from utils.data_transform import load_projections, load_demographics, load_infrastructure

from poster.hero_section import render as render_hero
from poster.skyline import render as render_skyline
from poster.data_pulse import render as render_data_pulse
from poster.infra_map import render as render_infra_map
from poster.cultural_layer import render as render_cultural
from poster.demographic_pyramid import render as render_pyramid


def create_poster(export_mode=True):
    """Create the full UP 2050 poster.
    
    Args:
        export_mode: If True, render all components in static final-state mode.
    
    Returns:
        matplotlib.figure.Figure: The assembled poster figure.
    """
    # Create canvas
    fig = Figure(figsize=(POSTER_WIDTH, POSTER_HEIGHT), dpi=POSTER_DPI)
    fig.patch.set_facecolor(CHARCOAL_NIGHT)
    
    # 6-zone GridSpec layout — tuned ratios for visual balance
    # Override palette defaults for better pyramid visibility
    tuned_ratios = [0.175, 0.155, 0.145, 0.200, 0.145, 0.180]
    gs = GridSpec(
        6, 1, figure=fig,
        height_ratios=tuned_ratios,
        hspace=0.02
    )
    
    # Load all data
    projections = load_projections()
    demographics = load_demographics()
    infrastructure = load_infrastructure()
    
    # === Zone 1: Hero Band ===
    ax_hero = fig.add_subplot(gs[0])
    render_hero(
        ax_hero,
        year='2050',
        tagline='The Future Is Ancient',
        subtext='240 Million Dreams · 1 River · Infinite Potential',
        export_mode=export_mode
    )
    
    # === Zone 2: Skyline Strip ===
    ax_skyline = fig.add_subplot(gs[1])
    render_skyline(ax_skyline, export_mode=export_mode)
    
    # === Zone 3: Data Row (4 Metric Cards) ===
    ax_data = fig.add_subplot(gs[2])
    render_data_pulse(ax_data, projections['metrics'], export_mode=export_mode)
    
    # === Zone 4: Infrastructure Map ===
    ax_map = fig.add_subplot(gs[3])
    render_infra_map(ax_map, infrastructure, export_mode=export_mode)
    
    # === Zone 5: Cultural Footer ===
    ax_culture = fig.add_subplot(gs[4])
    render_cultural(ax_culture, export_mode=export_mode)
    
    # === Zone 6: Demographic Pyramid / Caption Bar ===
    ax_pyramid = fig.add_subplot(gs[5])
    render_pyramid(ax_pyramid, demographics, export_mode=export_mode)
    
    return fig
