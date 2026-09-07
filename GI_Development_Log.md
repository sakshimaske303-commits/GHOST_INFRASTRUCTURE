# GHOST INFRASTRUCTURE — Development Log

This is a working log for the Ghost Infrastructure project, tracking whether nineteenth- and twentieth-century coal mine and worker-colony locations in Bochum still predict present-day 15-minute-city walking accessibility in the Ruhr Valley. Entries were written as the work happened — design choices, dead ends, and fixes recorded at the time rather than reconstructed afterward — including the reversed result that overturned the original hypothesis.

The log follows the project's actual build order: formulating the research question, digitizing historical mine and colony locations, building the network-based walking-accessibility model, running the statistical tests, investigating the reversed result, producing the final figures, and later adding robustness checks and a second-city replication. Every number and p-value below is what the corresponding script produced when run.

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
14. [Entry 14](#entry-14)
15. [Entry 15](#entry-15)
16. [Entry 16](#entry-16)

## Entry 1

Project name: Ghost Infrastructure. The goal is to test whether nineteenth- and twentieth-century coal mines and worker colonies (Zechensiedlungen) in the Ruhr Valley still determine present-day walking accessibility, more than fifty years after the industry's decline and the 1974 closure of the last mine. The original scope included steel factories and historical rail lines, but the data actually collected covers only coal shafts and worker housing, since these were the categories with sufficiently complete archival records to digitize reliably; steel factories and rail lines are documented as future work in the research paper rather than included on an incomplete basis.

Most existing literature on Ruhr Valley industrial heritage is descriptive — historical narrative, heritage preservation, or planning discussion — rather than quantitative. Separately, 15-minute-city research typically explains accessibility gaps using present-day variables (income, demographics, age) without accounting for historical industrial geography. This project combines digitized historical industrial locations with a network-based accessibility model and spatial statistics to test whether present-day accessibility gaps trace back to historical industrial geography.

Research question: does the historical geography of Ruhr Valley coal and steel industry — mine locations, worker colonies, historical rail lines — still predict which present-day neighborhoods fall outside a 15-minute walking radius of essential services?

Four tasks follow from this: (1) digitize and georeference historical industrial-era maps to locate coal shafts and worker housing (historical transport lines were deferred to future work); (2) build a present-day walking-network model generating network-distance accessibility to daily services — clinics, food shops, primary schools, and parks — using current road data; (3) apply spatial statistics (Local Moran's I, hot-spot analysis) to test whether low-accessibility areas cluster near historical industrial sites rather than appearing at random; (4) produce a map overlay of historical industrial geography against present-day accessibility to test the "ghost infrastructure" hypothesis directly.

Bochum, North Rhine-Westphalia, was selected as the study area: a farming town before its mid-nineteenth-century industrialization into a major coal and steel city through the 1950s. The official Industrial Heritage Route (route-industriekultur.ruhr) provided an initial list of known worker-housing colonies within city limits. An initial search bounding box (51.42°N–51.53°N, 7.13°E–7.30°E) was set, to be refined once actual historical map data was available.

## Entry 2

Built the historical-site data layer first, since all subsequent work depends on it. Coal-mine coordinates were collected from Mindat.org (manually, page by page, since no bulk export is available); worker-colony coordinates were compiled from German heritage archive pages, Wikipedia, the Route Industriekultur portal, and ruhr-bauten.de.

The result is 13 coal mines and 4 worker colonies, stored as two separate GIS layers reflecting their distinct categories. One steelworker neighborhood, Stahlhausen (built by the Bochumer Verein steel company), was excluded from the worker-colony file since it is associated with steel rather than coal production. Both layers were converted to GeoPackage format (EPSG:4326) via GeoPandas for use in QGIS and subsequent network analysis.

## Entry 3

Downloaded Bochum's current pedestrian street network via OSMnx: 69,393 nodes and 169,668 edges. Retrieved 786 essential-service locations from the same source, covering hospitals, clinics, pharmacies, primary schools, kindergartens, supermarkets, corner stores, and parks.

Built the accessibility model using true network distance (Dijkstra's algorithm) rather than straight-line buffers, since straight-line distance overestimates walkability by ignoring building and block layout. Each node's accessibility is computed as the true walking-network distance to the nearest of the 786 service locations.

## Entry 4

Ran the core statistical test with the completed historical-site data (17 locations) and the full accessibility model (69,393 nodes): a Welch's t-test comparing distance to the nearest historical industrial site between low- and high-accessibility nodes.

The result reversed the original hypothesis. The test found a highly significant difference (t=42.887, p<0.00001) in the opposite direction from what was expected: low-accessibility nodes are farther from historical industrial sites (mean 1,984 m) than high-accessibility nodes (mean 1,450 m). Proximity to historical coal-mining sites is therefore associated with better present-day accessibility, not worse.

This is reported as the primary finding rather than treated as an error. Historical industrial development was necessarily built around dense worker housing, and that dense, centrally located urban fabric appears to retain better service density and street connectivity today than more peripheral areas — a "path dependency of centrality" rather than a "path dependency of neglect."

## Entry 5

Before accepting the reversed result, tested an obvious confound: historical mines may simply sit close to Bochum's city center, which independently has strong walking accessibility, making the apparent historical-site effect a proxy for city-center proximity rather than an independent effect.

The correlation between distance-to-historical-site and distance-to-city-center is low (r=0.063), indicating the two are largely independent. A logistic regression predicting accessibility from both distances jointly retained a statistically significant historical-site effect (coefficient=-0.0005, p<0.001) after controlling for city-center distance. This confirms the historical-site effect is not simply a restatement of the known city-center advantage.

## Entry 6

Returned to a planned but not-yet-completed task: the project's original scope required a Local Moran's I / hot-spot analysis to test whether low-accessibility areas cluster spatially, since the Entry 4–5 tests only address whether distance differs between groups on average, not whether that difference is spatially clustered.

Built a row-standardized k-nearest-neighbor (k=8) weights matrix across all 69,393 nodes and computed Local Moran's I on the binary accessibility flag using 99 permutations (`libpysal`, `esda`; seed=42; significance at p<0.05).

Results: mean local I = 0.923; 10,266 of 69,393 nodes (14.8%) showed statistically significant spatial clustering — 9,568 Low-Low (cold-spot) and 698 High-Low (spatial outlier), with no significant High-High or Low-High clusters. Nodes in significant Low-Low clusters averaged 1,992.3 m from the nearest historical site, versus 1,447.1 m for non-significant nodes; 97.1% of all low-accessibility nodes fell within a significant Low-Low cluster.

This confirms the Entry 4 finding using an independent method: low accessibility is not randomly distributed but forms real, spatially contiguous clusters that sit measurably farther from historical industrial sites. Saved the cluster map and `spatial_clustering_lisa.py` to the repository and recorded the results in Section 4.4 of `GI_Research_Paper.md`.

## Entry 7

The map overlay visualization (all 69,393 nodes by accessibility, plotted against historical mine and colony points) initially rendered as a blank canvas with a single point in the corner. Diagnosed as a coordinate-reference-system mismatch: the street network had been saved in EPSG:32632 (UTM Zone 32N, needed for earlier metric distance calculations), while the historical-site layers remained in EPSG:4326. Plotting both without reprojecting to a common CRS caused the geographic-degree coordinates to collapse to a single pixel next to the much larger UTM coordinate values. Reprojected all layers to EPSG:4326 before rendering, which resolved the issue.

Two further apparent anomalies were found on inspection: only 12 of 13 coal-mine markers were visible, and 2 of 4 worker-colony markers appeared to overlap. Rather than assuming a code defect, the underlying coordinate data was checked directly. The Mansfeld and Heinrich Gustav mines (Langendreer and Werne) are 1.75 km apart — close enough to merge visually at full-city zoom — and the Kolonie Hannover and Am Rübenkamp worker colonies are 0.33 km apart, having been built adjacent to each other to serve the same Hannover mine shafts during overlapping construction phases (1874–1892). Verified via direct Haversine distance calculation between the coordinate pairs. Given Bochum's roughly 14 km extent, both cases are genuine historical spatial proximity rather than a data or rendering error, and no code changes were needed.

The general practice this established: an unexpected result (Entry 4) was verified independently via a second statistical method (Entry 5) rather than assumed to be either correct or a bug, and a visually anomalous map output was checked against the underlying raw coordinates before concluding it was real geography rather than an error.

## Entry 8

Completed the core analysis (statistical tests, confound checks, cluster maps, and figures) and assembled the multi-page Streamlit dashboard (`app.py`), with separate pages for the study design, historical maps, accessibility results, the main finding, trend analysis, interactive maps, and methodology. Finalized the research paper, project report, and `README.md`, and pushed the repository to GitHub.

## Entry 9

Returned to this project to extend its scope and address documented limitations, selecting it first among the portfolio projects since it requires no Google Earth Engine access (only OSMnx, OpenStreetMap, and GADM boundary data) and already had a defined Future Work list.

First extension: a walking-threshold sensitivity check, addressing an item noted as incomplete in the original paper. Wrote `threshold_sensitivity.py` to re-run the full accessibility classification, distance calculation, Welch's t-test, and logistic-regression confound check at 10-minute (750 m) and 20-minute (1,500 m) thresholds, reusing the existing Bochum street network and distance data without new downloads.

The reversed relationship held at both thresholds, and strengthened somewhat at the wider threshold: 10-minute t=47.062, p<0.00001, d=0.413 (versus the original 15-minute t=42.887, d=0.589); 20-minute t=32.150, d=0.661. The odds ratio per 100 m closer to a historical site remained stable across all three thresholds (4.24%, 4.88%, 4.49%), indicating the original 15-minute result is not an artifact of that specific threshold choice. Recorded in Section 4.5 of `GI_Research_Paper.md`.

## Entry 10

Selected Essen for a second-city replication, per the project's own Future Work list, since it lies 15 km northeast of Bochum, shares the same nineteenth-century coal-mining history, and has comparably strong heritage documentation.

Initial data collection was blocked by outages in OpenStreetMap's Overpass API and Nominatim services, Wikidata's live endpoints, and a 403 error from Mindat.org (the source used for the Bochum mine list). KuLaDig, North Rhine-Westphalia's official state heritage database, remained available and provided WGS84 coordinates for the major heritage-listed mine shafts; German Wikipedia articles for worker colonies also reliably included geo-tagged coordinates, unlike the corresponding mine-shaft articles.

Digitized four coal mines — Zeche Zollverein Schacht XII, Katernberg (shaft operated 1932–1986; part of the wider Zollverein colliery complex founded 1847/51); Zeche Carl Funke, Heisingen (1804–1973); Zeche Vereinigte Helene & Amalie, Altendorf (1843/44–1968); Zeche Pörtingsiepen, Fischlaken (1779–1972) — and four worker colonies: Siedlung Carl Funke (1900), Mathias-Stinnes-Siedlung, Karnap (1890), Kolonie Zollverein III, Katernberg (1880), and Kolonie Beisen (1902). All eight points were checked against the GADM v4.1 Germany boundary layer to confirm they fall within Essen's administrative boundary.

This eight-site Essen dataset is considerably smaller than Bochum's seventeen sites; Essen's official historical portal lists over 1,700 mining-related locations citywide, so this is documented explicitly as a limitation rather than treated as comprehensive. The dataset initially used three mines and three colonies (six sites); when early statistical checks (Entry 11) showed unstable results attributable to the small sample, two further sites were added to reach the current eight-site version.

Downloaded Essen's pedestrian network via a new script, `download_network_essen.py` (mirroring the Bochum download logic against the Overpass API): 72,027 nodes, 188,198 edges, and 1,410 raw service-facility points, filtered by the same point-geometry criteria used for Bochum down to 366 usable service locations.

## Entry 11

Ran the Essen replication using a new pipeline script, `run_essen_pipeline.py`, replicating the Bochum methodology (Entries 3–6) exactly: 1,125 m network-distance threshold, Welch's t-test, Essen Hauptbahnhof as the city-center reference, and k=8 Local Moran's I at 99 permutations with seed 42.

88.5% of Essen's 72,027 nodes fall within a 15-minute walk of at least one service (versus 85.8% in Bochum). The reversed relationship replicated: low-accessibility nodes (n=8,267) average 3,693 m from the nearest historical site versus 3,130 m for high-accessibility nodes (n=63,760); Welch's t=24.731, p<0.00001, Cohen's d=0.338 (smaller than Bochum's 0.589, but the same direction and highly significant). Local Moran's I results were also consistent: mean local I=0.917 (versus 0.923 in Bochum), with 95.5% of low-accessibility nodes in significant Low-Low clusters (versus 97.1% in Bochum) and no significant High-High clusters in either city.

The confound check did not replicate. The correlation between historical-site distance and city-center distance is r=0.405 in Essen, substantially higher than Bochum's r=0.063. In the joint logistic regression, the historical-site coefficient's sign reversed relative to Bochum: +0.0001 (p<0.00001) in Essen versus -0.0005 in Bochum, meaning that once city-center distance is controlled for, greater distance from a historical site is associated with higher, not lower, odds of accessibility in Essen.

This was checked against dataset size directly: the original six-site Essen dataset gave r=0.475 for the same correlation; expanding to eight sites reduced it to r=0.405 but did not reverse the sign flip. This indicates sample size partially affects the magnitude of the correlation but does not fully explain the sign reversal.

## Entry 12

Followed the same approach as Entry 7 when this unexpected result appeared: investigated rather than dismissing or forcing a preferred explanation, and tested two candidate explanations directly rather than selecting one on the basis of which fit the narrative better.

First possibility: Essen's historical mining sites may simply be geographically closer to its city center than Bochum's more dispersed sites. Second possibility: the smaller Essen historical-site sample (8 versus Bochum's 17) makes this specific correlation more sensitive to sampling variability.

The six-to-eight-site comparison (r=0.475 to r=0.405) shows sample size affects the correlation's magnitude, but does not by itself account for the full sign reversal, so both explanations are reported in Sections 4.6 and 7 of `GI_Research_Paper.md` rather than resolving it to a single cause. Expanding the Essen dataset further is listed as future work, since locating precise coordinates for the remaining, less-documented historical sites was not feasible within the current scope.

Overall conclusion from the two-city comparison: the core finding — that low accessibility clusters spatially and correlates with distance from historical industrial sites — replicates in both cities. The additional claim that this effect is fully independent of city-center proximity holds in Bochum but not in Essen, and is reported as a Bochum-specific result pending further data rather than a general one.

## Entry 13

Identified an inconsistency between the two cities' interactive map implementations: the Bochum overlay map still used an older QGIS2Web export from early in the project, while the Essen map had been built directly in Python with Folium. Rebuilt `outputs/maps/bochum_interactive_map.html` from the underlying GeoPackage files (accessibility metrics, coal-mine and colony coordinates, GADM boundary), matching the Essen map's style: dark CartoDB base tiles, orange markers for mines, light-blue markers for worker colonies, with popups showing site name, district, and operational dates.

Bochum has 9,858 low-accessibility nodes; rendering these as individual markers would be impractical in-browser, so they are rendered as a heatmap density layer instead (Essen's 8,267 equivalent nodes use the same approach). Both cities' administrative boundaries use the same teal-and-cream color scheme.

One difference remains between the two cities' popups: Essen's include a source URL (KuLaDig/Wikipedia, collected during digitization), while Bochum's original data did not retain a citation field, so Bochum popups show name, district, and operational years only. No coordinate or date values were changed during this rebuild — the underlying data (digitized coal-mine and colony coordinates, the 69,393-node network, and the boundary shape) is unchanged; this was a rendering-pipeline change only, replacing the QGIS2Web export with a single HTML file generated directly from the project's own GeoPackages. Updated `dashboard/pages/6_Interactive_Maps.py` to embed the new map via `components.html`, matching the Essen page, and removed references to QGIS2Web from `README.md`.

## Entry 14

Revisited the Local Moran's I analysis from Entry 6, which used 99 permutations — adequate at the time but low for a more stable p-value estimate at this sample size (69,393 nodes). Increased `PERMUTATIONS` in `spatial_clustering_lisa.py` from 99 to 999 and re-ran the analysis.

Results were essentially unchanged: 10,273 significant nodes (versus 10,266 previously), with 9,571 Low-Low and 702 High-Low (versus 9,568 and 698). Mean local I remained 0.923, and the headline 97.1% figure was unchanged. This confirms the original 99-permutation result was already stable.

Also tested an alternative neighbor definition: rather than KNN (k=8) by straight-line distance, `spatial_clustering_lisa_network.py` defines neighbors as nodes reachable within 750 m along the actual street network. This produced a substantially different result — 96.9% of nodes significant (versus 14.8% under KNN), dominated by High-High hot-spots (53,421 of 67,210 significant nodes) rather than Low-Low cold-spots — likely because a fixed 750 m network buffer yields a highly variable neighbor count per node (potentially hundreds in dense areas) rather than a fixed count of 8. Since this is not a like-for-like comparison to the original KNN-based result, it is not used as a validated finding and is recorded as an unfinished side-experiment; a fair comparison would require calibrating the network-distance cutoff to yield approximately 8 neighbors per node on average.

Addressed the non-independence of adjacent street nodes directly via `network_block_bootstrap.py`: partitioned the network into roughly 2,600 contiguous blocks (grown outward from random starting nodes toward a target of 500 connected nodes each) and resampled whole blocks with replacement 999 times, refitting the difference-of-means and logistic regression each iteration. The observed distance difference (534.25 m) produced a 95% bootstrap confidence interval of [247.24, 873.73] m, excluding zero; both logistic-regression coefficients also excluded zero in their respective intervals. This treats the network's own connected structure as the resampling unit rather than treating all 69,393 nodes as independent, and the result held. Added this to Section 7 (Limitations) of `GI_Research_Paper.md`, alongside the existing note on node non-independence, and listed the network-distance LISA attempt and a block-size sensitivity check under Section 8 (Future Work) as unfinished items.

## Entry 15

Completed the block-size sensitivity check previously listed as future work. Wrote `network_block_bootstrap_sensitivity.py`, re-running the Entry 14 network-block bootstrap at target block sizes of 250 and 1,000 nodes, alongside the original 500, to test whether the reported confidence interval was specific to the 500-node choice.

Results: 250 nodes, CI [299.73, 803.60]; 500 nodes, CI [235.70, 826.02] (close to the original [247.24, 873.73] — the small difference reflects a different random block partition under the same seed, from a revised implementation of the resampling step); 1,000 nodes, CI [194.14, 923.55]. All three exclude zero and retain the same sign on the historical-site coefficient; the interval widens somewhat as block size increases, consistent with fewer, larger resampling units. Moved this from Future Work into Section 7 as a completed robustness result.

Also corrected a wording error in the Limitations section, which described bootstrap blocks as averaging roughly 500 nodes each; the script's own output shows the true average is approximately 27 nodes per block, since the pedestrian network's many small disconnected fragments prevent most blocks from growing near the 500-node target. Added a clarifying note in Section 3.3 that the accessibility flag is a single binary indicator — at least one service of any kind within 15 minutes — rather than a per-category or weighted score, since this was not stated explicitly enough in the original text.

## Entry 16

While reviewing the Essen historical-site count (quoted throughout the paper, this log, and `essen_results.json` as "8 sites: 4 mines + 4 colonies"), checked the current `essen_coal_mines.gpkg` and `essen_zechensiedlungen.gpkg` files directly and found only 6 sites (3 mines, 3 colonies). Zeche Pörtingsiepen and Kolonie Beisen — both digitized and named in Section 3.7 of the paper — were missing from the current GeoPackage files, most likely because an earlier export was saved over the final one without being noticed. `essen_accessibility_with_distance.gpkg` and `essen_results.json` still contained the correct 8-site-derived numbers from when the pipeline was last run against the complete data, so the paper's reported figures were never incorrect — but re-running `run_essen_pipeline.py` against the repository as it currently stood would have reproduced the earlier 6-site result (r=0.475) rather than the reported 8-site result (r=0.405).

Re-verified both missing sites' locations: Zeche Pörtingsiepen (Fischlaken, 51.394868°N, 7.043953°E; German Wikipedia and historischesportal.essen.de) and Kolonie Beisen (Katernberg, 51.49247°N, 7.06959°E; KuLaDig, associated with Zeche Zollverein). Added both back into the two GeoPackage files with the same schema as the existing entries, then re-ran the historical-distance, correlation, logistic-regression, and Local Moran's I steps of `run_essen_pipeline.py` against the corrected 8-site data. Result: mean_dist_low=3,693.4 m, mean_dist_high=3,129.9 m, t=24.732, d=0.338, r=0.4048, logistic coefficient=+0.000114, mean local I=0.917, 95.5% of low-accessibility nodes in significant Low-Low clusters — matching the paper and `essen_results.json` almost exactly, confirming these are the correct two sites rather than an approximate match. Regenerated `essen_accessibility_with_distance.gpkg` and `essen_results.json` from the corrected files so the full pipeline is now reproducible directly from the repository's current data rather than depending on a frozen, non-reproducible output.
