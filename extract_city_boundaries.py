"""Extracts the Bochum and Essen city boundaries from your own GADM v4.1 download.

GADM's licence does not allow redistribution, so the boundary files are not stored in the repository.
1. Download the Germany GeoPackage (gadm41_DEU.gpkg) from https://gadm.org/download_country.html
2. Put it in data/boundaries/
3. Run from the repository root:  python extract_city_boundaries.py

Writes data/boundaries/bochum_city.gpkg and data/boundaries/essen_city.gpkg (GADM level 4, by GID_4).
The GID_4 codes are the ones used for all published results.
"""
import os

import geopandas as gpd

GADM = os.path.join("data", "boundaries", "gadm41_DEU.gpkg")
CITIES = {"bochum": "DEU.10.2.1.1_1", "essen": "DEU.10.12.1.1_1"}

if not os.path.exists(GADM):
    raise SystemExit(f"{GADM} not found. Download gadm41_DEU.gpkg from https://gadm.org first.")

level4 = gpd.read_file(GADM, layer="ADM_ADM_4")
for city, gid in CITIES.items():
    sel = level4[level4["GID_4"] == gid]
    if len(sel) != 1:
        raise SystemExit(f"Expected exactly 1 feature for {city} ({gid}), found {len(sel)}.")
    out = os.path.join("data", "boundaries", f"{city}_city.gpkg")
    sel.to_file(out, layer=f"{city}_city", driver="GPKG")
    print(f"Saved {out}: {sel.iloc[0]['NAME_4']} ({gid})")
