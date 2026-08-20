"""Full Essen pipeline (multi-city comparison), replicating the Bochum methodology:
isochrones -> distance to historical sites (Welch's t) -> city-center confound (logit) -> LISA.
Doesn't filter services outside the true boundary, same as the Bochum scripts (ox.features_from_place already scopes to it).
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
from libpysal.weights import KNN
from esda.moran import Moran_Local

WALK_SPEED_M_PER_MIN = 75
MAX_MINUTES = 15
MAX_DISTANCE_M = WALK_SPEED_M_PER_MIN * MAX_MINUTES

print("=== STEP 1: Load network + services ===")
G = ox.load_graphml("data/osm_network/essen_walk_network.graphml")
pois = gpd.read_file("data/osm_network/essen_essential_services.gpkg")
pois = pois[pois.geometry.type == "Point"]
print(f"Nodes: {len(G.nodes)}, Edges: {len(G.edges)}, Point services: {len(pois)}")

nodes, edges = ox.graph_to_gdfs(G)
poi_nodes = ox.distance.nearest_nodes(G, pois.geometry.x, pois.geometry.y)

print(f"\n=== STEP 2: 15-min accessibility ({MAX_DISTANCE_M}m) ===")
covered_nodes = set()
for node in set(poi_nodes):
    try:
        lengths = nx.single_source_dijkstra_path_length(G, node, cutoff=MAX_DISTANCE_M, weight="length")
        covered_nodes.update(lengths.keys())
    except Exception:
        continue

nodes["within_15min"] = nodes.index.isin(covered_nodes)
pct_covered = (nodes["within_15min"].sum() / len(nodes)) * 100
print(f"{pct_covered:.1f}% of {len(nodes)} nodes within 15-min walk of a service")
nodes.to_file("data/accessibility/essen_15min_coverage.gpkg", driver="GPKG")

print("\n=== STEP 3: Distance to historical sites + Welch's t-test ===")
mines = gpd.read_file("data/historical_georeferenced/essen_coal_mines.gpkg")
colonies = gpd.read_file("data/historical_georeferenced/essen_zechensiedlungen.gpkg")
historical_sites = pd.concat([mines[["geometry"]], colonies[["geometry"]]], ignore_index=True)
historical_gdf = gpd.GeoDataFrame(historical_sites, crs=nodes.crs)
print(f"Historical sites: {len(historical_gdf)} ({len(mines)} mines + {len(colonies)} colonies)")

nodes_m = nodes.to_crs("EPSG:32632")
historical_m = historical_gdf.to_crs("EPSG:32632")

hist_coords = np.array([(geom.x, geom.y) for geom in historical_m.geometry])
tree = cKDTree(hist_coords)
node_coords = np.array([(geom.x, geom.y) for geom in nodes_m.geometry])
distances, _ = tree.query(node_coords)
nodes_m["dist_to_historical_m"] = distances

low_access = nodes_m[nodes_m["within_15min"] == False]
high_access = nodes_m[nodes_m["within_15min"] == True]

print(f"Low-access (n={len(low_access)}): mean dist={low_access['dist_to_historical_m'].mean():.1f}m, median={low_access['dist_to_historical_m'].median():.1f}m")
print(f"High-access (n={len(high_access)}): mean dist={high_access['dist_to_historical_m'].mean():.1f}m, median={high_access['dist_to_historical_m'].median():.1f}m")

t_stat, p_value = stats.ttest_ind(
    low_access["dist_to_historical_m"].dropna(), high_access["dist_to_historical_m"].dropna(), equal_var=False
)
n1, n2 = len(low_access), len(high_access)
s1, s2 = low_access["dist_to_historical_m"].std(ddof=1), high_access["dist_to_historical_m"].std(ddof=1)
pooled_sd = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))
cohens_d = (low_access["dist_to_historical_m"].mean() - high_access["dist_to_historical_m"].mean()) / pooled_sd
print(f"Welch's t-test: t={t_stat:.3f}, p={p_value:.2e}, Cohen's d={cohens_d:.3f}")

nodes_m.to_file("data/accessibility/essen_accessibility_with_distance.gpkg", driver="GPKG")

print("\n=== STEP 4: City-center confound (Essen Hauptbahnhof) ===")
city_center = gpd.GeoDataFrame(
    {"geometry": [gpd.points_from_xy([7.0134], [51.4517])[0]]}, crs="EPSG:4326"
).to_crs("EPSG:32632")
center_coords = np.array([(city_center.geometry.iloc[0].x, city_center.geometry.iloc[0].y)])
tree_c = cKDTree(center_coords)
dist_to_center, _ = tree_c.query(node_coords)
nodes_m["dist_to_center_m"] = dist_to_center

corr = np.corrcoef(nodes_m["dist_to_historical_m"], nodes_m["dist_to_center_m"])[0, 1]
print(f"Correlation dist-to-historical vs dist-to-center: r={corr:.3f}")

nodes_m["within_15min_int"] = nodes_m["within_15min"].astype(int)
model = smf.logit("within_15min_int ~ dist_to_historical_m + dist_to_center_m", data=nodes_m).fit(disp=0)
coef_hist = model.params["dist_to_historical_m"]
p_hist = model.pvalues["dist_to_historical_m"]
coef_center = model.params["dist_to_center_m"]
p_center = model.pvalues["dist_to_center_m"]
odds_hist_per_100m_closer = (np.exp(-coef_hist * 100) - 1) * 100
odds_center_per_100m_closer = (np.exp(-coef_center * 100) - 1) * 100
print(model.summary())
print(f"\nOdds %/100m closer -- historical: {odds_hist_per_100m_closer:.2f}% (p={p_hist:.2e}), center: {odds_center_per_100m_closer:.2f}% (p={p_center:.2e})")

nodes_m.to_file("data/accessibility/essen_accessibility_with_distance.gpkg", driver="GPKG")

print("\n=== STEP 5: Local Moran's I (LISA) ===")
coords = np.column_stack([nodes_m.geometry.x.values, nodes_m.geometry.y.values])
y = nodes_m["within_15min"].astype(int).values
w = KNN.from_array(coords, k=8)
w.transform = "r"
lisa = Moran_Local(y, w, permutations=99, seed=42)
sig = lisa.p_sim < 0.05
quadrant = lisa.q

n_sig = sig.sum()
ll_sig = ((quadrant == 3) & sig).sum()
hh_sig = ((quadrant == 1) & sig).sum()
hl_sig = ((quadrant == 4) & sig).sum()
lh_sig = ((quadrant == 2) & sig).sum()
print(f"Mean local I: {lisa.Is.mean():.3f}")
print(f"Significant nodes: {n_sig}/{len(y)} ({100*n_sig/len(y):.1f}%)")
print(f"  LL (cold-spot): {ll_sig}, HH (hot-spot): {hh_sig}, HL: {hl_sig}, LH: {lh_sig}")

low_in_ll = ((quadrant == 3) & sig & (y == 0)).sum()
pct_low_in_ll = 100 * low_in_ll / (y == 0).sum()
print(f"Low-accessibility nodes falling in significant LL clusters: {low_in_ll}/{(y==0).sum()} ({pct_low_in_ll:.1f}%)")

np.save("essen_lisa_q.npy", quadrant)
np.save("essen_lisa_sig.npy", sig)

results = {
    "n_nodes": int(len(nodes)),
    "n_edges": int(len(G.edges)),
    "n_services": int(len(pois)),
    "n_historical_sites": int(len(historical_gdf)),
    "n_mines": int(len(mines)),
    "n_colonies": int(len(colonies)),
    "pct_covered_15min": round(pct_covered, 1),
    "n_low": int(n1), "n_high": int(n2),
    "mean_dist_low": round(low_access["dist_to_historical_m"].mean(), 1),
    "mean_dist_high": round(high_access["dist_to_historical_m"].mean(), 1),
    "median_dist_low": round(low_access["dist_to_historical_m"].median(), 1),
    "median_dist_high": round(high_access["dist_to_historical_m"].median(), 1),
    "t_stat": round(t_stat, 3),
    "p_value": p_value,
    "cohens_d": round(cohens_d, 3),
    "corr_hist_center": round(corr, 3),
    "logit_coef_historical": coef_hist,
    "logit_p_historical": p_hist,
    "logit_coef_center": coef_center,
    "logit_p_center": p_center,
    "odds_pct_per_100m_closer_historical": round(odds_hist_per_100m_closer, 2),
    "odds_pct_per_100m_closer_center": round(odds_center_per_100m_closer, 2),
    "lisa_mean_local_I": round(float(lisa.Is.mean()), 3),
    "lisa_n_significant": int(n_sig),
    "lisa_pct_significant": round(100*n_sig/len(y), 1),
    "lisa_ll_coldspot": int(ll_sig),
    "lisa_hh_hotspot": int(hh_sig),
    "lisa_hl_outlier": int(hl_sig),
    "lisa_lh_outlier": int(lh_sig),
    "pct_low_access_in_ll_cluster": round(pct_low_in_ll, 1),
}
with open("essen_results.json", "w") as f:
    json.dump(results, f, indent=2, default=str)
print("\nSaved: essen_results.json")
