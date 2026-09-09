"""Threshold-sensitivity comparison chart (Bochum, 10/15/20-min thresholds). Written to
close a reproducibility gap: the original outputs/plots/threshold_sensitivity_comparison.png
had no generating script in the repo. Rebuilt from outputs/threshold_sensitivity_results.json
(already-computed, committed results -- no re-analysis performed), matching the existing
image's two-panel layout: left = mean distance to nearest historical site by accessibility
group at each threshold, right = effect size (Cohen's d) across thresholds.
"""
import json
import matplotlib.pyplot as plt

BACKGROUND = "#2E3A61"
CARD_COLOR = "#B4D5D6"
LOW_COLOR = "#B65A2A"
HIGH_COLOR = "#4F6D7A"
ACCENT = "#7FB8BE"

with open("outputs/threshold_sensitivity_results.json") as f:
    results = json.load(f)

thresholds = ["10", "15", "20"]
labels = [f"{t}-min\n({results[t]['max_dist_m']}m)" for t in thresholds]
mean_low = [results[t]["mean_dist_low"] for t in thresholds]
mean_high = [results[t]["mean_dist_high"] for t in thresholds]
cohens_d = [results[t]["cohens_d"] for t in thresholds]
t_stats = [results[t]["t_stat"] for t in thresholds]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
fig.patch.set_facecolor(BACKGROUND)

# --- Panel 1: mean distance by accessibility group, grouped by threshold ---
ax1.set_facecolor(CARD_COLOR)
x = range(len(thresholds))
width = 0.35
bars_low = ax1.bar([i - width / 2 for i in x], mean_low, width, color=LOW_COLOR, alpha=0.9, label="Low accessibility")
bars_high = ax1.bar([i + width / 2 for i in x], mean_high, width, color=HIGH_COLOR, alpha=0.9, label="High accessibility")
ax1.set_xticks(list(x))
ax1.set_xticklabels(labels, color="white", fontsize=11)
ax1.set_ylabel("Mean distance to nearest\nhistorical industrial site (m)", color="white", fontsize=11, fontweight="bold")
ax1.set_title("Reversed relationship holds at every threshold", color="white", fontsize=13, fontweight="bold")
ax1.tick_params(colors="white", labelsize=10)
for s in ax1.spines.values():
    s.set_color("white")
legend1 = ax1.legend(loc="upper left", fontsize=10, framealpha=0.9)

# --- Panel 2: effect size (Cohen's d) across thresholds ---
ax2.set_facecolor(CARD_COLOR)
ax2.plot(list(x), cohens_d, color=LOW_COLOR, marker="o", markersize=10, linewidth=2.5)
for i, d in zip(x, cohens_d):
    ax2.text(i, d + 0.025, f"d={d:.3f}", ha="center", fontsize=11, fontweight="bold", color="#111")
ax2.set_xticks(list(x))
ax2.set_xticklabels([f"{t}-min" for t in thresholds], color="white", fontsize=11)
ax2.set_ylim(0, max(cohens_d) + 0.2)
ax2.set_ylabel("Effect size (Cohen's d)", color="white", fontsize=11, fontweight="bold")
ax2.set_title("Effect size across thresholds", color="white", fontsize=13, fontweight="bold")
ax2.tick_params(colors="white", labelsize=10)
for s in ax2.spines.values():
    s.set_color("white")

fig.suptitle("Walking-Threshold Sensitivity: Ghost Infrastructure Effect, Bochum",
              color="white", fontsize=18, fontweight="bold", y=1.02)

footer = " | ".join(f"{t}-min: t={t_stats[i]:.2f}, d={cohens_d[i]:.3f}" for i, t in enumerate(thresholds))
plt.figtext(0.5, -0.03, f"All three thresholds: Welch's t-test p<0.00001. {footer}",
            ha="center", fontsize=10.5, color=ACCENT, fontweight="bold")

plt.tight_layout()
plt.savefig("outputs/plots/threshold_sensitivity_comparison.png", dpi=300, facecolor=BACKGROUND, bbox_inches="tight")
plt.close()
print("Saved: outputs/plots/threshold_sensitivity_comparison.png")
