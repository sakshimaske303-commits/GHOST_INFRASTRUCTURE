# GHOST INFRASTRUCTURE

### How 19th-Century Coal Geography Still Shapes Who Gets a "15-Minute Life" Today — Now Tested Across Two Cities and Three Thresholds

Executive Summary · v1.1.0 · DOI: [10.5281/zenodo.21761320](https://doi.org/10.5281/zenodo.21761320) · Sakshi D. Maske

## Project Overview

At first sight these seemed like data anomalies — markers for both mines and colonies, that seemed to overlap in both length and position, which I just couldn't account for — in the cartographic outputs. Both had to be verified separately and retracked using precise distance estimations, but both were real data from old geographies as opposed to pipeline mistakes and were situated a few hundred metres away. This audit was an element of a larger project, to see whether Bochum's 19th-century history of mining and its associated colonies of workers' houses, which shut down in 1974, had left its mark on who had "real access" to walkable daily services today. In addition, beyond the headline reversal (historical industrial cores (HICs) are found to predict better, not worse, present-day accessibility levels), I extended the findings in two robustness directions: a more strict walking threshold and a more liberal walking threshold, and independently retracing the whole methodology on a second city (Essen) from the Ruhr Valley, with historical sources of its own. That replication was also genuinely mixed, in the sense that the raw reversed effect and the spatial-clustering result were both upheld in Essen, but the confound-independence result was not — I report that specific claim as “Bochum-specific” rather than general. It's one where the unexpected finding was tested against its most obvious confound (reversing the test example), was supported by an independent statistic that wasn't localized, was tested across multiple thresholds, and was tested across multiple cities, and it was checked for rendering artifacts by itself.

## The Question

More than 50 years since coal mining ended in Bochum in 1974, how long does that 19th-century coal-mining past leave a footprint in the city on who gets a real 15-minute city, i.e. walking distance to essential services, and who does not, and how much? After all, the modern morphology of the city of Bochum was not planned for the benefit of humans but for coal extraction and steel production — railways, highways and blocks of residential houses for workers were installed to cater 19th-century industry.

## The Method

Proximity to the historical sites was statistically compared with the accessibility of these sites at the present day with a Welch's t-test, followed by a correlation and logistic regression against the most obvious potential confounder, proximity to city centres, and then checked with a complementary Local Moran's I (LMI) spatial-clustering analysis. It was based on a real 15-minute accessibility model which was created on top of the complete 13 historical coal mines, 4 worker-housing colonies which were digitized from Mindat.org and from German heritage archives and the whole 69,393 pedestrian nodes (OSMnx) in Bochum.

## The Finding

Within the range of accessibility zones, the low-accessibility zones were, on average, actually further from the historical industrial areas of cities than the high-accessibility zones, a medium-to-large, highly significant effect that in Bochum held independently of distance to the city center. That is directly opposed to the original hypothesis, which expected historical industrial sites to predict present-day neglect instead. (As the "Is it true in a second city?" section below reports, the raw reversed effect itself replicates in Essen — the city-center independence does not.)

| Metric | Value |
|---|---|
| Low-accessibility nodes — avg. distance to site | 1,984 m (n = 9,858) |
| High-accessibility nodes — avg. distance to site | 1,450 m (n = 59,535) |
| Welch's t-test | t = 42.887, p < 0.00001 (Cohen's d = 0.589) |
| Confound check — distance-to-center correlation | r = 0.063 (genuinely independent) |
| Logistic regression — controlling for center | coefficient = -0.0005, p < 0.001 |
| Local Moran's I check | 97.1% of the nodes with low access were in a significant cold-spot cluster |
| Network-block bootstrap (spatial-dependence check) | 95% CI [247.24m, 873.73m] for the distance difference — excludes zero |

The interpretation is a “path dependency of centrality”, rather than the originally proposed “path dependency of neglect” — 19th century industrial centres developed by necessity around the mine sites and colonies of the population, and this has resulted in a high street density and level of services that appear to be present in the modern day.

## Two Robustness Extensions — NEW

Are 15 minutes a magic number?
The inverse pattern prevails — and intensifies — after the entire pipeline was re-run on the shortened 10 minute cutoff (750m) and the extended 20 minute cutoff (1,500m) – and that’s at every threshold tested (Cohen's d = 0.413 at 10-min, 0.589 at 15-min, 0.661 at 20-min).

Is it true in a second city?
The mixed result is not only reported for the part that confirms the original city's result, but for the whole result, also the part that did not replicate, by including it. Behind this refers also the raw reversed effect, described also in the other article, and the spatial-clustering result as obtained in Essen (with 4 mines and 4 worker colonies, 72,027-node network; 95.5% of the nodes with low access were in cold-spot clusters; t = 24.731, p < 0.00001, Cohen's d = 0.338). The "independent of city center" claim does not hold in Essen: here, the historical-site distance is moderately linked to the city-center distance (r = 0.405 vs. Bochum's r = 0.063); it thus remains to be proven in other regions of the Ruhr Valley.

## Validation & Robustness Checklist

- Full network-based accessibility model - 69,393 nodes in Bochum, 72,027 nodes in Essen - NOT a straight line radius!
- There was an obvious city-center proximity that has been explicitly tested (correlation r = 0.063 in Bochum).
- Logistic regression also finds independence in Bochum (with center distance, p < 0.001)
- In both cities, a complementary check using Local Moran's I spatial clustering (k=8, 999 permutations in Bochum, 99 in Essen).
- Main t-test/regression result also tested with a network-block bootstrap (999 resamples of 2,611 contiguous street-network chunks, grown toward a 500-node target but averaging roughly 27 nodes each because the pedestrian network fragments into many small components — instead of resampling individual nodes) — the 95% confidence interval stays clear of zero, and re-running the same bootstrap at 250-node and 1,000-node targets keeps that interval clear of zero at every target size tested.
- Effect size was reported rather than simply significance (Cohen's d = 0.589 Bochum, 0.338 Essen)
- Effect held — and increased — at all 3 cut points (10, 15, 20 minutes of walking).
- Independently replicated in another city (Essen), with the part that did not fully replicate also reported honestly.
- No cover-up of reversed-hypothesis result (reported honestly throughout)

## Honest Limitation

The connection across the time series is correlational, not causal: The confound check eliminates the confounding of being in the city center but doesn't eliminate all other possible confounding factor analyses. Unlike Bochum's 17-site dataset, Essen's 8-site subset mining register is not a significant proportion of the historical mining register in that city, and mapping of historical mine and colony site locations took place from secondary sources, with most locations sourced from Mindat.org, KuLaDig, Wikipedia, and regional heritage archives, rather than primary survey records. This finding here is now confirmed in Bochum, and, separately, replicated in a second Ruhr Valley city, Essen, but the more narrow claim that the effect is found irrespective of the proximity to the city center does not appear in Essen alone or in the context of a larger set of Essen results. A network-block bootstrap (see the checklist above and `GI_Research_Paper.md` Section 7) was later added specifically to test whether treating the 69,393 street nodes as independent observations was inflating the confidence in this result — it does not: the 95% confidence interval for the observed distance difference stays well clear of zero even when whole connected chunks of the street network are resampled instead of single nodes.

## Real-World Relevance

Most of the cities in Europe share Bochum's and Essen's industrial-core form established in the 19th century, and accessibility investment mis-directed on an intuitive, but flawed, idea is a real and preventable expense. Former industrial areas are typically viewed as the most deprived places in cities and towns, with poor connectivity and access to services. This project tested that assumption directly, on real network data, for two cities and three accessibility thresholds, and the assumption did not win — in every case, the raw effect and the spatial clustering agreed with each other and pointed the opposite way.

---

GitHub: [github.com/sakshimaske303-commits/GHOST_INFRASTRUCTURE](https://github.com/sakshimaske303-commits/GHOST_INFRASTRUCTURE) · Live Dashboard: [ghostinfrastructure-areytvp4x8ofu6l5tosj2z.streamlit.app](https://ghostinfrastructure-areytvp4x8ofu6l5tosj2z.streamlit.app) · Zenodo DOI: [10.5281/zenodo.21761320](https://doi.org/10.5281/zenodo.21761320)

**Sakshi D. Maske** — Independent Geospatial Researcher