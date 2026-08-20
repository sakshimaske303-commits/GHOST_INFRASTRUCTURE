"""LISA (Local Moran's I) on 15-min accessibility across Bochum's street network.
KNN(k=8) row-standardized weights, binary within_15min, 99 permutations, p<0.05.
Fills the spatial-clustering test the original t-test/logit pipeline didn't cover. Needs libpysal, esda.
"""

import os
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from libpysal.weights import KNN
from esda.moran import Moran_Local

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

NODES_PATH = os.path.join(BASE_DIR, "data", "accessibility", "bochum_accessibility_with_distance.gpkg")
MINES_PATH = os.path.join(BASE_DIR, "data", "historical_georeferenced", "bochum_coal_mines.gpkg")
COLONIES_PATH = os.path.join(BASE_DIR, "data", "historical_georeferenced", "bochum_zechensiedlungen.gpkg")
OUT_PATH = os.path.join(BASE_DIR, "outputs", "plots", "lisa_cluster_map.png")

BACKGROUND = "#0F3C65"
ACCENT = "#FFF2BA"

K_NEIGHBORS = 8
PERMUTATIONS = 99
SEED = 42
SIG_LEVEL = 0.05


def main():
    nodes = gpd.read_file(NODES_PATH, layer="nodes") if False else gpd.read_file(NODES_PATH)
    mines = gpd.read_file(MINES_PATH).to_crs(nodes.crs)
    colonies = gpd.read_file(COLONIES_PATH).to_crs(nodes.crs)

    coords = np.column_stack([nodes.geometry.x.values, nodes.geometry.y.values])
    y = nodes["within_15min"].astype(int).values

    w = KNN.from_array(coords, k=K_NEIGHBORS)
    w.transform = "r"

    lisa = Moran_Local(y, w, permutations=PERMUTATIONS, seed=SEED)

    sig = lisa.p_sim < SIG_LEVEL
    quadrant = lisa.q  # 1=HH, 2=LH, 3=LL, 4=HL

    print(f"Mean local I: {lisa.Is.mean():.3f}")
    print(f"Significant nodes (p<{SIG_LEVEL}): {sig.sum()} / {len(y)} ({100*sig.sum()/len(y):.1f}%)")
    print(f"  LL (cold-spot) significant: {((quadrant == 3) & sig).sum()}")
    print(f"  HH (hot-spot) significant:  {((quadrant == 1) & sig).sum()}")
    print(f"  HL significant: {((quadrant == 4) & sig).sum()}")
    print(f"  LH significant: {((quadrant == 2) & sig).sum()}")

    np.save(os.path.join(BASE_DIR, "lisa_q.npy"), quadrant)
    np.save(os.path.join(BASE_DIR, "lisa_sig.npy"), sig)

    # --- Plot ---
    fig, ax = plt.subplots(figsize=(11, 11), facecolor=BACKGROUND)
    ax.set_facecolor(BACKGROUND)

    ll_sig = (quadrant == 3) & sig
    hh_sig = (quadrant == 1) & sig
    hl_sig = (quadrant == 4) & sig
    lh_sig = (quadrant == 2) & sig
    not_sig = ~sig

    ax.scatter(coords[not_sig, 0], coords[not_sig, 1], s=2, color="#3A5A78", alpha=0.35, label="Not significant", zorder=1)
    ax.scatter(coords[ll_sig, 0], coords[ll_sig, 1], s=4, color="#4A90D9", alpha=0.85, label="Low-Low (cold-spot)", zorder=2)
    ax.scatter(coords[hh_sig, 0], coords[hh_sig, 1], s=4, color="#E85D5D", alpha=0.85, label="High-High (hot-spot)", zorder=2)
    ax.scatter(coords[hl_sig, 0], coords[hl_sig, 1], s=6, color=ACCENT, alpha=0.9, label="High-Low (outlier)", zorder=3)
    ax.scatter(coords[lh_sig, 0], coords[lh_sig, 1], s=6, color="#9B6BD9", alpha=0.9, label="Low-High (outlier)", zorder=3)

    mines_c = mines.geometry
    colonies_c = colonies.geometry
    ax.scatter(mines_c.x, mines_c.y, marker="^", s=140, color="white", edgecolor="black", linewidth=1.2, zorder=5, label="Coal mine (1829-1974)")
    ax.scatter(colonies_c.x, colonies_c.y, marker="D", s=110, color=ACCENT, edgecolor="black", linewidth=1.2, zorder=5, label="Worker colony (1870-1915)")

    ax.set_title(
        "Local Moran's I: Spatial Clusters of 15-Minute Accessibility, Bochum\n"
        f"KNN(k={K_NEIGHBORS}), {PERMUTATIONS} permutations, p<{SIG_LEVEL}",
        color="white", fontsize=14, pad=14,
    )
    ax.set_axis_off()

    legend = ax.legend(loc="lower left", fontsize=9, framealpha=0.9, facecolor="#0A2C4D", edgecolor=ACCENT, labelcolor="white")

    fig.text(0.5, 0.02, "Sakshi D. Maske — Independent Geospatial Researcher", color="#9FB3C8", fontsize=9, ha="center")

    plt.tight_layout()
    plt.savefig(OUT_PATH, dpi=200, facecolor=BACKGROUND, bbox_inches="tight")
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()
