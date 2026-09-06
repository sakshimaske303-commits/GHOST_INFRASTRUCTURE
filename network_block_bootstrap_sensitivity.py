"""
Sensitivity check on network_block_bootstrap.py: re-runs the identical
network-block bootstrap at BLOCK_TARGET_SIZE = 250, 500, 1000 to see
whether the observed difference / CI direction hold up across block sizes.
Same logic as network_block_bootstrap.py, just parameterized over target size.
"""

import os
import json
import numpy as np
import pandas as pd
import geopandas as gpd
import osmnx as ox
import networkx as nx
import statsmodels.formula.api as smf
from scipy.spatial import cKDTree

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

NODES_PATH = os.path.join(BASE_DIR, "data", "accessibility", "bochum_accessibility_with_distance.gpkg")
GRAPH_PATH = os.path.join(BASE_DIR, "data", "osm_network", "bochum_walk_network.graphml")
OUT_JSON = os.path.join(BASE_DIR, "outputs", "network_block_bootstrap_sensitivity_results.json")

CITY_CENTER_LONLAT = (7.2162, 51.4818)
N_BOOT = 999
RANDOM_SEED = 42
TARGET_SIZES = [250, 500, 1000]


def make_network_blocks(graph, node_ids, target_size, seed):
    rng = np.random.default_rng(seed)
    node_ids = set(node_ids)
    H = graph.subgraph(node_ids).copy()
    unassigned = set(H.nodes)
    blocks = []
    while unassigned:
        start = rng.choice(list(unassigned))
        block = []
        queue = [start]
        queued = {start}
        while queue and len(block) < target_size:
            node = queue.pop(0)
            if node not in unassigned:
                continue
            block.append(node)
            unassigned.discard(node)
            neighbours = list(H.neighbors(node))
            rng.shuffle(neighbours)
            for nb in neighbours:
                if nb in unassigned and nb not in queued:
                    queue.append(nb)
                    queued.add(nb)
        blocks.append(block)
    return blocks


def percentile_ci(values, alpha=0.05):
    values = np.asarray(values)
    return float(np.percentile(values, 100 * alpha / 2)), float(np.percentile(values, 100 * (1 - alpha / 2)))


def run_for_target(df, UG, target_size, seed):
    import time
    t0 = time.time()
    blocks = make_network_blocks(UG, df["osmid_key"].tolist(), target_size, seed)
    sizes = np.array([len(b) for b in blocks])
    block_lookup = {node: i for i, block in enumerate(blocks) for node in block}
    df = df.copy()
    df["block"] = df["osmid_key"].map(block_lookup).astype(int)
    print(f"  blocks built: {len(blocks)} (mean {sizes.mean():.1f}, min {sizes.min()}, max {sizes.max()}) [{time.time()-t0:.1f}s]", flush=True)

    high = df.loc[df["within"] == 1, "historical"]
    low = df.loc[df["within"] == 0, "historical"]
    observed_difference = low.mean() - high.mean()

    original_model = smf.logit("within ~ historical + center", data=df).fit(disp=0)
    beta_hist_original = original_model.params["historical"]
    beta_center_original = original_model.params["center"]
    print(f"  original model fit [{time.time()-t0:.1f}s]", flush=True)

    # Precompute numpy arrays + block -> row-index arrays for fast resampling
    hist_arr = df["historical"].to_numpy()
    center_arr = df["center"].to_numpy()
    within_arr = df["within"].to_numpy()
    block_arr = df["block"].to_numpy()
    n_blocks_total = block_arr.max() + 1
    block_indices = [np.where(block_arr == i)[0] for i in range(n_blocks_total)]

    rng = np.random.default_rng(seed)
    block_ids = np.arange(n_blocks_total)

    boot_diffs, boot_beta_hist, boot_beta_center = [], [], []
    successful = 0
    for b in range(N_BOOT):
        sampled = rng.choice(block_ids, size=len(block_ids), replace=True)
        idx = np.concatenate([block_indices[i] for i in sampled])

        h = hist_arr[idx]
        c = center_arr[idx]
        w = within_arr[idx]

        high_b = h[w == 1]
        low_b = h[w == 0]
        if len(high_b) == 0 or len(low_b) == 0:
            continue
        boot_diffs.append(low_b.mean() - high_b.mean())

        if len(np.unique(w)) < 2:
            continue
        try:
            boot_df = pd.DataFrame({"within": w, "historical": h, "center": c})
            model_b = smf.logit("within ~ historical + center", data=boot_df).fit(disp=0, maxiter=200)
            boot_beta_hist.append(model_b.params["historical"])
            boot_beta_center.append(model_b.params["center"])
            successful += 1
        except Exception:
            continue

        if (b + 1) % 100 == 0:
            print(f"  {b+1}/{N_BOOT} bootstrap reps done [{time.time()-t0:.1f}s]", flush=True)

    diff_ci = percentile_ci(boot_diffs)
    beta_hist_ci = percentile_ci(boot_beta_hist)
    beta_center_ci = percentile_ci(boot_beta_center)

    return {
        "block_target_size": target_size,
        "n_blocks": len(blocks),
        "mean_block_size": round(float(sizes.mean()), 2),
        "min_block_size": int(sizes.min()),
        "max_block_size": int(sizes.max()),
        "n_bootstrap_requested": N_BOOT,
        "n_bootstrap_successful_logit": successful,
        "observed_difference_m": round(float(observed_difference), 2),
        "bootstrap_ci_difference_m": [round(diff_ci[0], 2), round(diff_ci[1], 2)],
        "original_logit_coef_historical": beta_hist_original,
        "bootstrap_ci_logit_coef_historical": [beta_hist_ci[0], beta_hist_ci[1]],
        "original_logit_coef_center": beta_center_original,
        "bootstrap_ci_logit_coef_center": [beta_center_ci[0], beta_center_ci[1]],
    }


def main():
    print("Loading nodes...")
    nodes = gpd.read_file(NODES_PATH)
    nodes = nodes.dropna(subset=["dist_to_historical_m", "within_15min"]).copy()

    city_center = gpd.GeoDataFrame(
        {"geometry": gpd.points_from_xy([CITY_CENTER_LONLAT[0]], [CITY_CENTER_LONLAT[1]])},
        crs="EPSG:4326",
    ).to_crs(nodes.crs)
    center_coords = np.array([(city_center.geometry.iloc[0].x, city_center.geometry.iloc[0].y)])
    node_coords = np.array([(g.x, g.y) for g in nodes.geometry])
    tree = cKDTree(center_coords)
    nodes["dist_to_center_m"], _ = tree.query(node_coords)
    nodes["within_15min_int"] = nodes["within_15min"].astype(int)
    nodes["osmid_key"] = nodes["osmid"].astype(str)

    print("Loading network...")
    G = ox.load_graphml(GRAPH_PATH)
    G = nx.relabel_nodes(G, lambda n: str(n))
    UG = nx.Graph()
    UG.add_nodes_from(G.nodes)
    for u, v in G.edges():
        if u != v:
            UG.add_edge(u, v)

    network_ids = set(UG.nodes)
    nodes = nodes[nodes["osmid_key"].isin(network_ids)].copy()
    print(f"Matched observations: {len(nodes):,}")

    df = pd.DataFrame({
        "historical": nodes["dist_to_historical_m"].astype(float).values,
        "center": nodes["dist_to_center_m"].astype(float).values,
        "within": nodes["within_15min_int"].astype(int).values,
        "osmid_key": nodes["osmid_key"].values,
    })

    results = {}
    for target in TARGET_SIZES:
        print(f"\n=== Target block size {target} ===")
        r = run_for_target(df, UG, target, RANDOM_SEED)
        print(json.dumps(r, indent=2, default=str))
        results[str(target)] = r

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nSaved: {OUT_JSON}")


if __name__ == "__main__":
    main()
