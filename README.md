# GHOST INFRASTRUCTURE

**How 19th-Century Coal Geography Still Shapes Who Gets a "15-Minute Life" Today**

[![EarthArXiv](https://img.shields.io/badge/EarthArXiv-Preprint-B7410E.svg)](https://eartharxiv.org/repository/view/14809/) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21761320.svg)](https://doi.org/10.5281/zenodo.21761320)

## Live Dashboard

**Live Dashboard**: `https://ghostinfrastructure-areytvp4x8ofu6l5tosj2z.streamlit.app/`

*(Copy and paste this URL directly into your browser's address bar for correct rendering — clicking through GitHub's link preview can occasionally cause a temporary layout glitch on first load, which resolves after a single page refresh.)*

## Project Documentation

| Document | What's Inside |
|---|---|
| [`GI_Executive_Summary.md`](./GI_Executive_Summary.md) / [`.pdf`](./GI_Executive_Summary.pdf) | One-page snapshot — project overview, question, method, headline finding, robustness checklist, and links (start here) |
| [`GI_Research_Paper.md`](./GI_Research_Paper.md) | Formal academic paper — literature review, statistical methodology, results, discussion |
| [`GI_Development_Log.md`](./GI_Development_Log.md) | Full technical development log — every bug, debugging session, and methodology iteration |

---

The research project GHOST INFRASTRUCTURE investigates on the analytical level if the spatial distribution of coal mining areas and workers' quarters (Zechensiedlungen), which are characteristic elements of the industrial geography of Bochum’s 19th and 20th century, continues to structurally reflect the degree of present-day "15-minute city" accessibility – more than 50 years after the final closure of the last coal mine in the region.

But instead of using the term “industrial legacy” as a qualitative narrative metric, this project provides a new spatially and statistically quantifiable alternative measure: it tests something derived from historical geography (the digitized data) against a measure of urban accessibility derived from the network.

This core finding is tested for robustness, both across three walking-time thresholds - 10 – 15 – 20 minutes - and using an independent although comparable multi-city replication in Essen. Both extensions are reported in full, including the parts that are not easily replicable — see "What This Project Does" below.

---

## Interactive Maps & Plots

Interactive maps and headline charts are hosted via GitHub Pages:

**Maps**
- [Bochum — Historical Sites + Accessibility Overlay (Python/folium)](https://sakshimaske303-commits.github.io/GHOST_INFRASTRUCTURE/outputs/maps/bochum_interactive_map.html)
- [Essen — Historical Sites + Accessibility Overlay (Python/folium)](https://sakshimaske303-commits.github.io/GHOST_INFRASTRUCTURE/outputs/maps/essen_interactive_map.html)

**Plots**
- [Bochum vs. Essen Multi-City Comparison](https://sakshimaske303-commits.github.io/GHOST_INFRASTRUCTURE/outputs/plots/interactive/bochum_essen_comparison.html)
- [Walking-Time-Threshold Sensitivity](https://sakshimaske303-commits.github.io/GHOST_INFRASTRUCTURE/outputs/plots/interactive/threshold_sensitivity.html)
- [Distance-to-Historical-Site Comparison](https://sakshimaske303-commits.github.io/GHOST_INFRASTRUCTURE/outputs/plots/interactive/distance_comparison_boxplot.html)

*(All five are also embedded together on the dashboard's Interactive Maps & Plots page.)*

---

## What This Project Does

- Digitizes 13 historical coal mines and 4 worker housing colonies in Bochum from the Mindat.org archive and German heritage archives, stored as structurally separate GIS layers, plus 4 mines and 4 colonies in Essen from KuLaDig (Kultur.Landschaft.Digital) and Wikipedia for an independent multi-city replication
- Creates a connecting web of 15 minutes walking time for the entire pedestrian street network in Bochum and Essen (72,027 nodes in Essen, 69,393 nodes in Bochum) and not the area that is traversed in a straight line (radius) as is often used in simplified scenarios.
- Tests statistical significance of historical statistical link between industrial sites and accessibility
- Correlates and/or conducts logistic regression analyses to explicitly determine that the observed finding is not due to the most readily available confounder (city-center proximity, in this case)
- Runs a local spatial-cluster analysis (LISA) on finding at each node of network in both cities (using Local Moran's I)
- Tests its robustness at 3 walking-time cutpoints (10, 15, 20 minutes-cut) and finds that its effect remains and is enhanced at each cut
- Represents all results using a live distance-threshold explorer in an interactive dashboard, Python (folium) maps, and Plotly interactive plots

## Key Finding

An “inverted” effect, confirmed by a complementary spatial-statistical test. The hypothesis was historical industrial sites would be predictive of current site neglect. Contrary to the hypothesis, the evidence showed the opposite — the distance of low accessibility zones from historical industrial sites (1,984m) was on average, *further* than the distance that high accessibility zones were from historical industrial sites (1,450m): a medium-to-large, practically meaningful effect (Welch's t-test: Cohen's d=0.589; t=42.887, p<0.00001 — see the note below on how to read that p-value). This holds up against city-center proximity as a confound: there was practically no correlation between the two (r=0.063), and no presence of a "path dependency of neglect" as originally hypothesized, but a "path dependency of centrality". This is also supported by a complementary Local Moran's I spatial-clustering analysis — the same accessibility data viewed through a different statistical lens — which shows that 97.1% of low-accessibility nodes are contained within statistically significant spatial cold-spot clusters that support the notion that low accessibility is not random; it creates genuine, statistically significant and contiguous spatial low-accessibility zones, further from historical industrial sites. (Note: with 69,393 network nodes that are spatially correlated with their neighbors rather than independent observations, the p-values above are not the p-values of 69,393 independent samples — they should be read as evidence of a real, sizeable effect, with the effect size (Cohen's d) and the robustness/replication checks below carrying more weight than the p-value itself; see the Limitations section of `GI_Research_Paper.md` for the full discussion.)

Replicated - with a sincere nuance - in a second city. The same method applied to Essen generates the same raw reversed effect (Cohen's d=0.338) and the same result for the spatial clustering (95.5% vs. Bochum's 97.1%). However, it does not replicate the confounds-independence result: There exists a modest correlation between historical-site distance and city-center distance in Essen (r=0.405) but not in Bochum (r=0.063); controlling for city-center distance causes the sign of the historical-site effect to flip. The underlying "centrality legacy" mechanism itself appears to generalize across both cities; the stronger claim that it is independent of city-center proximity, on current evidence, does not.

The dashboard's Methodology page lists full methodology, as well as two independently-verified anomalies in the maps that are identified as genuine historical geography and not data errors, in the Project Overview of the `GI_Executive_Summary.md` and in the `GI_Development_Log.md`.

## Repository Structure

```text
GHOST_INFRASTRUCTURE/
├── dashboard/                       # Streamlit dashboard
├── data/
│   ├── historical_georeferenced/    # Bochum: 13 mines, 4 colonies; Essen: 4 mines, 4 colonies (GeoPackage)
│   ├── accessibility/               # Network accessibility models, both cities
│   ├── boundaries/                  # Bochum + Essen city boundaries (GADM)
│   └── osm_network/                 # Street networks + essential services (OSMnx), both cities
├── outputs/
│   ├── plots/                       # Static visualizations, including multi-city + threshold comparisons
│   │   └── interactive/             # Plotly interactive HTML charts
│   └── maps/                        # Interactive folium map exports
├── GI_Research_Paper.md             # Formal academic research paper
├── GI_Development_Log.md            # Full technical development log
├── map*.py                          # Visualization scripts
├── spatial_clustering_lisa.py       # Local Moran's I (LISA) spatial-clustering analysis (Bochum)
├── threshold_sensitivity.py         # 10/20-min robustness check (Bochum)
├── download_network_essen.py        # Essen OSM network download
├── run_essen_pipeline.py            # Full Essen accessibility + statistics pipeline
└── requirements.txt
```

## Tech Stack

Python · GeoPandas · OSMnx · NetworkX · Statsmodels · Plotly · Folium · Streamlit · GitHub Pages

## Data Sources

| Dataset | Provider |
|---|---|
| Coal Mine Locations (Bochum) | Mindat.org |
| Worker Colonies (Zechensiedlungen), Bochum | Wikipedia, Route Industriekultur, ruhr-bauten.de |
| Coal Mine Locations & Worker Colonies (Essen) | KuLaDig (Kultur.Landschaft.Digital, NRW state heritage GIS), Wikipedia |
| City Boundary | GADM v4.1 |
| Street Network & Essential Services | OpenStreetMap via OSMnx |

## Running Locally

```bash
git clone https://github.com/sakshimaske303-commits/GHOST_INFRASTRUCTURE.git
cd GHOST_INFRASTRUCTURE
pip install -r requirements.txt
cd dashboard
streamlit run app.py
```

## Author

**Sakshi D. Maske**

Independent Geospatial Researcher

## License

This project is licensed under [CC BY 4.0](LICENSE). See `CITATION.cff` for citation metadata.

---

*This project's full development process — including every debugging session and independently-verified map anomaly — is documented in `GI_Development_Log.md` for full transparency and reproducibility.*