import geopandas as gpd

germany = gpd.read_file("data/boundaries/gadm41_DEU.gpkg", layer="ADM_ADM_4")
bochum = germany[germany["NAME_4"] == "Bochum"]

bochum.to_file("data/boundaries/bochum_city.gpkg", driver="GPKG")
print(f"Saved: {len(bochum)} feature(s)")
print("Bounds:", bochum.total_bounds)