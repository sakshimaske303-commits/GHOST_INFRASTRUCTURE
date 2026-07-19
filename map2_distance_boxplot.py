import geopandas as gpd
import matplotlib.pyplot as plt

BACKGROUND = "#2E3A61"
CARD_COLOR = "#B4D5D6"
ACCENT = "#7FB8BE"
TEXT_DARK = "#111111"

nodes = gpd.read_file("data/accessibility/bochum_accessibility_with_distance.gpkg")

low_access = nodes[nodes["within_15min"] == False]["dist_to_historical_m"]
high_access = nodes[nodes["within_15min"] == True]["dist_to_historical_m"]

fig, ax = plt.subplots(figsize=(10, 7))
fig.patch.set_facecolor(BACKGROUND)
ax.set_facecolor(CARD_COLOR)

bp = ax.boxplot([high_access, low_access], tick_labels=["High Accessibility", "Low Accessibility"],
                 patch_artist=True, showfliers=False, widths=0.5)

for patch, color in zip(bp['boxes'], ["#4F6D7A", "#B65A2A"]):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)

for element in ['whiskers', 'caps', 'medians']:
    plt.setp(bp[element], color=TEXT_DARK, linewidth=1.5)

ax.set_ylabel("Distance to Nearest Historical Industrial Site (m)", color="white", fontsize=12, fontweight="bold")
ax.set_title("Ghost Infrastructure Effect\nHigh-Accessibility Nodes Are Closer to Historical Sites",
             color="white", fontsize=15, fontweight="bold", pad=20)
ax.tick_params(colors="white", labelsize=11)
for spine in ax.spines.values():
    spine.set_color("white")

plt.figtext(0.5, -0.02, "Welch's t-test: t=42.887, p<0.00001", ha="center", fontsize=10, color="#7FB8BE", fontweight="bold")

plt.tight_layout(rect=[0, 0.05, 1, 1])

plt.tight_layout()
plt.savefig("outputs/plots/distance_comparison_boxplot.png", dpi=200, facecolor=BACKGROUND, bbox_inches="tight")
plt.close()
print("Saved: outputs/plots/distance_comparison_boxplot.png")