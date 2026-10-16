"""
robustness_v2.py  --  Phase 2 analyses A, B, C of DEFENSIBILITY_PLAN.md (fixed specification).

A. Null model: 1,000 random sets of n sites (17 Bochum / 8 Essen) drawn from street-network nodes
   (the built-up-area proxy). Percentile of the observed Cohen's d and of the logit coefficient for
   historical-site distance controlling for city-center distance.
B. Urban-form controls: logit of access on historical distance + center distance + distance to the
   city boundary + log(1 + street nodes within 500 m), with the same null model for that coefficient;
   2 km grid-cluster bootstrap (999 resamples) of the raw distance difference; leave-one-site-out d;
   share of nodes with access within 750 m of each site.
C. Service definition: accessibility recomputed with ALL service features (polygons represented by
   their centroid in EPSG:32632) vs points only (the original v1 definition).

Run from the repository root:   python robustness_v2.py
Outputs: outputs/robustness/robustness_results.json, outputs/robustness/null_model.png
Runtime: about 15-30 minutes (mostly the 1,000-draw logit null models).
Do not change the settings below after the results are frozen (see DEFENSIBILITY_PLAN.md, section 0).
"""
import json
import os

import geopandas as gpd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import osmnx as ox
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from scipy.spatial import cKDTree

UTM = "EPSG:32632"
SEED = 42
N_NULL = 1000
N_BOOT = 999
GRID_M = 2000
DENSITY_RADIUS_M = 500
SITE_RADIUS_M = 750
MAX_DIST_M = 1125  # 15 min at 75 m/min, as in v1
OUT_DIR = os.path.join("outputs", "robustness")

CITIES = {
    "bochum": {
        "nodes": "data/accessibility/bochum_accessibility_with_distance.gpkg",
        "graph": "data/osm_network/bochum_walk_network.graphml",
        "services": "data/osm_network/bochum_essential_services.gpkg",
        "mines": "data/historical_georeferenced/bochum_coal_mines.gpkg",
        "colonies": "data/historical_georeferenced/bochum_zechensiedlungen.gpkg",
        "boundary": "data/boundaries/bochum_city.gpkg",
        "center_lonlat": (7.2162, 51.4818),  # same point as v1 (Rathaus area); see paper section 7
    },
    "essen": {
        "nodes": "data/accessibility/essen_accessibility_with_distance.gpkg",
        "graph": "data/osm_network/essen_walk_network.graphml",
        "services": "data/osm_network/essen_essential_services.gpkg",
        "mines": "data/historical_georeferenced/essen_coal_mines.gpkg",
        "colonies": "data/historical_georeferenced/essen_zechensiedlungen.gpkg",
        "boundary": "data/boundaries/essen_city.gpkg",
        "center_lonlat": (7.0134, 51.4517),  # Essen Hauptbahnhof, as in v1
    },
}


# ------------------------------------------------------------------ helpers
def xy_of(gdf):
    return np.column_stack([gdf.geometry.x.values, gdf.geometry.y.values])


def project_lonlat(lon, lat):
    g = gpd.GeoDataFrame(geometry=gpd.points_from_xy(lon, lat), crs="EPSG:4326").to_crs(UTM)
    return xy_of(g)


def cohens_d(dist, access):
    low, high = dist[access == 0], dist[access == 1]
    n1, n2 = len(low), len(high)
    sd = np.sqrt(((n1 - 1) * low.var(ddof=1) + (n2 - 1) * high.var(ddof=1)) / (n1 + n2 - 2))
    return float((low.mean() - high.mean()) / sd)


def logit_coef(df, formula, term):
    m = smf.logit(formula, data=df).fit(disp=0)
    return float(m.params[term]), float(m.pvalues[term])


def percentile_of(obs, null, more_extreme="greater"):
    null = np.asarray(null)
    if more_extreme == "greater":
        return float((null < obs).mean() * 100), float((null >= obs).mean())
    return float((null > obs).mean() * 100), float((null <= obs).mean())


def accessibility(graph_nodes_xy, csr, service_xy):
    src = np.unique(cKDTree(graph_nodes_xy).query(service_xy)[1])
    dist = dijkstra(csr, directed=True, indices=src, min_only=True, limit=MAX_DIST_M + 1e-6)
    return (dist <= MAX_DIST_M).astype(int)


# ------------------------------------------------------------------ per-city analysis
def run_city(name, cfg):
    print(f"\n==================== {name.upper()} ====================")
    rng = np.random.default_rng(SEED)

    nodes = gpd.read_file(cfg["nodes"]).to_crs(UTM)
    nodes["osmid_key"] = nodes["osmid"].astype(str)
    xy = xy_of(nodes)
    access_v1 = nodes["within_15min"].astype(int).values

    mines = gpd.read_file(cfg["mines"]).to_crs(UTM)
    colonies = gpd.read_file(cfg["colonies"]).to_crs(UTM)
    sites = np.vstack([xy_of(mines), xy_of(colonies)])
    site_names = list(mines["mine_name"]) + list(colonies["settlement_name"])
    n_sites = len(sites)
    dist_hist = cKDTree(sites).query(xy)[0]

    cxy = project_lonlat([cfg["center_lonlat"][0]], [cfg["center_lonlat"][1]])[0]
    dist_center = np.hypot(xy[:, 0] - cxy[0], xy[:, 1] - cxy[1])

    boundary = gpd.read_file(cfg["boundary"]).to_crs(UTM).geometry.iloc[0].boundary
    dist_boundary = gpd.GeoSeries(gpd.points_from_xy(xy[:, 0], xy[:, 1]), crs=UTM).distance(boundary).values
    density = np.array([len(i) for i in cKDTree(xy).query_ball_point(xy, DENSITY_RADIUS_M)])
    log_density = np.log1p(density)

    base = pd.DataFrame({"access": access_v1, "hist": dist_hist, "center": dist_center,
                         "boundary": dist_boundary, "logdens": log_density})
    f_center = "access ~ hist + center"
    f_full = "access ~ hist + center + boundary + logdens"

    # ---- observed (v1 outcome)
    obs_d = cohens_d(dist_hist, access_v1)
    obs_coef_c, obs_p_c = logit_coef(base, f_center, "hist")
    obs_coef_f, obs_p_f = logit_coef(base, f_full, "hist")
    print(f"observed d={obs_d:.3f}  coef|center={obs_coef_c:.6g}  coef|full={obs_coef_f:.6g}")

    # ---- A + B null model: random sites from street-network nodes
    null_d, null_c, null_f = [], [], []
    for r in range(N_NULL):
        fake = xy[rng.choice(len(xy), n_sites, replace=False)]
        dh = cKDTree(fake).query(xy)[0]
        null_d.append(cohens_d(dh, access_v1))
        df = base.assign(hist=dh)
        null_c.append(logit_coef(df, f_center, "hist")[0])
        null_f.append(logit_coef(df, f_full, "hist")[0])
        if (r + 1) % 100 == 0:
            print(f"  null model {r + 1}/{N_NULL}")
    pct_d, p_d = percentile_of(obs_d, null_d, "greater")
    pct_c, p_c = percentile_of(obs_coef_c, null_c, "less")
    pct_f, p_f = percentile_of(obs_coef_f, null_f, "less")

    # ---- B: 2 km grid-cluster bootstrap of the raw distance difference
    cell = (np.floor(xy[:, 0] / GRID_M).astype(np.int64) * 1_000_000 + np.floor(xy[:, 1] / GRID_M).astype(np.int64))
    _, inv = np.unique(cell, return_inverse=True)
    groups = [np.where(inv == k)[0] for k in range(inv.max() + 1)]
    boot = []
    for _ in range(N_BOOT):
        idx = np.concatenate([groups[k] for k in rng.integers(0, len(groups), len(groups))])
        a, d = access_v1[idx], dist_hist[idx]
        boot.append(d[a == 0].mean() - d[a == 1].mean())
    obs_diff = float(dist_hist[access_v1 == 0].mean() - dist_hist[access_v1 == 1].mean())

    # ---- B: leave-one-site-out and local coverage per site
    loso = [cohens_d(cKDTree(np.delete(sites, k, 0)).query(xy)[0], access_v1) for k in range(n_sites)]
    tree = cKDTree(xy)
    per_site = {}
    for nm, s in zip(site_names, sites):
        ii = tree.query_ball_point(s, SITE_RADIUS_M)
        per_site[nm] = {"n_nodes_within_750m": len(ii),
                        "pct_with_access_within_750m": round(float(access_v1[ii].mean() * 100), 1) if ii else None}

    # ---- C: service definition (points only vs all features)
    G = ox.load_graphml(cfg["graph"])
    gids = [str(n) for n in G.nodes]
    gpos = {n: i for i, n in enumerate(gids)}
    gxy = project_lonlat([float(G.nodes[n]["x"]) for n in G.nodes], [float(G.nodes[n]["y"]) for n in G.nodes])
    e = pd.DataFrame([(gpos[str(u)], gpos[str(v)], float(d["length"])) for u, v, d in G.edges(data=True)],
                     columns=["u", "v", "L"]).groupby(["u", "v"])["L"].min().reset_index()
    csr = csr_matrix((e["L"].values, (e["u"].values, e["v"].values)), shape=(len(gids), len(gids)))
    order = np.array([gpos[k] for k in nodes["osmid_key"]])

    services = gpd.read_file(cfg["services"])
    is_point = (services.geometry.geom_type == "Point").values
    pts_xy = xy_of(services[is_point].to_crs(UTM))
    services_utm = services.to_crs(UTM)
    all_xy = xy_of(gpd.GeoDataFrame(geometry=services_utm.geometry.centroid, crs=UTM))  # polygon -> centroid

    acc_points = accessibility(gxy, csr, pts_xy)[order]
    acc_all = accessibility(gxy, csr, all_xy)[order]
    match_v1 = float((acc_points == access_v1).mean())
    print(f"points-only recompute matches stored v1 flag for {100 * match_v1:.2f}% of nodes")

    def summary(acc):
        low, high = dist_hist[acc == 0], dist_hist[acc == 1]
        t, p = stats.ttest_ind(low, high, equal_var=False)
        return {"coverage_pct": round(float(acc.mean() * 100), 2), "n_low": int((acc == 0).sum()),
                "mean_dist_low_m": round(float(low.mean()), 1), "mean_dist_high_m": round(float(high.mean()), 1),
                "welch_t": round(float(t), 3), "cohens_d": round(cohens_d(dist_hist, acc), 3)}

    null_d_all = []
    for _ in range(N_NULL):
        fake = xy[rng.choice(len(xy), n_sites, replace=False)]
        null_d_all.append(cohens_d(cKDTree(fake).query(xy)[0], acc_all))
    sum_all = summary(acc_all)
    pct_d_all, p_d_all = percentile_of(sum_all["cohens_d"], null_d_all, "greater")

    res = {
        "n_nodes": int(len(xy)), "n_sites": int(n_sites),
        "A_null_model": {
            "draws": N_NULL, "site_pool": "street-network nodes",
            "observed_cohens_d": round(obs_d, 3),
            "null_d_mean": round(float(np.mean(null_d)), 3),
            "null_d_5_95": [round(float(np.percentile(null_d, 5)), 3), round(float(np.percentile(null_d, 95)), 3)],
            "observed_d_percentile": round(pct_d, 1), "share_null_d_ge_observed": round(p_d, 3),
            "share_null_d_positive": round(float((np.array(null_d) > 0).mean()), 3),
            "observed_coef_hist_given_center": obs_coef_c, "observed_p_hist_given_center": obs_p_c,
            "share_null_coef_le_observed": round(p_c, 3),
        },
        "B_urban_form": {
            "observed_coef_hist_full_model": obs_coef_f, "observed_p_hist_full_model": obs_p_f,
            "share_null_coef_full_le_observed": round(p_f, 3),
            "observed_difference_m": round(obs_diff, 1),
            "grid_bootstrap_cell_m": GRID_M, "n_cells": len(groups),
            "grid_bootstrap_ci95_m": [round(float(np.percentile(boot, 2.5)), 1), round(float(np.percentile(boot, 97.5)), 1)],
            "leave_one_site_out_d_min": round(float(min(loso)), 3), "leave_one_site_out_d_max": round(float(max(loso)), 3),
            "median_dist_boundary_low_vs_high_m": [round(float(np.median(dist_boundary[access_v1 == 0]))),
                                                   round(float(np.median(dist_boundary[access_v1 == 1])))],
            "median_nodes_within_500m_low_vs_high": [int(np.median(density[access_v1 == 0])),
                                                     int(np.median(density[access_v1 == 1]))],
            "per_site_local_access": per_site,
        },
        "C_service_definition": {
            "n_service_features": int(len(services)), "n_point_features": int(is_point.sum()),
            "points_only_recompute_match_v1_share": round(match_v1, 4),
            "points_only": summary(acc_points),
            "all_features": dict(sum_all, null_d_mean=round(float(np.mean(null_d_all)), 3),
                                 observed_d_percentile=round(pct_d_all, 1),
                                 share_null_d_ge_observed=round(p_d_all, 3)),
        },
    }
    return res, np.array(null_d), obs_d


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    results, nulls = {}, {}
    for name, cfg in CITIES.items():
        results[name], nd, od = run_city(name, cfg)
        nulls[name] = (nd, od)

    with open(os.path.join(OUT_DIR, "robustness_results.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {OUT_DIR}/robustness_results.json")

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    for ax, (name, (nd, od)) in zip(axes, nulls.items()):
        ax.hist(nd, bins=40, color="#7FB8BE", edgecolor="white")
        ax.axvline(od, color="#B65A2A", linewidth=2.5, label=f"real sites: d = {od:.3f}")
        share = (nd >= od).mean()
        ax.set_title(f"{name.capitalize()}: Cohen's d for {N_NULL} random site sets\n"
                     f"{100 * share:.0f}% of random sets reach the real effect", fontsize=11)
        ax.set_xlabel("Cohen's d (distance to nearest site, low vs high access nodes)")
        ax.set_ylabel("Number of random site sets")
        ax.legend()
    fig.suptitle("Null model: are real mining sites different from random locations in the street network?", fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "null_model.png"), dpi=200)
    print(f"Saved: {OUT_DIR}/null_model.png")

    for name, r in results.items():
        a, b, c = r["A_null_model"], r["B_urban_form"], r["C_service_definition"]
        print(f"\n--- {name} ---")
        print(f"A  observed d={a['observed_cohens_d']}  null mean={a['null_d_mean']}  share null >= observed={a['share_null_d_ge_observed']}")
        print(f"A  coef|center share null <= observed={a['share_null_coef_le_observed']}")
        print(f"B  coef|full={b['observed_coef_hist_full_model']:.4g}  share null <= observed={b['share_null_coef_full_le_observed']}")
        print(f"B  2km bootstrap CI={b['grid_bootstrap_ci95_m']}  LOSO d=[{b['leave_one_site_out_d_min']}, {b['leave_one_site_out_d_max']}]")
        print(f"C  points: {c['points_only']}")
        print(f"C  all:    {c['all_features']}")


if __name__ == "__main__":
    main()
