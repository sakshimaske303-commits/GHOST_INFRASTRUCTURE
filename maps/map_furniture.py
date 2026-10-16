"""Scale bar and north arrow for maps plotted in geographic coordinates (EPSG:4326, degrees).

Call after the data are plotted and the axis limits are final:
    add_scale_bar(ax, km=2)
    add_north_arrow(ax)
"""
import math

import matplotlib.patheffects as pe

HALO = [pe.withStroke(linewidth=4, foreground="#1a1a19")]


def add_scale_bar(ax, km=2, color="white", loc=(0.70, 0.06), fontsize=10):
    """Draws a km scale bar. Converts km to degrees of longitude at the map's centre latitude."""
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    lat = (y0 + y1) / 2
    dlon = km * 1000 / (111320 * math.cos(math.radians(lat)))
    xs = x0 + loc[0] * (x1 - x0)
    ys = y0 + loc[1] * (y1 - y0)
    ax.plot([xs, xs + dlon], [ys, ys], color=color, linewidth=3, solid_capstyle="butt", zorder=10, path_effects=HALO)
    for xt in (xs, xs + dlon):
        ax.plot([xt, xt], [ys - 0.004 * (y1 - y0), ys + 0.004 * (y1 - y0)], color=color, linewidth=1.5, zorder=10, path_effects=HALO)
    ax.text(xs + dlon / 2, ys + 0.012 * (y1 - y0), f"{km} km", color=color, ha="center", va="bottom",
            fontsize=fontsize, zorder=10, path_effects=HALO)


def add_north_arrow(ax, color="white", loc=(0.94, 0.90), fontsize=12):
    """Draws a simple north arrow (maps here are not rotated, so north is up)."""
    ax.annotate("", xy=(loc[0], loc[1]), xytext=(loc[0], loc[1] - 0.07), xycoords="axes fraction",
                arrowprops=dict(arrowstyle="-|>", color=color, lw=2, path_effects=HALO), zorder=10)
    ax.text(loc[0], loc[1] + 0.015, "N", transform=ax.transAxes, ha="center", va="bottom",
            fontsize=fontsize, fontweight="bold", color=color, zorder=10, path_effects=HALO)
