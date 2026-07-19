import osmnx as ox
import geopandas as gpd
import networkx as nx

print("Loading network and services...")
G = ox.load_graphml("data/osm_network/bochum_walk_network.graphml")
pois = gpd.read_file("data/osm_network/bochum_essential_services.gpkg")

pois = pois[pois.geometry.type == "Point"]
print(f"Point-based services: {len(pois)}")

# 15 minutes at average walking speed (~4.5 km/h = 75 m/min) = ~1125m network distance
WALK_SPEED_M_PER_MIN = 75
MAX_MINUTES = 15
MAX_DISTANCE_M = WALK_SPEED_M_PER_MIN * MAX_MINUTES

nodes, edges = ox.graph_to_gdfs(G)

# Find nearest network node for each service point
poi_nodes = ox.distance.nearest_nodes(G, pois.geometry.x, pois.geometry.y)

print(f"\nComputing 15-minute service catchments ({MAX_DISTANCE_M}m network distance)...")
covered_nodes = set()
for node in set(poi_nodes):
    try:
        lengths = nx.single_source_dijkstra_path_length(G, node, cutoff=MAX_DISTANCE_M, weight="length")
        covered_nodes.update(lengths.keys())
    except Exception:
        continue

print(f"Nodes within 15-min walk of any essential service: {len(covered_nodes)} / {len(nodes)}")

nodes["within_15min"] = nodes.index.isin(covered_nodes)
nodes.to_file("data/accessibility/bochum_15min_coverage.gpkg", driver="GPKG")
print("Saved: data/accessibility/bochum_15min_coverage.gpkg")

pct_covered = (nodes["within_15min"].sum() / len(nodes)) * 100
print(f"\n{pct_covered:.1f}% of network nodes are within a 15-minute walk of an essential service")