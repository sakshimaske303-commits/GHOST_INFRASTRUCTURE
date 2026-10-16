# GHOST INFRASTRUCTURE: Defensibility Plan and Stop Line

*Created 16 Oct 2026 after the full forensic review. This file is the single source of truth for what still needs doing, who does it, and **when we stop**. If a task is not listed here, it does not get done in this version.*

---

## 0. The one rule that prevents an infinite loop

> **The analysis specification below is fixed in advance. We run it once, freeze the numbers, write the paper once from those numbers, and stop.**
> The direction of the result does not trigger more work. If the "legacy" effect disappears after the new controls, **we report that**. We do not keep adding variables, cities or tests until it comes back.
> A new idea after the freeze goes into *Future Work*, not into the analysis.

The only things allowed to reopen work after the freeze are:
1. a **bug** (the code does not do what the text says), or
2. a **factual error** (a wrong number, place or date).

"Another robustness check would be nice" is **not** a reason to reopen.

---

## 1. Honest expectation (read before starting)

The forensic review found that 17 *random* points placed in Bochum's built-up area reproduce the "reversed" effect 98% of the time. The controls below will probably show that most of the effect is general urban form, not coal.

**That is fine, and it is still a complete, defensible paper.** The likely final story is:

> *"An apparent industrial-legacy signal in 15-minute accessibility largely reflects general urban form. A null-model test with population-weighted, Earth-observation-based controls shows how such legacy claims should be tested."*

Committees and reviewers respect a well-tested negative or partial result far more than an over-claimed positive one. The pre-agreed wording for each possible outcome is in §5.

---

## 2. Phases and status

| Phase | What | Who | Status |
|---|---|---|---|
| 1 | Factual corrections (wrong numbers, captions, stale dashboard values, broken output paths) | Claude | ✅ done 16 Oct (PDFs and figure images are regenerated only in Phase 5) |
| 2 | New analyses that need **no new data**: null model, urban-form controls, service-definition sensitivity | Claude (Sakshi re-runs once to confirm) | ✅ run 16 Oct, results frozen in `outputs/robustness/`; confirmed by Sakshi's own run, 16 Oct (S6) |
| 3 | New analyses that need **downloaded data**: population weighting (Zensus 2022) and settlement age (GHSL, Earth observation) | Sakshi downloads → Claude runs | D ✅ and E ✅ run 16 Oct (frozen) |
| 4 | **One** rewrite of the paper, then sync of the executive summary, README, dashboard, CITATION and dev log; verified literature | Claude drafts → Sakshi reviews voice | ✅ done 16 Oct; waiting for Sakshi's voice review (S7) |
| 5 | Regenerate PDFs once, commit, tag `v2.0`, **STOP** | Sakshi | ☐ |

---

## 3. Fix list

### Phase 1: factual corrections (Claude)
- [x] 786 → **248** point services actually used (786 = all OSM features downloaded; 538 were polygons and were dropped). State which categories survive: no hospitals and no parks in the point set. Essen: 1,410 → 366.
- [x] Essen is ~15 km **west** of Bochum, not northeast (paper, dev log, dashboard).
- [x] Fig. 8 / Fig. S3 caption: left and right panels were swapped.
- [x] "Grows stronger at every threshold" → d *rises as the threshold widens* (0.413 / 0.589 / 0.661). The 10-min value is smaller than the 15-min value.
- [x] Bootstrap description: the walk network is **one connected component**. Blocks are small because block growth is hemmed in by already-assigned nodes. Median block size = 1.
- [x] City-centre point: it is at 7.2162 E, 51.4818 N, ~570 m NW of the Hauptbahnhof (Rathaus/Innenstadt area). Checked with the true Hbf: r = 0.022, conclusion unchanged.
- [x] Centre odds 3.0% → 2.9%. Essen t = 24.731 → 24.732.
- [x] Essen "two explanations were tested" → explanation 1 is contradicted by the data (Essen's sites average 5.65 km from the centre vs 4.63 km for all nodes). Remove the Krupp (steel) argument.
- [x] Fig. 2 caption: it is not a "19th-century map". It is point locations on today's boundary.
- [x] Disclose that distance to sites and to the centre is straight-line (Euclidean).
- [x] Dashboard: stale bootstrap CI [247.24, 873.73] → [199.90, 885.16]; remove "~500 nodes each"; 786 → 248; northeast → west; "Two competing explanations tested" badge.
- [x] Dashboard *Theoretical Foundations*: stop displaying `imgg1.png`; label the subsidence mechanism as an untested hypothesis.
- [x] Code output paths: scripts must read and write `outputs/` consistently so the pipeline chains.
- [x] Code comments that call the centre point "Hauptbahnhof".
- [x] Essen CSVs: add the 2 missing sites (the GeoPackages already have all 8).
- [x] Dev log: add a correction entry; mark corrected statements in earlier entries.

### Phase 2: analyses with existing data (Claude)
Specification fixed here. Do not change it after running.
- [x] **A. Null model.** 1,000 random sets of *n* sites (17 Bochum, 8 Essen), drawn from street-network nodes (the built-up-area proxy), seed 42. Report the percentile of the observed Cohen's d, and of the logit coefficient for historical distance controlling for centre distance.
- [x] **B. Urban-form controls.** Logit of access on historical distance + centre distance + distance to city boundary + log(street nodes within 500 m), with the same null model applied to this coefficient (added to the spec before the first run). Also a 2 km grid-cluster bootstrap (999 resamples) of the distance difference, leave-one-site-out d, and local coverage within 750 m of each site.
- [x] **C. Service definition.** Re-run accessibility including polygon services (centroid of each polygon in EPSG:32632). Report coverage, t, d and the null-model percentile for points-only vs all features.

**Phase 2 results (frozen 16 Oct 2026; script `robustness_v2.py`, output `outputs/robustness/robustness_results.json`, figure `outputs/robustness/null_model.png`):**

| | Bochum | Essen |
|---|---|---|
| A. Observed d / mean d of 1,000 random site sets | 0.589 / 0.430 | 0.338 / 0.589 |
| A. Share of random sets with d ≥ observed | **22.5%** | **83.1%** |
| A. Share of random sets with coefficient (given centre) ≤ observed | 34.4% | 82.9% |
| B. Historical coefficient, full urban-form model | −0.000157 (v1: −0.000476) | −0.0000628 (v1: +0.000114) |
| B. Share of random sets with full-model coefficient ≤ observed | 25.4% | 35.6% |
| B. 2 km grid-bootstrap 95% CI of distance difference | [197, 907] m | [−2, 1147] m |
| B. Leave-one-site-out d | 0.369 – 0.697 | 0.011 – 0.450 |
| C. All services (incl. polygons): coverage / low-access nodes | 96.7% / 2,271 | 97.7% / 1,649 |
| C. All services: observed d / share of random sets with d ≥ observed | 1.499 / **4.3%** | 0.532 / **77.7%** |

*Verification (S6):* Sakshi's own run (real geopandas/shapely/statsmodels) reproduced every number. The only difference is Essen all-services (1,649 vs 1,652 low nodes in Claude's stand-in test), caused by polygon-centroid handling; the percentile is identical. The JSON files from Sakshi's run are the official ones.

**Reading (the §5 rule applied, no extra tests):** with the v1 points-only outcome, real mining sites are **not** distinguishable from random built-up locations in either city. With the more complete service definition, Bochum's sites **do** beat 95.7% of random sets, while Essen's do not. This is a *mixed* result. It will be reported as mixed. Phase 3 decides whether the Bochum all-services signal survives population weighting; nothing else gets added to "resolve" it.

**Decision rule fixed now, before Phase 3:** the paper may make the positive §5 claim for a city only if (i) the points-only and all-services definitions agree, **and** (ii) the population-weighted analysis D agrees. Otherwise the §5 "mixed" or "explained by urban form" wording applies.

### Phase 3: analyses with new data (Sakshi downloads, Claude runs)
- [x] **D. Population weighting** (Zensus 2022, 100 m grid). The unit becomes *people*, not street nodes; footpaths through forests with nobody living there drop out. Fixed specification:
  - Units: Zensus 100 m cells with population > 0 whose centre lies inside the city boundary. A cell's access = access of the nearest street node to its centre. Both service definitions (points only, all services).
  - Outcome: share of **residents** without 15-min access (population-weighted).
  - Tests: population-weighted Cohen's d of distance to nearest site; null model with 1,000 random site sets drawn uniformly from populated cells (seed 42); population-weighted logit of access on historical distance + centre distance + log(residents within 500 m), with the same null model for its historical coefficient.
**Phase 3D results (frozen 16 Oct 2026; script `robustness_v2_population.py`, output `outputs/robustness/population_results.json`, figure `outputs/robustness/null_model_population.png`).** Zensus 2022 cells inside the boundary: Bochum 6,924 cells / 353,661 residents; Essen 9,755 cells / 571,031 residents.

| Population-weighted | Bochum, points only | Bochum, all services | Essen, points only | Essen, all services |
|---|---|---|---|---|
| Residents without 15-min access | 11.7% | **2.1%** | 5.6% | **0.7%** |
| Weighted d (real sites) / mean of random sets | 0.404 / 0.299 | 0.994 / 0.527 | 0.392 / 0.327 | 0.861 / 0.694 |
| Share of random sets with d ≥ real | 35.2% | 10.6% | 43.0% | 41.3% |
| Share of random sets with coefficient ≤ real (controls: centre, residents within 500 m) | 58.6% | 23.6% | 35.7% | 34.2% |

**Reading under the decision rule (fixed before this run):** for residents, real mining sites are not distinguishable from random populated locations in any of the 4 cases. None reaches the 95% threshold. The Bochum all-services node-level signal from Phase 2 (95.7%) does **not** survive population weighting (89.4%). So, for **both cities**, the §5 wording "*the apparent legacy signal is explained by general urban form*" applies. A second, robust descriptive finding: with all services counted, only about 2% (Bochum) and 0.7% (Essen) of residents lack 15-minute access to any essential service; most "low-access" street nodes are places where few or no people live.

Data note for the paper: Zensus 2022 (reference date 15 May 2022) is licensed dl-de/by-2-0 and must be attributed. Values are slightly perturbed for confidentiality (cell-key method) and empty cells are not published.

- [x] **E. Settlement age** (GHSL GHS-BUILT-S, satellite-derived, epochs 1975 and 2020). This tests the paper's own policy claim that gaps sit in newer neighbourhoods. It is the project's Earth-observation component. Fixed specification:
  - Each populated Zensus cell takes the GHSL built-up surface of the GHSL cell containing its centre. A cell is "post-1975" if built-up surface in 1975 < 50% of its 2020 value; otherwise "pre-1975".
  - Report the share of residents without access in pre- vs post-1975 cells, and add the post-1975 flag to the D logit. Both service definitions. Report whatever comes out.

**Phase 3E results (frozen 16 Oct 2026; script `robustness_v2_settlement_age.py`, output `outputs/robustness/settlement_age_results.json`).** GHSL tile R3_C19, epochs 1975 and 2020. Cells with no 2020 built-up surface excluded: Bochum 50 cells / 418 residents; Essen 69 / 384. Residents living in post-1975 built-up cells: Bochum 11.8%, Essen 12.9%.

| Residents without 15-min access | Bochum, points only | Bochum, all services | Essen, points only | Essen, all services |
|---|---|---|---|---|
| in pre-1975 cells | 10.4% | 1.7% | 4.4% | 0.35% |
| in post-1975 cells | **22.0%** | **5.1%** | **14.2%** | **2.9%** |
| Odds ratio of access for post-1975 (controls: distance to sites, centre, residents within 500 m) | 0.94 | 0.87 | 0.90 | 0.38 |

**Reading:** in all 4 cases, residents of areas first built up after 1975 are 2–8 times more likely to lack 15-minute access, and the adjusted odds ratio is below 1 in all 4. This **supports** the paper's policy claim, which until now had no evidence behind it. It is reported as a consistent descriptive association. The p-values from this frequency-weighted model are over-confident (every resident counts as an observation, and there is spatial autocorrelation), so the paper uses the rates and the consistent direction, not the p-values. No null model was specified for E, and none will be added.

**All analyses are now frozen. From here, only Phases 4–5 remain: no new analyses.**

### Phase 4: one rewrite (Claude drafts, Sakshi reviews)
- [x] One research question + H0/H1 in the introduction. Title and conclusion match a cross-sectional design (no causal "boost", "persistence" or "legacy" claims beyond the evidence).
- [x] Results reported in the order A → B → C → D → E. Bochum is primary; Essen is reported with the same design, honestly (a non-replication if that is what it is).
- [x] Local Moran's I is removed as "independent corroboration" (explained in paper Section 9; no LISA map in v2).
- [x] Literature: 26 references, each checked to exist (Crossref or the publisher/repository record), all cited in the text. One unverifiable candidate (Hospers 2004) was left out. `MANUSCRIPT.md` was removed by Sakshi; only `GI_Research_Paper.md` remains as the master. A journal version is made from it later, when a journal is chosen.
- [x] Executive summary, README, dashboard, CITATION abstract and dev log synced to the final paper, **after** the paper is final, never before.
- [x] Maps get a scale bar, north arrow and "% of street nodes" legends (`maps/map_furniture.py`). A locator inset was dropped to keep the scope fixed. Images are regenerated in Phase 5.

### Phase 5: close (Sakshi)
Run from the repository root, in this order:
- [ ] Delete `outputs/plots/imgg1.png` (decision S5).
- [ ] `git rm --cached data/boundaries/bochum_city.gpkg data/boundaries/essen_city.gpkg` (the files stay on your disk; they just stop being published).
- [ ] Regenerate the map images: `python maps/map1_ghost_infrastructure.py`, `python maps/map3_historical_geography.py`, `python maps/map4_study_area.py`, and the three `_essen` versions.
- [ ] `python plot_settlement_age.py` (Figure 6).
- [ ] Read `GI_Research_Paper.md` once for your own voice (S7). Wording only: no new analyses, no new claims.
- [ ] Regenerate the PDFs once with VS Code from the final `.md` files: `GI_Research_Paper.md`, `GI_Executive_Summary.md`, `GI_Development_Log.md`. Copy the three PDFs into `dashboard/static/`.
- [ ] Journal-only files (`COVER_LETTER.md`, `TITLE_PAGE.md` text, `SUPPLEMENTARY_MATERIAL.pdf`) still describe v1. They are updated only when a journal is chosen; this is outside v2.0.
- [ ] `git commit`, tag `v2.0`. Update DOIs / Zenodo / EarthArXiv and the `date-released` in `CITATION.cff` (deliberately left until here).
- [ ] **STOP.**

---

## 4. Needs Sakshi's input or decision

| # | What | Why Claude can't do it |
|---|---|---|
| S1 ✅ | Download the **Zensus 2022 population 100 m grid** CSV (zensus2022.de → Ergebnisse → Gitterzellen → "Bevölkerungszahl", 100 m) and put the CSV in `data/population/` | Claude's workspace cannot reach German government sites |
| S2 | Download **GHSL GHS-BUILT-S R2023A**, epochs **1975** and **2020**, 100 m (or 3 arc-sec), the tile covering the Ruhr, from the JRC GHSL data portal. Put the GeoTIFFs in `data/ghsl/` | Same |
| S3 ✅ | *(licence)* Decide whether to switch to **MIT for code + CC BY 4.0 for text/figures + an ODbL notice for OSM-derived data**, and whether to replace the GADM boundaries (whose licence forbids redistribution) with **BKG VG250** (dl-de/by-2-0). If yes, download VG250 Gemeinden into `data/boundaries/` | Licence choice is the author's legal decision |
| S4 ✅ | Remove your home address and phone number from the public `TITLE_PAGE.md`? | Personal decision |
| S5 ✅ | `imgg1.png`: Claude has stopped the dashboard from showing it. Delete the file or keep it? If it was AI-generated, the AI declaration must say so | Only you know how it was made |
| S6 ✅ | From the repository root run `python robustness_v2.py` (about 15–30 min) in your normal Python environment, and send Claude the summary printed at the end. It should match the Phase 2 results table above (the last digit may differ slightly). The same goes for the Phase 3 script later | Claude's workspace has no geopandas/osmnx/statsmodels; it was tested with stand-ins |
| S7 | Review the Phase 4 draft for your own voice | It is your paper |
| S8 | Regenerate the PDFs, commit, push, tag | Claude does not push to your GitHub |

---

## 5. Pre-agreed interpretation (decided **before** seeing Phase 2–3 results)

| Result | What the paper is allowed to say |
|---|---|
| Observed effect beats ≥95% of random site sets **and** survives the population and urban-form controls | "The mining-settlement pattern is associated with better access **beyond** general urban form" (association, not causation) |
| Effect is within the random-site range **or** vanishes under the controls | "The apparent legacy signal is explained by general urban form; random-site null models are needed before claiming industrial legacy." This is a methodological contribution |
| Mixed (e.g., survives in Bochum but not Essen, or for nodes but not people) | Report exactly that, city by city. No extra tests to "resolve" it; the resolution goes to Future Work |
| Settlement age (E): low access concentrated in post-1975 built-up areas, or not | Report it either way. It confirms or refutes the policy claim |

---

## 6. Explicitly OUT of scope for this version (future work, not limitations to "fix")

Do **not** start any of these before `v2.0` is tagged:
- a third city (Dortmund, Gelsenkirchen …) or expanding Essen beyond its 8 sites
- georeferencing historical topographic maps, or digitizing historical rail/roads
- GWR or other spatially varying models; time series of accessibility
- more bootstrap block sizes, more LISA permutation counts, network-distance LISA
- weighted service indices, income/car-ownership data
- dashboard visual polish beyond correcting content

These remain listed as Future Work and as acknowledged limitations. A paper that names its limits clearly is complete; it does not need zero limitations.

---

## 7. Definition of done (all must be true, then stop)

1. Every Phase 1 item is ticked.
2. Analyses A–E have each been run **once** with the specification above, and the results are saved in `outputs/robustness/`.
3. Every number in the paper, executive summary, README and dashboard traces to a file in `outputs/`.
4. The paper has one RQ, and its conclusion answers that RQ using the §5 wording.
5. PDFs regenerated, repository tagged `v2.0`.

**When these five are true, the research is finished for this application.**
