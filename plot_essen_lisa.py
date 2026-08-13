import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

BACKGROUND = "#0F3C65"
ACCENT = "#FFF2BA"

nodes = gpd.read_file("data/accessibility/essen_accessibility_with_distance.gpkg")
mines = gpd.read_file("data/historical_georeferenced/essen_coal_mines.gpkg").to_crs(nodes.crs)
colonies = gpd.read_file("data/historical_georeferenced/essen_zechensiedlungen.gpkg").to_crs(nodes.crs)

quadrant = np.load("essen_lisa_q.npy")
sig = np.load("essen_lisa_sig.npy")

coords = np.column_stack([nodes.geometry.x.values, nodes.geometry.y.values])

ll_sig = (quadrant == 3) & sig
hh_sig = (quadrant == 1) & sig
hl_sig = (quadrant == 4) & sig
lh_sig = (quadrant == 2) & sig
not_sig = ~sig

fig, ax = plt.subplots(figsize=(11, 11), facecolor=BACKGROUND)
ax.set_facecolor(BACKGROUND)

ax.scatter(coords[not_sig, 0], coords[not_sig, 1], s=2, color="#3A5A78", alpha=0.35, label="Not significant", zorder=1)
ax.scatter(coords[ll_sig, 0], coords[ll_sig, 1], s=4, color="#4A90D9", alpha=0.85, label="Low-Low (cold-spot)", zorder=2)
ax.scatter(coords[hh_sig, 0], coords[hh_sig, 1], s=4, color="#E85D5D", alpha=0.85, label="High-High (hot-spot)", zorder=2)
ax.scatter(coords[hl_sig, 0], coords[hl_sig, 1], s=6, color=ACCENT, alpha=0.9, label="High-Low (outlier)", zorder=3)
ax.scatter(coords[lh_sig, 0], coords[lh_sig, 1], s=6, color="#9B6BD9", alpha=0.9, label="Low-High (outlier)", zorder=3)

ax.scatter(mines.geometry.x, mines.geometry.y, marker="^", s=140, color="white", edgecolor="black", linewidth=1.2, zorder=5, label="Coal mine")
ax.scatter(colonies.geometry.x, colonies.geometry.y, marker="D", s=110, color=ACCENT, edgecolor="black", linewidth=1.2, zorder=5, label="Worker colony")

ax.set_title(
    "Local Moran's I: Spatial Clusters of 15-Minute Accessibility, Essen\n"
    "KNN(k=8), 99 permutations, p<0.05 — Multi-City Comparison Case",
    color="white", fontsize=14, pad=14,
)
ax.set_axis_off()
legend = ax.legend(loc="lower left", fontsize=9, framealpha=0.9, facecolor="#0A2C4D", edgecolor=ACCENT, labelcolor="white")
fig.text(0.5, 0.02, "Sakshi D. Maske — Independent Geospatial Researcher", color="#9FB3C8", fontsize=9, ha="center")
plt.tight_layout()
plt.savefig("essen_lisa_cluster_map.png", dpi=200, facecolor=BACKGROUND, bbox_inches="tight")
print("Saved: essen_lisa_cluster_map.png")
