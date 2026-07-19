import streamlit as st
import streamlit.components.v1 as components
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, PALETTE

apply_custom_style()


def render_card(content_html, height=200):
    components.html(f"""
        <div style="background: #B4D5D6; border-radius: 10px; padding: 24px;
                    font-family: 'Inter', sans-serif; box-sizing: border-box; height: {height-48}px;">
            {content_html}
        </div>
    """, height=height)


st.markdown("<h1 style='text-align: center;'>📖 METHODOLOGY & DATA</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center; color: #FFFFFF; font-size: 1.5rem;'>"
    "Full Transparency and Reproducibility</h3>",
    unsafe_allow_html=True,
)
st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>Data Sources</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.95rem; margin:0 0 10px 0;">Historical Data</p>
        <p style="color:#333333; font-weight:600; font-size:0.9rem; line-height:1.7; margin:0;">
            Coal mines — Mindat.org (compiled record by record)<br>
            Worker colonies — Wikipedia, Route Industriekultur, ruhr-bauten.de<br>
            City boundary — GADM v4.1
        </p>
    """, height=240)
with col2:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.95rem; margin:0 0 10px 0;">Modern Data</p>
        <p style="color:#333333; font-weight:600; font-size:0.9rem; line-height:1.7; margin:0;">
            Street network — OpenStreetMap via OSMnx<br>
            Essential services — OpenStreetMap points of interest<br>
            69,393 nodes, 169,668 edges, 786 services
        </p>
    """, height=240)

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>The Validation Journey</h3>", unsafe_allow_html=True)

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

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>Honest Limitations</h3>", unsafe_allow_html=True)

render_card("""
    <p style="color:#111111; font-weight:700; font-size:1.05rem; line-height:1.8; margin:0;">
        This project relies on point-based historical site locations rather than full manual 
        boundary digitization of mine and colony extents — a deliberate scope decision given 
        project timeline constraints, disclosed transparently rather than presented as complete. 
        The 15-minute accessibility model treats all essential-service categories as equally 
        weighted, which does not capture genuine differences in how urgently each service type 
        matters to daily life.
    </p>
""", height=240)

st.markdown("---")

render_card("""
    <div style="text-align:center;">
        <p style="color:#333333; font-weight:700; text-transform:uppercase; letter-spacing:2px; font-size:0.85rem; margin:0 0 10px 0;">GitHub Repository</p>
        <p style="color:#111111; font-weight:700; font-size:1rem; margin:0;">
            <a href="https://github.com/sakshimaske303-commits/GHOST_INFRASTRUCTURE" target="_blank" style="color:#111111;">github.com/sakshimaske303-commits/GHOST-INFRASTRUCTURE</a>
        </p>
    </div>
""", height=140)

st.markdown("---")

render_card("""
    <div style="text-align:center;">
        <p style="color:#333333; font-weight:700; text-transform:uppercase; letter-spacing:2px; font-size:0.85rem; margin:0 0 10px 0;">Project Author</p>
        <p style="color:#111111; font-weight:900; font-size:2rem; margin:0 0 8px 0;">SAKSHI D. MASKE</p>
        <p style="color:#333333; font-weight:700; font-size:1rem; margin:0;">Independent Geospatial Researcher</p>
    </div>
""", height=230)

st.markdown("---")
st.markdown(
    "<p class='caption-text' style='text-align:center;'>GHOST INFRASTRUCTURE — A Historical GIS and Spatial Statistics Research Project</p>",
    unsafe_allow_html=True,
)