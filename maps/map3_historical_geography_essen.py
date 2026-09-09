"""Essen equivalent of map3_historical_geography.py (Bochum). Written to close a
reproducibility gap: the original outputs/plots/essen_historical_geography.png had no
generating script in the repo. Modeled directly on map3_historical_geography.py, same
style/palette, Essen boundary + historical-site data (4 mines, 4 worker colonies).
"""
import geopandas as gpd
import matplotlib.pyplot as plt

BACKGROUND = "#2E3A61"
LAND_COLOR = "#F5EFD8"
MINE_COLOR = "#B65A2A"
COLONY_COLOR = "#7FB8BE"
TEXT_COLOR = "#000000"

boundary = gpd.read_file("data/boundaries/essen_city.gpkg")
mines = gpd.read_file("data/historical_georeferenced/essen_coal_mines.gpkg")
colonies = gpd.read_file("data/historical_georeferenced/essen_zechensiedlungen.gpkg")

boundary = boundary.to_crs("EPSG:4326")
mines = mines.to_crs("EPSG:4326")
colonies = colonies.to_crs("EPSG:4326")

fig, ax = plt.subplots(figsize=(14, 12))
fig.patch.set_facecolor(BACKGROUND)
ax.set_facecolor(BACKGROUND)

# Essen city boundary as visible base layer, giving the map genuine area context
boundary.plot(ax=ax, facecolor=LAND_COLOR, edgecolor="#7FB8BE", linewidth=1.5, alpha=0.85, zorder=1)

mines.plot(ax=ax, color=MINE_COLOR, markersize=250, marker="^",
           edgecolor="white", linewidth=1.5, zorder=3)
colonies.plot(ax=ax, color=COLONY_COLOR, markersize=250, marker="s",
              edgecolor="white", linewidth=1.5, zorder=3)

# Short display names for the mine labels (mirrors the Bochum script's ".replace(' Coal Mine', '')"
# pattern -- Essen's source names use "Zeche <name>" instead, so a small explicit lookup is used).
mine_short_names = {
    "Zeche Zollverein (Schacht XII)": "Zollverein",
    "Zeche Carl Funke": "Carl Funke",
    "Zeche Vereinigte Helene & Amalie": "Helene & Amalie",
    "Zeche Pörtingsiepen": "Poertingsiepen",
}

mine_offsets = {
    "Zeche Zollverein (Schacht XII)": (-70, -32),
    "Zeche Carl Funke": (-14, 13),
    "Zeche Vereinigte Helene & Amalie": (8, 8),
    "Zeche Pörtingsiepen": (-118, -6),
}

for idx, row in mines.iterrows():
    offset = mine_offsets.get(row["mine_name"], (7, 7))
    ax.annotate(mine_short_names.get(row["mine_name"], row["mine_name"]),
                (row.geometry.x, row.geometry.y),
                xytext=offset, textcoords="offset points",
                fontsize=14, color="#000000", fontweight="bold")

colony_offsets = {
    "Mathias-Stinnes-Siedlung": (10, 8),
    "Kolonie Zollverein III": (-205, -8),
    "Kolonie Beisen": (10, 18),
    "Siedlung Carl Funke": (10, -4),
}

for idx, row in colonies.iterrows():
    offset = colony_offsets.get(row["settlement_name"], (6, -10))
    ax.annotate(row["settlement_name"],
                (row.geometry.x, row.geometry.y),
                xytext=offset, textcoords="offset points",
                fontsize=14, color="#000000", fontweight="bold")

bounds = boundary.total_bounds
x_pad = (bounds[2] - bounds[0]) * 0.08
y_pad = (bounds[3] - bounds[1]) * 0.08
ax.set_xlim(bounds[0] - x_pad, bounds[2] + x_pad)
ax.set_ylim(bounds[1] - y_pad, bounds[3] + y_pad)
ax.set_axis_off()

handles = [
    plt.Line2D([0], [0], marker="^", color="w", markerfacecolor=MINE_COLOR, markersize=14, label="Coal Mine (1779-1986)", linestyle="None"),
    plt.Line2D([0], [0], marker="s", color="w", markerfacecolor=COLONY_COLOR, markersize=14, label="Worker Colony (1880-1910)", linestyle="None"),
]
legend = ax.legend(handles=handles, loc="lower right", fontsize=15, frameon=True,
                    facecolor="#253250", edgecolor="#7FB8BE", framealpha=0.95, labelcolor="#FFFFFF")
for text in legend.get_texts():
    text.set_fontweight("bold")
    text.set_color("#FFFFFF")

fig.text(0.5, 0.95, "ESSEN'S INDUSTRIAL GEOGRAPHY", fontsize=24, fontweight="bold", color=TEXT_COLOR, ha="center")
fig.text(0.5, 0.915, "Coal Mines and Worker Colonies, 1779–1986 (4 mines + 4 colonies, multi-city replication dataset)",
          fontsize=13, color="#B0BEC5", ha="center")

plt.figtext(0.5, 0.02, "GHOST INFRASTRUCTURE — Sources: GADM, KuLaDig, Wikipedia",
            ha="center", fontsize=9, color="#7FB8BE")

plt.tight_layout(rect=[0, 0.03, 1, 0.9])
plt.savefig("outputs/plots/essen_historical_geography.png", dpi=300, facecolor=BACKGROUND, bbox_inches="tight")
plt.close()
print("Saved: outputs/plots/essen_historical_geography.png")
