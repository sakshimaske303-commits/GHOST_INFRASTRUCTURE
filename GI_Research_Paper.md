# Ghost Infrastructure: Historical Industrial Geography and the Persistence of Path Dependent Accessibility in Bochum, Germany

**Sakshi D. Maske**
Independent Geospatial Researcher

## Abstract

This study used the full pedestrian street network of Bochum, 69,393 street nodes, to run a Welch's t test. The result was a surprise. Street nodes with low accessibility sit significantly farther from old industrial sites than street nodes with high accessibility (t=42.887, p<0.00001, Cohen's d=0.589, a medium to large effect). This goes against what the original idea predicted. The study asks a simple question: does Bochum's 19th and 20th century industrial geography, its coal mines and its worker housing colonies (Zechensiedlungen), still shape who has a "15 minute city" today, more than 50 years after the last coal mine closed? To test this, 13 historical coal mines and 4 worker colonies were digitized from archive sources. Present day accessibility was measured using true network distance, not straight line distance, across the whole street network. The reversed pattern held up even after controlling for distance to the city center, a factor already known in the 15 minute city literature to predict accessibility on its own. In a logistic regression that included city center distance as a variable, the historical site effect stayed significant (coefficient=-0.0005, p<0.001), and the 2 distance measures were barely correlated with each other (r=0.063). A separate check, a Local Moran's I spatial clustering analysis, points to the same conclusion: 97.1% of low accessibility nodes sit inside statistically significant "cold spot" clusters. Low accessibility is not scattered at random. Under this KNN based spatial-clustering test, it forms statistically significant spatial clusters that sit noticeably farther from the old industrial sites. Economic geography has discussed ideas like this for a long time, but rarely tested them this directly, with real spatial data, inside a single city. The pattern found here suggests that the dense, tightly packed development built around 19th century industrial workers left behind a lasting legacy: better street connectivity and more nearby services, even after the industry itself disappeared.

The same test was repeated in a second city, and the honest result is mixed. Some parts held up, some did not, and both are reported here in full. In Essen (72,027 street nodes), the same reversed pattern showed up again, in the same direction and still highly significant (t=24.731, p<0.00001), with 95.5% of low accessibility nodes in significant cold spot clusters (close to Bochum's 97.1%). The effect size was smaller (Cohen's d=0.338, versus 0.589 in Bochum), and the spatial clustering result matched closely. But 1 part did not hold up: when both distance to historical site and distance to city center were entered into a single logistic regression, the historical site coefficient changed sign, negative in Bochum, positive in Essen. This means that in Essen, the historical site effect is closely tied to the city center effect, not independent of it the way it is in Bochum. So the general pattern, that old industrial sites predict better accessibility, seems to hold across cities, but the more specific claim, that this effect is independent of city center distance, appears to be true only in Bochum rather than as a general rule. A threshold sensitivity check, run before the Essen test, points the same way: the same reversed pattern held at a stricter 10 minute cutoff (750m, Cohen's d=0.413, p<0.00001) and a looser 20 minute cutoff (1,500m, Cohen's d=0.661, p<0.00001).

**Keywords**: path dependency, 15 minute city, urban accessibility, historical GIS, network analysis, post industrial geography, multi city replication, robustness checks

---

## 1. Introduction

Can a city still carry marks of its industrial past, more than 50 years later? These are marks that decide who can walk to daily services and who cannot. This is the question this study asks about Bochum, Germany. Bochum's streets were not laid out with walkers in mind. They were built for coal mines, steelworks, railways, and worker housing in the 19th century. The city's last coal mine closed in 1974.

## 2. Literature Review

Path dependency is a well established idea in research, but it is rarely tested at the small, street level scale used in this study.

Most path dependency research looks at bigger patterns: how whole cities grow, how governments manage regions, or how industrial culture shapes a place over time. Direct, number based tests of path dependency at the level of everyday walking access are rare. This gap is what the current study tries to fill. The idea of path dependency itself is old, and comes up across economic geography, urban history, and evolutionary economics. Many researchers argue that a neighborhood's layout stays locked in by the infrastructure, land use, and transport mode of the era that built it. Studies of port cities make a similar case (Hein & Schubert, 2021). Once a city invests heavily in infrastructure, that investment tends to stay in place long after its original economic purpose is gone. The same idea has been applied to old coal and steel regions, where not just the physical layout but also the local industrial culture can create a kind of "lock in" that shapes how, or whether, a place adapts during economic change (Görmar & Harfst, 2019).

### 2.2 The 15 Minute City and the City Center Advantage

1 finding from this body of research shaped the design of this study directly: a large comparative study of 10,000 cities worldwide found that access to services is better near city centers than at the edges, by a wide enough margin to matter. Because of this, city center distance had to be treated here as a known, independent driver of accessibility, something to rule out before claiming any pure historical industrial effect. Since 2021, research on the 15 Minute City idea has grown fast, both in academic work and in city planning itself. A recent review of this research (Omwamba, Rotaris, & Longo, 2025) found that most current studies now measure accessibility using real street network distance, not simple straight line radius, the same approach used in this study.

## 3. Data and Methodology

### 3.1 Study Area

Bochum has been a coal and steel town in Germany's Ruhr region since the mid 1800s. Its last working coal mine closed in 1974.

<p align="center">
  <img src="outputs/plots/study_area_bochum.png" width="700">
</p>

**Figure 1.** Map of the study area, showing Bochum's administrative boundary in North Rhine-Westphalia, Germany. Its long coal mining history and later transformation make it a strong test case for whether 19th and early 20th century industry still shapes present day access to a "15 minute city."

### 3.2 Historical Data

This study focused only on the largest and best documented industrial sites in Bochum. Many smaller sites (Kleinzechen, Erbstollen) from different periods were left out, since they are not well matched in size or documentation to the sites used here (see Section 7, Limitations). From archive sources, Mindat.org and German heritage records, 13 coal mines and 4 worker housing colonies (Zechensiedlungen) were digitized into 2 separate map layers, since mines and worker housing are different categories of site. 1 proposed worker colony was dropped during data checks because it was tied to steel production, not coal. Steelworks, railways, and roads from the same era were part of the original project idea, but were not digitized in this phase due to time limits and gaps in the archive record; this is listed as Future Work in Section 8.

<p align="center">
  <img src="outputs/plots/historical_geography.png" width="700">
</p>

**Figure 2.** A 19th century industrial map of Bochum, laid over the city's current boundary. This map is the base layer used to test whether traces of the industrial past still affect accessibility today.

### 3.3 Present Day Accessibility Model

Straight line "buffer circle" distance was not used on purpose. It would overstate real walking access, since it ignores buildings and city blocks that actually block a straight path. Instead, this study used true network distance of 1,125m (about a 15 minute walk), calculated with Dijkstra's algorithm from each service location. This matches how most current 15 minute city research measures distance. The model covered all 69,393 pedestrian street nodes and 169,668 street edges in Bochum, along with 786 essential service points (health, education, and daily needs locations) pulled from OSMnx. These 786 are point geometry OSM features only, since the accessibility model needs one coordinate per service; a hospital, school, or park that OSM maps as a building outline or polygon rather than a point is not counted here unless a separate point feature for it also exists. So this number reflects point represented services, not a full inventory of every mapped service facility. Each node was scored with a single yes or no flag: is it within 1,125m network distance of at least 1 service point, from any of 8 service categories? This means a node near only 1 pharmacy is treated the same as a node near a hospital, school, and supermarket combined. Section 7 discusses what this equal weighting choice means for the results, and Section 8 suggests a weighted or category count version as future work.

### 3.4 Statistical Testing and Confound Checks

Since past research shows city center distance predicts accessibility on its own, this study tested that link directly before drawing any conclusion about a historical site effect. 2 distances were compared: distance to historical site and distance to city center. Their correlation was measured, and a logistic regression was run using both distances together as predictors of accessibility, with results converted into odds ratios (percent change in odds per 100m) to make them easier to read. For each network node, the distance to the nearest historical site was calculated. Low accessibility and high accessibility node groups were then compared using a Welch's t test, and Cohen's d was reported using the pooled standard deviation.

### 3.5 Spatial Clustering (Local Moran's I)

Each street node was sorted into 1 of 4 spatial groups: High High (hot spot), Low Low (cold spot), High Low, or Low High (a spatial outlier), ranked from most to least accessible. First, spatial weights were built from all 69,393 street network nodes using their projected coordinates (EPSG:32632) and a K nearest neighbor method (k=8), row standardized. Then Local Moran's I (Anselin's LISA statistic) was calculated on the binary accessibility variable, using 999 conditional permutations (seed=42) and a significance level of p<0.05, with the `libpysal` and `esda` Python packages. This test asks a different question than the t test in Section 3.4. The t test only checks whether the 2 accessibility groups differ, on average, in distance to historical sites. This test checks something more specific, and it is the exact question this project set out to answer: is low accessibility itself spatially clustered, or scattered at random?

### 3.6 Robustness Check: Walking Threshold Sensitivity

Using the same 69,393 node network, the same service locations, and the same pre calculated historical site distances, the full pipeline, accessibility classification plus the Welch's t test, was re run at 2 new cutoffs: a stricter 10 minute walk (750m) and a looser 20 minute walk (1,500m). No new data was needed for this. The goal was to check whether the reversed pattern found at the original 15 minute cutoff (Sections 3.3 to 3.5) was just a result of that 1 time cutoff, or something more solid than that.

### 3.7 Multi City Replication: Essen

4 large coal mines (Zeche Zollverein, Zeche Carl Funke, Zeche Vereinigte Helene & Amalie, Zeche Pörtingsiepen) and 4 worker colonies (Siedlung Carl Funke, Mathias-Stinnes-Siedlung, Kolonie Zollverein III, Kolonie Beisen) were digitized from KuLaDig (North Rhine-Westphalia's official heritage GIS database) and German Wikipedia, then checked against Essen's administrative boundary (GADM v4.1) to confirm placement. Essen sits about 15km northeast of Bochum, in the same state. This test was set up from the start to answer a question named in Section 8 (Future Work): does the "path dependency of centrality" pattern hold only in Bochum, or does it also show up across the wider Ruhr Valley, which shares the same 19th century industrial history? Essen's 8 site dataset is smaller than Bochum's 17 site dataset. Essen's own historical archive, historischesportal.essen.de, lists around 1,700 mining related sites across the city. The same "major sites only" rule used for Bochum (Section 3.2) was applied here too. Essen's full pedestrian network (72,027 nodes, 188,198 edges) and 366 essential service points were pulled from OSMnx. The same 15 minute network distance threshold, Welch's t test, city center confound check (using Essen Hauptbahnhof, 51.4517°N 7.0134°E, as the reference point, matching the approach used for Bochum), and Local Moran's I procedure (Section 3.5) were applied without changes, with 1 exception: Essen's Local Moran's I was run at 99 permutations rather than the 999 later used for Bochum (Section 4.4), since p values were already stable at 99 permutations for this smaller dataset.

<p align="center">
  <img src="outputs/plots/study_area_essen.png" width="700">
</p>

**Figure 3.** Map of Essen's administrative boundary in North Rhine-Westphalia, Germany, the second Ruhr Valley city used to test whether the Bochum finding holds elsewhere. Directly comparable to Figure 1 (Bochum).

<p align="center">
  <img src="outputs/plots/essen_historical_geography.png" width="700">
</p>

**Figure 4.** Essen's historical coal mining geography: 4 coal mines and 4 worker colonies, digitized from KuLaDig and German Wikipedia. Directly comparable to Figure 2 (Bochum).

## 4. Results

### 4.1 Accessibility Coverage

85.8% of network nodes fell within a 15 minute walk of at least 1 essential service. The remaining 14.2% (9,858 nodes) did not.

<p align="center">
  <img src="outputs/plots/ghost_infrastructure_overlay.png" width="700">
</p>

**Figure 5.** Historical coal mining sites overlaid on present day 15 minute walking accessibility in Bochum. This map lays out the spatial relationship between old industrial sites and current accessibility, which the following sections test statistically.

### 4.2 The Reversed Relationship

In a sample this large (69,393 nodes), a statistically significant result does not always mean much in practice. Even a tiny difference can produce a very low p value at this scale. That is not what happened here. The effect size (Cohen's d=0.589, the group mean difference divided by pooled standard deviation) is medium to large. The numbers show this clearly: low accessibility nodes sit an average of 1,984m from the nearest historical site, while high accessibility nodes average only 1,450m, running counter to what the original hypothesis about industrial neglect predicted (Welch's t test: t=42.887, p<0.00001).

<p align="center">
  <img src="outputs/plots/distance_comparison_boxplot.png" width="700">
</p>

**Figure 6.** Box and whisker plot comparing distance to old coal mining sites for high and low accessibility nodes. Contrary to the original hypothesis, low accessibility areas sit farther from the old mining sites than high accessibility areas do.

### 4.3 Confound Check

Distance to a historical industrial site matters slightly more than distance to the city center: each 100m closer to a historical site raises the odds of 15 minute access by about 4.9%, compared to about 3.0% for each 100m closer to the city center. These 2 effects can be separated cleanly. The next question was how much overlap exists between them, and the answer is very little. The correlation between distance to historical site and distance to city center was low (r=0.063). A logistic regression with both variables together still found the historical site effect statistically significant after accounting for city center distance (coefficient=-0.0005, p<0.001). So the reversed effect is not simply standing in for the well known city center advantage described in the wider 15 minute city literature.

### 4.4 Spatial Clustering: Local Moran's I

Most low accessibility nodes sit inside a statistically significant Low Low cluster. Low accessibility in Bochum is not scattered randomly. It forms real neighborhoods of connected "cold spot" nodes, and these cold spot nodes sit noticeably farther from historical industrial sites than other nodes do. A direct comparison confirms this: nodes inside significant Low Low cold spot clusters average 1,992.3m from the nearest historical site, compared to 1,447.1m for nodes outside any significant cluster. In total, 10,273 of 69,393 nodes (close to 15%) showed statistically significant spatial clustering at p<0.05: 9,571 were Low Low (cold spot) and 702 were High Low outliers, with no significant High High or Low High clusters found. These 10,273 nodes describe 1 connected spatial pattern, not 10,273 separate, independent tests of the same idea. So no extra multiple testing correction was applied beyond the standard p<0.05 threshold, which is standard practice when using Local Moran's I to map clusters rather than to run a batch of unrelated hypothesis tests.

<p align="center">
  <img src="outputs/plots/lisa_cluster_map.png" width="700">
</p>

**Figure 7.** Local Moran's I cluster map. Blue nodes are significant "cold spot" (Low Low) clusters; gold nodes are significant spatial outliers (High Low); grey nodes are not significant. Triangles mark historical coal mines and diamonds mark worker colonies.

This result matches the original goal set for the spatial clustering test in this project. It agrees with the t test and logistic regression results in Sections 4.2 to 4.3, while answering a different question, 1 built specifically to account for spatial structure, instead of treating each node as an independent, unrelated data point.

### 4.5 Threshold Sensitivity Results

At all 3 thresholds tested, 10, 15, and 20 minutes, the odds ratio per 100m closer to a historical site stayed roughly the same (4.24% at 10 minutes, 4.88% at 15 minutes, 4.49% at 20 minutes), and remained significant (p<0.00001) after controlling for city center distance. The raw distances tell the same story. At the stricter 10 minute cutoff (750m, 67.1% coverage), low accessibility nodes still sat significantly farther from historical sites (1,778m vs. 1,402m; Welch's t=47.062, p<0.00001, Cohen's d=0.413). At the looser 20 minute cutoff (1,500m, 94.4% coverage), the same pattern held, and got stronger (2,098m vs. 1,492m; t=32.150, p<0.00001, Cohen's d=0.661), a bigger effect than the original 15 minute result (d=0.589). This suggests the finding is not just a result of choosing 15 minutes as the cutoff point. It looks like a solid pattern overall.

<p align="center">
  <img src="outputs/plots/threshold_sensitivity_comparison.png" width="750">
</p>

**Figure 8.** Left: effect size comparison of distance to nearest historical site by accessibility group. Right: mean distance to nearest historical site at 10, 15, and 20 minute thresholds. The reversed pattern holds, and grows stronger, at every threshold tested.

### 4.6 Multi City Replication: Essen

The Local Moran's I spatial clustering result is very close between the 2 cities: the mean Local Moran's I value across all nodes is 0.917 in Essen versus 0.923 in Bochum, and in both cities roughly the same share of low accessibility nodes sit inside significant Low Low cold spot clusters, 95.5% in Essen versus 97.1% in Bochum. Neither city showed any significant High High hot spot clusters. The raw reversed relationship also holds up in both direction and significance: low accessibility nodes in Essen (n=8,267) sit an average of 3,693m from the nearest historical site, compared to 3,130m for high accessibility nodes (n=63,760), Welch's t=24.731, p<0.00001, though with a smaller effect size than Bochum (Cohen's d=0.338 versus 0.589). Essen's results are a genuine mix of confirmation and disagreement, and both sides are reported here, not only the confirming part.

<p align="center">
  <img src="outputs/plots/essen_ghost_infrastructure_overlay.png" width="700">
</p>

**Figure 9.** Historical industrial sites overlaid on present day 15 minute walking accessibility in Essen. Directly comparable to Figure 5 (Bochum).

<p align="center">
  <img src="outputs/plots/essen_distance_comparison_boxplot.png" width="700">
</p>

**Figure 10.** Distance to historical sites for high and low accessibility nodes in Essen, comparable to Figure 6 (Bochum). Low accessibility nodes again sit farther from historical sites, with a smaller but similar effect.

Both cities showed a strong, consistent city center effect (odds per 100m closer to the center: 3% in Bochum, 4.2% in Essen). What did not hold up across cities was confound independence. The correlation between distance to historical site and distance to city center is r=0.405 in Essen, much higher than Bochum's r=0.063. This means that in Essen, distance to city center and distance to historical site are not nearly as separate from each other as they are in Bochum. Because of this, when both distances are entered into a single logistic regression, the sign of the historical site coefficient flips in Essen (coefficient=+0.000114, p<0.00001), while the city center coefficient itself stays negative in both cities. In plain terms: in Essen, being farther from a historical site starts to look like it raises the odds of good accessibility, once city center distance is already accounted for. Bochum works the other way around.

<p align="center">
  <img src="outputs/plots/bochum_essen_comparison.png" width="800">
</p>

**Figure 11.** Side by side comparison of Bochum and Essen across the 3 statistical tests. The raw reversed effect and the spatial clustering result both replicate; the confound independence result does not.

<p align="center">
  <img src="outputs/plots/essen_lisa_cluster_map.png" width="700">
</p>

**Figure 12.** Local Moran's I cluster map for Essen, directly comparable to Figure 7 (Bochum).

2 explanations were tested for why the confound independence result did not hold up in Essen. First, Essen's historical industrial sites may simply sit closer to its city center than Bochum's sites do. The Krupp steelworks, just outside this study's scope, which covers coal mining only, sat close to central Essen, while Bochum's coal mining sites were more spread out. Second, Essen's smaller dataset (8 sites, versus Bochum's 17) may itself be pulling the 2 distance measures closer together. Fewer reference points spread across a smaller area can make "distance to nearest site" start to track "distance from center" just from thinner spatial coverage, even without any real underlying effect. Some evidence favors this second explanation: when the Essen dataset was expanded from 6 sites to 8 sites, the correlation dropped from r=0.475 to r=0.405. That fits the sample size explanation, though it does not prove it (see Section 7, Limitations, for more on why this specific sub finding should be treated as provisional). Neither explanation contradicts the main finding. If anything, the Essen result strengthens the core idea, that industrial density leaves a lasting, statistically visible mark on connectivity, while showing that the stronger, more specific claim, that this mark is unrelated to city center proximity, does not automatically hold true in every city.

## 5. Discussion

Bochum's coal and steel infrastructure was built in the 19th century for a practical reason: to serve a large, concentrated workforce. That meant dense roads, dense markets, and dense housing. This study's results suggest that this dense footprint has outlasted the industry itself. The street connectivity and service density it created are still measurable more than 50 years after the mines closed, even though today's city center sits elsewhere. This extends path dependency research, usually applied to whole city growth patterns or port city institutions, down to a much smaller scale: everyday walking access inside a single city. None of this weakens the core finding that centrality, whether historical or present day, predicts better accessibility. If anything, it reframes that finding: this looks like a "path dependency of centrality," not a "path dependency of neglect."

This does not mean industrial areas were neglected. The data tells a different story. The name "Ghost Infrastructure" points to something that no longer exists economically but still shapes the city physically: the mines are gone, but their mark on the street layout is not. The "ghost" here is not a haunted, abandoned place. It is a cause (the coal industry) that has disappeared, while its effect (durable centrality and connectivity) remains, and that effect is clearly positive.

This does not overturn the general idea above, but it does add a caveat. The underlying mechanism may be shared across cities, while exactly how much historical versus present day centrality drives today's accessibility may vary by city, depending on each place's own industrial and administrative history. The Essen replication (Section 4.6) supports this caveat directly: the centrality and connectivity legacy shows up in both cities, but the stronger version of that legacy, independent of the present day city center, looks, on current evidence, more specific to Bochum than general to the whole Ruhr Valley.

## 6. Policy Implications

The accessibility gaps in this study are not inside the old industrial core. They sit on the edges, in newer neighborhoods built more recently. This points to where 15 minute city investment is most needed: not the historical industrial core, which already performs well, but these newer, peripheral areas. For planning, this suggests 2 things at once. First, keeping the old industrial hubs accessible, through infill development, mixed use zoning, and ongoing service provision, protects an asset the city already has, rather than something that needs saving. Second, heritage led regeneration of the old industrial core is still worthwhile, but it should be seen as building on a strength the city already has in accessibility terms, not as fixing its biggest accessibility problem, since that problem actually sits elsewhere in the city.

## 7. Limitations

These results should be read as spatial associations, not proven cause and effect. Factors like income, age, how long people have lived somewhere, and car ownership were not collected, so they could not be controlled for. A separate caution applies to sample size: the 69,393 street network nodes used in the Local Moran's I test (Section 4.4) are not independent of each other. Nearby nodes on the same street are naturally correlated, so this count should not be read as 69,393 independent data points. To address this directly, a network block bootstrap was run as an extra check (`network_block_bootstrap.py`, in the project repository). Instead of resampling individual nodes 1 at a time, which assumes independence, this method splits the street network into 2,598 connected blocks, each grown outward from a random starting node toward a target size of 500 nodes, and resamples whole blocks, with replacement, 999 times, refitting the same tests each time. In practice, most blocks stopped growing well before reaching 500 nodes, because the pedestrian network itself breaks into many small, disconnected pieces (dead ends, unlinked footway fragments). The real average block size came out to about 27 nodes (69,393 nodes divided by 2,598 blocks). The 500 node figure was only ever a target for the block growing algorithm, not the actual result. The observed distance difference (534.25m) produced a 95% bootstrap confidence interval of [199.90m, 885.16m], which stays clear of 0. The logistic regression coefficients for both distance measures also produced confidence intervals that stay clear of 0. Because this method treats the network's own connected structure as the unit being resampled, instead of treating each of the 69,393 nodes as independent, this result gives stronger evidence that the finding is not just a side effect of spatial autocorrelation. A follow up check confirms this is not specific to the 500 node target: re running the same bootstrap at 250 node and 1,000 node targets (`network_block_bootstrap_sensitivity.py`) gave 95% confidence intervals of [292.21m, 803.04m] at 250 nodes and [135.78m, 884.20m] at 1,000 nodes, both clear of 0, matching the 500 node result. The historical site logistic coefficient stayed negative and clear of 0 at every target size tested (250: [-0.000713, -0.000273]; 500: [-0.000755, -0.000212]; 1,000: [-0.000822, -0.000198]). As expected, the interval widens somewhat as block size grows, since fewer, larger blocks mean more resampling variance, but the direction of the effect and its distance from 0 hold at every setting tested. On the data side, the worker colony dataset (4 sites) is smaller than the coal mine dataset (13 sites), which limits how much can be said about colonies specifically. Both datasets cover only the major, well documented sites from Bochum's industrial era. No claim is made about coverage of the roughly 200 additional smaller sites (Kleinzechen, Erbstollen) in Bochum's full historical mining record, since those sites are not comparable in scale or documentation to the ones used here. This study also treats historical sites as points rather than mapped boundaries, due to project time limits, and it did not digitize historical rail or road infrastructure in this phase, even though that was part of the original project scope (see Section 8, Future Work). All essential service categories were weighted equally in the accessibility model, which does not reflect real differences in how important each service type is to daily life. Finally, the city center reference point used for the confound check (Bochum Hauptbahnhof) sits only a few hundred meters from a second plausible reference point (the Rathaus, the city's commercial center), and no second reference point could be validated for a robustness check. A different choice of city center might shift the confound estimate slightly, but given how low the correlation already is (r=0.063), a large change seems unlikely.

The historical site to city center correlation in Essen was 0.475 in an earlier, 6 site version of the dataset, and 0.405 in the current 8 site version, a real drop, which fits with the idea that dataset size may explain part of the correlation. Still, expanding the Essen dataset further, toward Bochum's 17 site scale, would need more time and better source records than this round of the project allowed (see Section 8, Future Work). Essen's own historical mining record lists around 1,700 sites citywide (per the Essen historical portal), so the 8 site dataset used here is a small sample of that full record, similar to how Bochum's 17 sites are a small sample of Bochum's own historical record. As with Bochum, this means the Essen confound results should be treated as provisional rather than final. The 2 Essen GIS layers used here (`essen_coal_mines.gpkg` and `essen_zechensiedlungen.gpkg`) contain all 4 mines and 4 colonies described above, so every number reported for Essen can be reproduced directly by re running `run_essen_pipeline.py` against the project's own data.

## 8. Future Work

2 directions planned at the start of this project were completed during the project itself, and are now reported in Sections 3.6 to 3.7 and 4.5 to 4.6: walking threshold sensitivity (confirmed to hold at 10 and 20 minute thresholds) and a second city comparison (replicated in Essen, with a mixed result, see Section 4.6). The directions below remain open for future work:

- Expand the Essen historical dataset closer to Bochum's scale, to properly test whether the confound independence result is a real Bochum vs Essen difference or a sample size effect. A starting point would be the roughly 1,700 mining sites listed at historischesportal.essen.de.
- Test whether the historical site effect still holds after controlling for present day socioeconomic factors, income, age, length of residence, car ownership, using German census (Zensus) data.
- Extend the multi city comparison beyond Bochum and Essen to other Ruhr Valley cities, such as Dortmund or Gelsenkirchen, to see whether Essen's departure from Bochum's pattern is the exception or the rule.
- Replace point based mine and colony locations with mapped site boundaries, to check whether the result depends on how sites are represented spatially.
- Test whether the historical site effect is stronger in some parts of Bochum (or Essen) than others, by modeling it as a spatially varying effect instead of 1 fixed value for the whole city.
- Replace the equal weighting of service categories with a weighted index that reflects real differences in importance. For example, weighting groceries, healthcare, and green space more heavily.
- Digitize historical rail and road infrastructure from the same era (as originally planned, see Section 3.2), to test whether access to old transport routes, not just mines and colonies, also predicts present day accessibility.
- Revisit spatial clustering using network based neighbor definitions instead of KNN. An early attempt at this produced a very different result from the KNN based version, most likely because a fixed network distance cutoff gives each node a much larger and more uneven neighbor count than a fixed k=8 does. That version is not used as a validated finding here, and is left for future work using a neighbor definition that compares more directly with the KNN method used here.
- Extend the current single snapshot design into a time series study, to see how this accessibility advantage has changed over time, rather than looking at just 1 point in time.

## 9. Conclusion

Testing a surprising result against its most obvious alternative explanation, and backing it up with an independent spatial clustering check, can reveal more than simply taking a first result at face value. That was the goal of this study. Bochum's industrialization began almost 150 years ago, and its last coal mine closed more than 50 years ago. Yet the city's 19th century industrial infrastructure still leaves a measurable mark today. That mark is not neglect, as the original hypothesis assumed, but a lasting, statistically significant boost to walking accessibility, confirmed by more than 1 method. This result points toward a new way to test path dependency ideas with real numbers, not just narrative.

A partial or imperfect result, reported honestly, is worth more than a tidier looking result that hides its rough edges. In that spirit, this study reports the Essen replication in full, including the part that did not match Bochum. The central finding held up under 2 separate robustness checks: it stayed significant at both a 10 minute and a 20 minute threshold, and it replicated across the full Essen pipeline, where the underlying "path dependency of centrality" pattern showed up again, even though the narrower claim, that this pattern is independent of city center distance, did not carry over as cleanly.

## References

Arthur, W. B. (1988). Urban Systems and Historical Path Dependence. In *Cities and Their Vital Systems: Infrastructure Past, Present, and Future* (pp. 85–97). National Academies Press. [https://www.nationalacademies.org/read/1093/chapter/5](https://www.nationalacademies.org/read/1093/chapter/5)

Görmar, F., & Harfst, J. (2019). Path Renewal or Path Dependence? The Role of Industrial Culture in Regional Restructuring. *Urban Science*, 3(4), 106. [https://doi.org/10.3390/urbansci3040106](https://doi.org/10.3390/urbansci3040106)

Hein, C., & Schubert, D. (2021). Resilience and Path Dependence: A Comparative Study of the Port Cities of London, Hamburg, and Philadelphia. *Journal of Urban History*, 47(2), 389–419. [https://doi.org/10.1177/0096144220925098](https://doi.org/10.1177/0096144220925098)

Bruno, M., Melo, H. P. M., Campanelli, B., & Loreto, V. (2024). A universal framework for inclusive 15-minute cities. *Nature Cities*, 1(10), 633–641. [https://doi.org/10.1038/s44284-024-00119-4](https://doi.org/10.1038/s44284-024-00119-4)

Omwamba, J., Rotaris, L., & Longo, G. (2025). An assessment of proximity in the 15-Minute City: A systematic literature review. *Urban Transitions*, 3, 100012. [https://doi.org/10.1016/j.ubtr.2025.100012](https://doi.org/10.1016/j.ubtr.2025.100012)

Moreno, C., Gall, C., Woo, J., Lee, D., & Bencekri, M. (2025). Assessing accessibility of cultural sites through the 15-minute city framework in Seoul. *International Journal of Urban Sciences*, 29(1), 8–39. [https://doi.org/10.1080/12265934.2025.2462820](https://doi.org/10.1080/12265934.2025.2462820)
