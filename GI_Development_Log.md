# GHOST INFRASTRUCTURE

## Mapping How 19th-Century Coal and Steel Geography Still Silently Controls Who Gets a "15-Minute Life" in the Ruhr Valley Today

## Index

1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Aim](#aim)
4. [Research Question](#research-question)
5. [Objectives](#objectives)
6. [Methodology Summary](#methodology-summary)
7. [Study Area](#study-area)
8. [Expected Outputs](#expected-outputs)
9. [Relevance](#relevance)
10. [Current Status](#current-status)
11. [Module Architecture](#ghost-infrastructure-module-architecture)
12. [Study Area — Decision Log](#study-area-decision-log)
13. [Module 3 — Historical Data Acquisition & Georeferencing](#module-3-historical-data-acquisition-georeferencing)
14. [Module 5 — Present-Day Network Accessibility Modeling](#module-5-present-day-network-accessibility-modeling)
15. [Module 6 — Spatial Statistical Test: An Unexpected, Reversed Finding](#module-6-spatial-statistical-test-an-unexpected-reversed-finding)
16. [Module 6A — Confound Verification: The Finding Holds Independently](#module-6a-confound-verification-the-finding-holds-independently)
17. [Module 6B — Local Moran's I: Fulfilling the Spatial-Clustering Objective](#module-6b-local-morans-i-fulfilling-the-spatial-clustering-objective)
18. [Module 7 — Geospatial Visualization](#module-7-geospatial-visualization)
19. [Design Principle Reinforced](#design-principle-reinforced)
20. [Definitive Distance Verification — Ghost Infrastructure Overlay Anomalies](#definitive-distance-verification-ghost-infrastructure-overlay-anomalies)
21. [Module 10 — Walking-Threshold Sensitivity Analysis](#module-10-walking-threshold-sensitivity-analysis)
22. [Module 11 — Multi-City Replication: Essen Historical Data Digitization](#module-11-multi-city-replication-essen-historical-data-digitization)
23. [Module 12 — Multi-City Replication: Essen Pipeline & Results](#module-12-multi-city-replication-essen-pipeline-results)
24. [Module 13 — Mixed Replication, Reported Honestly](#module-13-mixed-replication-reported-honestly)

## Project Overview

GHOST INFRASTRUCTURE is a historical-cartographic and spatial-network research project testing whether the Ruhr Valley's 19th and 20th-century industrial geography — coal-mine locations and worker-housing colonies (Zechensiedlungen) — continues to structurally predict present-day accessibility inequality, more than half a century after industrial decline began and years after the last mine's closure in 1974. (Steel-works and industrial-era railway networks were part of this project's original conceptual scope; the dataset actually compiled and analyzed covers coal mines and worker colonies specifically — the two feature types with sufficiently complete archival records for reliable digitization. Steel-works and historical transportation-network digitization are identified as Future Work in the Research Paper rather than claimed as completed here.)

Rather than treating "industrial legacy" as a qualitative, narrative concept — as it is predominantly treated in existing heritage and economic-geography literature — this project makes it spatially and statistically measurable, directly overlaying digitized historical industrial geography against a quantitative, network-based measure of present-day urban accessibility: the "15-minute city" framework.

## Problem Statement

The concept of "path dependency" — that historical spatial decisions continue to shape present-day urban outcomes long after their original rationale has disappeared — is a well-established theoretical idea in economic geography. Yet it is rarely tested with direct, quantitative spatial evidence. Existing scholarship on post-industrial urban legacy in regions like the Ruhr Valley is predominantly qualitative, focused on heritage narratives, cultural identity, and planning discourse, rather than on directly measuring whether historical industrial-era spatial patterns statistically correlate with present-day accessibility outcomes. Separately, the substantial and growing "15-minute city" equity literature examines accessibility inequality primarily through contemporary socioeconomic lenses — income, race, age — without testing whether inequality patterns trace back to a region's specific historical industrial geography.

## Aim

To develop a reproducible geospatial methodology that digitizes historical industrial-era spatial infrastructure in the Ruhr Valley and directly tests, using network-based accessibility modeling and spatial statistics, whether present-day "15-minute city" accessibility inequality is structurally patterned by this historical industrial geography.

## Research Question

Does the historical geography of Ruhr Valley coal and steel industry infrastructure — mine locations, worker-housing colonies, and industrial-era rail and road networks — continue to structurally predict which present-day neighborhoods fall inside or outside a "15-minute" accessibility standard, decades after industrial decline?

## Objectives

- Digitize and georeference historical industrial-era spatial data for a defined Ruhr Valley study area, including former coal-mine locations and worker-housing colonies (Zechensiedlungen). Industrial-era transportation infrastructure (rail and road networks) was part of the original scope but was ultimately deferred to Future Work — see the Research Paper's Future Work section.
- Construct a present-day network-based accessibility model (walking/cycling isochrones to essential services — healthcare, groceries, education, green space) using current road and path network data.
- Apply spatial statistical methods (Local Moran's I / hot-spot analysis) to test whether low-accessibility zones today are statistically clustered around historical industrial-era locations, rather than randomly distributed.
- Produce a direct cartographic overlay of historical industrial geography against present-day accessibility patterns, visually and statistically demonstrating (or disconfirming) a "ghost infrastructure" effect.
- Document the full historical-map digitization and georeferencing methodology as a reproducible process, extensible to other post-industrial regions.

## Methodology Summary

Historical maps of the Ruhr Valley's industrial-era geography (coal-mine sites, worker-housing colonies, historical rail lines) will be sourced from archival and digitized historical map collections, manually georeferenced in QGIS to align with the modern coordinate system, and digitized as vector layers representing 19th and early-to-mid-20th-century industrial infrastructure.

Present-day accessibility will be modeled using network analysis (QGIS Network Analyst or Python's OSMnx library) against current OpenStreetMap road and path data, generating 15-minute walking and cycling isochrones from residential areas to categories of essential services.

The historical industrial layer and present-day accessibility layer will then be spatially tested against each other using Local Moran's I hot-spot analysis, identifying whether statistically significant clusters of low accessibility today spatially coincide with historical industrial-era locations, rather than assuming a relationship from visual overlay alone.

## Study Area

A defined sub-region of the Ruhr Valley, Germany — the historical heart of the region's coal and steel industry, and the immediate geographic and institutional context of Ruhr University Bochum.

## Expected Outputs

- A digitized, georeferenced historical-industrial-geography dataset for the study area (mine locations, worker colonies, historical infrastructure).
- A present-day network-based 15-minute accessibility model for the same area.
- A spatial statistical test of historical-industrial-geography clustering against present-day accessibility inequality.
- A cartographic series overlaying historical industrial geography against modern accessibility patterns.
- An interactive dashboard and complete open-source, reproducible methodology.

## Relevance

This project connects directly to post-industrial urban planning and governance — testing whether infrastructure investment and accessibility-improvement decisions in former industrial regions should account for historically-rooted structural patterns, rather than treating accessibility inequality as a purely present-day phenomenon. Its methodology — combining historical cartographic digitization with modern spatial-network analysis and statistical hot-spot testing — is directly transferable to any post-industrial region globally.

## Current Status

Project Concept Finalized
Version 1.0

---

# GHOST INFRASTRUCTURE — Module Architecture

# MODULE 1 — Project Conceptualization & Literature Review
Research question, aim, and objectives finalized following a review of existing literature identifying two separate gaps: predominantly qualitative treatment of industrial-heritage legacy in economic geography, and the absence of historical-industrial-geography testing within the substantial contemporary "15-minute city" equity literature.

# MODULE 2 — Study Area Definition
Definition of the specific Ruhr Valley sub-region under study, anchored to the region's historical coal and steel industry core and Ruhr University Bochum's institutional context.

# MODULE 3 — Historical Data Acquisition & Georeferencing
Sourcing of historical maps (coal-mine locations, Zechensiedlungen worker-housing colonies, industrial-era transportation infrastructure) from archival and digitized historical map collections, followed by manual georeferencing in QGIS to align historical geography with the modern coordinate system.

# MODULE 4 — Historical Infrastructure Digitization
Manual vector digitization of georeferenced historical industrial-era features — mine boundaries, worker-housing colony extents, historical rail and road alignments — producing a structured, analysis-ready historical GIS layer.

# MODULE 5 — Present-Day Network Accessibility Modeling
Construction of a network-based 15-minute walking/cycling accessibility model using current OpenStreetMap road and path data, generating isochrones to essential-service categories (healthcare, groceries, education, green space) across the study area.

# MODULE 6 — Spatial Statistical Testing
Application of Local Moran's I / hot-spot analysis to test whether present-day low-accessibility zones are statistically clustered around historical industrial-era locations, rather than randomly distributed — the project's core empirical test.

# MODULE 7 — Cartographic Visualization
Production of the project's signature cartographic outputs — direct visual overlays of historical industrial geography against present-day accessibility patterns, designed to professional, publication-grade visual standards.

# MODULE 8 — Dashboard & Deployment
Development and deployment of an interactive dashboard presenting the historical-modern overlay, accessibility model, and statistical test results.

# MODULE 9 — Documentation
Project Journal, Research Paper, README, and GitHub deployment.

----------------------------------------------------------------------------------------------------

## Study Area — Decision Log

**Selected**: Bochum, North Rhine-Westphalia, Germany.

**Reasoning**: Bochum was a small agricultural town until iron, coal, and steel industries developed 
mid-19th century, becoming a defining Ruhr Valley industrial city through the 1950s. Directly 
relevant to the RePIC program's institutional context (Ruhr University Bochum, Semester 1 location). 
Multiple documented historical worker-housing colonies (Zechensiedlungen) exist within the city, 
cataloged by the region's Industrial Heritage Route (route-industriekultur.ruhr), providing a 
concrete, traceable historical data source.

**Approximate bounding box**: 51.42°N-51.53°N, 7.13°E-7.30°E (to be refined once historical map 
sources are acquired).

## Module 3 — Historical Data Acquisition & Georeferencing

Historical industrial-era spatial data for Bochum was compiled from Mindat.org (coal mine locations, 
sourced page-by-page since no bulk API was available) and German heritage/archival sources (Wikipedia, 
Route Industriekultur, ruhr-bauten.de) for worker-housing colonies (Zechensiedlungen).

Two independent datasets were compiled: 13 coal mines (Zeche) and 4 worker-housing colonies, kept as 
separate layers by design — a "Zeche" (mine) and a "Siedlung" (settlement) are structurally distinct 
feature types, not interchangeable, and a proposed steelworker colony (Stahlhausen, associated with 
Bochumer Verein rather than any coal mine) was explicitly excluded from the Zechensiedlungen dataset 
during review, since it belongs to a different industrial category despite being in the same city.

Both datasets were converted from compiled CSV format to georeferenced GeoPackage point layers 
(EPSG:4326) using GeoPandas, ready for direct QGIS integration.

## Module 5 — Present-Day Network Accessibility Modeling

Bochum's complete pedestrian street network (69,393 nodes, 169,668 edges) was acquired via OSMnx 
from OpenStreetMap, along with 786 essential-service points of interest (hospitals, clinics, 
pharmacies, schools, kindergartens, supermarkets, convenience stores, parks) — providing the 
foundation for network-based 15-minute walking accessibility analysis, as distinct from simple 
straight-line radius buffers.

## Module 6 — Spatial Statistical Test: An Unexpected, Reversed Finding

A Welch's t-test comparing distance-to-nearest-historical-industrial-site between low-accessibility 
and high-accessibility network nodes found a highly significant relationship (t=42.887, p<0.00001) — 
but in the opposite direction to the original hypothesis. Low-accessibility nodes were, on average, 
further from historical industrial sites (1984m) than high-accessibility nodes (1450m), meaning 
proximity to historical coal-mining infrastructure predicts BETTER present-day accessibility, not worse.

This is interpreted as a genuine, reportable finding rather than a failed hypothesis: historical 
industrial cores were, by necessity, built at the center of dense worker populations, and this 
central, historically-established urban fabric appears to retain stronger present-day service density 
and network connectivity than more peripheral areas — a "path dependency of centrality" rather than a 
"path dependency of neglect." The original hypothesis assumed industrial legacy would predict 
disadvantage; the evidence instead suggests industrial-era centrality predicts present-day advantage, 
with genuine accessibility gaps concentrated in areas further from the historical industrial core.

## Module 6A — Confound Verification: The Finding Holds Independently

Before accepting the reversed relationship as genuine, a confound was tested: since historical 
industrial sites might simply cluster near Bochum's city center (which independently predicts 
better accessibility), the historical-site effect could be a proxy for city-center proximity 
rather than a genuine independent effect.

Correlation between distance-to-historical-site and distance-to-city-center was low (r=0.063), 
indicating these are largely independent spatial variables, not proxies for one another. A logistic 
regression predicting 15-minute accessibility from both distances simultaneously found that distance 
to historical industrial sites remained a significant independent predictor (coefficient=-0.0005, 
p<0.001) even after controlling for distance to the city center — confirming the "ghost 
infrastructure" effect is genuine and independent, not an artifact of city-center clustering.

## Module 6B — Local Moran's I: Fulfilling the Spatial-Clustering Objective

The project's stated Objectives (Module 6, above) committed to applying Local Moran's I / hot-spot analysis to test whether low-accessibility zones are statistically clustered, rather than randomly distributed. The Welch's t-test and logistic regression reported in Module 6 and 6A tested a related but distinct question — whether *distance* to historical sites differs between accessibility groups — not spatial *clustering* of accessibility itself. This module closes that gap with the originally-promised test.

A K-nearest-neighbor (k=8) spatial weights matrix was constructed over all 69,393 street-network nodes (row-standardized), and Local Moran's I was computed on the binary within-15-minute accessibility variable using 99 conditional permutations (`libpysal`/`esda`, seed=42, significance at p<0.05).

Results: mean local I = 0.923. 10,266 of 69,393 nodes (14.8%) were statistically significant spatial clusters — of these, 9,568 were Low-Low ("cold-spot") clusters (contiguous zones of low accessibility surrounded by other low-accessibility nodes) and 698 were High-Low spatial outliers. No significant High-High or Low-High clusters were found. Cross-tabulating against distance to historical sites: nodes in significant LL cold-spot clusters average 1,992.3m from historical industrial sites, versus 1,447.1m for non-significant nodes — and 97.1% of all low-accessibility nodes fall within a statistically significant LL cluster.

This is a genuinely independent corroboration of the Module 6 finding via a different statistical method: low accessibility in Bochum is not randomly scattered but forms significant, spatially contiguous cold-spots that are measurably farther from historical industrial infrastructure than the rest of the city — directly answering the objective as originally stated. The cluster map (`outputs/plots/lisa_cluster_map.png`) and the reproducible script (`spatial_clustering_lisa.py`, project root) are checked into the repository. Full write-up in Research_Paper.md Section 4.4.

## Module 7 — Geospatial Visualization

The project's signature visualization — a full-city overlay of all 69,393 street-network nodes 
(colored by accessibility status), historical coal mine locations, and historical worker-colony 
locations — was produced and independently verified via a dedicated visual review pass.

An initial rendering attempt produced an apparently broken map showing only a single visible point. 
This was diagnosed, not assumed to be a plotting error, and traced to a coordinate reference system 
mismatch: the accessibility node layer had been saved in EPSG:32632 (UTM Zone 32N, a metric 
projection used earlier for accurate distance calculations), while the historical mine and colony 
layers remained in EPSG:4326 (geographic latitude/longitude). Plotting these together without 
reprojecting to a shared CRS caused the UTM-coordinate layer's actual geographic extent (values in 
the hundreds of thousands of meters) to render as a single indistinguishable point against the 
latitude/longitude layers' much smaller coordinate range. Explicitly reprojecting all three layers to 
a shared EPSG:4326 CRS before plotting resolved this.

A separate visual review pass identified two apparent anomalies: 12 visible triangles rather than the expected 13 coal mines, and 
2 of 4 worker-colony markers appearing to visually overlap. Both were investigated against the 
underlying coordinate data rather than assumed to be genuine errors, and confirmed as accurate 
reflections of real historical geography rather than data or plotting defects: two coal mines 
(Mansfeld and Heinrich Gustav, both in the Langendreer/Werne area) are located approximately 1.7km 
apart, close enough to visually merge at full-city map scale; two worker colonies (Kolonie Hannover 
and Am Rübenkamp) are located approximately 500m apart, consistent with both having been built to 
serve the same Hannover mine complex in overlapping construction periods (1874-1890 and 1888-1892 
respectively). No correction was needed — the apparent anomalies were genuine historical clustering, 
not data errors.

## Design Principle Reinforced

This module reinforces the same evidence-first discipline established across prior projects, applied 
here to a genuinely different type of validation: rather than a causal-inference placebo test, this 
project required verifying that an unexpected reversed statistical finding was not a confound 
(tested directly via correlation and multivariate regression), and that an independently-flagged 
visual anomaly in a cartographic output was not a data error (traced back to the underlying 
coordinate values and confirmed as genuine historical geography). In both cases, the anomaly was 
investigated to a specific, verifiable cause before being accepted or dismissed — consistent with the 
project's broader commitment to treating unexpected results as questions to resolve, not outcomes to 
either suppress or uncritically accept.

## Definitive Distance Verification — Ghost Infrastructure Overlay Anomalies

Following repeated review passes flagging "12 vs 13 mines" and colony-marker 
overlap across multiple map outputs, exact Haversine distances were calculated between the 
specific point pairs in question, rather than relying on further visual inspection.

Mansfeld and Heinrich Gustav coal mines: 1.75 km apart.
Kolonie Hannover and Am Rübenkamp worker colonies: 0.33 km apart.

Both distances are small enough to visually merge into single markers at full-city map scale 
(Bochum spans approximately 14 km), definitively confirming these are genuine close-proximity 
historical sites rather than data errors, duplicate entries, or pipeline bugs. This closes the 
verification loop initiated by that earlier review pass: the underlying data was independently 
confirmed correct via direct coordinate inspection (13 mines present, all coordinates valid) and 
now via exact distance calculation, rather than accepted or dismissed based on visual impression 
alone.

## Module 10 — Walking-Threshold Sensitivity Analysis

As part of a broader push to take every completed portfolio project further — adding missing
datasets, expanding scope, and reducing documented limitations wherever genuinely possible — this
project was selected as the first candidate, on the reasoning that it has zero Google Earth Engine
dependency (pure OSMnx/OpenStreetMap + public GADM boundaries) and an already-documented, concrete
Future Work list (Section 8 of the Research Paper) naming exactly the kind of expansion needed.

The first, zero-new-data item tackled was Future Work's "Walking-time-threshold sensitivity
analysis." `threshold_sensitivity.py` (new, project root) re-ran the full accessibility-classification
→ distance-to-historical-site → Welch's t-test → logistic-regression-confound pipeline at 10-minute
(750m) and 20-minute (1,500m) network-distance thresholds, reusing the already-downloaded Bochum
network graph and the already-computed `dist_to_historical_m`/`dist_to_center_m` fields — no new
data acquisition required.

Result: the reversed relationship holds at every threshold and *strengthens* as the threshold widens.
10-min: t=47.062, p<0.00001, Cohen's d=0.413. 15-min (original): t=42.887, d=0.589. 20-min: t=32.150,
p<0.00001, d=0.661. The odds ratio per 100m closer to a historical site stays stable across all three
(4.24%, 4.88%, 4.49%), confirming the original 15-minute result was not a threshold-dependent
artifact. Full results in `outputs/threshold_sensitivity_results.json`; comparison figure in
`outputs/plots/threshold_sensitivity_comparison.png`. Write-up in Research_Paper.md Section 4.5.

## Module 11 — Multi-City Replication: Essen Historical Data Digitization

The second Future Work item tackled was multi-city comparison, explicitly named in the paper's own
Future Work section ("Replicating this methodology in comparable Ruhr Valley cities (e.g., Dortmund,
Essen)"). Essen was selected as the comparison city — 15km northeast of Bochum, sharing the same
19th-century Ruhr coal-mining industrial history, and considerably better-documented in German
heritage-GIS sources than most alternatives.

**Geocoding constraint encountered and worked around.** OpenStreetMap's own infrastructure (Overpass
API, Nominatim) was not reliably reachable during this phase of data collection — the same category
of access limitation already documented for GEE-dependent projects elsewhere in the portfolio.
Wikidata's live API was also unavailable (cache-only), and Mindat.org (the source used
for Bochum's original mine dataset) returned 403 on automated fetch. The workaround: KuLaDig
(Kultur.Landschaft.Digital), North Rhine-Westphalia's own state cultural-heritage GIS database, proved
reliably fetchable and gives precise WGS84 coordinates (degree-minute-second format) for surviving
heritage-listed mine structures; German Wikipedia settlement/colony articles reliably carry geo-tagged
`{{Coordinate}}` infoboxes (unlike most demolished mine-shaft articles, which typically do not).

Four major coal mines were digitized this way: Zeche Zollverein (Schacht XII, Katernberg, 1851-1986 —
Essen's UNESCO World Heritage site), Zeche Carl Funke (Heisingen, 1804-1973), Zeche Vereinigte Helene
& Amalie (Altendorf, 1873-1965), Zeche Pörtingsiepen (Fischlaken, 1779-1972). Four worker colonies:
Siedlung Carl Funke (Heisingen, 1900-1901), Mathias-Stinnes-Siedlung (Karnap, 1890-1910), Kolonie
Zollverein III (Katernberg, 1880-~1901), Kolonie Beisen (Katernberg, 1902-1903). All 8 coordinates were
independently verified to fall within Essen's official administrative boundary (GADM v4.1, extracted
locally from the already-downloaded `gadm41_DEU.gpkg` covering all of Germany — no new download
needed for this step) before proceeding, as a basic sanity check on the geocoding.

This is explicitly a smaller dataset than Bochum's 17 sites (13 mines + 4 colonies) — Essen's own
historical portal (historischesportal.essen.de) documents approximately 1,700 historical mining
facilities citywide, and this round digitizes only the major, precisely-geocodable subset, an
honestly-scoped limitation rather than a claim of completeness (see Module 13 and Research_Paper.md
Section 7). An initial 3-mine/3-colony (6-site) version was expanded to the current 4-mine/4-colony
(8-site) version after the confound-check result (Module 12) suggested sample size might be
materially affecting the result — documented transparently below rather than silently revised.

The OSM walking-network download itself (`download_network_essen.py`, new — same method as the
original `download_network.py`, pointed at Essen) needed direct Overpass API access for the same
reason above; running it locally produced a 72,027-node, 188,198-edge network with 1,410 essential-service points (before
point-geometry filtering to 366 usable point locations, matching the original Bochum script's own
`pois[pois.geometry.type == "Point"]` filter).

## Module 12 — Multi-City Replication: Essen Pipeline & Results

`run_essen_pipeline.py` (new) replicates Modules 5, 6, 6A, and 6B end-to-end for Essen, reusing every
parameter and method unchanged from the Bochum pipeline (1,125m/15-min threshold, Welch's t-test,
Essen Hauptbahnhof as city-center reference, KNN k=8 LISA with 99 permutations, seed=42).

88.5% of Essen's 72,027 nodes fall within a 15-minute walk of a service (vs. Bochum's 85.8%). The raw
reversed relationship replicates: low-access nodes (n=8,267) average 3,693m from the nearest
historical site vs. 3,130m for high-access nodes (n=63,760) — Welch's t=24.731, p<0.00001, Cohen's
d=0.338 (smaller than Bochum's 0.589, but the same direction and highly significant). The Local
Moran's I result replicates closely: mean local I=0.917 (Bochum: 0.923), 95.5% of low-access nodes in
significant LL cold-spot clusters (Bochum: 97.1%), zero significant HH hot-spot clusters in either
city.

The confound check, however, does **not** replicate cleanly. Correlation between dist-to-historical
and dist-to-center is r=0.405 in Essen vs. r=0.063 in Bochum — a genuinely different result, not
noise. The confound-controlled logistic regression's historical-site coefficient flips sign in Essen
(+0.0001, p<0.00001) relative to Bochum (-0.0005): once city-center distance is controlled for,
greater distance from a historical site associates with *higher*, not lower, odds of accessibility in
Essen. This was checked twice — the 6-site version of the dataset gave r=0.475 and a still-reversed
coefficient; expanding to 8 sites reduced the correlation to r=0.405 but did not eliminate the sign
flip, suggesting sample-size/coverage-density inflation is a partial but not complete explanation
(see Module 13).

## Module 13 — Mixed Replication, Reported Honestly

Consistent with this project's established practice (Module 6/6A, Design Principle Reinforced, above)
of investigating unexpected results to a specific cause rather than suppressing or accepting them at
face value, the Essen confound-check discrepancy was not treated as a bug to fix or a result to
downplay. Two possible explanations were tested and documented rather than picked based on which one
was more convenient: (1) a genuine difference in each city's own industrial-versus-administrative
geography — Essen's coal-mining history may be more spatially concentrated near its present-day
center than Bochum's more dispersed sites; (2) a sampling-density artifact of Essen's smaller (8 vs.
17-site) historical dataset. The correlation's measured decline from r=0.475 (6 sites) to r=0.405 (8
sites) as more sites were added is evidence consistent with explanation (2) being at least a partial
contributor, though it does not, on its own, rule out explanation (1). Rather than force a conclusion
either way, both possibilities — and the specific evidence for each — are documented in
Research_Paper.md Sections 4.6 and 7, and expanding the Essen dataset further is named as Future Work
(Section 8) rather than pursued further this round, given the practical geocoding-precision limits
already reached on Essen's remaining, less-documented historical mining sites (see Module 11).

The overall conclusion drawn from this multi-city round: the "path dependency of centrality" effect
itself — the raw reversed relationship and its independent spatial-clustering corroboration — appears
to generalize across at least these two Ruhr Valley cities. The narrower, stronger claim that this
effect operates *independently* of city-center proximity is, on current two-city evidence, a
Bochum-specific rather than universal finding. Reporting a genuinely mixed multi-city result in full —
rather than only replicating the parts that confirm Bochum's own findings — is treated as the more
valuable and honest outcome of this round, consistent with how this project has handled every prior
unexpected result.