import geopandas as gpd

# Try Level 4 first (usually city/municipality level in Germany)
germany = gpd.read_file("data/boundaries/gadm41_DEU.gpkg", layer="ADM_ADM_4")
bochum = germany[germany["NAME_4"].str.contains("Bochum", case=False, na=False)]
print(f"Found {len(bochum)} matches at Level 4")
print(bochum[["NAME_4", "NAME_3", "NAME_2"]] if len(bochum) > 0 else "No matches")