import geopandas as gpd
import matplotlib.pyplot as plt

BACKGROUND = "#0E1A1F"
HISTORICAL_COLOR = "#F57C00"
LOW_ACCESS_COLOR = "#C62828"
HIGH_ACCESS_COLOR = "#2E7D32"
TEXT_COLOR = "#F5F7FA"

nodes = gpd.read_file("data/accessibility/bochum_accessibility_with_distance.gpkg")
mines = gpd.read_file("data/historical_georeferenced/bochum_coal_mines.gpkg")
colonies = gpd.read_file("data/historical_georeferenced/bochum_zechensiedlungen.gpkg")

# Ensure all layers share the same CRS before plotting together
nodes = nodes.to_crs("EPSG:4326")
mines = mines.to_crs("EPSG:4326")
colonies = colonies.to_crs("EPSG:4326")

fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BACKGROUND)
ax.set_facecolor(BACKGROUND)

low_access = nodes[nodes["within_15min"] == False]
high_access = nodes[nodes["within_15min"] == True]

high_access.plot(ax=ax, color=HIGH_ACCESS_COLOR, markersize=0.5, alpha=0.15, zorder=1)
low_access.plot(ax=ax, color=LOW_ACCESS_COLOR, markersize=1.5, alpha=0.5, zorder=2)

mines.plot(ax=ax, color=HISTORICAL_COLOR, markersize=180, marker="^",
           edgecolor="white", linewidth=1.5, zorder=4)
colonies.plot(ax=ax, color="#FFD54F", markersize=180, marker="s",
              edgecolor="white", linewidth=1.5, zorder=4)

ax.set_axis_off()

handles = [
    plt.Line2D([0], [0], marker="^", color="w", markerfacecolor=HISTORICAL_COLOR, markersize=14, label="Historical Coal Mine (1829-1974)", linestyle="None"),
    plt.Line2D([0], [0], marker="s", color="w", markerfacecolor="#FFD54F", markersize=14, label="Worker Colony (1870-1915)", linestyle="None"),
    plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=LOW_ACCESS_COLOR, markersize=10, label="Low 15-Min Accessibility (14.2% of city)", linestyle="None"),
    plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=HIGH_ACCESS_COLOR, markersize=10, label="High 15-Min Accessibility", linestyle="None"),
]
legend = ax.legend(handles=handles, loc="lower left", fontsize=11, frameon=True,
                    facecolor="#141A22", edgecolor="#00ACC1", framealpha=0.9, labelcolor=TEXT_COLOR)

fig.text(0.5, 0.95, "GHOST INFRASTRUCTURE", fontsize=28, fontweight="bold", color=TEXT_COLOR, ha="center")
fig.text(0.5, 0.915, "Historical Industrial Geography vs. Present-Day 15-Minute Accessibility — Bochum, Germany",
          fontsize=13, color="#B0BEC5", ha="center")

plt.figtext(0.5, 0.02, "GHOST INFRASTRUCTURE — Sources: Mindat.org, OpenStreetMap (OSMnx), German heritage archives",
            ha="center", fontsize=9, color="#888888")

plt.tight_layout(rect=[0, 0.03, 1, 0.9])
plt.savefig("outputs/plots/ghost_infrastructure_overlay.png", dpi=220, facecolor=BACKGROUND, bbox_inches="tight")
plt.close()
print("Saved: outputs/plots/ghost_infrastructure_overlay.png")