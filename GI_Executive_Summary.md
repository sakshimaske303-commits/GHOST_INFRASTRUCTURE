# GHOST INFRASTRUCTURE

### Does 19th-century coal-mining geography still shape who can walk to everyday services? A null-model test in Bochum and Essen

Executive Summary · v2.0 · Sakshi D. Maske

## The problem

Bochum and Essen, in Germany's Ruhr region, grew around coal mines and workers' housing colonies. It is often assumed that this industrial past still decides which neighbourhoods are well served today. If true, it would matter for where cities invest to make everyday services reachable on foot (the "15-minute city").

## The question

Is present-day 15-minute walking access in Bochum and Essen associated with the location of historical coal-mining sites, beyond what general urban form explains? And if not, what does distinguish the places where access is missing?

## Data and method

- **Historical sites:** 13 coal mines and 4 worker colonies in Bochum, and 4 mines and 4 colonies in Essen, compiled from documentary sources as points.
- **Accessibility:** the full OpenStreetMap pedestrian networks (69,393 and 72,027 nodes). A location has access if an essential service is within 1,125 m of walking distance (15 minutes). Two service definitions are used: point-mapped services only, and all mapped services.
- **People:** the Zensus 2022 100 m population grid, so that access is counted for residents, not street segments.
- **Settlement age (Earth observation):** GHSL built-up surface for 1975 and 2020, derived from Landsat and Sentinel-2.
- **Key test:** a null model. The real sites are compared with 1,000 random sets of locations in the same city. The decision rule was fixed in advance: the legacy claim needs the real sites to beat 95% of random sets, for both service definitions and for residents.

## Findings

| | Bochum | Essen |
|---|---|---|
| Naive effect: street nodes without access are farther from the sites (Cohen's d) | 0.589 | 0.338 |
| Random site sets reaching that effect (street nodes) | 22.5% | 83.1% |
| Random site sets reaching the effect, residents, all services | 10.6% | 41.3% |
| Residents without 15-min access (all services) | 2.1% | 0.69% |
| … in areas built up before 1975 / after 1975 (all services) | 1.7% / **5.1%** | 0.35% / **2.9%** |

1. **No mining-specific legacy.** The naive pattern is real, but random locations in the built-up city produce it too. For residents, the real sites are not distinguishable from random locations in either city. The apparent legacy is general urban form: access is good almost everywhere inside the city and weaker at its low-density edge.
2. **Access gaps are small for people.** Most street nodes without access lie in forests, fields and river valleys where few people live.
3. **Gaps sit in newer development.** Residents of areas first built up after 1975 are two to eight times more likely to lack 15-minute access, in both cities and under both service definitions.

## Why it matters

Legacy claims about cities are easy to make with a simple correlation and hard to defend. This project shows that a random-location null model and a population-based outcome can overturn a convincing-looking result. It also shows where planning attention belongs: in post-1975 peripheral development, not in the historical mining districts as such.

## Limitations

The study uses a small set of large, well-documented sites as points, a binary access measure, and straight-line distances to sites. It covers two cities at one point in time and includes no socioeconomic data. The settlement-age result is a consistent association, not a causal effect.

## Version note

Version 1.1 of this project reported the naive comparison as evidence of a "path dependency of centrality". An internal review found that this had not been tested against random locations, that only 248 of 786 service features had been used, and that a Local Moran's I result offered as corroboration was mechanically guaranteed. Version 2.0 corrects these points and reports the tested result.

---

GitHub: [github.com/sakshimaske303-commits/GHOST_INFRASTRUCTURE](https://github.com/sakshimaske303-commits/GHOST_INFRASTRUCTURE) · Live dashboard: [ghostinfrastructure-areytvp4x8ofu6l5tosj2z.streamlit.app](https://ghostinfrastructure-areytvp4x8ofu6l5tosj2z.streamlit.app)

**Sakshi D. Maske**, Independent Geospatial Researcher
