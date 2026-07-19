import geopandas as gpd
import pandas as pd
from scipy.spatial import cKDTree
import numpy as np
from scipy import stats

print("Loading data...")
nodes = gpd.read_file("data/accessibility/bochum_accessibility_with_distance.gpkg")

# Bochum city center (Hauptbahnhof area)
city_center = gpd.GeoDataFrame(
    {"geometry": [gpd.points_from_xy([7.2162], [51.4818])[0]]},
    crs="EPSG:4326"
).to_crs("EPSG:32632")

center_coords = np.array([(city_center.geometry.iloc[0].x, city_center.geometry.iloc[0].y)])
node_coords = np.array([(geom.x, geom.y) for geom in nodes.geometry])

tree = cKDTree(center_coords)
dist_to_center, _ = tree.query(node_coords)
nodes["dist_to_center_m"] = dist_to_center

# Correlation: is distance-to-historical-site just a proxy for distance-to-center?
corr = np.corrcoef(nodes["dist_to_historical_m"], nodes["dist_to_center_m"])[0, 1]
print(f"\nCorrelation between dist-to-historical-site and dist-to-city-center: {corr:.3f}")

# Partial test: does historical distance still predict accessibility 
# AFTER controlling for distance to center?
import statsmodels.formula.api as smf

nodes["within_15min_int"] = nodes["within_15min"].astype(int)
model = smf.logit(
    "within_15min_int ~ dist_to_historical_m + dist_to_center_m",
    data=nodes
).fit()
print(model.summary())