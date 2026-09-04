

import os
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
OUT_JSON = os.path.join(BASE_DIR, "outputs", "network_block_bootstrap_results.json")

# Bochum Hauptbahnhof -- same city-center reference point as test_confound.py
# and threshold_sensitivity.py, so results are directly comparable.
CITY_CENTER_LONLAT = (7.2162, 51.4818)

N_BOOT = 999
BLOCK_TARGET_SIZE = 500  # ~139 blocks at 69,393 nodes -- see note at bottom on sensitivity
RANDOM_SEED = 42


def make_network_blocks(graph, node_ids, target_size, seed):
    """Partition node_ids into contiguous network blocks via randomized BFS."""
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


def main():
    print("Loading nodes and computing dist_to_center_m / within_15min_int (same as test_confound.py)...")
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

    print(f"Building network blocks (target size {BLOCK_TARGET_SIZE})...")
    blocks = make_network_blocks(UG, nodes["osmid_key"].tolist(), BLOCK_TARGET_SIZE, RANDOM_SEED)
    sizes = np.array([len(b) for b in blocks])
    print(f"Blocks: {len(blocks):,} (mean size {sizes.mean():.1f}, min {sizes.min()}, max {sizes.max()})")

    block_lookup = {node: i for i, block in enumerate(blocks) for node in block}
    nodes["network_block"] = nodes["osmid_key"].map(block_lookup)

    df = pd.DataFrame({
        "historical": nodes["dist_to_historical_m"].astype(float).values,
        "center": nodes["dist_to_center_m"].astype(float).values,
        "within": nodes["within_15min_int"].astype(int).values,
        "block": nodes["network_block"].astype(int).values,
    })

    # --- Original (nominal, node-level) estimates -- kept for direct comparison ---
    high = df.loc[df["within"] == 1, "historical"]
    low = df.loc[df["within"] == 0, "historical"]
    observed_difference = low.mean() - high.mean()
    print(f"\nObserved difference (outside 15min - within 15min): {observed_difference:.2f} m")

    original_model = smf.logit("within ~ historical + center", data=df).fit(disp=0)
    beta_hist_original = original_model.params["historical"]
    beta_center_original = original_model.params["center"]
    print(f"Original logit coefficients: historical={beta_hist_original:.6f}, center={beta_center_original:.6f}")

    # --- Network-block bootstrap ---
    rng = np.random.default_rng(RANDOM_SEED)
    block_ids = np.array(sorted(df["block"].unique()))

    boot_diffs, boot_beta_hist, boot_beta_center = [], [], []
    successful = 0

    print(f"\nRunning {N_BOOT} network-block bootstrap replicates...")
    for b in range(N_BOOT):
        sampled = rng.choice(block_ids, size=len(block_ids), replace=True)
        pieces = [df[df["block"] == bid] for bid in sampled]
        boot = pd.concat(pieces, ignore_index=True)

        high_b = boot.loc[boot["within"] == 1, "historical"]
        low_b = boot.loc[boot["within"] == 0, "historical"]
        if len(high_b) == 0 or len(low_b) == 0:
            continue
        boot_diffs.append(low_b.mean() - high_b.mean())

        if boot["within"].nunique() < 2:
            continue
        try:
            model_b = smf.logit("within ~ historical + center", data=boot).fit(disp=0, maxiter=200)
            boot_beta_hist.append(model_b.params["historical"])
            boot_beta_center.append(model_b.params["center"])
            successful += 1
        except Exception:
            continue

        if (b + 1) % 100 == 0:
            print(f"  {b + 1}/{N_BOOT} (successful logit fits: {successful})")

    diff_ci = percentile_ci(boot_diffs)
    beta_hist_ci = percentile_ci(boot_beta_hist)
    beta_center_ci = percentile_ci(boot_beta_center)

    results = {
        "n_blocks": len(blocks),
        "block_target_size": BLOCK_TARGET_SIZE,
        "n_bootstrap_requested": N_BOOT,
        "n_bootstrap_successful_logit": successful,
        "observed_difference_m": round(float(observed_difference), 2),
        "bootstrap_ci_difference_m": [round(diff_ci[0], 2), round(diff_ci[1], 2)],
        "original_logit_coef_historical": beta_hist_original,
        "bootstrap_ci_logit_coef_historical": [beta_hist_ci[0], beta_hist_ci[1]],
        "original_logit_coef_center": beta_center_original,
        "bootstrap_ci_logit_coef_center": [beta_center_ci[0], beta_center_ci[1]],
    }

    print("\n=== NETWORK-BLOCK BOOTSTRAP RESULTS ===")
    print(f"Observed difference: {observed_difference:.2f} m, 95% CI [{diff_ci[0]:.2f}, {diff_ci[1]:.2f}] m")
    print(f"Historical-site logit coef: {beta_hist_original:.6f}, 95% CI [{beta_hist_ci[0]:.6f}, {beta_hist_ci[1]:.6f}]")
    print(f"City-center logit coef: {beta_center_original:.6f}, 95% CI [{beta_center_ci[0]:.6f}, {beta_center_ci[1]:.6f}]")

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w") as f:
        import json
        json.dump(results, f, indent=2)
    print(f"\nSaved: {OUT_JSON}")

    print("\nNOTE: BLOCK_TARGET_SIZE=500 is a starting value, not a fixed rule. Before treating this")
    print("as a final robustness result, re-run at e.g. 250 and 1000 and check the CI/direction hold up --")
    print("that's a sensitivity check on the bootstrap itself, same spirit as threshold_sensitivity.py.")


if __name__ == "__main__":
    main()
