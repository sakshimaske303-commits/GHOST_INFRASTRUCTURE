# GHOST INFRASTRUCTURE

## Mapping How 19th-Century Coal and Steel Geography Still Silently Controls Who Gets a "15-Minute Life" in the Ruhr Valley Today

## Project Overview

GHOST INFRASTRUCTURE is a historical-cartographic and spatial-network research project testing whether the Ruhr Valley's 19th and 20th-century industrial geography — coal-mine locations, steel-works, worker-housing colonies (Zechensiedlungen), and the railway networks built to serve them — continues to structurally determine present-day accessibility inequality, more than half a century after industrial decline began and years after the last mine's closure in 2018.

Rather than treating "industrial legacy" as a qualitative, narrative concept — as it is predominantly treated in existing heritage and economic-geography literature — this project makes it spatially and statistically measurable, directly overlaying digitized historical industrial geography against a quantitative, network-based measure of present-day urban accessibility: the "15-minute city" framework.

## Problem Statement

The concept of "path dependency" — that historical spatial decisions continue to shape present-day urban outcomes long after their original rationale has disappeared — is a well-established theoretical idea in economic geography. Yet it is rarely tested with direct, quantitative spatial evidence. Existing scholarship on post-industrial urban legacy in regions like the Ruhr Valley is predominantly qualitative, focused on heritage narratives, cultural identity, and planning discourse, rather than on directly measuring whether historical industrial-era spatial patterns statistically correlate with present-day accessibility outcomes. Separately, the substantial and growing "15-minute city" equity literature examines accessibility inequality primarily through contemporary socioeconomic lenses — income, race, age — without testing whether inequality patterns trace back to a region's specific historical industrial geography.

## Aim

To develop a reproducible geospatial methodology that digitizes historical industrial-era spatial infrastructure in the Ruhr Valley and directly tests, using network-based accessibility modeling and spatial statistics, whether present-day "15-minute city" accessibility inequality is structurally patterned by this historical industrial geography.

## Research Question

Does the historical geography of Ruhr Valley coal and steel industry infrastructure — mine locations, worker-housing colonies, and industrial-era rail and road networks — continue to structurally predict which present-day neighborhoods fall inside or outside a "15-minute" accessibility standard, decades after industrial decline?

## Objectives

- Digitize and georeference historical industrial-era spatial data for a defined Ruhr Valley study area, including former coal-mine locations, worker-housing colonies (Zechensiedlungen), and industrial-era transportation infrastructure.
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

## Module 6 — Confound Verification: The Finding Holds Independently

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

## Module 7 — Geospatial Visualization

The project's signature visualization — a full-city overlay of all 69,393 street-network nodes 
(colored by accessibility status), historical coal mine locations, and historical worker-colony 
locations — was produced and independently verified via cross-chat visual inspection.

An initial rendering attempt produced an apparently broken map showing only a single visible point. 
This was diagnosed, not assumed to be a plotting error, and traced to a coordinate reference system 
mismatch: the accessibility node layer had been saved in EPSG:32632 (UTM Zone 32N, a metric 
projection used earlier for accurate distance calculations), while the historical mine and colony 
layers remained in EPSG:4326 (geographic latitude/longitude). Plotting these together without 
reprojecting to a shared CRS caused the UTM-coordinate layer's actual geographic extent (values in 
the hundreds of thousands of meters) to render as a single indistinguishable point against the 
latitude/longitude layers' much smaller coordinate range. Explicitly reprojecting all three layers to 
a shared EPSG:4326 CRS before plotting resolved this.

Independent visual verification (conducted in a separate chat session, per project convention) 
identified two apparent anomalies: 12 visible triangles rather than the expected 13 coal mines, and 
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

Following repeated independent visual verification flagging "12 vs 13 mines" and colony-marker 
overlap across multiple map outputs, exact Haversine distances were calculated between the 
specific point pairs in question, rather than relying on further visual inspection.

Mansfeld and Heinrich Gustav coal mines: 1.75 km apart.
Kolonie Hannover and Am Rübenkamp worker colonies: 0.33 km apart.

Both distances are small enough to visually merge into single markers at full-city map scale 
(Bochum spans approximately 14 km), definitively confirming these are genuine close-proximity 
historical sites rather than data errors, duplicate entries, or pipeline bugs. This closes the 
verification loop initiated by external visual review: the underlying data was independently 
confirmed correct via direct coordinate inspection (13 mines present, all coordinates valid) and 
now via exact distance calculation, rather than accepted or dismissed based on visual impression 
alone.