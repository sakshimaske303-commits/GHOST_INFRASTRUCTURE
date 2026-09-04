

import os
import json
import numpy as np
import geopandas as gpd
import osmnx as ox
import networkx as nx
from libpysal.weights import W
from esda.moran import Moran_Local

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

NODES_PATH = os.path.join(BASE_DIR, "data", "accessibility", "bochum_accessibility_with_distance.gpkg")
GRAPH_PATH = os.path.join(BASE_DIR, "data", "osm_network", "bochum_walk_network.graphml")
OUT_JSON = os.path.join(BASE_DIR, "outputs", "lisa_network_results.json")

NETWORK_NEIGHBOR_M = 750  # < the 1,125m / 15-min threshold, on purpose (see module docstring)
PERMUTATIONS = 999
SEED = 42
SIG_LEVEL = 0.05


def main():
    print("Loading nodes and network...")
    nodes = gpd.read_file(NODES_PATH)
    nodes["osmid_key"] = nodes["osmid"].astype(str)

    G = ox.load_graphml(GRAPH_PATH)
    G = nx.relabel_nodes(G, lambda n: str(n))

    # Undirected, simple graph: we only need connectivity + edge length here,
    # not the original directed/multigraph walking rules.
    UG = nx.Graph()
    for u, v, data in G.edges(data=True):
        if u == v:
            continue
        length = data.get("length")
        try:
            length = float(length)
        except (TypeError, ValueError):
            continue
        if UG.has_edge(u, v):
            UG[u][v]["length"] = min(UG[u][v]["length"], length)
        else:
            UG.add_edge(u, v, length=length)

    graph_nodes = set(UG.nodes)
    missing = set(nodes["osmid_key"]) - graph_nodes
    if missing:
        print(f"WARNING: {len(missing):,} nodes in the GeoPackage are not in the network graph -- dropping them.")
    nodes = nodes[nodes["osmid_key"].isin(graph_nodes)].copy()
    print(f"Matched nodes: {len(nodes):,}")

    node_ids = nodes["osmid_key"].tolist()
    node_id_set = set(node_ids)

    print(f"Building network-distance weights (cutoff={NETWORK_NEIGHBOR_M}m)...")
    neighbor_dict = {}
    weight_dict = {}
    for i, node in enumerate(node_ids):
        lengths = nx.single_source_dijkstra_path_length(
            UG, node, cutoff=NETWORK_NEIGHBOR_M, weight="length"
        )
        nearby = [n for n in lengths if n != node and n in node_id_set]
        neighbor_dict[node] = nearby
        weight_dict[node] = [1.0] * len(nearby)
        if (i + 1) % 10000 == 0:
            print(f"  {i + 1:,} / {len(node_ids):,} nodes processed")

    w = W(neighbor_dict, weight_dict, ids=node_ids)
    w.transform = "r"
    print(f"Weights built. Islands (no neighbor within {NETWORK_NEIGHBOR_M}m): {len(w.islands):,}")

    analysis = nodes.set_index("osmid_key")
    y = analysis.loc[w.id_order, "within_15min"].astype(int).to_numpy()

    print(f"Running Local Moran's I ({PERMUTATIONS} permutations)...")
    lisa = Moran_Local(y, w, permutations=PERMUTATIONS, seed=SEED)

    sig = lisa.p_sim < SIG_LEVEL
    quadrant = lisa.q  # 1=HH, 2=LH, 3=LL, 4=HL

    results = {
        "neighbor_definition": f"network distance <= {NETWORK_NEIGHBOR_M}m",
        "permutations": PERMUTATIONS,
        "n_nodes": int(len(y)),
        "n_islands": int(len(w.islands)),
        "mean_local_I": round(float(lisa.Is.mean()), 3),
        "pct_significant": round(100 * sig.sum() / len(y), 1),
        "n_significant": int(sig.sum()),
        "n_LL_significant": int(((quadrant == 3) & sig).sum()),
        "n_HH_significant": int(((quadrant == 1) & sig).sum()),
        "n_HL_significant": int(((quadrant == 4) & sig).sum()),
        "n_LH_significant": int(((quadrant == 2) & sig).sum()),
    }

    print(json.dumps(results, indent=2))

    np.save(os.path.join(BASE_DIR, "lisa_network_q.npy"), quadrant)
    np.save(os.path.join(BASE_DIR, "lisa_network_sig.npy"), sig)
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {OUT_JSON}")
    print("Compare n_significant / pct_significant above against the KNN(k=8) version")
    print("(spatial_clustering_lisa.py's printed output) to see how much the neighbor")
    print("definition itself changes the result.")


if __name__ == "__main__":
    main()
