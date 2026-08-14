# 🏭 GHOST INFRASTRUCTURE

**How 19th-Century Coal Geography Still Shapes Who Gets a "15-Minute Life" Today**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21761320.svg)](https://doi.org/10.5281/zenodo.21761320)

## 🔗 Live Dashboard

**Live Dashboard**: `https://ghostinfrastructure-areytvp4x8ofu6l5tosj2z.streamlit.app/`

*(Copy and paste this URL directly into your browser's address bar for correct rendering — clicking through GitHub's link preview can occasionally cause a temporary layout glitch on first load, which resolves after a single page refresh.)*

## 📄 Project Documentation

| Document | What's Inside |
|---|---|
| ⚡ [`GI_Executive_Summary.pdf`](./GI_Executive_Summary.pdf) | One-page snapshot — question, method, headline finding, robustness checklist, and links (fastest overview) |
| 📘 [`GI_Project_Report.md`](./GI_Project_Report.md) | Polished project summary — methodology, findings, conclusions (start here) |
| 📗 [`GI_Research_Paper.md`](./GI_Research_Paper.md) | Formal academic paper — literature review, statistical methodology, results, discussion |
| 📙 [`GI_Development_Log.md`](./GI_Development_Log.md) | Full technical development log — every bug, debugging session, and methodology iteration |

---

GHOST INFRASTRUCTURE is a historical-cartographic and spatial-network research project testing whether Bochum's 19th and 20th-century coal-mining industrial geography — mine locations and worker-housing colonies (Zechensiedlungen) — continues to structurally predict present-day "15-minute city" accessibility, more than half a century after the region's last coal mine closed.

Rather than treating "industrial legacy" as a qualitative, narrative concept, this project makes it spatially and statistically measurable — directly testing digitized historical geography against a network-based measure of present-day urban accessibility.

The core finding is tested for robustness two ways: across three walking-time thresholds (10/15/20-minute), and via an independent multi-city replication in Essen. Both extensions are reported in full, including the parts that don't cleanly replicate — see "What This Project Does" below.

---

## 🗺️ Interactive Maps & Plots

Interactive maps and headline charts are hosted via GitHub Pages:

**Maps**
- [Bochum — Historical Sites + Accessibility Overlay (QGIS)](https://sakshimaske303-commits.github.io/GHOST_INFRASTRUCTURE/outputs/maps/ghost_infrastructure_overlay_map/index.html)
- [Essen — Historical Sites + Accessibility Overlay (Python/folium)](https://sakshimaske303-commits.github.io/GHOST_INFRASTRUCTURE/outputs/maps/essen_interactive_map.html)

**Plots**
- [Bochum vs. Essen Multi-City Comparison](https://sakshimaske303-commits.github.io/GHOST_INFRASTRUCTURE/outputs/plots/interactive/bochum_essen_comparison.html)
- [Walking-Time-Threshold Sensitivity](https://sakshimaske303-commits.github.io/GHOST_INFRASTRUCTURE/outputs/plots/interactive/threshold_sensitivity.html)
- [Distance-to-Historical-Site Comparison](https://sakshimaske303-commits.github.io/GHOST_INFRASTRUCTURE/outputs/plots/interactive/distance_comparison_boxplot.html)

*(All five are also embedded together on the dashboard's Interactive Maps & Plots page.)*

---

## 📊 What This Project Does

- Digitizes 13 historical coal mines and 4 worker-housing colonies in Bochum (from Mindat.org and German heritage archives), plus 4 mines and 4 colonies in Essen (from KuLaDig and Wikipedia) for an independent multi-city replication, kept as structurally distinct GIS layers
- Builds a true network-based 15-minute accessibility model across Bochum's complete 69,393-node and Essen's 72,027-node pedestrian street networks (not a simplified straight-line radius)
- Statistically tests whether historical industrial-site proximity predicts present-day accessibility
- Explicitly verifies the finding against its most obvious confound — city-center proximity — using correlation analysis and logistic regression
- Independently corroborates the finding with a Local Moran's I (LISA) spatial-clustering analysis across all network nodes, in both cities
- Tests robustness at three walking-time thresholds (10/15/20-minute) and confirms the effect holds — and strengthens — at every one
- Presents all findings through an interactive dashboard with a live distance-threshold explorer, QGIS- and Python-based interactive maps, and Plotly interactive plots

## 🔬 Key Finding

**A reversed, independently-verified effect.** The hypothesis was that historical industrial sites would predict present-day neglect. The evidence showed the opposite: low-accessibility zones are, on average, *further* from historical industrial sites (1,984m) than high-accessibility zones (1,450m) — a highly significant relationship (Welch's t-test, t=42.887, p<0.00001, Cohen's d=0.589). This holds independently of city-center proximity (correlation r=0.063; logistic regression coefficient=-0.0005, p<0.001, controlling for city-center distance) — a genuine **"path dependency of centrality"** rather than the originally hypothesized "path dependency of neglect." A Local Moran's I spatial-clustering analysis independently corroborates this: 97.1% of low-accessibility nodes fall inside statistically significant spatial cold-spot clusters, confirming low accessibility is not randomly scattered but forms genuine, spatially contiguous zones farther from historical industrial sites.

**Replicated — with an honestly-reported nuance — in a second city.** The same methodology run on Essen reproduces the raw reversed effect (Cohen's d=0.338) and the spatial-clustering result (95.5% vs. Bochum's 97.1%) almost exactly. It does *not* reproduce the confound-independence result: in Essen, historical-site distance correlates moderately with city-center distance (r=0.405 vs. Bochum's r=0.063), and the historical-site effect's sign reverses once city-center distance is controlled for. Both cities' results are reported in full — the underlying "centrality legacy" mechanism appears to generalize; the stronger claim that it's independent of city-center proximity, on current evidence, does not.

Full methodology, including two independently-verified map anomalies traced to genuine historical geography (not data errors), is documented in the dashboard's Methodology page and in `GI_Project_Report.md`.

## 🗂️ Repository Structure

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
│   └── maps/                        # Interactive QGIS2Web + folium map exports
├── GI_Project_Report.md             # Polished project summary and methodology
├── GI_Research_Paper.md             # Formal academic research paper
├── GI_Development_Log.md            # Full technical development log
├── map*.py                          # Visualization scripts
├── spatial_clustering_lisa.py       # Local Moran's I (LISA) spatial-clustering analysis (Bochum)
├── threshold_sensitivity.py         # 10/20-min robustness check (Bochum)
├── download_network_essen.py        # Essen OSM network download
├── run_essen_pipeline.py            # Full Essen accessibility + statistics pipeline
└── requirements.txt
```

## 🛠️ Tech Stack

Python · GeoPandas · OSMnx · NetworkX · Statsmodels · Plotly · Streamlit · QGIS · QGIS2Web · GitHub Pages

## 📚 Data Sources

| Dataset | Provider |
|---|---|
| Coal Mine Locations (Bochum) | Mindat.org |
| Worker Colonies (Zechensiedlungen), Bochum | Wikipedia, Route Industriekultur, ruhr-bauten.de |
| Coal Mine Locations & Worker Colonies (Essen) | KuLaDig (Kultur.Landschaft.Digital, NRW state heritage GIS), Wikipedia |
| City Boundary | GADM v4.1 |
| Street Network & Essential Services | OpenStreetMap via OSMnx |

## ▶️ Running Locally

```bash
git clone https://github.com/sakshimaske303-commits/GHOST_INFRASTRUCTURE.git
cd GHOST_INFRASTRUCTURE
pip install -r requirements.txt
cd dashboard
streamlit run app.py
```

## 👤 Author

**Sakshi D. Maske**

Independent Geospatial Researcher

## 📜 License

This project is licensed under [CC BY 4.0](LICENSE). See `CITATION.cff` for citation metadata.

---

*This project's full development process — including every debugging session and independently-verified map anomaly — is documented in `GI_Development_Log.md` for full transparency and reproducibility.*