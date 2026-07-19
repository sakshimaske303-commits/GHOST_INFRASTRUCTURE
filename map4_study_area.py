import geopandas as gpd
import matplotlib.pyplot as plt

BACKGROUND = "#2E3A61"
LAND_COLOR = "#F5EFD8"
TEXT_COLOR = "#FFFFFF"

boundary = gpd.read_file("data/boundaries/bochum_city.gpkg")
boundary = boundary.to_crs("EPSG:4326")

fig, ax = plt.subplots(figsize=(12, 10))
fig.patch.set_facecolor(BACKGROUND)
ax.set_facecolor(BACKGROUND)

boundary.plot(ax=ax, facecolor=LAND_COLOR, edgecolor="#7FB8BE", linewidth=2, alpha=0.9, zorder=1)

bounds = boundary.total_bounds
x_pad = (bounds[2] - bounds[0]) * 0.1
y_pad = (bounds[3] - bounds[1]) * 0.1
ax.set_xlim(bounds[0] - x_pad, bounds[2] + x_pad)
ax.set_ylim(bounds[1] - y_pad, bounds[3] + y_pad)
ax.set_axis_off()

fig.text(0.5, 0.94, "STUDY AREA: BOCHUM", fontsize=22, fontweight="bold", color=TEXT_COLOR, ha="center")
fig.text(0.5, 0.905, "North Rhine-Westphalia, Germany — Ruhr Valley",
          fontsize=12, color="#B0BEC5", ha="center")

plt.figtext(0.5, 0.03, "GHOST INFRASTRUCTURE — Boundary: GADM v4.1",
            ha="center", fontsize=9, color="#7FB8BE")

plt.tight_layout(rect=[0, 0.03, 1, 0.9])
plt.savefig("outputs/plots/study_area_bochum.png", dpi=220, facecolor=BACKGROUND, bbox_inches="tight")
plt.close()
print("Saved: outputs/plots/study_area_bochum.png")