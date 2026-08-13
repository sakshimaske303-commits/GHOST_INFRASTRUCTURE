"""
GHOST_INFRASTRUCTURE — Essen multi-city comparison, step 2 of 2 (run this locally).

This is the exact same method as the project's own download_network.py, just
pointed at Essen instead of Bochum. This step needs to run on YOUR machine
because the cloud sandbox Claude works in has OpenStreetMap's servers
(Overpass/Nominatim) blocked on its network allowlist -- same category of
limitation as the GEE-credential steps on the other projects.

Run this from the GHOST_INFRASTRUCTURE folder (same place you'd run the
original download_network.py), after `pip install osmnx` if not already
installed (you already have it, since you ran the Bochum version).

Then send back (or let Claude stage from your device) these two new files:
  data/osm_network/essen_walk_network.graphml
  data/osm_network/essen_essential_services.gpkg
"""
import osmnx as ox
import os

os.makedirs("data/osm_network", exist_ok=True)

print("Downloading Essen walking network...")
place_name = "Essen, Germany"

G = ox.graph_from_place(place_name, network_type="walk")
print(f"Network downloaded: {len(G.nodes)} nodes, {len(G.edges)} edges")

ox.save_graphml(G, "data/osm_network/essen_walk_network.graphml")
print("Saved: data/osm_network/essen_walk_network.graphml")

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

pois_clean.to_file("data/osm_network/essen_essential_services.gpkg", driver="GPKG")
print("Saved: data/osm_network/essen_essential_services.gpkg")
print("\nDone. Send these two files back (or Claude will stage them from your device).")
