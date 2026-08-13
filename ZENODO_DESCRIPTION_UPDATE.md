# Zenodo Record Update — GHOST_INFRASTRUCTURE

Notes for the next release. The existing DOI stays the same (`10.5281/zenodo.21761320`) — Zenodo
versions a record rather than replacing it. Plan: cut a new GitHub release (tag `v1.1.0`) once all
the files above are pushed; the GitHub↔Zenodo integration will auto-mint a new version under the
same concept DOI. Release title: **"v1.1.0 — Multi-City Robustness (Essen) + Threshold
Sensitivity"**.

New **Zenodo Description** field (replaces the existing one):

---

GHOST INFRASTRUCTURE tests whether Bochum's 19th and 20th-century coal-mining industrial geography
— mine locations and worker-housing colonies (Zechensiedlungen) — continues to structurally predict
present-day "15-minute city" walking accessibility, more than half a century after the region's last
coal mine closed. Contrary to the hypothesis that historical industrial sites would predict
present-day neglect, a Welch's t-test across Bochum's complete 69,393-node pedestrian street network
found the opposite: low-accessibility zones are significantly *further* from historical industrial
sites (t=42.887, p<0.00001, Cohen's d=0.589) — a "path dependency of centrality" rather than a
"path dependency of neglect." This is verified against its most obvious confound (city-center
proximity, r=0.063, genuinely independent) and independently corroborated by a Local Moran's I
spatial-clustering analysis (97.1% of low-accessibility nodes fall in significant cold-spot
clusters).

**v1.1.0 adds two robustness extensions.** First, the finding holds — and strengthens — at 10-minute
and 20-minute walking thresholds, not only the original 15-minute threshold (Cohen's d ranges
0.413–0.661). Second, the full methodology was independently replicated in Essen, a second Ruhr
Valley city (72,027-node network, 4 mines + 4 worker colonies digitized from KuLaDig and Wikipedia).
The raw reversed effect and the spatial-clustering result both replicate in Essen; the
confound-independence result does not — Essen's historical-site distance correlates moderately with
city-center distance (r=0.405, versus Bochum's r=0.063), and the historical-site effect's sign
reverses once city-center distance is controlled for. Both results are reported in full, including
two competing explanations tested for the discrepancy (genuine city-level difference vs. a
sample-size/coverage-density artifact of Essen's smaller 8-site dataset) — full detail in
`GI_Research_Paper.md` Sections 3.6–3.7, 4.5–4.6, and 7.

This project makes "industrial legacy" spatially and statistically measurable rather than treating
it as a qualitative narrative concept, testing digitized historical geography directly against a
network-based measure of present-day urban accessibility — now tested across two cities and three
accessibility thresholds.

**Keywords**: path dependency, 15-minute city, urban accessibility, historical GIS, network
analysis, post-industrial geography, Ruhr Valley, multi-city replication, robustness analysis,
Local Moran's I, spatial statistics

---

**Author / affiliation fields**: unchanged (Sakshi D. Maske, Independent Geospatial Researcher).

**License**: unchanged (CC BY 4.0).

**Related identifiers**: when Zenodo asks whether this is a new version of the existing record,
select "is a new version of" and link the existing DOI — this keeps both versions linked under one
concept DOI, which is the goal (citations to the concept DOI always resolve to the latest version;
citations to `zenodo.21761320` specifically will keep pointing at v1.0.0, which is correct scholarly
behavior).
