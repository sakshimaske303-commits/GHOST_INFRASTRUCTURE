"""Walking-time-threshold sensitivity check (Bochum): does the reversed distance
relationship hold at 10-min/750m and 20-min/1500m, not just 15-min/1125m?
Reuses the existing network/POIs and distances from verify_distances.py / test_confound.py.
"""
import json
import numpy as np
import pandas as pd
import geopandas as gpd
import networkx as nx
import osmnx as ox
from scipy import stats
from scipy.spatial import cKDTree
import statsmodels.formula.api as smf

WALK_SPEED_M_PER_MIN = 75
THRESHOLDS_MIN = [10, 15, 20]

print("Loading network and services...")
G = ox.load_graphml("data/osm_network/bochum_walk_network.graphml")
pois = gpd.read_file("data/osm_network/bochum_essential_services.gpkg")
pois = pois[pois.geometry.type == "Point"]
print(f"Point-based services: {len(pois)}")

nodes_full, edges = ox.graph_to_gdfs(G)
poi_nodes = ox.distance.nearest_nodes(G, pois.geometry.x, pois.geometry.y)

# Reference dataset with dist_to_historical_m (from verify_distances.py) and
# dist_to_center_m recomputed exactly as test_confound.py does.
ref = gpd.read_file("data/accessibility/bochum_accessibility_with_distance.gpkg")
ref = ref.set_index("osmid")

city_center = gpd.GeoDataFrame(
    {"geometry": [gpd.points_from_xy([7.2162], [51.4818])[0]]},
    crs="EPSG:4326"
).to_crs("EPSG:32632")
center_coords = np.array([(city_center.geometry.iloc[0].x, city_center.geometry.iloc[0].y)])
node_coords_ref = np.array([(geom.x, geom.y) for geom in ref.geometry])
tree_center = cKDTree(center_coords)
dist_to_center, _ = tree_center.query(node_coords_ref)
ref["dist_to_center_m"] = dist_to_center

results = {}

for minutes in THRESHOLDS_MIN:
    max_dist = WALK_SPEED_M_PER_MIN * minutes
    print(f"\n=== Threshold: {minutes} min ({max_dist}m network distance) ===")

    covered_nodes = set()
    for node in set(poi_nodes):
        try:
            lengths = nx.single_source_dijkstra_path_length(G, node, cutoff=max_dist, weight="length")
            covered_nodes.update(lengths.keys())
        except Exception:
            continue

    within = pd.Series(nodes_full.index.isin(covered_nodes), index=nodes_full.index, name="within_thresh")
    pct = within.sum() / len(within) * 100
    print(f"{pct:.1f}% of nodes within {minutes}-min walk of a service")

    # Join onto ref (indexed by osmid) to get dist_to_historical_m / dist_to_center_m
    df = ref.copy()
    df["within_thresh"] = within.reindex(df.index).values

    low = df[df["within_thresh"] == False]
    high = df[df["within_thresh"] == True]

    t_stat, p_value = stats.ttest_ind(
        low["dist_to_historical_m"].dropna(), high["dist_to_historical_m"].dropna(), equal_var=False
    )
    n1, n2 = low["dist_to_historical_m"].dropna().shape[0], high["dist_to_historical_m"].dropna().shape[0]
    s1, s2 = low["dist_to_historical_m"].std(ddof=1), high["dist_to_historical_m"].std(ddof=1)
    pooled_sd = np.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
    cohens_d = (low["dist_to_historical_m"].mean() - high["dist_to_historical_m"].mean()) / pooled_sd

    corr = np.corrcoef(df["dist_to_historical_m"], df["dist_to_center_m"])[0, 1]

    df["within_thresh_int"] = df["within_thresh"].astype(int)
    model = smf.logit(
        "within_thresh_int ~ dist_to_historical_m + dist_to_center_m", data=df
    ).fit(disp=0)
    coef_hist = model.params["dist_to_historical_m"]
    p_hist = model.pvalues["dist_to_historical_m"]
    odds_pct_per_100m = (np.exp(coef_hist * 100) - 1) * 100

    coef_center = model.params["dist_to_center_m"]
    odds_pct_center_per_100m = (np.exp(coef_center * 100) - 1) * 100

    results[minutes] = {
        "max_dist_m": max_dist,
        "pct_covered": round(pct, 1),
        "n_low": int(n1), "n_high": int(n2),
        "mean_dist_low": round(low["dist_to_historical_m"].mean(), 1),
        "mean_dist_high": round(high["dist_to_historical_m"].mean(), 1),
        "t_stat": round(t_stat, 3),
        "p_value": p_value,
        "cohens_d": round(cohens_d, 3),
        "corr_hist_center": round(corr, 3),
        "logit_coef_historical": coef_hist,
        "logit_p_historical": p_hist,
        "odds_pct_per_100m_historical": round(odds_pct_per_100m, 2),
        "odds_pct_per_100m_center": round(odds_pct_center_per_100m, 2),
    }
    print(f"Welch's t-test: t={t_stat:.3f}, p={p_value:.2e}, Cohen's d={cohens_d:.3f}")
    print(f"Logit: hist coef={coef_hist:.6f} (p={p_hist:.2e}), odds%/100m={odds_pct_per_100m:.2f}%")

with open("threshold_sensitivity_results.json", "w") as f:
    json.dump(results, f, indent=2, default=str)

print("\n\n=== SUMMARY TABLE ===")
for m, r in results.items():
    print(f"{m}min ({r['max_dist_m']}m): coverage={r['pct_covered']}%, "
          f"low={r['mean_dist_low']}m, high={r['mean_dist_high']}m, "
          f"t={r['t_stat']}, p={r['p_value']:.2e}, d={r['cohens_d']}, "
          f"odds%/100m(hist)={r['odds_pct_per_100m_historical']}%")

print("\nSaved: threshold_sensitivity_results.json")
