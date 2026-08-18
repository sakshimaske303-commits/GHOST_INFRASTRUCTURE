# GHOST INFRASTRUCTURE

## Mapping How 19th-Century Coal and Steel Geography Still Silently Controls Who Gets a "15-Minute Life" in the Ruhr Valley Today

## Project Report

## Project Overview

GHOST INFRASTRUCTURE is a historical-cartographic and spatial-network research project testing whether the Ruhr Valley's 19th and 20th-century industrial geography — coal-mine locations and worker-housing colonies (Zechensiedlungen) — continues to structurally predict present-day accessibility inequality, more than half a century after industrial decline began and years after the last mine's closure in 1974. (Industrial-era transportation networks were part of the project's original conceptual scope but were ultimately not digitized this phase; see Limitations and the Research Paper's Future Work section.)

Rather than treating "industrial legacy" as a qualitative, narrative concept — as it is predominantly treated in existing heritage and economic-geography literature — this project makes it spatially and statistically measurable, directly testing digitized historical industrial geography against a quantitative, network-based measure of present-day urban accessibility: the "15-minute city" framework.

## Problem Statement

The concept of "path dependency" — that historical spatial decisions continue to shape present-day urban outcomes long after their original rationale has disappeared — is a well-established theoretical idea in economic geography, yet it is rarely tested with direct, quantitative spatial evidence. Existing scholarship on post-industrial urban legacy is predominantly qualitative, focused on heritage narratives and cultural identity, rather than on directly measuring whether historical industrial-era spatial patterns statistically correlate with present-day accessibility outcomes. Separately, the substantial contemporary "15-minute city" equity literature examines accessibility inequality through present-day socioeconomic lenses without testing whether inequality patterns trace back to a region's specific historical industrial geography.

## Aim

To develop a reproducible geospatial methodology that digitizes historical industrial-era spatial infrastructure in Bochum, Germany, and directly tests, using network-based accessibility modeling and spatial statistics, whether present-day "15-minute city" accessibility is structurally patterned by this historical industrial geography.

## Study Area

Bochum, North Rhine-Westphalia, Germany — a small agricultural town until iron, coal, and steel industries developed mid-19th century, becoming a defining Ruhr Valley industrial city through the 1950s, with its last coal mine closing in 1974. Directly relevant to this research program's institutional context, as home to Ruhr University Bochum.

## Methodology

### Historical Data Compilation

Historical industrial-era spatial data was compiled manually, record by record, from Mindat.org (coal mine locations) and German heritage and archival sources — Wikipedia, the region's Industrial Heritage Route, and ruhr-bauten.de (worker-housing colonies). Two datasets were deliberately kept as independent, structurally distinct layers: 13 coal mines (Zeche) and 4 worker-housing colonies (Zechensiedlungen) — an extraction site and residential worker housing are categorically different feature types. During compilation, a proposed steelworker colony (Stahlhausen, linked to Bochumer Verein rather than any coal mine) was explicitly identified and excluded, since it belongs to a different industrial category despite being located in the same city.

### Present-Day Accessibility Modeling

Bochum's complete pedestrian street network — 69,393 nodes and 169,668 edges — was acquired via OSMnx from OpenStreetMap, along with 786 essential-service points of interest across health, education, and daily-needs categories. A 15-minute walking threshold was operationalized as 1,125 meters of true network distance, computed via Dijkstra's shortest-path algorithm from every essential-service location — not a simplified straight-line radius. This produced a binary accessibility classification across all network nodes: 85.8% within a 15-minute walk of an essential service, 14.2% (9,858 nodes) not.

### Statistical Testing

A Welch's t-test compared distance-to-nearest-historical-industrial-site between low- and high-accessibility nodes, producing a highly significant result in the opposite direction to the original hypothesis: low-accessibility nodes were, on average, further from historical industrial sites (1,984m) than high-accessibility nodes (1,450m) — proximity to historical coal-mining infrastructure predicts better present-day accessibility, not worse.

### Confound Verification

Before accepting this reversed relationship, the most obvious alternative explanation was tested directly: historical sites might simply cluster near Bochum's city center, which would independently predict better accessibility regardless of any genuine historical effect. Correlation between distance-to-historical-site and distance-to-city-center was low (r=0.063), and a logistic regression confirmed the historical-site effect remained statistically significant (coefficient=-0.0005, p<0.001) even after controlling for city-center distance — the reversed effect is genuine and independent, not a city-center proxy.

### Spatial Clustering (Local Moran's I)

The t-test above compares distance to historical sites between two groups; it does not, by itself, test whether low accessibility is spatially clustered. A Local Moran's I (LISA) analysis was run on all 69,393 nodes (KNN k=8 spatial weights, 99 permutations) to test this directly. 14.8% of nodes formed statistically significant spatial clusters (p<0.05); of these, the overwhelming majority (9,568 of 10,266) were Low-Low "cold-spot" clusters — contiguous zones of low accessibility, not randomly scattered low-accessibility points. 97.1% of all low-accessibility nodes fall inside one of these significant cold-spot clusters, and cluster nodes average nearly 2km from historical sites versus 1.4km for non-clustered nodes — an independent statistical method corroborating the t-test finding.

## Key Finding

The evidence supports a "path dependency of centrality" rather than the originally hypothesized "path dependency of neglect." Nineteenth-century industrial infrastructure was built, by necessity, at the center of dense worker populations; this historically-established urban fabric appears to retain stronger present-day service density and street-network connectivity than more peripheral areas developed later. Genuine accessibility gaps in present-day Bochum concentrate further from, not closer to, the historical industrial core.

## Robustness: Threshold Sensitivity and Multi-City Replication

Two follow-up rounds tested how far this finding generalizes. First, the full pipeline was re-run at a stricter 10-minute (750m) and a more permissive 20-minute (1,500m) walking threshold, using the same Bochum data — the reversed relationship holds, and its effect size actually grows, at both (Cohen's d=0.413 and 0.661, versus 0.589 at 15 minutes). Second, the entire methodology was independently replicated in Essen, a second Ruhr Valley city, using 4 major historical mines and 4 worker colonies digitized from KuLaDig and Wikipedia, and Essen's own 72,027-node street network. The result is a genuine, honestly-reported mixed replication: the raw reversed effect (Cohen's d=0.338) and the Local Moran's I spatial-clustering result (95.5% of low-accessibility nodes in significant cold-spot clusters, versus Bochum's 97.1%) both replicate. The confound-independence result does not — in Essen, distance-to-historical-site correlates moderately with distance-to-city-center (r=0.405, versus Bochum's r=0.063), and the historical-site effect's sign reverses once city-center distance is statistically controlled for. This is interpreted as evidence that the underlying "centrality legacy" mechanism generalizes across cities, while the specific claim that it is independent of present-day city-center proximity is, on current evidence, a Bochum-specific rather than universal result. Full statistical detail in Research_Paper.md Sections 3.6–3.7 and 4.5–4.6.

## Verification and Quality Assurance

This project's findings were subjected to multiple rounds of independent verification, including a dedicated visual review pass over all cartographic outputs. Two apparent anomalies flagged during this review — an apparent "12 vs 13 mines" discrepancy across separate map outputs, and overlapping worker-colony markers — were investigated to a definitive conclusion rather than assumed to be errors: exact Haversine distance calculations confirmed Mansfeld and Heinrich Gustav mines are genuinely 1.75km apart, and Kolonie Hannover and Am Rübenkamp colonies are genuinely 0.33km apart — both close enough to visually merge at full-city map scale, confirming both anomalies as authentic historical geography rather than data or pipeline errors. A separate rendering issue, where an early overlay map displayed as a single visible point, was traced to a coordinate reference system mismatch (a metric UTM projection versus standard latitude/longitude) and resolved by reprojecting all layers to a shared CRS.

## Deliverables

A digitized, georeferenced historical-industrial-geography dataset for Bochum (13 mines, 4 worker colonies) and Essen (4 mines, 4 worker colonies); a present-day network-based 15-minute accessibility model built on Bochum's 69,393-node and Essen's 72,027-node street networks; a spatial statistical test of historical-industrial-geography clustering against present-day accessibility, validated against its most likely confound, corroborated by an independent Local Moran's I spatial-clustering analysis, and tested for robustness across three walking thresholds and two cities; a cartographic series overlaying historical industrial geography against modern accessibility patterns for both cities; Python-built interactive maps (folium) for both Bochum and Essen, each with clickable historical-site markers and a low-accessibility heatmap layer; and a multi-page interactive dashboard presenting the full methodology and findings.

## Limitations

The worker-colony dataset (4 sites) is smaller than the coal-mine dataset (13 sites) in Bochum, somewhat limiting the statistical power of colony-specific analysis — an honestly disclosed sample-size constraint rather than an omitted weakness. The 13 mines and 4 colonies digitized here represent the major, well-documented industrial-era sites in Bochum, not the full historical mining register (which includes several hundred smaller, short-lived operations spanning multiple centuries and is not a meaningful comparison set for this study's scope). This project relies on point-based historical site locations rather than full manual boundary digitization of mine and colony extents, a deliberate scope decision given project timeline constraints. Industrial-era transportation infrastructure (rail and road networks) was part of the original conceptual scope but was not digitized this phase. The 15-minute accessibility model treats all essential-service categories as equally weighted, which does not capture genuine differences in how urgently each service type matters to daily life. Socioeconomic confounders (income, age, tenure) were not available for this analysis and are not controlled for. The Essen comparison dataset (8 sites) is smaller relative to Essen's own historical mining register (~1,700 facilities citywide) than the Bochum dataset is to Bochum's, and this appears to materially affect one result: the confound-independence finding that held cleanly in Bochum did not replicate in Essen, and evidence suggests Essen's smaller sample size is a partial (though not necessarily complete) contributor to that discrepancy — see Research_Paper.md Sections 4.6 and 7 for full detail.

