# Ghost Infrastructure: Historical Industrial Geography and the Persistence of Path-Dependent Accessibility in Bochum, Germany

**Sakshi D. Maske**
Independent Geospatial Researcher

## Abstract

The complete 69,393 pedestrian street node network from Bochum was used for a Welch's t-test, which revealed as a surprise that street nodes with low accessibility are actually significantly farther from historical industrial sites than street nodes with high accessibility (t=42.887, p<0.00001, Cohen's d=0.589 - medium-to-large effect), which is the opposite of what the original hypothesis expected. This is done by determining whether the industrial geography of Bochum in the 19th and 20th centuries in relation to the location of coal mines and the housing colonials for miners (Zechensiedlungen) can still be regarded as a prediction of the "15-minute city" access to everyday areas by walking or cycling, more than 50 years after the last coal mine was shut down. Each of 13 historical coal mines and 4 worker colonies have been digitized from existing archival sources, and accessibility for present-day mines was simulated by computing true network distance isochones over the entire street network. This inverse link remained significant in a logistic regression model when stratified by proximity to the inner core of the city which has been previously established as an important predictor of level of accessibility in the wider 15-minute city literature: with the city-center distance as the only independent variable modeled, the city-center coefficient remained statistically significant (coefficient=-0.0005, p<0.001); and the correlation between the two distance measures was very low (r=0.063). Combined with this, a spatial-clustering analysis of “Local Moran's I” (using a completely independent statistical method) confirms the same findings: that 97.1% of low-accessibility nodes can be identified as part of statistically significant spatial cold-spot clusters, indicating that low accessibility is not random but represents real, contiguous geographical areas that are measurably further from historical industrial infrastructure. Such theoretical reflections have been well understood in economic geography, but have not, until now, been directly tested using quantitative, measurable spatial evidence at the level of the internal accessibility structures of urban center cities: here, the historical context of "necessary" industrial development, built on the centrality of dense populations of worker migrant residents, seems to have left other tangible legacies of street-level connectivity and density of services that remain largely out of the care of the city itself.

Not all the copies were reproduced properly, and that's significant as well as the fact that some were. The same raw reversed relationship, however, still present in direction and significance (t=24.731, p<0.00001), was present in the 72,027 nodes of pedestrian network (95.5% of the low-accessibility nodes of the city in significant cold-spot clusters, compared to 97.1% of the nodes in Bochum). Cohen's d was lower (0.338 versus 0.589) and the Local Moran's I spatial clustering result was replicated almost exactly. However, this was not found to replicate — a logistic regression that jointly controls for both distance-to-historical-site and distance-to-city-center shows the coefficient of the historical-site effect changing sign (from positive to negative), meaning the historical-site effect is expected to be highly correlated with and non-independent to the city-center effect in Essen. The "path dependency of centrality"-effect in itself seems to generalize – but the finding that it doesn't happen if a city is not represented in the city center itself is, according to current evidence, a Bochum-specific and not general result. This is corroborated by a separate walking-threshold sensitivity analysis, which was performed prior to the Essen replication; the results, both before and after that replication, showed the same reversed correlation at an even stricter 10-minute (750m) and even more severe 20-minute (1500m) walking-threshold (Cohen's d=0.413, p<0.00001 and Cohen's d=0.661, p<0.00001 respectively).

**Keywords**: path dependency, 15-minute city, urban accessibility, historical GIS, network analysis, post-industrial geography, multi-city replication, robustness analysis

---

## 1. Introduction

Are there measurable traces from an industrial past, over 50 years ago, that still remain of which parts of a city have easy walking access to the services they provide in everyday life? This is the special question posed to Bochum, Germany. Bochum's urban morphology was never meant to be accessible to anyone, it was built for coal mines and steel works and was laid out for railways, roads and housing for coal miners in the 19th century. The final coal mine in the city recently shut down in 1974.

## 2. Literature Review

Path dependency is an empirically proven concept that has been well documented, but is rarely examined on the spatial scale we are interested in.

Despite the solid theoretical basis, there is comparatively little direct and quantitative path dependency testing, conducted at the level of intra-city accessibility; most research is conducted on a more general scale, exploring city growth, the institutional governance configuration or an industrial-culture narrative. This is the particular gap this study will remedy. The concept in itself, that of path dependency, has been around a long time and is known in economic geography, history of cities and evolutionary economics. The urban spatial structure has been considered to have a strong path-dependency, as the current layout of a neighbourhood will remain as a remnant of the infrastructure, land use patterns and the prevailing mode of transport in the period when it has been created. This has also been argued for in studies conducted on port cities; the presumption being that as historical infrastructure investments remain in place for extended periods of time, transitions occur spatiously and institutionally long after their former economic purpose has come and gone, to ensure that the built-in impacts remain.The same applies in regard to spatial and institutional transitions that have been studied concerning port cities; the presumption being that – the built-in impacts equating to historical infrastructure investments – will not be easily changed well after their original economic function is over. This is extended to former coal and steel areas claiming that not only the physical structure of a region but above all industrial culture and the cognitive "lock-in" lie behind the ability to renew or stick to its industrial culture during industrial restructuring (Görmar & Harfst, 2019); the Ruhr region is also discussed and used as a case example (Görmar & Harfst, 2015a).

### 2.2 The 15-Minute City and the City-Center Advantage

One of the direct findings from this literature that has proven directly relevant to this study's methodology was that service access proved to be measurably better within cities' central areas versus the peripheral areas, as reported by a large scale comparative study of 10,000 cities around the world. The present study thus confirmed that city-center proximity itself is a well established, independent predictor of accessibility on its own — a confound rule out of which it is necessary to remove to uncover any pure historical-industrial-site effect. Since 2021, the 15-Minute City concept has built up significant empirical literature, reflecting its popularity and the increased focus on creating these routines both within the urban sector and multi-sectoral fields. In a recent systematic review (Alonso et al., 2023) of empirical papers from 2021 to 2025, more than 100 peer-reviewed works were identified. In this literature, network-based accessibility modeling—calculating the actual walking-network distance, instead of simplifying the radius, to a point of interest — has become the predominant methodological approach, directly analogous to the network-distance methodology used here.

## 3. Data and Methodology

### 3.1 Study Area

Bochum is a characteristic coal and steel town of the Ruhr since the mid-19th century known for mining and steel manufacturing; its last coal mine was operational until 1974.

<p align="center">
  <img src="outputs/plots/study_area_bochum.png" width="700">
</p>

**Figure 1.** A layout of the study area including administrative boundaries of Bochum, North Rhine-Westphalia, Germany. Due to its extensive history of coal mining and its post-industrial transformation, it is a good place to investigate whether the nineteenth- and early twentieth-century impact of industry can still be felt in the present day in terms of access to 15-minute cities.

### 3.2 Historical Data

It was decided to work with only the major and comprehensively documents sites of the industrial era in Bochum, excluding the even larger numbers of small-scale sites (Kleinzechen, Erbstollen) from various eras in history, which can only be compared in size and documentation relative to those used in this data set (see Section 6, Limitations). From that, the 13 coal mines and 4 worker-housing colonies (Zechensiedlungen) were extracted from the Mindat.org and German heritage archive to be stored as two separate, distinct GIS layers because of their different categorisation (extraction site vs. worker housing). During data review, one of the proposed steelworker colonies was specifically eliminated because it was included with steel production and not coal. The conceptual scope of the project included steel-works and the railways and roads of the industrial era, however these have not been digitized in this phase due to time and availability of records/stages in the archive and Future Work will be documented (in line with the section 8).

<p align="center">
  <img src="outputs/plots/historical_geography.png" width="700">
</p>

**Figure 2.** The historical citiescape of coal-mining Bochum on an industrial map from the 19th century, presented as an overlay on the current city boundary (as basis for testing, whether still remnants of the industrial past affect accessibility today).

### 3.3 Present-Day Accessibility Model

The fact that simple straight-line buffer circles have been avoided was intentional as their use would overestimate real walkable accessibility because they use a logic of walking straight through buildings and city blocks. Rather, a measure of 1,125m of true network distance – calculated using Dijkstra's algorithm from each service location – was adopted, as is widely used in the current literature with regard to the metrics of the 15-minute city, which are usually network-based. This was applied over all 69,393 pedestrian street nodes and 169,668 pedestrian street edges of the city's street network and 786 essential service points of interest including health, education and daily needs features derived from the OSMnx library.

### 3.4 Statistical Testing and Confounds Verification

Given the current literature that has documented that proximity to the city center is used to predict accessibility independently of the other variables, an explicit test of this correlation was performed as a possible confounder before concluding this was a city-center effect: correlation between distance-to-historical-site and distance-to-city-center, and logistic regression of accessibility on distance-to-historical-site, distance-to-city-center, all in one model, with coefficients converted to odds ratios (percentage change in odds per 100m) for interpretability. The distance between each network node and the nearest historical industrial node was calculated and compared the two groups of network nodes (low vs. high accessibility) using a Welch's t-test and Cohen's d was reported, using the formula with pooled standard deviations.

### 3.5 Spatial Clustering (Local Moran's I)

After this analysis, each street node was classified into one of four spatial categories (sorted from highest accessibility to lowest, buysed: High-High (hot-spot), Low-Low (cold-spot), High-Low, or Low-High (spatial outlier). The process began by creating a binary variable with spatial weights based on the 15-minute conversion of the street-network, row-standardized, calculated with all of its 69,393 street-network nodes and their projected (EPSG:32632) coordinates, using a K-nearest-neighbor (k=8) method. Then, Local Moran's I (Anselin's LISA statistic) was calculated from the binary variable using 99 conditional permutations (seed=42), with statistical significance assessed at p<0.05 (`libpysal` and `esda` Python packages). This whole exercise attempts to answer something different from the Section 3.4 t-test, which just tests whether there is any difference in distance to historical sites between the accessibility groups, and a different method is named in the Objectives of this project, namely testing whether distance to historical sites is “clustered” by the spatially distinct question of whether low accessibility is spatially clustered or not.

### 3.6 Robustness Check: Walking-Threshold Sensitivity

As before, re-use the same 69,393 node network, same service locations and pre-computed historical-site-distances; no new data acquisition was necessary in order to re-run the entire accessibility-classification-and-welching's-test pipeline at a new and more stringent 10-minute threshold (750m) and at a new and more liberal 20-minute threshold (1,500m). The finding of a reversed relationship for all sections of this study when the 15-minute timeframe of “walkable access” was adopted (Section 3.3–3.5) was suspected to be an artifact of this time cut-off, and this test was made to verify that hypothesis.

### 3.7 Multi-City Replication: Essen

The four large historical coal mines (Zeche Zollverein, Zeche Carl Funke, Zeche Vereinigte Helene & Amalie, Zeche Pörtingsiepen) and four worker colonies (Siedlung Carl Funke, Mathias-Stinnes-Siedlung, Kolonie Zollverein III, Kolonie Beisen) were scanned using KuLaDig (Kultur) software.Landschaft.Two GIS databases, Digital (GADM) and German Wikipedia, already matched against the official database of administration in Essen (2), were independently cross-checked with Essen's administration area (GADM v4.1) to obtain more precise placement, which was on average 15km northeast of Bochum in North Rhine-Westphalia. Whether the ‘path dependency of centrality' finding is specific to Bochum or applies across the Ruhr Valley to the common industrial urban 19th century form lay in the test that this data set could enable, as was defined in this study's own Future Work section (Section 8): Does the ‘path dependency of centrality' occur in Bochum or does it apply throughout the Ruhr Valley of the shared industrial 19th century form. This Essen dataset (8 sites) is definitely a subset of Bochum (17 sites); the official historical portal of the city, historischesportal.essen.de, catalogues roughly 1,700 historical mining-related facilities throughout the city — the same major sites only decision that we made in Bochum (Section 3.2) was adopted here. Essen's complete pedestrian street network (72 027 nodes, 188 198 edges) and 366 point-based essential-service locations were then acquired using OSMnx, and the same 15-minute network-distance threshold, welch's t-test, city-center confound check (using Essen Hauptbahnhof, 51.4517°N 7.0134°E, as the city-center reference point — the same concept as used for Bochum) and Local Moran's I spatial-clustering procedure (Section 3.5) were applied unchanged.

<p align="center">
  <img src="outputs/plots/study_area_essen.png" width="700">
</p>

**Figure 3.** Study area showing the administrative boundary of Essen, North Rhine-Westphalia, Germany — the second Ruhr Valley city used to test whether the Bochum finding generalizes, directly comparable to Figure 1 (Bochum).

<p align="center">
  <img src="outputs/plots/essen_historical_geography.png" width="700">
</p>

**Figure 4.** Historical coal-mining geography of Essen: four major coal mines and four worker colonies digitized from KuLaDig and German Wikipedia, directly comparable to Figure 2 (Bochum).

## 4. Results

### 4.1 Accessibility Coverage

85.8% of network nodes fell within a 15-minute walk of at least one essential service; 14.2% (9,858 nodes) did not.

<p align="center">
  <img src="outputs/plots/ghost_infrastructure_overlay.png" width="700">
</p>

**Figure 5.** Historical coal-mining facilities and current 15-min walking reachability in Bochum (overlaid). The visualization displays the geographical context of the spatial distribution of former industrial sites to those of current accessibility, forming the foundation for the statistical comparisons which are explored in the subsequent sections.

### 4.2 The Reversed Relationship

It is super easy to confuse statistical significance = practical significance in this sample size (69,393 nodes) as a very small difference, which generally is of no practical significance, can produce a very low p value in a large-sample study. This is not the case here, however, since the effect size (Cohen's d=0.589) is of medium-to-large size (here computed as the difference between the group means divided by the pooled SD). This is reflected in the numbers below. The low-accessibility nodes were, conversely, further from historical industrial sites (on average 1,984m) than high-accessibility nodes (1,450m); this is unlike the original hypothesis regarding the influence of industrial legacy on present day neglect (Welch's t-test: t=42.887, p<0.00001).

<p align="center">
  <img src="outputs/plots/distance_comparison_boxplot.png" width="700">
</p>

**Figure 6.** Box and whisker plot of distance from old coal-mining areas (high and low accessibility). In contrast to the original formulation of the hypothesis, the low-accessibility areas are actually much more distant from previous mining areas than the high-accessibility areas, suggesting that the present-day accessibility in these areas is in a non-anticipated sense and relationship with the preceding mining geography.

### 4.3 Confound Verification

The relative impact of the closeness to a historical industrial site as a unit of distance is higher than the relative impact of closeness to the city center per 100m – the odds of being able to access the building within 15-min at the industrial site are about 4.9 % higher per 100m closer to the site, while the odds of being able to access the city are about 3.0 % higher per 100m closer to the city center. But that's only true because the two effects are strictly disentangled. This raised the question of how much the distance-to-historical-site effect overlaid distance to city-center — we did not see much correlation between the two variables (r=0.063), and iLogistic regression with both distance and city-center found the relationship with distance to historical-site still statistically significant after accounting for the city-center result (coefficient=-0.0005, p<0.001), so the opposite bias is not simply a proxy for the widely-cited city-center advantage from the larger 15-minute city literature.

### 4.4 Spatial Clustering: Local Moran's I

The majority of all these low-accessibility nodes lie in a statistically significant Low-Low cluster: Low accessibility is not a random distribution over all nodes in Bochum, but rather a statistically significant number of neighbouring nodes that are 'cold-spots' and measurably farther from the historic industrial infrastructure than the remain of the nodes. This is supported by a cross tabulation of cluster membership with distance to nearby historical industrial site: The average distance from the nearest historical industrial site to a cluster member node in significant LL cold-spot clusters is 1,992.3m—a higher average distance than for non-significant cluster member nodes, which average 1,447.1m. The resulting clustering analysis (also known as Local Moran's I, Section 3.5) identified 10,266 of 69,393 nodes (near 15%) that experienced statistically significant spatial clustering at p<0.05: 9,568 of these were Low-Low (cold-spot) clusters and 698 High-Low spatial outliers, while there was no statistically significant clustering of High-High or Low-High nodes.

<p align="center">
  <img src="outputs/plots/lisa_cluster_map.png" width="700">
</p>

**Figure 7.** Local Moran's cluster map. The blue nodes represent a part of statistically significant 'cold-spots' (know as ‘Low-Low' cluster); the gold colored nodes represent a part of statistically significant spatial outliers ('High-Low'); the grey nodes represent a part that is not statistically significant. Marked up for reference are the positions of historical mines of coal (triangles) and of worker colonies (diamonds).

This is the exact result of the original Objectives of this study, the spatial-clustering test, and is confirmed by the overall results through a method that is independent in terms of the statistical analysis used (Section 4.2-4.3) and which is specifically tailored to deal with spatial structure rather than assuming nodes to be independent observations.

### 4.5 Threshold-Sensitivity Results

For all three thresholds tested - 10 mins, 15 mins and 20 mins - the odds ratio per 100m closer to a historical site is roughly identical (4.24% at 10 mins, 4.88% at 15 mins, 4.49% at 20 mins) and significant at (p<0.00001), when controlling for distance to city center. This stability can be seen in the underlying distances as well. At a stricter 10-minute threshold (750m, 67.1% coverage), low-accessibility nodes remain significantly further from historical sites (1,778m vs. 1,402m; Welch's t=47.062, p<0.00001, Cohen's d=0.413), and at a more permissive 20-minute threshold (1,500m, 94.4% coverage), the same pattern holds and, notably, strengthens (2,098m vs. 1,492m; t=32.150, p<0.00001, Cohen's d=0.661) — larger than the original 15-minute effect (d=0.589). I don't believe that this is just because of the 15 minutes limit that they chose, it looks like a very solid relationship overall.

<p align="center">
  <img src="outputs/plots/threshold_sensitivity_comparison.png" width="750">
</p>

**Figure 8.** Effect size comparison of the distance to the nearest historical site for each accessibility group (left) and walking-threshold sensitivity (mean distance to the nearest historical site) at 10-, 15-, and 20-minute thresholds (right). The inverse relationship exists in all three—and evolves, reinforces and proliferates in all three.

### 4.6 Multi-City Replication: Essen

The Local Moran's I spatial-clustering result is very similar: In Essen there are almost identical chunks of Low-Low Local Moran: mean across all nodes=0.917 (versus 0.923 in Bochum) and in both cities, 95.5% of the nodes associated with each Local Moran are found within statistically significant Local Moran's I Low-Low cold-spot clusters (versus 97.1% for nodes in the Local Moran's I Low-Low cold-spot clusters in Bochum — with no nodes in either city found within statistically significant Local Moran's I High-High hot-spot clusters). The raw reversed relationship also replicates, both in terms of direction, and statistical significance: The average distance of low-accessibility nodes (n=8,267) to the nearest historical site (3,693m) is significantly higher than that of high-accessibility nodes (n=63,760) (3,130m), Welch's t=24.731, p<0.00001; with a lower effect size than Bochum (Cohen's d=0.338 versus 0.589). The experimentally reported results were essentially a combined mix of success and failure for Essen, as reported here below, but without the occurred failures being reported selectively.

<p align="center">
  <img src="outputs/plots/essen_ghost_infrastructure_overlay.png" width="700">
</p>

**Figure 9.** Overlay of historical industrial infrastructure and present-day 15-minute walking accessibility in Essen, directly comparable to Figure 5 (Bochum).

<p align="center">
  <img src="outputs/plots/essen_distance_comparison_boxplot.png" width="700">
</p>

**Figure 10.** Boxplots to compare distance to historical sites of high and low accessibility locations in Essen, which are comparable in comparison to those in Figure 6 (Bochum). A relationship counter to that of Bochum is obtained (low accessibility, far from historical sites) for nodes, and the effect size is smaller but similar for those.

The common trait in both cities was that the city-center effect itself remained a strong and consistent predictor also in Bochum (odds per 100m closer to the center: 3% for Bochum, 4.2% for Essen). The result of confound-independence did not hold true. This correlation is r=0.405 for distance-to-historical-site and r=0.063 for distance-to-city-center for Essen, respectively, much higher than for Bochum, and the distance-to-city-center is far from being an independent variable with respect to distance-to-historical-site. As such, the sign of the coefficient of the city-center distance changes in Essen (coefficient=+0.0001, p<0.00001) in a logistic regression model predicting accessibility from both distances, the coefficient for being farther from a historical site in Essen becomes higher with reading it in that way, rather than lower.

<p align="center">
  <img src="outputs/plots/bochum_essen_comparison.png" width="800">
</p>

**Figure 11.** Plots in comparison of Bochum and Essen using the three statistical tests. The raw reversed effect and spatial-clustering result by Local Moran both replicate; the Local Moran's independence result does not.

<p align="center">
  <img src="outputs/plots/essen_lisa_cluster_map.png" width="700">
</p>

**Figure 12.** Local Moran's I cluster map of Essen, which looks directly comparable to Figure 7 (Bochum)

It is not inappropriate to think of two possible explanations for the contrapositive to the confound-independence result not being realised in Essen. The first is that the historical industrial geography is, indeed, more compactly organized around the city centre in Essen than it is in Bochum: the Krupp steel works, which here is located directly next to, but outside the present scope of the historical study of coal mining activity, developed in closer fusion to the city centre than did the coal-mining sites in Bochum, and are spread out and fragmented in the city's core areas compared with their closer spatial concentration in Essen. The other, also methodologically important, alternative is that this may simply reflect the use of a smaller sample of historical sites from Essen, (8 historical sites, compared to 17 in Bochum), which, with less of these points spread throughout more of a city, leads to a somewhat higher likelihood of this correlation being affected by sampling effects rather than true differences in historical geography. The second explanation, that this correlation would have been even lower if the data had existed at the eight sites than at the six sites used in the previous version, as occurred here, would be consistent with — but not proof — of the sampling-artifact explanation (which is highlighted explicitly in Section 7 'Limitations' as being the reason why this specific sub-finding should be viewed as provisional pending fuller data for the Essen dataset); from this point to that, the correlation dropped from r=0.475 to r=0.405 upon expanding the dataset to eight sites from six sites. Not one of these is in contradiction to the principal finding, however. The Essen result does not weaken the interpretation in Section 5 — but rather it reinforces one of its most interesting features, namely the durable, statistical clustering signature of centrality connecting with industrial densities: only the (stronger, more specific) interpretation that such an effect is not due to the simple proximity of cities that can be generalized from the raw, but not the yielded result.

## 5. Discussion

The infrastructure of coal and steel was constructed in the 19th century, for economic reasons, in the middle of a large mass of people, the road system, the market facilities and the housing density needed to support that population. The results of this study indicate that the evidence suggests that compressive historical infrastructure footprint exists which is persistent beyond 50 years after the closure of the mines, and that this legacy of street connectivity and service density is entrenched, even though the location of modern city center is not dense. This extends the path-dependency literature, which has been used extensively in modelling broad urban growth patterns and port-city institutional arrangements, into the finer-grained planning domain of intra-city walkable accessibility. None of this detracts from the solid finding that centrality, historical or contemporary, predicts better levels of accessibility; indeed, that is likely the best way to see centrality, as a path "dependency of centrality" and not as "dependency of neglect.

It does not mean that it is a legacy of neglect or abandonment, it is the opposite that is shown by the results. They have selected "Ghost Infrastructure" to elicit an infrastructure that - although its economy no longer exists - still serves its physical and spatial impacts: gone are the mines, but not the impact on the cityscape. The “ghost” in the title is not an abandoned and haunted modern landscape but the absence of a cause (the coal industry) which nonetheless has had a measurable, largely positive and durable impact (durable centrality and connectivity).

This does not undermine the overall "path dependency of centrality" framing of the following research. But centrality-legacy mechanisms are assumed to hold across cities while the relative contribution of historical versus present-day centrality to patterns of present-day accessibility may be compatible with and plausible variation across cities, depending upon the unique industrial and administrative histories of each city. However, the following qualifiers can be added for the Essen replication (4.6). The centrality/connectivity legacy from the past has existed in both cities, but the tighter version of the legacy, that remains outside of the proximity of the city center, is more as a peculiar achievement of Bochum and has not yet been proven for the broader regional Ruhr Valley.

## 6. Policy Implications

The accessibility gaps are not located inside the historical industrial core, these gaps have been located in the periphery, in more recent neighborhoods, in the newly built parts of the cities – so it is possible to group 15-minute-city infrastructure investment needs and choose the most suitable areas that are not what is now the industrial core of the city, but what is called the periphery and just a bit more recently built parts of the cities. With that has direct implications for planning: To keep history's industrial hubs accessible and support them by infill development, mixed use zoning, continued provision of services etc., not to locate there the necessary investment necessary to "save the sites" for ultimate improvement may prove to be a more effective strategy for the post-industrial planning and development of the Ruhr Valley and likeness than giving them a disadvantageous role as "legacy-neglect zones". Nevertheless, this reframing does not leave aside the importance of such heritage-led regeneration of the former industrial cores, rather it proposes that this form of regeneration might simply be continuing to build upon one of the city's most significant foundations in terms of accessibility – which is an accessibility issue elsewhere in the city, that is much more important).

## 7. Limitations

The relationships reported in the study should be interpreted as simple spatial associations, and not fully adjusted as causal relationships, because socioeconomic confounders (such as income, age, tenure, car ownership) were not collected and hence are not controlled for. Additionally, a cautionary note should be included in any sample-size interpretation: sample-size information from the Local Moran's I analysis (Section 4.4) is for the same reason that the 69,393-observations street-network nodes are not independent observations—the information is derived from the node count but as constructed the street-network nodes in nearby areas are not independent—readers should consult the pattern of nodes rather than the pattern of nodes for the count when applying the construction as a sample size. On the data side, the worker-colony dataset (4 sites) is smaller than the coal-mine dataset (13 sites), which introduces some restrictions in terms of the statistical quality of the statistical sub-analyse on the colony level, and corresponds only to a selection of main and well-documented mining sites of the industrial era in Bochum (no coverage percentage is claimed against the full historical mining register of Bochum with about 200 additional smaller mining operations, Kleinzechen, Erbstollen, not comparable in scale and documentation with the sites analysed here). This study assumes point-based historical site locations instead of an assumed extent of mine and colony boundaries, based on the time required for this project; and although the focus of this study was on the time frame of the industrial era, the extents of rail and road infrastructure were not manually digitized in this phase (see Section 8, Future Work). For purposes of the accessibility model, the weights for all essential-service categories were assumed to be equal; this does not reflect the true weight differences for different categories of services in relation to their importance to everyday life. Lastly, the city-center reference point chosen for the confound analysis (Bochum Hauptbahnhof) is in this compact city geographically identical to the second (the Rathaus), which was also the site of commercial activity within a few hundred metres, and in this case a prefabricated second point of reference could not be validated for a robustness check, so a second differently defined city center would lead to an - maybe slight - other estimate of the confound, but with the low correlation between the two distance measures (r=0.063) not much different can be expected.

This effect is understood as a reflection of the historic site / city center correlation, which was measured at 0.475 for the 6-site version of this data set used in initial testing and at 0.405 in this 8-site version, showing a measurable difference, consistent with the idea that a sampling-density explanation accounts for at least a part of the correlation. However, the practical geocoding-precision limitations that remain on the historical Essen mining sites would require additional expansion to Bochum's 17-site scale (Future Work: Section 8), a scale not attempted here in this round for the resolution of the shares to be explained. The dataset used here (the Essen dataset) is a smaller subset of its much larger historical mining register (~1,700 facilities citywide, as shown in the historical Essen portal) than the Bochum historical dataset is of Bochum's, and — as in Bochum, where the 17-site dataset was tested for confound-independence — the 8-site dataset used here should be taken as provisional.

## 8. Future Work

The other scope decisions in this study suggest certain clear directions for further research, which are not left implicit here, but rather stated with particular specificity. Based on these two items, originally planned here, but now found accounted for, it is now reported in Sections 3.6-3.7 and 4.5-4.6: walking-timethreshold sensitivity (confirmed robust at 10 and 20-minute thresholds); multi city comparison (replicated in Essen, with a nuanced result — see Section 4.6).

-   Extend the Essen historical dataset to the scale of Bochum. To evaluate the question "Is there a similar historical-industrial geography" between Essen and Bochum, the remaining questions of the overall "confound-independence" would have to be solved. This could be done by digitizing further major Essen mines and colonies, starting with the ~1,700 mines registered in the catalog on historischesportal.essen.de.
Socio-economic confounders: testing if differences in historical sites are reproducible when controlling for the current socio-economic makeup of the populations (e.g. income, age, tenure, car ownership from German census/zensus data).
- Multi-city replication can be extended further to other cities (Bochum, Essen, e.g., Dortmund, Gelsenkirchen), to see whether the wealthy independence of Essens' departures from Bochum is the rule among the cities, or if the lean departures from Bochum are the rule, and Essen is the exception.
Replacing point based representations of mine and colony locations with polygons of historical sites, to determine if the result is sensitive to boundary representation.
To assess, whether the effect exists more strongly in a specific part of Bochum (or Essen) than in the other part, by assuming the historical-site effect to be spatially distributed on the city. Modeling this effect as a spatially varying effect across the city, instead of the assumption of a spatially constant one (global coefficient).
2. Substituting an equally-weighted essential-service accessibility indicator with a weighted index that will be based on the differential importance of service categories (e.g., groceries, healthcare, and green space are weighted more heavily).
Implementing infrastructure-digitization for the era of the Industrial Revolution (as originally conceived by the project, see Section 3.2), to determine if accessibility of the historical railways and roads themselves (and not the proximity to mines and colonies) also predicted their accessibility today.
Expanding current cross-sectional design to look at time-series trends of access to historical-sites as they may relate to the advantage program has offered over time, not one current snapshot in time.

## 9. Conclusion

A rigorously tested ‘surprising’ outcome, against the most plausible confounder, and backed up by an independent test on the spatial clustering, could be a more significant discovery than a “face value” test. And this study was aimed at showing that. It has now been almost 150 years since Bochum began its industrialization and over half a century since the last coal mine had closed its doors and 19th-century industrial infrastructure continues to leave its mark today — not through neglect as was assumed — but because of its lasting impact on the accessibility of walking distances.Half a century later than Bochum's industrial development and more than 50 years since its last coal mine, the imprint of historical industrial geography is statistically significant, independently verified and continues to impact the present-day walkscape of the city. This discovery paves a new path toward quantitative testing in path-dependency theory.

Apparently underwhelming or incomplete results, honestly investigated and reported, are more useful than a nicer-looking, but only partial result — hence this study presents an overall result for a replication of Essen, which yielded some results that conflicted with the original result from Essen. Not only is the core finding robust under both of the two additional robustness extensions (represented in the two panels of the error bar bar chart above), but the result is also significant at both 10- respectively 20-minute thresholds, and replicates the whole methodology in Essen, where the underlying “path-dependency of centrality” mechanism (represented in the two panels of the error bar bar chart above) generalizes beyond Bochum, even though the specific claim about how centrality is statistically independent from proximity to the city center does not straightforwardly generalize.

## References

Arthur, W. B. (1988). Urban Systems and Historical Path Dependence. In *Cities and Their Vital Systems: Infrastructure Past, Present, and Future* (pp. 85–97). National Academies Press. [https://www.nationalacademies.org/read/1093/chapter/5](https://www.nationalacademies.org/read/1093/chapter/5)

Görmar, F., & Harfst, J. (2019). Path Renewal or Path Dependence? The Role of Industrial Culture in Regional Restructuring. *Urban Science*, 3(4), 106. [https://doi.org/10.3390/urbansci3040106](https://doi.org/10.3390/urbansci3040106)

Hein, C., & Schubert, D. (2021). Resilience and Path Dependence: A Comparative Study of the Port Cities of London, Hamburg, and Philadelphia. *Journal of Urban History*, 47(2), 389–419. [https://doi.org/10.1177/0096144220925098](https://doi.org/10.1177/0096144220925098)

Bruno, M., Melo, H. P. M., Campanelli, B., & Loreto, V. (2024). A universal framework for inclusive 15-minute cities. *Nature Cities*, 1(10), 633–641. [https://doi.org/10.1038/s44284-024-00119-4](https://doi.org/10.1038/s44284-024-00119-4)

Omwamba, J., Rotaris, L., & Longo, G. (2025). An assessment of proximity in the 15-Minute City: A systematic literature review. *Urban Transitions*, 3, 100012. [https://doi.org/10.1016/j.ubtr.2025.100012](https://doi.org/10.1016/j.ubtr.2025.100012)

Moreno, C., Gall, C., Woo, J., Lee, D., & Bencekri, M. (2025). Assessing accessibility of cultural sites through the 15-minute city framework in Seoul. *International Journal of Urban Sciences*, 29(1), 8–39. [https://doi.org/10.1080/12265934.2025.2462820](https://doi.org/10.1080/12265934.2025.2462820)
