import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, PALETTE

apply_custom_style()


def render_card(content_html):
    st.markdown(f"""
        <div style="background: #B4D5D6; border-radius: 10px; padding: 20px; margin-bottom: 16px;">
            {content_html}
        </div>
    """, unsafe_allow_html=True)


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
    """)
with col2:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.95rem; margin:0 0 10px 0;">Modern Data</p>
        <p style="color:#333333; font-weight:600; font-size:0.9rem; line-height:1.7; margin:0;">
            Street network — OpenStreetMap via OSMnx<br>
            Essential services — OpenStreetMap points of interest<br>
            69,393 nodes, 169,668 edges, 786 services
        </p>
    """)

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>The Validation Journey</h3>", unsafe_allow_html=True)

with st.expander("**Two Historical Layers, Deliberately Kept Separate**"):
    st.markdown("""
    A "Zeche" (mine) and a "Siedlung" (settlement) are structurally distinct feature types — an 
    extraction site versus residential worker housing. They were compiled as two independent 
    datasets by design. A proposed steelworker colony (Stahlhausen) was explicitly excluded from 
    the Zechensiedlungen dataset during review, since it belongs to a different industrial category.
    """)

with st.expander("**A Reversed Finding, Investigated Rather Than Accepted**"):
    st.markdown("""
    The initial statistical test found historical industrial sites correlated with BETTER 
    present-day accessibility — the opposite of the original hypothesis. The most obvious confound 
    (city-center clustering) was tested directly. Correlation between distance-to-historical-site 
    and distance-to-city-center was low (r=0.063), and a logistic regression confirmed the 
    historical-site effect remained significant even after controlling for city-center proximity.
    """)

with st.expander("**A Visual Anomaly That Turned Out to Be Genuine Geography**"):
    st.markdown("""
    Independent visual verification flagged an apparent "12 vs 13 mines" discrepancy. Rather than 
    assuming a data error, exact Haversine distances were calculated: Mansfeld and Heinrich Gustav 
    mines are genuinely 1.75km apart, and Kolonie Hannover and Am Rübenkamp colonies are genuinely 
    0.33km apart — both close enough to visually merge at full-city map scale.
    """)

with st.expander("**A CRS Mismatch That Collapsed an Entire Map**"):
    st.markdown("""
    An early overlay map rendered as a single visible dot rather than a full city view, traced to 
    a coordinate reference system mismatch: the accessibility layer had been saved in a metric UTM 
    projection while the historical layers remained in standard latitude/longitude. Reprojecting 
    all layers to a shared CRS resolved it.
    """)

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>Honest Limitations</h3>", unsafe_allow_html=True)

render_card("""
    <p style="color:#111111; font-weight:700; font-size:1.05rem; line-height:1.8; margin:0;">
        This project relies on point-based historical site locations rather than full manual 
        boundary digitization. The worker-colony dataset (4 sites) is smaller than the coal-mine 
        dataset (13 sites), somewhat limiting statistical power for colony-specific analysis. The 
        15-minute accessibility model treats all essential-service categories as equally weighted.
    </p>
""")

st.markdown("---")

render_card("""
    <div style="text-align:center;">
        <p style="color:#333333; font-weight:700; text-transform:uppercase; letter-spacing:2px; font-size:0.85rem; margin:0 0 10px 0;">GitHub Repository</p>
        <p style="color:#111111; font-weight:700; font-size:1rem; margin:0;">
            <a href="https://github.com/sakshimaske303-commits/GHOST_INFRASTRUCTURE" target="_blank" style="color:#111111;">github.com/sakshimaske303-commits/GHOST_INFRASTRUCTURE</a>
        </p>
    </div>
""")

st.markdown("---")

render_card("""
    <div style="text-align:center;">
        <p style="color:#333333; font-weight:700; text-transform:uppercase; letter-spacing:2px; font-size:0.85rem; margin:0 0 10px 0;">Project Author</p>
        <p style="color:#111111; font-weight:900; font-size:2rem; margin:0 0 8px 0;">SAKSHI D. MASKE</p>
        <p style="color:#333333; font-weight:700; font-size:1rem; margin:0;">Independent Geospatial Researcher</p>
    </div>
""")

st.markdown("---")
st.markdown(
    "<p class='caption-text' style='text-align:center;'>GHOST INFRASTRUCTURE — A Historical GIS and Spatial Statistics Research Project</p>",
    unsafe_allow_html=True,
)