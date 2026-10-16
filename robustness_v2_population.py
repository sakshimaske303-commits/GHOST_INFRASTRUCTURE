"""
robustness_v2_population.py  --  Phase 3, analysis D of DEFENSIBILITY_PLAN.md (fixed specification).

Population weighting with the Zensus 2022 100 m grid (reference date 15 May 2022; licence dl-de/by-2-0,
(c) Statistische Aemter des Bundes und der Laender). The unit of analysis becomes residents, not street nodes.

- Units: Zensus 100 m cells (population > 0) whose centre lies inside the city boundary.
  A cell's access = access of the street-network node nearest to its centre.
  Both service definitions: points only (v1) and all services (polygon centroids), as in robustness_v2.py.
- Outcome: share of residents without 15-min access.
- Tests: population-weighted Cohen's d of distance to nearest historical site; null model with 1,000 random
  site sets drawn uniformly from populated cells (seed 42); population-weighted logit of access on
  historical distance + centre distance + log(1 + residents within 500 m), with the same null model
  applied to its historical-distance coefficient.

Run from the repository root after robustness_v2.py:   python robustness_v2_population.py
Outputs: outputs/robustness/population_results.json, outputs/robustness/null_model_population.png
Do not change the settings after the results are frozen (DEFENSIBILITY_PLAN.md, section 0).
"""
import json
import os
import zipfile

import geopandas as gpd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import osmnx as ox
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.sparse import csr_matrix
from scipy.spatial import cKDTree

from robustness_v2 import CITIES, OUT_DIR, SEED, UTM, accessibility, project_lonlat, xy_of

POP_ZIP = "data/population/Zensus2022_Bevoelkerungszahl.zip"   # official download, read directly (no unzip needed)
POP_MEMBER = "Zensus2022_Bevoelkerungszahl_100m-Gitter.csv"
LAEA = "EPSG:3035"
N_NULL = 1000
RESIDENT_RADIUS_M = 500
FORMULA = "access ~ hist + center + logres"


def weighted_d(dist, access, w):
    lo, hi = access == 0, access == 1
    W1, W2 = w[lo].sum(), w[hi].sum()
    m1, m2 = np.average(dist[lo], weights=w[lo]), np.average(dist[hi], weights=w[hi])
    v1 = (w[lo] * (dist[lo] - m1) ** 2).sum() / (W1 - 1)
    v2 = (w[hi] * (dist[hi] - m2) ** 2).sum() / (W2 - 1)
    sd = np.sqrt(((W1 - 1) * v1 + (W2 - 1) * v2) / (W1 + W2 - 2))
    return float((m1 - m2) / sd), float(m1), float(m2)


def weighted_coef(df, w):
    m = smf.glm(FORMULA, data=df, family=sm.families.Binomial(), freq_weights=w).fit()
    return float(m.params["hist"]), float(m.pvalues["hist"])


def load_cells(boundary_path):
    boundary = gpd.read_file(boundary_path)
    minx, miny, maxx, maxy = boundary.to_crs(LAEA).total_bounds
    with zipfile.ZipFile(POP_ZIP) as z, z.open(POP_MEMBER) as f:
        pop = pd.read_csv(f, sep=";", usecols=["x_mp_100m", "y_mp_100m", "Einwohner"])
    pop = pop[pop["x_mp_100m"].between(minx - 2000, maxx + 2000) & pop["y_mp_100m"].between(miny - 2000, maxy + 2000)]
    pop = pop[pop["Einwohner"] > 0].reset_index(drop=True)
    cells = gpd.GeoDataFrame(pop, geometry=gpd.points_from_xy(pop["x_mp_100m"], pop["y_mp_100m"]), crs=LAEA).to_crs(UTM)
    inside = cells.geometry.within(boundary.to_crs(UTM).geometry.iloc[0]).values
    cells = cells[inside]
    return xy_of(cells), cells["Einwohner"].values.astype(float)


def run_city(name, cfg):
    print(f"\n==================== {name.upper()} (population-weighted) ====================")
    rng = np.random.default_rng(SEED)
    cxy, pop = load_cells(cfg["boundary"])
    print(f"populated 100 m cells inside boundary: {len(cxy):,}  residents: {int(pop.sum()):,}")

    # accessibility on the network, both service definitions (same construction as robustness_v2.py)
    G = ox.load_graphml(cfg["graph"])
    gids = [str(n) for n in G.nodes]
    gpos = {n: i for i, n in enumerate(gids)}
    gxy = project_lonlat([float(G.nodes[n]["x"]) for n in G.nodes], [float(G.nodes[n]["y"]) for n in G.nodes])
    e = pd.DataFrame([(gpos[str(u)], gpos[str(v)], float(d["length"])) for u, v, d in G.edges(data=True)],
                     columns=["u", "v", "L"]).groupby(["u", "v"])["L"].min().reset_index()
    csr = csr_matrix((e["L"].values, (e["u"].values, e["v"].values)), shape=(len(gids), len(gids)))
    services = gpd.read_file(cfg["services"])
    is_point = (services.geometry.geom_type == "Point").values
    pts_xy = xy_of(services[is_point].to_crs(UTM))
    all_xy = xy_of(gpd.GeoDataFrame(geometry=services.to_crs(UTM).geometry.centroid, crs=UTM))
    acc_net = {"points_only": accessibility(gxy, csr, pts_xy), "all_services": accessibility(gxy, csr, all_xy)}

    d_node, nearest = cKDTree(gxy).query(cxy)
    acc = {k: v[nearest] for k, v in acc_net.items()}

    mines = gpd.read_file(cfg["mines"]).to_crs(UTM)
    colonies = gpd.read_file(cfg["colonies"]).to_crs(UTM)
    sites = np.vstack([xy_of(mines), xy_of(colonies)])
    n_sites = len(sites)
    hist = cKDTree(sites).query(cxy)[0]
    c = project_lonlat([cfg["center_lonlat"][0]], [cfg["center_lonlat"][1]])[0]
    center = np.hypot(cxy[:, 0] - c[0], cxy[:, 1] - c[1])
    ctree = cKDTree(cxy)
    logres = np.log1p(np.array([pop[i].sum() for i in ctree.query_ball_point(cxy, RESIDENT_RADIUS_M)]))

    out = {"n_cells": int(len(cxy)), "n_residents": int(pop.sum()),
           "median_cell_to_nearest_node_m": round(float(np.median(d_node)), 1)}
    nulls = {}
    for key, a in acc.items():
        df = pd.DataFrame({"access": a, "hist": hist, "center": center, "logres": logres})
        d_obs, m_lo, m_hi = weighted_d(hist, a, pop)
        coef_obs, p_obs = weighted_coef(df, pop)
        nd, nc = [], []
        for r in range(N_NULL):
            fake = cxy[rng.choice(len(cxy), n_sites, replace=False)]
            h = cKDTree(fake).query(cxy)[0]
            nd.append(weighted_d(h, a, pop)[0])
            nc.append(weighted_coef(df.assign(hist=h), pop)[0])
            if (r + 1) % 250 == 0:
                print(f"  {key}: null model {r + 1}/{N_NULL}")
        nd, nc = np.array(nd), np.array(nc)
        nulls[key] = (nd, d_obs)
        out[key] = {
            "pct_residents_without_access": round(float(pop[a == 0].sum() / pop.sum() * 100), 2),
            "residents_without_access": int(pop[a == 0].sum()),
            "weighted_mean_dist_low_m": round(m_lo, 1), "weighted_mean_dist_high_m": round(m_hi, 1),
            "weighted_cohens_d": round(d_obs, 3),
            "null_d_mean": round(float(nd.mean()), 3),
            "share_null_d_ge_observed": round(float((nd >= d_obs).mean()), 3),
            "coef_hist_given_center_logres": coef_obs, "p_hist_given_center_logres": p_obs,
            "share_null_coef_le_observed": round(float((nc <= coef_obs).mean()), 3),
        }
        print(f"  {key}: no-access residents {out[key]['pct_residents_without_access']}%  d={d_obs:.3f}  "
              f"share null d>=obs={out[key]['share_null_d_ge_observed']}  coef={coef_obs:.4g}  "
              f"share null coef<=obs={out[key]['share_null_coef_le_observed']}")
    return out, nulls


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    results, nulls = {}, {}
    for name, cfg in CITIES.items():
        results[name], nulls[name] = run_city(name, cfg)
    with open(os.path.join(OUT_DIR, "population_results.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {OUT_DIR}/population_results.json")

    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    for j, city in enumerate(CITIES):
        for i, key in enumerate(["points_only", "all_services"]):
            nd, od = nulls[city][key]
            ax = axes[i, j]
            ax.hist(nd, bins=40, color="#7FB8BE", edgecolor="white")
            ax.axvline(od, color="#B65A2A", linewidth=2.5, label=f"real sites: d = {od:.3f}")
            ax.set_title(f"{city.capitalize()}, {key.replace('_', ' ')}: {100 * (nd >= od).mean():.0f}% of random sets reach the real effect", fontsize=10)
            ax.set_xlabel("Population-weighted Cohen's d")
            ax.set_ylabel("Random site sets")
            ax.legend(fontsize=9)
    fig.suptitle("Null model, population-weighted (Zensus 2022, 100 m grid)", fontsize=12)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "null_model_population.png"), dpi=200)
    print(f"Saved: {OUT_DIR}/null_model_population.png")


if __name__ == "__main__":
    main()
