# GHOST INFRASTRUCTURE — Development Log

This is my working log for GHOST INFRASTRUCTURE, a project testing whether Bochum's 19th and 20th-century coal-mining geography still shapes who gets a walkable "15-minute life" in the Ruhr Valley today. I kept this log the way I keep every project's log — as an honest, chronological record of the decisions, dead ends, and fixes that went into the analysis, not a cleaned-up summary written after the fact.

What follows is organized as a set of entries, each covering one phase of the work: framing the research question, digitizing historical mine and colony locations, building a present-day accessibility model, running the statistical tests, verifying an unexpected result, visualizing it, and the robustness and multi-city extensions that came after. Every number, p-value, and decision below reflects what I actually found when I ran the analysis, including the result that reversed my original hypothesis.

## Index

1. [Entry 1](#entry-1)
2. [Entry 2](#entry-2)
3. [Entry 3](#entry-3)
4. [Entry 4](#entry-4)
5. [Entry 5](#entry-5)
6. [Entry 6](#entry-6)
7. [Entry 7](#entry-7)
8. [Entry 8](#entry-8)
9. [Entry 9](#entry-9)
10. [Entry 10](#entry-10)
11. [Entry 11](#entry-11)
12. [Entry 12](#entry-12)
13. [Entry 13](#entry-13)

## Entry 1

GHOST INFRASTRUCTURE is a historical-cartographic and spatial-network project testing whether the Ruhr Valley's 19th and 20th-century industrial geography — coal-mine locations and worker-housing colonies (Zechensiedlungen) — continues to structurally predict present-day accessibility inequality, more than half a century after industrial decline began and years after the last mine's closure in 1974. Steel-works and industrial-era railway networks were part of my original conceptual scope, but the dataset I actually compiled and analyzed covers coal mines and worker colonies specifically — the two feature types with sufficiently complete archival records for reliable digitization. I identified steel-works and historical transportation-network digitization as Future Work in the Research Paper rather than claiming them as completed.

Rather than treating "industrial legacy" as a qualitative, narrative concept — as it is predominantly treated in existing heritage and economic-geography literature — I wanted to make it spatially and statistically measurable: directly overlaying digitized historical industrial geography against a quantitative, network-based measure of present-day urban accessibility, the "15-minute city" framework.

The concept of "path dependency" — that historical spatial decisions continue to shape present-day urban outcomes long after their original rationale has disappeared — is a well-established theoretical idea in economic geography, yet it is rarely tested with direct, quantitative spatial evidence. Existing scholarship on post-industrial urban legacy in regions like the Ruhr Valley is predominantly qualitative, focused on heritage narratives, cultural identity, and planning discourse, rather than on directly measuring whether historical industrial-era spatial patterns statistically correlate with present-day accessibility outcomes. Separately, the substantial and growing "15-minute city" equity literature examines accessibility inequality primarily through contemporary socioeconomic lenses — income, race, age — without testing whether inequality patterns trace back to a region's specific historical industrial geography. That's the gap I set out to fill: a reproducible geospatial methodology that digitizes historical industrial-era spatial infrastructure in the Ruhr Valley and directly tests, using network-based accessibility modeling and spatial statistics, whether present-day "15-minute city" accessibility inequality is structurally patterned by this historical industrial geography.

My research question: does the historical geography of Ruhr Valley coal and steel industry infrastructure — mine locations, worker-housing colonies, and industrial-era rail and road networks — continue to structurally predict which present-day neighborhoods fall inside or outside a "15-minute" accessibility standard, decades after industrial decline? I set four objectives to answer it: digitize and georeference historical industrial-era spatial data for a defined study area, including former coal-mine locations and worker-housing colonies (industrial-era transportation infrastructure was part of the original scope but was ultimately deferred to Future Work); construct a present-day network-based accessibility model — walking/cycling isochrones to essential services like healthcare, groceries, education, and green space — using current road and path network data; apply spatial statistical methods (Local Moran's I / hot-spot analysis) to test whether low-accessibility zones today are statistically clustered around historical industrial-era locations, rather than randomly distributed; and produce a direct cartographic overlay of historical industrial geography against present-day accessibility patterns, visually and statistically demonstrating — or disconfirming — a "ghost infrastructure" effect.

For the study area I selected Bochum, North Rhine-Westphalia, Germany. Bochum was a small agricultural town until iron, coal, and steel industries developed mid-19th century, becoming a defining Ruhr Valley industrial city through the 1950s — and it's directly relevant to my institutional context, since it's home to Ruhr University Bochum. Multiple documented historical worker-housing colonies exist within the city, cataloged by the region's Industrial Heritage Route (route-industriekultur.ruhr), which gave me a concrete, traceable historical data source to start from. My approximate bounding box was 51.42°N–51.53°N, 7.13°E–7.30°E, to be refined once I actually acquired historical map sources.

The entries that follow document the actual acquisition process, sourcing decisions, and verification steps I used to test this question — including one result that reversed my original hypothesis entirely.

## Entry 2

With the study area and research question settled, the next task was building the historical layer everything else depends on: digitized, georeferenced locations of Bochum's coal mines and worker-housing colonies.

I compiled historical industrial-era spatial data for Bochum from Mindat.org (coal mine locations, sourced page-by-page since no bulk API was available) and German heritage/archival sources — Wikipedia, Route Industriekultur, and ruhr-bauten.de — for the worker-housing colonies (Zechensiedlungen).

I kept two independent datasets: 13 coal mines (Zeche) and 4 worker-housing colonies, as separate layers by design — a "Zeche" (mine) and a "Siedlung" (settlement) are structurally distinct feature types, not interchangeable. During review I found a proposed steelworker colony, Stahlhausen, associated with Bochumer Verein rather than any coal mine, and explicitly excluded it from the Zechensiedlungen dataset, since it belongs to a different industrial category despite being in the same city.

I converted both datasets from compiled CSV format into georeferenced GeoPackage point layers (EPSG:4326) using GeoPandas, ready for direct QGIS integration and for everything downstream.

## Entry 3

With 13 mines and 4 colonies digitized, the next task was building the present-day side of the comparison: a real, network-based accessibility model rather than a simplified straight-line radius.

I acquired Bochum's complete pedestrian street network via OSMnx from OpenStreetMap — 69,393 nodes, 169,668 edges — along with 786 essential-service points of interest: hospitals, clinics, pharmacies, schools, kindergartens, supermarkets, convenience stores, and parks. That gave me the foundation for a genuine network-based 15-minute walking accessibility analysis, computing true walking-network distance to each service category via Dijkstra's shortest-path algorithm rather than a buffer radius that would overstate real walkable access.

## Entry 4

With both layers ready — 17 historical sites and a full accessibility model across 69,393 nodes — I could finally run the test I'd built the whole pipeline for.

A Welch's t-test comparing distance-to-nearest-historical-industrial-site between low-accessibility and high-accessibility network nodes found a highly significant relationship (t=42.887, p<0.00001) — but in the opposite direction to my original hypothesis. Low-accessibility nodes were, on average, further from historical industrial sites (1,984m) than high-accessibility nodes (1,450m), meaning proximity to historical coal-mining infrastructure predicts better present-day accessibility, not worse.

I treated this as a genuine, reportable finding rather than a failed hypothesis: historical industrial cores were, by necessity, built at the center of dense worker populations, and this central, historically-established urban fabric appears to retain stronger present-day service density and network connectivity than more peripheral areas — a "path dependency of centrality" rather than a "path dependency of neglect." My original hypothesis assumed industrial legacy would predict disadvantage; the evidence instead suggests industrial-era centrality predicts present-day advantage, with genuine accessibility gaps concentrated in areas further from the historical industrial core.

## Entry 5

Before accepting the reversed relationship as genuine, I needed to rule out an obvious confound: since historical industrial sites might simply cluster near Bochum's city center, which independently predicts better accessibility, the historical-site effect could just be a proxy for city-center proximity rather than a genuine independent effect.

I checked the correlation between distance-to-historical-site and distance-to-city-center first — it came back low (r=0.063), indicating these are largely independent spatial variables, not proxies for one another. Then I ran a logistic regression predicting 15-minute accessibility from both distances simultaneously, and distance to historical industrial sites remained a significant independent predictor (coefficient=-0.0005, p<0.001) even after controlling for distance to the city center. That confirmed the "ghost infrastructure" effect is genuine and independent, not an artifact of city-center clustering.

## Entry 6

My original Objectives had committed to applying Local Moran's I / hot-spot analysis to test whether low-accessibility zones are statistically clustered, rather than randomly distributed. The Welch's t-test and logistic regression in Entries 4 and 5 tested a related but distinct question — whether distance to historical sites differs between accessibility groups — not spatial clustering of accessibility itself. This entry closes that gap with the test I'd originally promised.

I constructed a K-nearest-neighbor (k=8) spatial weights matrix over all 69,393 street-network nodes, row-standardized, and computed Local Moran's I on the binary within-15-minute accessibility variable using 99 conditional permutations (`libpysal`/`esda`, seed=42, significance at p<0.05).

Results: mean local I = 0.923. 10,266 of 69,393 nodes (14.8%) were statistically significant spatial clusters — of these, 9,568 were Low-Low ("cold-spot") clusters (contiguous zones of low accessibility surrounded by other low-accessibility nodes) and 698 were High-Low spatial outliers. No significant High-High or Low-High clusters turned up. When I cross-tabulated against distance to historical sites, nodes in significant LL cold-spot clusters averaged 1,992.3m from historical industrial sites, versus 1,447.1m for non-significant nodes — and 97.1% of all low-accessibility nodes fell within a statistically significant LL cluster.

This is a genuinely independent corroboration of the Entry 4 finding via a different statistical method: low accessibility in Bochum isn't randomly scattered but forms significant, spatially contiguous cold-spots that are measurably farther from historical industrial infrastructure than the rest of the city — directly answering the objective as I'd originally stated it. I checked the cluster map and the reproducible script (`spatial_clustering_lisa.py`, project root) into the repository, and wrote the full statistical detail up in `GI_Research_Paper.md` Section 4.4.

## Entry 7

With the statistical case made three independent ways, the next task was the project's signature visualization — a full-city overlay of all 69,393 street-network nodes, colored by accessibility status, alongside the historical coal mine and worker-colony locations.

An initial rendering attempt produced an apparently broken map showing only a single visible point. I diagnosed this rather than assuming it was a plotting error, and traced it to a coordinate reference system mismatch: the accessibility node layer had been saved in EPSG:32632 (UTM Zone 32N, a metric projection I'd used earlier for accurate distance calculations), while the historical mine and colony layers remained in EPSG:4326 (geographic latitude/longitude). Plotting these together without reprojecting to a shared CRS caused the UTM-coordinate layer's actual geographic extent — values in the hundreds of thousands of meters — to render as a single indistinguishable point against the latitude/longitude layers' much smaller coordinate range. Explicitly reprojecting all three layers to a shared EPSG:4326 CRS before plotting fixed it.

A separate visual review pass then flagged two apparent anomalies: 12 visible triangles rather than the expected 13 coal mines, and 2 of 4 worker-colony markers appearing to visually overlap. I investigated both against the underlying coordinate data rather than assuming they were genuine errors, and confirmed both as accurate reflections of real historical geography rather than data or plotting defects: two coal mines (Mansfeld and Heinrich Gustav, both in the Langendreer/Werne area) are located about 1.7km apart, close enough to visually merge at full-city map scale; two worker colonies (Kolonie Hannover and Am Rübenkamp) are located about 500m apart, consistent with both having been built to serve the same Hannover mine complex in overlapping construction periods (1874–1890 and 1888–1892 respectively). No correction was needed — the apparent anomalies were genuine historical clustering, not data errors.

This whole exercise reinforced a discipline I've carried through every project since: rather than a causal-inference placebo test, this case required verifying that an unexpected reversed statistical finding wasn't a confound — tested directly via correlation and multivariate regression in Entry 5 — and that an independently-flagged visual anomaly in a cartographic output wasn't a data error, traced back to the underlying coordinate values and confirmed as genuine historical geography. In both cases I investigated the anomaly to a specific, verifiable cause before accepting or dismissing it, rather than either suppressing it or uncritically accepting it.

Following repeated review passes flagging the "12 vs 13 mines" question and the colony-marker overlap across multiple map outputs, I went back and calculated exact Haversine distances between the specific point pairs in question, rather than relying on further visual inspection alone. Mansfeld and Heinrich Gustav coal mines: 1.75 km apart. Kolonie Hannover and Am Rübenkamp worker colonies: 0.33 km apart. Both distances are small enough to visually merge into single markers at full-city map scale (Bochum spans roughly 14 km), definitively confirming these are genuine close-proximity historical sites rather than data errors, duplicate entries, or pipeline bugs. That closed the verification loop I'd opened earlier: the underlying data was independently confirmed correct via direct coordinate inspection (13 mines present, all coordinates valid) and now via exact distance calculation, rather than accepted or dismissed on visual impression alone.

## Entry 8

With the core analysis, confound check, spatial-clustering corroboration, and visualization all done, the remaining work was presenting it and writing it up. I built a multi-page Streamlit dashboard — `app.py` as the entry point, with sub-pages covering study design, historical geography, accessibility analysis, the finding itself, trend exploration, interactive maps, and methodology — presenting the historical-modern overlay, the accessibility model, and the statistical test results in an explorable interface rather than a fixed document alone. Alongside the dashboard I wrote up the Research Paper, the Project Report, and the README, and pushed the repository to GitHub.

## Entry 9

As part of a broader push to take every completed portfolio project further — adding missing datasets, expanding scope, and reducing documented limitations wherever genuinely possible — I picked this project as the first candidate for that push, on the reasoning that it has zero Google Earth Engine dependency (pure OSMnx/OpenStreetMap plus public GADM boundaries) and an already-documented, concrete Future Work list naming exactly the kind of expansion needed.

The first, zero-new-data item I tackled was the Future Work list's "walking-time-threshold sensitivity analysis." I wrote `threshold_sensitivity.py` (new, project root) to re-run the full accessibility-classification → distance-to-historical-site → Welch's t-test → logistic-regression-confound pipeline at 10-minute (750m) and 20-minute (1,500m) network-distance thresholds, reusing the already-downloaded Bochum network graph and the already-computed distance fields — no new data acquisition required.

Result: the reversed relationship holds at every threshold and actually strengthens as the threshold widens. 10-min: t=47.062, p<0.00001, Cohen's d=0.413. 15-min (original): t=42.887, d=0.589. 20-min: t=32.150, p<0.00001, d=0.661. The odds ratio per 100m closer to a historical site stayed stable across all three (4.24%, 4.88%, 4.49%), confirming the original 15-minute result wasn't a threshold-dependent artifact. I wrote the full write-up into `GI_Research_Paper.md` Section 4.5.

## Entry 10

The second Future Work item I tackled was multi-city comparison, explicitly named in my own paper's Future Work section as replicating this methodology in comparable Ruhr Valley cities. I chose Essen as the comparison city — 15km northeast of Bochum, sharing the same 19th-century Ruhr coal-mining industrial history, and considerably better-documented in German heritage-GIS sources than most alternatives.

I hit a geocoding constraint early on. OpenStreetMap's own infrastructure (Overpass API, Nominatim) wasn't reliably reachable during this phase of data collection — the same category of access limitation I've documented for GEE-dependent projects elsewhere in the portfolio. Wikidata's live API was also unavailable (cache-only), and Mindat.org, the source I'd used for Bochum's original mine dataset, returned 403 on automated fetch. My workaround: KuLaDig (Kultur.Landschaft.Digital), North Rhine-Westphalia's own state cultural-heritage GIS database, proved reliably fetchable and gives precise WGS84 coordinates for surviving heritage-listed mine structures; German Wikipedia settlement/colony articles reliably carry geo-tagged coordinate infoboxes, unlike most demolished mine-shaft articles, which typically don't.

I digitized four major coal mines this way: Zeche Zollverein (Schacht XII, Katernberg, 1851–1986 — Essen's UNESCO World Heritage site), Zeche Carl Funke (Heisingen, 1804–1973), Zeche Vereinigte Helene & Amalie (Altendorf, 1873–1965), and Zeche Pörtingsiepen (Fischlaken, 1779–1972). Four worker colonies: Siedlung Carl Funke (Heisingen, 1900–1901), Mathias-Stinnes-Siedlung (Karnap, 1890–1910), Kolonie Zollverein III (Katernberg, 1880–~1901), and Kolonie Beisen (Katernberg, 1902–1903). I independently verified all 8 coordinates fell within Essen's official administrative boundary (GADM v4.1, extracted locally from the already-downloaded file covering all of Germany — no new download needed for this step) before proceeding, as a basic sanity check on the geocoding.

This is explicitly a smaller dataset than Bochum's 17 sites — Essen's own historical portal (historischesportal.essen.de) documents approximately 1,700 historical mining facilities citywide, and this round only digitizes the major, precisely-geocodable subset, an honestly-scoped limitation rather than a claim of completeness. I actually expanded an initial 3-mine/3-colony (6-site) version to the current 4-mine/4-colony (8-site) version after the confound-check result in Entry 11 suggested sample size might be materially affecting the result — worth documenting transparently rather than silently revising.

The OSM walking-network download itself (`download_network_essen.py`, new — same method as the original `download_network.py`, pointed at Essen) needed direct Overpass API access for the same reason above; running it locally produced a 72,027-node, 188,198-edge network with 1,410 essential-service points, before point-geometry filtering brought that down to 366 usable point locations, matching the original Bochum script's own point-geometry filter.

## Entry 11

With Essen's historical and network data ready, `run_essen_pipeline.py` (new) replicated Entries 3 through 6 end-to-end for Essen, reusing every parameter and method unchanged from the Bochum pipeline: the 1,125m/15-minute threshold, Welch's t-test, Essen Hauptbahnhof as the city-center reference, and KNN k=8 LISA with 99 permutations, seed=42.

88.5% of Essen's 72,027 nodes fell within a 15-minute walk of a service, versus Bochum's 85.8%. The raw reversed relationship replicated: low-access nodes (n=8,267) averaged 3,693m from the nearest historical site versus 3,130m for high-access nodes (n=63,760) — Welch's t=24.731, p<0.00001, Cohen's d=0.338 (smaller than Bochum's 0.589, but the same direction and highly significant). The Local Moran's I result replicated closely too: mean local I=0.917 (Bochum: 0.923), 95.5% of low-access nodes in significant LL cold-spot clusters (Bochum: 97.1%), and zero significant HH hot-spot clusters in either city.

The confound check, however, didn't replicate cleanly. Correlation between dist-to-historical and dist-to-center came out at r=0.405 in Essen versus r=0.063 in Bochum — a genuinely different result, not noise. The confound-controlled logistic regression's historical-site coefficient flipped sign in Essen (+0.0001, p<0.00001) relative to Bochum (-0.0005): once city-center distance is controlled for, greater distance from a historical site associates with higher, not lower, odds of accessibility in Essen. I checked this twice — the 6-site version of the dataset gave r=0.475 and a still-reversed coefficient; expanding to 8 sites reduced the correlation to r=0.405 but didn't eliminate the sign flip, suggesting sample-size/coverage-density inflation is a partial but not complete explanation.

## Entry 12

Consistent with the discipline I'd carried since Entry 7 — investigating unexpected results to a specific cause rather than suppressing or accepting them at face value — I didn't treat the Essen confound-check discrepancy from Entry 11 as a bug to fix or a result to downplay. I tested and documented two possible explanations rather than picking whichever was more convenient: first, a genuine difference in each city's own industrial-versus-administrative geography, since Essen's coal-mining history may be more spatially concentrated near its present-day center than Bochum's more dispersed sites; second, a sampling-density artifact of Essen's smaller (8 vs. 17-site) historical dataset. The correlation's measured decline from r=0.475 (6 sites) to r=0.405 (8 sites) as I added more sites is evidence consistent with the second explanation being at least a partial contributor, though it doesn't, on its own, rule out the first. Rather than force a conclusion either way, I documented both possibilities — and the specific evidence for each — in `GI_Research_Paper.md` Sections 4.6 and 7, and named expanding the Essen dataset further as Future Work rather than pursuing it further this round, given the practical geocoding-precision limits I'd already reached on Essen's remaining, less-documented historical mining sites.

The overall conclusion I drew from this multi-city round: the "path dependency of centrality" effect itself — the raw reversed relationship and its independent spatial-clustering corroboration — appears to generalize across at least these two Ruhr Valley cities. The narrower, stronger claim that this effect operates independently of city-center proximity is, on current two-city evidence, a Bochum-specific rather than universal finding. Reporting a genuinely mixed multi-city result in full — rather than only replicating the parts that confirm Bochum's own findings — felt like the more valuable and honest outcome of this round, consistent with how I've handled every prior unexpected result in this project.

## Entry 13

The Bochum overlay map was still the QGIS2Web export from early in the project, while Essen's equivalent had already been rebuilt directly in Python (folium) — an inconsistency worth fixing since both cities' underlying data and analysis were otherwise on equal footing.

I rebuilt `outputs/maps/bochum_interactive_map.html` from the same source geopackages (the Bochum accessibility, coal mine, and Zechensiedlungen geopackages, plus the GADM boundary filtered to Bochum) using the identical style I'd established for the Essen map: dark CartoDB tiles, an orange "industry"-icon marker per coal mine and a light-blue "home"-icon marker per worker colony, each with a click popup showing name, district, and active/construction years, and the 9,858 low-15-minute-accessibility nodes rendered as a heatmap layer rather than individual markers, since that many live points would overwhelm the browser the same way Essen's 8,267 would have. The city-boundary outline uses the same teal/cream style as Essen's.

One difference from Essen's popups: Essen's markers include a source-citation line (the KuLaDig/Wikipedia references I gathered during that city's digitization); Bochum's source geopackages don't carry a per-site citation field, so Bochum's popups show name, district, and dates only. Nothing about the underlying digitized site locations or dates changed — only the export mechanism.

No underlying data changed as part of this rebuild — the core datasets for Bochum (historical site digitization, the 69,393-node accessibility network, the city boundary) are the same inputs the original QGIS export used. This was purely a rendering/tooling fix: replacing a bulky, multi-file QGIS2Web export with a single self-contained HTML file generated straight from the project's own geopackages, consistent with how Essen's map — and every interactive map across the portfolio now — is built.

I updated `dashboard/pages/6_Interactive_Maps.py` to embed the new Bochum map the same way Essen's is embedded — reading the local HTML file and rendering it via `components.html`, instead of an iframe pointing at the old QGIS2Web export folder — updated its map legend text, and updated `README.md`'s map links and tech stack to drop the now-retired QGIS/QGIS2Web references.

Both cities' interactive maps are now built the same way, from the same kind of source data, with the same visual language — no QGIS dependency left anywhere in the interactive-map pipeline for either city.
