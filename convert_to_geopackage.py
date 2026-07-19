import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import os

os.makedirs("data/historical_georeferenced", exist_ok=True)

# Coal Mines
mines_df = pd.read_csv("data/historical_maps/coal_mines.csv")
mines_gdf = gpd.GeoDataFrame(
    mines_df,
    geometry=[Point(xy) for xy in zip(mines_df["longitude"], mines_df["latitude"])],
    crs="EPSG:4326"
)
mines_gdf.to_file("data/historical_georeferenced/bochum_coal_mines.gpkg", driver="GPKG")
print(f"Saved coal mines: {len(mines_gdf)} features")

# Zechensiedlungen
colonies_df = pd.read_csv("data/historical_maps/zechensiedlungen.csv")
colonies_gdf = gpd.GeoDataFrame(
    colonies_df,
    geometry=[Point(xy) for xy in zip(colonies_df["longitude"], colonies_df["latitude"])],
    crs="EPSG:4326"
)
colonies_gdf.to_file("data/historical_georeferenced/bochum_zechensiedlungen.gpkg", driver="GPKG")
print(f"Saved worker colonies: {len(colonies_gdf)} features")

print("\nBoth layers ready for QGIS.")