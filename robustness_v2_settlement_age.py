"""
robustness_v2_settlement_age.py  --  Phase 3, analysis E of DEFENSIBILITY_PLAN.md (fixed specification).

Earth-observation test of the paper's policy claim that access gaps sit in newer neighbourhoods.
Data: GHSL GHS-BUILT-S R2023A (JRC / Copernicus Emergency Management Service), built-up surface in m2 per
100 m cell, epochs 1975 and 2020, Mollweide (ESRI:54009), tile R3_C19. GHS-BUILT-S is derived from
Landsat (historical epochs) and Sentinel-2 (recent epochs) imagery.

- Each populated Zensus 2022 cell (as in robustness_v2_population.py) takes the GHSL built-up surface of
  the GHSL cell containing its centre.
- "post-1975" = built-up surface in 1975 < 50% of its 2020 value; otherwise "pre-1975".
  Cells with zero built-up surface in 2020 cannot be classified and are excluded (count reported).
- Reported for both service definitions: share of residents without 15-min access in pre- vs post-1975
  cells, and the population-weighted logit of robustness_v2_population.py with the post-1975 flag added.

Run from the repository root:   python robustness_v2_settlement_age.py
Reads the GHSL zips directly (no unzipping needed). Needs only Pillow for the GeoTIFFs.
Output: outputs/robustness/settlement_age_results.json
"""
import io
import json
import os
import zipfile

import geopandas as gpd
import numpy as np
import osmnx as ox
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from PIL import Image
from scipy.sparse import csr_matrix
from scipy.spatial import cKDTree

from robustness_v2 import CITIES, OUT_DIR, UTM, accessibility, project_lonlat, xy_of
from robustness_v2_population import RESIDENT_RADIUS_M, load_cells

GHSL = {
    "1975": ("data/ghsl/GHS_BUILT_S_E1975_GLOBE_R2023A_54009_100_V1_0_R3_C19.zip",
             "GHS_BUILT_S_E1975_GLOBE_R2023A_54009_100_V1_0_R3_C19.tif"),
    "2020": ("data/ghsl/GHS_BUILT_S_E2020_GLOBE_R2023A_54009_100_V1_0_R3_C19.zip",
             "GHS_BUILT_S_E2020_GLOBE_R2023A_54009_100_V1_0_R3_C19.tif"),
}
MOLLWEIDE = "ESRI:54009"
NODATA = 65535
POST_RATIO = 0.5
FORMULA = "access ~ hist + center + logres + post1975"

Image.MAX_IMAGE_PIXELS = None  # a 10,000 x 10,000 tile is expected


def read_tile(zip_path, member):
    with zipfile.ZipFile(zip_path) as z:
        img = Image.open(io.BytesIO(z.read(member)))
        tie = img.tag_v2[33922]    # ModelTiepointTag: (i, j, k, x, y, z)
        scale = img.tag_v2[33550]  # ModelPixelScaleTag: (sx, sy, sz)
        arr = np.array(img)
    return arr, float(tie[3]), float(tie[4]), float(scale[0]), float(scale[1])


def sample(tile, mx, my):
    arr, x0, y0, sx, sy = tile
    col = np.floor((mx - x0) / sx).astype(int)
    row = np.floor((y0 - my) / sy).astype(int)
    if (col < 0).any() or (row < 0).any() or (col >= arr.shape[1]).any() or (row >= arr.shape[0]).any():
        raise ValueError("Some cells fall outside the GHSL tile - check that tile R3_C19 is the right one.")
    v = arr[row, col].astype(float)
    v[v == NODATA] = np.nan
    return v


def run_city(name, cfg, tiles):
    print(f"\n==================== {name.upper()} (settlement age, GHSL) ====================")
    cxy, pop = load_cells(cfg["boundary"])
    cells_m = gpd.GeoDataFrame(geometry=gpd.points_from_xy(cxy[:, 0], cxy[:, 1]), crs=UTM).to_crs(MOLLWEIDE)
    mx, my = cells_m.geometry.x.values, cells_m.geometry.y.values
    b1975, b2020 = sample(tiles["1975"], mx, my), sample(tiles["2020"], mx, my)
    ok = np.isfinite(b1975) & np.isfinite(b2020) & (b2020 > 0)
    post = (b1975 < POST_RATIO * b2020).astype(int)
    print(f"cells: {len(cxy):,}  classifiable: {ok.sum():,}  post-1975 cells: {post[ok].sum():,}")

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
    nearest = cKDTree(gxy).query(cxy)[1]
    acc = {"points_only": accessibility(gxy, csr, pts_xy)[nearest],
           "all_services": accessibility(gxy, csr, all_xy)[nearest]}

    mines = gpd.read_file(cfg["mines"]).to_crs(UTM)
    colonies = gpd.read_file(cfg["colonies"]).to_crs(UTM)
    hist = cKDTree(np.vstack([xy_of(mines), xy_of(colonies)])).query(cxy)[0]
    c = project_lonlat([cfg["center_lonlat"][0]], [cfg["center_lonlat"][1]])[0]
    center = np.hypot(cxy[:, 0] - c[0], cxy[:, 1] - c[1])
    logres = np.log1p(np.array([pop[i].sum() for i in cKDTree(cxy).query_ball_point(cxy, RESIDENT_RADIUS_M)]))

    w = pop[ok]
    out = {"n_cells": int(len(cxy)), "n_cells_classifiable": int(ok.sum()),
           "n_cells_excluded_no_builtup_2020": int((~ok).sum()),
           "residents_excluded": int(pop[~ok].sum()),
           "pct_residents_in_post1975_cells": round(float(w[post[ok] == 1].sum() / w.sum() * 100), 2)}
    for key, a in acc.items():
        a_ok, p_ok = a[ok], post[ok]
        res = {}
        for label, m in (("pre1975", p_ok == 0), ("post1975", p_ok == 1)):
            res[f"residents_{label}"] = int(w[m].sum())
            res[f"pct_without_access_{label}"] = round(float(w[m & (a_ok == 0)].sum() / w[m].sum() * 100), 2) if w[m].sum() else None
        df = pd.DataFrame({"access": a_ok, "hist": hist[ok], "center": center[ok], "logres": logres[ok], "post1975": p_ok})
        fit = smf.glm(FORMULA, data=df, family=sm.families.Binomial(), freq_weights=w).fit()
        for term in ("post1975", "hist"):
            res[f"coef_{term}"] = float(fit.params[term])
            res[f"p_{term}"] = float(fit.pvalues[term])
        res["odds_ratio_post1975"] = round(float(np.exp(fit.params["post1975"])), 3)
        out[key] = res
        print(f"  {key}: without access pre-1975 {res['pct_without_access_pre1975']}% vs post-1975 "
              f"{res['pct_without_access_post1975']}%  |  OR(post1975)={res['odds_ratio_post1975']} "
              f"p={res['p_post1975']:.3g}  |  hist coef={res['coef_hist']:.4g} p={res['p_hist']:.3g}")
    return out


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tiles = {y: read_tile(*GHSL[y]) for y in GHSL}
    results = {name: run_city(name, cfg, tiles) for name, cfg in CITIES.items()}
    with open(os.path.join(OUT_DIR, "settlement_age_results.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {OUT_DIR}/settlement_age_results.json")


if __name__ == "__main__":
    main()
