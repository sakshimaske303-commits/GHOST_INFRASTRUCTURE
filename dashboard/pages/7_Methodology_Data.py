import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, page_header, footer_caption, card, kicker, card_body

apply_custom_style()

page_header("📖", "METHODOLOGY & DATA", "Full Transparency and Reproducibility")
st.markdown("---")

# ============================================================
# PROOF-OF-WORK POPOVERS — tiny, pulsing "📸" buttons next to the
# exact data source / finding they back up. Click to reveal the
# screenshot inline; nothing pushes the page layout around. Drop
# the PNGs into outputs/proof_screenshots/ (see filenames below)
# and these activate automatically — until then each falls back to
# a quiet "not added yet" note instead of breaking the page.
# ============================================================
st.markdown(f"""
<style>
    div[data-testid="stPopover"] button {{
        animation: proof-blink 1.8s ease-in-out infinite;
        border: 3px solid #FFF2BA !important;
        width: 32px !important;
        height: 32px !important;
        border-radius: 50% !important;
        padding: 0 !important;
        min-height: unset !important;
        min-width: unset !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }}
    div[data-testid="stPopover"] button p {{
        margin: 0 !important;
        font-size: 0.95rem !important;
        line-height: 1 !important;
    }}
    @keyframes proof-blink {{
        0%, 100% {{ box-shadow: 0 0 0px rgba(255, 242, 186, 0); }}
        50% {{ box-shadow: 0 0 12px rgba(255, 242, 186, 0.85); }}
    }}
</style>
""", unsafe_allow_html=True)

PROOF_DIR = os.path.join(PROJECT_ROOT, "outputs", "proof_screenshots")

def proof_popover(filename, caption):
    path = os.path.join(PROOF_DIR, filename)
    with st.popover("📸"):
        if os.path.exists(path):
            st.image(path, caption=caption, use_container_width=True)
        else:
            st.caption(f"Screenshot not added yet — save it as `outputs/proof_screenshots/{filename}`.")

st.markdown("<h3>Data Sources</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    card(
        kicker("Historical Data")
        + card_body(
            "Coal mines — Mindat.org (compiled record by record)<br>"
            "Worker colonies — Wikipedia, Route Industriekultur, ruhr-bauten.de<br>"
            "City boundary — GADM v4.1"
        )
    )
with col2:
    card(
        kicker("Modern Data")
        + card_body(
            "Street network — OpenStreetMap via OSMnx<br>"
            "Essential services — OpenStreetMap points of interest<br>"
            "Bochum: 69,393 nodes, 169,668 edges, 786 services<br>"
            "Essen: 72,027 nodes, 188,198 edges, 366 services"
        )
    )
    mc1, mc2 = st.columns([0.87, 0.13])
    with mc2:
        proof_popover("01_bochum_accessibility_qgis.png", "Bochum's 15-minute accessibility classification (green = within 15min, red = low-accessibility) with essential-services points, styled in QGIS — the modern-day baseline the historical industrial sites are compared against.")

st.markdown("---")

st.markdown("<h3>Essen (Multi-City Replication) Data Sources</h3>", unsafe_allow_html=True)
card(card_body(
    "Coal mines and worker colonies for the Essen replication were digitized from "
    "<strong>KuLaDig</strong> (Kultur.Landschaft.Digital, North Rhine-Westphalia's state "
    "cultural-heritage GIS database) and German Wikipedia — Mindat.org, the source used for Bochum, "
    "returned a 403 error on automated fetch for Essen entries, and Wikidata's live API was "
    "unavailable in this session's environment, so KuLaDig was used instead once it proved reliably "
    "fetchable and precise (WGS84 degree-minute-second coordinates for surviving heritage-listed "
    "structures). All 8 Essen coordinates were independently verified to fall inside Essen's official "
    "administrative boundary (GADM v4.1) before use. Full detail on the Robustness page and in "
    "Research_Paper.md Section 3.7.",
    large=True,
))

st.markdown("---")

st.markdown("<h3>The Validation Journey</h3>", unsafe_allow_html=True)

with st.expander("**Two Historical Layers, Deliberately Kept Separate**"):
    st.markdown("""
    A "Zeche" (mine) and a "Siedlung" (settlement) are structurally distinct feature types — an
    extraction site versus residential worker housing. They were compiled as two independent
    datasets by design. A proposed steelworker colony (Stahlhausen, linked to Bochumer Verein
    rather than any coal mine) was explicitly excluded from the Zechensiedlungen dataset during
    review, since it belongs to a different industrial category.
    """)

rfa, rfb = st.columns([0.94, 0.06])
with rfa:
    with st.expander("**A Reversed Finding, Investigated Rather Than Accepted**"):
        st.markdown("""
        The initial statistical test found historical industrial sites correlated with BETTER
        present-day accessibility — the opposite of the original hypothesis. Rather than reporting
        this at face value, the most obvious confound (city-center clustering) was tested directly.
        Correlation between distance-to-historical-site and distance-to-city-center was low (r=0.063),
        and a logistic regression confirmed the historical-site effect remained significant even after
        controlling for city-center proximity — the reversed finding is genuine, not a confound artifact.
        """)
with rfb:
    st.markdown("<div style='margin-top: 0.5rem;'></div>", unsafe_allow_html=True)
    proof_popover("02_test_confound_vscode.png", "test_confound.py open in VS Code — the city-center-proximity correlation and logistic regression that confirmed the reversed finding wasn't a confound artifact.")

vda, vdb = st.columns([0.94, 0.06])
with vda:
    with st.expander("**A Visual Anomaly That Turned Out to Be Genuine Geography**"):
        st.markdown("""
        Independent visual verification flagged an apparent "12 vs 13 mines" discrepancy on two
        separate map outputs. Rather than assuming a data error, the underlying coordinates were
        directly re-verified twice, confirming all 13 mines were genuinely present — two mines
        (Mansfeld and Heinrich Gustav) are simply located close enough (about 1.7km apart) to visually
        merge into a single marker at full-city map scale.
        """)
with vdb:
    st.markdown("<div style='margin-top: 0.5rem;'></div>", unsafe_allow_html=True)
    proof_popover("03_verify_distances_vscode.png", "verify_distances.py open in VS Code — the haversine re-check confirming Mansfeld and Heinrich Gustav are ~1.7km apart, not duplicate or missing points.")

cra, crb = st.columns([0.94, 0.06])
with cra:
    with st.expander("**A CRS Mismatch That Collapsed an Entire Map**"):
        st.markdown("""
        An early overlay map rendered as a single visible dot rather than a full city view. This was
        traced to a coordinate reference system mismatch: the accessibility layer had been saved in a
        metric UTM projection (EPSG:32632) for earlier distance calculations, while the historical
        layers remained in standard latitude/longitude (EPSG:4326). Reprojecting all layers to a shared
        CRS before plotting resolved it.
        """)
with crb:
    st.markdown("<div style='margin-top: 0.5rem;'></div>", unsafe_allow_html=True)
    proof_popover("04_map1_crs_fix_vscode.png", "map1_ghost_infrastructure.py open in VS Code — the '.to_crs(\"EPSG:4326\")' fix that reprojects every layer to a shared CRS before plotting, resolving the single-dot map.")

lca, lcb = st.columns([0.94, 0.06])
with lca:
    with st.expander("**Closing the Gap Between the Stated Objectives and the Executed Analysis**"):
        st.markdown("""
        This project's original Objectives named Local Moran's I / hot-spot analysis as the method for
        testing whether low-accessibility zones are spatially clustered. The Welch's t-test and logistic
        regression above test a related but distinct question — whether *distance* to historical sites
        differs between accessibility groups — not spatial *clustering* of accessibility itself. A
        Local Moran's I analysis (KNN k=8 spatial weights, 99 permutations, `libpysal`/`esda`) was run
        directly to close this gap: 97.1% of low-accessibility nodes fall inside a statistically
        significant Low-Low ("cold-spot") cluster, independently corroborating the reversed relationship.
        See "The Finding" page for the full cluster map, and `spatial_clustering_lisa.py` in the
        repository root for the reproducible script.
        """)
with lcb:
    st.markdown("<div style='margin-top: 0.5rem;'></div>", unsafe_allow_html=True)
    proof_popover("05_spatial_clustering_lisa_vscode.png", "spatial_clustering_lisa.py open in VS Code — the Local Moran's I script that closes the gap between the stated Objectives and the executed analysis.")

st.markdown("---")

st.markdown("<h3>Honest Limitations</h3>", unsafe_allow_html=True)

card(card_body(
    "This project relies on point-based historical site locations rather than full manual "
    "boundary digitization of mine and colony extents — a deliberate scope decision given "
    "project timeline constraints, disclosed transparently rather than presented as complete. "
    "The 13 mines and 4 colonies digitized for Bochum are the major, well-documented industrial-era "
    "sites, not the full historical mining register (which includes several hundred smaller "
    "operations spanning multiple centuries and is not a fair comparison set). Industrial-era "
    "rail and road infrastructure was part of the original scope but was not digitized this "
    "phase. The 15-minute accessibility model treats all essential-service categories as equally "
    "weighted, and socioeconomic confounders (income, age, tenure) are not controlled for — "
    "the reported relationships are descriptive spatial associations, not fully adjusted causal "
    "estimates. The Essen replication's 8-site dataset is smaller, relative to Essen's own much "
    "larger historical mining register, than the Bochum dataset is to Bochum's — and this appears "
    "to materially affect the confound-independence result specifically (see the Robustness page). "
    "Full detail in the Research Paper's Limitations and Future Work sections.",
    large=True,
))

st.markdown("---")
footer_caption("GHOST INFRASTRUCTURE — A Historical GIS and Spatial Statistics Research Project")
