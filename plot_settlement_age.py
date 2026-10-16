"""Figure: share of residents without 15-minute access, in areas built up before vs after 1975.
Reads the frozen results in outputs/robustness/settlement_age_results.json (no analysis here).
Run from the repository root:  python plot_settlement_age.py
"""
import json
from decimal import ROUND_HALF_UP, Decimal

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

with open("outputs/robustness/settlement_age_results.json", encoding="utf-8") as f:
    r = json.load(f)

groups = [("bochum", "points_only", "Bochum\n(point services)"),
          ("bochum", "all_services", "Bochum\n(all services)"),
          ("essen", "points_only", "Essen\n(point services)"),
          ("essen", "all_services", "Essen\n(all services)")]
pre = [r[c][k]["pct_without_access_pre1975"] for c, k, _ in groups]
post = [r[c][k]["pct_without_access_post1975"] for c, k, _ in groups]



def fmt(v):
    """Half-up rounding, as in the paper: 1 decimal, or 2 decimals below 1%."""
    q = Decimal("0.01") if v < 1 else Decimal("0.1")
    return f"{Decimal(str(v)).quantize(q, rounding=ROUND_HALF_UP)}%"


SURFACE, INK, MUTED, GRID = "#fcfcfb", "#1f1f1e", "#5f5e5a", "#e6e5e0"
PRE, POST = "#2a78d6", "#eb6834"

fig, ax = plt.subplots(figsize=(10, 5.6), facecolor=SURFACE)
ax.set_facecolor(SURFACE)
x = np.arange(len(groups))
w = 0.36
b1 = ax.bar(x - w / 2 - 0.01, pre, w, color=PRE, label="Built up before 1975")
b2 = ax.bar(x + w / 2 + 0.01, post, w, color=POST, label="First built up after 1975")
for bars in (b1, b2):
    for b in bars:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.4, fmt(b.get_height()),
                ha="center", va="bottom", fontsize=10, color=INK)
ax.set_xticks(x)
ax.set_xticklabels([g[2] for g in groups], color=INK, fontsize=10)
ax.set_ylabel("Residents without 15-minute walking access (%)", color=MUTED, fontsize=10)
ax.yaxis.grid(True, color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRID)
ax.tick_params(colors=MUTED, length=0)
ax.set_ylim(0, max(post) * 1.18)
ax.legend(frameon=False, fontsize=10, loc="upper right", labelcolor=INK)
ax.set_title("Residents of post-1975 development are more often without 15-minute access",
             loc="left", fontsize=12, color=INK, pad=14)
fig.text(0.01, 0.01, "Zensus 2022 100 m grid (residents); GHSL GHS-BUILT-S R2023A 1975 and 2020 (settlement age); "
         "post-1975 = 1975 built-up surface < 50% of 2020 value.", fontsize=8, color=MUTED)
fig.tight_layout(rect=[0, 0.04, 1, 1])
fig.savefig("outputs/robustness/settlement_age.png", dpi=200, facecolor=SURFACE)
print("Saved: outputs/robustness/settlement_age.png")
