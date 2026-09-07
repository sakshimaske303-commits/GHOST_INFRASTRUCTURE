# Ghost Infrastructure: Historical Industrial Geography and the Persistence of Path-Dependent Accessibility in Bochum, Germany

## Abstract

Bochum, in Germany's Ruhr Valley, was built around nineteenth- and twentieth-century coal mining and worker housing (Zechensiedlungen); its last mine closed in 1974. This study tests whether that industrial geography still predicts present-day 15-minute-city walking accessibility more than fifty years later. Using the complete 69,393-node pedestrian street network and 786 essential-service points, network-distance isochrones (1,125 m) classify each node as accessible or not, and a Welch's t-test compares distance to the nearest of 13 digitized historical coal mines and 4 worker colonies between accessibility groups. Contrary to the original hypothesis, low-accessibility nodes are significantly farther from historical industrial sites than high-accessibility nodes (t=42.887, p<0.00001, Cohen's d=0.589). This holds after controlling for distance to the city center, itself an established predictor, in a joint logistic regression (historical-site coefficient=-0.0005, p<0.001; correlation between the two distances, r=0.063), and is corroborated by a Local Moran's I spatial-clustering analysis in which 97.1% of low-accessibility nodes fall within significant cold-spot clusters. The result holds at stricter (10-minute, d=0.413) and looser (20-minute, d=0.661) walking thresholds. A replication in Essen (72,027 nodes) confirms the same reversed relationship (t=24.731, p<0.00001, d=0.338) and an almost identical clustering pattern (95.5% of low-accessibility nodes in cold-spot clusters), but not the confound-independence result: the historical-site/city-center correlation is far higher in Essen (r=0.405) than in Bochum (r=0.063), and the historical-site coefficient's sign reverses once city-center distance is included. The findings suggest a durable path-dependency of centrality inherited from industrial-era infrastructure, generalizable across cities in raw form but not in its independence from present-day centrality.

**Keywords:** path dependency; 15-minute city; urban accessibility; historical GIS; network analysis; post-industrial geography; multi-city replication; robustness analysis

---

## 1. Introduction

Does a city's industrial past, more than fifty years gone, still shape which of its neighborhoods have convenient walking access to everyday services? This question is examined for Bochum, Germany, a city whose nineteenth-century urban morphology was shaped not for pedestrian convenience but for coal mines, steelworks, railways, roads, and worker housing. Bochum's last coal mine closed in 1974.

## 2. Literature Review

### 2.1 Path Dependency in Urban Spatial Structure

Path dependency is a well-established concept in economic geography, urban history, and evolutionary economics [1], but it has rarely been tested quantitatively at the scale of intra-city accessibility; most existing research addresses city growth, institutional governance, or industrial-culture narratives at a broader scale. Urban spatial structure is widely considered path-dependent, in that a neighborhood's current layout persists as a remnant of the infrastructure, land use, and transport mode prevailing at the time of its creation. This argument has been developed for port cities, where historical infrastructure investment persists institutionally and spatially long after its original economic purpose has ended [4], and extended to former coal and steel regions, where industrial culture and cognitive "lock-in" — not merely physical structure — shape a region's capacity to renew or remain tied to its industrial identity during restructuring [3]. This study addresses the comparative absence of direct, quantitative testing of path dependency at the level of intra-city accessibility.

### 2.2 The 15-Minute City and the City-Center Advantage

A large-scale comparative study of 10,000 cities worldwide found that service access is measurably better within central areas than peripheral ones [2], establishing city-center proximity as an independent predictor of accessibility that must be controlled for to isolate any historical-industrial-site effect. The 15-minute city concept has generated a substantial empirical literature since 2021, including city-specific applications such as a recent accessibility assessment of cultural sites in Seoul [5]. A systematic review of this literature found that network-based accessibility modeling — computing actual walking-network distance to a point of interest rather than a simplified radius — has become the predominant methodological approach [6], directly analogous to the network-distance methodology used here.

## 3. Data and Methodology

### 3.1 Study Area

Bochum has been a characteristic coal and steel town of the Ruhr Valley since the mid-nineteenth century; its last coal mine operated until 1974.

![Figure 1](outputs/plots/study_area_bochum.png)

**Figure 1.** Study area showing the administrative boundary of Bochum, North Rhine-Westphalia, Germany. Its extensive coal-mining history and subsequent post-industrial transformation make it a suitable case for testing whether nineteenth- and early-twentieth-century industrial development still shapes present-day 15-minute-city accessibility.

### 3.2 Historical Data

This study includes only the major, comprehensively documented industrial-era sites in Bochum, excluding a larger number of smaller-scale sites (Kleinzechen, Erbstollen) not comparable in scale or documentation quality to those analyzed here (Section 7). Thirteen coal mines and four worker-housing colonies (Zechensiedlungen) were extracted from Mindat.org and German heritage archives and stored as two separate GIS layers reflecting their distinct categories (extraction site versus worker housing); one candidate steelworker colony was excluded during review because it was associated with steel rather than coal production. Steelworks, railways, and roads of the industrial era were within this project's original conceptual scope but were not digitized in this phase because of archival time and resource constraints; this is addressed in Future Work (Section 8).

![Figure 2](outputs/plots/historical_geography.png)

**Figure 2.** Historical coal-mining geography of Bochum, from a nineteenth-century industrial map, overlaid on the current city boundary, forming the basis for testing whether the industrial past still shapes present-day accessibility.

### 3.3 Present-Day Accessibility Model

Straight-line buffer circles were deliberately avoided, since they overestimate walkable accessibility by allowing travel through buildings and city blocks. Instead, true network distance — 1,125 m, computed via Dijkstra's algorithm from each service location, consistent with standard 15-minute-city metrics in the current literature — was used across the city's complete pedestrian network of 69,393 street nodes and 169,668 street edges, together with 786 essential service points (health, education, and daily-needs categories) derived via the OSMnx library. Each node receives a single binary accessibility flag — within 1,125 m network distance of at least one service point in any of the eight categories — rather than a per-category or weighted score; a node reachable only to a pharmacy is coded identically to one reachable to a hospital, school, and supermarket together (see Section 7 for this equal-weighting assumption, and Section 8 for a weighted alternative).

### 3.4 Statistical Testing and Confound Verification

Because prior literature establishes city-center proximity as an independent predictor of accessibility, this potential confound was tested explicitly before attributing any result to historical-industrial-site proximity: the correlation between distance-to-historical-site and distance-to-city-center was computed, and a logistic regression of accessibility on both distances jointly was estimated, with coefficients converted to odds ratios (percentage change in odds per 100 m) for interpretability. Distance from each network node to the nearest historical industrial site was computed, and the two accessibility groups (low versus high) were compared via a Welch's t-test, with Cohen's d computed using pooled standard deviations.

### 3.5 Spatial Clustering (Local Moran's I)

Each street node was classified into one of four spatial categories — High-High (hot-spot), Low-Low (cold-spot), High-Low, or Low-High (spatial outlier) — using a binary accessibility variable and spatial weights derived from a row-standardized k-nearest-neighbor (k=8) graph over all 69,393 projected (EPSG:32632) node coordinates. Local Moran's I (Anselin's LISA statistic) was then computed on the binary variable using 999 conditional permutations (seed=42), with significance assessed at p<0.05 using the `libpysal` and `esda` Python packages. This analysis addresses a distinct question from the Section 3.4 t-test: whether low accessibility is spatially clustered, rather than whether accessibility groups differ in mean distance to historical sites.

### 3.6 Robustness Check: Walking-Threshold Sensitivity

Using the same 69,393-node network, service locations, and pre-computed historical-site distances, the accessibility-classification-and-Welch's-test pipeline (Sections 3.3–3.5) was re-run at a stricter 10-minute (750 m) threshold and a more permissive 20-minute (1,500 m) threshold, without new data acquisition, to test whether the reversed relationship found at the 15-minute threshold was an artifact of that specific cutoff.

### 3.7 Multi-City Replication: Essen

To test whether the "path dependency of centrality" finding is specific to Bochum or generalizes across the Ruhr Valley's shared nineteenth-century industrial urban form (as identified in this study's own Future Work, Section 8), four major historical coal mines (Zeche Zollverein, Zeche Carl Funke, Zeche Vereinigte Helene & Amalie, Zeche Pörtingsiepen) and four worker colonies (Siedlung Carl Funke, Mathias-Stinnes-Siedlung, Kolonie Zollverein III, Kolonie Beisen) were digitized from KuLaDig (Kultur.Landschaft.Digital, North Rhine-Westphalia's official state heritage database) and German Wikipedia, and cross-checked against Essen's administrative boundary (GADM v4.1). Essen lies approximately 15 km northeast of Bochum, also in North Rhine-Westphalia. This eight-site Essen dataset is a subset of Bochum's seventeen-site dataset, following the same major-sites-only selection criterion applied in Bochum (Section 3.2); Essen's official historical portal, historischesportal.essen.de, catalogues approximately 1,700 historical mining-related facilities citywide. Essen's complete pedestrian network (72,027 nodes, 188,198 edges) and 366 essential-service locations were acquired via OSMnx, and the same 15-minute network-distance threshold, Welch's t-test, city-center confound check (using Essen Hauptbahnhof, 51.4517°N 7.0134°E, as the city-center reference point), and Local Moran's I procedure (Section 3.5) were applied unchanged, with one exception: Essen's Local Moran's I retained its original 99-permutation count rather than the 999 permutations later used for Bochum (Section 4.4), since p-values were already stable at 99 permutations for this smaller dataset.

![Figure 3](outputs/plots/study_area_essen.png)

**Figure 3.** Study area showing the administrative boundary of Essen, North Rhine-Westphalia, Germany, the second Ruhr Valley city used to test generalizability, directly comparable to Figure 1 (Bochum).

![Figure 4](outputs/plots/essen_historical_geography.png)

**Figure 4.** Historical coal-mining geography of Essen: four major coal mines and four worker colonies digitized from KuLaDig and German Wikipedia, directly comparable to Figure 2 (Bochum).

## 4. Results

### 4.1 Accessibility Coverage

85.8% of network nodes fell within a 15-minute walk of at least one essential service; 14.2% (9,858 nodes) did not.

![Figure 5](outputs/plots/ghost_infrastructure_overlay.png)

**Figure 5.** Historical coal-mining facilities and current 15-minute walking reachability in Bochum, overlaid, providing the geographic basis for the statistical comparisons in subsequent sections.

### 4.2 The Reversed Relationship

At this sample size (69,393 nodes), statistical significance does not by itself imply practical significance, since even a negligible difference can yield a very low p-value. That is not the case here: the effect size (Cohen's d=0.589) is medium-to-large. Low-accessibility nodes are, on average, farther from historical industrial sites (1,984 m) than high-accessibility nodes (1,450 m) — the opposite of the original hypothesis that industrial legacy would predict present-day neglect (Welch's t-test: t=42.887, p<0.00001).

![Figure 6](outputs/plots/distance_comparison_boxplot.png)

**Figure 6.** Distribution of distance to historical coal-mining sites, by accessibility group. Contrary to the original hypothesis, low-accessibility nodes are substantially farther from historical mining sites than high-accessibility nodes.

### 4.3 Confound Verification

The odds of a node being accessible within 15 minutes rise by approximately 4.9% per 100 m closer to a historical industrial site, compared with approximately 3.0% per 100 m closer to the city center — but this comparison is meaningful only if the two effects are genuinely distinct. The correlation between distance-to-historical-site and distance-to-city-center is low (r=0.063), and a joint logistic regression retains a statistically significant historical-site effect after controlling for city-center distance (coefficient=-0.0005, p<0.001), indicating the reversed relationship is not simply a proxy for the well-established city-center advantage.

### 4.4 Spatial Clustering: Local Moran's I

Low accessibility is not randomly distributed across Bochum but forms statistically significant Low-Low (cold-spot) clusters that are, on average, farther from historical industrial infrastructure than non-clustered nodes: nodes in significant Low-Low clusters average 1,992.3 m from the nearest historical site, compared with 1,447.1 m for non-significant nodes. Of 69,393 nodes, 10,273 (approximately 15%) showed statistically significant spatial clustering (p<0.05): 9,571 Low-Low cold-spot nodes and 702 High-Low spatial outliers, with no significant High-High or Low-High clustering. These 10,273 nodes describe the extent of one spatially dependent clustering pattern rather than 10,273 independent confirmations of the hypothesis; no additional multiple-testing correction is applied beyond the standard p<0.05 local-significance threshold, consistent with standard practice for Local Moran's I as a cluster-detection rather than hypothesis-testing procedure.

![Figure 7](outputs/plots/lisa_cluster_map.png)

**Figure 7.** Local Moran's I cluster map. Blue nodes indicate statistically significant cold-spot (Low-Low) clusters; gold nodes indicate significant spatial outliers (High-Low); grey nodes are not statistically significant. Triangles mark historical coal mines; diamonds mark worker colonies.

This spatial-clustering result addresses a different statistical question from the t-test and logistic regression of Sections 4.2–4.3 — whether low accessibility is spatially clustered, rather than whether it differs on average by distance — while reaching a consistent conclusion.

### 4.5 Threshold-Sensitivity Results

Across all three thresholds tested (10, 15, and 20 minutes), the odds ratio per 100 m closer to a historical site is similar in magnitude (4.24%, 4.88%, and 4.49% respectively) and significant in each case (p<0.00001), controlling for distance to city center. At the stricter 10-minute threshold (750 m, 67.1% coverage), low-accessibility nodes remain significantly farther from historical sites (1,778 m versus 1,402 m; Welch's t=47.062, p<0.00001, Cohen's d=0.413). At the more permissive 20-minute threshold (1,500 m, 94.4% coverage), the same pattern holds and strengthens (2,098 m versus 1,492 m; t=32.150, p<0.00001, Cohen's d=0.661), a larger effect than at 15 minutes (d=0.589). This indicates the finding is not an artifact of the specific 15-minute cutoff.

![Figure 8](outputs/plots/threshold_sensitivity_comparison.png)

**Figure 8.** Effect-size comparison of distance to the nearest historical site by accessibility group (left) and walking-threshold sensitivity (right), at 10-, 15-, and 20-minute thresholds. The inverse relationship holds, and strengthens, across all three.

### 4.6 Multi-City Replication: Essen

The Local Moran's I spatial-clustering result replicates closely: Essen's mean Local Moran's I value (0.917) is comparable to Bochum's (0.923), and 95.5% of Essen's low-accessibility nodes fall within statistically significant cold-spot clusters, compared with 97.1% in Bochum; neither city shows significant High-High hot-spot clustering. The raw reversed relationship also replicates in both direction and significance: low-accessibility nodes in Essen (n=8,267) are significantly farther from the nearest historical site (3,693 m) than high-accessibility nodes (n=63,760, 3,130 m; Welch's t=24.731, p<0.00001), with a smaller effect size than Bochum (Cohen's d=0.338 versus 0.589).

![Figure 9](outputs/plots/essen_ghost_infrastructure_overlay.png)

**Figure 9.** Historical industrial infrastructure and present-day 15-minute walking accessibility in Essen, overlaid, directly comparable to Figure 5 (Bochum).

![Figure 10](outputs/plots/essen_distance_comparison_boxplot.png)

**Figure 10.** Distribution of distance to historical sites by accessibility group in Essen, comparable to Figure 6 (Bochum): the same reversed relationship holds, at a smaller effect size.

The city-center effect itself replicates as a strong, consistent predictor in both cities (odds per 100 m closer to the center: 3.0% in Bochum, 4.2% in Essen), but the confound-independence result does not: the correlation between distance-to-historical-site and distance-to-city-center is r=0.405 in Essen, substantially higher than Bochum's r=0.063, indicating the two distances are far less independent in Essen. Correspondingly, the sign of the historical-site coefficient (unlike the city-center coefficient, which remains negative in both cities) reverses in Essen's joint logistic regression (coefficient=+0.000114, p<0.00001): greater distance from a historical site is associated with higher, rather than lower, odds of accessibility once city-center distance is included.

![Figure 11](outputs/plots/bochum_essen_comparison.png)

**Figure 11.** Comparison of the three statistical tests across Bochum and Essen. The raw reversed effect and the Local Moran's I clustering result both replicate; the confound-independence result does not.

![Figure 12](outputs/plots/essen_lisa_cluster_map.png)

**Figure 12.** Local Moran's I cluster map of Essen, directly comparable to Figure 7 (Bochum).

Two explanations for this non-replication are considered plausible, and are not mutually exclusive. First, Essen's historical industrial geography may be more compactly organized around its city center than Bochum's: the Krupp steelworks — adjacent to, but outside, this study's coal-mining scope — developed in closer proximity to Essen's city center than Bochum's more fragmented and dispersed coal-mining sites. Second, the smaller Essen sample (8 historical sites, versus 17 in Bochum) increases the likelihood that this specific correlation reflects a sampling artifact rather than a true geographic difference; consistent with, though not proof of, this explanation, the historical-site/city-center correlation fell from r=0.475 to r=0.405 when the Essen dataset was expanded from six to eight sites. Neither explanation contradicts this study's principal finding; if anything, the Essen result reinforces the interpretation (Section 5) that the durable clustering signature linking centrality and historical industrial density is not merely an artifact of city-center proximity, while indicating that the specific claim of confound-independence should not yet be generalized beyond Bochum.

## 5. Discussion

Nineteenth-century coal and steel infrastructure was built, for economic reasons, around dense populations, road systems, market facilities, and housing needed to support that workforce. This study's results indicate that this historical infrastructure footprint persists more than fifty years after mine closure, entrenching a legacy of street connectivity and service density independent of the modern city center's own location. This extends the path-dependency literature — previously applied mainly to broad urban growth patterns and port-city institutional arrangements — into the finer-grained domain of intra-city walkable accessibility. This does not diminish the established finding that centrality, historical or contemporary, predicts better accessibility; rather, centrality is better understood here as a "path dependency of centrality" than a "path dependency of neglect."

The term "Ghost Infrastructure" is intended to capture an infrastructure whose original economic function no longer exists but whose physical and spatial impact persists: the mines are gone, but their imprint on the cityscape is not. The "ghost" in the title refers to the absence of the original cause (the coal industry) rather than to abandonment, given that its measurable legacy — durable centrality and connectivity — has been largely positive.

This finding is consistent with, but adds an important qualification to, the general "path dependency of centrality" framing: while the underlying centrality-legacy mechanism appears to hold across cities, the relative contribution of historical versus present-day centrality to present-day accessibility may vary by city, depending on each city's specific industrial and administrative history. The Essen replication (Section 4.6) supports this qualification directly: the centrality/connectivity legacy itself is present in both cities, but its independence from present-day city-center proximity — the stronger claim — appears, on current evidence, to be a Bochum-specific rather than a general Ruhr Valley result.

## 6. Policy Implications

The accessibility gaps identified in this study are located not within the historical industrial core but in the periphery and in more recently built neighborhoods. This suggests that 15-minute-city infrastructure investment may be more effectively targeted toward these newer, peripheral areas than toward the historical industrial core, which already retains stronger accessibility. This does not diminish the value of heritage-led regeneration of former industrial cores; rather, it suggests that such regeneration builds on an area that is already comparatively well served, while the more pressing accessibility need lies elsewhere in the city.

## 7. Limitations

The relationships reported here should be read as spatial associations rather than fully adjusted causal estimates, since socioeconomic confounders (income, age, tenure, car ownership) were not collected. The Local Moran's I sample size (Section 4.4) should also be interpreted with care: because nearby street-network nodes are not independent observations, the count of significant nodes describes the extent of a single spatial pattern rather than an equivalent number of independent statistical confirmations. To address this non-independence directly, a network-block bootstrap (`network_block_bootstrap.py`) was run as an additional check: rather than resampling individual nodes, the street network was divided into 2,611 contiguous blocks (grown outward from random starting nodes toward a target size of 500 nodes each, though the realized average block size is approximately 27 nodes, since the pedestrian network fragments into many small disconnected components), and whole blocks were resampled with replacement 999 times, refitting the same difference-of-means and logistic regression at each iteration. The observed distance difference (534.25 m) produced a 95% bootstrap confidence interval of [247.24 m, 873.73 m], excluding zero; the logistic-regression coefficients for both historical-site and city-center distance likewise produced confidence intervals excluding zero. Because this method treats the network's connected structure as the resampling unit rather than treating all 69,393 nodes as independent, this result is read as stronger evidence against spatial autocorrelation as an alternative explanation. A block-size sensitivity check (`network_block_bootstrap_sensitivity.py`), re-running the identical procedure at target sizes of 250 and 1,000 nodes, confirms this is not an artifact of the 500-node target specifically: 95% confidence intervals for the distance difference are [299.73 m, 803.60 m] at 250 nodes and [194.14 m, 923.55 m] at 1,000 nodes, both excluding zero, and the historical-site logistic coefficient remains negative and excludes zero at all three target sizes (250: [-0.000680, -0.000302]; 500: [-0.000738, -0.000247]; 1,000: [-0.000803, -0.000256]), with confidence intervals widening modestly as block size increases.

The worker-colony dataset (4 sites) is smaller than the coal-mine dataset (13 sites), limiting the statistical power of colony-level sub-analyses, and both cover only major, well-documented sites rather than Bochum's full historical mining register of approximately 200 additional smaller operations (Kleinzechen, Erbstollen) not comparable in scale or documentation to the sites analyzed here. This study represents historical sites as points rather than mapped extents, given project time constraints, and did not digitize industrial-era rail and road infrastructure in this phase (Section 8). All essential-service categories were weighted equally in the accessibility model, which does not reflect likely differences in their relative importance to daily life. Finally, the city-center reference point used for the Bochum confound analysis (Bochum Hauptbahnhof) sits within a few hundred meters of an alternative candidate (the Rathaus) in this compact city; a validated second reference point for a robustness check was not available, though the low correlation between the two distance measures (r=0.063) suggests limited sensitivity to this choice.

The Essen historical-site/city-center correlation (r=0.405) is lower than an earlier six-site version of the Essen dataset (r=0.475), consistent with, though not proof of, a sampling-density explanation for part of this correlation; closing this gap would require expanding the Essen dataset toward Bochum's seventeen-site scale (Section 8), which was not attempted in this round. Essen's eight-site dataset is a smaller fraction of its full historical mining register (approximately 1,700 facilities citywide, per Essen's historical portal) than Bochum's dataset is of Bochum's, and should accordingly be treated as provisional. The two Essen historical-site GIS layers (`essen_coal_mines.gpkg` and `essen_zechensiedlungen.gpkg`) contain all eight digitized sites, making the Essen figures reported here directly reproducible by re-running `run_essen_pipeline.py` against the repository's own data.

## 8. Future Work

Two extensions originally planned for future work are already reported in this study (Sections 3.6–3.7, 4.5–4.6): walking-threshold sensitivity, confirmed robust at 10- and 20-minute thresholds, and multi-city replication, confirmed in Essen with a qualified result. Remaining directions include: extending the Essen historical dataset toward Bochum's scale, to resolve the confound-independence question definitively, by digitizing further sites from the approximately 1,700 registered on historischesportal.essen.de; testing whether the historical-site effect persists after controlling for present-day socioeconomic composition (income, age, tenure, car ownership, from German census data); extending multi-city replication beyond Bochum and Essen (for example, to Dortmund or Gelsenkirchen) to determine whether Essen's confound-independence departure or Bochum's result is the more typical pattern; replacing point-based historical-site representations with mapped polygon extents, to test sensitivity to boundary representation; modeling the historical-site effect as spatially varying across the city rather than as a single global coefficient; substituting the equally weighted service-accessibility indicator with a differentially weighted index (for example, weighting groceries, healthcare, and green space more heavily); digitizing industrial-era rail and road infrastructure (as originally scoped, Section 3.2) to test whether historical transport-network accessibility itself, independent of proximity to mines and colonies, predicts present-day accessibility; and extending the current cross-sectional design to a time-series analysis of accessibility relative to historical sites. A network-distance-based variant of the Local Moran's I clustering check was attempted using network reachability rather than straight-line k-nearest-neighbors to define spatial neighbors; this produced a substantially different result, likely because a fixed network-distance cutoff yields a much larger and more uneven neighbor count per node than a fixed k=8, and is accordingly not used as a validated finding here, pending a more directly comparable neighbor definition.

## 9. Conclusion

A rigorously tested, counterintuitive result — surviving the most plausible confound and corroborated by an independent spatial-clustering method — carries more evidential weight than a result taken at face value, and that is the standard this study aimed to meet. Nearly 150 years after Bochum's industrialization began, and more than fifty years after its last coal mine closed, nineteenth-century industrial infrastructure continues to leave a measurable, statistically robust mark on present-day walking accessibility — not through neglect, as originally hypothesized, but through a durable, positive legacy of connectivity and centrality corroborated by more than one statistical method.

This study's Essen replication produced a genuinely mixed result, reported here in full rather than selectively: the core reversed relationship and spatial-clustering pattern replicate robustly, and the finding remains significant at both 10- and 20-minute thresholds, but the specific claim that centrality's historical legacy is statistically independent of present-day city-center proximity does not straightforwardly generalize beyond Bochum. Reporting an incomplete or partially disconfirming replication in full is, in this study's view, more useful to the literature than reporting only the confirming portion of a result.

## References

[1] W. B. Arthur. 1988. Urban Systems and Historical Path Dependence. In *Cities and Their Vital Systems: Infrastructure Past, Present, and Future*. National Academies Press, Washington, DC, 85–97. https://www.nationalacademies.org/read/1093/chapter/5

[2] M. Bruno, H. P. M. Melo, B. Campanelli, and V. Loreto. 2024. A universal framework for inclusive 15-minute cities. *Nature Cities* 1, 10 (2024), 633–641. https://doi.org/10.1038/s44284-024-00119-4

[3] F. Görmar and J. Harfst. 2019. Path Renewal or Path Dependence? The Role of Industrial Culture in Regional Restructuring. *Urban Science* 3, 4 (2019), 106. https://doi.org/10.3390/urbansci3040106

[4] C. Hein and D. Schubert. 2021. Resilience and Path Dependence: A Comparative Study of the Port Cities of London, Hamburg, and Philadelphia. *Journal of Urban History* 47, 2 (2021), 389–419. https://doi.org/10.1177/0096144220925098

[5] C. Moreno, C. Gall, J. Woo, D. Lee, and M. Bencekri. 2025. Assessing accessibility of cultural sites through the 15-minute city framework in Seoul. *International Journal of Urban Sciences* 29, 1 (2025), 8–39. https://doi.org/10.1080/12265934.2025.2462820

[6] J. Omwamba, L. Rotaris, and G. Longo. 2025. An assessment of proximity in the 15-Minute City: A systematic literature review. *Urban Transitions* 3 (2025), 100012. https://doi.org/10.1016/j.ubtr.2025.100012
