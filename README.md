# GHOST INFRASTRUCTURE

**Does 19th-century coal-mining geography still shape who can walk to everyday services? A null-model test in Bochum and Essen, Germany (v2.0)**

[![EarthArXiv](https://img.shields.io/badge/EarthArXiv-Preprint-B7410E.svg)](https://eartharxiv.org/repository/view/14809/) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21761320.svg)](https://doi.org/10.5281/zenodo.21761320)

**Live dashboard:** `https://ghostinfrastructure-areytvp4x8ofu6l5tosj2z.streamlit.app/`

---

## In one paragraph

The Ruhr cities of Bochum and Essen grew around coal mines and workers' housing colonies, and it is often assumed that this industrial past still shapes which neighbourhoods are well served. A naive comparison seems to confirm a "legacy": street nodes without 15-minute walking access to essential services lie farther from the old mining sites (Cohen's d = 0.589 in Bochum). This project tests that claim properly, and it does not hold. A null model of 1,000 random site sets shows that random locations in the built-up city produce the same pattern (22.5% of random sets reach the real effect in Bochum, 83.1% in Essen). Once access is counted for residents (Zensus 2022 100 m grid), the real sites are not distinguishable from random locations in either city. What does distinguish the access gaps is settlement age: residents of areas first built up after 1975 (GHSL, satellite-derived) are two to eight times more likely to lack access. With all mapped services counted, only 2.1% of Bochum's and 0.69% of Essen's residents lack 15-minute access.

## Research question

*Is present-day 15-minute walking access in Bochum and Essen associated with the location of historical coal-mining sites, beyond what general urban form explains, and, if not, what does distinguish the places where access is missing?*

| Hypothesis | Result |
|---|---|
| **H1** Industrial legacy: real mine and colony sites beat at least 95% of random site sets, for both service definitions and for residents | **Not supported** in either city: the signal is explained by general urban form |
| **H2** Settlement age: residents of post-1975 development more often lack access | **Supported** in both cities and under both service definitions |

## Data

| Dataset | Use | Source / licence |
|---|---|---|
| 13 coal mines + 4 worker colonies (Bochum); 4 + 4 (Essen) | Historical sites (points) | Mindat.org, Wikipedia, Route Industriekultur, ruhr-bauten.de, KuLaDig; compiled by the author |
| OSM pedestrian network + essential services | Network accessibility (1,125 m, 15 min) | © OpenStreetMap contributors, ODbL; extracts of 18 Jul 2026 (Bochum) and 13 Aug 2026 (Essen) |
| Zensus 2022, 100 m population grid | Residents per cell | © Statistische Ämter des Bundes und der Länder, dl-de/by-2-0 |
| GHSL GHS-BUILT-S R2023A, 1975 and 2020, tile R3_C19 | Settlement age (Earth observation: Landsat + Sentinel-2) | © European Union, JRC; reuse with acknowledgement |
| GADM v4.1 level 4 | City boundaries | GADM; **not redistributed** (see below) |

## Method

1. **Accessibility:** a node has access if a service is within 1,125 m of network distance. Two service definitions: point-mapped features only (v1), and all features with polygon centroids.
2. **Naive comparison** (v1): Welch's t-test, Cohen's d, and a logit with distance to the centre.
3. **Null model:** 1,000 random site sets drawn from street-network nodes (seed 42).
4. **Urban-form controls:** distance to the city boundary, local street density, a 2 km grid-cluster bootstrap, and leave-one-site-out.
5. **Population weighting:** Zensus cells as the unit, with a null model drawn from populated cells.
6. **Settlement age:** a cell is post-1975 if its GHSL built-up surface in 1975 was below 50% of its 2020 value.

The specification and the decision rule were fixed in advance; see [`DEFENSIBILITY_PLAN.md`](./DEFENSIBILITY_PLAN.md).

## Reproduce

```bash
pip install -r requirements.txt
python extract_city_boundaries.py      # needs your own GADM download, see below
python robustness_v2.py                # A-C: null model, urban form, service definition (15-30 min)
python robustness_v2_population.py     # D: population weighting
python robustness_v2_settlement_age.py # E: settlement age (GHSL)
python plot_settlement_age.py          # Figure 6
cd dashboard && streamlit run app.py
```

Data you have to add yourself (not in the repository):

- **GADM:** download `gadm41_DEU.gpkg` from https://gadm.org and place it in `data/boundaries/`. GADM's licence does not allow redistribution, so the city boundaries are extracted locally by `extract_city_boundaries.py`.
- **Zensus 2022:** the repository includes the official zip `data/population/Zensus2022_Bevoelkerungszahl.zip`. The scripts read it directly; do not commit the unzipped 153 MB CSV.
- **GHSL:** `data/ghsl/` contains the two official tile zips for R3_C19. The scripts read them directly.

All frozen results are in `outputs/robustness/`.

## Repository structure

```text
GHOST_INFRASTRUCTURE/
├── GI_Research_Paper.md             # The paper (v2.0)
├── GI_Executive_Summary.md          # Two-page summary
├── GI_Development_Log.md            # Full development history, including the v2 review
├── DEFENSIBILITY_PLAN.md            # Fixed analysis spec, decision rule and stop line for v2.0
├── robustness_v2*.py                # v2 analyses (A-E)
├── plot_settlement_age.py           # Figure 6
├── extract_city_boundaries.py       # Boundaries from your own GADM download
├── outputs/robustness/              # Frozen v2 results (JSON) and figures
├── maps/                            # Static map scripts (Bochum + Essen)
├── dashboard/                       # Streamlit dashboard
├── data/                            # Historical sites, OSM network/services, Zensus zip, GHSL zips
└── (v1 scripts)                     # compute_isochrones.py, spatial_correlation_test.py, test_confound.py,
                                     # threshold_sensitivity.py, run_essen_pipeline.py, spatial_clustering_lisa*.py,
                                     # network_block_bootstrap*.py: kept for the record; see paper Section 9
```

## What changed from v1.1

v1.1 reported the naive comparison as evidence of a "path dependency of centrality". An internal forensic review (October 2026) found that this claim had not been tested against random locations. It also found that only 248 of the 786 OSM service features had been used, and that the Local Moran's I "corroboration" was mechanically guaranteed by the construction of the variable. v2.0 adds the null model, population and settlement-age data, and reports the result as it is. Details: paper Section 9 and `GI_Development_Log.md`, Entries 17–18.

## Licence

Code: MIT. Text, figures and the compiled historical-site data: CC BY 4.0. Third-party data keep their own licences (table above). See [`LICENSE`](./LICENSE). Citation metadata: [`CITATION.cff`](./CITATION.cff).

## Author

**Sakshi D. Maske**, Independent Geospatial Researcher
