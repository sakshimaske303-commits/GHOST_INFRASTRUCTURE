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


st.markdown("<h1 style='text-align: center;'>🏛️ STUDY DESIGN</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center; color: #FFFFFF; font-size: 1.5rem;'>"
    "Why Bochum, Why 15-Minute Accessibility, Why This Question</h3>",
    unsafe_allow_html=True,
)
st.markdown("---")

st.markdown("""
<p style='color:#FFFFFF; font-weight:600; font-size:1.1rem; line-height:1.7;'>
The concept of "path dependency" — that historical spatial decisions continue to shape 
present-day urban outcomes long after their original rationale has disappeared — is a 
well-established idea in economic geography. This project makes it measurable, directly 
testing digitized historical industrial geography against a quantitative, network-based 
measure of present-day urban accessibility: the "15-minute city" framework.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>Study Area</h3>", unsafe_allow_html=True)

study_area_path = os.path.join(PROJECT_ROOT, "outputs", "plots", "study_area_bochum.png")
if os.path.exists(study_area_path):
    st.image(study_area_path, use_container_width=True)

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>Why Bochum</h3>", unsafe_allow_html=True)

render_card("""
    <p style="color:#111111; font-weight:700; font-size:1rem; line-height:1.7; margin:0;">
        Bochum was a small agricultural town until iron, coal, and steel industries developed 
        mid-19th century, becoming a defining Ruhr Valley industrial city through the 1950s. 
        The last coal mine in Bochum closed in 1973. Bochum is also directly relevant to this 
        research program's institutional context — home to Ruhr University Bochum.
    </p>
""")

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>The Research Question</h3>", unsafe_allow_html=True)

render_card("""
    <p style="color:#111111; font-weight:800; font-size:1.15rem; line-height:1.8; margin:0;">
        Does the historical geography of Ruhr Valley coal and steel industry infrastructure — 
        mine locations, worker-housing colonies, and industrial-era transportation networks — 
        continue to structurally predict which present-day neighborhoods fall inside or 
        outside a "15-minute" accessibility standard, decades after industrial decline?
    </p>
""")

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>Methodology at a Glance</h3>", unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)

with m1:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.85rem; text-transform:uppercase; margin:0 0 8px 0;">Step 1</p>
        <p style="color:#111111; font-weight:800; font-size:1rem; margin:0 0 8px 0;">Historical Digitization</p>
        <p style="color:#333333; font-weight:600; font-size:0.85rem; margin:0;">
            13 coal mines and 4 worker colonies compiled and georeferenced from Mindat.org and 
            German heritage archives.
        </p>
    """)

with m2:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.85rem; text-transform:uppercase; margin:0 0 8px 0;">Step 2</p>
        <p style="color:#111111; font-weight:800; font-size:1rem; margin:0 0 8px 0;">Network Accessibility</p>
        <p style="color:#333333; font-weight:600; font-size:0.85rem; margin:0;">
            69,393-node pedestrian street network built via OSMnx, tested against 786 essential 
            services using true network-distance isochrones.
        </p>
    """)

with m3:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.85rem; text-transform:uppercase; margin:0 0 8px 0;">Step 3</p>
        <p style="color:#111111; font-weight:800; font-size:1rem; margin:0 0 8px 0;">Statistical Testing</p>
        <p style="color:#333333; font-weight:600; font-size:0.85rem; margin:0;">
            Welch's t-test plus logistic regression, explicitly controlling for city-center 
            proximity as a confound.
        </p>
    """)

st.markdown("---")
st.markdown(
    "<p class='caption-text' style='text-align:center;'>GHOST INFRASTRUCTURE — Bochum, Ruhr Valley, Germany</p>",
    unsafe_allow_html=True,
)