import osmnx as ox
import os

os.makedirs("data/osm_network", exist_ok=True)

print("Downloading Bochum walking network...")
place_name = "Bochum, Germany"

# Walking network for 15-minute accessibility analysis
G = ox.graph_from_place(place_name, network_type="walk")

print(f"Network downloaded: {len(G.nodes)} nodes, {len(G.edges)} edges")

ox.save_graphml(G, "data/osm_network/bochum_walk_network.graphml")
print("Saved: data/osm_network/bochum_walk_network.graphml")

# Also download essential services (points of interest) for accessibility targets
print("\nDownloading essential services...")

tags = {
    "amenity": ["hospital", "clinic", "pharmacy", "school", "kindergarten"],
    "shop": ["supermarket", "convenience"],
    "leisure": ["park"],
}

pois = ox.features_from_place(place_name, tags)
print(f"Essential services found: {len(pois)}")

pois_clean = pois[["geometry"]].copy()
for col in ["amenity", "shop", "leisure", "name"]:
    if col in pois.columns:
        pois_clean[col] = pois[col]

pois_clean.to_file("data/osm_network/bochum_essential_services.gpkg", driver="GPKG")
print("Saved: data/osm_network/bochum_essential_services.gpkg")