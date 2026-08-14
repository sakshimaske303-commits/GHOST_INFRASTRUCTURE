"""Interactive Plotly versions of the three headline GHOST INFRASTRUCTURE
charts. Same underlying data as the static figures - just Plotly instead of
matplotlib, so every point/box gets a hover tooltip."""

import json
import os

import geopandas as gpd
import plotly.graph_objects as go

OUT = "outputs/plots/interactive"
os.makedirs(OUT, exist_ok=True)

DARK_LAYOUT = dict(
    template="plotly_dark",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="#1a2340",
    font=dict(family="Inter, sans-serif", color="#F0F4F8"),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
    margin=dict(t=70, b=50, l=70, r=30),
)

BOCHUM_COLOR = "#4F6D7A"
ESSEN_COLOR = "#B65A2A"


# ============================================================
# 1. DISTANCE COMPARISON BOXPLOT — Bochum + Essen, high vs low accessibility
# ============================================================
def build_distance_boxplot():
    bochum = gpd.read_file("data/accessibility/bochum_accessibility_with_distance.gpkg")
    essen = gpd.read_file("data/accessibility/essen_accessibility_with_distance.gpkg")

    fig = go.Figure()
    for city, df, color in [("Bochum", bochum, BOCHUM_COLOR), ("Essen", essen, ESSEN_COLOR)]:
        high = df[df["within_15min"] == True]["dist_to_historical_m"]
        low = df[df["within_15min"] == False]["dist_to_historical_m"]
        fig.add_trace(go.Box(
            y=high, name=f"{city} — High Accessibility", marker_color=color, boxmean=True,
            hovertemplate="High Accessibility<br>Distance: %{y:.0f}m<extra></extra>",
        ))
        fig.add_trace(go.Box(
            y=low, name=f"{city} — Low Accessibility", marker_color=color, boxmean=True,
            marker=dict(opacity=0.55),
            hovertemplate="Low Accessibility<br>Distance: %{y:.0f}m<extra></extra>",
        ))

    fig.update_layout(
        title="Ghost Infrastructure Effect — Distance to Nearest Historical Industrial Site",
        yaxis_title="Distance to nearest historical industrial site (m)",
        height=580, boxmode="group", **DARK_LAYOUT,
    )
    fig.write_html(f"{OUT}/distance_comparison_boxplot.html", include_plotlyjs="cdn")
    print("Saved:", f"{OUT}/distance_comparison_boxplot.html")


# ============================================================
# 2. THRESHOLD SENSITIVITY — effect size + p-value by walking threshold
# ============================================================
def build_threshold_sensitivity():
    with open("outputs/threshold_sensitivity_results.json") as f:
        results = json.load(f)

    minutes = sorted(int(m) for m in results.keys())
    cohens_d = [results[str(m)]["cohens_d"] for m in minutes]
    p_values = [max(results[str(m)]["p_value"], 1e-300) for m in minutes]
    pct_covered = [results[str(m)]["pct_covered"] for m in minutes]
    labels = [f"{m} min" for m in minutes]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=labels, y=cohens_d, name="Effect size (Cohen's d)", marker_color="#7FB8BE",
        yaxis="y1",
        customdata=list(zip(p_values, pct_covered)),
        hovertemplate="%{x}<br>Cohen's d = %{y:.3f}<br>p = %{customdata[0]:.2e}<br>Coverage = %{customdata[1]:.1f}%<extra></extra>",
    ))
    fig.update_layout(
        title="Walking-Time-Threshold Sensitivity — Bochum",
        xaxis_title="Accessibility threshold",
        yaxis=dict(title="Effect size (Cohen's d)"),
        height=520, **DARK_LAYOUT,
    )
    fig.write_html(f"{OUT}/threshold_sensitivity.html", include_plotlyjs="cdn")
    print("Saved:", f"{OUT}/threshold_sensitivity.html")


# ============================================================
# 3. BOCHUM VS ESSEN COMPARISON — replication summary
# ============================================================
def build_bochum_essen_comparison():
    bochum = {
        "n_nodes": 69393, "n_sites": 17, "pct_covered": 85.8,
        "t_stat": 42.887, "cohens_d": 0.589,
        "corr_hist_center": 0.063,
        "odds_hist": 4.9, "odds_center": 3.0,
        "lisa_pct_sig": 14.8, "pct_low_in_ll": 97.1,
    }
    with open("outputs/essen_results.json") as f:
        essen = json.load(f)

    cities = ["Bochum", "Essen"]
    colors = [BOCHUM_COLOR, ESSEN_COLOR]

    fig = go.Figure()
    metrics = [
        ("Effect size (Cohen's d)", [bochum["cohens_d"], essen["cohens_d"]], "d"),
        ("Confound correlation (dist-hist vs dist-center)", [bochum["corr_hist_center"], essen["corr_hist_center"]], "r"),
        ("% low-access nodes in LL cold-spot cluster", [bochum["pct_low_in_ll"], essen["pct_low_access_in_ll_cluster"]], "%"),
    ]

    for i, (title, vals, unit) in enumerate(metrics):
        fig.add_trace(go.Bar(
            x=cities, y=vals, name=title, marker_color=colors,
            xaxis=f"x{i+1}" if i else "x", yaxis=f"y{i+1}" if i else "y",
            hovertemplate="%{x}<br>" + title + ": %{y:.3f}<extra></extra>",
            showlegend=False,
        ))

    fig.update_layout(
        grid=dict(rows=1, columns=3, pattern="independent"),
        title="Ghost Infrastructure: Bochum vs. Essen Multi-City Comparison",
        height=520, **{**DARK_LAYOUT, "margin": dict(t=90, b=90, l=50, r=30)},
        annotations=[
            dict(text="Raw reversed effect:<br>replicates in both cities", x=0.14, y=1.14, xref="paper", yref="paper", showarrow=False, font=dict(size=12)),
            dict(text="Confound independence:<br>does NOT replicate in Essen", x=0.5, y=1.14, xref="paper", yref="paper", showarrow=False, font=dict(size=12)),
            dict(text="Spatial clustering (LISA):<br>replicates almost exactly", x=0.86, y=1.14, xref="paper", yref="paper", showarrow=False, font=dict(size=12)),
            dict(text=f"Essen: {essen['n_nodes']:,} nodes, {essen['n_historical_sites']} historical sites (vs Bochum's 17) &nbsp;|&nbsp; "
                       f"Welch's t-test both cities p&lt;0.00001 &nbsp;|&nbsp; Essen confound-controlled logit: historical-site "
                       f"coefficient sign REVERSES (entangled with city-center, unlike Bochum)",
                 x=0.5, y=-0.18, xref="paper", yref="paper", showarrow=False, font=dict(size=10.5, color="#7FB8BE")),
        ],
    )
    fig.write_html(f"{OUT}/bochum_essen_comparison.html", include_plotlyjs="cdn")
    print("Saved:", f"{OUT}/bochum_essen_comparison.html")


if __name__ == "__main__":
    build_distance_boxplot()
    build_threshold_sensitivity()
    build_bochum_essen_comparison()
