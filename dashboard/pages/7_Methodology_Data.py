import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, page_header, footer_caption, card, kicker, card_body

apply_custom_style()

page_header("📖", "METHODOLOGY & DATA", "Full Transparency and Reproducibility")
st.markdown("---")

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
            "69,393 nodes, 169,668 edges, 786 services"
        )
    )

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

with st.expander("**A Reversed Finding, Investigated Rather Than Accepted**"):
    st.markdown("""
    The initial statistical test found historical industrial sites correlated with BETTER
    present-day accessibility — the opposite of the original hypothesis. Rather than reporting
    this at face value, the most obvious confound (city-center clustering) was tested directly.
    Correlation between distance-to-historical-site and distance-to-city-center was low (r=0.063),
    and a logistic regression confirmed the historical-site effect remained significant even after
    controlling for city-center proximity — the reversed finding is genuine, not a confound artifact.
    """)

with st.expander("**A Visual Anomaly That Turned Out to Be Genuine Geography**"):
    st.markdown("""
    Independent visual verification flagged an apparent "12 vs 13 mines" discrepancy on two
    separate map outputs. Rather than assuming a data error, the underlying coordinates were
    directly re-verified twice, confirming all 13 mines were genuinely present — two mines
    (Mansfeld and Heinrich Gustav) are simply located close enough (about 1.7km apart) to visually
    merge into a single marker at full-city map scale.
    """)

with st.expander("**A CRS Mismatch That Collapsed an Entire Map**"):
    st.markdown("""
    An early overlay map rendered as a single visible dot rather than a full city view. This was
    traced to a coordinate reference system mismatch: the accessibility layer had been saved in a
    metric UTM projection (EPSG:32632) for earlier distance calculations, while the historical
    layers remained in standard latitude/longitude (EPSG:4326). Reprojecting all layers to a shared
    CRS before plotting resolved it.
    """)

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

st.markdown("---")

st.markdown("<h3>Honest Limitations</h3>", unsafe_allow_html=True)

card(card_body(
    "This project relies on point-based historical site locations rather than full manual "
    "boundary digitization of mine and colony extents — a deliberate scope decision given "
    "project timeline constraints, disclosed transparently rather than presented as complete. "
    "The 13 mines and 4 colonies digitized here are the major, well-documented industrial-era "
    "sites, not the full historical mining register (which includes several hundred smaller "
    "operations spanning multiple centuries and is not a fair comparison set). Industrial-era "
    "rail and road infrastructure was part of the original scope but was not digitized this "
    "phase. The 15-minute accessibility model treats all essential-service categories as equally "
    "weighted, and socioeconomic confounders (income, age, tenure) are not controlled for — "
    "the reported relationships are descriptive spatial associations, not fully adjusted causal "
    "estimates. Full detail in the Research Paper's Limitations and Future Work sections.",
    large=True,
))

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    card(f"""
        <div style="text-align:center;">
            {kicker("GitHub Repository")}
            <p style="font-weight:700; font-size:0.95rem; margin:0;">
                <a href="https://github.com/sakshimaske303-commits/GHOST_INFRASTRUCTURE" target="_blank" style="color:#0F3C65;">github.com/sakshimaske303-commits/GHOST_INFRASTRUCTURE</a>
            </p>
        </div>
    """)
with col2:
    card(f"""
        <div style="text-align:center;">
            {kicker("Project Author")}
            <p style="font-family:'Bitter',serif; font-weight:900; font-size:1.7rem; margin:0 0 4px 0;">SAKSHI D. MASKE</p>
            <p style="font-weight:700; font-size:0.9rem; margin:0;">Independent Geospatial Researcher</p>
        </div>
    """)

st.markdown("---")
footer_caption("GHOST INFRASTRUCTURE — A Historical GIS and Spatial Statistics Research Project")
