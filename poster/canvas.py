"""
UP 2050 — Poster Canvas Compositor
Root compositor: creates the 1080x1080 Matplotlib Figure with 6-zone GridSpec,
calls all section renderers, and returns the assembled figure.
"""

from matplotlib.figure import Figure
from matplotlib.gridspec import GridSpec

from utils.palette import (
    CHARCOAL_NIGHT, POSTER_WIDTH, POSTER_HEIGHT, POSTER_DPI
)
from utils.data_transform import load_projections, load_demographics, load_infrastructure

from poster.hero_section import render as render_hero
from poster.skyline import render as render_skyline
from poster.data_pulse import render as render_data_pulse
from poster.infra_map import render as render_infra_map
from poster.cultural_layer import render as render_cultural
from poster.demographic_pyramid import render as render_pyramid


def create_poster(export_mode=True):
    """Create the full UP 2050 poster."""
    fig = Figure(figsize=(POSTER_WIDTH, POSTER_HEIGHT), dpi=POSTER_DPI)
    fig.patch.set_facecolor(CHARCOAL_NIGHT)

    # Increased spacing between zones to prevent overlap
    tuned_ratios = [0.16, 0.14, 0.16, 0.20, 0.14, 0.20]
    gs = GridSpec(
        6, 1, figure=fig,
        height_ratios=tuned_ratios,
        hspace=0.08,          # was 0.02 — this was causing overlap
        top=0.98,
        bottom=0.02,
        left=0.02,
        right=0.98,
    )

    projections   = load_projections()
    demographics  = load_demographics()
    infrastructure = load_infrastructure()

    ax_hero = fig.add_subplot(gs[0])
    render_hero(
        ax_hero,
        year='2050',
        tagline='The Future Is Ancient',
        subtext='240 Million Dreams · 1 River · Infinite Potential',
        export_mode=export_mode
    )

    ax_skyline = fig.add_subplot(gs[1])
    render_skyline(ax_skyline, export_mode=export_mode)

    ax_data = fig.add_subplot(gs[2])
    render_data_pulse(ax_data, projections['metrics'], export_mode=export_mode)

    ax_map = fig.add_subplot(gs[3])
    render_infra_map(ax_map, infrastructure, export_mode=export_mode)

    ax_culture = fig.add_subplot(gs[4])
    render_cultural(ax_culture, export_mode=export_mode)

    ax_pyramid = fig.add_subplot(gs[5])
    render_pyramid(ax_pyramid, demographics, export_mode=export_mode)

    return fig