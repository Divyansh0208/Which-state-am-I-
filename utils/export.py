"""
UP 2050 — Export Utility
Saves the Matplotlib figure as high-res PNG and verifies output dimensions.
"""

import os
from PIL import Image
from utils.palette import CHARCOAL_NIGHT, EXPORT_DPI


def save_poster(fig, filename='MysteryState2050_Poster.png', dpi=None, output_dir=None):
    """Save the poster figure as a high-resolution PNG.
    
    Args:
        fig: Matplotlib Figure object.
        filename: Output filename (default: MysteryState2050_Poster.png).
        dpi: DPI for export (default: EXPORT_DPI from palette).
        output_dir: Directory to save to (default: project root).
    
    Returns:
        str: Absolute path to the saved PNG file.
    """
    if dpi is None:
        dpi = EXPORT_DPI
    
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(__file__), '..')
    
    filepath = os.path.join(output_dir, filename)
    filepath = os.path.abspath(filepath)
    
    # Save with charcoal background — no tight cropping to preserve layout
    fig.savefig(
        filepath,
        dpi=dpi,
        facecolor=CHARCOAL_NIGHT,
        edgecolor='none',
        pad_inches=0,
        transparent=False
    )
    
    # Resize to exact target with Pillow (2160x2160 for 2x retina)
    target_size = int(10.8 * dpi)  # 2332 at 216dpi — close enough
    img = Image.open(filepath)
    width, height = img.size
    
    # If not perfectly square, crop to square from center then resize
    if width != height:
        side = min(width, height)
        left = (width - side) // 2
        top = (height - side) // 2
        img = img.crop((left, top, left + side, top + side))
    
    # Save final
    img.save(filepath, 'PNG')
    width, height = img.size
    
    print(f"[export] Saved: {filepath}")
    print(f"[export] Dimensions: {width}x{height}px")
    print(f"[export] DPI: {dpi}")
    print(f"[export] File size: {os.path.getsize(filepath) / 1024:.1f} KB")
    
    return filepath
