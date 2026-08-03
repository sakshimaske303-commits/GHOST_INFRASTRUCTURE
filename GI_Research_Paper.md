# Ghost Infrastructure: Historical Industrial Geography and the Persistence of Path-Dependent Accessibility in Bochum, Germany

**Sakshi D. Maske**
Independent Geospatial Researcher

## Abstract

The theoretical concept of "path dependency" — that historical spatial decisions continue to shape present-day urban outcomes long after their original rationale has disappeared — is well established in economic geography, yet rarely tested with direct, quantitative spatial evidence, particularly at the scale of a single city's internal accessibility structure. This study tests whether Bochum's 19th and 20th-century coal-mining industrial geography — mine locations and worker-housing colonies (Zechensiedlungen) — continues to structurally predict present-day "15-minute city" walking accessibility, more than five decades after the region's last coal mine closed. Thirteen historical coal mines and four worker colonies were digitized from archival sources, and present-day accessibility was modeled using true network-distance isochrones across Bochum's complete 69,393-node pedestrian street network. Contrary to the hypothesis that historical industrial sites would predict present-day neglect, a Welch's t-test found the opposite: low-accessibility network nodes are significantly further from historical industrial sites than high-accessibility nodes (t=42.887, p<0.00001, Cohen's d=0.589, a medium-to-large effect). This reversed relationship was verified against its most obvious confound — proximity to the city center, a well-documented predictor of accessibility in the broader 15-minute-city literature — and found to hold independently (logistic regression coefficient=-0.0005, p<0.001, controlling for city-center distance; correlation between the two distance measures was low, r=0.063). A Local Moran's I spatial-clustering analysis independently corroborates this finding via a distinct statistical method: 97.1% of low-accessibility nodes fall within statistically significant spatial cold-spot clusters, confirming that low accessibility is not randomly distributed but forms genuine, spatially contiguous zones measurably farther from historical industrial infrastructure. The evidence supports a "path dependency of centrality" rather than a "path dependency of neglect": historical industrial infrastructure, built by necessity at the center of dense worker populations, appears to have left a durable legacy of street connectivity and service density that persists independently of the city's present-day center.

**Keywords**: path dependency, 15-minute city, urban accessibility, historical GIS, network analysis, post-industrial geography

---

## 1. Introduction

Bochum's urban form was never designed around human accessibility. It was built around coal mines and steel works, with railways, roads, and worker-housing colonies laid out to serve 19th-century industrial production. The last coal mine in Bochum closed in 1974. This study asks whether that historical industrial geography — more than half a century removed from its original economic function — continues to leave a measurable, statistically detectable imprint on which parts of the city today offer genuine walkable access to essential services.

## 2. Literature Review

### 2.1 Path Dependency: A Well-Established Theory, Rarely Tested Spatially

Path dependency — the principle that the past shapes the present through locked-in infrastructure and institutional decisions — is a long-established concept spanning economic geography, urban history, and evolutionary economics. Urban spatial structure has been characterized as heavily path-dependent, with a neighborhood's present-day form continuing to reflect the infrastructure, land-use patterns, and dominant transportation technology of the era in which it was built. Studies of port cities have similarly argued that the longevity of historical infrastructure investment makes spatial and institutional transitions difficult long after a port's original economic function has diminished. Work on post-industrial regional restructuring has extended this idea specifically to former coal and steel regions, arguing that industrial culture and cognitive "lock-in" — not merely physical infrastructure — shape whether a region renews or remains dependent on its industrial-era path, with the Ruhr region itself discussed as a case study of this dynamic (Görmar & Harfst, 2019). Despite this substantial theoretical foundation, direct, quantitative, GIS-based testing of path dependency at the scale of intra-city accessibility — rather than broad city growth patterns, institutional governance arrangements, or industrial-culture narratives — remains comparatively rare, representing the specific gap this study addresses.

### 2.2 The 15-Minute City and the City-Center Advantage

The 15-minute city framework, prioritizing proximity-based access to essential services via walking and cycling, has generated a substantial and rapidly growing empirical literature since 2021, with over 100 peer-reviewed publications identified in a recent systematic review spanning 2021 to early 2025. Network-based accessibility modeling — computing true walking-network distance to points of interest rather than simplified straight-line radii — has emerged as the dominant methodological approach in this literature, directly consistent with the network-distance methodology adopted in this study. A large-scale comparative study spanning 10,000 cities globally found a consistent and largely unsurprising pattern: city centers have measurably better service access than peripheral areas. This finding is directly relevant to the present study's methodology, since it establishes city-center proximity as a well-documented, independent predictor of accessibility in its own right — precisely the confound this study needed to rule out before treating any historical-industrial-site effect as genuine.

## 3. Data and Methodology

### 3.1 Study Area

Bochum, North Rhine-Westphalia, Germany — a defining Ruhr Valley coal and steel city from the mid-19th century through the 1950s, with its final coal mine closing in 1974.

<p align="center">
  <img src="outputs/plots/study_area_bochum.png" width="700">
</p>

**Figure 1.** Study area showing the administrative boundary of Bochum, North Rhine-Westphalia, Germany. Bochum was selected as the study area because of its well-documented coal-mining history and its transformation into a post-industrial city, providing an ideal setting to examine whether nineteenth- and twentieth-century industrial geography continues to influence present-day 15-minute-city accessibility.

### 3.2 Historical Data

Thirteen coal mines and four worker-housing colonies (Zechensiedlungen) were compiled from Mindat.org and German heritage archival sources, kept as two independent, structurally distinct GIS layers given their categorically different nature (extraction site versus residential housing). A proposed steelworker colony was explicitly excluded during data review, since it was linked to steel rather than coal production. This dataset represents the major, well-documented industrial-era sites in Bochum rather than the region's complete historical mining register, which includes several hundred additional small-scale operations (Kleinzechen, Erbstollen) spanning multiple centuries that are not comparable in scale or documentation quality to the thirteen major Zechen analyzed here (see Section 6, Limitations). Steel-works and industrial-era rail and road infrastructure were part of the project's original conceptual scope but were not digitized in this phase, given archival availability and timeline constraints; digitizing them is identified as Future Work (Section 8).

<p align="center">
  <img src="outputs/plots/historical_geography.png" width="700">
</p>

**Figure 2.** Historical coal-mining geography of Bochum derived from nineteenth-century industrial maps. Former mining sites are shown alongside the modern administrative boundary, providing the historical spatial framework used to evaluate whether legacy industrial infrastructure continues to influence present-day urban accessibility.

### 3.3 Present-Day Accessibility Model

Bochum's complete pedestrian street network (69,393 nodes, 169,668 edges) was acquired via OSMnx, alongside 786 essential-service points of interest across health, education, and daily-needs categories. A 15-minute walking threshold was operationalized as 1,125 meters of true network distance, computed via Dijkstra's shortest-path algorithm from every service location — consistent with the network-based approach dominant in the current 15-minute-city literature, and avoiding the straight-line-radius approach known to overstate real walkable accessibility.

### 3.4 Statistical Testing and Confound Verification

Distance from each network node to its nearest historical industrial site was computed and compared between low- and high-accessibility node groups via Welch's t-test, with effect size reported as Cohen's d (pooled-standard-deviation formula). Given the established literature finding that city-center proximity independently predicts accessibility, this was explicitly tested as a potential confound: correlation between distance-to-historical-site and distance-to-city-center, and a logistic regression predicting accessibility from both distance measures simultaneously, with coefficients additionally converted to odds ratios (percentage change in odds per 100m) for interpretability.

### 3.5 Spatial Clustering (Local Moran's I)

The t-test in Section 3.4 tests whether distance to historical sites *differs* between accessibility groups; it does not test whether low accessibility is spatially *clustered*, which is a distinct question and was the specific method named in this project's original Objectives. To test this directly, a K-nearest-neighbor (k=8) spatial weights matrix, row-standardized, was constructed over all 69,393 street-network nodes using their projected (EPSG:32632) coordinates. Local Moran's I (Anselin's LISA statistic) was then computed on the binary 15-minute-accessibility variable using 99 conditional permutations (seed=42), with statistical significance assessed at p<0.05 (`libpysal` and `esda` Python packages). Each node was classified into one of four quadrants — High-High (hot-spot), Low-Low (cold-spot), High-Low, or Low-High (spatial outliers) — based on its own value and its neighbors' average value.

## 4. Results

### 4.1 Accessibility Coverage

85.8% of network nodes fell within a 15-minute walk of at least one essential service; 14.2% (9,858 nodes) did not.

<p align="center">
  <img src="outputs/plots/ghost_infrastructure_overlay.png" width="700">
</p>

**Figure 3.** Overlay of historical coal-mining infrastructure and present-day 15-minute walking accessibility in Bochum. The visualization illustrates the spatial relationship between former industrial sites and modern accessibility patterns, providing the geographical basis for the statistical comparison presented in the following sections.

### 4.2 The Reversed Relationship

Low-accessibility nodes were, on average, further from historical industrial sites (1,984m) than high-accessibility nodes (1,450m) — a highly significant difference (Welch's t-test, t=42.887, p<0.00001), opposite in direction to the original hypothesis that industrial legacy would predict present-day neglect. The effect size is medium-to-large (Cohen's d=0.589, computed as the mean difference divided by the pooled standard deviation), indicating this is a practically meaningful difference and not merely a statistically significant one inflated by the very large sample size (69,393 nodes) — a distinction worth stating explicitly given how easily large-N studies can report a significant p-value for a trivially small effect.

<p align="center">
  <img src="outputs/plots/distance_comparison_boxplot.png" width="700">
</p>

**Figure 4.** Boxplot comparing the distance from historical coal-mining sites for high-accessibility and low-accessibility locations. Contrary to the original hypothesis, low-accessibility locations are significantly farther from former mining sites than high-accessibility locations, indicating that historical industrial geography does not predict present-day accessibility in the expected direction.

### 4.3 Confound Verification

Correlation between distance-to-historical-site and distance-to-city-center was low (r=0.063), indicating these are largely independent spatial variables. A logistic regression including both distances simultaneously found the historical-site effect remained statistically significant (coefficient=-0.0005, p<0.001) after controlling for city-center distance — confirming the reversed relationship is not merely a proxy for the well-documented city-center advantage established in the broader 15-minute-city literature. Converted to odds ratios, each 100m closer to a historical industrial site is associated with approximately 4.9% higher odds of 15-minute accessibility, compared to approximately 3.0% higher odds per 100m closer to the city center — the historical-site effect is, per unit distance, the larger of the two.

### 4.4 Spatial Clustering: Local Moran's I

The Local Moran's I analysis (Section 3.5) found a mean local I of 0.923 across all nodes. 10,266 of 69,393 nodes (14.8%) formed statistically significant spatial clusters at p<0.05. Of these, 9,568 were Low-Low ("cold-spot") clusters — contiguous zones of low accessibility surrounded by other low-accessibility nodes — and 698 were High-Low spatial outliers (isolated low-accessibility nodes surrounded by high-accessibility neighbors); no statistically significant High-High or Low-High clusters were found.

<p align="center">
  <img src="outputs/plots/lisa_cluster_map.png" width="700">
</p>

**Figure 5.** Local Moran's I cluster map. Blue points mark nodes belonging to statistically significant Low-Low ("cold-spot") clusters; gold points mark High-Low spatial outliers; grey points are not statistically significant. Historical coal mines (triangles) and worker colonies (diamonds) are overlaid for reference.

Cross-tabulating cluster membership against distance to historical sites: nodes in significant LL cold-spot clusters average 1,992.3m from the nearest historical industrial site, compared to 1,447.1m for non-significant nodes. Critically, 97.1% of all low-accessibility nodes fall within a statistically significant LL cluster — meaning low accessibility in Bochum is not scattered randomly across the city but forms genuine, spatially contiguous cold-spots, and those cold-spots are measurably farther from historical industrial infrastructure than the rest of the network. This result directly fulfills the spatial-clustering test named in this study's original Objectives, and corroborates the Section 4.2–4.3 findings via a statistically independent method that explicitly accounts for spatial structure rather than treating nodes as independent observations.

## 5. Discussion

This finding is best understood as a "path dependency of centrality" rather than a "path dependency of neglect." Nineteenth-century coal and steel infrastructure was built, by economic necessity, at the center of dense worker populations — with the road networks, market infrastructure, and housing density required to serve that population. This study's evidence suggests that dense historical infrastructure footprint, independent of the modern city center's location, has left a durable legacy of street connectivity and service density persisting more than fifty years after the mines closed. This directly extends the path-dependency literature — previously applied primarily to broad urban growth patterns and port-city institutional arrangements — into the finer-grained domain of intra-city walkable accessibility, while remaining consistent with, rather than contradicting, the established finding that centrality (of any origin, historical or contemporary) predicts better accessibility outcomes.

A note on the project's title and framing is warranted given this finding. "Ghost Infrastructure" was chosen to evoke infrastructure whose original economic function has vanished while its physical and spatial legacy persists — the mines are gone, but their effect on the city's fabric is not. It is not intended to imply that this legacy is one of neglect or abandonment; the results show the opposite. Read precisely, the "ghost" in the title refers to an absent cause (the coal industry) producing a present, measurable, and — as this study finds — largely positive effect (durable centrality and connectivity), not to a haunted or neglected present-day landscape.

## 6. Policy Implications

If historical industrial cores retain a durable centrality advantage rather than accumulating disadvantage, post-industrial urban planning in the Ruhr Valley and comparable regions may be better served by treating these areas as accessibility assets to reinforce — through infill development, mixed-use zoning, and continued service provision — rather than as legacy-neglect zones requiring remedial investment. Conversely, this study's finding that accessibility gaps concentrate in areas *away* from the historical industrial core suggests that peripheral, more recently developed neighborhoods — not the historic industrial center — may be the areas most in need of targeted 15-minute-city infrastructure investment. This reframing does not diminish the value of heritage-led regeneration in former industrial cores; it suggests such regeneration may be building on an already-favorable accessibility foundation, while the more urgent accessibility deficit lies elsewhere in the city.

## 7. Limitations

The worker-colony dataset (4 sites) is smaller than the coal-mine dataset (13 sites), somewhat limiting the statistical power of colony-specific sub-analysis. The 13 mines and 4 colonies analyzed here represent the major, well-documented industrial-era sites in Bochum, not the city's complete historical mining register, which includes several hundred additional small-scale operations (Kleinzechen, Erbstollen) spanning multiple centuries; these are not comparable in scale or documentation quality to the major Zechen analyzed here and no coverage percentage is claimed against that broader, heterogeneous register. This study relies on point-based historical site locations rather than full manual digitization of mine and colony boundary extents, a scope decision made given project timeline constraints. Industrial-era rail and road infrastructure — part of this project's original conceptual scope — was not digitized in this phase (see Future Work, Section 8). All essential-service categories were treated as equally weighted in the accessibility model, which does not capture genuine variation in how urgently different service types matter to daily life. The city-center reference point used in the confound analysis (Bochum Hauptbahnhof) is, in this compact city, geographically coincident with the Rathaus and commercial core within a few hundred meters — a genuinely distinct second reference point could not be verified for a robustness check, so this study cannot rule out that a differently defined city center might yield a modestly different confound estimate, though the very low correlation (r=0.063) between the two distance measures makes a materially different result unlikely. Socioeconomic confounders (income, age, tenure, car ownership) were not available for this analysis and are not controlled for; the reported relationships should be read as descriptive spatial associations, not fully adjusted causal estimates. Finally, the Local Moran's I analysis (Section 4.4), like the underlying accessibility data itself, treats the 69,393 street-network nodes as the unit of analysis; because nearby nodes share street segments and service catchments by construction, they are not independent observations, which the KNN-based spatial weights matrix is specifically designed to account for — but readers should note this spatial non-independence when interpreting the raw node count (rather than the cluster-level pattern) as a sample size.

## 8. Future Work

This study's scope decisions point to several directions for follow-up research, listed here rather than left implicit:

- **Socioeconomic confounders.** Incorporating income, age, tenure, and car-ownership data (e.g., from German census/Zensus sources) to test whether the historical-site effect holds after controlling for present-day socioeconomic composition.
- **Weighted service index.** Replacing the equally-weighted essential-service accessibility measure with a weighted index reflecting the differential importance of service categories (e.g., healthcare and groceries weighted more heavily than green space).
- **Geographically Weighted Regression (GWR).** Modeling the historical-site effect as spatially varying across the city, rather than assuming a single global coefficient, to test whether the effect is stronger in some parts of Bochum than others.
- **Multi-city comparison.** Replicating this methodology in comparable Ruhr Valley cities (e.g., Dortmund, Essen) to test whether the "path dependency of centrality" finding generalizes beyond Bochum or is specific to its particular urban history.
- **Multi-year, phenology-normalized time-series trend.** Extending the present cross-sectional design to track how the historical-site accessibility advantage has changed over time, rather than testing a single present-day snapshot.
- **Industrial-era transportation network digitization.** Digitizing historical rail and road infrastructure — part of this project's original conceptual scope (see Section 3.2) — to test whether historical transportation connectivity, not just proximity to mines and colonies, independently predicts present-day accessibility.
- **Walking-time-threshold sensitivity analysis.** Testing whether the reversed relationship holds at alternative accessibility thresholds (e.g., 10-minute and 20-minute walks), not only the 15-minute threshold used here.
- **Polygon-based historical site boundaries.** Replacing point-based mine and colony locations with digitized boundary polygons, to test whether the finding is sensitive to this representational choice.

## 9. Conclusion

Nearly a century and a half after Bochum's industrialization began, and more than fifty years after its last coal mine closed, historical industrial geography continues to leave a statistically significant, independently verified imprint on present-day walkable accessibility — not through neglect, as originally hypothesized, but through the enduring legacy of dense infrastructure built to serve 19th-century industrial populations. This finding directly extends path-dependency theory into a new, quantitatively testable domain, and demonstrates that a rigorously verified "surprising" result — checked explicitly against its most likely confound and corroborated by an independent spatial-clustering test — can constitute a more substantive contribution than a hypothesis confirmed at face value.

## References

Arthur, W. B. (1988). Urban Systems and Historical Path Dependence, in *Cities and Their Vital Systems*. National Academies Press.

Görmar, F., & Harfst, J. (2019). Path Renewal or Path Dependence? The Role of Industrial Culture in Regional Restructuring. *Urban Science*, 3(4), 106. https://doi.org/10.3390/urbansci3040106

Hein, C., & Schubert, D. (2021). Resilience and Path Dependence: A Comparative Study of the Port Cities of London, Hamburg, and Philadelphia. *Journal of Urban History*.

Sony Computer Science Laboratories. A Universal Framework for Inclusive 15-minute Cities. *Nature Cities* (2024), as reported via CNU.org.

Systematic literature review: An assessment of proximity in the 15-Minute City. *ScienceDirect* (2025).

Bencekri, M., & Moreno, C. Assessing accessibility of cultural sites through the 15-minute city framework in Seoul. *International Journal of Urban Sciences* (2025).

