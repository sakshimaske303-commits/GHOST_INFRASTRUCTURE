# GHOST INFRASTRUCTURE

## Mapping How 19th-Century Coal and Steel Geography Still Silently Controls Who Gets a "15-Minute Life" in the Ruhr Valley Today

## Project Journal

## Project Overview

GHOST INFRASTRUCTURE is a historical-cartographic and spatial-network research project testing whether the Ruhr Valley's 19th and 20th-century industrial geography — coal-mine locations, worker-housing colonies (Zechensiedlungen), and the transportation networks built to serve them — continues to structurally determine present-day accessibility inequality, more than half a century after industrial decline began and years after the last mine's closure in 1974.

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

## Key Finding

The evidence supports a "path dependency of centrality" rather than the originally hypothesized "path dependency of neglect." Nineteenth-century industrial infrastructure was built, by necessity, at the center of dense worker populations; this historically-established urban fabric appears to retain stronger present-day service density and street-network connectivity than more peripheral areas developed later. Genuine accessibility gaps in present-day Bochum concentrate further from, not closer to, the historical industrial core.

## Verification and Quality Assurance

This project's findings were subjected to multiple rounds of independent verification, including external cross-chat visual review of all cartographic outputs. Two apparent anomalies flagged during this review — an apparent "12 vs 13 mines" discrepancy across separate map outputs, and overlapping worker-colony markers — were investigated to a definitive conclusion rather than assumed to be errors: exact Haversine distance calculations confirmed Mansfeld and Heinrich Gustav mines are genuinely 1.75km apart, and Kolonie Hannover and Am Rübenkamp colonies are genuinely 0.33km apart — both close enough to visually merge at full-city map scale, confirming both anomalies as authentic historical geography rather than data or pipeline errors. A separate rendering issue, where an early overlay map displayed as a single visible point, was traced to a coordinate reference system mismatch (a metric UTM projection versus standard latitude/longitude) and resolved by reprojecting all layers to a shared CRS.

## Deliverables

A digitized, georeferenced historical-industrial-geography dataset for Bochum (13 mines, 4 worker colonies); a present-day network-based 15-minute accessibility model built on a 69,393-node street network; a spatial statistical test of historical-industrial-geography clustering against present-day accessibility, validated against its most likely confound; a cartographic series overlaying historical industrial geography against modern accessibility patterns; and a multi-page interactive dashboard presenting the full methodology and findings.

## Limitations

The worker-colony dataset (4 sites) is smaller than the coal-mine dataset (13 sites), somewhat limiting the statistical power of colony-specific analysis — an honestly disclosed sample-size constraint rather than an omitted weakness. This project relies on point-based historical site locations rather than full manual boundary digitization of mine and colony extents, a deliberate scope decision given project timeline constraints. The 15-minute accessibility model treats all essential-service categories as equally weighted, which does not capture genuine differences in how urgently each service type matters to daily life.

