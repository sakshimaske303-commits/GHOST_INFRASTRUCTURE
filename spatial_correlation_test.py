import geopandas as gpd
import pandas as pd
from scipy.spatial import cKDTree
import numpy as np

print("Loading data...")
nodes = gpd.read_file("data/accessibility/bochum_15min_coverage.gpkg")
mines = gpd.read_file("data/historical_georeferenced/bochum_coal_mines.gpkg")
colonies = gpd.read_file("data/historical_georeferenced/bochum_zechensiedlungen.gpkg")

# Combine historical industrial sites into one set
historical_sites = pd.concat([
    mines[["geometry"]],
    colonies[["geometry"]]
], ignore_index=True)
historical_gdf = gpd.GeoDataFrame(historical_sites, crs=nodes.crs)

print(f"Historical sites: {len(historical_gdf)}")

# Ensure same CRS, project to metric for distance calculation
nodes_m = nodes.to_crs("EPSG:32632")  # UTM Zone 32N, covers Germany
historical_m = historical_gdf.to_crs("EPSG:32632")

# For each network node, find distance to nearest historical industrial site
hist_coords = np.array([(geom.x, geom.y) for geom in historical_m.geometry])
tree = cKDTree(hist_coords)

node_coords = np.array([(geom.x, geom.y) for geom in nodes_m.geometry])
distances, _ = tree.query(node_coords)

nodes_m["dist_to_historical_m"] = distances

# Compare: average distance to historical sites for LOW accessibility nodes
# vs HIGH accessibility nodes
low_access = nodes_m[nodes_m["within_15min"] == False]
high_access = nodes_m[nodes_m["within_15min"] == True]

print(f"\nLow-accessibility nodes (n={len(low_access)}):")
print(f"  Mean distance to nearest historical site: {low_access['dist_to_historical_m'].mean():.1f}m")
print(f"  Median distance: {low_access['dist_to_historical_m'].median():.1f}m")

print(f"\nHigh-accessibility nodes (n={len(high_access)}):")
print(f"  Mean distance to nearest historical site: {high_access['dist_to_historical_m'].mean():.1f}m")
print(f"  Median distance: {high_access['dist_to_historical_m'].median():.1f}m")

# Statistical test: is the difference significant?
from scipy import stats
t_stat, p_value = stats.ttest_ind(
    low_access["dist_to_historical_m"].dropna(),
    high_access["dist_to_historical_m"].dropna(),
    equal_var=False
)
print(f"\nWelch's t-test: t={t_stat:.3f}, p={p_value:.5f}")

nodes_m.to_file("data/accessibility/bochum_accessibility_with_distance.gpkg", driver="GPKG")
print("\nSaved: data/accessibility/bochum_accessibility_with_distance.gpkg")