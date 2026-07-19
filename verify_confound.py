import geopandas as gpd

mines = gpd.read_file("data/historical_georeferenced/bochum_coal_mines.gpkg")
colonies = gpd.read_file("data/historical_georeferenced/bochum_zechensiedlungen.gpkg")

print("Coal mines bounds:", mines.total_bounds)
print("Colonies bounds:", colonies.total_bounds)

# Bochum city center approximate coordinates: 51.4818°N, 7.2162°E