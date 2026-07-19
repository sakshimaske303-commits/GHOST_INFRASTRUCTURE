# 🏭 GHOST INFRASTRUCTURE

**How 19th-Century Coal Geography Still Shapes Who Gets a "15-Minute Life" Today**

## 🔗 Live Dashboard

**[View the interactive dashboard →](https://ghostinfrastructure-areytvp4x8ofu6l5tosj2z.streamlit.app/)

## 📄 Project Documentation

| Document | What's Inside |
|---|---|
| 📘 [`Project_Journal.md`](./Project_Journal.md) | Polished project summary — methodology, findings, conclusions (start here) |
| 📗 [`Research_Paper.md`](./Research_Paper.md) | Formal academic paper — literature review, statistical methodology, results, discussion |
| 📙 [`Devlopment_Log.md`](./Devlopment_Log.md) | Full technical development log — every bug, debugging session, and methodology iteration |

---

GHOST INFRASTRUCTURE is a historical-cartographic and spatial-network research project testing whether Bochum's 19th and 20th-century coal-mining industrial geography — mine locations and worker-housing colonies (Zechensiedlungen) — continues to structurally determine present-day "15-minute city" accessibility, more than half a century after the region's last coal mine closed.

Rather than treating "industrial legacy" as a qualitative, narrative concept, this project makes it spatially and statistically measurable — directly testing digitized historical geography against a network-based measure of present-day urban accessibility.

---

Interactive geospatial map hosted via GitHub Pages: **[View the interactive overlay map →](https://sakshimaske303-commits.github.io/GHOST_INFRASTRUCTURE/outputs/maps/ghost_infrastructure_overlay_map/index.html)**

---

## 📊 What This Project Does

- Digitizes 13 historical coal mines and 4 worker-housing colonies from Mindat.org and German heritage archives, kept as two structurally distinct GIS layers
- Builds a true network-based 15-minute accessibility model across Bochum's complete 69,393-node pedestrian street network (not a simplified straight-line radius)
- Statistically tests whether historical industrial-site proximity predicts present-day accessibility
- Explicitly verifies the finding against its most obvious confound — city-center proximity — using correlation analysis and logistic regression
- Presents all findings through an interactive dashboard with a live distance-threshold explorer and QGIS-based interactive maps

## 🔬 Key Finding

**A reversed, independently-verified effect.** The hypothesis was that historical industrial sites would predict present-day neglect. The evidence showed the opposite: low-accessibility zones are, on average, *further* from historical industrial sites (1,984m) than high-accessibility zones (1,450m) — a highly significant relationship (Welch's t-test, t=42.887, p<0.00001). This holds independently of city-center proximity (correlation r=0.063; logistic regression coefficient=-0.0005, p<0.001, controlling for city-center distance) — a genuine **"path dependency of centrality"** rather than the originally hypothesized "path dependency of neglect."

Full methodology, including two independently-verified map anomalies traced to genuine historical geography (not data errors), is documented in the dashboard's Methodology page and in `Project_Journal.md`.

## 🗂️ Repository Structure

```text
GHOST_INFRASTRUCTURE/
├── dashboard/                       # Streamlit dashboard (7 pages)
├── data/
│   ├── historical_georeferenced/    # 13 coal mines, 4 worker colonies (GeoPackage)
│   ├── accessibility/               # 69,393-node network accessibility model
│   ├── boundaries/                  # Bochum city boundary (GADM)
│   └── osm_network/                 # Street network + essential services (OSMnx)
├── outputs/
│   ├── plots/                       # Static visualizations
│   └── maps/                        # Interactive QGIS2Web map export
├── Project_Journal.md               # Polished project summary and methodology
├── Research_Paper.md                # Formal academic research paper
├── Devlopment_Log.md                # Full technical development log
├── map*.py                          # Visualization scripts
└── requirements.txt
```

## 🛠️ Tech Stack

Python · GeoPandas · OSMnx · NetworkX · Statsmodels · Plotly · Streamlit · QGIS · QGIS2Web · GitHub Pages

## 📚 Data Sources

| Dataset | Provider |
|---|---|
| Coal Mine Locations | Mindat.org |
| Worker Colonies (Zechensiedlungen) | Wikipedia, Route Industriekultur, ruhr-bauten.de |
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

---

*This project's full development process — including every debugging session and independently-verified map anomaly — is documented in `Devlopment_Log.md` for full transparency and reproducibility.*