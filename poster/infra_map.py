"""
UP 2050 — Infrastructure Map Renderer
Renders expressway network and airport/city dots from GeoJSON data.
Uses Matplotlib paths (not GeoPandas) for lightweight rendering.
No text labels on the map — purely visual.
"""

import numpy as np
from matplotlib.patches import FancyArrowPatch, Circle
from matplotlib.collections import LineCollection
from utils.palette import (
    CHARCOAL_NIGHT, GANGA_BLUE, DEEP_SAFFRON, GOLD, WHITE,
    PALE_MIST, GRID_LINE, GLOW_CYAN, DARK_BLUE,
    FONT_BODY, SIZE_CAPTION, WEIGHT_REGULAR
)


def render(ax, geojson_data, export_mode=True):
    """Render infrastructure map into the given Axes.
    
    Args:
        ax: Matplotlib Axes for this zone.
        geojson_data: Parsed GeoJSON dict (FeatureCollection).
        export_mode: If True, render static final state.
    """
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_facecolor(CHARCOAL_NIGHT)
    
    # Extract features by type
    expressways = []
    airports = []
    cities = []
    
    for feature in geojson_data['features']:
        ftype = feature['properties'].get('type', '')
        if ftype == 'expressway':
            expressways.append(feature)
        elif ftype == 'airport':
            airports.append(feature)
        elif ftype == 'city':
            cities.append(feature)
    
    # Calculate bounding box for coordinate normalization
    all_coords = []
    for f in geojson_data['features']:
        geom = f['geometry']
        if geom['type'] == 'LineString':
            all_coords.extend(geom['coordinates'])
        elif geom['type'] == 'Point':
            all_coords.append(geom['coordinates'])
    
    if not all_coords:
        return
    
    lons = [c[0] for c in all_coords]
    lats = [c[1] for c in all_coords]
    
    # Add padding
    lon_min, lon_max = min(lons) - 0.5, max(lons) + 0.5
    lat_min, lat_max = min(lats) - 0.5, max(lats) + 0.5
    
    def norm_x(lon):
        return 0.05 + 0.9 * (lon - lon_min) / (lon_max - lon_min)
    
    def norm_y(lat):
        return 0.05 + 0.85 * (lat - lat_min) / (lat_max - lat_min)
    
    # Draw subtle grid
    for i in range(5):
        y_grid = 0.05 + i * 0.2125
        ax.plot([0.05, 0.95], [y_grid, y_grid], color=GRID_LINE,
                linewidth=0.3, alpha=0.3, transform=ax.transAxes, zorder=0)
        x_grid = 0.05 + i * 0.225
        ax.plot([x_grid, x_grid], [0.05, 0.90], color=GRID_LINE,
                linewidth=0.3, alpha=0.3, transform=ax.transAxes, zorder=0)
    
    # Draw expressways as glowing lines
    expressway_colors = [GANGA_BLUE, GLOW_CYAN, '#2196F3', '#4DD0E1']
    for idx, eway in enumerate(expressways):
        coords = eway['geometry']['coordinates']
        xs = [norm_x(c[0]) for c in coords]
        ys = [norm_y(c[1]) for c in coords]
        
        color = expressway_colors[idx % len(expressway_colors)]
        
        # Glow effect — wider, more transparent line behind
        ax.plot(xs, ys, color=color, linewidth=4.0, alpha=0.15,
                transform=ax.transAxes, zorder=1, solid_capstyle='round')
        # Main line
        ax.plot(xs, ys, color=color, linewidth=1.8, alpha=0.8,
                transform=ax.transAxes, zorder=2, solid_capstyle='round')
    
    # Draw airports as pulsing markers
    for airport in airports:
        lon, lat = airport['geometry']['coordinates']
        x, y = norm_x(lon), norm_y(lat)
        
        # Outer glow
        ax.plot(x, y, marker='o', color=DEEP_SAFFRON, markersize=12,
                alpha=0.2, transform=ax.transAxes, zorder=3)
        # Inner dot
        ax.plot(x, y, marker='^', color=DEEP_SAFFRON, markersize=7,
                alpha=0.9, transform=ax.transAxes, zorder=4,
                markeredgecolor=WHITE, markeredgewidth=0.5)
    
    # Draw cities as gold dots
    for city in cities:
        lon, lat = city['geometry']['coordinates']
        x, y = norm_x(lon), norm_y(lat)
        pop = city['properties'].get('population_2050_millions', 5)
        
        # Size proportional to population
        size = 4 + (pop / 20) * 8
        
        # Outer glow
        ax.plot(x, y, marker='o', color=GOLD, markersize=size + 4,
                alpha=0.15, transform=ax.transAxes, zorder=3)
        # City dot
        ax.plot(x, y, marker='o', color=GOLD, markersize=size,
                alpha=0.8, transform=ax.transAxes, zorder=4,
                markeredgecolor=WHITE, markeredgewidth=0.3)
    
    # Section label (top-left)
    ax.text(0.05, 0.94, 'INFRASTRUCTURE CORRIDOR 2050',
            fontsize=SIZE_CAPTION, fontweight='bold',
            fontfamily=FONT_BODY, color=PALE_MIST,
            ha='left', va='top', transform=ax.transAxes,
            alpha=0.5, zorder=5)
