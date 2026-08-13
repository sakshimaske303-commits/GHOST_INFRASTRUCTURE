import json
import matplotlib.pyplot as plt
import numpy as np

BACKGROUND = "#2E3A61"
CARD_COLOR = "#B4D5D6"
ACCENT = "#7FB8BE"

bochum = {
    "n_nodes": 69393, "n_sites": 17, "pct_covered": 85.8,
    "t_stat": 42.887, "cohens_d": 0.589,
    "corr_hist_center": 0.063,
    "odds_hist": 4.9, "odds_center": 3.0,
    "lisa_pct_sig": 14.8, "pct_low_in_ll": 97.1,
}
with open("essen_results.json") as f:
    essen = json.load(f)

fig, axes = plt.subplots(1, 3, figsize=(17, 6))
fig.patch.set_facecolor(BACKGROUND)

cities = ["Bochum", "Essen"]
colors = ["#4F6D7A", "#B65A2A"]

# Panel 1: Cohen's d (raw reversed-effect size)
ax = axes[0]
ax.set_facecolor(CARD_COLOR)
d_vals = [bochum["cohens_d"], essen["cohens_d"]]
bars = ax.bar(cities, d_vals, color=colors, alpha=0.85, width=0.5)
for b, v in zip(bars, d_vals):
    ax.text(b.get_x()+b.get_width()/2, v+0.02, f"d={v:.3f}", ha="center", fontsize=11, fontweight="bold", color="#111")
ax.set_ylabel("Effect size (Cohen's d)", color="white", fontsize=11, fontweight="bold")
ax.set_title("Raw reversed effect:\nreplicates in both cities", color="white", fontsize=12, fontweight="bold")
ax.tick_params(colors="white", labelsize=11)
for s in ax.spines.values(): s.set_color("white")

# Panel 2: correlation between historical-site distance and center distance (confound entanglement)
ax2 = axes[1]
ax2.set_facecolor(CARD_COLOR)
corr_vals = [bochum["corr_hist_center"], essen["corr_hist_center"]]
bars2 = ax2.bar(cities, corr_vals, color=colors, alpha=0.85, width=0.5)
for b, v in zip(bars2, corr_vals):
    ax2.text(b.get_x()+b.get_width()/2, v+0.01, f"r={v:.3f}", ha="center", fontsize=11, fontweight="bold", color="#111")
ax2.axhline(0.3, color="#111", linestyle="--", linewidth=1, alpha=0.6)
ax2.set_ylabel("Correlation: dist-to-historical-site\nvs dist-to-city-center", color="white", fontsize=10.5, fontweight="bold")
ax2.set_title("Confound independence:\ndoes NOT replicate in Essen", color="white", fontsize=12, fontweight="bold")
ax2.tick_params(colors="white", labelsize=11)
for s in ax2.spines.values(): s.set_color("white")

# Panel 3: LISA - % low-access nodes in significant cold-spot clusters
ax3 = axes[2]
ax3.set_facecolor(CARD_COLOR)
lisa_vals = [bochum["pct_low_in_ll"], essen["pct_low_access_in_ll_cluster"]]
bars3 = ax3.bar(cities, lisa_vals, color=colors, alpha=0.85, width=0.5)
for b, v in zip(bars3, lisa_vals):
    ax3.text(b.get_x()+b.get_width()/2, v+1, f"{v:.1f}%", ha="center", fontsize=11, fontweight="bold", color="#111")
ax3.set_ylim(0, 105)
ax3.set_ylabel("% of low-accessibility nodes in\nsignificant LL cold-spot clusters", color="white", fontsize=10.5, fontweight="bold")
ax3.set_title("Spatial clustering (LISA):\nreplicates almost exactly", color="white", fontsize=12, fontweight="bold")
ax3.tick_params(colors="white", labelsize=11)
for s in ax3.spines.values(): s.set_color("white")

fig.suptitle("Ghost Infrastructure: Bochum vs. Essen Multi-City Comparison", color="white", fontsize=16, fontweight="bold", y=1.03)
plt.figtext(0.5, -0.05,
            f"Essen: {essen['n_nodes']:,} nodes, {essen['n_historical_sites']} historical sites (Phase 1 subset vs Bochum's 17) | "
            f"Welch's t-test both cities p<0.00001 | Essen confound-controlled logit: historical-site coefficient sign REVERSES "
            f"(entangled with city-center, unlike Bochum)",
            ha="center", fontsize=9.5, color=ACCENT, fontweight="bold", wrap=True)

plt.tight_layout()
plt.savefig("bochum_essen_comparison.png", dpi=200, facecolor=BACKGROUND, bbox_inches="tight")
print("Saved: bochum_essen_comparison.png")
